# Architecture

```text
Input Reader
    ↓
Rule Loader
    ↓
Scanner
    ↓
Findings
    ↓
Sanitizer + Masked Audit
    ↓
Human Review Gate
    ↓
Skill Scaffolder
    ↓
Skill Validator
```

| Module | Responsibility |
|---|---|
| `cli.py` | command parsing and exit codes |
| `models.py` | findings, rules, reports, validation result |
| `rules.py` | load and validate YAML rules |
| `scanner.py` | deterministic pattern matching |
| `sanitizer.py` | typed replacements and masked audit output |
| `scaffolder.py` | Agent Skill directory generation |
| `validator.py` | structure, metadata, and privacy checks |

Core modules contain no HTTP client and make no network request.
