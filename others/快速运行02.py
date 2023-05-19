from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import PromptLayerChatOpenAI

llm = PromptLayerChatOpenAI(temperature=0)

tools = load_tools(["serpapi"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("易方达基金的总经理是谁？他今年的年龄是多少？")



