from __future__ import annotations

import json
from pathlib import Path

from workskill_safe.models import Finding, ScanReport
from workskill_safe.scanner import scan_file


def sanitize_text(text: str, findings: tuple[Finding, ...]) -> str:
    lines = text.splitlines(keepends=True)
    by_line: dict[int, list[Finding]] = {}
    for finding in findings:
        by_line.setdefault(finding.line, []).append(finding)

    for line_number, line_findings in by_line.items():
        index = line_number - 1
        line = lines[index]
        for finding in sorted(line_findings, key=lambda item: item.start, reverse=True):
            line = line[: finding.start] + finding.replacement + line[finding.end :]
        lines[index] = line
    return "".join(lines)


def sanitize_file(
    input_path: Path,
    output_path: Path,
    audit_path: Path | None = None,
    rules_path: Path | None = None,
) -> ScanReport:
    if input_path.resolve() == output_path.resolve():
        raise ValueError("Refusing to overwrite the input file")
    report = scan_file(input_path, rules_path)
    original = input_path.read_text(encoding="utf-8")
    sanitized = sanitize_text(original, report.findings)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(sanitized, encoding="utf-8")

    target_audit = audit_path or output_path.with_suffix(output_path.suffix + ".audit.json")
    target_audit.parent.mkdir(parents=True, exist_ok=True)
    audit_payload = report.to_dict()
    audit_payload["output"] = output_path.name
    target_audit.write_text(
        json.dumps(audit_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return report
