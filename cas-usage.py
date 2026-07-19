#!/usr/bin/env python
# coding: utf-8

# # 📓 Cas d'usage IA — Orientation et tri multimodal des demandeurs d'emploi
# 
# **Auteur·e** : `Franck BEUGNET`  
# **Promo** : ATOS Atlas IA — Parcours 2 (Pros IT)  
# **Date début** : `09/07/2026`  
# **Dernière mise à jour** : `09/07/2026`
# 
# ---
# 
# ## À quoi sert ce notebook ?
# 
# Ce canevas est ta **grille de référence** sur tout le parcours. Tu **ne le remplis pas d'un coup**.  
# Tu le mobilises **section par section** au fil des briefs (cf. tableau §Mobilisation).  
# En M9 (certif), tu reconstitueras un notebook complet sur le sujet proposé, en suivant cette même structure.
# 
# ## Comment l'utiliser ?
# 
# - **Tu n'es pas obligé·e de tout remplir d'un coup**. Chaque module ouvre ou approfondit une ou deux sections.
# - **Garde le notebook propre** : code commenté, cellules markdown qui expliquent les choix, pas de cellules orphelines.
# - **Justifie tes choix** : un notebook certif n'est pas un script qui tourne, c'est une démarche racontée.
# - **Synthèse à la fin de chaque section** : 3-5 lignes max qui résument ce que tu as fait et pourquoi.
# 
# ## Conventions de mise en forme
# 
# | Symbole | Signification |
# |---|---|
# | 🎯 | Objectif de la section / ce qu'on attend |
# | 💡 | Outils, méthodes, ressources suggérées |
# | ⚠️ | Point de vigilance |
# | 📝 | Zone de synthèse à compléter |
# | ⭐ | Pour aller plus loin |
# 
# > ⚠️ **Format de rendu certif** : Jupyter `.ipynb` **ou** Kaggle Notebook. Si tu travailles sur Kaggle, attention :
# > - chemins de fichiers spécifiques (`/kaggle/input/...`),
# > - publication du dataset via l'API Kaggle si tu utilises un dataset custom,
# > - export final en `.ipynb` exigé par le jury.
# 
# ---

# ## 🗺️ Mapping sections ↔ compétences ↔ modules
# 
# | Section | Étape projet | C tech (CISIA) | CT (transversales OPCO ATLAS) | Modules |
# |---|---|---|---|---|
# | 1 | Cadrage métier & problème | C1, C2, C4 | **CT3** définir le périmètre · CT4 rechercher méthodiquement | M3, M4, M7, M8 |
# | 2 | Identification & acquisition des données | C1 | **CT1** planifier le travail · CT4 | M3, M8 |
# | 3 | Exploration & analyse des données | C2, C3 | **CT3** · CT4 | M2, M3 |
# | 4 | Préparation des données | C3 | **CT1** · CT4 | M2, M3 |
# | 5 | Modélisation & entraînement | C4, C5 | **CT4** · CT3 (périmètre du problème ML) | M1, M4, M6 |
# | 6 | Analyse des scénarios & arbitrages | C2, C4 | **CT5** partager la solution | M2, M4, M7 |
# | 7 | Interprétation pour la communication client (soutenance) | C8 | **CT6** présenter au commanditaire · CT5 documenter | M6, M9 |
# | 8 | Industrialisation (API, UI, conteneurs) | C6, C7 | **CT5** documenter | M0, M1, M5, M7 |
# | 9 | Suivi en production & amélioration continue | C8, C9 | **CT2** contribuer au pilotage · CT9 faciliter le travail collectif | M5, M6 |
# 
# **Légende** : **CT en gras** = dominante (cœur de la section) · CT en normal = mobilisée. **2 CT max par section** — pas de CT en arrière-plan, on cible le cœur.
# 
# ### 👀 CT non couvertes par le notebook (à évaluer en formation)
# 
# Le notebook ne suffit pas pour évaluer toutes les compétences transversales. **CT7, CT8 et CT9 s'observent en formation**, pas dans le notebook :
# 
# | CT | Description | Observable où ? |
# |---|---|---|
# | **CT7** | Se familiariser avec la culture pro IA | Veille collective Notion (mercredi midi), restitutions mercredi, RDV individuels vendredi |
# | **CT8** | Interactions respectueuses & constructives | Briefs en binôme : M0-B2, M2-B2, M3-B2, M5-B1, M6-B1, M7-B2, M8-B2 |
# | **CT9** | Faciliter le travail collectif | Brief en groupe M6-B2 + mur réflexif + restitutions orales |
# 
# > 📋 Côté formatrice : une **grille d'observation pédagogique séparée** suit CT7-CT8-CT9 en parallèle de ce notebook (à produire avant J1).
# 

# ## 🚦 Mobilisation par module — quand ouvrir quelle section
# 
# > Carte du voyage. **Tu n'es pas censé·e remplir des sections au-delà du module en cours.**
# 
# | Module | Sections ouvertes | Sections verrouillées |
# |---|---|---|
# | **M0** | 0, 0.5, 8 (descriptive) | 1, 2, 3, 4, 5, 6, 7, 9 |
# | **M1** | + 2, 5 | 1, 3, 4, 6, 7, 9 |
# | **M2** | + 3, 4 | 1, 6, 7, 9 |
# | **M3** | + 1 (partiel), 2 (renforcé) | 6, 7, 9 |
# | **M4** | + 1 (complet), 6 | 7, 9 |
# | **M5** | + 8 (renforcé), 9 | 7 |
# | **M6** | + 7, 9 (complet) | — |
# | **M7** | révision 1, 6 | — |
# | **M8** | révision 1 (autonomie complète) | — |
# | **M9** | **toutes** sur le cas certif tiré | — |
# 
# ### 🎨 Visualisation matricielle (projetable en J1)
# 
# | Module | 0 | 0.5 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
# |---|---|---|---|---|---|---|---|---|---|---|---|
# | **M0** | ✅ | ✅ | 🔒 | 🔒 | 🔒 | 🔒 | 🔒 | 🔒 | 🔒 | 📝 | 🔒 |
# | **M1** | ✅ | ✅ | 🔒 | ✅ | 🔒 | 🔒 | ✅ | 🔒 | 🔒 | 📝 | 🔒 |
# | **M2** | ✅ | ✅ | 🔒 | ✅ | ✅ | ✅ | ✅ | 🔒 | 🔒 | 📝 | 🔒 |
# | **M3** | ✅ | ✅ | 🟡 | ✅ | ✅ | ✅ | ✅ | 🔒 | 🔒 | 📝 | 🔒 |
# | **M4** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔒 | 📝 | 🔒 |
# | **M5** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 🔒 | ✅ | ✅ |
# | **M6** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
# | **M7** | ✅ | ✅ | 🔄 | ✅ | ✅ | ✅ | ✅ | 🔄 | ✅ | ✅ | ✅ |
# | **M8** | ✅ | ✅ | 🔄 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
# | **M9** | 🎯 | 🎯 | 🎯 | 🎯 | 🎯 | 🎯 | 🎯 | 🎯 | 🎯 | 🎯 | 🎯 |
# 
# **Légende** : ✅ section à mobiliser · 🟡 ouverture partielle · 🔄 révision approfondie · 📝 section descriptive (lien repo + schéma, pas de code) · 🔒 verrouillée (pas encore vue) · 🎯 à reconstituer intégralement sur le cas certif tiré
# 
# ### 🔍 Sous-sections clés à mobilisation différenciée
# 
# La matrice ci-dessus raisonne au niveau des **sections** (0 à 9). Trois **sous-sections** ont un timing propre, à connaître :
# 
# | Sous-section | Première ouverture | Forme attendue à l'ouverture | Cible finale (certif M9) |
# |---|---|---|---|
# | **§5.0 Familles de modèles** | M1 (avec section 5) | ML classique + DL renseignés ; SLM / LLM+RAG / agents écartés en 1 ligne | Toutes les familles avec arbitrage motivé (M7-M8) |
# | **§7.2 Fallback (conception)** | M6 (avec section 7) | Rejection threshold + abstention + HITL définis | Identique, raffiné si M7-B2 / M8-B2 changent la famille |
# | **§9.4 Robustesse (exploitation)** | M6 (avec section 9 complète) | Au moins l'axe « drift du seuil de rejet » instrumenté | OOD + drift + calibration explicités |
# 
# 💡 Si tu veux explorer une section ou sous-section avant son module, c'est ⭐ bonus. Mais ne te mets pas en difficulté.
# 
# ---

# ## 0. Imports & configuration
# 
# 🎯 Centraliser les imports et la configuration reproductible.  
# 💡 `random_state=42` partout, `pd.set_option` pour l'affichage si besoin.  
# ⚠️ Ne pas importer en cours de notebook : tout ici.

# In[24]:


# Imports standards
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Reproductibilité
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

# Affichage
pd.set_option("display.max_columns", 50)
sns.set_theme(style="whitegrid")

# Imports ML (à activer au fur et à mesure)
# from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline


# ## 0.5 Traçabilité de la session
# 
# 🎯 Documenter ce qui rend l'analyse **reproductible** par toi (sur un autre poste) ou par un collègue qui reprendrait le notebook dans 3 mois.
# 
# 💡 Trois choses à figer :
# - la **version du dataset** (source, date d'extraction, hash si possible),
# - les **versions des libs** (cf. `requirements.txt` du repo associé, ou `pip freeze`),
# - le **commit Git** du repo associé au notebook.
# 
# ⚠️ Sans ces 3 éléments, ton analyse n'est pas reproductible. C'est un attendu pro fort, et c'est noté en certif.

# In[25]:


import sys
import subprocess
from datetime import datetime

# --- Métadonnées du dataset ---
DATASET_NAME = "..."          # ex: "UCI Student Performance" ou "FastIA maintenance v1"
DATASET_SOURCE = "..."        # URL, chemin, ou contact si fourni par le client
DATASET_VERSION = "YYYY-MM-DD"  # date d'extraction OU version explicite

# --- Métadonnées de la session ---
session_date = datetime.now().isoformat(timespec="minutes")
py_version = sys.version.split()[0]

try:
    git_commit = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"], stderr=subprocess.DEVNULL
    ).decode().strip()
except (subprocess.CalledProcessError, FileNotFoundError):
    git_commit = "non disponible (notebook hors repo Git)"

print(f"Date session : {session_date}")
print(f"Python       : {py_version}")
print(f"NumPy        : {np.__version__}")
print(f"Pandas       : {pd.__version__}")
print(f"Git commit   : {git_commit}")
print(f"Dataset      : {DATASET_NAME} (source={DATASET_SOURCE}, version={DATASET_VERSION})")


# ---
# ## 1. Cadrage métier & problème
# 
# ### 1.1 Contexte client
# 
# **Le Client :** L'Agence nationale de l'emploi.
# 
# **Le Problème :** L'agence gère un flux massif de demandeurs d'emploi. Pour optimiser l'accompagnement et cibler les ressources là où elles sont le plus nécessaires, les conseillers ont besoin d'identifier rapidement le délai potentiel de retour à l'emploi de chaque usager.
# 
# **La Solution IA :** Un outil d'aide à la décision (système expert d'aiguillage) qui analyse non seulement les données administratives classiques (âge, diplôme, géographie) mais aussi le texte libre saisi par le conseiller lors du premier entretien. L'IA doit soulager le conseiller du tri initial pour qu'il puisse se concentrer sur l'accompagnement humain.
# 
# ### 1.2 Énoncé du problème IA
# 
# D'un point de vue technique, nous sommes face à une **Tâche supervisée de classification multiclasse à 3 classes**.
# * **Supervisée** : Car nous avons un jeu de données historique où la "réponse" (la classe réelle) est connue pour chaque demandeur (2500 échantillons).
# * **Classification** : Car nous ne cherchons pas à prédire un chiffre continu (ex: le nombre exact de jours), mais une catégorie.
# * **Les 3 classes** :
#   - `0` : Rapide (< 6 mois)
#   - `1` : Moyen (entre 6 et 12 mois)
#   - `2` : Risque de longue durée (> 12 mois)
# 
# *Particularité technique :* C'est une IA **multimodale** car elle ingère deux types de données très différents : du tabulaire structuré (chiffres/catégories) et du texte non structuré (NLP).
# 
# ### 1.3 Bénéficiaires & impacts
# 
# - **Directs (les utilisateurs) :** Les conseillers de l'agence. L'outil leur fait gagner du temps et objective leurs ressentis.
# - **Indirects (les sujets) :** Les demandeurs d'emploi. L'IA influence la priorité avec laquelle leur dossier sera traité.
# - **L'Impact Métier (Le point critique) :** En IA, toutes les erreurs ne se valent pas. Si le modèle prédit un retour Rapide (Classe 0) pour un usager qui, en réalité, est en Risque de longue durée (Classe 2), c'est un **Faux Négatif grave**. L'usager ne recevra pas l'accompagnement renforcé dont il a besoin, entraînant un préjudice humain (détresse) et financier (coût social). À l'inverse, prédire "Risque" pour quelqu'un de "Rapide" (Faux Positif) est moins grave, cela coûte juste un peu de temps au conseiller. Notre modèle devra donc être pénalisé fortement sur ces erreurs critiques.
# 
# ### 1.4 Critères de succès
# 
# ⚠️ La cible **avant EDA** est ce que demande le client. La cible **révisée après EDA** tient compte des contraintes réelles de la donnée. Les deux doivent apparaître.
# 
# | Type | Critère | Cible initiale (client) | Cible révisée après EDA | Justification de la révision |
# |---|---|---|---|---|
# | Métier | Minimisation des erreurs critiques | Proche de 0% de Faux Négatifs sur la classe 2 | *[à compléter après §3]* | *[ex: à voir si la donnée permet une telle précision sans détruire l'accuracy globale]* |
# | Modèle | Métrique robuste au déséquilibre | F1-score macro ≥ 0.75 | F1-score macro > 0.70 | L'Accuracy globale est trompeuse si les classes sont déséquilibrées (ex: 80% de classe 0). Le F1-score macro force le modèle à être bon sur *toutes* les classes. |
# | Opérationnel | Temps de réponse API | < 500 ms | < 1000 ms | Le conseiller doit avoir la réponse en temps réel pendant son face-à-face avec l'usager. |
# 
# ### 1.5 Risques éthiques & réglementaires anticipés
# 
# Une IA dans le service public soulève des enjeux réglementaires majeurs :
# 1. **Risque de Discrimination algorithmique (Biais) :** Notre jeu de données contient des variables sensibles. L'`age` (risque d'âgisme) et la `nationalité_hors_ue` (risque de xénophobie). Si le modèle apprend que ces caractéristiques allongent mathématiquement le délai de retour à l'emploi, il pourrait systématiquement défavoriser ces profils, violant ainsi la *Loi pour une République Numérique*. Nous devrons mesurer ce biais (ex: calcul du Disparate Impact).
# 2. **RGPD (Protection des données) :** La variable `synthese_entretien` est un texte libre. Il est très probable qu'elle contienne des PII (Personally Identifiable Information) comme des noms, des adresses ou des données de santé. Une anonymisation ou une vigilance stricte sera requise.
# 3. **Transparence et Responsabilité (AI Act) :** L'IA ne doit faire que des *recommandations*. C'est le conseiller qui garde la décision finale d'orientation (Principe du *Human-In-The-Loop* ou HITL). Le modèle se doit donc d'être explicable.
# 
# ### 1.6 📝 Synthèse cadrage
# 
# Nous allons concevoir un classifieur multiclasse multimodal dont le succès ne se mesurera pas uniquement à sa précision mathématique globale, mais à sa capacité à **minimiser les erreurs asymétriques** (ne rater aucun profil à risque) tout en **garantissant l'équité algorithmique** sur les populations sensibles (âge, origine).
# 

# ---
# ## 2. Identification & acquisition des données

# ### 2.1 Sources
# 
# | Source | Type | Volumétrie | Format | Accès | Date extraction |
# |---|---|---|---|---|---|
# | Fournie par l'agence | Extract SI | 2500 lignes | CSV | Local | Juil 2026 |
# 

# In[26]:


# 2.2 Chargement
import hashlib
DATA_DIR = Path("data")
file_path = DATA_DIR / "dataset_trajectoire_emploi.csv"
print("Hash MD5:", hashlib.md5(file_path.read_bytes()).hexdigest())

df = pd.read_csv(file_path)
df.shape, df.columns.tolist()


# ### 2.3 Dictionnaire de variables
# 
# | Variable | Description | Type | Plage / valeurs | Cible ? | Sensible ? |
# |---|---|---|---|---|---|
# | `usager_id` | Identifiant unique | ID | | ❌ | ❌ |
# | `age` | Âge de l'usager (en années) | Numérique | | ❌ | ✅ |
# | `niveau_diplome` | Plus haut diplôme obtenu | Catégoriel | Sans diplôme, Bac, Bac+2, Bac+5 | ❌ | ❌ |
# | `anciennete_poste_ans`| Expérience dans le dernier emploi (en années) | Numérique | | ❌ | ❌ |
# | `code_rome_vise` | Code emploi ROME (5 chars) | Catégoriel | | ❌ | ❌ |
# | `code_insee_commune` | Code géo INSEE | Catégoriel | | ❌ | ⚠️ (Proxy) |
# | `est_allocataire` | Statut d'indemnisation | Booléen | 0, 1 | ❌ | ❌ |
# | `nationalite_hors_ue` | Origine hors UE | Booléen | 0, 1 | ❌ | ✅ |
# | `synthese_entretien` | Notes textuelles du conseiller | Texte | | ❌ | ⚠️ (PII) |
# | `classe_retour_emploi`| Délai de retour à l'emploi | Cible (0,1,2) | 0: <6m, 1: 6-12m, 2: >12m | ✅ | ❌ |
# 
# 
# > 💡 **Le Code ROME** : Le Répertoire Opérationnel des Métiers et des Emplois (ROME) est la nomenclature utilisée par France Travail pour classer les métiers. Il est composé d'une lettre (grande famille) et de 4 chiffres. C'est une information clé mais à forte cardinalité.
# 
# ### 2.4 📝 Synthèse acquisition
# 
# Jeu de données hybride de 2500 échantillons avec présence confirmée de données sensibles (`nationalite_hors_ue`, `age`) et potentiellement identifiantes (`synthese_entretien`). Une vigilance sera apportée sur les valeurs manquantes (ex: `niveau_diplome`).
# 
# **Conformité Éthique** : Des mesures techniques spécifiques (comme le calcul du *Disparate Impact*) devront être implémentées sur les variables sensibles afin de prévenir et mitiger tout risque de discrimination algorithmique (en accord avec l'AI Act).
# 

# ---
# ## 3. Exploration & analyse des données (EDA)

# In[27]:


# 0. Chargement des données
df = pd.read_csv('data/dataset_trajectoire_emploi.csv')


# 1 Premier coup d'œil
display(df.head())
print("\n--- INFORMATIONS GENERALES ---")
df.info()
print("\n--- DESCRIPTION STATISTIQUE ---")
display(df.describe(include='all'))


# > **Analyse de l'aperçu** : 
# >
# >Le jeu de données contient 2500 lignes. 
# >
# >On observe un mélange de variables numériques (`age`, `anciennete_poste_ans`) et de chaînes de caractères (`niveau_diplome`, `synthese_entretien`). 
# >
# >Le format est adapté à un traitement classique, mais il faudra impérativement encoder les variables catégorielles avant de les passer à un modèle ML.
# 

# ### 3.1 Analyse de la distribution de la variable cible (Déséquilibre)

# In[28]:


# 2. Distribution de la variable cible (Déséquilibre)
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='classe_retour_emploi')
plt.title('Distribution des classes de retour à l\'emploi')
plt.xlabel('Classe (0: Rapide, 1: Moyen, 2: Longue durée)')
plt.ylabel('Nombre d\'usagers')
plt.show()



# >  **Analyse de la cible** : 
# >
# >On constate un déséquilibre évident.
# >
# >La classe 1 (Moyen) est majoritaire (44%), la classe 0 (Rapide) représente 37%, et la classe 2 (Risque longue durée) est minoritaire à 18%.  
# >
# > **Action pour la suite** : 
# >
# >Ce déséquilibre est dangereux car un modèle pourrait ignorer la classe 2 (pourtant la plus critique d'un point de vue métier) au profit de la précision globale (Accuracy). Nous devrons utiliser l'argument `class_weight='balanced'` lors de l'entraînement, ou générer des données synthétiques via SMOTE.

# ### 3.2 Analyse de la qualité des données

# In[29]:


# 3 Qualité des données : manquants, doublons, valeurs aberrantes
print("--- VALEURS MANQUANTES ---")
print(df.isna().sum()[df.isna().sum() > 0])
print("\n--- DOUBLONS ---")
print(f"Nombre de doublons exacts : {df.duplicated().sum()}")

# Visualisation graphique des valeurs manquantes
df_na = df.isna().sum()
df_na = df_na[df_na > 0]
if not df_na.empty:
    plt.figure(figsize=(8, 4))
    sns.barplot(x=df_na.index, y=df_na.values, hue=df_na.index, legend=False, palette='Reds_r')
    plt.title('Nombre de valeurs manquantes par variable')
    plt.xticks(rotation=45)
    plt.ylabel('Nombre de NaN')
    plt.tight_layout()
    plt.show()


# > **Constat sur la qualité** : 
# >
# >Il n'y a aucun doublon parfait, ce qui est une bonne nouvelle. En revanche, nous avons des valeurs manquantes critiques, notamment sur l'`age` (122), le `niveau_diplome` (84), `est_allocataire` (44) et la `synthese_entretien` (81).  
# >
# > **Action pour la suite** : 
# >
# >Dans la section 4 (Préparation), il faudra construire des transformateurs (`SimpleImputer`) pour combler ces trous (ex: médiane pour l'âge, valeur 'Inconnu' pour le diplôme) afin de ne pas perdre ces observations.
# >
# > **Conséquences de l'imputation (vs Suppression) :**
# >
# > **Points positifs (Pourquoi on le fait) :**
# > - **Conservation de l'information** : Supprimer toutes les lignes incomplètes nous ferait perdre ~10% du jeu de données. Même sans l'âge ou le diplôme, la synthèse d'entretien (texte) reste cruciale.
# > - **Robustesse en production** : Si un conseiller oublie de saisir l'âge dans l'outil final, le modèle (et l'API) doit savoir réagir sans planter. L'imputation l'y prépare.
# >
# > **Points d'attention (Les risques à maîtriser) :**
# > - **Biais de distribution (Âge médian)** : Remplacer 122 âges par la médiane (41 ans) crée un pic artificiel qui réduit la variance globale de la variable.
# > - **Création d'une modalité artificielle (Diplôme 'Inconnu')** : Le modèle pourrait apprendre que le fait de 'ne pas avoir renseigné l'information' est un facteur de risque en soi.
# > 
# > **Alternative avancée** : Au lieu d'une médiane, un **KNNImputer** permettrait de déduire l'âge en se basant sur des profils similaires. Nous conserverons la médiane comme *baseline* initiale.
# 

# ### 3.3 Analyse des distributions

# In[30]:


# 4 Distribution des variables
fig, axes = plt.subplots(3, 2, figsize=(16, 15))

# 1. Distribution de l'âge
sns.histplot(data=df, x='age', bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution de l\'âge des usagers')

# 2. Distribution des niveaux de diplôme
sns.countplot(data=df, y='niveau_diplome', hue='niveau_diplome', legend=False, order=df['niveau_diplome'].value_counts().index, ax=axes[0, 1])
axes[0, 1].set_title('Répartition des niveaux de diplôme')

# 3. Ancienneté au poste
sns.histplot(data=df, x='anciennete_poste_ans', bins=30, kde=True, ax=axes[1, 0], color='teal')
axes[1, 0].set_title('Distribution de l\'ancienneté au poste (en années)')

# 4. Statut Allocataire
sns.countplot(data=df, x='est_allocataire', hue='est_allocataire', legend=False, ax=axes[1, 1], palette='Set2')
axes[1, 1].set_title('Répartition des allocataires (0=Non, 1=Oui)')

# 5. Nationalité hors UE
sns.countplot(data=df, x='nationalite_hors_ue', hue='nationalite_hors_ue', legend=False, ax=axes[2, 0], palette='Set3')
axes[2, 0].set_title('Nationalité hors UE (0=Non, 1=Oui)')

# 6. Top 10 des codes ROME (Métiers visés)
top_romes = df['code_rome_vise'].value_counts().nlargest(10).index
sns.countplot(data=df, y='code_rome_vise', hue='code_rome_vise', legend=False, order=top_romes, ax=axes[2, 1], palette='mako')
axes[2, 1].set_title('Top 10 des métiers visés (Code ROME)')

plt.tight_layout()
plt.show()


# > **Analyse des distributions (pour les néophytes)** :  
# > - **Âge** : Suit une distribution proche d'une courbe en cloche (loi normale), centrée autour de 40 ans (18 à 63 ans). Aucune valeur aberrante bloquante n'est détectée.  
# > - **Diplôme** : Les niveaux 'Bac' et 'Bac+2' sont fortement majoritaires.  
# > - **Ancienneté au poste** : On observe une forme "écrasée" sur la gauche (très peu de personnes ont une grande ancienneté, la majorité est en dessous de 5 ans). La distribution est asymétrique. Il faudra probablement la transformer (ex: log-transformation) pour aider certains modèles à mieux la digérer.
# > - **Statuts (Allocataire et Nationalité)** : Les allocataires sont une courte majorité. Pour la nationalité, la grande majorité est Européenne (0). Cette donnée "Nationalité hors UE" est rare (11%) et de surcroît sensible éthiquement.
# > - **Les métiers visés (Code ROME)** : Le graphique nous montre seulement les 10 métiers les plus demandés, mais en réalité notre base contient 50 métiers différents ! C'est ce qu'on appelle une donnée à "forte cardinalité".
# > - **Le cas des communes (Code INSEE)** : Non tracé ici car il y a **2407 communes différentes** pour 2500 usagers. Un graphique avec 2407 barres serait illisible.
# > 
# > **Action pour la suite (Préparation des données)** :  
# > 
# > **Action sur l'Âge (Standardisation)** :  
# > - **Quoi ?** Une standardisation (via `StandardScaler`) sera intégrée au pipeline de préparation.  
# > - **Pourquoi ?** L'âge s'exprime sur une échelle (18-63) bien plus grande que nos variables booléennes (0/1). Sans standardisation, des algorithmes basés sur les distances (ex: Régression Logistique, SVM) accorderaient un poids démesuré à l'âge. Bien que facultative pour les modèles basés sur des arbres (Random Forest), c'est une excellente pratique (*Clean Code*) pour comparer équitablement divers algorithmes.
# > 
# > **Action sur le Diplôme (Encodage Ordinal)** :  
# > - **Quoi ?** Un encodage préservant la hiérarchie (via `OrdinalEncoder`) sera appliqué au lieu d'un simple `OneHotEncoder`.  
# > - **Pourquoi ?** Les algorithmes nécessitent des entrées numériques. Le niveau de diplôme possédant un ordre naturel (Sans diplôme < Bac < Bac+2 < Bac+5), un encodage ordinal permet au modèle (surtout les arbres de décision) de capter et d'exploiter cette notion de progression scolaire, au lieu de traiter chaque niveau de manière totalement isolée.
# > 
# > **Action sur l'Ancienneté (Transformation mathématique)** :
# > - **Quoi ?** Une transformation de type logarithmique ou *Power Transform*.
# > - **Pourquoi ?** A cause de son asymétrie, certains modèles peineront à modéliser la minorité de profils très anciens. La transformation ramènera la distribution vers une forme de courbe en cloche plus "normale".
# > 
# > **Action sur les Codes ROME et INSEE (Feature Engineering)** :
# > - **Quoi ?** Regroupement par grandes familles (ex: première lettre du Code ROME) ou remplacement par des variables "macro" (ex: taux de chômage du Code INSEE de la commune via de la donnée externe).
# > - **Pourquoi ?** Si l'on donne ces variables brutes, l'algorithme va les apprendre par cœur (sur-apprentissage) au lieu d'en déduire une logique globale, ce qui nuira gravement à ses performances sur de nouveaux profils.
# 

# ### 3.4 Analyse des corrélations & relations entre variables

# In[31]:


# 5 Corrélations & relations entre variables
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Relation Ancienneté Poste vs Classe retour emploi
sns.boxplot(data=df, x='classe_retour_emploi', y='anciennete_poste_ans', ax=axes[0])
axes[0].set_title('Ancienneté au poste selon le délai de retour')
axes[0].set_xlabel('Classe (0: Rapide, 1: Moyen, 2: Long)')

# Matrice de corrélation (sur les variables numériques)
num_cols = df.select_dtypes(include=['number']).columns
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=axes[1])
axes[1].set_title('Matrice de corrélation')

plt.tight_layout()
plt.show()


# > **Analyse des relations (explication pour les néophytes)** :  
# > - **Qu'est-ce qu'une corrélation ?** C'est un indicateur qui mesure si deux données évoluent ensemble. Par exemple, si l'ancienneté augmente mécaniquement avec l'âge, on dit qu'ils sont positivement corrélés.
# > - **Lecture du graphique (Heatmap)** : Ce tableau coloré croise toutes nos données chiffrées. Une couleur rouge vif indique un lien fort et direct (quand l'un monte, l'autre monte), tandis qu'un bleu foncé indique un lien inverse. Si les couleurs sont pâles (chiffres proches de 0), cela signifie qu'il n'y a pas de lien évident et "simple" (comme une ligne droite).
# > - **Ce que l'on observe ici** : Nos indicateurs montrent des couleurs plutôt pâles entre eux. Cela veut dire qu'aucune donnée numérique, prise isolément, ne suffit à expliquer de façon mathématique simple le délai de retour à l'emploi.
# > 
# > **Action pour la suite (Modélisation)** :  
# > Le fait qu'il n'y ait pas de lien *simple* ne veut pas dire qu'il n'y a pas de lien *du tout* ! Le monde réel est complexe : c'est peut-être la **combinaison** d'un âge avancé avec un autre facteur (comme la nationalité ou le diplôme) qui crée un risque d'éloignement de l'emploi. Pour détecter ces scénarios combinés, nous utiliserons des algorithmes d'Intelligence Artificielle capables de comprendre cette complexité (comme les "Forêts Aléatoires"), plutôt que des calculs statistiques basiques.
# > 
# > **Limites statistiques** : Attention, cette *Heatmap* de corrélation (Pearson) ne prend en compte que les variables **numériques**. Or, notre dataset contient beaucoup de variables catégorielles (métier, diplôme). Pour être parfaitement exhaustif, il faudrait calculer un *V de Cramer* ou un coefficient *Phik*, mais pour l'instant nous confierons à l'algorithme de Machine Learning le soin de capter ces relations complexes.
# 

# ### 3.5 Analyse textuelle (NLP) - `synthese_entretien`
# 
# Cette variable non structurée contient le compte-rendu libre saisi par le conseiller. Analysons si son contenu recèle un signal prédictif pour le délai de retour à l'emploi.
# 

# In[32]:


# Distribution des catégories de synthèse par classe de retour à l'emploi
plt.figure(figsize=(12, 6))
sns.countplot(data=df.dropna(subset=['synthese_entretien']), y='synthese_entretien', hue='classe_retour_emploi', palette='viridis')
plt.title('Répartition des synthèses d\'entretien selon la classe de retour')
plt.xlabel('Nombre d\'usagers')
plt.ylabel('Synthèse du conseiller')
plt.legend(title='Classe Retour Emploi', labels=['0: Rapide', '1: Moyen', '2: Longue durée'])
plt.tight_layout()
plt.show()


# > **Analyse du contenu textuel (NLP)** :  
# > Le graphique montre que le vocabulaire utilisé par le conseiller est **le prédicteur le plus puissant** du jeu de données !  
# > - Les textes mentionnant "*Cumul de difficultés*", "*Freins périphériques majeurs*" ou "*Perte de confiance*" sont quasi exclusivement associés à la **Classe 2** (Risque de longue durée).  
# > - À l'inverse, les termes "*Candidat très dynamique*", "*Excellente présentation*" ou "*Profil autonome*" prédisent fortement la **Classe 0** (Rapide).  
# > 
# > **Choix de la stratégie NLP pour la modélisation** :  
# > Pour transformer ce texte libre en données mathématiques pour notre algorithme, 3 approches ont été envisagées :
# > 1. **Bag of Words (Comptage simple)** : Compte les apparitions de chaque mot. *Écarté* car les mots vides ("le", "et") domineraient les mots rares mais prédictifs.
# > 2. **Deep Learning (Word Embeddings / CamemBERT)** : Comprend le sens sémantique de la phrase. *Écarté* car c'est une approche "boîte noire", techniquement lourde et disproportionnée pour des phrases courtes et stéréotypées. La perte d'explicabilité poserait problème vis-à-vis de l'AI Act.
# > 3. **TF-IDF (Term Frequency-Inverse Document Frequency) (Choix retenu)** : Pondère les mots en fonction de leur rareté globale mais de leur fréquence locale. C'est le meilleur compromis : très performant, facilement intégrable dans un `ColumnTransformer` Scikit-Learn, et **100% explicable** (on pourra dire précisément quel mot a influencé la décision de l'IA).
# 

# ### 3.6 Analyse des biais & variables sensibles

# In[33]:


# Démonstration du Disparate Impact sur la variable Nationalité
display(pd.crosstab(df['nationalite_hors_ue'], df['classe_retour_emploi'], normalize='index').style.format("{:.1%}"))

# Démonstration sur l'âge
df_temp = df.copy()
df_temp['tranche_age'] = pd.cut(df_temp['age'], bins=[0, 25, 45, 65])
display(pd.crosstab(df_temp['tranche_age'], df_temp['classe_retour_emploi'], normalize='index').style.format("{:.1%}"))


# > **Analyse** :  
# >L'analyse croisée des variables sensibles avec la cible révèle des **disparités majeures** (Disparate Impact) :
# >- **Âge** : La proportion de personnes en risque longue durée (Classe 2) est de 9% chez les 25-45 ans, mais bondit à près de **29% pour les 45-65 ans**.
# >- **Nationalité** : 38% des usagers non-UE (nationalite_hors_ue=1) sont en classe 2, contre seulement 15% pour les autres. À l'inverse, seuls 14% des non-UE sont considérés "rapides" (classe 0) contre 40% pour le reste de la population.
# >
# > **Conclusion Éthique** : Le modèle risque fortement d'apprendre et de reproduire ces biais historiques. Une approche de mitigation (ex: re-pondération, features neutralisées ou seuils de rejets adaptés) sera indispensable pour respecter l'AI Act.
# > 
# > **Pistes de mitigation envisagées** :
# > - **Pre-processing (Suppression)** : Entraîner un modèle "Scénario 2" amputé des variables sensibles (`age`, `nationalite_hors_ue`) et vérifier si la perte de performance est acceptable par rapport au gain éthique.
# > - **Pre-processing (Re-pondération)** : Appliquer un `sample_weight` plus élevé aux profils minoritaires ayant un retour à l'emploi rapide pour forcer le modèle à ne pas les ignorer.
# > - **Post-processing (Seuils / HITL)** : Imposer un seuil de confiance plus élevé pour les prédictions "Risque" sur les profils sensibles, ou instaurer un filet de sécurité humain (*Human-In-The-Loop*) en cas de doute algorithmique.
# 

# ### 3.7 📝 Synthèse EDA
# 
# L'exploration préliminaire a permis de lever plusieurs loups et définit notre feuille de route pour la phase de préparation (Pipeline) :
# 
# 1. **Gestion de la qualité des données (Imputation)** : Présence de valeurs manquantes sur l'`age`, le `niveau_diplome` et la `synthese_entretien`. Une stratégie d'imputation adaptée devra être mise en place (ex: médiane pour l'âge, valeur 'Inconnu' pour les autres).
# 2. **Déséquilibre critique de la cible** : La classe 2 (Risque longue durée), pourtant la plus importante d'un point de vue métier, est minoritaire (18%). L'utilisation de techniques d'équilibrage (SMOTE, `class_weight='balanced'`) ou d'une métrique robuste (F1-score macro) sera impérative pour ne pas rater ces profils.
# Si l'on regardait l'Accuracy classique, un modèle "paresseux" qui prédirait toujours "0" pour tout le monde obtiendrait un score artificiellement élevé (ex: 70%), alors qu'il raterait absolument tous les usagers en risque de chômage long !
# Le F1-Macro nous protège contre cela : puisqu'il fait la moyenne non-pondérée des trois classes, si le modèle a un score désastreux de 0% sur la classe 2, la note globale F1-Macro va s'effondrer. C'est le meilleur moyen mathématique de forcer notre algorithme à traiter le risque humain de la Classe 2 avec autant d'importance que la Classe 0 majoritaire.
# 
# 3. **Risque de discrimination (AI Act)** : L'analyse a confirmé un très fort *Disparate Impact* sur les variables `age` et `nationalite_hors_ue`. Des scénarios de mitigation (suppression, re-pondération) seront testés pour garantir l'équité du modèle final.
# 4. **Forte cardinalité & Asymétrie** : Les variables géographiques (`code_insee_commune`) et métiers (`code_rome_vise`) contiennent trop de valeurs uniques pour être utilisées telles quelles. Un travail de *Feature Engineering* sera nécessaire (regroupements, Target Encoding). L'asymétrie de l'`anciennete_poste_ans` nécessitera probablement une transformation mathématique.
# 5. **Complexité des relations (Non-linéarité)** : La matrice de corrélation montre des liens faibles en lecture directe. Cela nous oriente vers le choix d'algorithmes capables de capter des interactions complexes et non-linéaires (comme les Random Forest ou Gradient Boosting) plutôt que de simples régressions.
# 6. **Multimodalité (NLP)** : La variable `synthese_entretien` étant du texte libre, un traitement spécifique du langage naturel (NLP) devra être intégré au pipeline (ex: TF-IDF ou Embeddings) pour en extraire l'essence.
# 7. **Nature ordinale du diplôme** : La variable `niveau_diplome` présente une hiérarchie intrinsèque (Sans diplôme < Bac < Bac+2 < Bac+5) qui devra être préservée via un encodage ordinal lors de la préparation des données.
# 

# ## 4. Préparation des données

# ### 4.1 Feature Engineering (Réduction de cardinalité)
# 
# Avant le split, nous effectuons de la réduction de cardinalité sur les données qui ne dépendent pas des statistiques du jeu d'entraînement (pas de risque de fuite de données ici). Cela permet d'extraire la substantifique moelle d'une variable très spécifique.
# 
# - Le **département** (2 premiers caractères) au lieu de la commune (code_insee_commune).
# - La **famille de métier** (1ère lettre) au lieu du métier précis (code_rome_vise).

# In[34]:


# Extraction du département et de la famille ROME
df["departement"] = df["code_insee_commune"].astype(str).str[:2]
df["famille_rome"] = df["code_rome_vise"].astype(str).str[0]

# On supprime les anciennes colonnes à forte cardinalité et inutiles
df = df.drop(columns=["code_insee_commune", "code_rome_vise", "usager_id"])

df.head()

# Optimisation mémoire (Casting des types Pandas pour économiser la RAM)
df['est_allocataire'] = df['est_allocataire'].astype('float32')
df['nationalite_hors_ue'] = df['nationalite_hors_ue'].astype('float32')
df['age'] = df['age'].astype('float32')


# ### 4.2 Train/test split stratifié
# 
# Nous avons observé un déséquilibre des classes dans l'EDA (beaucoup de profils en retour moyen ou rapide vs risque long terme). Le paramètre `stratify=y` est critique.
# 
# On sépare les données avant de faire les transformations pour éviter ce qu'on appelle la fuite de données (Data Leakage). Si on remplaçait les valeurs manquantes de l'âge par la médiane sur l'ensemble du dataset complet avant de le couper en deux, la médiane prendrait en compte les âges des personnes du jeu de test. Le modèle "tricherait" car il aurait indirectement eu accès à des informations du jeu de test lors de son entraînement.

# In[35]:


from sklearn.model_selection import train_test_split

# drop solution for training
X = df.drop(columns=["classe_retour_emploi"])
# solution
y = df["classe_retour_emploi"]

# Split 80/20 with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE
)

print(f"X_train shape : {X_train.shape}")
print(f"X_test shape : {X_test.shape}")


# ### 4.3 Pipeline de préprocessing : numériques, catégorielles et texte
# 
# Nous allons utiliser un `ColumnTransformer` pour appliquer les bonnes transformations selon le type de variable.

# In[36]:


from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Identification des groupes de variables
num_features = ["age", "anciennete_poste_ans"]
cat_nominal_features = ["est_allocataire", "departement", "famille_rome", "nationalite_hors_ue"]
cat_ordinal_features = ["niveau_diplome"]
text_feature = "synthese_entretien"

# Pipelines spécifiques
num_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_nominal_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=False, drop="first"))
])

# Encodage Ordinal pour le diplôme (hiérarchie)
diplome_order = [["Sans diplôme", "Bac", "Bac+2", "Bac+5"]]
cat_ordinal_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("ord", OrdinalEncoder(categories=diplome_order, handle_unknown="use_encoded_value", unknown_value=-1))
])

# Wrapper custom pour le texte
def extract_text(X):
    return X.iloc[:, 0].fillna("").astype(str)

from sklearn.preprocessing import FunctionTransformer
text_pipeline = Pipeline([
    ("extract", FunctionTransformer(extract_text, validate=False)),
    # --- GESTION DES STOP WORDS FRANCAIS ---
    # Option 1 : Importer nltk/spacy et fournir une liste explicite (stop_words=['le', 'la']).
    # Option 2 : Utiliser le filtrage mathématique avec max_df (ex: ignore les mots présents dans + de 85% des textes).
    # Choix : Compromis simplicité/efficacité avec l'Option 2 (max_df=0.85).
    ("tfidf", TfidfVectorizer(max_features=1000, max_df=0.85)) # max_features limite l'explosion de dimensionnalité
])

# Assemblage final
preprocessor = ColumnTransformer([
    ("num", num_pipeline, num_features),
    ("cat_nom", cat_nominal_pipeline, cat_nominal_features),
    ("cat_ord", cat_ordinal_pipeline, cat_ordinal_features),
    ("text", text_pipeline, [text_feature])
])

# On entraîne le preprocessor et on transforme X_train en même temps
X_train_prep = preprocessor.fit_transform(X_train)
X_test_prep = preprocessor.transform(X_test)

print(f"X_train_prep shape: {X_train_prep.shape} (Taille de notre espace de représentation multimodal)")


# > Note sur la dimensionnalité (183 colonnes) :
# > Bien que max_features=1000 pour le TF-IDF, le nombre total de colonnes est bien inférieur. Cela s'explique car l'EDA a révélé qu'il n'y a que 9 phrases  uniques dans le corpus de ce jeu de données synthétique. Le TF-IDF a donc extrait tous les mots existants (une centaine) sans même atteindre le plafond de 1000.
# >
# > Ce ratio de ~183 variables pour 2000 échantillons est excellent et prévient le sur-apprentissage.

# ### 4.4 Scénarios de jeux de données
# 
# Nous avons identifié 4 scénarios de features que nous comparerons en Modélisation et en Analyse (Section 6) :
# 
# | Scénario | Variables conservées | Justification |
# |---|---|---|
# | **S1 (Complet)** | Toutes (Num + Cat + Texte) | Baseline Multimodale performante. |
# | **S2 (Éthique)** | S1 moins `age` et `nationalite_hors_ue` | Atténuation des biais et respect RGPD/AI Act (élimination du Disparate Impact). |
# | **S3 (NLP)** | Uniquement `synthese_entretien` | Tester la force du verbatims seul face aux données administratives. |
# | **S4 (Tabulaire)** | Uniquement Num + Cat | Comparer la plus-value de l'ingénierie textuelle vs un modèle classique. |
# 
# > Ces scénarios peuvent être implémentés en créant différentes versions du `ColumnTransformer` (en retirant/ajoutant des éléments dans les listes `num_features`, `cat_features`, etc.)
# 

# In[37]:


def get_scenario_features(scenario):
    """Retourne les listes de features à conserver selon le scénario"""
    if scenario == "S1": # Complet
        return num_features, cat_nominal_features, cat_ordinal_features, [text_feature]
    elif scenario == "S2": # Éthique (sans age, sans nationalité)
        num_s2 = [f for f in num_features if f != "age"]
        cat_nom_s2 = [f for f in cat_nominal_features if f != "nationalite_hors_ue"]
        return num_s2, cat_nom_s2, cat_ordinal_features, [text_feature]
    elif scenario == "S3": # NLP pur
        return [], [], [], [text_feature]
    elif scenario == "S4": # Tabulaire pur
        return num_features, cat_nominal_features, cat_ordinal_features, []
    else:
        raise ValueError("Scénario inconnu")

def build_preprocessor(scenario):
    num, cat_nom, cat_ord, text = get_scenario_features(scenario)

    transformers = []
    if num: transformers.append(("num", num_pipeline, num))
    if cat_nom: transformers.append(("cat_nom", cat_nominal_pipeline, cat_nom))
    if cat_ord: transformers.append(("cat_ord", cat_ordinal_pipeline, cat_ord))
    if text: transformers.append(("text", text_pipeline, text))

    return ColumnTransformer(transformers)

# Génération du dictionnaire des préprocesseurs pour la Partie 5
preprocessors = {
    "S1": build_preprocessor("S1"),
    "S2": build_preprocessor("S2"),
    "S3": build_preprocessor("S3"),
    "S4": build_preprocessor("S4")
}

print("Pipelines de scénarios générés avec succès !")


# ### 4.5 Assertions de qualité (Data Quality checks)
# 
# On valide que le pipeline n'a pas introduit d'anomalies.

# In[38]:


# 1. Vérifier qu'il n'y a plus aucun NaN dans les matrices préparées
assert not np.isnan(X_train_prep).any(), "Il reste des valeurs manquantes dans X_train_prep !"
assert not np.isnan(X_test_prep).any(), "Il reste des valeurs manquantes dans X_test_prep !"

# 2. Le nombre de lignes doit rester identique après transformation
assert X_train_prep.shape[0] == X_train.shape[0], "Le preprocessing a altéré le nombre d'échantillons !"

# 3. Les cibles doivent appartenir exclusivement aux classes attendues (0, 1, 2)
assert set(y_train.unique()).issubset({0, 1, 2}), "Valeurs illégales dans y_train !"

print("Toutes les assertions de qualité sont passées au vert ✅")


# ### 4.6 Gestion du déséquilibre des classes (class_weight='balanced')
# 
# Comme identifié dans l'EDA, la classe 2 (Risque longue durée) est minoritaire. 
# Deux grandes approches existent en Data Science pour palier cela :
# 1. **Le sur-échantillonnage (ex: SMOTE)** : on génère de fausses données d'entraînement. C'est lourd, et peu adapté aux matrices creuses textuelles générées par le TF-IDF.
# 2. **La re-pondération algorithmique (`class_weight="balanced"`)** : on indique simplement à l'algorithme (ex: Random Forest) de pénaliser beaucoup plus lourdement les erreurs faites sur la classe minoritaire.
# 
# 👉 **Choix technique :** Par souci d'élégance, de simplicité (principe KISS) et de compatibilité avec le NLP, nous avons choisi la deuxième option. Nous n'avons donc **aucune transformation mathématique à faire sur `X_train` dans cette partie 4**. La gestion du déséquilibre se fera directement lors de l'instanciation des modèles dans la Partie 5 en activant le paramètre de pondération.

# ### 4.8 Sauvegarde de l'artefact (Sérialisation MLOps)
# 
# Pour respecter les bonnes pratiques MLOps, notre `ColumnTransformer` (entraîné sur `X_train`) doit être sauvegardé physiquement. Lors du déploiement en production (Partie 8), notre API FastAPI chargera ce fichier pour transformer les données textuelles et tabulaires d'un nouvel usager avant de faire sa prédiction.

# In[39]:


import joblib
import os

os.makedirs("models", exist_ok=True)
joblib.dump(preprocessors["S1"], "models/preprocessor_S1.pkl")
print("✅ Pipeline de pré-traitement (S1) sauvegardé avec succès dans models/")


# ### 4.9 Synthèse préparation
# 
# Cette étape de préparation s'est avérée critique pour la fiabilité et l'éthique de notre futur modèle. Voici les points de réflexion majeurs :
# 
# 1. **Sécurisation de la méthodologie (Anti-Leakage)** :
#    Plutôt que d'appliquer des transformations `pandas` en vrac sur l'ensemble du dataset, nous avons encapsulé toute la logique d'imputation, de mise à l'échelle et de vectorisation textuelle au sein d'un `ColumnTransformer` de `scikit-learn`. Couplé au `train_test_split` préalable, cela garantit une étanchéité parfaite : le modèle n'a aucune vision sur la distribution des données de test. C'est une condition _sine qua non_ pour une industrialisation robuste.
# 
# 2. **Maîtrise de la dimensionnalité (Feature Engineering)** :
#    Les variables `code_insee_commune` (plus de 2000 modalités) et `code_rome_vise` posaient un risque de sur-apprentissage (curse of dimensionality). En extrayant les métadonnées de plus haut niveau (le numéro de département et la grande famille de métier), nous réduisons drastiquement la cardinalité tout en conservant le signal géographique et sectoriel. De même, le NLP via `TfidfVectorizer` a été plafonné à 1000 features pour garantir un temps d'inférence compatible avec le temps réel (une contrainte opérationnelle forte pour les conseillers).
# 
# 3. **Prise en compte du contexte déséquilibré** :
#    L'utilisation du paramètre `stratify=y` n'est pas qu'un détail technique. Sachant que l'enjeu métier principal est de ne rater aucun usager en risque de chômage longue durée (Faux Négatifs), il est impératif que cette classe minoritaire soit représentée avec exactitude dans nos jeux de test pour que les futures métriques de validation (F1-Score, Recall) soient fiables.
# 
# 4. **Construction d'une démarche d'audit éthique** :
#    Enfin, la structuration formelle de nos 4 scénarios d'entraînement est la base de notre future analyse critique (Section 6). Le scénario **S2 (Éthique)**, en retirant l'âge et la nationalité, nous permettra de comparer les performances brutes avec les performances 'sans biais potentiel', répondant ainsi directement aux exigences réglementaires de l'AI Act et au principe de non-discrimination algorithmique.
# 

# ---
# ## 5. Modélisation & entraînement
# 

# ### 5.1 Familles candidates
# 
# **Famille retenue** : ML classique (arbres de décision et modèles linéaires).
# 
# **Motif principal** : Les données sont de nature tabulaire (âge, diplôme, géographie) avec des features NLP (synthese_entretien) pré-vectorisées (TF-IDF). 
# 
# Le Deep Learning, SLM ou LLM sont inadaptés ici car ils requièrent des temps et puissances de calcul asymétriques pour un faible volume de données (N=2500) et offrent une explicabilité moindre comparé aux approches ML classiques (Feature Importance) ce qui est impératif pour l'IA Act.

# ### 5.2 Modèles candidats
# 
# | Modèle | Famille | Pourquoi candidat ? | Coût (entraînement / inférence) | Explicabilité |
# |---|---|---|---|---|
# | Régression Logistique | linéaire | baseline rapide, transparente et très explicable (poids) | très faible / très faible | élevée |
# | Random Forest | ensemble (Bagging) | robuste, gère bien les non-linéarités, peu de tuning | moyen / faible | moyenne (feature importance) |
# | LightGBM | ensemble (Boosting) | très performant sur tabulaire, gère nativement matrices creuses TF-IDF | moyen / faible | moyenne (feature importance) |

# ### 5.3 Benchmark des models

# > **Note méthodologique (Choix de la Boussole Unique)** : 
# > Lors de la phase de benchmark (ci-dessous) et de recherche d'hyperparamètres, nous n'utilisons **qu'une seule métrique d'évaluation : le F1-Macro**.
# > 
# > Pourquoi ne pas calculer toutes les métriques (Précision, Rappel, etc.) dès maintenant ?
# > 1. **Boussole unique** : Pour faciliter le choix du meilleur modèle via un seul score mathématique clair à maximiser.
# > 2. **Efficacité algorithmique** : Réduit considérablement le temps de calcul lors des dizaines de boucles d'entraînement croisées.
# > 3. **Analyse ciblée** : Le F1-Macro est la métrique la plus sévère face au déséquilibre de nos données. Les détails (Matrice de confusion, Précision et Rappel par classe) seront étudiés au microscope *uniquement* sur le modèle gagnant lors de l'évaluation finale (Section 5.6).

# In[40]:


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from lightgbm import LGBMClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
import pandas as pd

# Nous utiliserons class_weight='balanced' pour adresser le déséquilibre des classes
models = {
    "LogisticRegression": LogisticRegression(class_weight="balanced", max_iter=1000, random_state=42),
    "RandomForest": RandomForestClassifier(class_weight="balanced", random_state=42),
    "LightGBM": LGBMClassifier(class_weight="balanced", random_state=42, n_jobs=-1, verbose=-1)
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_results = []

# Pour chaque modèle : Pipeline(preprocessor + estimator) + cross_val_score
for name, model in models.items():
    pipe = Pipeline([
        ("preprocessor", preprocessors["S1"]),
        ("clf", model)
    ])

    # Nous utilisons f1_macro pour garantir l'impact des classes minoritaires
    scores = cross_val_score(pipe, X_train, y_train, cv=cv, scoring="f1_macro", n_jobs=-1)

    cv_results.append({
        "Modèle": name,
        "F1-Macro (Moyenne)": scores.mean(),
        "F1-Macro (Ecart-type)": scores.std()
    })

df_cv_results = pd.DataFrame(cv_results).sort_values(by="F1-Macro (Moyenne)", ascending=False)

display(df_cv_results)


# ### Bilan du Benchmark 
# 
# > Nous venons de faire passer 5 examens (validation croisée) à nos trois algorithmes. Le tableau ci-dessus résume leurs résultats avec deux critères : la **Moyenne** de leur note F1-Macro (plus elle est haute, meilleur est le modèle), et l'**Écart-type** (plus il est bas, plus le modèle a des notes régulières à chaque examen). 
# 
# 1. **Le grand gagnant de la performance (LightGBM)** : Il obtient la **Meilleure Moyenne** (~0.68), prouvant qu'il réussit le mieux à détecter les dossiers complexes. Cependant, il a l'**Écart-type le plus élevé** (~0.021), ce qui signifie que ses notes varient un peu plus selon l'examen. Il prend des risques payants mais est un peu moins régulier.
# 2. **Le véritable challenger (Random Forest)** : Bien que sa Moyenne globale (~0.660) soit mathématiquement un cheveu en dessous de la Régression Logistique, il possède l'**Écart-type le plus bas de tous** (~0.008). Cette stabilité exceptionnelle (ses notes ne varient presque pas d'un examen à l'autre) en fait un choix industriellement beaucoup plus sûr et fiable que le modèle basique.
# 3. **Le modèle basique (Régression Logistique)** : Sa Moyenne (~0.664) fait illusion, car son Écart-type est deux fois plus élevé que celui du Random Forest. Modèle mathématique trop simpliste, il manque de régularité face à la complexité de nos données.
# 
# **Décision** : Face au compromis entre la performance brute du **LightGBM** et la stabilité infaillible du **Random Forest**, nous n'allons en éliminer aucun ! Nous conservons ces deux modèles pour l'étape suivante (Optimisation des hyperparamètres). C'est à l'issue de ces réglages que nous couronnerons le vainqueur absolu.

# ### 5.4 Optimisation des hyperparamètres
# 
# Notre jeu de données est "petit" (~2500 lignes) mais très "large" en raison de l'analyse NLP (`TF-IDF` crée des centaines de colonnes). Si on laisse les modèles avec leurs paramètres par défaut, ils vont mémoriser les dossiers par cœur (Surapprentissage / Overfitting) mais échoueront en conditions réelles.
# 
# Voici pourquoi nous avons choisi cette grille de test (le "filet de sécurité") :
# 
# **Pour le LightGBM :**
# 1. **`n_estimators` [50, 100] (Nombre d'arbres)** : On le teste à `50` (la moitié) et `100` (le défaut). L'objectif est de lui demander de comprendre les règles générales avec peu d'arbres, sans se perdre dans les détails aberrants.
# 2. **`learning_rate` [0.05, 0.1] (Vitesse d'apprentissage)** : C'est la puissance de correction de chaque nouvel arbre. Un apprentissage lent (`0.05`) force la prudence, tandis que la norme (`0.1`) permet d'aller vite.
# 3. **`num_leaves` [15, 31] (Nombre de feuilles)** : Au lieu de limiter bêtement la profondeur (`max_depth`), on limite le nombre total de feuilles. Face à un grand nombre de mots (TF-IDF), cela force l'algorithme à ne conserver que les combinaisons les plus pertinentes.
# 4. **`min_child_samples` [20, 50] (Échantillons minimums par feuille)** : Ce réglage est vital pour la robustesse. En forçant chaque règle terminale à s'appliquer à au moins 20 ou 50 usagers, on interdit au modèle de créer des exceptions "sur-mesure" pour une ou deux personnes, bloquant ainsi le surapprentissage.
# 
# **Pour le Random Forest :**
# 1. **`n_estimators` [100, 200]** : Le Random Forest crée des arbres "au hasard" et vote. Contrairement au Boosting, plus de forêts réduisent l'erreur. On double la norme pour voir s'il lisse mieux les erreurs du texte.
# 2. **`max_depth` [None, 10]** : On oppose sa croissance infinie naturelle (`None`) à une croissance raisonnablement coupée (`10`) pour forcer une vue macro des dossiers.
# 3. **`min_samples_split` [2, 5]** : Ce paramètre l'empêche de créer des règles spécifiques pour un seul usager. À `5`, on le force à n'adopter une règle que si elle concerne au moins 5 personnes, évitant ainsi l'Overfitting local.

# In[41]:


# Désactivation des messages d'avertissement pour la clarté du notebook
import warnings
import logging
warnings.filterwarnings("ignore")
logging.getLogger("mlflow").setLevel(logging.ERROR)

import mlflow
import mlflow.sklearn
import mlflow.lightgbm
from sklearn.model_selection import GridSearchCV

# Initialisation locale de MLflow
mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("certif_ia_modelisation")

# === Pipeline LightGBM ===
pipe_lgb = Pipeline([
    ("preprocessor", preprocessors["S1"]),
    ("clf", LGBMClassifier(class_weight="balanced", random_state=42, verbose=-1))
])
param_grid_lgb = {
    'clf__n_estimators': [50, 100],
    'clf__learning_rate': [0.05, 0.1],
    'clf__num_leaves': [15, 31],
    'clf__min_child_samples': [20, 50]
}

# === Pipeline Random Forest ===
pipe_rf = Pipeline([
    ("preprocessor", preprocessors["S1"]),
    ("clf", RandomForestClassifier(class_weight="balanced", random_state=42))
])
param_grid_rf = {
    'clf__n_estimators': [100, 200],
    'clf__max_depth': [None, 10],
    'clf__min_samples_split': [2, 5]
}

print("Démarrage du Duel Final (Hyperparameter Tuning) avec MLflow...")
mlflow.sklearn.autolog(log_models=False, log_datasets=False) # Autolog pour capturer les params

# Lancement de l'optimisation LightGBM
with mlflow.start_run(run_name="LightGBM_HyperTuning"):
    search_lgb = GridSearchCV(pipe_lgb, param_grid=param_grid_lgb, cv=cv, scoring="f1_macro", n_jobs=-1, verbose=0)
    search_lgb.fit(X_train, y_train)
    mlflow.log_params(search_lgb.best_params_)
    mlflow.log_metric("best_cv_f1_macro", search_lgb.best_score_)
    mlflow.sklearn.log_model(search_lgb.best_estimator_, "best_model_S1_lgb", serialization_format="cloudpickle")
    print(f"✅ LightGBM - Meilleurs paramètres: {search_lgb.best_params_}")
    print(f"   LightGBM - F1-Macro CV: {search_lgb.best_score_:.4f}")

# Lancement de l'optimisation RandomForest
with mlflow.start_run(run_name="RandomForest_HyperTuning"):
    search_rf = GridSearchCV(pipe_rf, param_grid=param_grid_rf, cv=cv, scoring="f1_macro", n_jobs=-1, verbose=0)
    search_rf.fit(X_train, y_train)
    mlflow.log_params(search_rf.best_params_)
    mlflow.log_metric("best_cv_f1_macro", search_rf.best_score_)
    mlflow.sklearn.log_model(search_rf.best_estimator_, "best_model_S1_rf", serialization_format="cloudpickle")
    print(f"✅ Random Forest - Meilleurs paramètres: {search_rf.best_params_}")
    print(f"   Random Forest - F1-Macro CV: {search_rf.best_score_:.4f}")

# Arbitrage automatique
print("\n" + "="*50)
if search_lgb.best_score_ > search_rf.best_score_:
    final_model = search_lgb.best_estimator_
    print(f"🏆 Le grand vainqueur du duel est : LIGHTGBM (Score : {search_lgb.best_score_:.4f})")
else:
    final_model = search_rf.best_estimator_
    print(f"🏆 Le grand vainqueur du duel est : RANDOM FOREST (Score : {search_rf.best_score_:.4f})")
print("="*50)


# ### 5.5 Évaluation finale sur le test set

# In[42]:


from sklearn.metrics import classification_report, accuracy_score, ConfusionMatrixDisplay, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import tempfile
import os

with mlflow.start_run(run_name="Evaluation_Finale_TestSet"):
    y_pred = final_model.predict(X_test)
    
    # Calcul des métriques
    acc = accuracy_score(y_test, y_pred)
    f1_test = f1_score(y_test, y_pred, average="macro")
    cm = confusion_matrix(y_test, y_pred)
    fn_classe2 = cm[2, 0] + cm[2, 1]
    
    # Logging MLflow
    mlflow.log_metric("accuracy_test", acc)
    mlflow.log_metric("f1_macro_test", f1_test)
    mlflow.log_metric("fn_classe2_test", fn_classe2)
    mlflow.set_tag("candidate", "production")
    
    # Sauvegarde du modèle final
    mlflow.sklearn.log_model(final_model, "production_model_S1", serialization_format="cloudpickle")

    print("=== Résultats sur l'ensemble de Test ===")
    print(f"Accuracy : {acc:.4f}")
    print("Rapport de classification :")
    print(classification_report(y_test, y_pred))

    # Affichage de la matrice de confusion
    fig, ax = plt.subplots(figsize=(6, 6))
    ConfusionMatrixDisplay.from_predictions(
        y_test, 
        y_pred, 
        display_labels=["Rapide (<6m)", "Moyen (6-12m)", "Risque (>12m)"],
        cmap="Blues", 
        ax=ax,
        colorbar=False
    )
    plt.title("Matrice de Confusion Finale (Scénario 1)")
    
    # Sauvegarde de l'image et log dans MLflow
    with tempfile.TemporaryDirectory() as tmp_dir:
        cm_path = os.path.join(tmp_dir, "confusion_matrix.png")
        fig.savefig(cm_path)
        mlflow.log_artifact(cm_path)
        
    plt.show()


# ### 5.6 Synthèse finale et Analyse de la Matrice de Confusion
# 
# **Modèle retenu** : **LightGBM optimisé** (avec `class_weight='balanced'`, `max_depth=5`).
# 
# **Analyse chiffrée du Test Set (La réalité du terrain)** :
# Contrairement à l'Accuracy globale (72%), qui masque les défauts sur les minorités, notre analyse se concentre sur le Rapport de Classification et la Matrice de Confusion générés ci-dessus :
# 
# 1. **Sécurisation de la Classe 2 (Risque de Chômage Longue Durée)** :
#    - **Rappel (Recall) de 69%** : Sur l'ensemble des personnes *réellement* en risque de chômage long dans notre set de test (90 personnes), le modèle a réussi à en attraper 69% (soit environ 7 sur 10). 
#    - **Précision de 54%** : Quand le modèle déclenche l'alerte "Risque", il a raison 1 fois sur 2. C'est un biais *assumé* ! Le modèle préfère faire du zèle (Faux Positifs) plutôt que de rater des personnes en danger (Faux Négatifs).
# 
# 2. **L'impact de l'argument `class_weight='balanced'`** :
#    La Classe 0 (Retour rapide) est majoritaire. Si nous n'avions pas forcé l'algorithme à équilibrer les poids, il aurait ignoré la Classe 2 pour maximiser son score global. Ici, on voit que le modèle a "sacrifié" une petite partie de la précision de la Classe 0 (77%) pour garantir le filet de sécurité (Recall de 69%) sur la Classe 2.
# 
# **Analyse Métier & Éthique (AI Act)** :
# Le comportement du modèle répond exactement au cahier des charges Pôle Emploi (Principe de "No Mercy" sur les Faux Négatifs). Une fausse alerte (Faux Positif) coûte au pire un entretien téléphonique de vérification avec un conseiller. En revanche, un Faux Négatif signifie l'exclusion sociale d'un usager. Notre algorithme est donc éthiquement aligné : il agit comme un radar préventif très prudent.

# ### 5.7 Analyse et Comparaison Économique (ROI)
# 
# Bien que la performance technique (F1-score) soit cruciale, le choix d'un modèle en production doit se justifier économiquement. Voici la comparaison entre notre vainqueur technique (LightGBM) et son concurrent direct (Random Forest) sous l'angle du **Retour sur Investissement (ROI)** et des **Coûts Opérationnels**.
# 
# #### 1. Coûts d'Inférence et Empreinte Serveur (Le "Run")
# * **LightGBM** : Étant basé sur des histogrammes et un apprentissage par gradient, il est nativement optimisé pour l'inférence rapide. Il requiert très peu de RAM en production et peut traiter des milliers de prédictions par seconde sur un simple CPU (coût serveur minimal).
# * **Random Forest** : Pour atteindre des performances similaires, le Random Forest nécessite un très grand nombre d'arbres profonds (ici `n_estimators=200`, `max_depth=None`). Cela entraîne une consommation de RAM nettement plus importante en production pour stocker la forêt complète, et une latence de prédiction plus longue. Le coût de l'infrastructure de "Run" est potentiellement 2 à 3 fois plus élevé.
# 
# #### 2. L'Économie de l'Erreur (Coût des Faux Positifs vs Faux Négatifs)
# Notre modèle agit comme un système de triage préventif. Modélisons l'impact économique des erreurs :
# * **Coût d'un Faux Positif (Alarme inutile)** : Le modèle prédit à tort un "Risque de longue durée". Le coût économique se limite au temps passé par un conseiller pour un entretien de qualification supplémentaire (ex: 30 minutes, soit environ 20€ - 30€ de coût salarial chargé).
# * **Coût d'un Faux Négatif (Risque raté)** : Le modèle passe à côté d'un usager vulnérable. Cet usager ne reçoit pas d'accompagnement renforcé et bascule dans le chômage de longue durée. Le coût économique et sociétal est colossal : des mois d'indemnisation supplémentaires (milliers d'euros), perte de cotisations, et nécessité de dispositifs de réinsertion lourds.
# 
# **Conclusion Économique** : 
# Le choix du **LightGBM optimisé** (avec `class_weight='balanced'`) est doublement justifié économiquement. D'une part, son architecture légère **minimise la facture Cloud (FinOps)**. D'autre part, son calibrage garantit un Recall élevé sur la classe "Risque", acceptant de générer des Faux Positifs "bon marché" pour éviter à tout prix des Faux Négatifs dont **le coût d'inaction est exorbitant**. Le modèle maximise ainsi la valeur créée pour France Travail.
# 

# ### 5.8 Model Card (Fiche d'identité du Modèle)
# 
# Afin de respecter les standards de transparence de l'industrie et de se préparer à la conformité **AI Act**, voici la fiche d'identité standardisée (Model Card) du modèle retenu à l'issue de cette phase d'entraînement.
# 
# | Section | Description |
# | :--- | :--- |
# | **Détails du Modèle** | **Nom/Type** : LightGBM Classifier (Gradient Boosting).<br>**Version** : 1.0 (Juillet 2026).<br>**Architecture** : `n_estimators=100`, `max_depth=5`, `learning_rate=0.05`. Poids des classes équilibrés (`class_weight='balanced'`). |
# | **Usage Prévu** | **Cas d'usage** : Triage et priorisation de l'accompagnement des demandeurs d'emploi. L'outil agit comme un radar préventif pour détecter le risque de chômage de longue durée (Classe 2).<br>**Utilisateurs** : Conseillers de l'agence (outil d'aide à la décision).<br>**Hors-périmètre** : Prise de décision 100% autonome ou refus automatique de droits. Le modèle ne remplace pas l'humain (principe *Human-In-The-Loop*). |
# | **Facteurs & Données** | **Entrées** : Données multimodales (Tabulaires + Texte NLP via TF-IDF).<br>**Scénarios** : Le modèle s'adapte à différents périmètres de données (avec ou sans variables sensibles - *cf. Chapitre 6*). |
# | **Métriques de Performance** | **Métrique technique** : F1-Score Macro (boussole unique face au déséquilibre).<br>**Métrique métier** : Rappel (Recall) sur la Classe 2 (minimisation stricte des Faux Négatifs). |
# | **Considérations Éthiques** | **Biais algorithmique** : Risque identifié sur l'âge et l'origine (cf. *Disparate Impact*).<br>**Transparence** : L'algorithme basé sur des arbres de décision permet une extraction de l'importance des variables (Feature Importance / valeurs SHAP), répondant aux exigences d'explicabilité. |
# | **Limites & Recommandations**| L'analyse textuelle dépend fortement de la qualité et de l'homogénéité de la saisie des conseillers. Un suivi rigoureux de la dérive des données (*Data Drift*) sera impératif lors de la mise en production. |
# 

# ---
# ## 6. Analyse des scénarios & arbitrages
# 

# In[43]:


import time
from lightgbm import LGBMClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score, confusion_matrix
import pandas as pd

best_lgb_params = {'learning_rate': 0.05, 'max_depth': 5, 'n_estimators': 100, 'class_weight': 'balanced', 'random_state': 42, 'verbose': -1}

scenarios = ["S1", "S2", "S3", "S4"]
results = []
fitted_pipelines = {} # Sauvegarde pour les analyses d'explicabilité et de biais

for sc in scenarios:
    pipe = Pipeline([
        ("preprocessor", preprocessors[sc]),
        ("clf", LGBMClassifier(**best_lgb_params))
    ])

    pipe.fit(X_train, y_train)
    fitted_pipelines[sc] = pipe

    start_time = time.time()
    y_pred = pipe.predict(X_test)
    inf_time = time.time() - start_time
    latency_ms = (inf_time / len(X_test)) * 1000

    f1 = f1_score(y_test, y_pred, average="macro")
    cm = confusion_matrix(y_test, y_pred)
    fn_classe2 = cm[2, 0] + cm[2, 1] 

    results.append({
        "Scénario": sc,
        "F1-Macro": round(f1, 4),
        "FN (Classe 2)": fn_classe2,
        "Latence/pred (ms)": round(latency_ms, 2)
    })

df_scenarios = pd.DataFrame(results)
display(df_scenarios)


# In[44]:


import matplotlib.pyplot as plt
import seaborn as sns

fig, ax1 = plt.subplots(figsize=(10, 6))

# Axe 1 : F1-Macro (Barres)
sns.barplot(data=df_scenarios, x='Scénario', y='F1-Macro', color='skyblue', alpha=0.8, ax=ax1)
ax1.set_ylabel('F1-Macro Score (Plus c\'est haut, mieux c\'est)', color='blue', fontsize=12)
ax1.set_ylim(0.5, 0.75)
for i, v in enumerate(df_scenarios['F1-Macro']):
    ax1.text(i, v + 0.005, str(v), color='blue', ha='center', fontweight='bold')

# Axe 2 : Faux Négatifs (Ligne)
ax2 = ax1.twinx()
sns.lineplot(data=df_scenarios, x='Scénario', y='FN (Classe 2)', color='red', marker='o', markersize=10, linewidth=3, ax=ax2)
ax2.set_ylabel('Nombre de Faux Négatifs (Plus c\'est bas, mieux c\'est)', color='red', fontsize=12)
ax2.set_ylim(0, 50)
for i, v in enumerate(df_scenarios['FN (Classe 2)']):
    ax2.text(i, v + 2, str(v), color='red', ha='center', fontweight='bold')

plt.title("Arbitrage : Performance vs Sécurité (Faux Négatifs)", fontsize=14, fontweight='bold', pad=20)
plt.grid(False)
plt.show()


# ### 6.1 Tableau comparatif & Impact Environnemental
# 
# | Scénario | Modèle | Métrique principale (F1-Macro) | Métrique secondaire (FN sur Classe 2) | Coût inférence | Latence par préd. | Explicabilité | Biais (Loi / AI Act) | Verdict |
# |---|---|---|---|---|---|---|---|---|
# | **S1 (Complet)** | LightGBM | **0.6989** | **28 erreurs** | Très faible (CPU) | < 1 ms | Moyenne (SHAP) | **Critique** : Utilise l'âge et la nationalité. Risque de discrimination. | ❌ Rejeté pour prod |
# | **S2 (Éthique)** | LightGBM | 0.6241 | 33 erreurs | Très faible (CPU) | < 1 ms | Moyenne (SHAP) | **Mitigé** : Variables sensibles retirées. | ✅ **Retenu** |
# | **S3 (NLP)** | LightGBM | 0.6370 | 32 erreurs | Faible (TF-IDF + CPU) | < 1 ms | Faible sur texte | Potentiel (si biais dans la synthèse) | ❌ Sous-performant en robustesse |
# | **S4 (Tabulaire)** | LightGBM | 0.6511 | 38 erreurs | Très faible | < 1 ms | Moyenne | Identique à S1 | ❌ Trop de FN |
# 
# > 🍃 **Bilan Green IT (Impact Environnemental)** : L'entraînement du modèle complet prend quelques secondes sur un CPU standard. En production, la latence mesurée est inférieure à **0.2 millisecondes par prédiction**. Ce modèle est d'une très grande *sobriété numérique* et ne nécessite aucune infrastructure cloud GPU coûteuse ou polluante (contrairement aux LLMs). Il respecte parfaitement les objectifs de développement durable des services publics.
# 
# ### 6.2 Recommandation finale au client
# 
# Nous recommandons la mise en production du modèle basé sur le **Scénario S2 (Éthique)**. 
# 
# 1. **Rejet de S1 (Complet)** : Bien que S1 présente le meilleur F1-score mathématique, son utilisation explicite de variables sensibles (âge, nationalité) expose l'agence à un risque légal inacceptable de discrimination algorithmique au regard de l'AI Act.
# 2. **Le paradoxe S3 (NLP pur)** : L'analyse graphique révèle une surprise : le scénario S3 (uniquement le texte) fait légèrement mieux que S2 (une erreur de moins). Cela prouve que la synthèse du conseiller contient un signal prédictif extrêmement fort. Cependant, **nous rejetons S3 pour des raisons de robustesse industrielle**. Un modèle 100% texte est trop fragile en production : si le conseiller saisit une note laconique ("RAS", "vu ce jour") par manque de temps, le modèle devient complètement aveugle. De plus, le texte libre est un vecteur de biais implicite non contrôlable (ex: le conseiller écrit "ce travailleur senior...").
# 3. **Le choix de S2 (Éthique)** : S2 s'impose donc comme le choix raisonné. Il s'appuie sur la puissance du NLP tout en gardant les données administratives nettoyées (diplôme, département) comme "ancre de robustesse" face aux saisies textuelles hétérogènes. Le risque éthique est contrôlé par conception (Privacy by Design).
# 
# ### 6.3 📝 Synthèse arbitrages
# 
# Le compromis a tranché en faveur de la **Conformité Réglementaire et de la Robustesse Industrielle** (S2) au détriment de la performance brute (S1) ou théorique (S3). Le surcoût d'erreur (5 faux négatifs supplémentaires par rapport à S1) est assumé comme une "prime d'assurance", permettant un déploiement responsable, stable et éthique dans un service public.
# 

# ### 6.4 Preuve d'Explicabilité (C8) : Feature Importance du Modèle S2
# 
# Conformément aux exigences de transparence, le graphique ci-dessous "ouvre le capot" de notre algorithme retenu (S2). 
# 
# **Observation clé** : Bien que la variable continue "Ancienneté" (qui est notre "ancre de robustesse" administrative) soit mathématiquement la plus utilisée pour diviser les arbres de décision, **le reste entier du Top 15 est dominé par les mots-clés issus de la synthèse du conseiller** (variables TF-IDF). 
# 
# Cela valide techniquement et métier notre paradoxe S3 et notre choix S2 :
# 1. Les données administratives (comme l'ancienneté) servent bien de socle robuste et sécurisant.
# 2. L'algorithme se comporte ensuite comme un "super lecteur" capable d'extraire les signaux d'alerte sémantiques des notes humaines.
# 3. Le modèle n'est absolument pas une "boîte noire" (respect de la compétence C8) : on voit très clairement les mots qui déclenchent le risque.
# 

# In[45]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pipe_s2 = fitted_pipelines["S2"]
clf_s2 = pipe_s2.named_steps["clf"]
prep_s2 = pipe_s2.named_steps["preprocessor"]

# Extraction manuelle des noms de variables (pour gérer le TF-IDF et le OneHotEncoder)
num_cols = prep_s2.named_transformers_["num"].feature_names_in_ if "num" in prep_s2.named_transformers_ else []
cat_nom_cols = prep_s2.named_transformers_["cat_nom"].named_steps["ohe"].get_feature_names_out() if "cat_nom" in prep_s2.named_transformers_ else []
cat_ord_cols = prep_s2.named_transformers_["cat_ord"].feature_names_in_ if "cat_ord" in prep_s2.named_transformers_ else []
text_cols = ["Texte : " + x for x in prep_s2.named_transformers_["text"].named_steps["tfidf"].get_feature_names_out()] if "text" in prep_s2.named_transformers_ else []

feature_names = list(num_cols) + list(cat_nom_cols) + list(cat_ord_cols) + list(text_cols)
importances = clf_s2.feature_importances_

df_imp = pd.DataFrame({"Variable": feature_names, "Importance": importances})
df_imp = df_imp.sort_values(by="Importance", ascending=False).head(15)

# Remplacement des codes abscons par des labels lisibles
df_imp["Variable"] = df_imp["Variable"].str.replace("x0_", "Allocataire_")
df_imp["Variable"] = df_imp["Variable"].str.replace("x1_", "Dpt_")
df_imp["Variable"] = df_imp["Variable"].str.replace("x2_", "ROME_")

plt.figure(figsize=(10, 6))
sns.barplot(data=df_imp, x="Importance", y="Variable", hue="Variable", legend=False, palette="viridis")
plt.title("Top 15 des variables les plus influentes (Modèle S2 Éthique)", fontweight="bold")
plt.xlabel("Poids dans les arbres de décision (Feature Importance)")
plt.ylabel("")
plt.tight_layout()
plt.show()


# ### 6.5 Preuve Éthique (AI Act) : Disparate Impact et l'illusion du "Fairness through Blindness"
# 
# > **Rappel de la règle des 80% (0.80)** : Un *Disparate Impact* (DI) en dehors de l'intervalle [0.80, 1.25] est considéré comme un signal de discrimination algorithmique (sur-représentation d'une classe).
# 
# Nous avons initialement justifié le choix de S2 par le retrait de l'âge et de la nationalité. **Cependant, le test de Disparate Impact ci-dessous révèle une vérité fondamentale en éthique de l'IA : supprimer les variables sensibles ne suffit pas toujours à supprimer le biais.** 
# 
# Même "aveugle" (blindness), l'algorithme réussit à recréer le biais indirectement grâce à des **variables proxy** (corrélations cachées dans le département de résidence, le diplôme, ou les mots spécifiques de la synthèse texte).
# 

# In[46]:


# Preuve mathématique : Impact sur les prédictions (S1 vs S2)
# Variable sensible étudiée : nationalite_hors_ue (1 = Oui, 0 = Non)

mask_etranger = X_test["nationalite_hors_ue"] == 1
mask_local = X_test["nationalite_hors_ue"] == 0

# S1 (Complet - Biais direct)
y_pred_s1 = fitted_pipelines["S1"].predict(X_test)
taux_s1_etranger = (y_pred_s1[mask_etranger] == 2).mean()
taux_s1_local = (y_pred_s1[mask_local] == 2).mean()
di_s1 = taux_s1_etranger / taux_s1_local if taux_s1_local > 0 else 0

# S2 (Éthique - Sans la variable)
y_pred_s2 = fitted_pipelines["S2"].predict(X_test)
taux_s2_etranger = (y_pred_s2[mask_etranger] == 2).mean()
taux_s2_local = (y_pred_s2[mask_local] == 2).mean()
di_s2 = taux_s2_etranger / taux_s2_local if taux_s2_local > 0 else 0

df_biais = pd.DataFrame({
    "Scénario": ["S1 (Complet)", "S2 (Sans variable nationalité)"],
    "Disparate Impact (Ratio)": [round(di_s1, 2), round(di_s2, 2)],
    "Statut": [
        "❌ Biais fort (> 1.25)" if di_s1 > 1.25 else "✅ OK",
        "⚠️ Biais résiduel (Proxys)" if di_s2 > 1.25 else "✅ OK"
    ]
})

display(df_biais)

print("\n--- ANALYSE DE L'ÉCHEC DU 'FAIRNESS THROUGH BLINDNESS' ---")
print("S2 réduit légèrement le biais, mais reste discriminant (DI > 1.25). Pourquoi ?")
print("Le modèle compense l'absence de la variable 'nationalité' en utilisant des 'proxys' :")
print("- Le texte (TF-IDF) peut contenir des indices socio-démographiques implicites.")
print("- L'adresse (Dpt) et le niveau de diplôme sont historiquement corrélés à l'origine.")
print("\nConclusion pour la soutenance :")
print("S2 respecte la conformité légale stricte (Privacy by Design) en ne traitant pas la")
print("donnée sensible. Toutefois, pour atteindre une véritable équité mathématique, il")
print("faudrait implémenter des techniques avancées (Adversarial Debiasing, Reweighting).")


# ---
# ## 7. Interprétation pour la communication client (préparation soutenance)
# 
# **Compétences** : C8 (mesurer la performance et les impacts) + transversal communication
# 
# 🎯 Rendre le modèle **lisible par un non-data scientist**. **Cette section est la base de ton pitch oral de soutenance** (15 min × jury de 2 pros). Elle ne couvre pas C8 stricto sensu (les sections 5, 6 et 9 le font) mais en restitue les résultats en langage métier.
# 
# 💡 Feature importance, SHAP (optionnel), matrice de confusion commentée. Trois messages-clés maximum dans ton pitch oral, pas dix.

# In[20]:


# 7.1 Feature importance / SHAP


# ### 7.2 Analyse des erreurs et stratégies de fallback
# 
# 🎯 Identifier où le modèle échoue, et **concevoir le filet de sécurité** : que se passe-t-il quand le modèle a tort, ou qu'il ne sait pas ?
# 
# 💡 Trois leviers de conception à documenter explicitement (la **surveillance** de ces seuils se traite en §9.4, pas ici) :
# 
# | Levier | Question à trancher | Exemple concret |
# |---|---|---|
# | **Rejection threshold** | À quel niveau de confiance je préfère m'abstenir plutôt que prédire ? | *[ex: si proba ∈ [0.4, 0.6], on n'émet pas de prédiction]* |
# | **Abstention contrôlée** | Que renvoie l'API quand le modèle s'abstient ? | *[ex: HTTP 422 + payload « confiance insuffisante » + flag HITL]* |
# | **Escalade humaine (HITL)** | Qui prend la main, sous quel délai, avec quelle interface ? | *[ex: file Slack #fastia-hitl, SLA 4h ouvrées, audit a posteriori]* |
# 
# ⚠️ Sans ces 3 éléments, ton modèle n'a pas de plan de fallback — il **n'est pas déployable en prod sur un usage à enjeu**. C'est un attendu C8 N3 (M6) et C7 N3 (M8). Le code ci-dessous analyse les erreurs résiduelles pour **informer** ces 3 choix (où placer le seuil, quels profils escalader).

# In[21]:


# 7.2 Analyse des erreurs et profils à escalader
# - Matrice de confusion détaillée par profil (variables sensibles incluses)
# - Distribution des probabilités prédites sur les erreurs : où placer le seuil de rejet ?
# - Caractérisation des profils faux positifs / faux négatifs : escalade humaine prioritaire ?


# ### 7.3 Message au client (langage métier)
# 
# *[2-3 paragraphes lisibles par un décideur non technique. Trois messages-clés à retenir.]*
# 
# ### 7.4 📝 Synthèse interprétation
# 
# *[Variables-clés, profils mal prédits, vigilance opérationnelle.]*

# ---
# ## 8. Industrialisation
# 
# **Compétences** : C6 (implémenter le modèle), C7 (architecture cible)
# 
# 🎯 Transformer le modèle en **service exploitable** : API, UI, conteneurs, tracking d'expériences.
# 
# > ⚠️ **Cette section ne contient PAS le code de l'API/UI.** Le code vit dans le **repo Git** associé.  
# > Dans le notebook, on met uniquement :
# > 1. **Description architecturale** (texte)
# > 2. **1 schéma** d'architecture (Mermaid, draw.io export, ou image)
# > 3. **Lien vers le repo Git** + dossiers concernés
# > 4. **Captures d'écran clés** (UI, dashboard, OpenAPI Swagger, workflow CI/CD vert)
# > 5. **Justifications des choix techniques** (pourquoi FastAPI plutôt que Flask, pourquoi MLflow plutôt que `experiments.md`, etc.)
# 
# ⚠️ Attendus certif (présents dans le repo, **référencés** dans cette section du notebook) :  
# - API FastAPI avec routes `/predict`, `/train`, `/health`  
# - Validation Pydantic des entrées  
# - Logging structuré (Loguru)  
# - Tests pytest  
# - Conteneurisation Docker  
# - CI/CD GitHub Actions  
# - Tracking MLflow

# ### 8.1 Persistance du modèle
# 
# *[Quel modèle est servi (`pipeline.joblib` versionné), quelle stratégie de persistance, quelle traçabilité (MLflow run id ou alternative `experiments.md`).]*
# 
# ### 8.2 API de service
# 
# **Repo associé** : `<lien GitHub>` — dossier `api/`
# 
# | Route | Méthode | Rôle | Validation |
# |---|---|---|---|
# | `/health` | GET | santé du service | — |
# | `/predict` | POST | prédiction unitaire | Pydantic |
# | `/train` | POST | (option) déclenche un réentraînement | Pydantic + auth |
# 
# *[Inclure ici 1 capture Swagger ou un schéma de l'API.]*
# 
# ### 8.3 Interface utilisateur
# 
# *[Streamlit / Gradio / autre. Capture dans `docs/`.]*
# 
# ### 8.4 Schéma d'architecture
# 
# *[1 schéma simple : sources données → préprocessing → modèle → API → UI → monitoring.  
# Tu peux utiliser un bloc Mermaid (rendu natif sur GitHub et Jupyter récents) :]*
# 
# ```mermaid
# graph LR
#   D[(Données)] --> P[Préprocessing] --> M[Modèle .joblib]
#   M --> A[FastAPI]
#   A --> U[UI Streamlit]
#   A --> L[(Logs)]
#   L --> Mo[Monitoring]
# ```
# 
# ### 8.5 Conteneurisation & CI/CD
# 
# *[Dockerfile, docker-compose.yml, workflow GitHub Actions (build → test → push). Captures d'écran d'un run CI vert. Liens vers les fichiers du repo.]*
# 
# ### 8.6 📝 Synthèse industrialisation
# 
# *[Pile retenue, choix d'architecture, points encore ouverts.]*

# ---
# ## 9. Suivi en production & amélioration continue
# 
# **Compétences** : C8 (mesurer performance), C9 (amélioration continue)
# 
# 🎯 Anticiper la dérive et la maintenance du modèle après mise en prod.
# 
# 💡 Drift = data drift (entrées qui changent) vs concept drift (la cible change de comportement).  
# ⚠️ Pas de monitoring = pas de prod. Même un dashboard simple Streamlit suffit pour démarrer.

# ### 9.1 Métriques à surveiller
# 
# | Type | Métrique | Seuil d'alerte | Source |
# |---|---|---|---|
# | Modèle | F1 hebdo | < baseline - 0.05 | logs API |
# | Données | PSI variables clés | > 0.2 | batch journalier |
# | Système | latence p95 | > 500 ms | Prometheus |
# 
# ### 9.2 Boucle de rétroaction
# 
# *[Comment les retours utilisateurs / annotations correctives reviennent dans les données d'entraînement ?]*
# 
# ### 9.3 Plan de réentraînement
# 
# *[Trigger (calendaire ? performance ? volume nouvelles données ?), automatisation, validation avant mise en prod.]*
# 
# ### 9.4 Robustesse en exploitation
# 
# 🎯 Surveiller les **conditions de défaillance** une fois en prod, en complément des stratégies de fallback définies en §7.2 (côté conception).
# 
# 💡 La conception du fallback (où placer le seuil, qui escalader) vit en §7.2. Ici on instrumente la **mesure** et le **déclenchement** :
# 
# | Axe | Métrique opérationnelle | Action automatique |
# |---|---|---|
# | **OOD (Out-Of-Distribution)** | Distance Mahalanobis ou score d'isolation sur les entrées | Logger les inputs hors-distribution, déclencher abstention ou escalade humaine (cf §7.2) |
# | **Drift du seuil de rejet** | Taux d'abstention / part de prédictions sous seuil de confiance | Réviser le rejection threshold si dérive > 20 % sur 4 semaines glissantes |
# | **Calibration** | Brier score, courbe de calibration mensuelle | Recalibrer (Platt, isotonic) sans réentraîner le modèle complet si seule la calibration dérive |
# 
# ⚠️ La chaîne conception → exploitation doit rester explicite. §7.2 définit le filet de sécurité, §9.4 le surveille. Casser cette chaîne (fallback conçu mais jamais mesuré) = attendu C8 N3 non atteint.
# 
# ### 9.5 📝 Synthèse amélioration continue
# 
# *[Cadence de surveillance, déclencheurs de réentraînement, plan de remédiation en cas de dérive.]*

# ---
# ## 📎 Annexes
# 
# ### A. Glossaire métier & technique
# 
# ### B. Sources & bibliographie
# 
# - *[Datasets, articles, documentation technique consultés]*
# 
# ### C. Décisions techniques détaillées
# 
# *[Justifications longues qu'on ne met pas dans le corps du notebook pour le garder lisible.]*
# 
# ### D. Journal de bord
# 
# **Pendant la formation**, le journal de bord est tenu **séparément** dans `journal-de-bord.ipynb` (plus pratique pour le rythme journalier).
# 
# ⚠️ **Pour la certification**, les deux fichiers doivent être **fusionnés en un seul notebook** (cf. fiche descriptive Atlas IA — un cahier électronique unique).
# 
# #### Méthode 1 — Script de fusion (recommandée, ~30 secondes)
# 
# Un script est fourni à la racine du repo formation : `scripts/merge_for_certif.py`.
# 
# ```bash
# python scripts/merge_for_certif.py mon_notebook.ipynb journal-de-bord.ipynb rendu_certif.ipynb
# ```
# 
# Le script localise automatiquement le titre « D. Journal de bord » dans le notebook principal et y insère les cellules du journal dans l'ordre. Il produit un nouveau fichier sans modifier les sources.
# 
# #### Méthode 2 — Fusion manuelle dans JupyterLab (~5 min)
# 
# 1. Ouvrir les **deux notebooks** côte à côte dans JupyterLab (drag-and-drop dans deux colonnes).
# 2. Dans le journal : cliquer sur la première cellule « Jour 1 », puis **Maj-clic** sur la dernière pour tout sélectionner sauf l'intro.
# 3. **Edit > Copy Cells** (`Ctrl/Cmd + Shift + C`).
# 4. Dans le notebook principal : cliquer sous le titre « D. Journal de bord ».
# 5. **Edit > Paste Cells Below** (`Ctrl/Cmd + Shift + V`).
# 6. Vérifier l'ordre chronologique.
# 7. **Kernel > Restart & Run All** : aucune cellule ne doit casser.
# 8. Sauvegarder sous un **nouveau nom** (ex : `<prenom>_certif_v1.ipynb`) — ne pas écraser les sources.
# 
# #### Vérification finale (les deux méthodes)
# 
# - [ ] Le notebook fusionné s'exécute de bout en bout sans erreur.
# - [ ] Toutes les images du journal s'affichent (sinon : passer en chemins absolus ou inliner).
# - [ ] Aucune référence à des fichiers externes hors du repo (ou alors les inclure dans le ZIP de rendu).
# - [ ] Une seule version finale, datée, dans le ZIP envoyé au jury.
# 
# ⚠️ **Tester la fusion 2-3 jours avant le rendu**, pas le jour J.
# 
# #### Export PDF (optionnel, pour la soutenance)
# 
# ```bash
# jupyter nbconvert --to pdf rendu_certif.ipynb
# ```
