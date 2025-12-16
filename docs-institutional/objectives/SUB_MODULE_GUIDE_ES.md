# SUB_MODULE_GUIDE_ES – Objetivos

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `objectives/` define los **objetivos institucionales y estratégicos** de FINSIG.  
Traduce los principios en acciones concretas y medibles, garantizando que cada módulo contribuya a la misión global de robustez, transparencia y adopción institucional.  
Este sub-módulo se integra en el directorio `docs-institutional` junto con `principles/` y `methods/`.

---

## 📑 Alcance
- **Objetivos normativos**: alineación con estándares internacionales (ISO/IEC, GDPR, AML/KYC).  
- **Objetivos técnicos**: robustez, trazabilidad, interoperabilidad multi-módulo.  
- **Objetivos institucionales**: adopción regional y continental, credibilidad ante reguladores.  
- **Objetivos sociales**: inclusión financiera, justicia digital, protección de datos.  

---

## 📂 Organización de archivos

### 📂 docs/
- **OBJECTIVES_GUIDE.md** → marco global de objetivos institucionales.  
- **TECH_OBJECTIVES.md** → objetivos técnicos y robustez de sistemas.  
- **INSTITUTIONAL_OBJECTIVES.md** → objetivos institucionales y adopción regional.  
- **SOCIAL_OBJECTIVES.md** → inclusión financiera y justicia digital.  

### 📂 conformity/
- **objectives_validator.py** → verifica la conformidad de los módulos con los objetivos definidos.  
- **tech_objectives_checker.py** → controla el cumplimiento de objetivos técnicos.  
- **institutional_objectives_checker.py** → valida el cumplimiento de objetivos institucionales.  
- **social_objectives_checker.py** → asegura la conformidad con objetivos sociales.  

### 📂 modules/
- **objectives_engine.py** → motor principal de seguimiento de objetivos.  
- **objectives_mapping.py** → mapeo de objetivos normativos, técnicos, institucionales y sociales.  
- **objectives_audit.py** → registro y auditoría de objetivos alcanzados.  

### 📂 tests/
- **test_objectives_engine.py** → pruebas sobre la robustez del motor de objetivos.  
- **test_tech_objectives_checker.py** → pruebas sobre objetivos técnicos.  
- **test_institutional_objectives_checker.py** → pruebas sobre objetivos institucionales.  
- **test_social_objectives_checker.py** → pruebas sobre objetivos sociales.  

### 📂 workflows/
- **objectives-validation.yml** → verifica la conformidad global con los objetivos.  
- **tech-objectives-validation.yml** → validación de objetivos técnicos.  
- **institutional-objectives-validation.yml** → validación de objetivos institucionales.  
- **social-objectives-validation.yml** → validación de objetivos sociales.  

---

## ⚙️ Funcionamiento
- Los objetivos se definen en `OBJECTIVES_GUIDE.md` y se aplican mediante `objectives_engine.py`.  
- Cada categoría de objetivos se valida con los checkers (`tech_objectives_checker.py`, `institutional_objectives_checker.py`, etc.).  
- Los workflows CI/CD garantizan que los objetivos se respeten en cada actualización.  
- Las auditorías se registran en `objectives_audit.py` y se integran en `BITACORA.md`.  

---

## ✅ Impacto institucional
- **Fiabilidad**: objetivos claros y medibles.  
- **Transparencia**: seguimiento auditado y documentado.  
- **Ética**: inclusión y justicia digital integradas en los objetivos.  
- **Adopción**: credibilidad reforzada ante reguladores e instituciones.  

---

## 📌 Conclusión
El sub-módulo `objectives/` es la **traducción operativa de los principios** en el directorio `docs-institutional`.  
Define las acciones concretas que guían FINSIG, garantizando robustez, transparencia y adopción institucional.  
Su integración con `principles/` y `methods/` asegura una coherencia completa en la documentación institucional.