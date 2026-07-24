# 💼 Orientation et Tri Multimodal des Demandeurs d'Emploi — System MLOps & AI Act

![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.41-red.svg)
![MLflow](https://img.shields.io/badge/MLflow-3.14-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-cyan.svg)
![AI Act Compliance](https://img.shields.io/badge/AI%20Act-Conforme%20(S2)-purple.svg)

> **Projet de Certification IA — Parcours ATOS Atlas IA**  
> **Auteur :** Franck BEUGNET  
> **Cas d'Usage :** Outil d'Aide à la Décision (HITL) pour le tri et l'orientation des demandeurs d'emploi.

---

## 📌 Présentation du Projet

Ce projet implémente une solution IA end-to-end de classification multiclasse multimodale (données tabulaires + texte libre NLP) permettant d'estimer le délai de retour à l'emploi des usagers (`0: < 6 mois`, `1: 6-12 mois`, `2: > 12 mois`).

Conçu selon les exigences d'audit et d'éthique de l'**AI Act** et du **RGPD**, le pipeline retient le scénario **S2 (Éthique)** en appliquant le principe de *Privacy by Design* (retrait de l'âge et de l'origine) couplé à une gestion explicite de l'incertitude (seuil de confiance minimal à 65% avec escalade vers un conseiller humain *Human-In-The-Loop*).

---

## 📁 Architecture du Dépôt

```text
certification_upskilling_ia/
├── api/                        # Service Backend REST (FastAPI)
│   ├── __init__.py
│   ├── main.py                 # Application FastAPI & endpoints (/predict, /health, /train)
│   └── schemas.py              # Schémas de validation Pydantic v2
├── ui/                         # Interface Frontend Conseiller (Streamlit)
│   └── app.py                  # Dashboard interactif conseillers & visualisations
├── models/                     # Artefacts de production sérialisés
│   ├── pipeline_production.joblib  # Pipeline complet S2 (LightGBM + Preprocessor NLP)
│   ├── pipeline_production.json    # Fichier de métadonnées (Model Card technique)
│   └── preprocessor_S*.joblib      # Scénarios de prétraitement
├── data/                       # Jeu de données & documentation
│   ├── dataset_trajectoire_emploi.csv  # Dataset source usagers
│   └── DATASHEET.md            # Fiche d'identité de la donnée (Gebru et al., 2018)
├── tests/                      # Suite de tests automatisés (Pytest)
│   ├── test_api.py             # Tests unitaires & intégration API
│   └── test_pipeline.py        # Tests de chargement et prédiction modèle
├── .github/workflows/          # Pipeline CI/CD GitHub Actions
│   └── ci.yml
├── Dockerfile                  # Image Docker multi-stage build Python 3.12
├── docker-compose.yml          # Orchestration multi-services (API + UI)
├── cas-usage.ipynb             # Notebook de synthèse & démonstration
├── cas-usage.py                # Script Python miroir reproductible
├── journal-de-bord.ipynb       # Journal de suivi des sessions de travail
├── requirements.txt            # Dépendances Python versionnées
└── README.md                   # Documentation principale du dépôt
```

---

## 🚀 Démarrage Rapide

### 1. Prérequis & Installation Locale

Assurez-vous de disposer de Python 3.12+ et de Git.

```bash
# Créer et activer un environnement virtuel
python -m venv venv
# Sur Windows :
venv\Scripts\activate
# Sur Linux/macOS :
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

---

## 🖥️ Lancement des Services (Backend & Frontend)

### Option A : Lancement Local (Recommandé pour le développement)

#### 1. Démarrer le Backend (API FastAPI)

Dans un premier terminal :

```bash
uvicorn api.main:app --reload --port 8000
```

- **API REST :** `http://localhost:8000`
- **Documentation interactive Swagger (OpenAPI) :** `http://localhost:8000/docs`
- **Endpoint de Santé :** `http://localhost:8000/health`

#### 2. Démarrer le Frontend (Interface Streamlit)

Dans un second terminal :

```bash
streamlit run ui/app.py --server.port 8501
```

- **Interface Web Conseiller :** `http://localhost:8501`

---

### Option B : Lancement avec Docker Compose (Recommandé pour la Production)

Lancez l'intégralité de la pile conteneurisée (API + UI) en une seule commande :

```bash
docker-compose up --build
```

- **API FastAPI (Conteneur) :** `http://localhost:8000/docs`
- **UI Streamlit (Conteneur) :** `http://localhost:8501`

Pour stopper les conteneurs :

```bash
docker-compose down
```

---

## 🧪 Exécution des Tests

Le projet intègre une suite complète de tests unitaires et d'intégration avec `pytest` :

```bash
pytest tests/ -v
```

---

## 📊 Suivi des Expérimentations (MLflow)

Toutes les itérations de modélisation et métriques (F1-Macro, matrices de confusion) sont enregistrées dans la base SQLite locale `mlflow.db`.

Pour visualiser l'interface MLflow :

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Accédez au tableau de bord sur `http://localhost:5000`.

---

## 📄 Documentation & Traçabilité (AI Act)

- **Datasheet du Dataset :** Consulter [data/DATASHEET.md](data/DATASHEET.md) (Format Gebru et al., 2018).
- **Model Card du Modèle :** Consulter [models/pipeline_production.json](models/pipeline_production.json) (Format Mitchell et al., 2019).

---

## 👤 Auteur & Contact

- **Auteur :** Franck BEUGNET (`franck.beugnet@atos.net`)
- **Cadre :** Certification Upskilling IA — ATOS Atlas IA (Promo 2026)
