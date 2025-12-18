from core.architecture.modules.schemas.audit_schema import AuditSchema
from core.architecture.modules.schemas.compliance_schema import ComplianceSchema

def validate_required_fields(schema_obj, required_fields):
    """
    Vérifie que tous les champs obligatoires sont présents et non vides.
    """
    for field in required_fields:
        value = getattr(schema_obj, field, None)
        if value is None or (isinstance(value, str) and not value.strip()):
            raise ValueError(f"Champ obligatoire manquant ou vide: {field}")
    return True


def validate_schema_signature(schema_obj):
    """
    Vérifie que la signature correspond aux données du schéma.
    """
    expected_signature = schema_obj.generate_signature()
    if schema_obj.signature != expected_signature:
        raise ValueError(f"Signature invalide pour {schema_obj.__class__.__name__}")
    return True


def validate_audit_schema(audit: AuditSchema):
    """
    Validation croisée pour AuditSchema.
    """
    required_fields = ["id", "timestamp", "actor", "action", "version", "signature"]
    validate_required_fields(audit, required_fields)
    validate_schema_signature(audit)
    return True


def validate_compliance_schema(compliance: ComplianceSchema):
    """
    Validation croisée pour ComplianceSchema.
    """
    required_fields = ["id", "timestamp", "regulator", "status", "version", "signature"]
    validate_required_fields(compliance, required_fields)
    validate_schema_signature(compliance)
    return True