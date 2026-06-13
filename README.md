# WorkSkill Safe

[繁體中文](docs/zh-TW/PROJECT_OVERVIEW.md) | English

> Privacy-first, local-first CLI for turning work notes into reusable Agent Skills without publishing confidential data.

## Why this project exists

Knowledge workers often want to preserve repeatable methods from meeting notes, project logs, and proposal work. Those sources can contain employer information, client identifiers, personal data, internal URLs, authentication material, or context that should never be published.

WorkSkill Safe provides a deterministic and reviewable local workflow:

```text
private note
    ↓
scan
    ↓
sanitize + masked audit report
    ↓
human review
    ↓
Agent Skill scaffold
    ↓
validate
```

## Status

Early MVP. The tool reduces obvious disclosure risks but does not guarantee anonymization, regulatory compliance, or prevention of contextual re-identification.

## Core commands

```bash
workskill-safe scan INPUT
workskill-safe sanitize INPUT --output OUTPUT
workskill-safe scaffold INPUT --output DIR --reviewed
workskill-safe validate SKILL_DIR
workskill-safe demo
```

## Quick start

```bash
python -m pip install -e ".[dev]"
workskill-safe demo
python -m pytest
```

## Design principles

- local-first and offline core behavior
- deterministic privacy rules
- fail closed when configuration or safety is uncertain
- no external model or service required
- no raw work data in the public repository
- synthetic public examples only
- human review before publication
- auditable transformations without exposing full secret values

## Public repository boundary

Allowed:

- source code
- public documentation
- generic rules
- fully synthetic fixtures
- aggregate, non-identifying maintenance evidence

Prohibited:

- real employer or client documents
- raw meeting notes or work logs
- personal data
- pricing, contracts, internal KPIs, or unpublished strategy
- private URLs or file paths
- authentication material or local configuration secrets

Read `PRIVACY.md` and `docs/THREAT_MODEL.md` before using the project.

## Documentation

- Traditional Chinese overview: `docs/zh-TW/PROJECT_OVERVIEW.md`
- Traditional Chinese privacy guide: `docs/zh-TW/PRIVACY_GUIDE.md`
- Project specification: `docs/PROJECT_SPEC.md`
- Architecture: `docs/ARCHITECTURE.md`
- Threat model: `docs/THREAT_MODEL.md`
- Pilot plan: `docs/PILOT_PLAN.md`
- Codex handoff: `CODEX_HANDOFF.md`

## License

MIT
