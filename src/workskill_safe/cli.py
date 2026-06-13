from __future__ import annotations

import argparse
import json
import sys
import tempfile
from collections.abc import Sequence
from pathlib import Path

from workskill_safe.rules import RulesError
from workskill_safe.sanitizer import sanitize_file
from workskill_safe.scaffolder import ScaffoldError, scaffold_skill
from workskill_safe.scanner import scan_file
from workskill_safe.validator import validate_skill


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="workskill-safe",
        description="Turn sanitized work notes into reviewable Agent Skill drafts.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Scan a UTF-8 text or Markdown file")
    scan.add_argument("input", type=Path)
    scan.add_argument("--rules", type=Path)
    scan.add_argument("--json", action="store_true", dest="as_json")

    sanitize = sub.add_parser("sanitize", help="Replace findings and create a masked audit")
    sanitize.add_argument("input", type=Path)
    sanitize.add_argument("--output", type=Path, required=True)
    sanitize.add_argument("--audit", type=Path)
    sanitize.add_argument("--rules", type=Path)

    scaffold = sub.add_parser("scaffold", help="Generate an Agent Skill draft")
    scaffold.add_argument("input", type=Path)
    scaffold.add_argument("--output", type=Path, required=True)
    scaffold.add_argument("--name")
    scaffold.add_argument("--description")
    scaffold.add_argument("--reviewed", action="store_true")

    validate = sub.add_parser("validate", help="Validate a Skill directory")
    validate.add_argument("skill_dir", type=Path)

    demo = sub.add_parser("demo", help="Run a full synthetic demonstration")
    demo.add_argument("--output", type=Path)
    return parser


def _run_scan(args: argparse.Namespace) -> int:
    report = scan_file(args.input, args.rules)
    if args.as_json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(f"Findings: {len(report.findings)}")
        for item in report.findings:
            print(
                f"L{item.line} [{item.severity.value}] {item.category} "
                f"{item.masked_preview} ({item.rule_id})"
            )
    return 2 if report.has_critical else 0


def _run_sanitize(args: argparse.Namespace) -> int:
    report = sanitize_file(args.input, args.output, args.audit, args.rules)
    print(f"Sanitized file: {args.output}")
    print(f"Findings replaced: {len(report.findings)}")
    if report.has_critical:
        print(
            "Critical findings were sanitized, but downstream scaffolding "
            "remains blocked pending review."
        )
        return 2
    return 0


def _run_scaffold(args: argparse.Namespace) -> int:
    target = scaffold_skill(
        args.input,
        args.output,
        reviewed=args.reviewed,
        name=args.name,
        description=args.description,
    )
    print(f"Skill draft: {target}")
    return 0


def _run_validate(args: argparse.Namespace) -> int:
    result = validate_skill(args.skill_dir)
    if result.valid:
        print("Validation passed")
        for warning in result.warnings:
            print(f"Warning: {warning}")
        return 0
    print("Validation failed")
    for error in result.errors:
        print(f"Error: {error}")
    return 1


def _run_demo(args: argparse.Namespace) -> int:
    base = args.output or Path(tempfile.mkdtemp(prefix="workskill-safe-demo-"))
    base.mkdir(parents=True, exist_ok=True)
    source = base / "synthetic-note.md"
    sanitized = base / "synthetic-note.sanitized.md"
    skill_root = base / "skills"
    source.write_text(
        "# Synthetic Work Note\n\n"
        "Contact: demo.user@example.test\n"
        "Phone: +1-202-555-0147\n"
        "Link: https://internal.example.test/project-alpha\n"
        "Path: C:\\\\Private\\\\ProjectAlpha\\\\meeting.md\n\n"
        "1. Read the sanitized note.\n"
        "2. Extract explicit actions.\n"
        "3. Preserve missing owners as TBD.\n"
        "4. List blockers separately.\n",
        encoding="utf-8",
    )
    report = sanitize_file(source, sanitized)
    target = scaffold_skill(
        sanitized,
        skill_root,
        reviewed=True,
        name="synthetic-action-register",
    )
    result = validate_skill(target)
    print(f"Demo directory: {base}")
    print(f"Findings sanitized: {len(report.findings)}")
    print(f"Generated Skill: {target}")
    print(f"Validation: {'passed' if result.valid else 'failed'}")
    return 0 if result.valid else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "scan":
            return _run_scan(args)
        if args.command == "sanitize":
            return _run_sanitize(args)
        if args.command == "scaffold":
            return _run_scaffold(args)
        if args.command == "validate":
            return _run_validate(args)
        if args.command == "demo":
            return _run_demo(args)
    except (FileNotFoundError, ValueError, RulesError, ScaffoldError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 3 if isinstance(exc, RulesError) else 1
    parser.error("Unknown command")
    return 4


def entrypoint() -> None:
    raise SystemExit(main())
