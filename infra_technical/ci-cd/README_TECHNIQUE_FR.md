# README TECHNIQUE – Pipeline CI/CD de FINSIG

---

## 🎯 Objectif

Le module CI/CD assure la **robustesse**, la **traçabilité** et l’**auditabilité** de l’infrastructure technique de FINSIG.  
Il permet de tester, empaqueter, déployer et surveiller les composants dans un environnement reproductible et conforme.  
Ce pipeline est conçu pour fonctionner de manière fiable même en contexte de crise, renforçant la crédibilité institutionnelle.

---

## 📂 Structure générale

### 🔧 `configs/`
- `pyproject.toml` → métadonnées du projet, dépendances et configuration des outils (pytest, flake8, mypy, bandit).  
- `requirements.txt` → dépendances organisées par catégories : cœur, développement, CI/CD, monitoring.  
- `pytest.ini` → standardisation de la découverte des tests, rapports de couverture, sortie JUnit et logs horodatés.  
- `mypy.ini` → vérification stricte des types, codes d’erreur et support des plugins (`pydantic.mypy`).

### ⚙️ `workflows/`
- `ci.yml` → orchestration globale des étapes CI/CD.  
- `tests.yml` → exécution des tests unitaires avec couverture.  
- `lint.yml` → contrôle qualité et sécurité du code.  
- `build.yml` → empaquetage Python et vérification d’installabilité.  
- `docker.yml` → construction et push des images Docker vers GHCR.  
- `deploy.yml` → simulation de déploiement staging via Docker Compose.

### 📈 Monitoring & Alertes
- `prometheus.yml` → configuration de Prometheus pour collecter les métriques de l’app, de la base de données et des exporters.  
- `alert_rules.yml` → règles d’alerte critiques (app down, DB down, CPU/mémoire élevée).  
- `docker-compose.yml` → déploiement local complet (app, Postgres, exporters, Prometheus).

### 🧪 Tests & Validation
- `tests/` → pipelines de validation (`test_ci.yml`, `test_lint.yml`, `test_build.yml`) et tests des utilitaires (`test_ci_cd_utils.py`).  
- `schemas/` → schéma de validation des workflows et artefacts (`ci_cd_schema.json`).  
- `utils/` → fonctions utilitaires pour logs, hash et horodatages (`ci_cd_utils.py`).

### 📚 Documentation
- `README_TECHNIQUE_FR.md / EN / ES` → documentation technique trilingue.  
- `BITACORA_CI-CD_FR.md / EN / ES` → journal institutionnel de l’évolution CI/CD.  
- `CI_CD_GUIDE.md` → principes de conception, méthodologie et gouvernance des workflows CI/CD.

---

## 🔄 Étapes du pipeline

1. **Tests**  
   - Exécution des tests unitaires avec `pytest`.  
   - Mesure de la couverture et export des rapports (`coverage.xml`, `test-results.xml`).

2. **Linting & Sécurité**  
   - Vérification du style avec `flake8`.  
   - Analyse des vulnérabilités avec `bandit`.  
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
   - Healthchecks intégrés.

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