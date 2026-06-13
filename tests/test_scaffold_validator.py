from pathlib import Path

import pytest

from workskill_safe.scaffolder import ScaffoldError, scaffold_skill
from workskill_safe.validator import validate_skill


def _synthetic_email() -> str:
    return "demo.user" + "@" + "example.test"


def test_scaffold_requires_human_review(tmp_path: Path) -> None:
    source = tmp_path / "sanitized.md"
    source.write_text("1. Read input.\n2. Produce output.\n", encoding="utf-8")
    with pytest.raises(ScaffoldError, match="Human review"):
        scaffold_skill(source, tmp_path / "skills", reviewed=False)


def test_generated_skill_validates(tmp_path: Path) -> None:
    source = tmp_path / "sanitized.md"
    source.write_text(
        "1. Confirm the objective.\n"
        "2. Extract actions.\n"
        "3. List missing information.\n",
        encoding="utf-8",
    )
    target = scaffold_skill(
        source,
        tmp_path / "skills",
        reviewed=True,
        name="action-register",
    )
    result = validate_skill(target)
    assert result.valid, result.errors


def test_validator_rejects_sensitive_content(tmp_path: Path) -> None:
    skill = tmp_path / "unsafe-skill"
    skill.mkdir()
    sensitive_value = _synthetic_email()
    (skill / "SKILL.md").write_text(
        "---\n"
        "name: unsafe-skill\n"
        "description: This description is intentionally long enough for validation.\n"
        "---\n\n"
        "# Unsafe Skill\n\n"
        "## Privacy\n\nDo not use on raw data.\n\n"
        f"Contact: {sensitive_value}\n",
        encoding="utf-8",
    )
    result = validate_skill(skill)
    assert not result.valid
    assert any("Sensitive patterns remain" in error for error in result.errors)


def test_scaffold_blocks_critical_placeholder(tmp_path: Path) -> None:
    source = tmp_path / "sanitized.md"
    source.write_text("Value: [SECRET_REMOVED]\n", encoding="utf-8")
    with pytest.raises(ScaffoldError, match="Critical"):
        scaffold_skill(source, tmp_path / "skills", reviewed=True)
