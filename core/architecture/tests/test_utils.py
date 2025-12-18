"""
test_utils.py – core/architecture/tests

🎯 Purpose:
Unit tests for the institutional utility toolkit (utils.py) of FINSIG.
Ensures that:
- IDs and timestamps are generated correctly
- Validation helpers raise errors when expected
- JSON serialization/deserialization works properly
- Safe dictionary operations behave consistently

✅ Impact:
Guarantees consistency, reliability, and reusability of institutional utility functions.
"""

import pytest
from core.architecture.modules.utils import utils


# -----------------------------
# ✅ Tests for Identifiers & Timestamps
# -----------------------------

def test_generate_id_prefix():
    """
    Ensure generated ID starts with the given prefix.
    """
    uid = utils.generate_id("TEST")
    assert uid.startswith("TEST-")


def test_current_timestamp_format():
    """
    Ensure timestamp is in ISO 8601 format.
    """
    ts = utils.current_timestamp()
    assert "T" in ts  # ISO format includes 'T' separator


# -----------------------------
# ✅ Tests for Validation Helpers
# -----------------------------

def test_validate_not_empty_passes():
    """
    Ensure non-empty values pass validation.
    """
    utils.validate_not_empty("value", "field")


def test_validate_not_empty_raises_error():
    """
    Ensure empty values raise ValueError.
    """
    with pytest.raises(ValueError):
        utils.validate_not_empty("", "field")


def test_validate_positive_number_passes():
    """
    Ensure positive numbers pass validation.
    """
    utils.validate_positive_number(10, "amount")


def test_validate_positive_number_raises_error():
    """
    Ensure non-positive numbers raise ValueError.
    """
    with pytest.raises(ValueError):
        utils.validate_positive_number(-5, "amount")


# -----------------------------
# ✅ Tests for JSON Utilities
# -----------------------------

def test_to_json_and_from_json():
    """
    Ensure JSON serialization and deserialization work correctly.
    """
    data = {"id": "001", "value": 100}
    json_str = utils.to_json(data)
    parsed = utils.from_json(json_str)
    assert parsed["id"] == "001"
    assert parsed["value"] == 100


# -----------------------------
# ✅ Tests for Safe Dictionary Operations
# -----------------------------

def test_safe_get_existing_key():
    """
    Ensure safe_get returns value for existing key.
    """
    data = {"a": 1}
    assert utils.safe_get(data, "a") == 1


def test_safe_get_missing_key():
    """
    Ensure safe_get returns default for missing key.
    """
    data = {"a": 1}
    assert utils.safe_get(data, "b", "default") == "default"


def test_merge_dicts():
    """
    Ensure merge_dicts combines dictionaries correctly.
    """
    base = {"a": 1, "b": 2}
    updates = {"b": 3, "c": 4}
    merged = utils.merge_dicts(base, updates)
    assert merged["a"] == 1
    assert merged["b"] == 3
    assert merged["c"] == 4