from pydantic import BaseModel, Field
from typing import Optional
import hashlib


class ComplianceSchema(BaseModel):
    """
    Schéma institutionnel pour les validations réglementaires.
    Inclut version et signature pour traçabilité et authenticité.
    """

    id: str = Field(..., description="Identifiant unique de la validation")
    timestamp: str = Field(..., description="Horodatage ISO 8601 UTC")
    regulator: str = Field(..., description="Autorité ou module de conformité")
    status: str = Field(..., description="Résultat de la validation (valid/invalid)")
    notes: Optional[str] = Field(None, description="Notes ou commentaires")

    # Champs ajoutés
    version: str = Field(..., description="Version du schéma de conformité")
    signature: Optional[str] = Field(None, description="Signature SHA256 pour garantir l'intégrité")

    def generate_signature(self) -> str:
        """
        Génère une signature SHA256 basée sur les champs critiques.
        """
        raw = f"{self.id}{self.timestamp}{self.regulator}{self.status}{self.version}"
        self.signature = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        return self.signature