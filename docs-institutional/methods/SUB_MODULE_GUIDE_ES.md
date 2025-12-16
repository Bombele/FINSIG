# SUB_MODULE_GUIDE_ES – Métodos

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `methods/` define los **métodos institucionales y técnicos** utilizados para implementar los principios y alcanzar los objetivos de FINSIG.  
Constituye el marco operativo que garantiza que cada acción se realice de manera robusta, transparente y conforme a los estándares internacionales.  
Este sub-módulo se integra en el directorio `docs-institutional` junto con `principles/` y `objectives/`.

---

## 📑 Alcance
- **Métodos normativos**: aplicación de estándares ISO/IEC, GDPR, AML/KYC.  
- **Métodos técnicos**: CI/CD, auditabilidad del software, modularidad e interoperabilidad.  
- **Métodos institucionales**: gobernanza, documentación multilingüe, adopción regional y continental.  
- **Métodos sociales**: inclusión, justicia digital, transmisión pedagógica.  

---

## 📂 Organización de archivos

### 📂 docs/
- **METHODS_GUIDE.md** → marco global de métodos institucionales y técnicos.  
- **NORMATIVE_METHODS.md** → métodos normativos y conformidad internacional.  
- **TECH_METHODS.md** → métodos técnicos y robustez de sistemas.  
- **INSTITUTIONAL_METHODS.md** → métodos institucionales y gobernanza.  
- **SOCIAL_METHODS.md** → inclusión y justicia digital.  

### 📂 conformity/
- **methods_validator.py** → verifica la conformidad de los módulos con los métodos definidos.  
- **normative_methods_checker.py** → controla la aplicación de métodos normativos.  
- **tech_methods_checker.py** → valida la implementación de métodos técnicos.  
- **institutional_methods_checker.py** → asegura la conformidad de métodos institucionales.  
- **social_methods_checker.py** → verifica la aplicación de métodos sociales.  

### 📂 modules/
- **methods_engine.py** → motor principal de aplicación de métodos.  
- **methods_mapping.py** → mapeo de métodos normativos, técnicos, institucionales y sociales.  
- **methods_audit.py** → registro y auditoría de métodos aplicados.  

### 📂 tests/
- **test_methods_engine.py** → pruebas sobre la robustez del motor de métodos.  
- **test_normative_methods_checker.py** → pruebas sobre métodos normativos.  
- **test_tech_methods_checker.py** → pruebas sobre métodos técnicos.  
- **test_institutional_methods_checker.py** → pruebas sobre métodos institucionales.  
- **test_social_methods_checker.py** → pruebas sobre métodos sociales.  

### 📂 workflows/
- **methods-validation.yml** → verifica la conformidad global con los métodos.  
- **normative-methods-validation.yml** → validación de métodos normativos.  
- **tech-methods-validation.yml** → validación de métodos técnicos.  
- **institutional-methods-validation.yml** → validación de métodos institucionales.  
- **social-methods-validation.yml** → validación de métodos sociales.  

---

## ⚙️ Funcionamiento
- Los métodos se definen en `METHODS_GUIDE.md` y se aplican mediante `methods_engine.py`.  
- Cada categoría de métodos se valida con los checkers (`normative_methods_checker.py`, `tech_methods_checker.py`, etc.).  
- Los workflows CI/CD garantizan que los métodos se respeten en cada actualización.  
- Las auditorías se registran en `methods_audit.py` y se integran en `BITACORA.md`.  

---

## ✅ Impacto institucional
- **Fiabilidad**: métodos claros y robustos.  
- **Transparencia**: seguimiento auditado y documentado.  
- **Ética**: inclusión y justicia digital integradas en los métodos.  
- **Adopción**: credibilidad reforzada ante reguladores e instituciones.  

---

## 📌 Conclusión
El sub-módulo `methods/` es la **implementación operativa de principios y objetivos** en el directorio `docs-institutional`.  
Define las prácticas concretas que guían FINSIG, garantizando robustez, transparencia y adopción institucional.  
Su integración con `principles/` y `objectives/` asegura una coherencia completa en la documentación institucional.