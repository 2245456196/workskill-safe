# Privacy Policy and Data Boundary

Traditional Chinese guidance: `docs/zh-TW/PRIVACY_GUIDE.md`.

## Core rule

The public repository stores only source code, public documentation, generic rules, synthetic fixtures, aggregate maintenance evidence, and manually approved non-identifying examples.

Raw work material must remain in a private local workspace.

## Prohibited public content

- employer or client documents
- meeting notes from real projects
- customer, partner, employee, family, health, or financial data
- pricing, cost, margin, contract, negotiation, KPI, roadmap, or unpublished sales data
- internal URLs, document links, chat groups, repository names, hostnames, IP addresses, or private file paths
- names, emails, phone numbers, addresses, birthdays, identifiers, account numbers, or precise locations
- authentication material or local configuration secrets

## Fail-closed conditions

The tool must refuse downstream Skill generation when a likely secret remains, rule configuration is missing or invalid, human approval has not been recorded, a private absolute path remains, or unresolved confidentiality findings remain.

## No guarantee

Automated sanitization is not proof of anonymity. WorkSkill Safe does not guarantee anonymization, compliance, legal authorization, or prevention of every disclosure.
