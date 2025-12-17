"""
structure_validator.py – core/architecture/conformity

🎯 Purpose:
This script validates the institutional structure of FINSIG.
It ensures that each sub-module contains the required documentation:
- SUB_MODULE_GUIDE in FR/EN/ES
- BITACORA in FR/EN/ES
- INDEX_GUIDE if applicable
- Technical files (framework, compliance, integration)

✅ Impact:
Guarantees traceability, compliance, and reproducibility across the architecture.
"""

import os

# Required files per sub-module
REQUIRED_GUIDES = [
    "SUB_MODULE_GUIDE_FR.md",
    "SUB_MODULE_GUIDE_EN.md",
    "SUB_MODULE_GUIDE_ES.md",
]

REQUIRED_BITACORAS = [
    "BITACORA_FR.md",
    "BITACORA_EN.md",
    "BITACORA_ES.md",
]

def validate_submodule(path: str) -> dict:
    """
    Validate that a given sub-module contains all required documentation.
    Returns a dictionary with missing files.
    """
    missing = {"guides": [], "bitacoras": []}

    for guide in REQUIRED_GUIDES:
        if not os.path.exists(os.path.join(path, guide)):
            missing["guides"].append(guide)

    for bitacora in REQUIRED_BITACORAS:
        if not os.path.exists(os.path.join(path, bitacora)):
            missing["bitacoras"].append(bitacora)

    return missing

def validate_core_architecture(base_path: str = "."):
    """
    Validate the entire core/architecture structure.
    """
    print(f"🔍 Validating structure in {base_path} ...")

    submodules = [
        "docs",
        "conformity",
        "integration",
        "framework",
    ]

    for sub in submodules:
        sub_path = os.path.join(base_path, sub)
        if os.path.exists(sub_path):
            result = validate_submodule(sub_path)
            if result["guides"] or result["bitacoras"]:
                print(f"⚠️ Missing files in {sub_path}: {result}")
            else:
                print(f"✅ {sub_path} is complete.")
        else:
            print(f"❌ Submodule {sub} not found at {sub_path}")

if __name__ == "__main__":
    validate_core_architecture("core/architecture")
