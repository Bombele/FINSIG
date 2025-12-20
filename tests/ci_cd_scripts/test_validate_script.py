import subprocess
import json

def test_validate_script_runs(tmp_path):
    result = subprocess.run(["bash", "scripts/validate.sh"], capture_output=True, text=True)
    assert result.returncode == 0
    validation_file = "infra_technical/ci-cd/artifacts/artifact-validation.json"
    with open(validation_file) as f:
        data = json.load(f)
    assert "status" in data
    assert data["status"] in ["PASSED", "FAILED"]