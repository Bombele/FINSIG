#!/bin/bash
set -e
mkdir -p infra_technical/ci-cd/artifacts/docker
docker build -t ghcr.io/bombele/finsig:1.0.0 .
docker save ghcr.io/bombele/finsig:1.0.0 -o infra_technical/ci-cd/artifacts/docker/docker-image.tar
sha256sum infra_technical/ci-cd/artifacts/docker/docker-image.tar > infra_technical/ci-cd/artifacts/docker/docker-hash.txt