# https://promptlayer.com/home
from util.keys import initial

# 初始化秘钥配置
initial()

from langchain.chat_models import PromptLayerChatOpenAI
from langchain.schema import HumanMessage

chat = PromptLayerChatOpenAI(pl_tags=["langchain"])
chat([HumanMessage(content="I am a cat and I want")])




