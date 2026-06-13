# Codex Handoff

## Current state

ChatGPT has already completed the project specification, bilingual documentation, initial Python implementation, tests, GitHub templates, and CI configuration.

Codex should not rebuild the project from scratch.

## Codex role

Use Codex only for targeted work after reviewing a specific Issue or failed check:

- diagnose GitHub Actions failures
- fix test, lint, typing, or packaging problems
- add narrowly scoped privacy regression cases
- review edge cases
- improve implementation without changing the privacy boundary

## Read first

1. `AGENTS.md`
2. `PRIVACY.md`
3. the assigned GitHub Issue
4. relevant source and tests
5. `docs/zh-TW/MAINTAINER_GUIDE.md` when maintainer context is needed

## Restrictions

- Synthetic fixtures only.
- No external model or service in core commands.
- No telemetry or cloud processing.
- Do not publish a Release.
- Do not submit the OpenAI application.
- Do not make broad rewrites when a targeted fix is sufficient.

## Required report

For every task, provide changed files, test results, privacy impact, remaining risk, and the pull request link.
