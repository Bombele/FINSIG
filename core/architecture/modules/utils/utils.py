"""
utils.py – core/architecture/modules/utils

🎯 Purpose:
Provides institutional utility functions for FINSIG.
These utilities ensure:
- Standardized identifiers
- Consistent timestamps
- Validation helpers
- JSON serialization/deserialization
- Safe dictionary operations

✅ Impact:
Guarantees consistency, reliability, and reusability across all modules.
"""

import uuid
import datetime
import json
from typing import Any, Dict, Optional


# -----------------------------
# 🔑 Identifiers & Timestamps
# -----------------------------

def generate_id(prefix: str = "FINSIG") -> str:
    """
    Generate a unique institutional identifier.
    Example: FINSIG-20251218-<UUID>
    """
    return f"{prefix}-{datetime.datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"


def current_timestamp() -> str:
    """
    Return the current timestamp in ISO 8601 format.
    """
    return datetime.datetime.now().isoformat()


# -----------------------------
# ✅ Validation Helpers
# -----------------------------

def validate_not_empty(value: Any, field_name: str) -> None:
    """
    Ensure a value is not empty.
    Raises ValueError if invalid.
    """
    if value is None or (isinstance(value, str) and value.strip() == ""):
        raise ValueError(f"Field '{field_name}' cannot be empty.")


def validate_positive_number(value: Any, field_name: str) -> None:
    """
    Ensure a number is positive.
    Raises ValueError if invalid.
    """
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"Field '{field_name}' must be a positive number.")


# -----------------------------
# 📂 JSON Utilities
# -----------------------------

def to_json(data: Dict[str, Any], indent: int = 4) -> str:
    """
    Serialize a dictionary to JSON string.
    """
    return json.dumps(data, ensure_ascii=False, indent=indent)


def from_json(json_str: str) -> Dict[str, Any]:
    """
    Deserialize a JSON string to dictionary.
    """
    return json.loads(json_str)


# -----------------------------
# 🛠️ Safe Dictionary Operations
# -----------------------------

def safe_get(data: Dict[str, Any], key: str, default: Optional[Any] = None) -> Any:
    """
    Safely get a value from a dictionary.
    Returns default if key not found.
    """
    return data.get(key, default)


def merge_dicts(base: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries (updates overwrite base).
    """
    result = base.copy()
    result.update(updates)
    return result


# -----------------------------
# 🧪 Example Usage
# -----------------------------

if __name__ == "__main__":
    # Generate ID and timestamp
    print("🔑 Generated ID:", generate_id("TEST"))
    print("⏱️ Current timestamp:", current_timestamp())

    # Validate values
    try:
        validate_not_empty("", "username")
    except ValueError as e:
        print("⚠️ Validation error:", e)

    try:
        validate_positive_number(-5, "amount")
    except ValueError as e:
        print("⚠️ Validation error:", e)

    # JSON utilities
    data = {"id": "001", "value": 100}
    json_str = to_json(data)
    print("📂 JSON string:", json_str)
    print("📂 Parsed JSON:", from_json(json_str))

    # Safe dictionary operations
    base = {"a": 1, "b": 2}
    updates = {"b": 3, "c": 4}
    merged = merge_dicts(base, updates)
    print("🛠️ Merged dict:", merged)
    print("🔎 Safe get:", safe_get(merged, "d", "default"))
