from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

# tools = load_tools(["serpapi", "llm-math"], llm=llm)
tools = load_tools(["llm-math", "serpapi"], llm=llm)

# llm = OpenAI(openai_api_key=getEnv('OPENAI_KEY'),temperature=0)

# tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")


# > Entering new AgentExecutor chain...
#  I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to the 0.43 power.
# Action: Search
# Action Input: "Leo DiCaprio girlfriend"
# Observation: He went on to date Gisele Bündchen, Bar Refaeli, Blake Lively, Toni Garrn and Nina Agdal, among others, before finally settling down with current girlfriend Camila Morrone, who is 23 years his junior.
# Thought: I need to calculate Camila Morrone's age raised to the 0.43 power.
# Action: Calculator
# Action Input: 23^0.43
# Observation: Answer: 3.8507291225496925
# Thought: I now know the final answer.
# Final Answer: Camila Morrone's age raised to the 0.43 power is 3.8507291225496925.
#
# > Finished chain.

