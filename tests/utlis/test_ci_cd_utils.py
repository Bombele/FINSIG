import os
import json
import hashlib
import datetime
import logging

import pytest

# Exemple de fonctions utilitaires (à adapter selon ton module réel)
def generate_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

def timestamp_now() -> str:
    return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

def validate_artifact(artifact_path: str) -> dict:
    if not os.path.exists(artifact_path):
        return {"status": "FAILED", "reason": "File not found"}
    return {"status": "PASSED", "reason": "File exists"}

# --- Tests unitaires ---

def test_generate_hash_consistency():
    content = "FINSIG"
    h1 = generate_hash(content)
    h2 = generate_hash(content)
    assert h1 == h2
    assert len(h1) == 64  # SHA256 length

def test_timestamp_format():
    ts = timestamp_now()
    # Vérifie que le format correspond à YYYY-MM-DD HH:MM:SS
    assert len(ts) == 19
    assert ts[4] == "-" and ts[7] == "-" and ts[13] == ":"

def test_validate_artifact_pass(tmp_path):
    # Crée un fichier temporaire
    f = tmp_path / "artifact.txt"
    f.write_text("dummy content")
    result = validate_artifact(str(f))
    assert result["status"] == "PASSED"

def test_validate_artifact_fail(tmp_path):
    fake_file = tmp_path / "missing.txt"
    result = validate_artifact(str(fake_file))
    assert result["status"] == "FAILED"