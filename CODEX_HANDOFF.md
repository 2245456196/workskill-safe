# Codex Handoff

## Objective

Implement WorkSkill Safe as a public, installable, testable Python 3.11+ CLI:

> A privacy-first local tool for turning work notes into reusable Agent Skills without publishing confidential data.

## Read first

1. `AGENTS.md`
2. `PRIVACY.md`
3. `docs/PROJECT_SPEC.md`
4. `docs/THREAT_MODEL.md`
5. `tasks/01_BOOTSTRAP.md`
6. `tasks/02_IMPLEMENT_MVP.md`
7. `tasks/03_TEST_RELEASE.md`

## Non-negotiable constraints

- All public fixtures must be fully synthetic.
- Never add real company, client, person, project, private path, URL, pricing, contract, KPI, credential, or confidential data.
- Core functionality must work offline and must not call an external LLM or API.
- Use fail-closed behavior when safety or configuration is uncertain.
- Never overwrite raw input by default.
- Audit output must not contain full original secret values.
- Do not fabricate users, adoption, issues, stars, or maintenance evidence.
- Do not publish a Release or submit the OpenAI application without explicit maintainer approval.

## Required repository structure

```text
workskill-safe/
├─ README.md
├─ AGENTS.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ SECURITY.md
├─ PRIVACY.md
├─ GOVERNANCE.md
├─ ROADMAP.md
├─ CHANGELOG.md
├─ CODE_OF_CONDUCT.md
├─ pyproject.toml
├─ src/workskill_safe/
├─ tests/
├─ skills/work-log-to-skill/
├─ examples/
├─ docs/
└─ .github/
```

## Required commands

```bash
workskill-safe scan INPUT
workskill-safe sanitize INPUT --output OUTPUT
workskill-safe scaffold INPUT --output DIR
workskill-safe validate SKILL_DIR
workskill-safe demo
```

## Minimum verification

```bash
python -m pytest
ruff check .
mypy src
workskill-safe demo
```

## Git workflow

Do not implement everything in one commit. Use meaningful branches and PRs, for example:

- `chore/bootstrap-python-project`
- `feat/privacy-scanner`
- `feat/sanitize-and-audit`
- `feat/skill-scaffold-validator`
- `test/ci-security`
- `docs/v0.1-preparation`

For every stage, report:

1. completed work
2. changed files
3. test results
4. privacy impact
5. remaining risk
6. proposed PR title and body

## Start instruction

Before modifying files, summarize your understanding of:

- the privacy boundary
- the exact MVP scope
- the fail-closed conditions
- the planned branch sequence

Then complete the tasks in order.
