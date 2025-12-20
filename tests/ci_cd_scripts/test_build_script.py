import subprocess
import os

def test_build_script_runs(tmp_path):
    result = subprocess.run(["bash", "scripts/build.sh"], capture_output=True, text=True)
    assert result.returncode == 0
    # Vérifie que les artefacts sont générés
    build_dir = "infra_technical/ci-cd/artifacts/build"
    assert os.path.exists(build_dir)
    assert any(f.endswith(".whl") or f.endswith(".tar.gz") for f in os.listdir(build_dir))