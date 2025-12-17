"""
compliance_schema.py – core/architecture/modules/schemas

🎯 Purpose:
Defines the institutional schema for compliance validations in FINSIG.
Compliance records ensure:
- Verification of data/document conformity with institutional and regulatory standards
- Traceability of validation processes
- Standardized reporting for audits and scoring
- Multilingual readiness (FR/EN/ES)

✅ Impact:
Guarantees reliable, auditable, and standardized compliance checks across modules.
"""

from typing import Optional, Dict
from pydantic import BaseModel, Field, validator
import datetime


class ComplianceRecord(BaseModel):
    """
    Institutional Compliance Record Schema for FINSIG.
    """

    id: str = Field(..., description="Unique identifier for the compliance record")
    timestamp: datetime.datetime = Field(..., description="ISO 8601 timestamp of the compliance check")
    validator: str = Field(..., description="User or system performing the compliance validation")
    module: str = Field(..., description="Module where the compliance check occurred (collection, normalization, orchestration, etc.)")
    rule: str = Field(..., description="Compliance rule or regulation applied")
    status: str = Field(..., description="Result of the compliance check (passed, failed, warning)")
    details: Optional[Dict] = Field(default_factory=dict, description="Additional contextual information about the compliance check")

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
            raise ValueError("Compliance record ID cannot be empty.")
        return v

    @validator("status")
    def validate_status(cls, v):
        """
        Ensure status is one of the allowed values.
        """
        allowed = {"passed", "failed", "warning"}
        if v.lower() not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return v.lower()


# Example usage
if __name__ == "__main__":
    try:
        record = ComplianceRecord(
            id="COMP-001",
            timestamp="2025-12-17T18:50:00",
            validator="system",
            module="normalization",
            rule="ISO-8601 timestamp validation",
            status="passed",
            details={"field": "timestamp", "message": "Value conforms to ISO 8601"}
        )
        print("✅ Valid compliance record:", record.dict())
    except Exception as e:
        print("⚠️ Validation error:", e)
