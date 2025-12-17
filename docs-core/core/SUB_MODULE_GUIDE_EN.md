# SUB_MODULE_GUIDE_EN – Core

---

## 🎯 Purpose of the sub-module
The `core/` sub-module defines the **institutional backbone** of FINSIG.  
It harmonizes and integrates the sub-modules `audit/`, `data/`, `governance/`, and `reports/` to ensure documentation, technical, and regulatory coherence.  
This module is the **root** of the documentation and the entry point for institutional onboarding.

---

## 📑 Scope
- **Central architecture**: organization and articulation of sub-modules.  
- **Interoperability**: integration of rules and formats across modules.  
- **Multilingual documentation**: FR/EN/ES for international adoption.  
- **Traceability**: global index of validations and decisions.  
- **Pedagogical transmission**: clear guide for partners and regulators.  

---

## 📂 File organization

### 📂 docs/
- **CORE_GUIDE.md** → global framework of the core module.  
- **INDEX_GUIDE.md** → index of sub-modules and documentation navigation.  
- **INTEGRATION_GUIDE.md** → interoperability rules between sub-modules.  
- **BITACORA.md** → central log of validations and decisions.  

### 📂 conformity/
- **core_validator.py** → verifies global coherence of the core module.  
- **integration_checker.py** → controls interoperability between sub-modules.  
- **index_checker.py** → validates documentation navigation.  

### 📂 modules/
- **core_engine.py** → main engine for core management.  
- **core_mapping.py** → mapping of sub-modules and dependencies.  
- **core_logger.py** → logging of global validations.  

### 📂 tests/
- **test_core_engine.py** → tests on robustness of the core engine.  
- **test_integration_checker.py** → tests on interoperability.  
- **test_index_checker.py** → tests on index coherence.  

### 📂 workflows/
- **core-validation.yml** → verifies global compliance of the core module.  
- **integration-validation.yml** → validation of interoperability rules.  
- **index-validation.yml** → validation of documentation navigation.  

---

## ⚙️ Operation
- The `core/` module centralizes rules defined in the sub-modules.  
- Validations are ensured by `core_validator.py` and CI/CD workflows.  
- Decisions and audits are logged in `BITACORA.md`.  
- The global index (`INDEX_GUIDE.md`) enables clear and pedagogical navigation.  

---

## ✅ Institutional impact
- **Reliability**: robust and coherent central framework.  
- **Transparency**: decisions and validations accessible in a single log.  
- **Interoperability**: harmonization across all sub-modules.  
- **Transmission**: onboarding facilitated for teams and partners.  
- **Adoption**: strengthened credibility with regional and continental institutions.  

---

## 📌 Conclusion
The `core/` sub-module is the **digital constitution of FINSIG**.  
It defines the central architecture, ensures documentation coherence, and guarantees institutional robustness.  
Its integration with `audit/`, `data/`, `governance/`, and `reports/` makes `core/` the **anchor point of central documentation**.