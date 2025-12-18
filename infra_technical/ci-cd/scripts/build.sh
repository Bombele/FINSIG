#!/bin/bash
set -e
pip install build twine
rm -rf dist build *.egg-info
python -m build
twine check dist/*
cp dist/*.whl infra_technical/ci-cd/artifacts/build/
cp dist/*.tar.gz infra_technical/ci-cd/artifacts/build/