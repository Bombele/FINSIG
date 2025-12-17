"""
finance_schema.py – core/architecture/modules/schemas

🎯 Purpose:
Defines the institutional schema for financial transactions in FINSIG.
Financial records ensure:
- Standardized representation of transactions
- Compliance with institutional and regulatory requirements
- Traceability for audit and scoring modules
- Multilingual readiness (FR/EN/ES)

✅ Impact:
Guarantees reliable, auditable, and standardized financial data pipelines.
"""

from typing import Optional, Dict
from pydantic import BaseModel, Field, validator
import datetime


class FinanceRecord(BaseModel):
    """
    Institutional Finance Record Schema for FINSIG.
    """

    id: str = Field(..., description="Unique identifier for the financial transaction")
    timestamp: datetime.datetime = Field(..., description="ISO 8601 timestamp of the transaction")
    amount: float = Field(..., description="Transaction amount in numeric format")
    currency: str = Field(..., description="Currency code (ISO 4217 standard, e.g., USD, EUR, CDF)")
    sender: str = Field(..., description="Entity initiating the transaction")
    receiver: str = Field(..., description="Entity receiving the transaction")
    type: str = Field(..., description="Transaction type (payment, transfer, refund, etc.)")
    status: str = Field(..., description="Transaction status (pending, completed, failed)")
    metadata: Optional[Dict] = Field(default_factory=dict, description="Additional contextual information")

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
            raise ValueError("Finance record ID cannot be empty.")
        return v

    @validator("currency")
    def validate_currency(cls, v):
        """
        Ensure currency code is uppercase and length is 3 (ISO 4217).
        """
        if not v or len(v) != 3:
            raise ValueError("Currency must be a 3-letter ISO 4217 code.")
        return v.upper()

    @validator("status")
    def validate_status(cls, v):
        """
        Ensure status is one of the allowed values.
        """
        allowed = {"pending", "completed", "failed"}
        if v.lower() not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return v.lower()


# Example usage
if __name__ == "__main__":
    try:
        record = FinanceRecord(
            id="FIN-001",
            timestamp="2025-12-17T18:55:00",
            amount=2500.75,
            currency="USD",
            sender="Bank_A",
            receiver="Client_X",
            type="transfer",
            status="completed",
            metadata={"region": "RDC", "compliance": "AML/KYC validated"}
        )
        print("✅ Valid finance record:", record.dict())
    except Exception as e:
        print("⚠️ Validation error:", e)
