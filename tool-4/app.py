import sys

sys.path.append('.')

from util.keys import initial

# 初始化秘钥配置
# initial('.env')
initial()

from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory


template = """Assistant是OpenAI训练的一个大型语言模型。

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

{history}
Human: {human_input}
Assistant:"""

prompt = PromptTemplate(
    input_variables=["history", "human_input"],
    template=template
)


chatgpt_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=prompt,
    verbose=True,
    memory=ConversationBufferWindowMemory(k=2),
)

output = chatgpt_chain.predict(human_input="姚明的妻子是谁？")
print(output)

output = chatgpt_chain.predict(human_input="她的年龄是多少？")
print(output)

output = chatgpt_chain.predict(human_input="他曾在哪里工作？")
print(output)


# > Entering new LLMChain chain...
# Prompt after formatting:
# Assistant是OpenAI训练的一个大型语言模型。
#
# Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.
#
# Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.
#
# Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.
#
#
# Human: 姚明的妻子是谁？
# Assistant:
#
# > Finished chain.
#  姚明的妻子是张雪静，他们于2007年结婚，并于2010年生下一个女儿。
#
#
# > Entering new LLMChain chain...
# Prompt after formatting:
# Assistant是OpenAI训练的一个大型语言模型。
#
# Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.
#
# Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.
#
# Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.
#
# Human: 姚明的妻子是谁？
# AI:  姚明的妻子是张雪静，他们于2007年结婚，并于2010年生下一个女儿。
# Human: 她的年龄是多少？
# Assistant:
#
# > Finished chain.
#  张雪静的年龄是37岁，出生于1983年。
#
#
# > Entering new LLMChain chain...
# Prompt after formatting:
# Assistant是OpenAI训练的一个大型语言模型。
#
# Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.
#
# Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.
#
# Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.
#
# Human: 姚明的妻子是谁？
# AI:  姚明的妻子是张雪静，他们于2007年结婚，并于2010年生下一个女儿。
# Human: 她的年龄是多少？
# AI:  张雪静的年龄是37岁，出生于1983年。
# Human: 他曾在哪里工作？
# Assistant:
#
# > Finished chain.
#  姚明曾在NBA的多个球队担任过球员，包括火箭队、湖人队和灰熊队。他还曾在中国篮球联赛的上海男篮担任过总经理。

