#!/bin/bash
set -e
./infra_technical/ci-cd/scripts/build.sh
./infra_technical/ci-cd/scripts/docker.sh
./infra_technical/ci-cd/scripts/reports.sh
./infra_technical/ci-cd/scripts/validate.sh