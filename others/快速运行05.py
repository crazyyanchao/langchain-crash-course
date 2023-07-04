from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.chat_models import ChatOpenAI, PromptLayerChatOpenAI
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
from langchain import SerpAPIWrapper
from langchain.agents.tools import Tool
from langchain import LLMMathChain

search = SerpAPIWrapper()
llm = PromptLayerChatOpenAI(temperature=0, pl_tags=["agent_planner_executor-LLMMathChain"])
llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events"
    ),
    Tool(
        name="Calculator",
        func=llm_math_chain.run,
        description="useful for when you need to answer questions about math"
    ),
]

model = PromptLayerChatOpenAI(temperature=0, pl_tags=["agent_planner_executor"])

planner = load_chat_planner(model)

executor = load_agent_executor(model, tools, verbose=True)

agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

response = agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")


print("response:" + response)
