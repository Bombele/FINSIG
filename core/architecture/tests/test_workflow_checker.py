"""
test_workflow_checker.py – core/architecture/tests

🎯 Purpose:
Unit tests for the institutional workflow checker of FINSIG.
Ensures that:
- Workflow sequences are validated correctly
- Mandatory steps are present and in the right order
- Invalid workflows raise errors
- Valid workflows pass successfully

✅ Impact:
Guarantees institutional reliability, reproducibility, and conformity of operational workflows.
"""

import pytest
from core.architecture.modules.conformity.workflow_checker import WorkflowChecker


# -----------------------------
# 🔧 Fixtures
# -----------------------------

@pytest.fixture
def checker():
    # Institutional workflow sequence: collection → normalization → conformity → scoring → storage → traceability
    return WorkflowChecker(
        required_sequence=[
            "collection",
            "normalization",
            "conformity",
            "scoring",
            "storage",
            "traceability"
        ]
    )


@pytest.fixture
def valid_workflow():
    return [
        {"step": "collection", "status": "done"},
        {"step": "normalization", "status": "done"},
        {"step": "conformity", "status": "done"},
        {"step": "scoring", "status": "done"},
        {"step": "storage", "status": "done"},
        {"step": "traceability", "status": "done"},
    ]


@pytest.fixture
def invalid_workflow_missing_step():
    return [
        {"step": "collection", "status": "done"},
        {"step": "normalization", "status": "done"},
        # Missing conformity
        {"step": "scoring", "status": "done"},
        {"step": "storage", "status": "done"},
        {"step": "traceability", "status": "done"},
    ]


@pytest.fixture
def invalid_workflow_wrong_order():
    return [
        {"step": "collection", "status": "done"},
        {"step": "scoring", "status": "done"},  # Wrong order
        {"step": "normalization", "status": "done"},
        {"step": "conformity", "status": "done"},
        {"step": "storage", "status": "done"},
        {"step": "traceability", "status": "done"},
    ]


# -----------------------------
# ✅ Tests
# -----------------------------

def test_valid_workflow_passes(checker, valid_workflow):
    """
    Ensure a valid workflow passes validation.
    """
    assert checker.validate_sequence(valid_workflow) is True


def test_missing_step_raises_error(checker, invalid_workflow_missing_step):
    """
    Ensure missing mandatory step raises ValueError.
    """
    with pytest.raises(ValueError) as excinfo:
        checker.validate_sequence(invalid_workflow_missing_step)
    assert "conformity" in str(excinfo.value)


def test_wrong_order_raises_error(checker, invalid_workflow_wrong_order):
    """
    Ensure wrong order raises ValueError.
    """
    with pytest.raises(ValueError) as excinfo:
        checker.validate_sequence(invalid_workflow_wrong_order)
    assert "order" in str(excinfo.value).lower()


def test_bulk_validation(checker, valid_workflow, invalid_workflow_missing_step):
    """
    Ensure bulk validation works and returns results for each workflow.
    """
    workflows = [valid_workflow, invalid_workflow_missing_step]
    results = checker.bulk_validate(workflows)
    assert isinstance(results, list)
    assert results[0]["status"] == "valid"
    assert results[1]["status"] == "invalid"


def test_partial_workflow(checker):
    """
    Ensure partial workflows are flagged as invalid.
    """
    partial = [{"step": "collection", "status": "done"}]
    with pytest.raises(ValueError):
        checker.validate_sequence(partial)
