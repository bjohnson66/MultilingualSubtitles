# src/multilingual_subtitles/llm/api.py
"""
LLM interface definitions and base abstractions.

Responsibilities:
- Define protocol(s) or abstract base classes for LLM clients
- Standardize input/output formats (e.g., message-based chat)
- Enable backend-agnostic interaction with different LLM providers

Key design considerations:
- Support chat-style interactions (role-based messages)
- Allow future extensions (streaming, tool use, etc.)
- Keep interface minimal but expressive

Concrete implementations (e.g., Ollama, OpenAI) will live in separate modules.
"""
from typing import Protocol, List


class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content


class LLMClient(Protocol):
    def chat(self, messages: List[Message]) -> str:
        ...