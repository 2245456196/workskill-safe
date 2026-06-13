# Project Specification

## Product statement

WorkSkill Safe is a local-first Python CLI that scans and sanitizes work notes, produces a masked audit report, scaffolds a reusable Agent Skill draft, and validates the result before publication.

## User story

As a knowledge worker, I want to extract a reusable workflow from private notes without copying confidential details into a public Agent Skill repository.

## MVP commands

```bash
workskill-safe scan INPUT
workskill-safe sanitize INPUT --output OUTPUT
workskill-safe scaffold INPUT --output DIR
workskill-safe validate SKILL_DIR
workskill-safe demo
```

## Functional requirements

### Scan

Support UTF-8 `.md` and `.txt` files. Detect at minimum:

- email addresses
- phone-like strings
- URLs
- Windows and Unix absolute paths
- common secret and token formats
- configurable forbidden terms
- confidentiality markers

Each finding must include category, severity, line number, masked preview, rule identifier, and remediation guidance. Full secret values must not appear in logs.

### Sanitize

- Never overwrite input by default.
- Replace findings with typed placeholders.
- Produce a separate masked audit report.
- Preserve procedural structure where possible.
- Block downstream scaffolding when critical findings remain.

### Scaffold

Input must have passed sanitization and human review.

Generate:

```text
skill-name/
├─ SKILL.md
└─ references/
   ├─ workflow.md
   └─ quality-checklist.md
```

`SKILL.md` must contain YAML front matter with `name` and `description`, plus purpose, preconditions, inputs, workflow, output contract, non-trigger conditions, privacy guardrails, and validation criteria.

### Validate

Validate:

- required files
- YAML front matter
- name and description
- trigger clarity
- privacy section
- forbidden terms
- secret patterns
- private absolute paths
- unresolved sensitive findings

### Demo

One command must run the complete pipeline using only synthetic repository fixtures.

## Non-functional requirements

- Python 3.11+
- offline core behavior
- deterministic output
- type hints on public functions
- cross-platform paths
- Traditional Chinese input supported
- no telemetry in the MVP
- no external API calls in core commands
- explicit exit codes

## Suggested exit codes

- `0`: success
- `1`: validation or recoverable input failure
- `2`: critical privacy or security finding
- `3`: configuration error
- `4`: internal error

## Acceptance tests

1. Safe synthetic note passes.
2. Email, phone, URL, Windows path, and Unix path are detected.
3. Token-like secrets cause a critical result.
4. Missing or invalid rule files fail closed.
5. Sanitizer never overwrites input by default.
6. Audit reports mask original values.
7. Generated Skills contain required metadata.
8. Validator rejects sensitive output.
9. Demo succeeds without network access.
10. Tests include Traditional Chinese content.
