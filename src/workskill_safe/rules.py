from __future__ import annotations

from importlib.resources import files
from pathlib import Path
from typing import Any

import yaml

from workskill_safe.models import Rule, Severity


class RulesError(ValueError):
    """Raised when privacy rules cannot be loaded safely."""


def _default_rules_path() -> Path:
    resource = files("workskill_safe").joinpath("rules/default_rules.yml")
    return Path(str(resource))


def load_rules(path: Path | None = None) -> tuple[Rule, ...]:
    rules_path = path or _default_rules_path()
    if not rules_path.exists():
        raise RulesError(f"Rule file is missing: {rules_path}")

    try:
        raw: Any = yaml.safe_load(rules_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise RulesError(f"Unable to load rule file: {rules_path}") from exc

    if not isinstance(raw, dict) or not isinstance(raw.get("rules"), list):
        raise RulesError("Rule file must contain a top-level 'rules' list")

    loaded: list[Rule] = []
    for index, item in enumerate(raw["rules"]):
        if not isinstance(item, dict):
            raise RulesError(f"Rule at index {index} is not a mapping")
        required = {"id", "category", "severity", "pattern", "replacement", "message"}
        missing = required.difference(item)
        if missing:
            raise RulesError(f"Rule at index {index} is missing: {sorted(missing)}")
        try:
            severity = Severity(str(item["severity"]))
        except ValueError as exc:
            raise RulesError(f"Rule {item['id']} has invalid severity") from exc
        loaded.append(
            Rule(
                rule_id=str(item["id"]),
                category=str(item["category"]),
                severity=severity,
                pattern=str(item["pattern"]),
                replacement=str(item["replacement"]),
                message=str(item["message"]),
            )
        )

    if not loaded:
        raise RulesError("Rule file contains no rules")
    return tuple(loaded)
