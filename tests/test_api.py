import pytest
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["LOKY_MAX_CPU_COUNT"] = "1"

from fastapi.testclient import TestClient
from api.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert "model_loaded" in data

def test_predict_valid_input(client):
    payload = {
        "anciennete_poste_ans": 3.5,
        "niveau_diplome": "Bac+2",
        "code_insee_commune": "75101",
        "code_rome_vise": "M1805",
        "est_allocataire": 1,
        "synthese_entretien": "Experience solide en gestion de projets IT. Reconversion envisagee."
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert "label" in data
    assert "probabilities" in data
    assert "confidence" in data
    assert "fallback" in data
    assert data["prediction"] in [0, 1, 2]

def test_predict_invalid_input_pydantic_validation(client):
    # Ancienneté négative hors bornes validation (ge=0)
    payload = {
        "anciennete_poste_ans": -5.0,
        "niveau_diplome": "Bac",
        "code_insee_commune": "75101",
        "code_rome_vise": "M1805",
        "est_allocataire": 1,
        "synthese_entretien": "Test invalid"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Unprocessable Entity (Pydantic ValidationError)

def test_predict_batch(client):
    payload = {
        "usagers": [
            {
                "anciennete_poste_ans": 2.0,
                "niveau_diplome": "Bac",
                "code_insee_commune": "59000",
                "code_rome_vise": "A1201",
                "est_allocataire": 0,
                "synthese_entretien": "Candidat debutant."
            },
            {
                "anciennete_poste_ans": 10.0,
                "niveau_diplome": "Bac+5",
                "code_insee_commune": "69001",
                "code_rome_vise": "M1805",
                "est_allocataire": 1,
                "synthese_entretien": "Cadre tres experimente."
            }
        ]
    }
    response = client.post("/predict/batch", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 2
    assert len(data["predictions"]) == 2
