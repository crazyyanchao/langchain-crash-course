from util.keys import initial

# ===========================初始化秘钥配置===========================
initial()

import os
from langchain import PromptTemplate
from custom_moss import MossLLM
from custom_chatglm import ChatGLMLLM
from langchain.chat_models import PromptLayerChatOpenAI
from cypher import GraphCypherQAChain
from neo4j_graph import Neo4jGraph
from langchain.chains.llm import LLMChain
from langchain.chains.graph_qa.prompts import PROMPT
from example_selector import ExampleSelector

# ===========================初始化图数据库连接对象===========================
graph = Neo4jGraph(
    url=os.environ.get("NEO4J_URL"),
    username=os.environ.get("NEO4J_USER"),
    password=os.environ.get("NEO4J_PWD")
)

# ===========================创建一些样例数据===========================
graph.query(
    """
MERGE (m:Movie {name:"Top Gun"})
WITH m
UNWIND ["Tom Cruise", "Val Kilmer", "Anthony Edwards", "Meg Ryan"] AS actor
MERGE (a:Actor {name:actor})
MERGE (a)-[:ACTED_IN]->(m)
"""
)

# ===========================跟踪调用记录===========================
llm = PromptLayerChatOpenAI(pl_tags=["neo4j"], temperature=0)

# ===========================使用自定义的QA_CHAIN===========================
# qa_llm = MossLLM(temperature=0.001)
qa_llm = ChatGLMLLM(temperature=0.001)

# ===========================定义CYPHER_PROMPT===========================
examples = """
# Who played in Top Gun?
MATCH (a:Actor)-[:ACTED_IN]->(m:Movie {name: 'Top Gun'})
RETURN a.name AS result;
"""

qa = "Who played in Top Gun?"

# graph.set_schema(examples)
# 设置样例Cypher：进行动态向量计算获取examples
similar_prompt = ExampleSelector()
graph.set_schema(similar_prompt.get_examples(qa))

CYPHER_GENERATION_TEMPLATE = """
You are an assistant with an ability to generate Cypher queries based off example Cypher queries.
Example Cypher queries are:\n{schema}\n
Do not response with any explanation or any other information except the Cypher query.
You do not ever apologize and strictly generate cypher statements based of the provided Cypher examples.
Do not provide any Cypher statements that can't be inferred from Cypher examples.
Inform the user when you can't infer the cypher statement due to the lack of context of the conversation and state what is the missing context.

The question is:
{question}"""

CYPHER_GENERATION_PROMPT = PromptTemplate(
    input_variables=["schema", "question"], template=CYPHER_GENERATION_TEMPLATE
)

# ===========================执行Chains===========================
chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, qa_chain=LLMChain(llm=qa_llm, prompt=PROMPT),
    cypher_prompt=CYPHER_GENERATION_PROMPT, verbose=True
)

output = chain.run(qa)

print(output)

# > Entering new GraphCypherQAChain chain...
# Generated Cypher:
# MATCH (a:Actor)-[:ACTED_IN]->(m:Movie {name: 'Top Gun'})
# RETURN a.name AS result;
# Full Context:
# [{'result': 'Meg Ryan'}, {'result': 'Val Kilmer'}, {'result': 'Tom Cruise'}, {'result': 'Anthony Edwards'}]
#
# > Finished chain.
# Tom Cruise, Val Kilmer, and Meg Ryan all played characters in the film Topgun.
