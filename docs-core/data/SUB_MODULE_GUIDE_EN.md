# SUB_MODULE_GUIDE_EN – Data

---

## 🎯 Purpose of the sub-module
The `data/` sub-module defines the institutional and technical framework of **data structuring, validation, and governance** within FINSIG.  
It ensures robustness, traceability, and interoperability of data flows across different modules.  
This sub-module is integrated into the `docs-core` folder alongside `audit/`, `governance/`, and `reports/`.

---

## 📑 Scope
- **Data modeling**: definition of standardized structures and formats.  
- **Validation**: control of data quality and compliance.  
- **Traceability**: logging of flows and integration into `BITACORA.md`.  
- **Interoperability**: harmonization of data for multi-module integration.  
- **Pedagogical transmission**: clear and multilingual documentation for institutional onboarding.  

---

## 📂 File organization

### 📂 docs/
- **DATA_GUIDE.md** → global framework of data governance.  
- **DATA_MODEL.md** → principles of modeling and structuring.  
- **DATA_VALIDATION.md** → rules of validation and compliance.  
- **DATA_TRACEABILITY.md** → principles of traceability and auditability.  
- **DATA_INTEROPERABILITY.md** → integration and harmonization across modules.  

### 📂 conformity/
- **data_validator.py** → verifies compliance of data with defined standards.  
- **model_checker.py** → controls coherence of data models.  
- **validation_checker.py** → ensures quality and compliance of data.  
- **traceability_checker.py** → validates traceability of flows.  
- **interoperability_checker.py** → verifies multi-module integration.  

### 📂 modules/
- **data_engine.py** → main engine for data management.  
- **data_mapping.py** → mapping of models and data flows.  
- **data_logger.py** → logging of flows and validations.  
- **data_audit.py** → auditing of data management processes.  

### 📂 tests/
- **test_data_engine.py** → tests on robustness of the data engine.  
- **test_model_checker.py** → tests on coherence of models.  
- **test_validation_checker.py** → tests on data compliance.  
- **test_traceability_checker.py** → tests on traceability.  
- **test_interoperability_checker.py** → tests on multi-module integration.  

### 📂 workflows/
- **data-validation.yml** → verifies overall compliance of the sub-module.  
- **model-validation.yml** → validation of data models.  
- **validation-validation.yml** → validation of data quality.  
- **traceability-validation.yml** → validation of traceability.  
- **interoperability-validation.yml** → validation of multi-module integration.  

---

## ⚙️ Operation
- Data is defined in `DATA_GUIDE.md` and applied via `data_engine.py`.  
- Each aspect (modeling, validation, traceability, interoperability) is validated by the checkers.  
- CI/CD workflows ensure data governance remains coherent and compliant.  
- Audits are logged in `data_logger.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and robust framework for data governance.  
- **Transparency**: flows documented and verifiable.  
- **Interoperability**: harmonization across modules and languages.  
- **Transmission**: onboarding facilitated for teams and partners.  
- **Adoption**: strengthened credibility with regional and continental institutions.  

---

## 📌 Conclusion
The `data/` sub-module is the **data governance backbone of the docs-core folder**.  
It defines modeling, validation, and traceability of flows, ensuring robustness, transparency, and institutional adoption.  
Its integration with `audit/`, `governance/`, and `reports/` ensures complete coherence in central documentation.