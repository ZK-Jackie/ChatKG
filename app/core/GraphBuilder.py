import os
import re
import json
import warnings
import time
from itertools import islice
from typing import List
from tqdm import tqdm
from langchain_core.prompts import PromptTemplate
from app.core.MarkdownReader import MarkdownReader
from app.core.GraphNeo4j import GraphNeo4j
from app.core.InfoTree import InfoForest
from zhipuai import ZhipuAI



default_prompt_template = (
    "请你对知识文本执行知识提取任务。\n"
    "请根据提供的多级标题和文本内容，执行以下知识提取任务：\n"
    "1. 综合多个等级的标题，从标题中提取出知识实体，知识实体是一个知识名词。\n"
    "2. 从**文本内容**中找出这些知识实体的属性名及属性，忽略**文本内容**中的例题、分析、答案。\n"
    "3. 找出多个实体之间的指向和关系。\n"
    "4. 将提取的内容以JSON字符串格式输出。\n\n"
    "## 输入内容\n"
    "{insertion}"
    "## 输出格式\n"
    "输出应为一个JSON字符串，包含以下结构：\n"
    "- **知识实体**：包含知识实体及其属性。\n"
    "- **实体关系**：描述实体之间的关系。\n"
    "## 输出示例\n"
    "```json{output_format}```"
)

default_insertion_template = (
    "**{level_name}**：\n"
    "```markdown\n"
    "{level_content}\n"
    "```\n\n"
)

default_level_names = ["书籍名称", "一级标题", "二级标题", "三级标题", "四级标题", "五级标题", "六级标题", "七级标题",
                       "八级标题"]
default_content_names = "文本内容"

default_output_format = """
    {
      "知识实体": {
        "实体1": {
          "属性": {
            "属性1": "...",
            "属性2": "...",
            ...
          }
        },
        "实体2": {
          ...
        }
      },
      "实体关系": {
        "实体1": {
          "关系1": ["实体2", "实体3"]
        },
        "实体2": {
          "关系2": [...]
        },
      }
    }
    """


class GraphBuilder:
    file: str | List[str] | None

    engine: str
    prompt_template: str
    insertion_template: str

    doc_trees: InfoForest | None = None

    _allowed_engines = ["graphrag", "tradition"]

    def __init__(self,
                 file: str | List[str] | None,
                 engine: str,
                 prompt_template: str = default_prompt_template,
                 insertion_template: str = default_insertion_template):
        self.file = file
        self.engine = engine
        self.prompt_template = prompt_template
        self.insertion_template = insertion_template

    @property
    def engine(self) -> str:
        return self._engine

    @engine.setter
    def engine(self, new_val: str):
        if new_val not in self._allowed_engines:
            raise ValueError(f"Value must be one of {self._allowed_engines}")
        self._engine = new_val

    def get_doc_trees(self, **engine_kwargs):
        if self.doc_trees is None:
            self.doc_trees = MarkdownReader(file=self.file, **engine_kwargs).indexing()
        return self.doc_trees

    def build(self, **engine_kwargs):
        # 0. 数据初始化
        res: List[dict] | None = None
        if self.engine == "graphrag":
            res = self._graphrag_engine(engine_kwargs)
        elif self.engine == "tradition":
            res = self._tradition_engine(engine_kwargs)
        return res

    def _tradition_engine(self, kwargs):
        # 0. 数据预处理
        info = MarkdownReader(file=self.file, **kwargs).indexing()
        # 1. 构建insertions
        insertions = []
        # 遍历每一章节
        for tree in tqdm(info, desc="Building insertions"):
            # 遍历每一节点
            for node_title_list, node_content in tree:
                if not node_content:
                    continue
                # 构建多个insertion
                temp_insertions = ""
                # 遍历每一级标题
                for i, title in enumerate(node_title_list):
                    temp_insertions += self.insertion_template.format(level_name=default_level_names[i],
                                                                      level_content=title)
                # 添加文本内容

                temp_insertions += self.insertion_template.format(level_name=default_content_names,
                                                                  level_content=node_content)
                # 添加到insertions
                insertions.append(temp_insertions)
        # 2. 构建prompt
        prompts = []
        for insertion in tqdm(insertions, desc="Building prompts"):
            prompts.append(
                PromptTemplate
                .from_template(self.prompt_template)
                .invoke({"insertion": insertion, "output_format": default_output_format})
                .to_string()
            )
        # 3. 调用引擎，构建知识图谱
        tasks = []
        client: ZhipuAI = kwargs.get("llm")     # 从llm参数中获取client，当前这里是智谱AI，后续再做拓展
        for prompt in prompts:
            # temp_response = kwargs.get("llm").chat.completions.create(
            #     model=kwargs.get("model"),
            #     messages=[
            #         {"role": "user", "content": prompt},
            #     ]
            # ).choices[0].message
            # json_obj = self._json_parse(temp_response)
            # responses.append(json_obj)
            temp_response = client.chat.asyncCompletions.create(
                model=kwargs.get("model"),
                messages=[
                    {"role": "user", "content": prompt},
                ]
            )
            tasks.append({
                "task_content": prompt,
                "task_id": temp_response.id
            })

        # 等待所有任务完成
        responses = []
        try:
            for task in tqdm(tasks, desc="Waiting for completions"):
                temp_response = None
                temp_task_status = "PROCESSING"
                while temp_task_status != "SUCCESS":
                    if temp_task_status == "FAILED":
                        warnings.warn(f"Task {task} failed!")
                        temp_response = {
                            "choices": [
                                {
                                    "message": {
                                        "content": "Task failed!"
                                    }
                                }
                            ]
                        }
                        break
                    time.sleep(2)   # 每2秒查询一次
                    temp_response = client.chat.asyncCompletions.retrieve_completion_result(id=task["task_id"])
                    temp_task_status = temp_response.task_status
                # 解析 llm 的回答为 json
                dict_result = self._json_parse(temp_response.choices[0].message.content)
                responses.append({
                    "task_id": task["task_id"],
                    "task_content": task["task_content"],
                    "task_result": dict_result
                })
                # 将 llm 的回答创建/追加写入一个文件内
                with open("temp_responses.json", "a", encoding="utf-8") as f:
                    json.dump("\n", f)
                    json.dump(responses[-1], f, separators=(',', ':'), ensure_ascii=False)
        except Exception as ex:
            # 紧急保存responses
            timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
            with open(f"exception_responses-{timestamp}.json", "w", encoding="utf-8") as f:
                json.dump(responses, f, indent=2, ensure_ascii=False)
            raise ex
        # 4. 最终转化
        final_res = []
        for response in responses:
            final_res.append(response["task_result"])
        return responses

    def _json_parse(self, raw_str: str):
        try:
            # 把 json 字符串转换为字典
            out = json.loads(raw_str)
        except Exception as e1:
            # 若生成markdown代码块字符串，需要从代码块中提取json字符串
            try:
                out = json.loads(raw_str.split("```")[1])
            except Exception as e2:
                try:
                    out = self._extract_json_code_block(raw_str)
                except Exception as e3:
                    out = {
                        "raw": raw_str
                    }
                    warnings.warn(f"Failed to parse json: {raw_str}")
        return out

    def _extract_json_code_block(self, raw_str: str):
        # Regular expression to match ```json ... ```
        pattern = re.compile(r'```json\s*(.*?)\s*```', re.DOTALL)
        # Find all matches
        matches = pattern.findall(raw_str)
        return json.loads(matches[0])

    def _graphrag_engine(self, kwargs):
        pass


if __name__ == "__main__":
    """
    GraphBuilder类将会是用户使用本程序的核心类之一，用户将会通过这个类来构建知识图谱。
    下文在演示怎么用这个类来构建知识图谱。
    这个类还在不断完善开发，后续会将每个组件拆分到其他文件中，以便于维护。
    """
    # from dotenv import load_dotenv
    #
    # load_dotenv()
    #
    # zhipu_client = ZhipuAI(api_key=os.getenv("ZHIPU_API_KEY"))
    # result = (GraphBuilder(file="ch1.md",
    #                        engine="tradition")
    #           .build(skip_mark="<abd>",
    #                  llm=zhipu_client,
    #                  model="glm-4-0520"))
    # json.dump(result, open("result.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    forest = GraphBuilder(file="ch1.md", engine="tradition").get_doc_trees(skip_mark="<abd>")
    result = json.load(open("result.json", "r", encoding="utf-8"))
    # 同时遍历两个对象，一一填充对应
    for tree in forest.trees:
        for node, res in zip(islice(tree, 1, None), result):
            if node.content:
                node.struct_info = res["task_result"]
    # 将每个节点组织成cypher语句即将被调用的对象
    cqls = []
    for tree in forest.trees:
        for node in tree:
            if node.content:
                cqls.extend(node.to_cypher_obj())
    print(cqls)
    # 插入到neo4j数据库中
    graph = GraphNeo4j()

