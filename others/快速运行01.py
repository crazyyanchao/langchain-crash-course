from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain.chat_models import PromptLayerChatOpenAI
from langchain.schema import HumanMessage

llm = PromptLayerChatOpenAI(pl_tags=["langchain"],temperature=0)

tools = load_tools(["llm-math", "serpapi"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("易方达基金的总经理是谁他今年的年龄是多少他年龄的0.76次方是多少？")



