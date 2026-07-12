# Skill : Interface Graphique avec Streamlit 🖥️

**Agent référent :** ML Engineer

## 🎯 Objectif
Développer une interface utilisateur simple, intuitive et fonctionnelle pour que les conseillers (non-techniciens) puissent interroger le modèle d'IA et consulter l'historique, conformément au cahier des charges.

## 🛠️ Règles d'implémentation
1. **Architecture Front/Back Séparée :**
   - Streamlit ne DOIT PAS exécuter le modèle directement ni charger le `.pkl`.
   - L'application Streamlit agit uniquement comme un client HTTP qui fait des requêtes vers l'API FastAPI (sur `http://localhost:8000/predict`).
2. **Le Formulaire de Saisie (Onglet 1) :**
   - Créer un formulaire (`st.form`) pour recueillir les informations de l'usager.
   - Les variables catégorielles (Niveau de diplôme) doivent utiliser des menus déroulants (`st.selectbox`).
   - L'âge et le code INSEE doivent avoir des contrôles de saisie de base (ex: pas d'âge négatif).
   - Un grand champ de texte libre (`st.text_area`) pour la "Synthèse de l'entretien".
3. **Restitution des Résultats :**
   - L'affichage doit être lisible pour un humain (ex: "Risque Faible" plutôt que "Classe 0").
   - Utiliser des jauges de couleur (`st.progress` ou HTML/CSS) pour afficher la *confiance* de la prédiction.
   - Si la confiance est sous le seuil de rejet, afficher une alerte rouge demandant une "Escalade Humaine".
   - Afficher l'explicabilité : Intégrer le graphe local généré (ou les "Top Features") expliquant pourquoi cette décision a été prise.
4. **L'Historique (Onglet 2) :**
   - Interroger la route `GET /history` de l'API.
   - Afficher les requêtes passées sous forme de tableau de bord (`st.dataframe`).
   - Permettre au conseiller d'envoyer un feedback ("Je suis d'accord" ou "Je ne suis pas d'accord") qui appellera la route `/retrain` de FastAPI.
