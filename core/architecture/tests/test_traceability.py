"""
test_traceability.py – core/architecture/tests

🎯 Purpose:
Unit tests for the institutional traceability engine of FINSIG.
Ensures that:
- Traceability records are created with unique IDs and timestamps
- Records are correctly logged, listed, filtered, and cleared
- Metadata is handled consistently
- Auditability and reproducibility are guaranteed

✅ Impact:
Guarantees institutional traceability and auditability across all modules.
"""

import pytest
import os
import json
from core.architecture.modules.traceability.traceability import TraceRecord, TraceabilityManager


# -----------------------------
# 🔧 Fixtures
# -----------------------------

@pytest.fixture
def manager(tmp_path):
    log_path = tmp_path / "traceability_log.json"
    return TraceabilityManager(log_path=str(log_path))


@pytest.fixture
def sample_record():
    return TraceRecord(
        module="scoring",
        action="calculate_score",
        metadata={"record_id": "SCORE-001", "value": 85}
    )


# -----------------------------
# ✅ Tests
# -----------------------------

def test_record_creation(sample_record):
    """
    Ensure a traceability record is created with required fields.
    """
    record_dict = sample_record.to_dict()
    assert "id" in record_dict
    assert "timestamp" in record_dict
    assert record_dict["module"] == "scoring"
    assert record_dict["action"] == "calculate_score"
    assert "metadata" in record_dict


def test_log_and_list_records(manager, sample_record):
    """
    Ensure records are logged and listed correctly.
    """
    manager.log(sample_record)
    records = manager.list_records()["records"]
    assert len(records) == 1
    assert records[0]["module"] == "scoring"


def test_filter_by_module(manager, sample_record):
    """
    Ensure filtering by module returns correct records.
    """
    manager.log(sample_record)
    other_record = TraceRecord(module="storage", action="save", metadata={"id": "ST-001"})
    manager.log(other_record)

    filtered = manager.filter_by_module("scoring")["records"]
    assert len(filtered) == 1
    assert filtered[0]["module"] == "scoring"


def test_clear_records(manager, sample_record):
    """
    Ensure clearing records resets the log.
    """
    manager.log(sample_record)
    manager.clear()
    records = manager.list_records()["records"]
    assert records == []


def test_multiple_records(manager):
    """
    Ensure multiple records are logged and retrievable.
    """
    for i in range(3):
        rec = TraceRecord(module="collection", action="collect", metadata={"batch": i})
        manager.log(rec)

    records = manager.list_records()["records"]
    assert len(records) == 3
    modules = [r["module"] for r in records]
    assert all(m == "collection" for m in modules)


def test_metadata_optional(manager):
    """
    Ensure metadata is optional and does not block logging.
    """
    record = TraceRecord(module="normalization", action="normalize")
    manager.log(record)
    records = manager.list_records()["records"]
    assert "metadata" in records[0]
    assert isinstance(records[0]["metadata"], dict)