# SOUS_MODULE_GUIDE – IA agentique institutionnelle

## 🎯 Objectif du sous-module
Le sous-module `ai-agentic` a pour mission d’intégrer une IA générative dotée d’une couche agentique pour la décision autonome.  
Il combine la connexion à des modèles existants (GPT, Claude, LLaMA/open-source) avec une trajectoire progressive vers la souveraineté institutionnelle.  
Ce sous-module s’aligne sur la gouvernance ITCAA, les exigences de conformité **bancaire et comptable** (KYC, AML, IFRS, GAAP), et l’interopérabilité avec les autres modules FINSIG.

---

## 📑 Portée
- **Connexion à des IA existantes** : abstractions de fournisseurs via API, gestion des clés et quotas.  
- **Couche agentique** : orchestration de tâches, outils sécurisés, traçabilité des décisions.  
- **Souveraineté progressive** : exécution locale/offline (llama.cpp, GGUF) pour résilience.  
- **Gouvernance et conformité** : contrôle des biais, journalisation, validation des décisions, respect des normes bancaires et comptables.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **AI_GUIDE.md** → principes d’intégration (API vs offline), scénarios pédagogiques, critères d’évaluation.  
- **AGENTS_GUIDE.md** → conception des agents (rôles, outils autorisés, protocoles de décision).  
- **ETHICS_GUIDE.md** → cadre éthique et conformité (KYC, AML, IFRS, GAAP, privacy, transparence).  
- **SYSTEMS_GUIDE.md** → cartographie technique (fournisseurs, offline, sécurité, interopérabilité).  

### 📂 agents/
- **orchestrator.py** → boucle agentique, planification de tâches, gestion des outils, traçabilité.  
- **tools/** → connecteurs autorisés et audités (recherche interne, génération de rapports).  
- **providers/** → abstractions API pour modèles externes et backends offline.  

### 📂 conformity/
- **policy_guard.py** → application des politiques (contenu autorisé, confidentialité).  
- **evals.py** → tests d’équité, robustesse et conformité.  
- **decision_validator.py** → vérification de cohérence et explicabilité des décisions.  

### 📂 configs/
- **providers.yaml** → configuration des fournisseurs (priorités, fallback, quotas).  
- **ai.toml** → paramètres agentiques (température, limites, outils autorisés).  
- **ethics.toml** → règles bancaires et comptables (KYC, AML, IFRS, GAAP, auditabilité).  

### 📂 schemas/
- **prompts_schema.json** → structure des prompts institutionnels.  
- **decision_trace.json** → format de journalisation des décisions.  
- **report_schema.json** → gabarit des livrables produits par l’agent.  

### 📂 tests/
- **test_orchestrator.py** → tests de la boucle agentique.  
- **test_policy_guard.py** → tests des politiques.  
- **test_providers.py** → tests des abstractions API.  
- **test_offline_backend.py** → tests des backends locaux (llama.cpp/GGUF).  

---

## 🔄 Workflows CI/CD intégrés

### 📂 .github/workflows/
- **ai-agentic.yml**  
  → Pipeline principal :  
  - Vérification du bon fonctionnement de `orchestrator.py`.  
  - Contrôle des outils et connecteurs autorisés.  
  - Export des résultats dans `reports/ai-agentic/`.  

- **ethics-compliance.yml**  
  → Pipeline de conformité :  
  - Vérification des règles bancaires et comptables (KYC, AML, IFRS, GAAP).  
  - Contrôle de l’anonymisation et de la confidentialité.  
  - Journalisation des résultats dans `BITACORA.md`.  

- **providers-validation.yml**  
  → Pipeline de validation des fournisseurs :  
  - Tests des API externes (GPT, Claude, etc.).  
  - Vérification des backends offline (llama.cpp/GGUF).  
  - Contrôle du fallback et de la résilience.  

- **decision-trace.yml**  
  → Pipeline de traçabilité :  
  - Vérification de la cohérence des journaux (`decision_trace.json`).  
  - Signature et hash des traces.  
  - Export des rapports vers `reports/trace/`.  

---

## ⚙️ Fonctionnement
- Entrée contrôlée et anonymisée selon `ethics.toml`.  
- Orchestration des tâches via `orchestrator.py` et respect des politiques de `policy_guard.py`.  
- Exécution hybride : priorité aux fournisseurs externes, fallback vers backends offline.  
- Validation des sorties par `evals.py` et `decision_validator.py`.  
- Traçabilité complète via `decision_trace.json` et journalisation dans `BITACORA.md`.  

---

## ✅ Impact institutionnel
- **Rapidité de valeur** : adoption immédiate via APIs.  
- **Traçabilité totale** : décisions explicables et auditées.  
- **Interopérabilité** : intégration harmonieuse aux modules FINSIG.  
- **Résilience** : fonctionnement hybride online/offline.  
- **Conformité bancaire et comptable** : respect des règles KYC, AML, IFRS et GAAP.  

---

## 📌 Conclusion
Le sous-module `ai-agentic` transforme FINSIG en une infrastructure d’IA agentique gouvernée, sûre et progressive.  
Il permet des preuves de valeur rapides avec fournisseurs existants, tout en préparant une souveraineté institutionnelle avec des backends offline et des modules spécialisés, dans le respect des **normes bancaires et comptables**.
