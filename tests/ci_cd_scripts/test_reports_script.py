import subprocess
import os

def test_reports_script_runs(tmp_path):
    result = subprocess.run(["bash", "scripts/reports.sh"], capture_output=True, text=True)
    assert result.returncode == 0
    reports_dir = "infra_technical/ci-cd/reports"
    assert os.path.exists(reports_dir)
    assert "coverage.xml" in os.listdir(reports_dir)
    assert "test-results.xml" in os.listdir(reports_dir)