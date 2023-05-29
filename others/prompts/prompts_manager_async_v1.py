from util.keys import initial

# 初始化秘钥配置
initial('../../.env')


import os
import aiohttp
import anyio
import datetime
from typing import List


PROMPTLAYER_API = "https://api.promptlayer.com/rest/track-request"


def count_tokens(text):
    word_count = len(text)
    return word_count


class Promptlayer:

    async def track_request(
        self,
        model_name: str,
        user_prompt: str,
        tags: List,
        assistant_output: str,
        temperature: float
    ):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                PROMPTLAYER_API,
                json={
                    "function_name": "langchain.PromptLayerChatOpenAI",
                    "provider_type": "langchain",
                    "args": [
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ],
                    "kwargs": {
                        "model": model_name,
                        "request_timeout": "None",
                        "max_tokens": count_tokens(user_prompt),
                        "stream": "False",
                        "n": 1,
                        "temperature": temperature
                    },
                    "tags": tags,
                    "request_response": [
                        {
                            "role": "assistant",
                            "content": assistant_output
                        }
                    ],
                    "request_start_time": datetime.datetime.now().timestamp(),
                    "request_end_time": datetime.datetime.now().timestamp(),
                    "api_key": os.environ.get("PROMPTLAYER_API_KEY")
                },
            ) as response:
                request_response = await response.json()

        return request_response


async def main():
    promptlayer = Promptlayer()

    result = await promptlayer.track_request(
        model_name="llm",
        user_prompt="test",
        tags=["test"],
        assistant_output="test",
        temperature=0.001
    )

    print(result)


if __name__ == '__main__':
    anyio.run(main)

