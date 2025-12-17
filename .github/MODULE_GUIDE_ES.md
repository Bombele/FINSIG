# MODULE_GUIDE – .github/workflows/

---

## 🎯 Objetivo
La carpeta `.github/workflows/` es la **cámara de automatización CI/CD** de FINSIG.  
Contiene archivos YAML que definen los pipelines de GitHub Actions, garantizando la validación continua, el despliegue automatizado y la calidad institucional.

---

## 📑 Alcance
- **Integración continua (CI)**: ejecución automática de pruebas unitarias y de integración.  
- **Despliegue continuo (CD)**: automatización de entregas y publicaciones en producción.  
- **Calidad del software**: verificación de estándares (linting, mypy, pytest, etc.).  
- **Trazabilidad**: registro de workflows ejecutados para garantizar el cumplimiento.  
- **Interoperabilidad**: integración con otros módulos (`core`, `compliance`, `infra-*`).

---

## 📂 Organización
Cada archivo `.yml` o `.yaml` corresponde a un **workflow específico**:  
- `ci.yml` → pipeline de pruebas y validación.  
- `deploy.yml` → pipeline de despliegue.  
- `quality.yml` → pipeline de control de calidad.  
- `docs.yml` → pipeline de validación documental.  

*(los nombres pueden variar según los archivos presentes, pero la lógica se mantiene)*

---

## ⚙️ Funcionamiento
- Los workflows se ejecutan automáticamente según eventos de GitHub:  
  - **push** → validación de commits.  
  - **pull_request** → verificación antes de la fusión.  
  - **release** → despliegue institucional.  
- Cada workflow actúa como una **ley técnica** en la constitución digital, garantizando robustez y cumplimiento.  
- Los resultados de los workflows son visibles en la pestaña **Actions** del repositorio GitHub.

---

## ✅ Impacto institucional
- **Fiabilidad**: cada modificación se valida automáticamente.  
- **Transparencia**: los workflows aseguran trazabilidad pública.  
- **Calidad**: cumplimiento de estándares técnicos y regulatorios.  
- **Adopción**: credibilidad reforzada ante socios institucionales gracias a una automatización clara.

---

## 📌 Conclusión
El módulo `.github/workflows/` es la **columna vertebral CI/CD** de FINSIG.  
Encarna la disciplina técnica e institucional, garantizando que cada paso de desarrollo y despliegue respete los estándares de calidad y cumplimiento.