# SUB_MODULE_GUIDE_ES – Core

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `core/` define la **columna vertebral institucional** de FINSIG.  
Armoniza e integra los sub-módulos `audit/`, `data/`, `governance/` y `reports/` para garantizar la coherencia documental, técnica y regulatoria.  
Este módulo es la **raíz** de la documentación y el punto de entrada para el onboarding institucional.

---

## 📑 Alcance
- **Arquitectura central**: organización y articulación de los sub-módulos.  
- **Interoperabilidad**: integración de reglas y formatos entre los módulos.  
- **Documentación multilingüe**: FR/EN/ES para adopción internacional.  
- **Trazabilidad**: índice global de validaciones y decisiones.  
- **Transmisión pedagógica**: guía clara para socios y reguladores.  

---

## 📂 Organización de archivos

### 📂 docs/
- **CORE_GUIDE.md** → marco global del módulo core.  
- **INDEX_GUIDE.md** → índice de sub-módulos y navegación documental.  
- **INTEGRATION_GUIDE.md** → reglas de interoperabilidad entre sub-módulos.  
- **BITACORA.md** → registro central de validaciones y decisiones.  

### 📂 conformity/
- **core_validator.py** → verifica la coherencia global del módulo core.  
- **integration_checker.py** → controla la interoperabilidad entre sub-módulos.  
- **index_checker.py** → valida la navegación documental.  

### 📂 modules/
- **core_engine.py** → motor principal de gestión del core.  
- **core_mapping.py** → mapeo de sub-módulos y dependencias.  
- **core_logger.py** → registro de validaciones globales.  

### 📂 tests/
- **test_core_engine.py** → pruebas sobre la robustez del motor core.  
- **test_integration_checker.py** → pruebas sobre la interoperabilidad.  
- **test_index_checker.py** → pruebas sobre la coherencia del índice.  

### 📂 workflows/
- **core-validation.yml** → verifica la conformidad global del módulo core.  
- **integration-validation.yml** → validación de reglas de interoperabilidad.  
- **index-validation.yml** → validación de la navegación documental.  

---

## ⚙️ Funcionamiento
- El módulo `core/` centraliza las reglas definidas en los sub-módulos.  
- Las validaciones se aseguran mediante `core_validator.py` y workflows CI/CD.  
- Las decisiones y auditorías se registran en `BITACORA.md`.  
- El índice global (`INDEX_GUIDE.md`) permite una navegación clara y pedagógica.  

---

## ✅ Impacto institucional
- **Fiabilidad**: marco central robusto y coherente.  
- **Transparencia**: decisiones y validaciones accesibles en un registro único.  
- **Interoperabilidad**: armonización entre todos los sub-módulos.  
- **Transmisión**: onboarding facilitado para equipos y socios.  
- **Adopción**: credibilidad reforzada ante instituciones regionales y continentales.  

---

## 📌 Conclusión
El sub-módulo `core/` es la **constitución digital de FINSIG**.  
Define la arquitectura central, asegura la coherencia documental y garantiza la robustez institucional.  
Su integración con `audit/`, `data/`, `governance/` y `reports/` convierte a `core/` en el **punto de anclaje de la documentación central**.