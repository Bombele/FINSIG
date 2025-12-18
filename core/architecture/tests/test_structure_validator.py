"""
test_structure_validator.py – core/architecture/tests

🎯 Purpose:
Unit tests for the institutional structure validator of FINSIG.
Ensures that:
- Documents comply with required institutional schema
- Mandatory fields are present
- Invalid structures raise errors
- Valid structures pass successfully

✅ Impact:
Guarantees conformity, reliability, and auditability of institutional documentation.
"""

import pytest
from core.architecture.modules.conformity.structure_validator import StructureValidator


# -----------------------------
# 🔧 Fixtures
# -----------------------------

@pytest.fixture
def validator():
    return StructureValidator(required_fields=["id", "timestamp", "module", "action"])


@pytest.fixture
def valid_document():
    return {
        "id": "DOC-001",
        "timestamp": "2025-12-18T10:00:00",
        "module": "scoring",
        "action": "calculate_score",
        "metadata": {"value": 85}
    }


@pytest.fixture
def invalid_document_missing_field():
    return {
        "id": "DOC-002",
        "timestamp": "2025-12-18T10:05:00",
        "action": "store_record"
        # Missing 'module'
    }


@pytest.fixture
def invalid_document_empty_field():
    return {
        "id": "",
        "timestamp": "2025-12-18T10:10:00",
        "module": "storage",
        "action": "save"
    }


# -----------------------------
# ✅ Tests
# -----------------------------

def test_valid_document_passes(validator, valid_document):
    """
    Ensure a valid document passes validation.
    """
    assert validator.validate(valid_document) is True


def test_missing_field_raises_error(validator, invalid_document_missing_field):
    """
    Ensure missing mandatory field raises ValueError.
    """
    with pytest.raises(ValueError) as excinfo:
        validator.validate(invalid_document_missing_field)
    assert "module" in str(excinfo.value)


def test_empty_field_raises_error(validator, invalid_document_empty_field):
    """
    Ensure empty mandatory field raises ValueError.
    """
    with pytest.raises(ValueError) as excinfo:
        validator.validate(invalid_document_empty_field)
    assert "id" in str(excinfo.value)


def test_bulk_validation(validator, valid_document, invalid_document_missing_field):
    """
    Ensure bulk validation works and returns results for each document.
    """
    documents = [valid_document, invalid_document_missing_field]
    results = validator.bulk_validate(documents)
    assert isinstance(results, list)
    assert results[0]["status"] == "valid"
    assert results[1]["status"] == "invalid"


def test_metadata_optional(validator, valid_document):
    """
    Ensure metadata is optional and does not block validation.
    """
    doc = valid_document.copy()
    doc.pop("metadata")
    assert validator.validate(doc) is True
