from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003", max_tokens=1024)
print(llm("怎么评价人工智能"))
