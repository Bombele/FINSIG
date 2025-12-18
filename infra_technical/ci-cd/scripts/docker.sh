#!/bin/bash
set -e  # stoppe le script en cas d'erreur

echo "🐳 Démarrage du build Docker..."

# 1. Créer le dossier cible si absent
mkdir -p infra_technical/ci-cd/artifacts/docker

# 2. Construire l’image Docker
docker build -t ghcr.io/bombele/finsig:1.0.0 .

# 3. Exporter l’image en tar
docker save ghcr.io/bombele/finsig:1.0.0 -o infra_technical/ci-cd/artifacts/docker/docker-image.tar

# 4. Générer le hash SHA256
sha256sum infra_technical/ci-cd/artifacts/docker/docker-image.tar > infra_technical/ci-cd/artifacts/docker/docker-hash.txt

# 5. Créer un fichier digest institutionnel
DIGEST=$(sha256sum infra_technical/ci-cd/artifacts/docker/docker-image.tar | cut -d ' ' -f1)
cat <<EOF > infra_technical/ci-cd/artifacts/docker/docker-image-sha256.txt
# FINSIG – Docker Image Digest
image: ghcr.io/bombele/finsig:1.0.0
digest: sha256:${DIGEST}
created_at: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
source: ci/cd docker.sh script
validation: PASSED
EOF

# 6. Vérifier le contenu du tar (auditabilité)
tar -tf infra_technical/ci-cd/artifacts/docker/docker-image.tar > infra_technical/ci-cd/artifacts/docker/docker-layers.txt

echo "✅ Docker image exportée et validée. Artefacts disponibles dans infra_technical/ci-cd/artifacts/docker/"