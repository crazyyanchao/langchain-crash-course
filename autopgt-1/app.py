import sys

sys.path.append('.')

from util.keys import initial

# 初始化秘钥配置
initial('.env')

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain import SerpAPIWrapper

# App 框架
st.title('🦜🔗 短视频脚本创作 (゜-゜)つロ~')
prompt = st.text_input('请输入你的提示信息')

# 提示模板
title_template = PromptTemplate(
    input_variables=['topic'],
    template='给我用中文写一个关于 {topic} 的视频标题。'
)

script_template = PromptTemplate(
    input_variables=['title', 'serapi_search'],
    template='根据这个标题：{title}，给我用中文写一个视频脚本，同时结合Google的搜索结果：{serapi_search}。'
)

# 会话历史
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# 设置大模型工具
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

serapi = SerpAPIWrapper(params={'engine': 'google'})

# 如果有提示，将内容显示到屏幕上
if prompt:
    title = title_chain.run(prompt)
    serapi_search = serapi.run(prompt)
    script = script_chain.run(title=title, serapi_search=serapi_search)

    st.write(title)
    st.write(script)

    with st.expander('标题'):
        st.info(title_memory.buffer)

    with st.expander('脚本'):
        st.info(script_memory.buffer)

    with st.expander('Google 搜索结果'):
        st.info(serapi_search)
