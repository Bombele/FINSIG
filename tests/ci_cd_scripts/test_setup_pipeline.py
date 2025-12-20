import subprocess

def test_setup_pipeline_runs():
    result = subprocess.run(["bash", "scripts/setup_pipeline.sh"], capture_output=True, text=True)
    assert result.returncode == 0
    # Vérifie que pip et dépendances sont installées
    assert "Successfully installed" in result.stdout or "Requirement already satisfied" in result.stdout