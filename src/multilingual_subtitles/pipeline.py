# src/multilingual_subtitles/pipeline.py
"""
Core pipeline orchestration.

Responsibilities:
- Coordinate the full subtitle generation workflow:
    1. Audio extraction (if needed)
    2. Speech-to-text transcription
    3. Text translation via LLM
    4. Subtitle formatting (e.g., SRT/VTT)
- Remain independent of specific STT/LLM implementations
- Operate purely on abstract interfaces defined in submodules

Design goals:
- Composable and testable
- No direct dependency on external services
- Clear data flow between stages
"""

def run_pipeline():
    """
    Placeholder pipeline function.
    """
    return "pipeline not implemented yet"