import json

nb_path = 'journal-de-bord.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

normalized_cells = [
"""## 📅 Session du 2026-05-15 : Cadrage et Architecture Agentique

**Objectifs du jour :**
- Analyser le sujet et définir l'architecture globale du projet (Harness, rôles, skills).

**Actions réalisées :**
- Analyse du `sujet.md` pour comprendre les enjeux (classification multimodale, déséquilibre, éthique).
- Création de la charte de collaboration (`agent.md`).
- Initialisation du dépôt Git et création d'un `.gitignore` standard.
- Conception de l'équipe virtuelle (Data Scientist, ML Engineer, Ethicien, Tech Lead) dans `.agents/roles/`.
- Création de 7 recettes techniques (Skills) dans `.agents/skills/`.
- Mise en place des Micro-Workflows (QA Loop, Experiment Loop).

**Décisions / Remarques :**
- Tous les Skills ont été intégrés dans le système global de l'assistant pour garantir leur application continue.""",

"""## 📅 Session du 2026-05-25 : Cadrage Métier et Initialisation EDA

**Objectifs du jour :**
- Définir le cadrage métier et démarrer l'exploration des données.

**Actions réalisées :**
- Remplissage du Cadrage métier (Section 1) basé sur le besoin d'aiguillage.
- Identification des données et rédaction du dictionnaire de variables (Section 2).
- Détection des variables sensibles (`nationalite_hors_ue`, `age`) pour l'audit éthique.
- Initialisation de l'EDA avec le chargement des données et la distribution de la cible.

**Décisions / Remarques :**
- Le but premier sera de minimiser les faux négatifs sur la classe 2 (Risque > 12 mois) car c'est là que réside le risque humain et financier majeur.""",

"""## 📅 Session du 2026-06-05 : Acquisition des données

**Objectifs du jour :**
- Sécuriser et documenter le processus d'acquisition des données.

**Actions réalisées :**
- Validation et complétion de la Partie 2 du notebook.
- Intégration du hachage MD5 dans la phase de chargement pour la reproductibilité.
- Mise à jour du dictionnaire des variables (précision des unités).
- Ajout d'une exigence de conformité éthique (Disparate Impact).

**Décisions / Remarques :**
- Utilisation explicite du hachage cryptographique pour sécuriser toute modification du dataset.""",

"""## 📅 Session du 2026-06-16 : Exploration et Analyse des Données (EDA)

**Objectifs du jour :**
- Réaliser l'analyse exploratoire complète des données tabulaires.

**Actions réalisées :**
- Réalisation de la Partie 3 (Qualité des données, valeurs manquantes, doublons).
- Ajout de visualisations avec Seaborn (distributions et corrélations).
- Preuve chiffrée du Disparate Impact sur l'âge et la nationalité (crosstab).
- Rédaction de la synthèse EDA mettant en avant 3 axes critiques.

**Décisions / Remarques :**
- Mise en lumière précoce des problèmes éthiques dans l'EDA pour justifier les futures techniques de remédiation.""",

"""## 📅 Session du 2026-06-27 : Analyse Textuelle (NLP) et Clôture de l'EDA

**Objectifs du jour :**
- Finaliser l'EDA en intégrant l'analyse textuelle et lancer l'audit qualité.

**Actions réalisées :**
- Ajout d'une analyse Textuelle (NLP) sur `synthese_entretien` justifiant le TF-IDF.
- Restructuration de la synthèse de l'EDA en 6 points cardinaux.
- Lancement d'un workflow `/delegate` d'audit : nettoyage graphique, ajout Data-Viz et limites statistiques (V de Cramer).

**Décisions / Remarques :**
- Le choix du TF-IDF a été acté officiellement par rapport au Deep Learning pour garantir l'explicabilité (AI Act).""",

"""## 📅 Session du 2026-07-07 : Préparation des données (Partie 4)

**Objectifs du jour :**
- Construire le pipeline de transformation des données (Pre-processing).

**Actions réalisées :**
- Implémentation du `train_test_split` stratifié (80/20).
- Feature engineering pour réduire la cardinalité (`departement`, `famille_rome`).
- Construction d'un `ColumnTransformer` anti-Data Leakage (Imputation, Scaler, OneHot, Ordinal, TF-IDF).
- Optimisation de la mémoire vive via un casting strict Pandas.
- Création dynamique de 4 scénarios d'inférence (S1 à S4) et sérialisation via `joblib`.
- Implémentation d'assertions (`assert`) strictes pour l'intégrité.

**Décisions / Remarques :**
- L'approche SMOTE a été écartée au profit d'une pondération algorithmique (`class_weight='balanced'`), plus compatible avec les matrices creuses du NLP.""",

"""## 📅 Session du 2026-07-18 : Modélisation et MLflow (Partie 5)

**Objectifs du jour :**
- Entraîner, évaluer et sélectionner le meilleur modèle d'apprentissage.

**Actions réalisées :**
- Configuration d'un serveur MLflow local (`sqlite:///mlflow.db`).
- Résolution des erreurs de sérialisation via `cloudpickle`.
- Benchmark des modèles (Régression Logistique, Random Forest, LightGBM) en utilisant le F1-Macro.
- Exécution d'un Duel Final par `GridSearchCV` (LightGBM vs Random Forest).
- Victoire du LightGBM optimisé (`max_depth=5`, F1-Macro 0.7030).
- Analyse métier de la Matrice de Confusion validant le principe "No Mercy".

**Décisions / Remarques :**
- Le modèle accepte de générer des Faux Positifs pour garantir un haut Recall (69%) sur les chômeurs longue durée.""",

"""## 📅 Session du 2026-07-29 : Arbitrages, Éthique & Explicabilité (Partie 5 & 6)

**Objectifs du jour :**
- Valider le modèle sous le prisme de l'éthique (AI Act) et de l'explicabilité.

**Actions réalisées :**
- Ajout formel de la Model Card pour le LightGBM.
- Évaluation croisée des 4 scénarios (S1 à S4) et calcul de la latence (Green IT).
- Génération du graphique d'explicabilité *Feature Importance* (Top 15).
- Calcul du *Disparate Impact* (S1 vs S2) et analyse critique du "Fairness through Blindness".

**Décisions / Remarques :**
- Validation officielle du scénario S2 (Éthique) pour le déploiement. C'est le meilleur compromis entre conformité légale et performance.""",

"""## 📅 Session du 2026-08-09 : Audit final et Consolidation

**Objectifs du jour :**
- Sécuriser le notebook, réviser les objectifs de performance et finaliser la documentation.

**Actions réalisées :**
- Restauration complète du notebook suite à un écrasement accidentel.
- Révision de la cible théorique du F1-Macro à 0.60 pour assumer la contrainte *Privacy by Design*.
- Résolution d'un bug majeur d'application des hyperparamètres (les kwargs `clf__` étaient ignorés).
- Sérialisation correcte des pipelines des 4 scénarios (`joblib.dump`).
- Rédaction de la justification métier (le modèle agit comme un 'radar préventif' épaulé par un fallback).
- Démonstration mathématique annexe sur la Régression Logistique.

**Décisions / Remarques :**
- Baisse de performance assumée. La sécurité est garantie par le seuil de confiance à 65% (filet humain).""",

"""## 📅 Session du 2026-08-19 : Standardisation MLOps & Sauvegarde (Partie 6.9)

**Objectifs du jour :**
- Optimiser et standardiser les artefacts générés en vue de l'industrialisation.

**Actions réalisées :**
- Remplacement global des extensions `.pkl` par `.joblib` pour les préprocesseurs et pipelines.
- Résolution des Warnings Windows & erreurs SQLite MLflow (variable `LOKY_MAX_CPU_COUNT`, désactivation autologging pendant GridSearchCV).
- Filtrage ciblé des `UserWarning` Scikit-Learn.
- Exportation du pipeline optimisé (`pipeline_production.joblib`) et des métadonnées enrichies (`pipeline_production.json`).
- Installation de la dépendance `shap`.

**Décisions / Remarques :**
- Suppression du suffixe `_S2` dans le nom de l'artefact final pour garantir une interface agnostique au service API.""",

"""## 📅 Session du 2026-08-30 : Industrialisation et API FastAPI (Partie 8)

**Objectifs du jour :**
- Développer, déboguer et conteneuriser l'API de prédiction.

**Actions réalisées :**
- Débogage de l'API FastAPI (erreur de désynchronisation de version `scikit-learn` entre entraînement et inférence). Fixation des versions dans `requirements.txt`.
- Mise à jour de l'API pour utiliser `model_dump()` au lieu de `dict()`.
- Création et paramétrage de l'infrastructure Docker et CI/CD (GitHub Actions).
- Génération d'un `README.md` exhaustif décrivant l'architecture et les commandes.

**Décisions / Remarques :**
- L'API démarre correctement avec l'artefact sérialisé et les tests unitaires pytest passent.""",

"""## 📅 Session du 2026-09-10 : Regards Critiques & Éthique de l'IA (Annexe C)

**Objectifs du jour :**
- Documenter formellement les choix techniques et éthiques pour la soutenance.

**Actions réalisées :**
- Création de l'Annexe C (Regards critiques sur la modélisation).
- Justification du retrait de l'Âge (lutte contre le Disparate Impact).
- Justification NLP : TF-IDF (Boîte Blanche) vs Deep Learning (Boîte Noire).
- Explication de la gestion de la Cardinalité et du Sur-apprentissage.
- Ajout de perspectives pour le passage à l'échelle (Scale-up).
- Intégration de réflexions sur le Paradoxe de la boucle de rétroaction et le Biais d'automatisation.

**Décisions / Remarques :**
- Le modèle actuel est robuste pour un MVP, mais l'architecture devra évoluer lors d'un passage à l'échelle.""",

"""## 📅 Session du 2026-09-21 : Monitoring API (Prometheus & Grafana)

**Objectifs du jour :**
- Superviser les performances techniques et métiers de l'API de prédiction.

**Actions réalisées :**
- Intégration de `prometheus-fastapi-instrumentator` à l'API.
- Exposition du endpoint `/metrics` et création de compteurs/histogrammes métiers.
- Ajout du service Grafana dans `docker-compose.yml`.
- Configuration automatique (provisioning) de la datasource Prometheus.
- Création et montage d'un Dashboard Métier pour visualiser le taux de fallback et les prédictions.

**Décisions / Remarques :**
- L'observabilité temps-réel permet de surveiller immédiatement le taux de recours au conseiller (Fallback).""",

"""## 📅 Session du 2026-10-02 : Documentation et Amélioration Continue (Partie 9)

**Objectifs du jour :**
- Finaliser la stratégie de suivi en production et d'amélioration continue.

**Actions réalisées :**
- Détail des métriques de Monitoring (Ch 9.1) en distinguant temps réel (Prometheus) et batch (MLflow).
- Déplacement du paragraphe sur la Boucle de Rétroaction (Ch 9.2) pour anticiper les effets de bord.
- Complétion du Glossaire Métier et Technique (Annexe A).
- Enrichissement des Sources & Bibliographie (Annexe B) avec l'AI Act et les standards.

**Décisions / Remarques :**
- Le workbook est désormais prêt pour la soutenance, démontrant une approche MLOps et éthique de bout en bout."""
]

# The first cell is the `# Journal de bord` title, so entries start at index 1
entry_index = 0
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        if '2026' in source:
            if entry_index < len(normalized_cells):
                cell['source'] = [line + '\n' for line in normalized_cells[entry_index].split('\n')]
                entry_index += 1

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"Notebook mis à jour avec {entry_index} cellules normalisées.")
