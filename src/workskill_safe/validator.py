from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from workskill_safe.models import ValidationResult
from workskill_safe.scanner import scan_text

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_skill(skill_dir: Path) -> ValidationResult:
    errors: list[str] = []
    warnings: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return ValidationResult(False, ("Missing SKILL.md",))

    text = skill_file.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    metadata: dict[str, Any] = {}
    if not match:
        errors.append("Missing or invalid YAML front matter")
    else:
        try:
            loaded = yaml.safe_load(match.group(1))
            if isinstance(loaded, dict):
                metadata = loaded
            else:
                errors.append("YAML front matter must be a mapping")
        except yaml.YAMLError:
            errors.append("YAML front matter cannot be parsed")

    name = metadata.get("name")
    description = metadata.get("description")
    if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
        errors.append("Metadata 'name' must use lowercase kebab-case")
    if not isinstance(description, str) or len(description.strip()) < 30:
        errors.append("Metadata 'description' is missing or too vague")

    lowered = text.lower()
    if "privacy" not in lowered:
        errors.append("Missing privacy guidance")
    if "when not to use" not in lowered and "do not use" not in lowered:
        errors.append("Missing non-trigger conditions")

    findings = scan_text(text)
    if findings:
        categories = sorted({item.category for item in findings})
        errors.append(f"Sensitive patterns remain: {', '.join(categories)}")

    references_dir = skill_dir / "references"
    if not references_dir.exists():
        warnings.append("No references directory")

    return ValidationResult(not errors, tuple(errors), tuple(warnings))
