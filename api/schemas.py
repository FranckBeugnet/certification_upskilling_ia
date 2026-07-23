from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class UsagerInput(BaseModel):
    anciennete_poste_ans: float = Field(
        ..., ge=0.0, le=50.0, description="Ancienneté dans le dernier emploi en années"
    )
    niveau_diplome: str = Field(
        ..., description="Plus haut diplôme obtenu: 'Sans diplôme', 'Bac', 'Bac+2', 'Bac+5'"
    )
    code_insee_commune: str = Field(
        ..., min_length=5, max_length=5, description="Code géo INSEE (ex: '75101')"
    )
    code_rome_vise: str = Field(
        ..., min_length=5, max_length=5, description="Code ROME métier visé (ex: 'M1805')"
    )
    est_allocataire: int = Field(
        ..., ge=0, le=1, description="Statut indemnisation (0: Non, 1: Oui)"
    )
    synthese_entretien: str = Field(
        default="", description="Notes textuelles saisies par le conseiller lors de l'entretien"
    )

class PredictionOutput(BaseModel):
    prediction: int = Field(..., description="Classe prédite (0, 1 ou 2)")
    label: str = Field(..., description="Libellé de la classe d'orientation métier")
    probabilities: Dict[str, float] = Field(..., description="Probabilités pour chaque classe")
    confidence: float = Field(..., description="Niveau de confiance du modèle (max probabilité)")
    fallback: bool = Field(..., description="Vrai si la confiance est sous le seuil (65%) -> Escalade Humaine")
    message: str = Field(..., description="Message explicatif pour le conseiller")

class BatchUsagerInput(BaseModel):
    usagers: List[UsagerInput]

class BatchPredictionOutput(BaseModel):
    total: int
    predictions: List[PredictionOutput]

class HealthCheckOutput(BaseModel):
    status: str
    model_loaded: bool
    model_version: Optional[str] = "v1.0.0"
    timestamp: str
