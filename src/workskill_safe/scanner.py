from __future__ import annotations

import re
from pathlib import Path

from workskill_safe.models import Finding, Rule, ScanReport
from workskill_safe.rules import load_rules


def mask_value(value: str) -> str:
    if len(value) <= 4:
        return "*" * len(value)
    return f"{value[:2]}{'*' * min(12, len(value) - 4)}{value[-2:]}"


def scan_text(text: str, rules: tuple[Rule, ...] | None = None) -> tuple[Finding, ...]:
    active_rules = rules or load_rules()
    findings: list[Finding] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for rule in active_rules:
            try:
                flags = 0 if rule.rule_id == "confidentiality-marker" else re.IGNORECASE
                pattern = re.compile(rule.pattern, flags)
            except re.error as exc:
                raise ValueError(f"Invalid regex in rule {rule.rule_id}") from exc
            for match in pattern.finditer(line):
                findings.append(
                    Finding(
                        rule_id=rule.rule_id,
                        category=rule.category,
                        severity=rule.severity,
                        line=line_number,
                        start=match.start(),
                        end=match.end(),
                        masked_preview=mask_value(match.group(0)),
                        replacement=rule.replacement,
                        message=rule.message,
                    )
                )
    return tuple(sorted(findings, key=lambda item: (item.line, item.start, item.rule_id)))


def scan_file(path: Path, rules_path: Path | None = None) -> ScanReport:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"Input file does not exist: {path}")
    text = path.read_text(encoding="utf-8")
    return ScanReport(source=path, findings=scan_text(text, load_rules(rules_path)))
