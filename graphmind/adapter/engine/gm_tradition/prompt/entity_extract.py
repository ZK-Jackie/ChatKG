system_prompt = (
    "你是一个专业的知识提取助手，你的任务是准确无误地从提供的文本区域中提取关键信息。"
    "关键信息包括概念、定义、定理、性质、原理和算法等客观知识。"
    "请忽略所有非关键细节，如公式字母、示例、主观意见和辅助解释。"
    "你的输出应该严格遵循要求，并确保输出信息的准确性和结构化。"
)

user_prompt_template = (
    "## 任务\n"
    "根据工作流程，从输入内容中提取概念性名词和与知识相关的名词，以及它们的属性。忽略公式字母、辅助例子和其他无关内容。\n"
    "## 工作流程\n"
    "步骤1：从多级标题中提取包含离散数学的一个或多个知识名词作为实体。\n"
    "步骤2：对于步骤1提取的每个实体，从正文文本中提取出其定义、应用、特点、条件或结论等其他内容作为属性。\n"
    "步骤3：对每个实体进行分类，确保每个实体与“概念、定理、性质、原理、算法”中的一个实体类型相对应。\n"
    "## 注意\n"
    "- 忽略数学公式中的字母，如变量、常数等。\n"
    "- 忽略用于解释或辅助理解的例子。\n"
    "- 忽略文本中的标点符号和数字。\n"
    "- 不能以完整的标题名字作为实体。\n"
    "- 输出示例中，带有“[]”的文本应当被替换为实际内容。\n\n"
    "## 输出示例\n"
    "{output_example}"
    "## 输入内容\n"
    "{insertion}"
    "## 输出格式\n"
    "{output_format}"
)

prompt_insertion_template = (
    "{level_name}：\n"
    "```\n"
    "{level_content}\n"
    "```\n\n"
)

prompt_output_format = """
{"[实体1名称]": {"实体类型": "[实体类型]", "[属性名1]": "[属性值1]","[属性名2]": "[属性值2]",...},
 "[实体2名称]": {"实体类型": "[实体类型]","[属性名1]": "[属性值1]",...},
 ...}
"""

user_output_example = """
{"离散数学": {"实体类型": "概念","定义": "研究离散量的数学学科","应用": "支撑计算机科学的发展",...},
 "数理逻辑": {"实体类型": "原理","地位": "是离散数学的重要分支","特点": "基于逻辑推及规则，研究命题、谓词、推理等"},
 ...}
"""

text_level_names = ["书籍名称", "一级标题", "二级标题", "三级标题", "四级标题", "五级标题", "六级标题", "七级标题", "八级标题"]

text_content_name = "文本内容"