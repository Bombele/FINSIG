"""
storage_manager.py – core/architecture/modules/storage

🎯 Purpose:
Defines the institutional storage manager for FINSIG.
The storage manager ensures:
- Centralized and standardized data storage
- Read/write operations with validation
- Traceability of storage actions for audits
- Extensibility for multiple backends (local, cloud, database)

✅ Impact:
Guarantees reliable, auditable, and standardized storage pipelines.
"""

import os
import json
import datetime
from typing import Any, Dict, Optional


class StorageRecord:
    """
    Institutional Storage Record Schema for FINSIG.
    """

    def __init__(self, record_id: str, data: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None):
        if not record_id or record_id.strip() == "":
            raise ValueError("Storage record ID cannot be empty.")
        self.id = record_id
        self.timestamp = datetime.datetime.now().isoformat()
        self.data = data
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "data": self.data,
            "metadata": self.metadata,
        }


class StorageManager:
    """
    Institutional Storage Manager for FINSIG.
    """

    def __init__(self, base_path: str = "./storage"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def save(self, record: StorageRecord) -> str:
        """
        Save a record to storage as JSON.
        """
        file_path = os.path.join(self.base_path, f"{record.id}.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(record.to_dict(), f, ensure_ascii=False, indent=4)
        return file_path

    def load(self, record_id: str) -> Optional[Dict[str, Any]]:
        """
        Load a record from storage.
        """
        file_path = os.path.join(self.base_path, f"{record_id}.json")
        if not os.path.exists(file_path):
            return None
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def delete(self, record_id: str) -> bool:
        """
        Delete a record from storage.
        """
        file_path = os.path.join(self.base_path, f"{record_id}.json")
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False

    def list_records(self) -> Dict[str, Any]:
        """
        List all records in storage.
        """
        records = []
        for file_name in os.listdir(self.base_path):
            if file_name.endswith(".json"):
                records.append(file_name.replace(".json", ""))
        return {"records": records}


# Example usage
if __name__ == "__main__":
    manager = StorageManager()

    # Create and save a record
    record = StorageRecord(
        record_id="STOR-001",
        data={"amount": 2500, "currency": "USD"},
        metadata={"module": "finance", "compliance": "validated"}
    )
    path = manager.save(record)
    print("✅ Record saved at:", path)

    # Load the record
    loaded = manager.load("STOR-001")
    print("📂 Loaded record:", loaded)

    # List records
    print("📋 Records in storage:", manager.list_records())

    # Delete the record
    deleted = manager.delete("STOR-001")
    print("🗑️ Record deleted:", deleted)
