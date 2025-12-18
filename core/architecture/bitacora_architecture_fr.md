# BITACORA – core/architecture

---

## 📅 Journal des activités

- **2025-12-18** – Mise à jour de `audit_schema.py` et `compliance_schema.py` avec les champs `version` et `signature` (SHA256).  
- **2025-12-18** – Mise à jour de `structure_validator.py` pour valider croisement des signatures et des champs obligatoires.  
- **2025-12-18** – Ajout de la fonction `export_to_csv()` dans `traceability.py` et uniformisation des horodatages en UTC.  
- **2025-12-18** – Ajout des tests unitaires `test_audit_schema.py` et `test_compliance_schema.py` pour la validation des signatures.  
- **2025-12-18** – Ajout du workflow CI/CD `workflows/tests.yml` (pytest + couverture).  
- **2025-12-18** – Amélioration de `test_pipeline_orchestrator.py` avec des cas d’erreurs de dépendances.  
- **2025-12-18** – Amélioration de `test_utils.py` avec des cas limites (`None`, chaînes invalides, dictionnaires vides).  
- **2025-12-17** – Ajout du module `schemas` et création des fichiers associés.  
- **2025-12-17** – Mise à jour des `BITACORA` et `README_TECHNIQUE` en versions trilingues (FR/EN/ES).  
- **2025-12-17** – Création de `pipeline_orchestrator.py`.  
- **2025-12-16** – Recréation de `workflow_checker.py`.  
- **2025-12-16** – Mise à jour de `structure_validator.py`.  
- **2025-12-15** – Initialisation du sous-module `conformity/`.  
- **2025-12-14** – Structuration initiale de `core/architecture`.

---

## ✅ État des validations

- Validateurs opérationnels (`structure_validator.py`, `workflow_checker.py`).  
- Validation croisée des signatures (`audit_schema`, `compliance_schema`).  
- Modules de collecte et de normalisation testés.  
- Pipeline d’orchestration validé (y compris erreurs de dépendances).  
- Schémas validés (`base`, `finance`, `audit`, `compliance`).  
- Moteur de scoring opérationnel.  
- Gestionnaire de stockage opérationnel.  
- Moteur de traçabilité opérationnel (UTC + export CSV).  
- Utilitaires opérationnels (cas limites couverts).  
- Tests unitaires intégrés (`pytest`).  
- Workflow CI/CD actif (`workflows/tests.yml`).  
- Documentation trilingue en place.  
- Bitácora mise à jour.

---

## 📌 Conclusion

La bitácora `core/architecture` trace désormais l’évolution complète du sous-module et de ses modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`, `utils`) ainsi que leurs **tests unitaires** et le **workflow CI/CD**.  
Elle garantit la traçabilité institutionnelle, la conformité documentaire, la robustesse technique et l’auditabilité fiable.