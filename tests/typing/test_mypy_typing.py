import subprocess
import os

def test_mypy_runs_and_generates_report(tmp_path):
    """
    Vérifie que mypy s'exécute correctement avec la configuration institutionnelle
    et génère un rapport d'audit.
    """
    reports_dir = "infra_technical/ci-cd/reports"
    os.makedirs(reports_dir, exist_ok=True)

    # Exécution de mypy avec configuration
    result = subprocess.run(
        ["mypy", "--config-file", "infra-config/sub-module/mypy.ini", "src"],
        capture_output=True,
        text=True
    )

    # Vérifie que mypy s'est exécuté
    assert result.returncode in [0, 1]  # 0 = succès, 1 = erreurs de typage
    assert "error" in result.stdout.lower() or "Success" in result.stdout

    # Sauvegarde du rapport institutionnel
    report_file = os.path.join(reports_dir, "mypy-report.log")
    with open(report_file, "w") as f:
        f.write(result.stdout)

    # Vérifie que le rapport est bien généré
    assert os.path.exists(report_file)
    with open(report_file) as f:
        content = f.read()
    assert "mypy" in content or "error" in content.lower()