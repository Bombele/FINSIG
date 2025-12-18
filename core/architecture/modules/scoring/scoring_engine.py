"""
scoring_engine.py – core/architecture/modules/scoring

🎯 Purpose:
Defines the institutional scoring engine for FINSIG.
The scoring engine ensures:
- Calculation of compliance, risk, and performance scores
- Integration with normalized and validated data
- Traceability of scoring logic for audits
- Standardized outputs for institutional decision-making

✅ Impact:
Guarantees reliable, auditable, and standardized scoring pipelines.
"""

from typing import Dict, Any
from pydantic import BaseModel, Field, validator
import datetime


class ScoringResult(BaseModel):
    """
    Institutional Scoring Result Schema for FINSIG.
    """

    id: str = Field(..., description="Unique identifier for the scoring record")
    timestamp: datetime.datetime = Field(..., description="ISO 8601 timestamp of the scoring operation")
    module: str = Field(..., description="Module where scoring was applied (finance, compliance, audit, etc.)")
    score: float = Field(..., description="Calculated score between 0 and 100")
    category: str = Field(..., description="Category of scoring (risk, compliance, performance)")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional contextual information")

    @validator("timestamp", pre=True)
    def validate_timestamp(cls, v):
        if isinstance(v, str):
            try:
                return datetime.datetime.fromisoformat(v)
            except Exception:
                raise ValueError("Invalid timestamp format. Must be ISO 8601.")
        return v

    @validator("score")
    def validate_score(cls, v):
        if v < 0 or v > 100:
            raise ValueError("Score must be between 0 and 100.")
        return round(v, 2)


class ScoringEngine:
    """
    Institutional Scoring Engine for FINSIG.
    """

    def __init__(self):
        self.rules = {
            "risk": self._risk_score,
            "compliance": self._compliance_score,
            "performance": self._performance_score,
        }

    def calculate(self, record_id: str, module: str, category: str, data: Dict[str, Any]) -> ScoringResult:
        """
        Calculate a score based on category and input data.
        """
        if category not in self.rules:
            raise ValueError(f"Unknown scoring category: {category}")

        score = self.rules[category](data)
        result = ScoringResult(
            id=record_id,
            timestamp=datetime.datetime.now(),
            module=module,
            score=score,
            category=category,
            details=data,
        )
        return result

    def _risk_score(self, data: Dict[str, Any]) -> float:
        """
        Example risk scoring logic.
        """
        base = 50
        if data.get("amount", 0) > 10000:
            base += 20
        if data.get("country") in {"RDC", "Venezuela"}:
            base += 10
        return min(base, 100)

    def _compliance_score(self, data: Dict[str, Any]) -> float:
        """
        Example compliance scoring logic.
        """
        passed_rules = data.get("passed_rules", 0)
        total_rules = data.get("total_rules", 1)
        return (passed_rules / total_rules) * 100

    def _performance_score(self, data: Dict[str, Any]) -> float:
        """
        Example performance scoring logic.
        """
        tasks_completed = data.get("tasks_completed", 0)
        tasks_total = data.get("tasks_total", 1)
        return (tasks_completed / tasks_total) * 100


# Example usage
if __name__ == "__main__":
    engine = ScoringEngine()
    try:
        record = engine.calculate(
            record_id="SCORE-001",
            module="finance",
            category="risk",
            data={"amount": 15000, "country": "RDC"}
        )
        print("✅ Scoring result:", record.dict())
    except Exception as e:
        print("⚠️ Scoring error:", e)
