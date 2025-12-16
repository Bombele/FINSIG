# SUB_MODULE_GUIDE_EN – Knowledge

---

## 🎯 Purpose of the sub-module
The `knowledge/` sub-module defines the institutional and technical framework of **knowledge management** within FINSIG.  
It organizes, structures, and transmits disciplinary knowledge to ensure robustness, traceability, and institutional adoption.  
This sub-module is integrated into the `docs-disciplinary` folder alongside `domains/` and `gates/`.

---

## 📑 Scope
- **Disciplinary structuring**: organization of knowledge by modules and sub-modules.  
- **Multilingual documentation**: transmission in FR/EN/ES for international onboarding.  
- **Traceability**: logging and auditing of integrated knowledge.  
- **Interoperability**: harmonization of formats for multi-branch integration.  
- **Pedagogical transmission**: clear guides to facilitate intergenerational and institutional adoption.  

---

## 📂 File organization

### 📂 docs/
- **KNOWLEDGE_GUIDE.md** → global framework of knowledge management.  
- **STRUCTURE_GUIDE.md** → principles of disciplinary structuring.  
- **MULTILINGUAL_GUIDE.md** → methodology for trilingual documentation.  
- **TRACEABILITY_GUIDE.md** → principles of traceability and auditability.  
- **PEDAGOGY_GUIDE.md** → pedagogical transmission and onboarding.  

### 📂 conformity/
- **knowledge_validator.py** → verifies compliance of modules with knowledge management standards.  
- **structure_checker.py** → controls coherence of disciplinary structuring.  
- **multilingual_checker.py** → ensures compliance of translations and multilingual harmonization.  
- **traceability_checker.py** → validates knowledge traceability.  
- **pedagogy_checker.py** → verifies compliance of pedagogical guides.  

### 📂 modules/
- **knowledge_engine.py** → main engine for knowledge management.  
- **knowledge_mapping.py** → mapping of disciplinary knowledge.  
- **knowledge_audit.py** → logging and auditing of integrated knowledge.  
- **knowledge_transmission.py** → pedagogical transmission engine.  

### 📂 tests/
- **test_knowledge_engine.py** → tests on robustness of the knowledge engine.  
- **test_structure_checker.py** → tests on structuring coherence.  
- **test_multilingual_checker.py** → tests on multilingual compliance.  
- **test_traceability_checker.py** → tests on traceability.  
- **test_pedagogy_checker.py** → tests on pedagogical transmission.  

### 📂 workflows/
- **knowledge-validation.yml** → verifies overall compliance of the sub-module.  
- **structure-validation.yml** → validation of disciplinary structuring.  
- **multilingual-validation.yml** → validation of translations and harmonization.  
- **traceability-validation.yml** → validation of traceability.  
- **pedagogy-validation.yml** → validation of pedagogical guides.  

---

## ⚙️ Operation
- Knowledge is defined in `KNOWLEDGE_GUIDE.md` and applied via `knowledge_engine.py`.  
- Each aspect (structuring, multilingual, traceability, pedagogy) is validated by the checkers.  
- CI/CD workflows ensure disciplinary documentation remains coherent and compliant.  
- Audits are logged in `knowledge_audit.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and robust disciplinary framework.  
- **Transparency**: audited and documented knowledge.  
- **Interoperability**: multilingual and multi-module harmonization.  
- **Transmission**: onboarding facilitated for teams and partners.  
- **Adoption**: strengthened credibility with regional and continental institutions.  

---

## 📌 Conclusion
The `knowledge/` sub-module is the **disciplinary foundation of the docs-disciplinary folder**.  
It defines structuring, transmission, and traceability of knowledge, ensuring robustness, transparency, and institutional adoption.  
Its integration with `domains/` and `gates/` ensures complete coherence in disciplinary documentation.