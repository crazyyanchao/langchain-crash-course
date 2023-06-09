import os

from util.env import getEnv


# 初始化秘钥配置
def initial(env='../.env'):
    # OPENAI 模型接口调用秘钥 https://openai.com
    os.environ['OPENAI_API_KEY'] = getEnv('OPENAI_KEY', env)

    # SERPAPI 搜索工具秘钥 https://serpapi.com
    os.environ['SERPAPI_API_KEY'] = getEnv('SERPAPI_KEY', env)

    # OPENAI 接口用量记录工具秘钥 https://promptlayer.com
    os.environ["PROMPTLAYER_API_KEY"] = getEnv('PROMPTLAYER_KEY', env)

    # Natural Language Actions: https://nla.zapier.com/get-started/
    os.environ["ZAPIER_NLA_API_KEY"] = getEnv('ZAPIER_NLA_KEY', env)

    # HuggingFace: https://huggingface.co/settings/tokens
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = getEnv('HUGGINGFACEHUB_TOKEN', env)

    os.environ["CHATGLM_API"] = getEnv('CHATGLM_API', env)
    os.environ["MOSS_API"] = getEnv('MOSS_API', env)
    os.environ["NEO4J_URL"] = getEnv('NEO4J_URL', env)
    os.environ["NEO4J_USER"] = getEnv('NEO4J_USER', env)
    os.environ["NEO4J_PWD"] = getEnv('NEO4J_PWD', env)
