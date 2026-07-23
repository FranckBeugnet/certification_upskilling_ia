import streamlit as st
import pandas as pd
import requests
import json
import joblib
import numpy as np
from pathlib import Path

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Orientation Demandeurs d'Emploi — France Travail",
    page_icon="💼",
    layout="wide"
)

API_URL = "http://localhost:8000"
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "pipeline_production.joblib"

st.title("💼 Assistant d'Orientation & Tri Multimodal — France Travail")
st.markdown("""
> **Système d'Aide à la Décision (Human-In-The-Loop)**  
> Ce modèle éthique (S2) aide les conseillers à recommander le bon niveau d'accompagnement tout en garantissant la conformité **AI Act & RGPD** (*Privacy by Design* : sans âge ni origine).
""")

st.sidebar.header("📋 Informations du demandeur d'emploi")

# Formulaire latéral
anciennete = st.sidebar.number_input("Ancienneté dernier emploi (années)", min_value=0.0, max_value=50.0, value=3.5, step=0.5)
diplome = st.sidebar.selectbox("Plus haut diplôme obtenu", ["Sans diplôme", "Bac", "Bac+2", "Bac+5"], index=1)
code_insee = st.sidebar.text_input("Code INSEE Commune (5 chiffres)", value="75101", max_chars=5)
code_rome = st.sidebar.text_input("Code ROME métier visé (5 chars)", value="M1805", max_chars=5)
allocataire = st.sidebar.radio("Statut allocataire", ["Non (0)", "Oui (1)"], index=1)
est_allocataire_val = 1 if "Oui" in allocataire else 0

st.sidebar.subheader("📝 Synthese d'entretien (NLP)")
synthese = st.sidebar.text_area(
    "Notes du conseiller",
    value="Le candidat présente une bonne expérience professionnelle mais manque de confiance sur les outils numériques modernes. Motivation élevée pour une reconversion.",
    height=150
)

submit_btn = st.sidebar.button("🚀 Évaluer le dossier", type="primary")

col1, col2 = st.columns([1, 1])

if submit_btn:
    payload = {
        "anciennete_poste_ans": float(anciennete),
        "niveau_diplome": str(diplome),
        "code_insee_commune": str(code_insee),
        "code_rome_vise": str(code_rome),
        "est_allocataire": int(est_allocataire_val),
        "synthese_entretien": str(synthese)
    }

    st.subheader("📊 Résultat du tri & Prédiction du délai")

    # Tentative d'appel à l'API FastAPI, sinon inférence directe localement
    response_data = None
    try:
        res = requests.post(f"{API_URL}/predict", json=payload, timeout=3)
        if res.status_code == 200:
            response_data = res.json()
    except Exception:
        # Inférence directe locale de secours
        if MODEL_PATH.exists():
            pipeline = joblib.load(MODEL_PATH)
            df_in = pd.DataFrame([payload])
            df_in["departement"] = df_in["code_insee_commune"].astype(str).str[:2]
            df_in["famille_rome"] = df_in["code_rome_vise"].astype(str).str[0]
            
            probas = pipeline.predict_proba(df_in)[0]
            pred = int(np.argmax(probas))
            conf = float(probas[pred])
            labels = {0: "Rapide (< 6 mois)", 1: "Moyen (6 à 12 mois)", 2: "Risque de longue durée (> 12 mois)"}
            fallback = conf < 0.65
            
            response_data = {
                "prediction": pred,
                "label": labels[pred],
                "probabilities": {labels[i]: float(probas[i]) for i in range(len(probas))},
                "confidence": round(conf, 4),
                "fallback": fallback,
                "message": f"⚠️ Confiance insuffisante ({conf:.1%}). Escalade requise." if fallback else f"✅ Orientation : {labels[pred]} ({conf:.1%})"
            }

    if response_data:
        conf_pct = response_data["confidence"] * 100
        label = response_data["label"]
        fallback = response_data["fallback"]

        with col1:
            st.metric(label="Orientation recommandée", value=label)
            st.progress(response_data["confidence"])
            st.write(f"**Score de confiance :** `{conf_pct:.1f}%` (Seuil minimal : `65.0%`) ")

            if fallback:
                st.error("⚠️ **ALERTE HUMAN-IN-THE-LOOP (HITL)**")
                st.warning("""
                Le niveau de confiance du modèle est sous le seuil de 65%.  
                **Action requise :** L'IA s'abstient et remet la décision finale d'orientation au conseiller humain.
                """)
            else:
                st.success("✅ **CONFIRMATION AUTOMATIQUE**")
                st.info("Le modèle émet une recommandation à haute confiance.")

        with col2:
            st.subheader("🎯 Distribution des probabilités")
            proba_df = pd.DataFrame(
                list(response_data["probabilities"].items()),
                columns=["Classe", "Probabilité"]
            )
            st.bar_chart(proba_df.set_index("Classe"))
    else:
        st.error("Impossible de contacter l'API REST ni de charger le modèle local.")
