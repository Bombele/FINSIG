# SUB_MODULE_GUIDE_ES – Auditoría

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `audit/` define el marco institucional y técnico de la **registro y trazabilidad** dentro de FINSIG.  
Garantiza que cada acción, validación y workflow sea registrada, verificada y conforme a los estándares internacionales.  
Este sub-módulo se integra en el directorio `docs-core` junto con `data/`, `governance/` y `reports/`.

---

## 📑 Alcance
- **Conformidad normativa**: alineación con ISO/IEC, GDPR, AML/KYC.  
- **Registro técnico**: documentación de eventos, logs y validaciones.  
- **Trazabilidad institucional**: integración de auditorías en `BITACORA.md`.  
- **Interoperabilidad**: armonización con otros sub-módulos (`data`, `governance`, `reports`).  
- **Transparencia**: documentación clara y multilingüe para adopción institucional.  

---

## 📂 Organización de archivos

### 📂 docs/
- **AUDIT_GUIDE.md** → marco global de auditoría y trazabilidad.  
- **NORMATIVE_AUDIT.md** → principios de conformidad normativa.  
- **TECH_AUDIT.md** → registro técnico y eventos.  
- **INSTITUTIONAL_AUDIT.md** → auditoría institucional y gobernanza.  
- **REPORTING_AUDIT.md** → integración de auditorías en informes.  

### 📂 conformity/
- **audit_validator.py** → verifica la conformidad de los módulos con los estándares de auditoría.  
- **normative_audit_checker.py** → controla la conformidad normativa.  
- **tech_audit_checker.py** → valida el registro técnico.  
- **institutional_audit_checker.py** → asegura la conformidad institucional.  
- **reporting_audit_checker.py** → verifica la integración de auditorías en informes.  

### 📂 modules/
- **audit_engine.py** → motor principal de gestión de auditorías.  
- **audit_mapping.py** → mapeo de auditorías normativas, técnicas e institucionales.  
- **audit_logger.py** → registro de eventos y validaciones.  
- **audit_audit.py** → auditoría de procesos internos.  

### 📂 tests/
- **test_audit_engine.py** → pruebas sobre la robustez del motor de auditoría.  
- **test_normative_audit_checker.py** → pruebas sobre conformidad normativa.  
- **test_tech_audit_checker.py** → pruebas sobre registro técnico.  
- **test_institutional_audit_checker.py** → pruebas sobre auditorías institucionales.  
- **test_reporting_audit_checker.py** → pruebas sobre integración de auditorías en informes.  

### 📂 workflows/
- **audit-validation.yml** → verifica la conformidad global del sub-módulo.  
- **normative-audit-validation.yml** → validación de auditorías normativas.  
- **tech-audit-validation.yml** → validación de auditorías técnicas.  
- **institutional-audit-validation.yml** → validación de auditorías institucionales.  
- **reporting-audit-validation.yml** → validación de integración de auditorías en informes.  

---

## ⚙️ Funcionamiento
- Las auditorías se definen en `AUDIT_GUIDE.md` y se aplican mediante `audit_engine.py`.  
- Cada aspecto (normativo, técnico, institucional, reporting) se valida con los checkers.  
- Los workflows CI/CD garantizan que la trazabilidad se respete en cada actualización.  
- Las auditorías se registran en `audit_logger.py` y se integran en `BITACORA.md`.  

---

## ✅ Impacto institucional
- **Fiabilidad**: marco claro y robusto para la trazabilidad.  
- **Transparencia**: auditorías documentadas y verificables.  
- **Interoperabilidad**: integración armonizada con `data`, `governance` y `reports`.  
- **Adopción**: credibilidad reforzada ante reguladores e instituciones.  

---

## 📌 Conclusión
El sub-módulo `audit/` es la **columna de trazabilidad del directorio docs-core**.  
Define los mecanismos de registro y conformidad, garantizando robustez, transparencia y adopción institucional.  
Su integración con `data/`, `governance/` y `reports/` asegura una coherencia completa en la documentación central.