# src/multilingual_subtitles/types.py

from dataclasses import dataclass

@dataclass
class Segment:
    start: float
    end: float
    text: str