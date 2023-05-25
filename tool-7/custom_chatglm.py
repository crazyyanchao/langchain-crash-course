import os
from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

CHATGLM_API = os.environ.get("CHATGLM_API")


class ChatGLMLLM(LLM):
    temperature: float = 0.001
    type = "chatglm"

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return self.api(prompt, self.temperature)

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"type": self.type}

    @staticmethod
    def api(prompt, temperature):
        headers = {"Content-type": "application/json"}
        url = CHATGLM_API
        data = {
            "query": prompt,
            "history": [],
            "max_length": 2048,
            "temperature": temperature
        }

        # UNSAFE_LEGACY_RENEGOTIATION_DISABLED ERROR FIX
        import urllib3
        from urllib3.util.ssl_ import create_urllib3_context

        ctx = create_urllib3_context()
        ctx.load_default_certs()
        ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

        with urllib3.PoolManager(ssl_context=ctx) as http:
            response = http.request("POST", url, json=data, headers=headers)
            return response.json()['response']
