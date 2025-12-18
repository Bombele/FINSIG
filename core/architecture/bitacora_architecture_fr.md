# BITACORA – core/architecture

---

## 📅 Journal des activités

- **2025-12-18** – Mise à jour du `README_TECHNIQUE_FR.md` pour inclure les modules `scoring`, `storage`, `traceability` et `utils`.  
- **2025-12-18** – Création du fichier `scoring_engine.py` (module `scoring`) pour calculer des scores institutionnels (risque, conformité, performance).  
- **2025-12-18** – Création du fichier `storage_manager.py` (module `storage`) pour gérer le stockage institutionnel (sauvegarde, lecture, suppression, traçabilité).  
- **2025-12-18** – Création du fichier `traceability.py` (module `traceability`) pour enregistrer les actions institutionnelles avec auditabilité.  
- **2025-12-18** – Création du fichier `utils.py` (module `utils`) pour fournir des fonctions utilitaires réutilisables (IDs, horodatage, validations, JSON, dictionnaires).  
- **2025-12-17** – Ajout du module `schemas` et création des fichiers `base_schema.py`, `finance_schema.py`, `audit_schema.py`, `compliance_schema.py`.  
- **2025-12-17** – Mise à jour des `BITACORA` et `README_TECHNIQUE` en versions trilingues (FR/EN/ES).  
- **2025-12-17** – Création du script `pipeline_orchestrator.py` (module `orchestration`).  
- **2025-12-16** – Recréation du script `workflow_checker.py` pour valider la documentation trilingue.  
- **2025-12-16** – Mise à jour du `structure_validator.py`.  
- **2025-12-15** – Initialisation du sous-module `conformity/`.  
- **2025-12-14** – Structuration initiale du sous-module `core/architecture`.

---

## ✅ État des validations

- Validateurs opérationnels (`structure_validator.py`, `workflow_checker.py`).  
- Modules de collecte et de normalisation testés.  
- Pipeline d’orchestration validé.  
- Schémas validés (`base`, `finance`, `audit`, `compliance`).  
- Moteur de scoring opérationnel.  
- Gestionnaire de stockage opérationnel.  
- Moteur de traçabilité opérationnel.  
- Utilitaires (`utils.py`) opérationnels.  
- Documentation trilingue en place.  
- Bitácora mise à jour.

---

## 📌 Notes techniques

- Intégration des validateurs dans CI/CD.  
- Séquence d’exécution : Collecte → Normalisation → Conformité → Orchestration → Schémas → Scoring → Stockage → Traçabilité → Utilitaires.  
- Logs centralisés dans `logs/`.  
- Données normalisées et validées avant compliance, scoring et audit.  
- Utilitaires garantissent cohérence et réutilisabilité.

---

## 📌 Conclusion

La bitácora `core/architecture` trace désormais l’évolution complète du sous-module et de ses modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`, `utils`).  
Elle garantit la traçabilité institutionnelle, la conformité documentaire et la robustesse technique.