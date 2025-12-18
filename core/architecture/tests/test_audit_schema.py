import pytest
from core.architecture.modules.schemas.audit_schema import AuditSchema
from core.architecture.conformity.structure_validator import validate_audit_schema


def test_audit_schema_signature_valid():
    audit = AuditSchema(
        id="AUD-001",
        timestamp="2025-12-18T10:00:00Z",
        actor="system",
        action="create",
        details={"records": 5},
        version="1.0"
    )
    audit.generate_signature()
    assert validate_audit_schema(audit) is True


def test_audit_schema_signature_invalid():
    audit = AuditSchema(
        id="AUD-002",
        timestamp="2025-12-18T10:05:00Z",
        actor="system",
        action="update",
        details={"records": 10},
        version="1.0",
        signature="wrong_signature"
    )
    with pytest.raises(ValueError):
        validate_audit_schema(audit)