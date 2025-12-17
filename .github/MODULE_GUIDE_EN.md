# MODULE_GUIDE – .github/workflows/

---

## 🎯 Purpose
The `.github/workflows/` folder is the **CI/CD automation chamber** of FINSIG.  
It contains YAML files defining GitHub Actions pipelines, ensuring continuous validation, automated deployment, and institutional quality.

---

## 📑 Scope
- **Continuous Integration (CI)**: automatic execution of unit and integration tests.  
- **Continuous Deployment (CD)**: automation of deliveries and production releases.  
- **Software Quality**: verification of standards (linting, mypy, pytest, etc.).  
- **Traceability**: logging of executed workflows to guarantee compliance.  
- **Interoperability**: integration with other modules (`core`, `compliance`, `infra-*`).

---

## 📂 Organization
Each `.yml` or `.yaml` file corresponds to a **specific workflow**:  
- `ci.yml` → testing and validation pipeline.  
- `deploy.yml` → deployment pipeline.  
- `quality.yml` → quality control pipeline.  
- `docs.yml` → documentation validation pipeline.  

*(names may vary depending on actual files, but the logic remains consistent)*

---

## ⚙️ Functioning
- Workflows are triggered automatically by GitHub events:  
  - **push** → commit validation.  
  - **pull_request** → verification before merging.  
  - **release** → institutional deployment.  
- Each workflow acts as a **technical law** in the digital constitution, ensuring robustness and compliance.  
- Workflow results are visible in the **Actions** tab of the GitHub repository.

---

## ✅ Institutional Impact
- **Reliability**: every modification is automatically validated.  
- **Transparency