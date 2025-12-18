# README TECHNIQUE – Pipeline CI/CD de FINSIG

---

## 🎯 Objectif

Le module CI/CD assure la **robustesse**, la **traçabilité** et l’**auditabilité** de l’infrastructure technique de FINSIG.  
Il permet de tester, empaqueter, déployer et surveiller les composants dans un environnement reproductible et conforme.  
Ce pipeline est conçu pour fonctionner de manière fiable même en contexte de crise, renforçant la crédibilité institutionnelle.

---

## 📂 Structure générale

### 🔧 `configs/`
- `pyproject.toml` → métadonnées du projet, dépendances et configuration des outils (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → dépendances hiérarchisées (cœur, développement, CI/CD, monitoring).  
- `pytest.ini` → standardisation des tests, rapports de couverture, sortie JUnit et logs horodatés.  
- `mypy.ini` → typage strict, codes d’erreur, support des plugins (`pydantic.mypy`).

### ⚙️ `.github/workflows/`
- `build-validation.yml` → validation du packaging Python (`wheel`, `sdist`), installabilité et artefacts pour audit.  
- `lint-validation.yml` → exécution de flake8, bandit et mypy pour qualité, sécurité et typage.  
- `tests-validation.yml` → exécution des tests unitaires avec couverture et rapports JUnit.  
- `security-check.yml` → analyse des vulnérabilités du code et des dépendances (bandit + safety).  
- `deploy-validation.yml` → simulation de déploiement staging via Docker Compose avec healthchecks et Prometheus.  
- `lint-check.yml` → contrôle rapide de style et typage.  
- `ci-validation.yml` → orchestration globale des workflows en parallèle.

### 📈 Monitoring & Orchestration
- `prometheus.yml` → collecte des métriques (app, base de données, exporters).  
- `alert_rules.yml` → règles d’alerte critiques (app down, DB down, CPU/mémoire élevée).  
- `docker-compose.yml` → déploiement local complet (app, Postgres, exporters, Prometheus).

### 🧪 Tests & Validation
- `tests/` → pipelines de validation (`test_ci.yml`, `test_lint.yml`, `test_build.yml`) et tests utilitaires (`test_ci_cd_utils.py`).  
- `schemas/` → schéma de validation des workflows et artefacts (`ci_cd_schema.json`).  
- `utils/` → fonctions utilitaires pour logs, hash et horodatages (`ci_cd_utils.py`).

### 📚 Documentation
- `README_TECHNIQUE_FR.md / EN / ES` → documentation technique trilingue.  
- `BITACORA_CI-CD_FR.md / EN / ES` → journaux institutionnels de l’évolution CI/CD.  
- `CI_CD_GUIDE.md` → principes de conception, méthodologie et gouvernance.

---

## 🔄 Étapes du pipeline

1. **Tests**  
   - Exécution des tests unitaires avec `pytest`.  
   - Mesure de la couverture et export des rapports (`coverage.xml`, `test-results.xml`).

2. **Linting & Sécurité**  
   - Vérification du style avec `flake8`.  
   - Analyse des vulnérabilités avec `bandit` et `safety`.  
   - Vérification statique des types avec `mypy`.

3. **Build & Empaquetage**  
   - Génération des artefacts Python (`wheel`, `sdist`).  
   - Vérification de l’installabilité et de la reproductibilité.

4. **Dockerisation**  
   - Construction de l’image Docker.  
   - Push vers GitHub Container Registry (GHCR).

5. **Déploiement Staging**  
   - Simulation complète via `docker-compose`.  
   - Services inclus : app, base de données, monitoring, exporters.  
   - Healthchecks intégrés (app, DB, Prometheus).

6. **Monitoring & Alertes**  
   - Prometheus collecte les métriques.  
   - Alertes critiques activées en cas de panne ou de surcharge.

---

## ✅ Impact institutionnel

- **Robustesse** → validée par les tests et l’empaquetage automatisé.  
- **Conformité** → assurée par linting, typage et analyse de sécurité.  
- **Auditabilité** → rapports de couverture, JUnit et métriques Prometheus exportables.  
- **Reproductibilité** → garantie par Docker et les configs standardisées.  
- **Résilience** → monitoring et alertes intégrés pour continuité opérationnelle.  
- **Crédibilité** → documentation trilingue et bitácoras pour validation externe.

---

## 📌 Conclusion

Ce pipeline CI/CD est la **colonne vertébrale technique de FINSIG**.  
Il démontre la capacité du projet à être testé, sécurisé, empaqueté, déployé et surveillé de manière **transparente et auditable**.  
C’est un atout stratégique pour la validation institutionnelle, l’intégration de partenaires et la conformité réglementaire.