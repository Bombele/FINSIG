# SUB_MODULE_GUIDE – core/architecture

---

## 🎯 Purpose
This guide defines the structure and responsibilities of the sub-modules within the `core/architecture` directory.  
It ensures institutional consistency, traceability, and auditability across FINSIG.

---

## 📂 Sub-modules

### 1. conformity/
- **structure_validator.py** → Checks the presence and compliance of mandatory files.  
- **workflow_checker.py** → Validates documentation sequence and workflow consistency.  
- **Role**: Ensure institutional and documentation compliance.

### 2. collection/
- **data_collection.py** → Collects and validates raw data (CSV, JSON, API).  
- **logs/collection_log.txt** → Logs collections for traceability.  
- **Role**: Centralize institutional data collection and guarantee traceability.

### 3. normalization/
- **data_normalization.py** → Normalizes data (dates, strings, numbers, mandatory fields, duplicates).  
- **Role**: Standardize data to ensure compatibility with compliance and audit modules.

### 4. orchestration/
- **pipeline_orchestrator.py** → Orchestrates the full pipeline (collection → normalization → conformity → audit/scoring).  
- **Role**: Guarantee order, traceability, and integration of steps.

### 5. schemas/
- **base_schema.py** → Generic institutional schema (id, timestamp, source, value, metadata).  
- **finance_schema.py** → Schema for financial transactions.  
- **audit_schema.py** → Schema for audit logs.  
- **compliance_schema.py** → Schema for regulatory validations.  
- **Role**: Define standardized data structures for all modules, ensuring consistency and auditability.

---

## ⚙️ Requirements
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions or pipelines in `infra_technical/ci-cd/`

---

## 📌 Best Practices
- Respect trilingual nomenclature (`FR`, `EN`, `ES`) for guides, bitácoras, and technical READMEs.  
- Update the `BITACORA` after each modification.  
- Normalize data before passing it to compliance, scoring, and audit modules.  
- Use `pipeline_orchestrator.py` as the entry point to guarantee order and traceability.  
- Centralize schemas in `schemas/` to avoid divergence between modules.  

---

## 📌 Conclusion
The `core/architecture` sub-module now consists of five key modules: `conformity`, `collection`, `normalization`, `orchestration`, and `schemas`.  
This structure guarantees robust technical governance, documentation compliance, and institutional traceability.