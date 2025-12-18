#!/bin/bash
set -e  # stoppe le script en cas d'erreur

echo "🚀 Initialisation complète du pipeline CI/CD..."

# 1. Mise à jour de pip et installation des dépendances nécessaires
pip install --upgrade pip
pip install build twine flake8 mypy bandit safety pytest coverage

# 2. Nettoyage des anciens artefacts
rm -rf dist build *.egg-info

# 3. Création des dossiers institutionnels
mkdir -p infra_technical/ci-cd/artifacts/build
mkdir -p infra_technical/ci-cd/artifacts/docker
mkdir -p infra_technical/ci-cd/artifacts/reports
mkdir -p infra_technical/ci-cd/artifacts/validation

# 4. Exécution des scripts spécialisés
./infra_technical/ci-cd/scripts/build.sh
./infra_technical/ci-cd/scripts/docker.sh
./infra_technical/ci-cd/scripts/reports.sh
./infra_technical/ci-cd/scripts/validate.sh

echo "✅ Setup pipeline terminé avec succès."
echo "📂 Tous les artefacts et validations sont disponibles dans infra_technical/ci-cd/artifacts/"