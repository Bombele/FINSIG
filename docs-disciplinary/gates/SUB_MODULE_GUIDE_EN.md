# SUB_MODULE_GUIDE_EN – Gates

---

## 🎯 Purpose of the sub-module
The `gates/` sub-module defines the **disciplinary and institutional gates** of FINSIG.  
It organizes mechanisms of access, validation, and transition between different domains and knowledge, ensuring robustness, traceability, and compliance.  
This sub-module is integrated into the `docs-disciplinary` folder alongside `knowledge/` and `domains/`.

---

## 📑 Scope
- **Disciplinary access control**: validation of entries and exits between modules.  
- **Normative gates**: alignment with ISO/IEC, GDPR, AML/KYC standards.  
- **Technical gates**: CI/CD, software auditability, multi-module interoperability.  
- **Institutional gates**: governance, certification, and regional adoption.  
- **Pedagogical gates**: transmission and intergenerational onboarding.  

---

## 📂 File organization

### 📂 docs/
- **GATES_GUIDE.md** → global framework of disciplinary gates.  
- **ACCESS_GATE.md** → guide on access mechanisms.  
- **NORMATIVE_GATE.md** → guide on normative gates.  
- **TECH_GATE.md** → guide on technical gates.  
- **INSTITUTIONAL_GATE.md** → guide on institutional gates.  
- **PEDAGOGY_GATE.md** → guide on pedagogical gates.  

### 📂 conformity/
- **gates_validator.py** → verifies compliance of disciplinary gates.  
- **access_gate_checker.py** → controls validity of access mechanisms.  
- **normative_gate_checker.py** → ensures compliance of normative gates.  
- **tech_gate_checker.py** → validates technical gates.  
- **institutional_gate_checker.py** → verifies compliance of institutional gates.  
- **pedagogy_gate_checker.py** → controls compliance of pedagogical gates.  

### 📂 modules/
- **gates_engine.py** → main engine for gate management.  
- **gates_mapping.py** → mapping of disciplinary gates.  
- **gates_audit.py** → logging and auditing of applied gates.  

### 📂 tests/
- **test_gates_engine.py** → tests on robustness of the gates engine.  
- **test_access_gate_checker.py** → tests on access mechanisms.  
- **test_normative_gate_checker.py** → tests on normative gates.  
- **test_tech_gate_checker.py** → tests on technical gates.  
- **test_institutional_gate_checker.py** → tests on institutional gates.  
- **test_pedagogy_gate_checker.py** → tests on pedagogical gates.  

### 📂 workflows/
- **gates-validation.yml** → verifies overall compliance of the sub-module.  
- **access-gate-validation.yml** → validation of access mechanisms.  
- **normative-gate-validation.yml** → validation of normative gates.  
- **tech-gate-validation.yml** → validation of technical gates.  
- **institutional-gate-validation.yml** → validation of institutional gates.  
- **pedagogy-gate-validation.yml** → validation of pedagogical gates.  

---

## ⚙️ Operation
- Gates are defined in `GATES_GUIDE.md` and applied via `gates_engine.py`.  
- Each type of gate is validated by specific checkers.  
- CI/CD workflows ensure mechanisms of transition remain coherent and compliant.  
- Audits are logged in `gates_audit.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: robust and compliant access mechanisms.  
- **Transparency**: gates audited and documented.  
- **Interoperability**: multi-domain and multi-module harmonization.  
- **Transmission**: onboarding facilitated for teams and partners.  
- **Adoption**: strengthened credibility with regional and continental institutions.  

---

## 📌 Conclusion
The `gates/` sub-module is the **disciplinary gateway of the docs-disciplinary folder**.  
It defines mechanisms of access, validation, and transmission, ensuring robustness, transparency, and institutional adoption.  
Its integration with `knowledge/` and `domains/` ensures complete coherence in disciplinary documentation.