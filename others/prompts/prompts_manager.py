import datetime
import os
from typing import List

from util.keys import initial

# 初始化秘钥配置
initial('../../.env')

import requests


def publish_prompt_template(
        user_prompt: str,
        tags: List,
        assistant_output: str
):
    tags.append("customllm")
    request_response = requests.post(
        "https://api.promptlayer.com/rest/track-request",
        json={
            "function_name": "langchain.PromptLayerChatOpenAI",
            "provider_type": "langchain",
            "args":
                [
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
            "kwargs":
                {
                    "model": "llm",
                    "request_timeout": "None",
                    "max_tokens": "None",
                    "stream": "False",
                    "n": 1,
                    "temperature": 0.0
                },
            "tags": tags,
            "request_response":
                [
                    {
                        "role": "assistant",
                        "content": assistant_output
                    }
                ],
            "request_start_time": datetime.datetime.now().timestamp(),
            "request_end_time": datetime.datetime.now().timestamp(),
            "api_key": os.environ.get("PROMPTLAYER_API_KEY")
        },
    )

    print(request_response.json())


if __name__ == '__main__':
    publish_prompt_template(
        user_prompt="test",
        tags=["test"],
        assistant_output="test"
    )
