# Task 02 — Implement the MVP

## Goal

Implement `scan`, `sanitize`, `scaffold`, `validate`, and `demo` as deterministic local commands.

## Scan

- Detect email, phone-like strings, URLs, Windows paths, Unix paths, common token formats, confidentiality markers, and configurable forbidden terms.
- Report category, severity, line number, masked preview, rule ID, and remediation.
- Never print a full secret.
- Fail closed when rules are missing or invalid.

## Sanitize

- Never overwrite input by default.
- Replace findings with typed placeholders.
- Produce a separate masked audit report.
- Preserve procedural structure.
- Block scaffolding when critical findings remain.

## Scaffold

Generate:

```text
skill-name/
├─ SKILL.md
└─ references/
   ├─ workflow.md
   └─ quality-checklist.md
```

The generated Skill must contain:

- YAML front matter with `name` and `description`
- purpose
- preconditions
- required inputs
- ordered workflow
- output contract
- non-trigger conditions
- privacy guardrails
- validation checklist

## Validate

Reject missing metadata, missing privacy guidance, unresolved sensitive findings, forbidden terms, secret patterns, and private absolute paths.

## Demo

Run the complete pipeline on repository-owned synthetic fixtures only.

## Acceptance criteria

- All five commands are documented.
- Exit codes match `docs/PROJECT_SPEC.md`.
- Traditional Chinese input is supported.
- Core modules do not perform network calls.
- Public fixtures are synthetic.

## Suggested branches

- `feat/privacy-scanner`
- `feat/sanitize-and-audit`
- `feat/skill-scaffold-validator`
