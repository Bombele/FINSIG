import subprocess
import os

def test_docker_script_runs(tmp_path):
    result = subprocess.run(["bash", "scripts/docker.sh"], capture_output=True, text=True)
    assert result.returncode == 0
    docker_dir = "infra_technical/ci-cd/artifacts/docker"
    assert os.path.exists(docker_dir)
    assert "docker-image.tar" in os.listdir(docker_dir)
    assert "docker-image-sha256.txt" in os.listdir(docker_dir)