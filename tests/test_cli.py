from pathlib import Path

from workskill_safe.cli import main


def test_demo_pipeline(tmp_path: Path) -> None:
    assert main(["demo", "--output", str(tmp_path)]) == 0
    assert (tmp_path / "skills" / "synthetic-action-register" / "SKILL.md").exists()


def test_scan_missing_file_returns_error(tmp_path: Path) -> None:
    assert main(["scan", str(tmp_path / "missing.md")]) == 1
