# Pilot 01 Result — Proposal Workflow

## Scope

This pilot uses a fully synthetic scenario derived from recurring proposal-work patterns: requirement framing, stakeholder analysis, MVP selection, commercial assumptions, evidence gaps, reviewer objections, and slide planning.

No real organization, customer, person, project, amount, date, link, or internal document is included.

## Pipeline result

| Check | Result |
|---|---|
| Source lines | 128 |
| Findings detected | 5 |
| Finding categories | marker, email, phone, URL, path |
| Sanitization | Passed |
| Skill generation | Passed |
| Skill validation | Passed |
| Remaining formatted findings | 0 |
| Second synthetic case | Passed |

## What the pilot demonstrated

1. Fragmented proposal notes can be converted into a repeatable decision workflow.
2. Stakeholder needs, solution scope, MVP, commercial assumptions, and evidence can be separated.
3. Unsupported claims can be marked as assumptions or pending validation.
4. Reviewer objections can drive structural changes instead of wording-only edits.
5. The same workflow can be applied to a different synthetic proposal case.

## Gaps found

1. Pattern scanning cannot detect contextual re-identification created by combinations of industry, time, value, location, role, and unusual process details.
2. Proposal outputs need a fixed schema to make cases comparable.
3. The second-case result needs an automated structural test.

## Follow-up issues

- #14 Contextual re-identification checklist
- #15 Fixed proposal output schema
- #16 Structural test for proposal workflow

## Decision

- Keep the proposal workflow Skill.
- Complete Issues #14–#16 before the first release.
- Publish only synthetic examples and aggregate results.
