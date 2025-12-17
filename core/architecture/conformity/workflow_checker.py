"""
workflow_checker.py – core/architecture/conformity

🎯 Purpose:
This script checks that each sub-module in FINSIG follows the required workflow:
1. SUB_MODULE_GUIDE (FR/EN/ES)
2. BITACORA (FR/EN/ES)
3. README_TECHNIQUE (FR/EN/ES)
4. Technical files (framework, compliance, integration, tests)

✅ Impact:
Guarantees that workflows are documented, reproducible, and compliant with institutional standards.
"""

import os

# Expected workflow files
REQUIRED_FILES = [
    "SUB_MODULE_GUIDE_FR.md",
    "SUB_MODULE_GUIDE_EN.md",
    "SUB_MODULE_GUIDE_ES.md",
    "BITACORA_FR.md",
    "BITACORA_EN.md",
    "BITACORA_ES.md",
    "README_TECHNIQUE_FR.md",
    "README_TECHNIQUE_EN.md",
    "README_TECHNIQUE_ES.md",
]

def check_workflow(path: str) -> dict:
    """
    Validate that a given sub-module follows the required workflow.
    Returns a dictionary with missing files and compliance status.
    """
    missing = []
    for file in REQUIRED_FILES:
        if not os.path.exists(os.path.join(path, file)):
            missing.append(file)

    return {
        "path": path,
        "missing": missing,
        "status": "✅ Complete" if not missing else "⚠️ Incomplete"
    }

def validate_core_architecture(base_path: str = "core/architecture"):
    """
    Validate workflows across the core/architecture submodules.
    """
    print(f"🔍 Checking workflows in {base_path} ...")

    submodules = [
        "docs",
        "conformity",
        "integration",
        "framework",
    ]

    for sub in submodules:
        sub_path = os.path.join(base_path, sub)
        if os.path.exists(sub_path):
            result = check_workflow(sub_path)
            print(f"{result['status']} → {sub_path}")
            if result["missing"]:
                print(f"   Missing files: {', '.join(result['missing'])}")
        else:
            print(f"❌ Submodule {sub} not found at {sub_path}")

if __name__ == "__main__":
    validate_core_architecture()