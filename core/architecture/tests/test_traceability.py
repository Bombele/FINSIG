import os
import csv
import pytest
from core.architecture.modules.traceability.traceability import Traceability


def test_log_event_creates_entry_with_utc_timestamp():
    trace = Traceability()
    trace.log_event("collection", "start", {"source": "API"})
    assert len(trace.logs) == 1
    entry = trace.logs[0]
    # Vérifie que le timestamp est bien en UTC ISO 8601
    assert entry["timestamp"].endswith("Z")
    assert "T" in entry["timestamp"]


def test_log_event_with_empty_metadata():
    trace = Traceability()
    trace.log_event("normalization", "done")
    entry = trace.logs[0]
    assert isinstance(entry["metadata"], dict)
    assert entry["metadata"] == {}


def test_export_to_csv_creates_file(tmp_path):
    trace = Traceability()
    trace.log_event("audit", "validate", {"records": 10})
    filepath = tmp_path / "traceability_log.csv"
    trace.export_to_csv(str(filepath))

    assert filepath.exists()

    # Vérifie que le fichier contient bien les colonnes attendues
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        assert len(rows) == 1
        assert "timestamp" in rows[0]
        assert rows[0]["module"] == "audit"
        assert rows[0]["action"] == "validate"


def test_export_to_csv_with_no_logs(tmp_path, capsys):
    trace = Traceability()
    filepath = tmp_path / "empty_log.csv"
    trace.export_to_csv(str(filepath))
    captured = capsys.readouterr()
    assert "Aucun log à exporter" in captured.out
    assert not filepath.exists()