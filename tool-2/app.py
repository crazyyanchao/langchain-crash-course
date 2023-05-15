import sys

sys.path.append('.')

from util.keys import initial

# 初始化秘钥配置
initial('.env')

import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect

    Here are some examples different Tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell you.
    - Informal: Went to Barcelona for the weekend. Lots to tell you.  

    Here are some examples of words in different dialects:
    - American: French Fries, cotton candy, apartment, garbage, cookie, green thumb, parking lot, pants, windshield
    - British: chips, candyfloss, flag, rubbish, biscuit, green fingers, car park, trousers, windscreen

    Example Sentences from each dialect:
    - American: I headed straight for the produce section to grab some fresh vegetables, like bell peppers and zucchini. After that, I made my way to the meat department to pick up some chicken breasts.
    - British: Well, I popped down to the local shop just the other day to pick up a few bits and bobs. As I was perusing the aisles, I noticed that they were fresh out of biscuits, which was a bit of a disappointment, as I do love a good cuppa with a biscuit or two.

    Please start the email with a warm introduction. Add the introduction if you need to. And please reply the final response in Simplified Chinese and attach at the end.

    Below is the email, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}

    YOUR {dialect} RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template,
)


def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm


st.set_page_config(page_title="邮件助手", page_icon=":robot:")
st.header("邮件助手")

col1, col2 = st.columns(2)

with col1:
    st.markdown("办公室白领经常想要改善他们发送电子邮件的技巧，但缺少这样做的技能。 \n\n 这个工具 \
                将帮助你提高你的电子邮件技巧，把你的电子邮件转换成更专业的格式。 该工具 \
                由 [LangChain](https://langchain.com/) 和 [OpenAI](https://openai.com) 提供支持。参考于这个项目 \
                [globalize-text-streamlit](https://github.com/gkamradt/globalize-text-streamlit). \n\n 在这里查看源码 [Github](https://github.com/crazyyanchao/langchain-crash-course/tree/main/tool-2)")

with col2:
    st.image(image='tool-2/TweetScreenshot.png', width=500,
             caption='https://twitter.com/DannyRichman/status/1598254671591723008')

st.markdown("## 输入您需要转换的电子邮件")


def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ", placeholder="Ex: sk-2twmA8tfCb8un4...",
                               key="openai_api_key_input")
    return input_text


openai_api_key = get_api_key()

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        'Which tone would you like your email to have?',
        ('Formal', 'Informal'))

with col2:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ('American', 'British'))


def get_text():
    # input_text = st.text_area(label="Email Input", label_visibility='Collapsed', placeholder="Your Email...",
    #                           key="email_input")
    input_text = st.text_area(label="Email Input", placeholder="Your Email...",
                              key="email_input")
    return input_text


email_input = get_text()

if len(email_input.split(" ")) > 700:
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()


def update_text_with_example():
    print("in updated")
    st.session_state.email_input = "Sally I am starts work at yours monday from dave"

# Sally I am starts work at yours monday from dave
# 莎莉，我星期一从戴夫那里开始上班

# st.button("*See An Example*", type='secondary', help="Click to see an example of the email you will be converting.",
#           on_click=update_text_with_example)

st.button("参见示例", help="单击查看要转换的电子邮件示例。",
          on_click=update_text_with_example)

st.markdown("### 转换的电子邮件:")

if email_input:
    if not openai_api_key:
        st.warning(
            'Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)')
        st.stop()

    llm = load_LLM(openai_api_key=openai_api_key)

    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)

    formatted_email = llm(prompt_with_email)

    st.write(formatted_email)

