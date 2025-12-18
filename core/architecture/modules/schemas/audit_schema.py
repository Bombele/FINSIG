from pydantic import BaseModel, Field
from typing import Optional
import hashlib


class AuditSchema(BaseModel):
    """
    Schéma institutionnel pour les journaux d'audit.
    Inclut version et signature pour traçabilité et authenticité.
    """

    id: str = Field(..., description="Identifiant unique de l'audit")
    timestamp: str = Field(..., description="Horodatage ISO 8601 UTC")
    actor: str = Field(..., description="Auteur ou système ayant généré l'audit")
    action: str = Field(..., description="Action réalisée")
    details: dict = Field(..., description="Détails supplémentaires de l'audit")

    # Champs ajoutés
    version: str = Field(..., description="Version du schéma d'audit")
    signature: Optional[str] = Field(None, description="Signature SHA256 pour garantir l'intégrité")

    def generate_signature(self) -> str:
        """
        Génère une signature SHA256 basée sur les champs critiques.
        """
        raw = f"{self.id}{self.timestamp}{self.actor}{self.action}{self.version}"
        self.signature = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        return self.signature