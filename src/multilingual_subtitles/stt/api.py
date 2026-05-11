# src/multilingual_subtitles/stt/api.py
"""
Speech-to-text (STT) interface definitions.

Responsibilities:
- Define protocol(s) or abstract base classes for STT clients
- Standardize transcription output format, including:
    - Text content
    - Start/end timestamps
- Provide a consistent interface for different STT backends

Design goals:
- Enable interchangeable STT implementations
- Support both batch and potential streaming use cases
- Keep output structured for downstream subtitle generation
"""
from typing import Protocol, List

from multilingual_subtitles.types import Segment

class EmptyTranscriptionError(Exception):
    """
    Raised when transcription is empty
    """

class STTClient(Protocol):
    def transcribe(self, audio_path: str) -> List[Segment]:
        ...