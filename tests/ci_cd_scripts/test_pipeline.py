import subprocess
import os

def test_pipeline_runs():
    result = subprocess.run(["bash", "scripts/pipeline.sh"], capture_output=True, text=True)
    assert result.returncode == 0
    # Vérifie que tous les dossiers sont remplis
    assert os.path.exists("infra_technical/ci-cd/artifacts/build")
    assert os.path.exists("infra_technical/ci-cd/artifacts/docker")
    assert os.path.exists("infra_technical/ci-cd/reports")