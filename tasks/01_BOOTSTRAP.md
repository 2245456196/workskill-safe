# Task 01 — Bootstrap the Python Project

## Goal

Create a clean Python 3.11+ open-source project without implementing the full feature set yet.

## Required work

- Add `pyproject.toml`.
- Create `src/workskill_safe/` and `tests/`.
- Add a minimal CLI with `--help`.
- Add `.gitignore` and `.pre-commit-config.yaml`.
- Add MIT `LICENSE`.
- Add `CONTRIBUTING.md`, `SECURITY.md`, `GOVERNANCE.md`, `ROADMAP.md`, `CHANGELOG.md`, and `CODE_OF_CONDUCT.md`.
- Add development dependencies for pytest, ruff, and mypy.
- Preserve the privacy boundary defined in `PRIVACY.md`.

## `.gitignore` minimum

```text
.venv/
venv/
__pycache__/
.pytest_cache/
.mypy_cache/
.ruff_cache/
dist/
build/
*.egg-info/
.env
.env.*
.workskill-safe/
private/
raw/
output/
audit/
*.key
*.pem
```

## Acceptance criteria

- Editable install succeeds.
- Package imports.
- CLI help succeeds.
- A minimal test passes.
- No network dependency is required.
- Documentation accurately marks the project as pre-release.

## Suggested branch and PR

- Branch: `chore/bootstrap-python-project`
- PR: `Bootstrap privacy-first Python CLI project`
