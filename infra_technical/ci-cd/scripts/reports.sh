#!/bin/bash
set -e
mkdir -p infra_technical/ci-cd/artifacts/reports
pytest --cov=./ --cov-report=xml:infra_technical/ci-cd/artifacts/reports/coverage.xml \
       --junitxml=infra_technical/ci-cd/artifacts/reports/test-results.xml || true
flake8 > infra_technical/ci-cd/artifacts/reports/lint-report.txt || true
mypy . >> infra_technical/ci-cd/artifacts/reports/lint-report.txt || true
bandit -r . -f json -o infra_technical/ci-cd/artifacts/reports/security-report.json || true
safety check --json > infra_technical/ci-cd/artifacts/reports/security-report.json || true