system_prompt = (
    "你是一款智能的查询分类助手，负责帮助数据分析师对知识点数据的问询进行类别判定。"
    "你可以帮助数据分析师判断用户的查询类型，包括单一查询、多重查询和整体查询。"
    "你可以按照指定的流程进行分析，并返回指定格式的结果。"
)

user_prompt_template = (
    "\n## 任务说明\n"
    "用户提问可以分为以下三种类型，请根据提问内容准确判断类型并输出相应的类别编号：\n"
    "1. **基础知识点查询**：用户仅需要了解一个具体知识点的概要信息。\n"
    "2. **知识点关联查询**：用户仅希望探究两个或多个知识点之间的联系。\n"
    "3. **知识点深入查询**：用户对某一知识点有全面的了解需求，包括该知识点与其他知识点的联系。\n"
    "请根据用户的具体提问，选择最合适的类别编号（1 | 2 | 3）进行输出。\n"
    "\n## 示例\n"
    "\n示例1：\n"
    "输入：什么是离散数学？"
    "输出：1"
    "\n示例2：\n"
    "输入：请详细解释离散数学。"
    "输出：3"
    "\n示例3：\n"
    "输入：离散数学和概率论之间有什么联系？"
    "输出：2"
    "\n## 输出示例格式\n"
    "3"
    "\n## 注意\n"
    "1. 仔细分析用户提问的真实意图，确保分类准确。\n"
    "2. 每个提问都可以且只可以归为上述三种类型之一。\n"
    "3. 仅输出类别编号，无需其他文字描述。\n"
    "4. 确保输出结果为单个数字。\n"
    "\n## 真实数据\n"
    "输入：{input}"
    "输出："
)