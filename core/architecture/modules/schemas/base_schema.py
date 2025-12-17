"""
base_schema.py – core/architecture/modules/schemas

🎯 Purpose:
Defines institutional data schemas for FINSIG.
Schemas ensure:
- Consistent structure across modules
- Validation of mandatory fields
- Compatibility with compliance and audit requirements
- Multilingual readiness (FR/EN/ES)

✅ Impact:
Guarantees reliable, auditable, and standardized data pipelines.
"""

from typing import Optional
from pydantic import BaseModel, Field, validator
import datetime


class InstitutionalRecord(BaseModel):
    """
    Base schema for institutional records in FINSIG.
    """

    id: str = Field(..., description="Unique identifier for the record")
    timestamp: datetime.datetime = Field(..., description="ISO 8601 timestamp of the record")
    source: str = Field(..., description="Origin of the data (CSV, JSON, API, etc.)")
    value: Optional[float] = Field(None, description="Numeric value associated with the record")
    metadata: Optional[dict] = Field(default_factory=dict, description="Additional contextual metadata")

    @validator("timestamp", pre=True)
    def validate_timestamp(cls, v):
        """
        Ensure timestamp is in ISO 8601 format.
        """
        if isinstance(v, str):
            try:
                return datetime.datetime.fromisoformat(v)
            except Exception:
                raise ValueError("Invalid timestamp format. Must be ISO 8601.")
        return v

    @validator("id")
    def validate_id(cls, v):
        """
        Ensure ID is not empty.
        """
        if not v or v.strip() == "":
            raise ValueError("ID cannot be empty.")
        return v

    @validator("source")
    def normalize_source(cls, v):
        """
        Normalize source string (lowercase, stripped).
        """
        return v.strip().lower()


# Example usage
if __name__ == "__main__":
    try:
        record = InstitutionalRecord(
            id="001",
            timestamp="2025-12-17T18:30:00",
            source="API",
            value=123.45,
            metadata={"country": "RDC", "language": "FR"}
        )
        print("✅ Valid record:", record.dict())
    except Exception as e:
        print("⚠️ Validation error:", e)