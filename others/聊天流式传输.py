from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI, ChatAnthropic
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage

llm = OpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
resp = llm("Write me a song about sparkling water.")

# llm.generate(["Tell me a joke."])

# chat = ChatOpenAI(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
# resp = chat([HumanMessage(content="Write me a song about sparkling water.")])

# chat = ChatAnthropic(streaming=True, callbacks=[StreamingStdOutCallbackHandler()], temperature=0)
# resp = chat([HumanMessage(content="Write me a song about sparkling water.")])

