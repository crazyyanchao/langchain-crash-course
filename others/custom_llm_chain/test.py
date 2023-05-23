from util.keys import initial

# 初始化秘钥配置
initial('../../.env')

from langchain.callbacks.stdout import StdOutCallbackHandler
from langchain.chat_models.openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate

from others.custom_llm_chain.custom_llm_chain import MyCustomChain

chain = MyCustomChain(
    prompt=PromptTemplate.from_template('tell us a joke about {topic}'),
    llm=ChatOpenAI()
)

chain.run({'topic': 'callbacks'}, callbacks=[StdOutCallbackHandler()])

