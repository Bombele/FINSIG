"""
test_pipeline_orchestrator.py – core/architecture/tests

🎯 Purpose:
Unit tests for the institutional pipeline orchestrator of FINSIG.
Ensures that:
- Each module (collection, normalization, conformity, scoring, storage, traceability) is invoked correctly
- Data flows consistently through the pipeline
- Errors are handled gracefully
- Traceability records are generated

✅ Impact:
Guarantees reliability, reproducibility, and auditability of the institutional pipeline.
"""

import pytest
import json
from core.architecture.modules.orchestration.pipeline_orchestrator import PipelineOrchestrator
from core.architecture.modules.utils import utils


# -----------------------------
# 🔧 Fixtures
# -----------------------------

@pytest.fixture
def sample_data():
    return [
        {"id": "TX-001", "amount": 100, "currency": "USD"},
        {"id": "TX-002", "amount": 200, "currency": "EUR"},
    ]


@pytest.fixture
def orchestrator(tmp_path):
    log_path = tmp_path / "traceability_log.json"
    return PipelineOrchestrator(trace_log_path=str(log_path))


# -----------------------------
# ✅ Tests
# -----------------------------

def test_pipeline_runs_successfully(orchestrator, sample_data):
    """
    Ensure the pipeline runs end-to-end without errors.
    """
    result = orchestrator.run_pipeline(sample_data)
    assert isinstance(result, dict)
    assert "normalized" in result
    assert "scored" in result
    assert "stored" in result
    assert "traceability" in result


def test_normalization(orchestrator, sample_data):
    """
    Ensure normalization produces consistent output.
    """
    result = orchestrator.normalize(sample_data)
    for record in result:
        assert "id" in record
        assert isinstance(record["amount"], (int, float))


def test_conformity(orchestrator, sample_data):
    """
    Ensure conformity validation catches missing fields.
    """
    invalid_data = [{"amount": 50}]  # missing 'id'
    with pytest.raises(ValueError):
        orchestrator.validate_conformity(invalid_data)


def test_scoring(orchestrator, sample_data):
    """
    Ensure scoring assigns a risk/compliance score.
    """
    result = orchestrator.score(sample_data)
    for record in result:
        assert "score" in record
        assert isinstance(record["score"], (int, float))


def test_storage(orchestrator, sample_data, tmp_path):
    """
    Ensure storage saves and retrieves records.
    """
    storage_file = tmp_path / "storage.json"
    orchestrator.store(sample_data, str(storage_file))
    with open(storage_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == len(sample_data)


def test_traceability(orchestrator, sample_data):
    """
    Ensure traceability records are generated.
    """
    orchestrator.run_pipeline(sample_data)
    records = orchestrator.trace_manager.list_records()["records"]
    assert len(records) > 0
    assert all("module" in rec for rec in records)


def test_utils_functions():
    """
    Ensure utils functions work as expected.
    """
    uid = utils.generate_id("TEST")
    assert uid.startswith("TEST-")

    ts = utils.current_timestamp()
    assert "T" in ts  # ISO format

    merged = utils.merge_dicts({"a": 1}, {"b": 2})
    assert merged["a"] == 1 and merged["b"] == 2

    json_str = utils.to_json({"x": 1})
    assert isinstance(json_str, str)
    parsed = utils.from_json(json_str)
    assert parsed["x"] == 1
