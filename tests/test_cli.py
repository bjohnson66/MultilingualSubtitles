# tests/test_cli.py

from multilingual_subtitles.cli import main


def test_cli_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "CLI is working" in captured.out