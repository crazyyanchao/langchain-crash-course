from util.keys import initial

# 初始化秘钥配置
initial('../../.env')

import os
import aiohttp
import asyncio
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
            async with session.post(PROMPTLAYER_API, json={
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
                        "model": model_name,
                        "request_timeout": "None",
                        "max_tokens": count_tokens(user_prompt),
                        "stream": "False",
                        "n": 1,
                        "temperature": temperature
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
            }) as response:
                request_response = await response.json()

        return request_response


if __name__ == '__main__':
    promptlayer = Promptlayer()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(promptlayer.track_request(
        model_name="llm",
        user_prompt="test",
        tags=["async"],
        assistant_output="test",
        temperature=0.001
    ))
    loop.close()

    print(result)
