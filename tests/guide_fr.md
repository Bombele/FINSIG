##############################################
# 📖 MODULE_GUIDE – Tests (FINSIG)
##############################################

## 1. Objectif
Le sous-module **Tests** garantit la robustesse, la conformité et l’auditabilité de FINSIG :
- Vérification des utilitaires et fonctions transversales.  
- Validation des règles de juridiction et conformité réglementaire.  
- Contrôle des identités et accès.  
- Tests de conformité (KYC, AML, ISO/IEC, RGPD).  
- Automatisation via scripts CI/CD.  

----------------------------------------------

## 2. Dossier `utlis/`
📂 tests/utlis/  
- test_utils.py → Vérifie les fonctions utilitaires partagées (formatage, parsing, calculs).  
- test_helpers.py → Tests sur les helpers internes.  

👉 **Bonne pratique** : isoler les tests unitaires pour chaque fonction utilitaire.  

----------------------------------------------

## 3. Dossier `jurisdictions/`
📂 tests/jurisdictions/  
- test_jurisdiction_rules.py → Vérifie les règles par juridiction (Afrique, Amérique du Sud, Europe).  
- test_local_compliance.py → Tests sur les normes locales (banques centrales, régulateurs).  

👉 **Bonne pratique** : simuler différents contextes réglementaires pour garantir l’adaptabilité continentale.  

----------------------------------------------

## 4. Dossier `identity/`
📂 tests/identity/  
- test_identity_validator.py → Vérifie la validation des identités.  
- test_access_manager.py → Tests sur la gestion des accès et rôles.  
- test_authentication.py → Vérifie les mécanismes d’authentification.  

👉 **Bonne pratique** : inclure des cas de fraude et d’accès non autorisé.  

----------------------------------------------

## 5. Dossier `compliance/`
📂 tests/compliance/  
- test_kyc_checker.py → Vérifie la conformité KYC.  
- test_aml_checker.py → Vérifie la conformité AML.  
- test_iso_validator.py → Vérifie la conformité ISO/IEC et RGPD.  
- test_audit_rules.py → Vérifie l’application des règles d’audit.  

👉 **Bonne pratique** : centraliser les tests de conformité pour éviter duplication.  

----------------------------------------------

## 6. Dossier `ci_cd_scripts/`
📂 tests/ci_cd_scripts/  
- test_lint.sh → Vérifie la qualité du code.  
- test_coverage.sh → Mesure la couverture des tests.  
- test_deploy.sh → Simule le déploiement et vérifie la robustesse.  
- test_ci.yml → Workflow CI/CD pour automatiser les tests.  

👉 **Bonne pratique** : intégrer ces scripts dans GitHub Actions pour validation continue.  

----------------------------------------------

## 7. Résultat attendu
- **Utlis** → validation des fonctions transversales.  
- **Jurisdictions** → conformité locale et continentale.  
- **Identity** → robustesse des accès et authentification.  
- **Compliance** → conformité institutionnelle (KYC, AML, ISO/IEC).  
- **CI/CD Scripts** → automatisation et validation continue.  

----------------------------------------------

## 8. Conclusion / Synthèse
Le sous-module **Tests** est la **garantie de robustesse et de conformité institutionnelle** de FINSIG.  
- Il couvre les utilitaires, juridictions, identités et conformité.  
- Il intègre des scripts CI/CD pour automatiser la validation.  
- Il assure une traçabilité et une auditabilité complètes.  

Ensemble, il constitue un **socle transversal de validation**, prêt pour adoption et certification.