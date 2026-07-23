# 📄 Datasheet — Dataset Trajectoire Emploi (version clean)

> **Modèle Gebru et al. (2018), format 7 sections (1 page max).**  
> Document de traçabilité d'ingénierie et d'audit éthique/qualité.  
> **Public cible :** DPO + équipe métier + équipe data science — lisible par un non-data-scientist.

---

## 1. Motivation

Ce dataset est fourni pour prototyper un cas d'usage d'orientation et de tri multimodal des demandeurs d'emploi (système expert d'aiguillage).

- **Source principale :** `dataset_trajectoire_emploi.csv` (historique d'accompagnement usagers).
- **Objectif initial :** Estimer le risque de délai de retour à l'emploi (`classe_retour_emploi`) à partir de caractéristiques socio-économiques, géographiques et textuelles.
- **Objectif de cette version "clean" :** Fournir un dataset consolidé, relisible et documenté pour audit qualité/éthique et expérimentation contrôlée sous les exigences de l'AI Act.

---

## 2. Composition

> Précisions sur la volumétrie, le typage des colonnes, la distribution de la cible et les **variables sensibles signalées explicitement**.

| Aspect | Valeur |
|---|---|
| Nombre de lignes | 2500 |
| Nombre de colonnes | 10 colonnes |
| Cible | `classe_retour_emploi` : `0` (< 6 mois), `1` (6-12 mois), `2` (> 12 mois) |
| Distribution cible | `0` : 44.0 % / `1` : 38.0 % / `2` : 18.0 % (déséquilibre) |
| Variables sensibles | `age` ⚠️ (âgisme), `nationalite_hors_ue` ⚠️ (origine), `synthese_entretien` ⚠️ (PII) |
| Valeurs manquantes | `niveau_diplome` (imputées par modalité majoritaire) |

**Schéma des colonnes** :

| Colonne | Type | Modalités / range | Note |
|---|---|---|---|
| `usager_id` | Identifiant | String / UUID | Exclu du pipeline de modélisation |
| `age` | Numérique | 18 — 64 ans | Variable sensible (âgisme) |
| `niveau_diplome` | Catégorielle ordonnée | Sans diplôme, Bac, Bac+2, Bac+5 | Encodée en ordinal |
| `anciennete_poste_ans` | Numérique | 0 — 40 ans | Expérience dans le dernier emploi |
| `code_rome_vise` | Catégorielle | Code ROME 5 chars | Réduit à la famille ROME (1er char) |
| `code_insee_commune` | Catégorielle | Code géo INSEE 5 chars | Réduit au département (2 1ers chars) |
| `est_allocataire` | Catégorielle / Booléen | 0, 1 | Statut d'indemnisation |
| `nationalite_hors_ue` | Catégorielle / Booléen | 0, 1 | Variable sensible (origine) |
| `synthese_entretien` | Texte libre | Notes du conseiller | Traitement NLP (TF-IDF 1000 features) |
| `classe_retour_emploi` | Cible multiclasse | 0 (< 6m), 1 (6-12m), 2 (> 12m) | Déséquilibre sur la classe 2 (18 %) |

---

## 3. Processus de collecte

- Représente un historique de dossiers de demandeurs d'emploi suivis en agence.
- **Biais de sélection probable :** Seules les personnes inscrites à l'agence sont représentées (pas la population générale).
- **Biais historique probable :** La cible `classe_retour_emploi` peut refléter des discriminations ou des pratiques métiers antérieures.

---

## 4. Préprocessing appliqué

- **Imputation des manquants :**
  - numériques : médiane (`SimpleImputer(strategy="median")`),
  - catégorielles/ordinales : modalité la plus fréquente (`SimpleImputer(strategy="most_frequent")`).
- **Encodage des catégorielles :**
  - nominales (`departement`, `famille_rome`, `est_allocataire`) : `OneHotEncoder(handle_unknown="ignore", drop="first")`,
  - ordinales (`niveau_diplome`) : `OrdinalEncoder` avec ordre hiérarchique explicite.
- **Normalisation des numériques :** `StandardScaler` (`age`, `anciennete_poste_ans`).
- **Traitement NLP :** Extraction de texte et `TfidfVectorizer` (stop words français, max 1000 features).
- **Scénarios Éthiques :** En Mode S2 (Éthique), retrait des variables sensibles `age` et `nationalite_hors_ue` (*Privacy by Design*).

---

## 5. Usages prévus / à éviter

**Usages prévus :**
- Outil d'aide à la décision (système d'aiguillage) sous supervision humaine (Human-In-The-Loop).
- Audit de qualité de données et détection de biais éthiques (Disparate Impact).

**Usages à éviter :**
- Décision 100% automatisée sans contrôle humain (interdit par l'AI Act / RGPD Art. 22).
- Profilage répressif ou exclusion automatique d'allocataires.
- Réutilisation hors contexte sans recalibrage.

---

## 6. Distribution

- **Transmis à :** Équipe Data Science, Équipe Métier, DPO.
- **Format :** CSV / Parquet local (`data/dataset_trajectoire_emploi.csv`).
- **Conditions :** Usage interne, accès contrôlé, interdiction de diffusion externe sans validation DPO.

---

## 7. Maintenance

- **Mainteneur :** Franck BEUGNET.
- **Version :** v1.0.0 — 2026-07-23.
- **Contact issue :** Ouvrir un ticket interne Data Quality / Conformité.

---
*Datasheet produite selon la méthodologie Gebru et al. (2018).*
