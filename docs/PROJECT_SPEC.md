# Project Specification

Traditional Chinese version: `docs/zh-TW/PROJECT_SPEC.md`.

## Product statement

WorkSkill Safe is a local-first Python CLI that scans and sanitizes work notes, produces a masked audit report, scaffolds a reusable Agent Skill draft, and validates the result before publication.

## MVP commands

```bash
workskill-safe scan INPUT
workskill-safe sanitize INPUT --output OUTPUT
workskill-safe scaffold INPUT --output DIR --reviewed
workskill-safe validate SKILL_DIR
workskill-safe demo
```

## Functional requirements

- Scan UTF-8 Markdown or text for identifiers, URLs, paths, sensitive material, and confidentiality markers.
- Replace findings with typed placeholders without overwriting input.
- Produce masked audit reports without full sensitive values or private absolute paths.
- Require human approval before Skill generation.
- Block critical placeholders from downstream scaffolding.
- Validate Skill metadata, non-trigger conditions, privacy guidance, and remaining sensitive patterns.
- Run a complete offline demonstration using synthetic data.

## Non-functional requirements

- Python 3.11+
- deterministic and offline core behavior
- Traditional Chinese content support
- no telemetry
- no external service calls
- explicit exit codes
- tests, lint, type checks, build, and demo in CI
