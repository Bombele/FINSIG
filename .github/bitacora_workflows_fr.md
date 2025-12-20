##############################################
# 📖 BITÁCORA FINALE – workflows (FR)
##############################################

## 📅 Journal des Activités

- **2025-12-19** – Création du workflow `ci.yml` pour validation continue (lint, typage, tests, sécurité).  
- **2025-12-19** – Création du workflow `deploy.yml` pour déploiement staging avec Docker Compose et healthchecks.  
- **2025-12-19** – Création du workflow `monitoring.yml` pour validation Prometheus et règles d’alerte (`alert_rules.yml`).  
- **2025-12-19** – Création du workflow `test-scripts.yml` pour validation des scripts CI/CD (`build.sh`, `docker.sh`, `reports.sh`, `validate.sh`, `setup_pipeline.sh`, `pipeline.sh`).  
- **2025-12-19** – Création du workflow `test-pipeline.yml` pour validation ciblée des scripts critiques (`validate.sh`, `pipeline.sh`).  
- **2025-12-19** – Création du workflow global `ci-cd.yml` orchestrant CI, Deploy, Monitoring et Tests.  
- **2025-12-19** – Ajout de la génération et export des rapports institutionnels (`reports/`) et artefacts (`artifacts/`).  
- **2025-12-19** – Mise à jour des bitácoras trilingues (FR/EN/ES) pour assurer la traçabilité des workflows.  
- **2025-12-19** – Création de `WORKFLOWS_GUIDE.md` documentant méthodologie, principes de conception et gouvernance CI/CD.  

---

## ✅ État de Validation

- Workflow CI validé (`ci.yml`).  
- Workflow de déploiement staging validé (`deploy.yml`).  
- Workflow de monitoring validé (`monitoring.yml`).  
- Workflow de tests des scripts CI/CD validé (`test-scripts.yml`).  
- Workflow de tests pipeline validé (`test-pipeline.yml`).  
- Workflow global d’orchestration validé (`ci-cd.yml`).  
- Rapports exportés dans `reports/` (JUnit, couverture, sécurité, déploiement, monitoring).  
- Artefacts consolidés dans `artifacts/` (build Python, image Docker, hashes, logs).  
- Guide `WORKFLOWS_GUIDE.md` fournit gouvernance et méthodologie.  
- Bitácoras mises à jour et alignées avec les évolutions.  

---

## 📌 Conclusion

La bitácora `workflows/` enregistre l’**évolution complète** du sous-module CI/CD de FINSIG.  
Elle garantit **traçabilité institutionnelle**, **robustesse technique**, **sécurité renforcée** et **auditabilité fiable**.  
Avec l’intégration de **`reports/`**, **`artifacts/`** et des workflows CI/CD, le module offre une **séparation claire entre validation technique, déploiement, monitoring et auditabilité institutionnelle**.  
Ce sous-module est la **colonne vertébrale de l’orchestration CI/CD de FINSIG**, démontrant sa capacité à être validé, déployé, monitoré et certifié de manière **transparente et crédible**.
