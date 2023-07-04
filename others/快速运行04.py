import asyncio
import time
from typing import List, Tuple, Any, Union
from langchain.schema import AgentAction, AgentFinish
from langchain.agents import Tool, AgentExecutor, BaseMultiActionAgent, AgentType, initialize_agent, load_tools
from langchain import OpenAI, SerpAPIWrapper
# from src.hack.config import openai_api_key, serper_api_key
import os

from util.keys import initial

# 初始化秘钥配置
initial()

questions = [
    "Who won the US Open men's final in 2019? What is his age raised to the 0.334 power?",
    "Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?",
    "Who won the most recent formula 1 grand prix? What is their age raised to the 0.23 power?",
    "Who won the US Open women's final in 2019? What is her age raised to the 0.34 power?",
    "Who is Beyonce's husband? What is his age raised to the 0.19 power?"
]


async def task_run(questions):
    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    s = time.perf_counter()
    # If running this outside of Jupyter, use asyncio.run or loop.run_until_complete
    tasks = [agent.arun(q) for q in questions]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - s
    print(f"Concurrent executed in {elapsed:0.2f} seconds.")


loop = asyncio.get_event_loop()
loop.run_until_complete(task_run(questions))
# print('再看下运行情况：', task_run)
loop.close()
