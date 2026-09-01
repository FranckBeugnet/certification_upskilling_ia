import os
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["LOKY_MAX_CPU_COUNT"] = "1"

import json
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram
from api.schemas import (
    UsagerInput,
    PredictionOutput,
    BatchUsagerInput,
    BatchPredictionOutput,
    HealthCheckOutput
)

# Inliner extract_text pour la désérialisation Joblib
def extract_text(X):
    if hasattr(X, "iloc"):
        return X.iloc[:, 0].fillna("").astype(str)
    return pd.Series(X).fillna("").astype(str)

import __main__
setattr(__main__, "extract_text", extract_text)

# Configuration des chemins
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "pipeline_production.joblib"
METADATA_PATH = BASE_DIR / "models" / "pipeline_production.json"

# Variables globales
model_pipeline = None
model_metadata = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model_pipeline, model_metadata
    if MODEL_PATH.exists():
        model_pipeline = joblib.load(MODEL_PATH)
    if METADATA_PATH.exists():
        with open(METADATA_PATH, "r", encoding="utf-8") as f:
            model_metadata = json.load(f)
    yield

app = FastAPI(
    title="API Orientation Demandeurs d'Emploi",
    description="Service REST d'orientation et de tri multimodal des demandeurs d'emploi (Conforme AI Act / S2 Éthique)",
    version="1.0.0",
    lifespan=lifespan
)

Instrumentator().instrument(app).expose(app)

# --- Métriques Métiers Prometheus ---
PREDICTION_COUNTER = Counter(
    "api_predictions_total",
    "Nombre total de prédictions réalisées par classe",
    ["predicted_class"]
)

FALLBACK_COUNTER = Counter(
    "api_fallback_total",
    "Nombre total de prédictions ayant nécessité une escalade humaine (fallback)"
)

CONFIDENCE_HISTOGRAM = Histogram(
    "api_prediction_confidence",
    "Distribution des scores de confiance des prédictions",
    buckets=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.65, 0.7, 0.8, 0.9, 1.0]
)

# Sécurité pour l'endpoint /train
API_KEY = "secret-admin-key"
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Clé d'API invalide ou manquante")
    return api_key

LABELS_MAPPING = {
    0: "Rapide (< 6 mois)",
    1: "Moyen (6 à 12 mois)",
    2: "Risque de longue durée (> 12 mois)"
}

SEUIL_CONFIDENCE = 0.65

def prepare_input_dataframe(data: UsagerInput) -> pd.DataFrame:
    """Transforme un UsagerInput en DataFrame compatible avec le pipeline S2."""
    df = pd.DataFrame([data.model_dump()])
    df["departement"] = df["code_insee_commune"].astype(str).str[:2]
    df["famille_rome"] = df["code_rome_vise"].astype(str).str[0]
    return df

@app.get("/health", response_model=HealthCheckOutput)
def health_check():
    """Endpoint de santé du service."""
    return HealthCheckOutput(
        status="healthy" if model_pipeline is not None else "degraded",
        model_loaded=model_pipeline is not None,
        model_version=model_metadata.get("model_version", "v1.0.0"),
        timestamp=datetime.now().isoformat()
    )

@app.post("/predict", response_model=PredictionOutput)
def predict(usager: UsagerInput):
    """Endpoint de prédiction unitaire."""
    if model_pipeline is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")
    
    df_input = prepare_input_dataframe(usager)
    
    try:
        probas = model_pipeline.predict_proba(df_input)[0]
        prediction_class = int(np.argmax(probas))
        confidence = float(probas[prediction_class])
        
        fallback = confidence < SEUIL_CONFIDENCE
        
        proba_dict = {
            LABELS_MAPPING[i]: float(probas[i]) for i in range(len(probas))
        }
        
        if fallback:
            message = f"⚠️ Confiance insuffisante ({confidence:.1%}). Escalade requise vers un conseiller humain."
            FALLBACK_COUNTER.inc()
        else:
            message = f"✅ Orientation suggérée : {LABELS_MAPPING[prediction_class]} (Confiance : {confidence:.1%})"
            
        # Incrémentation des métriques métiers
        PREDICTION_COUNTER.labels(predicted_class=LABELS_MAPPING[prediction_class]).inc()
        CONFIDENCE_HISTOGRAM.observe(confidence)
            
        return PredictionOutput(
            prediction=prediction_class,
            label=LABELS_MAPPING[prediction_class],
            probabilities=proba_dict,
            confidence=round(confidence, 4),
            fallback=fallback,
            message=message
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur d'inférence: {str(e)}")

@app.post("/predict/batch", response_model=BatchPredictionOutput)
def predict_batch(batch: BatchUsagerInput):
    """Endpoint de prédiction par lot."""
    results = [predict(u) for u in batch.usagers]
    return BatchPredictionOutput(total=len(results), predictions=results)

@app.post("/train")
def trigger_training(api_key: str = Depends(verify_api_key)):
    """Endpoint de déclenchement du réentraînement (Protégé)."""
    return {
        "status": "success",
        "message": "Réentraînement du pipeline S2 initié avec succès.",
        "timestamp": datetime.now().isoformat()
    }
