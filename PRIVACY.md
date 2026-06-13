# Privacy Policy and Data Boundary

## Core rule

The public repository stores only source code, public documentation, generic rules, synthetic fixtures, aggregate maintenance evidence, and manually approved non-identifying examples.

Raw work material must remain in a private local workspace.

## Prohibited public content

- employer or client documents
- meeting notes from real projects
- customer, partner, employee, family, health, or financial data
- pricing, cost, margin, contract, negotiation, KPI, roadmap, or sales data that is not public
- internal URLs, document links, chat groups, repository names, hostnames, IP addresses, or private file paths
- names, email addresses, phone numbers, addresses, birthdays, identifiers, account numbers, or precise locations
- API keys, access tokens, passwords, cookies, SSH keys, OAuth secrets, certificates, or `.env` files

## Allowed public content

- source code
- generic workflow descriptions
- fully synthetic test cases
- generic detection and redaction rules
- aggregate pilot metrics that cannot identify a person, organization, project, or event
- manually reviewed examples that cannot be re-identified

## Data classification

| Class | Meaning | Public repository |
|---|---|---|
| PUBLIC | Already public and licensed | Allowed |
| SYNTHETIC | Completely fabricated for testing | Allowed |
| SANITIZED | Transformed and manually reviewed | Limited |
| INTERNAL | Private operational information | Prohibited |
| CONFIDENTIAL | Business, client, or personal information | Prohibited |
| SECRET | Authentication or credential material | Never allowed |

When classification is uncertain, treat the material as `CONFIDENTIAL`.

## Fail-closed conditions

The tool must refuse downstream Skill generation when:

- a likely secret is detected
- a rule file is missing or invalid
- human approval has not been recorded
- output contains an absolute private path
- output contains confidentiality markers or unresolved sensitive findings

## Human review

Automated sanitization is not proof of anonymity. Reviewers must also consider contextual re-identification from combinations of industry, date, location, amount, role, and unusual workflow details.

## No guarantee

WorkSkill Safe does not guarantee anonymization, compliance, legal authorization, or prevention of every disclosure. Publication remains the user's responsibility.
