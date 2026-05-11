# tests/test_stt.py
import pytest

from multilingual_subtitles.stt.api import (
    Segment,
    EmptyTranscriptionError,
)

from multilingual_subtitles.stt.mock_backend import (
    MockSTTClient,
)


def test_mock_transcription_returns_segments():
    client = MockSTTClient()

    segments = client.transcribe("fake_audio.wav")

    assert isinstance(segments, list)
    assert len(segments) == 2

    assert isinstance(segments[0], Segment)

    assert segments[0].text == "Hello"
    assert segments[1].text == "world"

    assert segments[0].start == 0.0
    assert segments[0].end == 2.0


def test_empty_transcription_raises_exception():
    client = MockSTTClient(empty=True)

    with pytest.raises(EmptyTranscriptionError):
        client.transcribe("empty.wav")