import os

from util.keys import initial

# 初始化秘钥配置
initial()

from custom_moss import MossLLM
from custom_chatglm import ChatGLMLLM
from langchain.chat_models import PromptLayerChatOpenAI
from cypher import GraphCypherQAChain
from neo4j_graph import Neo4jGraph
from langchain.chains.llm import LLMChain
from langchain.chains.graph_qa.prompts import PROMPT

graph = Neo4jGraph(
    url=os.environ.get("NEO4J_URL"),
    username=os.environ.get("NEO4J_USER"),
    password=os.environ.get("NEO4J_PWD")
)

# 创建一些样例数据
graph.query(
    """
MERGE (m:Movie {name:"Top Gun"})
WITH m
UNWIND ["Tom Cruise", "Val Kilmer", "Anthony Edwards", "Meg Ryan"] AS actor
MERGE (a:Actor {name:actor})
MERGE (a)-[:ACTED_IN]->(m)
"""
)

# 刷新图模式信息
graph.refresh_schema()

print(graph.get_schema)

# 跟踪调用记录
llm = PromptLayerChatOpenAI(pl_tags=["neo4j"], temperature=0)

# 使用自定义的QA_CHAIN
# qa_llm = MossLLM(temperature=0.001)
qa_llm = ChatGLMLLM(temperature=0.001)

chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, qa_chain=LLMChain(llm=qa_llm, prompt=PROMPT), verbose=True
)

output = chain.run("Who played in Top Gun?")

print(output)

#         Node properties are the following:
#         [{'properties': [{'property': 'name', 'type': 'STRING'}], 'labels': 'Movie'}, {'properties': [{'property': 'name', 'type': 'STRING'}], 'labels': 'Actor'}]
#         Relationship properties are the following:
#         []
#         The relationships are the following:
#         ['(:Actor)-[:ACTED_IN]->(:Movie)']
#
#
#
# > Entering new GraphCypherQAChain chain...
# Generated Cypher:
# MATCH (a:Actor)-[:ACTED_IN]->(m:Movie {name: 'Top Gun'})
# RETURN a.name
# Full Context:
# [{'a.name': 'Meg Ryan'}, {'a.name': 'Val Kilmer'}, {'a.name': 'Tom Cruise'}, {'a.name': 'Anthony Edwards'}]
#
# > Finished chain.
# Tom Cruise, Val Kilmer, and Meg Ryan all played characters in the film Topgun.
