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
├── api/                         # Service backend FastAPI
│   ├── __init__.py
│   ├── main.py                  # Points d'entrée API (/predict, /health, /train)
│   └── schemas.py               # Schémas Pydantic v2 pour validation
├── ui/                          # Interface conseiller Streamlit
│   └── app.py                   # Dashboard décisionnel et visualisations
├── data/                        # Données sources et documentation de référence
│   ├── dataset_trajectoire_emploi.csv
│   ├── DATASHEET.md
│   └── ...
├── docs/                        # Supports de cours, audits, méthodologie
│   ├── 01_*.md
│   ├── 02_*.md
│   ├── 03_*.md
│   ├── 04_*.md
│   └── 05_*.md
├── models/                      # Artefacts et modèles de production
│   ├── pipeline_production.joblib
│   ├── pipeline_production.json
│   ├── preprocessor_S1.joblib
│   ├── preprocessor_S2.joblib
│   ├── preprocessor_S3.joblib
│   └── preprocessor_S4.joblib
├── mlruns/                      # Expériences et artefacts MLflow
│   └── ...
├── tests/                       # Suite de tests Python (Pytest)
│   ├── __init__.py
│   ├── test_api.py
│   └── test_pipeline.py
├── .github/                     # CI/CD GitHub Actions
│   └── workflows/
│       └── ci.yml
├── .agents/                     # Configuration d'agents / rôles / compétences
│   ├── memory/
│   ├── roles/
│   ├── skills/
│   └── workflows/
├── Dockerfile                   # Image Docker du projet
├── docker-compose.yml           # Orchestration API + UI
├── cas-usage.ipynb              # Notebook de démonstration et synthèse
├── cas-usage.py                 # Script Python reproductible
├── journal-de-bord.ipynb        # Journal de travail / suivi du projet
├── fix_jobs.py                  # Script utilitaire pour jobs/traçabilité
├── update_nb.py                 # Script de mise à jour notebooks
├── index.md                     # Index documentaire du dépôt
├── sujet.md                     # Sujet officiel du cas d'usage
├── agent.md                     # Documentation de l'agent/assistant
├── requirements.txt             # Dépendances Python du projet
├── README.md                    # Documentation principale du dépôt
├── diagramme.png                # Schéma d'architecture / flux
├── mlflow.db                    # Base SQLite locale MLflow
├── .gitignore
├── .pytest_cache/               # Cache de test local (généré)
├── venv/                        # Environnement virtuel local (généré)
├── __pycache__/                # Cache Python local (généré)
└── .git/                        # Dossier Git (non source, local)
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
