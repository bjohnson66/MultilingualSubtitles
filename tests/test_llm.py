# tests/test_llm.py
from multilingual_subtitles.llm.api import Message
from multilingual_subtitles.llm.mock_backend import MockLLMClient


def test_llm_identity_mode_returns_last_user_message():
    llm = MockLLMClient(mode="identity")

    messages = [
        Message(role="system", content="Translate text"),
        Message(role="user", content="Hello world"),
    ]

    result = llm.chat(messages)

    assert result == "Hello world"


def test_llm_polish_mode_translates_known_words():
    llm = MockLLMClient(mode="polish")

    messages = [
        Message(role="user", content="Hello"),
    ]

    result = llm.chat(messages)

    assert result == "Cześć"