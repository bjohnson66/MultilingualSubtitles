# tests/test_pipeline.py
import pytest

from multilingual_subtitles.pipeline import run_pipeline
from multilingual_subtitles.stt.mock_backend import MockSTTClient
from multilingual_subtitles.llm.mock_backend import MockLLMClient

def test_pipeline_with_stt_only():
    stt = MockSTTClient()  # Use the STT mock

    result = run_pipeline(stt, "fake_audio.wav")

    expected = (
        "1\n"
        "00:00:00,000 --> 00:00:02,000\n"
        "Hello\n\n"
        "2\n"
        "00:00:02,000 --> 00:00:04,000\n"
        "world\n"
    )

    assert result == expected

def test_pipeline_with_stt_and_llm_translation():
    stt = MockSTTClient()  # Use the STT mock
    llm = MockLLMClient(mode="polish")  # Use LLM mock in polish translation mode

    result = run_pipeline(stt, "fake_audio.wav", llm)

    expected = (
        "1\n"
        "00:00:00,000 --> 00:00:02,000\n"
        "Cześć\n\n"
        "2\n"
        "00:00:02,000 --> 00:00:04,000\n"
        "świat\n"
    )

    assert result == expected