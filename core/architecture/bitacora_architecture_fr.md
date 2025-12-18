# BITACORA – core/architecture

---

## 📅 Journal des activités

- **2025-12-18** – Mise à jour du `README_TECHNIQUE_FR.md` pour inclure les modules `scoring`, `storage` et `traceability` en plus de `conformity`, `collection`, `normalization`, `orchestration` et `schemas`.  
- **2025-12-18** – Création du fichier `scoring_engine.py` (module `scoring`) pour calculer des scores institutionnels (risque, conformité, performance).  
- **2025-12-18** – Création du fichier `storage_manager.py` (module `storage`) pour gérer le stockage institutionnel (sauvegarde, lecture, suppression, traçabilité).  
- **2025-12-18** – Création du fichier `traceability.py` (module `traceability`) pour enregistrer les actions institutionnelles (collecte, normalisation, conformité, scoring, stockage) avec auditabilité.  
- **2025-12-17** – Mise à jour du `README_TECHNIQUE_FR.md` pour inclure le module `schemas`.  
- **2025-12-17** – Création des fichiers `base_schema.py`, `finance_schema.py`, `audit_schema.py`, `compliance_schema.py` (module `schemas`).  
- **2025-12-17** – Mise à jour des `BITACORA` et `README_TECHNIQUE` en versions trilingues (FR/EN/ES).  
- **2025-12-17** – Création du script `pipeline_orchestrator.py` (module `orchestration`).  
- **2025-12-16** – Recréation du script `workflow_checker.py` pour valider la documentation trilingue.  
- **2025-12-16** – Mise à jour du `structure_validator.py`.  
- **2025-12-15** – Initialisation du sous-module `conformity/`.  
- **2025-12-14** – Structuration initiale du sous-module `core/architecture`.

---

## ✅ État des validations

- `structure_validator.py` et `workflow_checker.py` opérationnels et testés en local.  
- Modules de collecte et de normalisation validés.  
- Pipeline d’orchestration testé et validé.  
- Schémas validés (`base`, `finance`, `audit`, `compliance`).  
- Moteur de scoring opérationnel (risque, conformité, performance).  
- Gestionnaire de stockage opérationnel (sauvegarde, lecture, suppression, traçabilité).  
- Moteur de traçabilité opérationnel (journalisation, filtrage, nettoyage des enregistrements).  
- Documentation technique trilingue en place.  
- Bitácora mise à jour.

---

## 📌 Notes techniques

- Les validateurs doivent être intégrés dans les pipelines CI/CD.  
- Séquence d’exécution :  
  1. Collecte (`data_collection.py`)  
  2. Normalisation (`data_normalization.py`)  
  3. Conformité (`structure_validator.py`, `workflow_checker.py`)  
  4. Orchestration (`pipeline_orchestrator.py`)  
  5. Schémas (`base_schema.py`, `finance_schema.py`, `audit_schema.py`, `compliance_schema.py`)  
  6. Scoring (`scoring_engine.py`)  
  7. Stockage (`storage_manager.py`)  
  8. Traçabilité (`traceability.py`)  
- Chaque sous-module doit contenir guides, bitácoras et README techniques trilingues.  
- Les fichiers de log doivent être placés dans `logs/`.  
- Les données doivent être normalisées et validées avant passage dans les modules compliance, scoring et audit.  
- Les résultats de scoring et de stockage doivent être intégrés dans les rapports institutionnels.  
- La traçabilité garantit la reproductibilité et l’auditabilité des workflows.

---

## 📌 Conclusion

La bitácora `core/architecture` trace désormais l’évolution complète du sous-module et de ses modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`).  
Elle garantit la traçabilité institutionnelle, la conformité documentaire et la robustesse technique, offrant une base fiable pour la gouvernance numérique et la validation réglementaire.