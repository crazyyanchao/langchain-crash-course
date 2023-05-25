import os
import requests
import datetime
from typing import List

PROMPTLAYER_API = "https://api.promptlayer.com/rest/track-request"


def count_tokens(text):
    word_count = len(text)
    return word_count


class Promptlayer:

    @staticmethod
    def track_request(
            model_name: str,
            user_prompt: str,
            tags: List,
            assistant_output: str,
            temperature: float
    ):
        request_response = requests.post(
            PROMPTLAYER_API,
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
            },
        )

        return request_response


if __name__ == '__main__':
    promptlayer = Promptlayer()
    promptlayer.track_request(
        model_name="llm",
        user_prompt="test",
        tags=["test"],
        assistant_output="test",
        temperature=0.001
    )
