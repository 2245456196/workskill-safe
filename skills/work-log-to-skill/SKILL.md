---
name: work-log-to-skill
description: >-
  Convert a sanitized and human-reviewed work note into a reusable Agent Skill draft.
  Use only after privacy scanning. Do not use on raw employer, client, personal,
  regulated, authentication-bearing, or confidential material.
---

# Work Log to Skill

## Purpose

Extract a repeatable method from sanitized work material without retaining case-specific facts.

## Preconditions

- The input passed privacy scanning.
- A human reviewed the sanitized content.
- The output is a reusable method, not a summary of private facts.

## Workflow

1. Identify the repeatable objective.
2. Separate procedural knowledge from case-specific facts.
3. Define trigger and non-trigger conditions.
4. List required inputs.
5. Convert the method into ordered steps.
6. Define the output contract.
7. Add privacy guardrails.
8. Test with a synthetic example.

## When not to use

Do not use on raw company, client, personal, authentication, private-link, or confidential data.

## Privacy guardrails

Stop when identifying context, private paths, links, authentication material, or authorization uncertainty remains.

## Validation checklist

- [ ] Reusable beyond the original case
- [ ] No source-specific identifiers
- [ ] Clear trigger and non-trigger conditions
- [ ] Testable output
- [ ] Synthetic verification completed
