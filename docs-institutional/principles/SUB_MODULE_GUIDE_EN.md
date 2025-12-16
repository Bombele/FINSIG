# SUB_MODULE_GUIDE_EN – Principles

---

## 🎯 Purpose of the sub-module
The `principles/` sub-module defines the **institutional and normative principles** that guide the design, governance, and adoption of FINSIG.  
It serves as the doctrinal foundation of the project, ensuring coherence, transparency, and alignment with international standards and ethical values.

---

## 📑 Scope
- **Universal principles**: transparency, robustness, inclusion, auditability.  
- **International standards**: alignment with ISO/IEC, GDPR, human rights.  
- **Institutional ethics**: respect for confidentiality, data sovereignty, digital justice.  
- **Regional and continental adoption**: principles adapted to local realities while remaining universal.  

---

## 📂 File organization

### 📂 docs/
- **PRINCIPLES_GUIDE.md** → global framework of institutional principles.  
- **ETHICS_GUIDE.md** → ethical principles and digital justice.  
- **INCLUSION_GUIDE.md** → principles of financial and social inclusion.  
- **TRANSPARENCY_GUIDE.md** → principles of transparency and auditability.  

### 📂 conformity/
- **principles_validator.py** → verifies compliance of modules with institutional principles.  
- **ethics_checker.py** → controls respect for ethical principles.  
- **inclusion_checker.py** → validates application of inclusion principles.  
- **transparency_checker.py** → ensures compliance with transparency principles.  

### 📂 modules/
- **principles_engine.py** → main engine for applying principles.  
- **principles_mapping.py** → mapping of universal and local principles.  
- **principles_audit.py** → logging and auditing of applied principles.  

### 📂 tests/
- **test_principles_engine.py** → tests on robustness of the principles engine.  
- **test_ethics_checker.py** → tests on respect for ethical principles.  
- **test_inclusion_checker.py** → tests on application of inclusion principles.  
- **test_transparency_checker.py** → tests on compliance with transparency principles.  

### 📂 workflows/
- **principles-validation.yml** → verifies overall compliance with principles.  
- **ethics-validation.yml** → validation of ethical principles.  
- **inclusion-validation.yml** → validation of inclusion principles.  
- **transparency-validation.yml** → validation of transparency principles.  

---

## ⚙️ Operation
- Principles are defined in `PRINCIPLES_GUIDE.md` and applied via `principles_engine.py`.  
- Each module is validated by the checkers (`ethics_checker.py`, `inclusion_checker.py`, etc.).  
- CI/CD workflows ensure principles are respected at each update.  
- Audits are logged in `principles_audit.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and robust normative framework.  
- **Transparency**: principles audited and documented.  
- **Ethics**: respect for human rights and digital justice.  
- **Adoption**: universal principles adapted to local realities to foster regional integration.  

---

## 📌 Conclusion
The `principles/` sub-module is the **doctrinal foundation of the docs-institutional folder**.  
It defines the values and standards that guide FINSIG, ensuring robustness, transparency, and institutional adoption.  
Its integration with `objectives/` and `methods/` ensures complete coherence in institutional documentation.