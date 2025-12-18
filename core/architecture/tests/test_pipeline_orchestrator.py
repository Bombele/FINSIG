def test_pipeline_missing_normalization(orchestrator, sample_data):
    """
    Ensure pipeline raises an error if normalization step is skipped.
    """
    # Simuler une dépendance cassée : données non normalisées
    with pytest.raises(RuntimeError) as excinfo:
        orchestrator.run_pipeline([{"id": "TX-001"}])  # données incomplètes
    assert "normalization" in str(excinfo.value).lower()


def test_pipeline_missing_conformity(orchestrator, sample_data):
    """
    Ensure pipeline raises an error if conformity validation is not performed.
    """
    # Supprimer volontairement un champ obligatoire pour déclencher l'erreur
    broken_data = [{"id": "TX-001", "amount": 100}]  # manque 'currency'
    with pytest.raises(ValueError) as excinfo:
        orchestrator.run_pipeline(broken_data)
    assert "conformity" in str(excinfo.value).lower()


def test_pipeline_scoring_dependency(orchestrator, sample_data):
    """
    Ensure scoring step fails if normalization/conformity not done before.
    """
    # Injecter des données brutes sans normalisation
    raw_data = [{"id": "TX-003", "amount": "not_a_number", "currency": "USD"}]
    with pytest.raises(RuntimeError) as excinfo:
        orchestrator.score(raw_data)  # scoring dépend de normalisation
    assert "normalize" in str(excinfo.value).lower()


def test_pipeline_storage_dependency(orchestrator, sample_data, tmp_path):
    """
    Ensure storage step fails if scoring not performed before.
    """
    storage_file = tmp_path / "storage.json"
    # Injecter des données sans score
    unscored_data = [{"id": "TX-004", "amount": 50, "currency": "USD"}]
    with pytest.raises(RuntimeError) as excinfo:
        orchestrator.store(unscored_data, str(storage_file))
    assert "score" in str(excinfo.value).lower()