"""
data_normalization.py – core/architecture/modules/normalization

🎯 Purpose:
This module standardizes and normalizes raw data collected in FINSIG.
It ensures:
- Consistent formats (dates, numbers, strings)
- Removal of duplicates and invalid entries
- Enforcement of mandatory fields
- Preparation of clean datasets for compliance, scoring, and audit modules

✅ Impact:
Guarantees reliable, auditable, and institutionally compliant data pipelines.
"""

import datetime
from typing import List, Dict, Any

MANDATORY_FIELDS = ["id", "timestamp", "source"]

class DataNormalizer:
    """
    Institutional Data Normalizer for FINSIG.
    """

    def __init__(self, data: List[Dict[str, Any]]):
        self.data = data

    def normalize_dates(self, field: str = "timestamp") -> None:
        """
        Normalize date fields to ISO 8601 format.
        """
        for record in self.data:
            if field in record:
                try:
                    record[field] = datetime.datetime.fromisoformat(str(record[field])).isoformat()
                except Exception:
                    record[field] = None  # mark invalid dates

    def normalize_strings(self, fields: List[str]) -> None:
        """
        Normalize string fields (strip spaces, lowercase).
        """
        for record in self.data:
            for field in fields:
                if field in record and isinstance(record[field], str):
                    record[field] = record[field].strip().lower()

    def normalize_numbers(self, fields: List[str]) -> None:
        """
        Normalize numeric fields (convert to float).
        """
        for record in self.data:
            for field in fields:
                if field in record:
                    try:
                        record[field] = float(record[field])
                    except Exception:
                        record[field] = None

    def enforce_mandatory_fields(self) -> List[Dict[str, Any]]:
        """
        Ensure mandatory fields exist in each record.
        """
        normalized = []
        for record in self.data:
            if all(field in record and record[field] is not None for field in MANDATORY_FIELDS):
                normalized.append(record)
        self.data = normalized
        return self.data

    def remove_duplicates(self) -> None:
        """
        Remove duplicate records based on 'id'.
        """
        seen = set()
        unique = []
        for record in self.data:
            if record["id"] not in seen:
                unique.append(record)
                seen.add(record["id"])
        self.data = unique

    def run_full_normalization(self) -> List[Dict[str, Any]]:
        """
        Execute the full normalization pipeline.
        """
        self.normalize_dates()
        self.normalize_strings(["source"])
        self.enforce_mandatory_fields()
        self.remove_duplicates()
        return self.data


# Example usage
if __name__ == "__main__":
    sample_data = [
        {"id": "001", "timestamp": "2025-12-17 15:30", "source": " API ", "value": "100"},
        {"id": "001", "timestamp": "2025-12-17 15:30", "source": " api ", "value": "100"},
        {"id": "002", "timestamp": "2025-12-17T15:45:00", "source": "CSV", "value": "200"},
        {"id": None, "timestamp": "invalid_date", "source": "json", "value": "300"},
    ]

    normalizer = DataNormalizer(sample_data)
    clean_data = normalizer.run_full_normalization()
    print("✅ Normalized Data:", clean_data)
