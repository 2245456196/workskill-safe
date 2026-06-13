# WorkSkill Safe

> Privacy-first CLI for turning work notes into reusable Agent Skills without publishing confidential data.

## Status

Bootstrap specification stage. The repository is being prepared for Codex implementation.

## Problem

Operational knowledge is often buried in work logs, meeting notes, and project records. These sources may contain company-confidential information, client identifiers, personal data, internal URLs, credentials, or context that should never be published.

WorkSkill Safe will provide a local-first, deterministic and reviewable workflow:

```text
private note
    ↓
scan
    ↓
sanitize + audit report
    ↓
human approval
    ↓
Agent Skill scaffold
    ↓
validate
```

## Planned core commands

```bash
workskill-safe scan INPUT
workskill-safe sanitize INPUT --output OUTPUT
workskill-safe scaffold INPUT --output DIR
workskill-safe validate SKILL_DIR
workskill-safe demo
```

## Design principles

- Local-first
- No external model or API required for core commands
- Fail closed
- Deterministic privacy rules
- Human review before publication
- Synthetic examples only in the public repository
- Auditable transformations

## Important limitation

This project will not guarantee anonymization, regulatory compliance, or prevention of every disclosure. Contextual re-identification remains possible, so generated output always requires human review.

## Current handoff

Codex should read `AGENTS.md`, `PRIVACY.md`, `docs/PROJECT_SPEC.md`, `docs/THREAT_MODEL.md`, and `CODEX_HANDOFF.md` before implementation.

## License

MIT license will be added during repository bootstrap.
