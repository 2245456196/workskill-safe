# Threat Model

## Assets

- private work notes
- employer and client confidentiality
- personal information
- credentials
- unpublished business logic
- generated public Agent Skills

## Threats and mitigations

### Direct identifier leakage

Examples: names, emails, phone numbers, URLs, and account identifiers.

Mitigations: deterministic patterns, private forbidden-term rules, typed replacements, and final validation.

### Secret leakage

Examples: API keys, tokens, passwords, cookies, and private keys.

Mitigations: critical severity, fail-closed behavior, masked reports, tests, pre-commit controls, and CI secret scanning.

### Contextual re-identification

A text may omit names but still reveal the organization or project through a unique combination of industry, date, amount, location, role, and workflow.

Mitigations: generalize dates and numbers, remove distinctive context, use placeholders, require human review, and keep public examples fully synthetic.

### Raw input accidentally committed

Mitigations: dedicated private workspace, strict `.gitignore`, pre-commit checks, CI scanning, and documentation.

### False confidence

Users may interpret a successful scan as a guarantee of safety.

Mitigations: explicit warnings, no compliance claim, human approval, and conservative exit behavior.

### Missing or malformed rule configuration

Mitigations: configuration validation, fail closed, and regression tests.

### Audit log leakage

Mitigations: never store full secret values, use masked previews, write locally, and ignore audit output by default.

### Hidden network transmission

Mitigations: no network dependencies in core modules and automated tests that guard against network access.

## Trust boundaries

- Input files are untrusted.
- Configuration files may be malformed.
- Generated output is not automatically safe.
- Human approval is required before publication.
- Public repository fixtures must remain synthetic.

## Residual risk

No deterministic scanner can fully understand organizational context or all re-identification risks. Publication decisions remain the user's responsibility.
