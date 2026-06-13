from __future__ import annotations

import re
from pathlib import Path

from workskill_safe.scanner import scan_text


class ScaffoldError(ValueError):
    """Raised when a Skill cannot be generated safely."""


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "generated-work-skill"


def _extract_steps(text: str) -> list[str]:
    steps: list[str] = []
    for line in text.splitlines():
        match = re.match(r"\s*(?:\d+[.)]|[-*])\s+(.+)", line)
        if not match:
            continue
        candidate = match.group(1).strip()
        if "[" in candidate or "]" in candidate:
            continue
        if len(candidate) > 160:
            candidate = candidate[:157].rstrip() + "..."
        steps.append(candidate)
    return steps[:10]


def scaffold_skill(
    input_path: Path,
    output_dir: Path,
    *,
    reviewed: bool,
    name: str | None = None,
    description: str | None = None,
) -> Path:
    if not reviewed:
        raise ScaffoldError("Human review is required; pass reviewed=True only after approval")
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    text = input_path.read_text(encoding="utf-8")
    if "[SECRET_REMOVED]" in text:
        raise ScaffoldError("Critical secret placeholder remains; do not scaffold this source")

    remaining = scan_text(text)
    if remaining:
        raise ScaffoldError("Input still contains findings; sanitize and review it first")

    skill_name = slugify(name or input_path.stem)
    target = output_dir / skill_name
    if target.exists() and any(target.iterdir()):
        raise ScaffoldError(f"Target directory is not empty: {target}")

    target.mkdir(parents=True, exist_ok=True)
    references = target / "references"
    references.mkdir(exist_ok=True)

    steps = _extract_steps(text)
    if not steps:
        steps = [
            "Confirm the objective and required inputs.",
            "Apply the reusable workflow without copying source-specific facts.",
            "Produce the defined output and list missing information.",
            "Run the privacy and quality checklist before returning the result.",
        ]
    step_block = "\n".join(f"{index}. {step}" for index, step in enumerate(steps, start=1))
    skill_description = description or (
        "Convert a sanitized and human-reviewed work note into a reusable workflow. "
        "Use only when the input contains no private, confidential, personal, or credential data. "
        "Do not use on raw employer or client material."
    )

    skill_md = f"""---
name: {skill_name}
description: >-
  {skill_description}
---

# {skill_name.replace('-', ' ').title()}

## Purpose

Apply a reusable method extracted from sanitized work material without retaining
case-specific facts.

## Preconditions

- The input passed privacy scanning.
- Sensitive findings were sanitized.
- A human reviewed the sanitized content.
- The output is a method, not a record of the original event.

## Inputs

- sanitized source material
- target user or role
- desired output
- known constraints

## Workflow

{step_block}

## Output contract

Return a clear, testable result with assumptions, missing information, and validation status.

## When not to use

Do not use when the source contains raw company, client, personal, regulated,
credential, private-link, or confidential information.

## Privacy guardrails

- Do not copy source-specific names, dates, values, URLs, or paths.
- Do not infer identities or unpublished business facts.
- Stop when authorization or privacy status is uncertain.
- Require human review before publication.

## Validation checklist

- [ ] Reusable beyond the original case
- [ ] No source-specific identifiers
- [ ] Trigger and non-trigger conditions are clear
- [ ] Output format is testable
- [ ] Privacy guardrails are present
- [ ] Synthetic test case passes
"""
    (target / "SKILL.md").write_text(skill_md, encoding="utf-8")
    (references / "workflow.md").write_text(
        "# Workflow Reference\n\n" + step_block + "\n",
        encoding="utf-8",
    )
    (references / "quality-checklist.md").write_text(
        "# Quality Checklist\n\n"
        "- [ ] Narrow, reusable objective\n"
        "- [ ] Explicit inputs and output\n"
        "- [ ] No identifying context\n"
        "- [ ] Privacy boundary preserved\n"
        "- [ ] Synthetic verification completed\n",
        encoding="utf-8",
    )
    return target
