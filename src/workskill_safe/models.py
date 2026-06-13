from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
from pathlib import Path
from typing import Any


class Severity(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True)
class Rule:
    rule_id: str
    category: str
    severity: Severity
    pattern: str
    replacement: str
    message: str


@dataclass(frozen=True)
class Finding:
    rule_id: str
    category: str
    severity: Severity
    line: int
    start: int
    end: int
    masked_preview: str
    replacement: str
    message: str

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["severity"] = self.severity.value
        return data


@dataclass(frozen=True)
class ScanReport:
    source: Path
    findings: tuple[Finding, ...]

    @property
    def has_critical(self) -> bool:
        return any(item.severity == Severity.CRITICAL for item in self.findings)

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source.name,
            "finding_count": len(self.findings),
            "has_critical": self.has_critical,
            "findings": [item.to_dict() for item in self.findings],
        }


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    errors: tuple[str, ...]
    warnings: tuple[str, ...] = ()
