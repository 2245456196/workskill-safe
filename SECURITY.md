# Security Policy

## Supported versions

Until a stable release, only the latest published version is supported.

## Reporting vulnerabilities

Do not open a public Issue containing secrets, authentication material, personal data, private URLs, real confidential documents, or exploit details that would expose users.

Use GitHub private vulnerability reporting when enabled. If it is unavailable, use the private contact method listed on the maintainer's GitHub profile.

## Security model

Core commands operate locally and do not require network access. Controls include deterministic scanning, fail-closed behavior, masked audit reports, human approval, synthetic fixtures, and CI checks.

## Limitation

Pattern matching cannot detect every contextual secret or re-identification risk. Users remain responsible for authorization and final review before publication.
