# SUB_MODULE_GUIDE_ES – Puertas

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `gates/` define las **puertas disciplinarias e institucionales** de FINSIG.  
Organiza los mecanismos de acceso, validación y transición entre los diferentes dominios y conocimientos, garantizando robustez, trazabilidad y conformidad.  
Este sub-módulo se integra en el directorio `docs-disciplinary` junto con `knowledge/` y `domains/`.

---

## 📑 Alcance
- **Control de acceso disciplinario**: validación de entradas y salidas entre módulos.  
- **Puertas normativas**: alineación con estándares ISO/IEC, GDPR, AML/KYC.  
- **Puertas técnicas**: CI/CD, auditabilidad del software, interoperabilidad multi-módulo.  
- **Puertas institucionales**: gobernanza, certificación y adopción regional.  
- **Puertas pedagógicas**: transmisión y onboarding intergeneracional.  

---

## 📂 Organización de archivos

### 📂 docs/
- **GATES_GUIDE.md** → marco global de las puertas disciplinarias.  
- **ACCESS_GATE.md** → guía sobre mecanismos de acceso.  
- **NORMATIVE_GATE.md** → guía sobre puertas normativas.  
- **TECH_GATE.md** → guía sobre puertas técnicas.  
- **INSTITUTIONAL_GATE.md** → guía sobre puertas institucionales.  
- **PEDAGOGY_GATE.md** → guía sobre puertas pedagógicas.  

### 📂 conformity/
- **gates_validator.py** → verifica la conformidad de las puertas disciplinarias.  
- **access_gate_checker.py** → controla la validez de los mecanismos de acceso.  
- **normative_gate_checker.py** → asegura la conformidad de las puertas normativas.  
- **tech_gate_checker.py** → valida las puertas técnicas.  
- **institutional_gate_checker.py** → verifica la conformidad de las puertas institucionales.  
- **pedagogy_gate_checker.py** → controla la conformidad de las puertas pedagógicas.  

### 📂 modules/
- **gates_engine.py** → motor principal de gestión de puertas.  
- **gates_mapping.py** → mapeo de puertas disciplinarias.  
- **gates_audit.py** → registro y auditoría de puertas aplicadas.  

### 📂 tests/
- **test_gates_engine.py** → pruebas sobre la robustez del motor de puertas.  
- **test_access_gate_checker.py** → pruebas sobre mecanismos de acceso.  
- **test_normative_gate_checker.py** → pruebas sobre puertas normativas.  
- **test_tech_gate_checker.py** → pruebas sobre puertas técnicas.  
- **test_institutional_gate_checker.py** → pruebas sobre puertas institucionales.  
- **test_pedagogy_gate_checker.py** → pruebas sobre puertas pedagógicas.  

### 📂 workflows/
- **gates-validation.yml** → verifica la conformidad global del sub-módulo.  
- **access-gate-validation.yml** → validación de mecanismos de acceso.  
- **normative-gate-validation.yml** → validación de puertas normativas.  
- **tech-gate-validation.yml** → validación de puertas técnicas.  
- **institutional-gate-validation.yml** → validación de puertas institucionales.  
- **pedagogy-gate-validation.yml** → validación de puertas pedagógicas.  

---

## ⚙️ Funcionamiento
- Las puertas se definen en `GATES_GUIDE.md` y se aplican mediante `gates_engine.py`.  
- Cada tipo de puerta se valida con checkers específicos.  
- Los workflows CI/CD garantizan que los mecanismos de transición se mantengan coherentes y conformes.  
- Las auditorías se registran en `gates_audit.py` y se integran en `BITACORA.md`.  

---

## ✅ Impacto institucional
- **Fiabilidad**: mecanismos de acceso robustos y conformes.  
- **Transparencia**: puertas auditadas y documentadas.  
- **Interoperabilidad**: armonización multi-dominio y multi-módulo.  
- **Transmisión**: onboarding facilitado para equipos y socios.  
- **Adopción**: credibilidad reforzada ante instituciones regionales y continentales.  

---

## 📌 Conclusión
El sub-módulo `gates/` es la **puerta disciplinaria del directorio docs-disciplinary**.  
Define los mecanismos de acceso, validación y transmisión, garantizando robustez, transparencia y adopción institucional.  
Su integración con `knowledge/` y `domains/` asegura una coherencia completa en la documentación disciplinaria.