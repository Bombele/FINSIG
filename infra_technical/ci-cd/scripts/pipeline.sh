#!/bin/bash
set -e  # stoppe le script en cas d'erreur

echo "🚀 Lancement du pipeline CI/CD complet..."

# 1. Build des artefacts Python
./infra_technical/ci-cd/scripts/build.sh

# 2. Construction et export de l'image Docker
./infra_technical/ci-cd/scripts/docker.sh

# 3. Génération des rapports (tests, coverage, lint, sécurité)
./infra_technical/ci-cd/scripts/reports.sh

# 4. Validation croisée et génération du fichier institutionnel
./infra_technical/ci-cd/scripts/validate.sh

echo "✅ Pipeline CI/CD terminé avec succès."
echo "📂 Artefacts disponibles dans infra_technical/ci-cd/artifacts/"