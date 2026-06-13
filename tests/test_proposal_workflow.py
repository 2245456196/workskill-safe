from pathlib import Path


def test_proposal_skill_structure() -> None:
    skill_dir = Path("skills/proposal-flow-review-ready")
    skill_text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")

    required_sections = (
        "name: proposal-flow-review-ready",
        "## Purpose",
        "## When to use",
        "## When not to use",
        "## Required inputs",
        "## Workflow",
        "## Output contract",
        "## Evidence rules",
        "## Privacy guardrails",
        "## Validation checklist",
    )
    for section in required_sections:
        assert section in skill_text

    assert (skill_dir / "references/output-schema.md").exists()
    assert (skill_dir / "references/workflow.md").exists()
    assert (skill_dir / "references/quality-checklist.md").exists()


def test_second_case_result_structure() -> None:
    result = Path("pilots/proposal-process/second-case-result.md").read_text(
        encoding="utf-8"
    )
    required_sections = (
        "## Executive summary",
        "## Minimum viable scope",
        "## Evidence status",
        "## Action list",
        "## Six-page slide outline",
        "## Result",
    )
    for section in required_sections:
        assert section in result
