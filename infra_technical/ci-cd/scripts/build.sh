#!/bin/bash
set -e  # stoppe le script en cas d'erreur

echo "🚀 Démarrage du build Python..."

# 1. Installer les dépendances nécessaires
pip install --upgrade pip
pip install build twine

# 2. Nettoyer l'environnement
rm -rf dist build *.egg-info

# 3. Générer les artefacts Python (wheel + sdist)
python -m build

# 4. Vérifier les artefacts avec Twine
twine check dist/*

# 5. Créer le dossier cible si absent
mkdir -p infra_technical/ci-cd/artifacts/build

# 6. Déplacer les artefacts générés
cp dist/*.whl infra_technical/ci-cd/artifacts/build/
cp dist/*.tar.gz infra_technical/ci-cd/artifacts/build/

echo "✅ Build terminé. Artefacts disponibles dans infra_technical/ci-cd/artifacts/build/"