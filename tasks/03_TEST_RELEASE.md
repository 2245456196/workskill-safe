# Task 03 — Test, CI, Pilot Support, and Release Preparation

## Tests

Cover at minimum:

- safe input
- email
- phone
- URL
- Windows path
- Unix path
- token-like secret
- confidentiality marker
- invalid or missing rule configuration
- invalid YAML front matter
- missing Skill description
- sensitive generated Skill
- input overwrite protection
- masked audit output
- Traditional Chinese content

Every new privacy rule requires:

- positive test
- near-miss test
- false-positive consideration

## CI

Add GitHub Actions for:

- pytest
- ruff
- mypy
- package build
- demo
- secret scanning
- dependency review when available

Add a guard that core modules do not make network calls.

## Private pilot support

Create local-only pilot templates and aggregate metrics. Never commit raw pilot content.

Recommended private pilots:

1. sanitized meeting notes to action register
2. sanitized proposal process to review checklist
3. sanitized daily work log to reusable intake workflow

Only publish aggregate counts, synthetic reproductions, Issue links, rule improvements, and release changes.

## Release preparation

- Verify README commands.
- Update CHANGELOG and ROADMAP.
- Add a release checklist.
- Prepare `v0.1.0` notes.
- Do not publish the Release without explicit maintainer approval.
- Do not submit the OpenAI application automatically.

## Definition of ready for maintainer review

```bash
python -m pytest
ruff check .
mypy src
workskill-safe demo
```

All commands pass on a clean GitHub runner, public fixtures are synthetic, and no sensitive content is present.

## Suggested branches

- `test/ci-security`
- `docs/v0.1-preparation`
