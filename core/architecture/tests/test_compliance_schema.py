import pytest
from core.architecture.modules.schemas.compliance_schema import ComplianceSchema
from core.architecture.conformity.structure_validator import validate_compliance_schema


def test_compliance_schema_signature_valid():
    compliance = ComplianceSchema(
        id="COMP-001",
        timestamp="2025-12-18T10:15:00Z",
        regulator="internal",
        status="valid",
        notes="All checks passed",
        version="1.0"
    )
    compliance.generate_signature()
    assert validate_compliance_schema(compliance) is True


def test_compliance_schema_signature_invalid():
    compliance = ComplianceSchema(
        id="COMP-002",
        timestamp="2025-12-18T10:20:00Z",
        regulator="internal",
        status="invalid",
        notes="Missing field",
        version="1.0",
        signature="wrong_signature"
    )
    with pytest.raises(ValueError):
        validate_compliance_schema(compliance)