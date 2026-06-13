# AGENTS.md

## Mission

Maintain WorkSkill Safe as a small, local-first, privacy-first CLI that converts sanitized work knowledge into reusable Agent Skill drafts.

## Priority order

1. Privacy and security
2. Correctness
3. Testability
4. Clear documentation
5. Small maintainable scope
6. Convenience

## Non-negotiable rules

- Never add real company, client, employee, family, health, financial, credential, or private project data.
- Use synthetic fixtures only.
- Never add API keys, tokens, internal URLs, private paths, `.env`, or credentials.
- Core commands must work offline.
- Do not call remote LLMs in v0.1.x.
- Fail closed when rules cannot be loaded or safety is uncertain.
- Do not silently remove content; produce an audit record.
- Do not claim perfect detection or compliance.
- Do not weaken tests to make CI pass.
- Do not push feature work directly to `main`.
- Do not submit external forms or publish releases without explicit maintainer approval.

## Expected commands

```bash
python -m pytest
ruff check .
mypy src
workskill-safe demo
```

## Repository conventions

- Python 3.11+
- `src/` layout
- Type hints on public functions
- Small pure functions where possible
- Deterministic tests
- Structured error messages
- No hidden network calls
- Public documentation in English
- Conventional Commit style preferred

## Definition of done

A change is done only when:

- tests pass
- lint and type checks pass
- privacy regression tests pass
- documentation matches actual CLI behavior
- no sensitive fixture is introduced
- CHANGELOG is updated for user-visible behavior changes
- PR explains risk, verification, and privacy impact
