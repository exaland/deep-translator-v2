from unittest.mock import patch

import pytest
from requests import HTTPError, Response

from deep_translator import ChatGptTranslator


def test_chatgpt_translates_with_default_model(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "environment-key")
    with patch("deep_translator.chatgpt.requests.post") as post:
        post.return_value.json.return_value = {
            "choices": [{"message": {"content": "Hallo"}}]
        }

        assert ChatGptTranslator(target="german").translate("Hello") == "Hallo"

    post.assert_called_once_with(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": "Bearer environment-key"},
        json={
            "model": "gpt-6-luna",
            "messages": [
                {
                    "role": "user",
                    "content": (
                        'Translate the text below into de.\nText: "Hello"'
                    ),
                }
            ],
        },
        timeout=60,
    )
    post.return_value.raise_for_status.assert_called_once_with()


def test_chatgpt_uses_custom_model_and_surfaces_http_error():
    response = Response()
    response.status_code = 404
    with patch(
        "deep_translator.chatgpt.requests.post", return_value=response
    ) as post:
        translator = ChatGptTranslator(api_key="test-key", model="custom-model")
        with pytest.raises(HTTPError) as exc:
            translator.translate("Hello")

    assert exc.value.response is response
    assert post.call_args[1]["json"]["model"] == "custom-model"
