from util.keys import initial

# 初始化秘钥配置
initial()

from langchain import PromptTemplate, HuggingFaceHub, LLMChain

template = """Question: {question}
Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature": 0, "max_length": 64})
llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
print(llm_chain.run(question))

# import requests
#
# API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xl"
# headers = {"Authorization": "Bearer xxx"}
#
#
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()
#
#
# output = query({
#     "inputs": "The answer to the universe is",
# })

