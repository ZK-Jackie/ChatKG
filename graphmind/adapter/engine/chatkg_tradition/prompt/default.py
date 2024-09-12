default_system_prompt = (
    "你是一个知识提取助手，你的任务是分析用户提供的文本，并从中提取关键信息。"
    "在提取信息时，请专注于事实、数据点和关键概念。"
    "忽略非关键细节和主观意见。"
    "请以要求的格式提供提取出的知识点。"
)

default_prompt_template = (
    "请根据提供的多级标题和文本内容，执行以下知识提取任务：\n"
    "1. 综合多个等级的标题，从标题中提取出一个或多个知识实体，每个知识实体都是一个知识名词。\n"
    "2. 从**文本内容**中找出这些知识实体的属性名及属性，忽略**文本内容**中的例题、分析、答案。\n"
    "3. 从标题之间、标题与正文之间、正文之间找出或总结出提取的实体之间的关系词。\n"
    "4. 将提取的内容以JSON字符串格式输出。\n\n"
    "## 输入内容\n"
    "{insertion}"
    "## 输出格式\n"
    "输出应为一个JSON字符串，包含以下结构：\n"
    "- **知识实体**：从标题中提取出，包含知识实体及其属性。\n"
    "- **实体关系**：从**文本内容**中提取出，描述知识实体之间的关系。\n"
    "## 输出示例\n"
    "```json{output_format}```"
)

default_insertion_template = (
    "**{level_name}**：\n"
    "```markdown\n"
    "{level_content}\n"
    "```\n\n"
)

default_level_names = ["书籍名称", "一级标题", "二级标题", "三级标题", "四级标题",
                       "五级标题", "六级标题", "七级标题", "八级标题"]
default_content_name = "文本内容"

default_output_format = """
    {
      "知识实体": {
        "实体1": {
          "属性1": "...",
          "属性2": "......",
          ...
        },
        "实体2": {
          ...
        }
      },
      "实体关系": {
        "实体1": {
          "关系词1": ["实体2", "实体3"],
          "关系词2": ["实体4"],
          ...
        },
        "实体2": {
          "关系词1": [...],
          ...
        },
      }
    }
"""