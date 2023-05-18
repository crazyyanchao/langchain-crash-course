import sys

sys.path.append('.')

from util.keys import initial

# 初始化秘钥配置
# initial('.env')
initial()

from langchain.llms import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.utilities.zapier import ZapierNLAWrapper

llm = OpenAI(temperature=.3)
zapier = ZapierNLAWrapper()
toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
agent = initialize_agent(toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 我们可以通过打印的方式看到我们都在 Zapier 里面配置了哪些可以用的工具
for tool in toolkit.get_tools():
    print(tool.name)
    print(tool.description)
    print("\n\n")

agent.run('请用中文总结最后一封"xxx@google.com"发给我的邮件。并将总结发送给"xxx@qq.com"')


# Gmail: Find Email
# A wrapper around Zapier NLA actions. The input to this tool is a natural language instruction, for example "get the latest email from my bank" or "send a slack message to the #general channel". Each tool will have params associated with it that are specified as a list. You MUST take into account the params when creating the instruction. For example, if the params are ['Message_Text', 'Channel'], your instruction should be something like 'send a slack message to the #general channel with the text hello world'. Another example: if the params are ['Calendar', 'Search_Term'], your instruction should be something like 'find the meeting in my personal calendar at 3pm'. Do not make up params, they will be explicitly specified in the tool description. If you do not have enough information to fill in the params, just say 'not enough information provided in the instruction, missing <param>'. If you get a none or null response, STOP EXECUTION, do not try to another tool!This tool specifically used for: Gmail: Find Email, and has params: ['Search_String']
# 
# 
# 
# Gmail: Send Email
# A wrapper around Zapier NLA actions. The input to this tool is a natural language instruction, for example "get the latest email from my bank" or "send a slack message to the #general channel". Each tool will have params associated with it that are specified as a list. You MUST take into account the params when creating the instruction. For example, if the params are ['Message_Text', 'Channel'], your instruction should be something like 'send a slack message to the #general channel with the text hello world'. Another example: if the params are ['Calendar', 'Search_Term'], your instruction should be something like 'find the meeting in my personal calendar at 3pm'. Do not make up params, they will be explicitly specified in the tool description. If you do not have enough information to fill in the params, just say 'not enough information provided in the instruction, missing <param>'. If you get a none or null response, STOP EXECUTION, do not try to another tool!This tool specifically used for: Gmail: Send Email, and has params: ['Body', 'To', 'Subject', 'Cc']
# 
# 
# 
# 
# 
# > Entering new AgentExecutor chain...
#  I need to find the latest email from xxx@google.com and summarize it in Chinese
# Action: Gmail: Find Email
# Action Input: Find the latest email from xxx@google.com
# Observation: {"from__email": "xxx@google.com", "body_plain": "Welcome to Bard! Your creative and helpful collaborator here to supercharge your imagination, boost productivity and bring your ideas to life. Try it now: https://bard.google.com. As an early experiment, it won't always get it right, but with your help and feedback, it'll get better every day. For info on how Google will use your info and interactions with Bard, see our FAQ page: https://bard.google.com/faq. Thanks for being an early experimenter! Google LLC 1600 Amphitheatre Parkway, Mountain View, CA 94043. This message sent to you because you signed up to use Bard. Available in select markets and languages.", "from__name": "Bard, an AI experiment by Google", "subject": "Get started with Bard", "message_url": "https://mail.google.com/mail/u/0/#inbox/18808835749dbbcf", "date": "Wed, 10 May 2023 18:53:24 -0700", "to__emails": "CrazyYanChao@gmail.com", "attachment_count": "0"}
# Thought: I need to summarize the email in Chinese
# Action: None
# Action Input: None
# Observation: None is not a valid tool, try another one.
# Thought: I need to send the summary to xxx@qq.com
# Action: Gmail: Send Email
# Action Input: Send an email to xxx@qq.com with the subject "Summary of Bard Email" and the body "欢迎使用Bard！Bard是一个可以提高创造力、提高效率、实现想法的有用合作者。立即尝试：https：//bard.google.com。作为一个早期的实验，它不会总是正确的，但是有了您的帮助和反馈，它每天都会变得更好。有关Google如何使用您的信息和与Bard的互动，
# Observation: {"threadId": "1882d495df27a3b3", "labelIds": "SENT"}
# Thought: I now know the final answer
# Final Answer: 已将总结发送给xxx@qq.com
# 
# > Finished chain.
