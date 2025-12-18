# TECHNICAL README – core/architecture

---

## 🎯 Purpose
This module defines FINSIG’s institutional architecture.  
It ensures documentation consistency, traceability, and auditability through sub-modules, standardized schemas, and unit tests.

---

## 📂 Sub-modules

### 1. conformity/
- **structure_validator.py** → Checks presence and compliance of mandatory files.  
- **workflow_checker.py** → Controls workflow sequence and consistency.  
- **Cross-validation**: verifies SHA256 signatures in `audit_schema.py` and `compliance_schema.py`.

### 2. collection/
- **data_collection.py** → Collects and validates raw data (CSV, JSON, API).  
- **logs/collection_log.txt** → Collection logs for traceability.

### 3. normalization/
- **data_normalization.py** → Normalizes data (dates, strings, numbers, mandatory fields, duplicates).

### 4. orchestration/
- **pipeline_orchestrator.py** → Orchestrates the full pipeline (collection → normalization → conformity → audit/scoring).  
- **Dependency tests**: ensure each stage fails if the previous one is missing.

### 5. schemas/
- **base_schema.py** → Generic institutional schema.  
- **finance_schema.py** → Financial transactions schema.  
- **audit_schema.py** → Audit logs schema, includes `version` and `signature` (SHA256).  
- **compliance_schema.py** → Compliance validations schema, includes `version` and `signature` (SHA256).  
- **generate_signature()** → Generates cryptographic signature to guarantee integrity and authenticity.

### 6. traceability/
- **traceability.py** → Institutional traceability engine.  
  - UTC timestamp (ISO 8601).  
  - CSV export via `export_to_csv()` for external audit.

### 7. utils/
- **utils.py** → Institutional utility functions (validation, JSON, dict merge).  
- Edge cases tested: `None`, invalid strings, empty dicts.

---

## 📂 tests/
- **test_structure_validator.py**  
- **test_workflow_checker.py**  
- **test_pipeline_orchestrator.py**  
- **test_traceability.py**  
- **test_utils.py**  
- **test_audit_schema.py**  
- **test_compliance_schema.py**

---

## 📂 workflows/
- **tests.yml** → GitHub Actions workflow running `pytest` and coverage on every commit/PR.

---

## 📌 Conclusion
The `core/architecture` module is complete, robust, and audit-ready: SHA256 signatures, UTC timestamps, CSV export, and CI/CD ensure strong technical governance.