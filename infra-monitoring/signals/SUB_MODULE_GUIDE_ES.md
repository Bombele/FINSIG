# SUB_MODULE_GUIDE_ES – Señales

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `signals/` define el marco técnico e institucional de la **gestión de señales** dentro de FINSIG.  
Permite recolectar, normalizar, analizar y difundir señales provenientes de diferentes módulos para mejorar la supervisión, la correlación y la toma de decisiones institucionales.  
Este sub-módulo se integra en el módulo principal `infra-monitoring` junto con `observability/` y `security/`.

---

## 📑 Alcance
- **Recolección de señales**: eventos de sistemas, métricas, alertas.  
- **Normalización**: estandarización de formatos para interoperabilidad multi-módulo.  
- **Análisis**: detección de patrones y correlación de señales.  
- **Difusión**: transmisión de señales a los módulos observability y security.  
- **Auditabilidad**: registro de señales críticas en `BITACORA.md`.  

---

## 📂 Organización de archivos

### 📂 docs/
- **SIGNALS_GUIDE.md** → principios y metodología de gestión de señales.  
- **COLLECTION_GUIDE.md** → guía sobre la recolección de señales.  
- **ANALYSIS_GUIDE.md** → guía sobre el análisis y la correlación.  
- **DISSEMINATION_GUIDE.md** → guía sobre la difusión de señales.  

### 📂 conformity/
- **signals_validator.py** → verifica la coherencia de las señales recolectadas.  
- **collection_checker.py** → valida la recolección de señales.  
- **analysis_checker.py** → asegura la conformidad de los análisis.  
- **dissemination_checker.py** → valida la difusión de señales.  

### 📂 modules/
- **signals_collector.py** → motor de recolección de señales.  
- **signals_normalizer.py** → motor de normalización.  
- **signals_analyzer.py** → motor de análisis y correlación.  
- **signals_dispatcher.py** → motor de difusión de señales.  

### 📂 tests/
- **test_signals_collector.py** → pruebas sobre la recolección de señales.  
- **test_signals_normalizer.py** → pruebas sobre la normalización.  
- **test_signals_analyzer.py** → pruebas sobre el análisis y la correlación.  
- **test_signals_dispatcher.py** → pruebas sobre la difusión.  

### 📂 workflows/
- **signals-validation.yml** → verifica la conformidad global del sub-módulo.  
- **collection-validation.yml** → validación de la recolección.  
- **analysis-validation.yml** → validación de los análisis.  
- **dissemination-validation.yml** → validación de la difusión.  

---

## ⚙️ Funcionamiento
- Las señales se recolectan continuamente con `signals_collector.py`.  
- Se normalizan con `signals_normalizer.py` para garantizar la interoperabilidad.  
- Los análisis y correlaciones se realizan con `signals_analyzer.py`.  
- Las señales se difunden hacia los módulos observability y security mediante `signals_dispatcher.py`.  
- Los workflows CI/CD garantizan trazabilidad y conformidad.  

---

## ✅ Impacto institucional
- **Fiabilidad**: recolección y procesamiento coherente de señales.  
- **Interoperabilidad**: formatos estandarizados para integración multi-módulo.  
- **Auditabilidad**: registro de señales críticas.  
- **Proactividad**: mejora de la supervisión y la toma de decisiones.  

---

## 📌 Conclusión
El sub-módulo `signals/` es un **pilar del módulo infra-monitoring**.  
Asegura la recolección, el análisis y la difusión de señales, fortaleciendo la supervisión y la eficiencia institucional.  
Su integración con `observability/` y `security/` permite una supervisión completa y proactiva de la infraestructura FINSIG.