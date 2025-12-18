"""
traceability.py – core/architecture/modules/traceability

🎯 Purpose:
Defines the institutional traceability engine for FINSIG.
The traceability engine ensures:
- Logging of all institutional actions (collection, normalization, conformity, scoring, storage)
- Standardized format with unique ID, timestamp, module, action, and metadata
- Auditability and reproducibility of institutional workflows
- Extensibility for integration with compliance and reporting pipelines

✅ Impact:
Guarantees reliable, auditable, and standardized traceability across all modules.
"""

import os
import json
import uuid
import datetime
from typing import Dict, Any, Optional


class TraceRecord:
    """
    Institutional Traceability Record Schema for FINSIG.
    """

    def __init__(self, module: str, action: str, metadata: Optional[Dict[str, Any]] = None):
        self.id = str(uuid.uuid4())
        self.timestamp = datetime.datetime.now().isoformat()
        self.module = module
        self.action = action
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "module": self.module,
            "action": self.action,
            "metadata": self.metadata,
        }


class TraceabilityManager:
    """
    Institutional Traceability Manager for FINSIG.
    """

    def __init__(self, log_path: str = "./logs/traceability_log.json"):
        self.log_path = log_path
        os.makedirs(os.path.dirname(self.log_path), exist_ok=True)
        if not os.path.exists(self.log_path):
            with open(self.log_path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def log(self, record: TraceRecord) -> None:
        """
        Append a traceability record to the log file.
        """
        with open(self.log_path, "r+", encoding="utf-8") as f:
            data = json.load(f)
            data.append(record.to_dict())
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)

    def list_records(self) -> Dict[str, Any]:
        """
        List all traceability records.
        """
        with open(self.log_path, "r", encoding="utf-8") as f:
            return {"records": json.load(f)}

    def filter_by_module(self, module: str) -> Dict[str, Any]:
        """
        Filter records by module.
        """
        with open(self.log_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            filtered = [rec for rec in data if rec.get("module") == module]
            return {"records": filtered}

    def clear(self) -> None:
        """
        Clear all traceability records.
        """
        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump([], f)


# Example usage
if __name__ == "__main__":
    manager = TraceabilityManager()

    # Create and log a record
    record = TraceRecord(
        module="scoring",
        action="calculate_score",
        metadata={"record_id": "SCORE-001", "category": "risk", "value": 85}
    )
    manager.log(record)
    print("✅ Traceability record logged.")

    # List all records
    print("📋 All records:", manager.list_records())

    # Filter by module
    print("🔎 Records for scoring:", manager.filter_by_module("scoring"))

    # Clear records (for reset)
    # manager.clear()
    # print("🗑️ Traceability log cleared.")
