# Threat Model

## Assets

Private work notes, employer and client confidentiality, personal information, authentication material, unpublished business logic, and generated public Agent Skills.

## Main threats

- direct identifier leakage
- authentication-material leakage
- contextual re-identification
- accidental commit of raw input
- false confidence after automated scanning
- malformed or missing rules
- audit log leakage
- hidden network transmission

## Controls

- deterministic rules
- critical severity for high-risk patterns
- typed replacements
- masked audit output
- basename-only audit paths
- fail-closed rule loading
- human review gate
- critical-placeholder block
- synthetic fixtures
- no-network source guard
- CI and secret scanning

## Residual risk

No deterministic scanner fully understands organizational context. Publication decisions remain the maintainer's responsibility.
