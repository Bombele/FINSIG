"""
pipeline_orchestrator.py – core/architecture/modules/orchestration

🎯 Purpose:
This module orchestrates the institutional pipeline of FINSIG.
It ensures that data flows through the correct sequence:
1. Collection (raw data ingestion)
2. Normalization (cleaning and standardization)
3. Conformity checks (documentation and workflow validation)
4. Audit/Scoring modules (future integration)

✅ Impact:
Guarantees that processes are executed in the right order,
with traceability and compliance at every stage.
"""

import os
import sys
from typing import List, Dict, Any

# Import modules (assuming relative paths inside core/architecture/modules)
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "collection"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "normalization"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "conformity"))

try:
    from data_collection import DataCollector
    from data_normalization import DataNormalizer
    import structure_validator
    import workflow_checker
except ImportError:
    print("⚠️ Warning: Some modules could not be imported. Check paths and dependencies.")


class PipelineOrchestrator:
    """
    Institutional Pipeline Orchestrator for FINSIG.
    """

    def __init__(self, source_type: str = "json", source_path: str = None):
        self.source_type = source_type
        self.source_path = source_path
        self.data: List[Dict[str, Any]] = []

    def run_collection(self) -> List[Dict[str, Any]]:
        """
        Step 1: Collect data from source.
        """
        collector = DataCollector(source_type=self.source_type, source_path=self.source_path)
        self.data = collector.collect()
        if collector.validate():
            collector.log_collection()
            print("✅ Data collection successful.")
        else:
            print("⚠️ Data collection validation failed.")
        return self.data

    def run_normalization(self) -> List[Dict[str, Any]]:
        """
        Step 2: Normalize collected data.
        """
        normalizer = DataNormalizer(self.data)
        self.data = normalizer.run_full_normalization()
        print("✅ Data normalization complete.")
        return self.data

    def run_conformity_checks(self) -> None:
        """
        Step 3: Run conformity checks on documentation and workflows.
        """
        print("🔍 Running conformity checks...")
        structure_validator.validate_core_architecture()
        workflow_checker.validate_core_architecture()
        print("✅ Conformity checks complete.")

    def execute_pipeline(self) -> List[Dict[str, Any]]:
        """
        Execute the full pipeline: collection → normalization → conformity.
        """
        print("🚀 Starting pipeline orchestration...")
        self.run_collection()
        self.run_normalization()
        self.run_conformity_checks()
        print("🎯 Pipeline orchestration complete.")
        return self.data


# Example usage
if __name__ == "__main__":
    orchestrator = PipelineOrchestrator(source_type="json", source_path="sample_data.json")
    final_data = orchestrator.execute_pipeline()
    print("📊 Final normalized dataset:", final_data)
