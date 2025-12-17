
## 🇪🇸 README_TECHNIQUE_ES.md

```markdown
# README Técnico – core/architecture

---

## 🎯 Objetivo
Este archivo proporciona instrucciones técnicas para usar y mantener el submódulo `core/architecture` de FINSIG.  
Complementa el `SUB_MODULE_GUIDE` (carta institucional) y la `BITACORA` (registro de actividades).

---

## 📂 Estructura
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Carta del submódulo.  
- `BITACORA_FR/EN/ES.md` → Registro de actividades trilingüe.  
- `README_TECHNIQUE_FR/EN/ES.md` → Manual técnico trilingüe.  
- `docs/ARCHITECTURE_GUIDE.md` → Principios estructurales.  
- `conformity/structure_validator.py` → Script de validación.  
- `conformity/workflow_checker.py` → Script de control de flujos.

---

## ⚙️ Requisitos
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions o pipelines en `infra_technical/ci-cd/`

---

## 🚀 Uso
```bash
# Validar la conformidad documental
python conformity/structure_validator.py

# Verificar los flujos de trabajo
python conformity/workflow_checker.py

# Ejecutar las pruebas
pytest tests/