import json
from pathlib import Path

import pytest

from workskill_safe.sanitizer import sanitize_file


def _synthetic_email() -> str:
    return "demo.user" + "@" + "example.test"


def test_sanitize_masks_findings_and_audit(tmp_path: Path) -> None:
    source = tmp_path / "source.md"
    target = tmp_path / "sanitized.md"
    synthetic_email = _synthetic_email()
    source.write_text(f"Contact {synthetic_email}\n", encoding="utf-8")

    report = sanitize_file(source, target)

    assert len(report.findings) == 1
    assert target.read_text(encoding="utf-8") == "Contact [EMAIL_REMOVED]\n"
    audit = json.loads((tmp_path / "sanitized.md.audit.json").read_text(encoding="utf-8"))
    assert audit["source"] == "source.md"
    assert synthetic_email not in json.dumps(audit)


def test_sanitize_refuses_to_overwrite_source(tmp_path: Path) -> None:
    source = tmp_path / "source.md"
    source.write_text("safe content\n", encoding="utf-8")
    with pytest.raises(ValueError, match="overwrite"):
        sanitize_file(source, source)
