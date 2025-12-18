import os
import hashlib
import logging
import pytest
from datetime import datetime

# Import des utilitaires du module CI/CD
from infra_technical.ci_cd.utils import (
    generate_hash,
    log_event,
    timestamp_now,
    validate_artifact
)

# Configuration du logger pour les tests
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ci_cd_utils_test")


def test_generate_hash_consistency():
    """Le hash doit être déterministe et identique pour la même entrée."""
    data = "finsig-ci-cd"
    h1 = generate_hash(data)
    h2 = generate_hash(data)
    assert h1 == h2
    assert isinstance(h1, str)
    assert len(h1) == 64  # SHA256


def test_generate_hash_uniqueness():
    """Le hash doit être différent pour des entrées différentes."""
    h1 = generate_hash("finsig-ci-cd")
    h2 = generate_hash("finsig-ci-cd-alt")
    assert h1 != h2


def test_timestamp_now_format():
    """Le timestamp doit être au format ISO 8601."""
    ts = timestamp_now()
    # Exemple attendu : 2025-12-18T14:47:00Z
    assert isinstance(ts, str)
    assert "T" in ts
    assert ts.endswith("Z")


def test_log_event_creates_entry(tmp_path):
    """Le log doit créer une entrée dans un fichier."""
    log_file = tmp_path / "ci_cd_test.log"
    log_event("TEST_EVENT", "Pipeline started", log_file=str(log_file))
    assert log_file.exists()
    content = log_file.read_text()
    assert "TEST_EVENT" in content
    assert "Pipeline started" in content


def test_validate_artifact(tmp_path):
    """La validation d’un artefact doit réussir si le fichier existe."""
    artifact = tmp_path / "artifact.txt"
    artifact.write_text("dummy content")
    assert validate_artifact(str(artifact)) is True

    # Cas d’erreur : fichier inexistant
    assert validate_artifact(str(tmp_path / "missing.txt")) is False
