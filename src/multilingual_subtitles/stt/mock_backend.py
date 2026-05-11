# src/multilingual_subtitles/stt/mock_backend.py
"""
Mock implementation of Speech To Text using our api protocol for test driven development.
"""

from multilingual_subtitles.stt.api import (
    Segment,
    EmptyTranscriptionError,
)


class MockSTTClient:
    """
    Mock STT backend used for testing.
    """

    def __init__(self, empty=False):
        self.empty = empty

    def transcribe(self, audio_path: str):
        if self.empty:
            raise EmptyTranscriptionError(
                "No speech detected in audio."
            )

        return [
            Segment(0.0, 2.0, "Hello"),
            Segment(2.0, 4.0, "world"),
        ]