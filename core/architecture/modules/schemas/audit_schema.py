"""
audit_schema.py – core/architecture/modules/schemas

🎯 Purpose:
Defines the institutional schema for audit logs in FINSIG.
Audit logs ensure:
- Traceability of actions across modules
- Accountability of users and systems
- Compliance with institutional and regulatory requirements
- Standardized format for multilingual documentation (FR/EN/ES)

✅ Impact:
Guarantees reliable, auditable, and standardized tracking of events.
"""

from typing import Optional, Dict
from pydantic import BaseModel, Field, validator
import datetime


class AuditRecord(BaseModel):
    """
    Institutional Audit Record Schema for FINSIG.
    """

    id: str = Field(..., description="Unique identifier for the audit record")
    timestamp: datetime.datetime = Field(..., description="ISO 8601 timestamp of the action")
    actor: str = Field(..., description="User or system initiating the action")
    action: str = Field(..., description="Action performed (create, update, delete, validate, etc.)")
    module: str = Field(..., description="Module where the action occurred (collection, normalization, conformity, orchestration, schemas)")
    status: str = Field(..., description="Result of the action (success, failure, warning)")
    details: Optional[Dict] = Field(default_factory=dict, description="Additional contextual information about the action")

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
            raise ValueError("Audit record ID cannot be empty.")
        return v

    @validator("status")
    def validate_status(cls, v):
        """
        Ensure status is one of the allowed values.
        """
        allowed = {"success", "failure", "warning"}
        if v.lower() not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return v.lower()


# Example usage
if __name__ == "__main__":
    try:
        record = AuditRecord(
            id="AUD-001",
            timestamp="2025-12-17T18:45:00",
            actor="system",
            action="validate",
            module="conformity",
            status="success",
            details={"file": "README_TECHNIQUE_FR.md", "message": "Validation passed"}
        )
        print("✅ Valid audit record:", record.dict())
    except Exception as e:
        print("⚠️ Validation error:", e)
