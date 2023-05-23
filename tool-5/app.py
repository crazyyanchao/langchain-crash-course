from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.chat_models import ChatOpenAI
from langchain.chat_models import PromptLayerChatOpenAI

# from langchain.chains import GraphCypherQAChain
from cypher import GraphCypherQAChain

# from langchain.graphs import Neo4jGraph
from neo4j_graph import Neo4jGraph

# pip install neo4j-driver==1.7.6
# neo4j-3.5.22
graph = Neo4jGraph(
    url="bolt://localhost:7687", username="neo4j", password="123456"
)

# pip install neo4j-driver==5.8.0
# neo4j-5.8.0
# graph = Neo4jGraph(
#     url="neo4j+s://c33fb403.databases.neo4j.io", username="neo4j", password="_GHXOEmNyysoATp2yR6wxXDgpBrg9x2VSXyyWcUHNiI"
# )

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

# 不跟踪调用记录
# chain = GraphCypherQAChain.from_llm(
#     ChatOpenAI(temperature=0), graph=graph, verbose=True
# )

# 跟踪调用记录
chain = GraphCypherQAChain.from_llm(
    PromptLayerChatOpenAI(pl_tags=["neo4j"], temperature=0), graph=graph, verbose=True
)

output = chain.run("Who played in Top Gun?")
# output = chain.run("Have Meg Ryan and Val Kilmer acted in the movie Top Gun?")

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
# Tom Cruise and Anthony Edwards played in Top Gun.


# Tom Cruise, Val Kilmer, Anthony Edwards, and Meg Ryan played in Top Gun.

