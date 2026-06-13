# Release Checklist

## Code

- [ ] `python -m pytest` passes
- [ ] `ruff check .` passes
- [ ] `mypy src` passes
- [ ] `workskill-safe demo` passes
- [ ] package build passes

## Privacy

- [ ] synthetic fixtures only
- [ ] no private paths or URLs
- [ ] audit reports do not expose full values
- [ ] privacy and threat-model documents are current
- [ ] final repository scan completed

## GitHub

- [ ] Issue linked
- [ ] PR reviewed
- [ ] CI green
- [ ] changelog updated
- [ ] explicit maintainer approval received
