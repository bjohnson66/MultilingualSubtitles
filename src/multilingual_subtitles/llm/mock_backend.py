# src/multilingual_subtitles/llm/mock_backend.py
"""
Mock implementation of LLM translation using our api protocol for test driven development.
"""

class MockLLMClient:
    """
    Deterministic fake LLM used for pipeline testing.
    """

    def __init__(self, mode="identity"):
        self.mode = mode

    def chat(self, messages):
        # extract last user message
        last_user = None

        for m in messages:
            if m.role == "user":
                last_user = m.content

        if last_user is None:
            return ""

        if self.mode == "identity":
            return last_user

        if self.mode == "polish":
            mapping = {
                "Hello": "Cześć",
                "world": "świat",
            }
            return mapping.get(last_user, last_user)

        raise ValueError(f"Unknown mode: {self.mode}")