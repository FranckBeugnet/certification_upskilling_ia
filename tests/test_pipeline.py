import pytest
import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["LOKY_MAX_CPU_COUNT"] = "1"

import joblib
import pandas as pd
import numpy as np
from pathlib import Path

def extract_text(X):
    if hasattr(X, "iloc"):
        return X.iloc[:, 0].fillna("").astype(str)
    return pd.Series(X).fillna("").astype(str)

import __main__
setattr(__main__, "extract_text", extract_text)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "pipeline_production.joblib"

def test_model_file_exists():
    assert MODEL_PATH.exists(), f"Le fichier modèle {MODEL_PATH} est introuvable."

def test_pipeline_prediction():
    pipeline = joblib.load(MODEL_PATH)
    
    sample_data = pd.DataFrame([{
        "anciennete_poste_ans": 4.0,
        "niveau_diplome": "Bac+2",
        "code_insee_commune": "75101",
        "code_rome_vise": "M1805",
        "est_allocataire": 1,
        "synthese_entretien": "Profil experimente en support utilisateur."
    }])
    
    sample_data["departement"] = sample_data["code_insee_commune"].astype(str).str[:2]
    sample_data["famille_rome"] = sample_data["code_rome_vise"].astype(str).str[0]
    
    probas = pipeline.predict_proba(sample_data)
    assert probas.shape == (1, 3), "La sortie des probabilités doit être de dimension (1, 3)."
    assert np.isclose(np.sum(probas), 1.0), "La somme des probabilités doit valoir 1.0."
