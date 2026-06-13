from workskill_safe.models import Rule, Severity
from workskill_safe.scanner import scan_text


def test_custom_high_risk_rule_is_critical() -> None:
    rule = Rule(
        rule_id="synthetic-critical",
        category="synthetic",
        severity=Severity.CRITICAL,
        pattern="SYNTHETIC_CRITICAL_MARKER",
        replacement="[REMOVED]",
        message="Synthetic critical rule for testing.",
    )
    findings = scan_text("SYNTHETIC_CRITICAL_MARKER\n", (rule,))
    assert any(item.severity == Severity.CRITICAL for item in findings)
