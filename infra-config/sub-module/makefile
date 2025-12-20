# ============================================
# 📖 Makefile – infra-config/sub-module
# ============================================

# Variables
PYTHON := python3
PIP := $(PYTHON) -m pip
SRC := src
TESTS := tests
REPORTS := infra_technical/ci-cd/reports
ARTIFACTS := infra_technical/ci-cd/artifacts

# Cibles par défaut
.PHONY: all install lint typing test security coverage reports clean

all: install lint typing test security coverage reports

# --------------------------------------------
# 🔧 Installation des dépendances
# --------------------------------------------
install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# --------------------------------------------
# 🧹 Linting et formatage
# --------------------------------------------
lint:
	flake8 $(SRC) $(TESTS)
	black --check $(SRC) $(TESTS)

# --------------------------------------------
# 🔍 Typage strict avec mypy
# --------------------------------------------
typing:
	mypy --config-file infra-config/sub-module/mypy.ini $(SRC)

# --------------------------------------------
# 🧪 Tests unitaires avec pytest
# --------------------------------------------
test:
	pytest $(TESTS) \
		--junitxml=$(REPORTS)/test-results.xml \
		--log-file=$(REPORTS)/pytest.log

# --------------------------------------------
# 🔒 Audit de sécurité
# --------------------------------------------
security:
	bandit -r $(SRC) -f json -o $(REPORTS)/bandit-report.json
	safety check -r requirements.txt --json > $(REPORTS)/safety-report.json

# --------------------------------------------
# 📊 Couverture de code
# --------------------------------------------
coverage:
	pytest $(TESTS) \
		--cov=$(SRC) \
		--cov-report=xml:$(REPORTS)/coverage.xml \
		--cov-report=html:$(REPORTS)/coverage-html

# --------------------------------------------
# 📝 Génération des rapports institutionnels
# --------------------------------------------
reports: test coverage security typing lint
	@echo "=== Rapports générés dans $(REPORTS) ==="

# --------------------------------------------
# 🧹 Nettoyage des artefacts
# --------------------------------------------
clean:
	rm -rf $(REPORTS)/*
	rm -rf $(ARTIFACTS)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +
