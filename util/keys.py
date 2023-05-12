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
