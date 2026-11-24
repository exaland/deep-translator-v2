__copyright__ = "Copyright (C) 2026 Exaland Concept "

import os
from typing import List, Optional

import requests

from deep_translator.base import BaseTranslator
from deep_translator.constants import OPEN_AI_ENV_VAR
from deep_translator.exceptions import ApiKeyException


class ChatGptTranslator(BaseTranslator):
    """
    class that wraps functions, which use the ChatGPT
    under the hood to translate word(s)
    """

    def __init__(
        self,
        source: str = "auto",
        target: str = "english",
        api_key: Optional[str] = None,
        model: str = "gpt-6-luna",
        **kwargs,
    ):
        """
        @param api_key: your openai api key.
        @param source: source language
        @param target: target language
        @param model: OpenAI model that supports Chat Completions
        """
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY") or os.getenv(OPEN_AI_ENV_VAR)
        if not api_key:
            raise ApiKeyException(env_var="OPENAI_API_KEY")

        self.api_key = api_key
        self.model = model

        super().__init__(source=source, target=target, **kwargs)

    def translate(self, text: str, **kwargs) -> str:
        """
        @param text: text to translate
        @return: translated text
        """
        prompt = f"Translate the text below into {self.target}.\n"
        prompt += f'Text: "{text}"'

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

    def translate_file(self, path: str, **kwargs) -> str:
        return self._translate_file(path, **kwargs)

    def translate_batch(self, batch: List[str], **kwargs) -> List[str]:
        """
        @param batch: list of texts to translate
        @return: list of translations
        """
        return self._translate_batch(batch, **kwargs)
