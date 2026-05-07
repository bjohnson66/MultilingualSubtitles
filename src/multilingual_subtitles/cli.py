# src/multilingual_subtitles/cli.py
"""
Command-line interface for the multilingual_subtitles package.

Responsibilities:
- Parse user input (file paths, language options, output formats)
- Initialize default pipeline components (STT, LLM, etc.)
- Execute the end-to-end subtitle generation pipeline
- Provide user-friendly output and error messages

This module should remain thin and delegate all core logic to pipeline.py.
"""

def main():
    """
    Entry point for the subgen CLI.
    """
    print("multilingual_subtitles CLI is working!")