# src/multilingual_subtitles/stt/__init__.py
"""
Speech-to-text (STT) integration layer.

This package contains:
- Abstract interfaces for transcription engines
- Concrete implementations (e.g., Whisper)
- Data structures representing timed transcription segments

All STT backends must conform to the interfaces defined in api.py.
"""