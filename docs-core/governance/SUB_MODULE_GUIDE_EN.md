# SUB_MODULE_GUIDE_EN – Governance

---

## 🎯 Purpose of the sub-module
The `governance/` sub-module defines the framework for **institutional governance and compliance** within FINSIG.  
It ensures that all decisions, validations, and regulatory alignments are documented, accessible, and multilingual.  
This sub-module integrates into `docs-core` alongside `audit/`, `data/`, and `reports/`.

---

## 📑 Scope
- **Governance rules**: definition of institutional governance standards.  
- **Compliance**: alignment with regulatory frameworks (banking, insurance, telcos).  
- **Multilingual documentation**: FR/EN/ES for international adoption.  
- **Integration**: interoperability with `audit`, `data`, and `reports`.  
- **Pedagogical transmission**: clear guides for onboarding and institutional use.  

---

## 📂 File organization

### 📂 docs/
- **GOVERNANCE_GUIDE.md** → global framework of governance.  
- **COMPLIANCE_GUIDE.md** → definition of compliance rules.  
- **INSTITUTIONAL_GUIDE.md** → institutional governance formats.  
- **INTEGRATION_GUIDE.md** → interoperability with other modules.  

### 📂 conformity/
- **governance_validator.py** → verifies compliance of governance rules.  
- **compliance_checker.py** → controls coherence of compliance.  
- **institutional_checker.py** → validates governance formats.  
- **integration_checker.py** → ensures interoperability.  

### 📂 modules/
- **governance_engine.py** → main engine for governance management.  
- **governance_mapping.py** → mapping of governance and compliance.  
- **governance_logger.py** → logging of governance decisions.  
- **governance_audit.py** → auditing of governance processes.  

### 📂 tests/
- **test_governance_engine.py** → tests on robustness of governance engine.  
- **test_compliance_checker.py** → tests on compliance coherence.  
- **test_institutional_checker.py** → tests on governance formats.  
- **test_integration_checker.py** → tests on interoperability.  

### 📂 workflows/
- **governance-validation.yml** → verifies overall compliance of the sub-module.  
- **compliance-validation.yml** → validation of compliance rules.  
- **institutional-validation.yml** → validation of governance formats.  
- **integration-validation.yml** → validation of interoperability.  

---

## ⚙️ Operation
- Governance is defined in `GOVERNANCE_GUIDE.md` and applied via `governance_engine.py`.  
- Each aspect (compliance, formats, integration) is validated by the checkers.  
- CI/CD workflows ensure governance remains coherent and compliant.  
- Decisions are logged in `governance_logger.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and robust framework for governance.  
- **Transparency**: decisions documented and verifiable.  
- **Interoperability**: harmonization across modules and languages.  
- **Transmission**: onboarding facilitated for teams and partners.  
- **Adoption**: strengthened credibility with regional and continental institutions.  

---

## 📌 Conclusion
The `governance/` sub-module is the **governance backbone of the docs-core folder**.  
It defines rules, compliance, and formats, ensuring robustness, transparency, and institutional adoption.  
Its integration with `audit/`, `data/`, and `reports/` ensures complete coherence in central documentation.