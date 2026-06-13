from pathlib import Path

import pytest

from workskill_safe.rules import RulesError, load_rules
from workskill_safe.scanner import scan_text


def _synthetic_email() -> str:
    return "demo.user" + "@" + "example.test"


def _synthetic_phone() -> str:
    return "+1" + "-202" + "-555" + "-0147"


def _synthetic_url() -> str:
    return "https" + "://" + "internal.example.test/project-alpha"


def test_scanner_detects_common_sensitive_patterns() -> None:
    text = (
        f"Email: {_synthetic_email()}\n"
        f"Phone: {_synthetic_phone()}\n"
        f"Link: {_synthetic_url()}\n"
        "Path: C:\\Private\\ProjectAlpha\\meeting.md\n"
    )
    categories = {finding.category for finding in scan_text(text)}
    assert {"email", "phone", "url", "path"}.issubset(categories)


def test_scanner_supports_traditional_chinese_content() -> None:
    findings = scan_text("聯絡方式：" + _synthetic_email() + "\n")
    assert any(item.category == "email" for item in findings)


def test_missing_rules_fail_closed(tmp_path: Path) -> None:
    with pytest.raises(RulesError):
        load_rules(tmp_path / "missing.yml")
