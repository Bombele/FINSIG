# SUB_MODULE_GUIDE_EN – Reports

---

## 🎯 Purpose of the sub-module
The `reports/` sub-module defines the framework for **reporting and institutional traceability** within FINSIG.  
It ensures that all audits, compliance checks, and governance decisions are documented, accessible, and multilingual.  
This sub-module integrates into `docs-core` alongside `audit/`, `data/`, and `governance/`.

---

## 📑 Scope
- **Reporting rules**: definition of institutional reporting standards.  
- **Traceability**: logging of compliance and governance decisions.  
- **Multilingual documentation**: FR/EN/ES for international adoption.  
- **Integration**: interoperability with `audit`, `data`, and `governance`.  
- **Pedagogical transmission**: clear guides for onboarding and institutional use.  

---

## 📂 File organization

### 📂 docs/
- **REPORTS_GUIDE.md** → global framework of reporting.  
- **TRACEABILITY_GUIDE.md** → definition of traceability rules.  
- **FORMATS_GUIDE.md** → institutional reporting formats.  
- **INTEGRATION_GUIDE.md** → interoperability with other modules.  

### 📂 conformity/
- **reports_validator.py** → verifies compliance of reporting rules.  
- **traceability_checker.py** → controls coherence of traceability.  
- **formats_checker.py** → validates reporting formats.  
- **integration_checker.py** → ensures interoperability.  

### 📂 modules/
- **reports_engine.py** → main engine for reporting management.  
- **reports_mapping.py** → mapping of reports and traceability.  
- **reports_logger.py** → logging of reports and validations.  
- **reports_audit.py** → auditing of reporting processes.  

### 📂 tests/
- **test_reports_engine.py** → tests on robustness of reporting engine.  
- **test_traceability_checker.py** → tests on traceability coherence.  
- **test_formats_checker.py** → tests on reporting formats.  
- **test_integration_checker.py** → tests on interoperability.  

### 📂 workflows/
- **reports-validation.yml** → verifies overall compliance of the sub-module.  
- **traceability-validation.yml** → validation of traceability rules.  
- **formats-validation.yml** → validation of reporting formats.  
- **integration-validation.yml** → validation of interoperability.  

---

## ⚙️ Operation
- Reporting is defined in `REPORTS_GUIDE.md` and applied via `reports_engine.py`.  
- Each aspect (traceability, formats, integration) is validated by the checkers.  
- CI/CD workflows ensure reporting remains coherent and compliant.  
- Reports are logged in `reports_logger.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and robust framework for reporting.  
- **Transparency**: decisions documented and verifiable.  
- **Interoperability**: harmonization across modules and languages.  
- **Transmission**: onboarding facilitated for teams and partners.  
- **Adoption**: strengthened credibility with regional and continental institutions.  

---

## 📌 Conclusion
The `reports/` sub-module is the **reporting backbone of the docs-core folder**.  
It defines rules, traceability, and formats, ensuring robustness, transparency, and institutional adoption.  
Its integration with `audit/`, `data/`, and `governance/` ensures complete coherence in central documentation.