#!/bin/bash
set -e  # stoppe le script en cas d'erreur

echo "📊 Génération des rapports CI/CD..."

# 1. Créer le dossier cible si absent
mkdir -p infra_technical/ci-cd/artifacts/reports

# 2. Lancer les tests avec couverture
pytest --cov=./ \
       --cov-report=xml:infra_technical/ci-cd/artifacts/reports/coverage.xml \
       --junitxml=infra_technical/ci-cd/artifacts/reports/test-results.xml || true

# 3. Générer le rapport de lint (flake8 + mypy)
flake8 > infra_technical/ci-cd/artifacts/reports/lint-report.txt || true
mypy . >> infra_technical/ci-cd/artifacts/reports/lint-report.txt || true

# 4. Générer le rapport de sécurité (bandit + safety)
bandit -r . -f json -o infra_technical/ci-cd/artifacts/reports/security-report.json || true
safety check --json > infra_technical/ci-cd/artifacts/reports/security-report.json || true

echo "✅ Rapports générés dans infra_technical/ci-cd/artifacts/reports/"