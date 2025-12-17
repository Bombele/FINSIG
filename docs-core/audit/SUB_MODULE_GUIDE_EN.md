# SUB_MODULE_GUIDE_EN – Audit

---

## 🎯 Purpose of the sub-module
The `audit/` sub-module defines the institutional and technical framework of **logging and traceability** within FINSIG.  
It ensures that every action, validation, and workflow is recorded, verified, and compliant with international standards.  
This sub-module is integrated into the `docs-core` folder alongside `data/`, `governance/`, and `reports/`.

---

## 📑 Scope
- **Normative compliance**: alignment with ISO/IEC, GDPR, AML/KYC.  
- **Technical logging**: recording of events, logs, and validations.  
- **Institutional traceability**: integration of audits into `BITACORA.md`.  
- **Interoperability**: harmonization with other sub-modules (`data`, `governance`, `reports`).  
- **Transparency**: clear and multilingual documentation for institutional adoption.  

---

## 📂 File organization

### 📂 docs/
- **AUDIT_GUIDE.md** → global framework of audit and traceability.  
- **NORMATIVE_AUDIT.md** → principles of normative compliance.  
- **TECH_AUDIT.md** → technical logging and events.  
- **INSTITUTIONAL_AUDIT.md** → institutional audit and governance.  
- **REPORTING_AUDIT.md** → integration of audits into reports.  

### 📂 conformity/
- **audit_validator.py** → verifies compliance of modules with audit standards.  
- **normative_audit_checker.py** → controls normative compliance.  
- **tech_audit_checker.py** → validates technical logging.  
- **institutional_audit_checker.py** → ensures institutional compliance.  
- **reporting_audit_checker.py** → verifies integration of audits into reports.  

### 📂 modules/
- **audit_engine.py** → main engine for audit management.  
- **audit_mapping.py** → mapping of normative, technical, and institutional audits.  
- **audit_logger.py** → logging of events and validations.  
- **audit_audit.py** → auditing of internal processes.  

### 📂 tests/
- **test_audit_engine.py** → tests on robustness of the audit engine.  
- **test_normative_audit_checker.py** → tests on normative compliance.  
- **test_tech_audit_checker.py** → tests on technical logging.  
- **test_institutional_audit_checker.py** → tests on institutional audits.  
- **test_reporting_audit_checker.py** → tests on integration of audits into reports.  

### 📂 workflows/
- **audit-validation.yml** → verifies overall compliance of the sub-module.  
- **normative-audit-validation.yml** → validation of normative audits.  
- **tech-audit-validation.yml** → validation of technical audits.  
- **institutional-audit-validation.yml** → validation of institutional audits.  
- **reporting-audit-validation.yml** → validation of audit integration into reports.  

---

## ⚙️ Operation
- Audits are defined in `AUDIT_GUIDE.md` and applied via `audit_engine.py`.  
- Each aspect (normative, technical, institutional, reporting) is validated by the checkers.  
- CI/CD workflows ensure traceability is respected at each update.  
- Audits are logged in `audit_logger.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and robust framework for traceability.  
- **Transparency**: audits documented and verifiable.  
- **Interoperability**: harmonized integration with `data`, `governance`, and `reports`.  
- **Adoption**: strengthened credibility with regulators and institutions.  

---

## 📌 Conclusion
The `audit/` sub-module is the **traceability backbone of the docs-core folder**.  
It defines mechanisms of logging and compliance, ensuring robustness, transparency, and institutional adoption.  
Its integration with `data/`, `governance/`, and `reports/` ensures complete coherence in central documentation.