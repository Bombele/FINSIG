import os
import hashlib
import logging
from datetime import datetime, timezone

# Configuration du logger institutionnel
logger = logging.getLogger("ci_cd_utils")
logger.setLevel(logging.INFO)

# Ajout d’un handler par défaut si aucun n’est configuré
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def generate_hash(data: str) -> str:
    """
    Génère un hash SHA256 pour garantir la traçabilité et l’intégrité des données.
    
    Args:
        data (str): Donnée en entrée.
    Returns:
        str: Empreinte SHA256 hexadécimale.
    """
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def timestamp_now() -> str:
    """
    Retourne un horodatage ISO 8601 en UTC pour assurer la traçabilité institutionnelle.
    
    Returns:
        str: Timestamp au format ISO 8601 (ex: 2025-12-18T15:09:00Z).
    """
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log_event(event_type: str, message: str, log_file: str = None) -> None:
    """
    Enregistre un événement dans les logs institutionnels.
    
    Args:
        event_type (str): Type d’événement (ex: TEST, BUILD, DEPLOY).
        message (str): Message descriptif.
        log_file (str, optional): Fichier de log cible. Si None, utilise le logger standard.
    """
    entry = f"{timestamp_now()} | {event_type} | {message}"
    if log_file:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    else:
        logger.info(entry)


def validate_artifact(path: str) -> bool:
    """
    Vérifie l’existence d’un artefact pour garantir l’auditabilité.
    
    Args:
        path (str): Chemin du fichier à valider.
    Returns:
        bool: True si le fichier existe, False sinon.
    """
    exists = os.path.isfile(path)
    log_event("VALIDATE_ARTIFACT", f"{path} exists={exists}")
    return exists
