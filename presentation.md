---
marp: true
theme: default
paginate: true
header: "🎓 **Soutenance de Certification** — Ingénieur IA"
footer: "🧑‍💻 **Candidat** : Franck Beugnet | 🚀 **Projet** : IA d'Orientation Professionnelle"
size: 16:9
style: |
  section {
    font-size: 26px;
  }
  h1 {
    color: #0d47a1;
  }
  h2 {
    color: #1565c0;
  }
  header {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    padding: 15px 40px;
    box-sizing: border-box;
    background-color: #f0f4f8;
    color: #0d47a1;
    font-size: 20px;
    font-weight: 600;
    border-bottom: 3px solid #1565c0;
  }
  footer {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 15px 40px;
    box-sizing: border-box;
    background-color: #f0f4f8;
    color: #0d47a1;
    font-size: 18px;
    border-top: 3px solid #1565c0;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .tech-box {
    background-color: #f0f4f8;
    border-left: 5px solid #1976d2;
    padding: 10px;
    margin-top: 10px;
    font-size: 22px;
  }
  .si-card {
    background: #ffffff;
    border: 2px solid #1565c0;
    border-radius: 8px;
    padding: 10px 14px;
    text-align: center;
    box-shadow: 2px 2px 8px rgba(0,0,0,0.08);
  }
  .si-arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: #0d47a1;
    font-weight: bold;
  }
---

<!-- _class: lead -->
# Projet de Certification IA
## Système d'Orientation et de Prévention du Chômage Longue Durée

**Candidat : Franck Beugnet** — *Promo ATOS Atlas IA (Parcours 2 : Pros IT)*  
*Conception, industrialisation et audit d'un produit Data de bout en bout*

**Stack :** Python 3.12 · Scikit-Learn · LightGBM · FastAPI · Streamlit · MLflow · Prometheus · Docker

---

# Plan de la Soutenance (30 minutes cadencées)

1. **Cadrage Métier, Éthique & Objectifs (AI Act)** `[00:00 - 05:00 | 5 min]`
2. **Audit, Qualité & Pipeline End-to-End** `[05:00 - 10:00 | 5 min]`
3. **Modélisation, 4 Scénarios & Explicabilité (SHAP)** `[10:00 - 17:00 | 7 min]`
4. **Architecture Cible, Flux SI & Déploiement API** `[17:00 - 22:00 | 5 min]`
5. **Supervision MLOps, CI/CD & Dérive (Drift)** `[22:00 - 27:00 | 5 min]`
6. **Bilan Économique, Perspectives & Démonstration** `[27:00 - 30:00 | 3 min]`

---

# 1. Cadrage Métier & Objectifs

---

## Le Constat Métier

<style scoped>
section { font-size: 18px; padding-top: 52px; padding-bottom: 45px; }
.hero-context {
  background: #f0f4f8;
  border-left: 4px solid #1565c0;
  padding: 5px 12px;
  margin-bottom: 10px;
  font-size: 15px;
  line-height: 1.3;
  border-radius: 0 5px 5px 0;
  color: #0d47a1;
}
.main-grid {
  display: grid;
  grid-template-columns: 1fr 1.25fr;
  gap: 1rem;
  align-items: stretch;
}
.meta-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 8px 12px;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.matrix-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 4px;
  font-size: 13px;
  text-align: center;
  margin: 0;
}
.matrix-table th, .matrix-table td {
  padding: 5px 5px;
  border-radius: 4px;
}
</style>

<div class="hero-context">
  <b>Contexte métier :</b> Au sein du service public de l'emploi, le premier entretien d'aiguillage est un moment décisif où le conseiller doit identifier au plus tôt les situations vulnérables afin de mobiliser immédiatement le bon accompagnement.
</div>

<div class="main-grid">
  <div class="meta-card">
    <div>
      <div style="font-weight: bold; color: #1565c0; margin-bottom: 6px; font-size: 15.5px;">
        🎯 Le Défi Opérationnel au Guichet
      </div>
      <ul style="margin: 0; padding-left: 18px; line-height: 1.35; font-size: 14px;">
        <li style="margin-bottom: 4px;"><b>Flux massif d'usagers :</b> Temps d'échange limité pour déceler les freins périphériques.</li>
        <li style="margin-bottom: 4px;"><b>Solution IA Multimodale :</b> Fusion des critères administratifs et des notes textuelles du conseiller.</li>
        <li><b>Répartition de la cible terrain :</b><br>
          • <b>Classe 0 (Rapide &lt; 6m) :</b> 37% <i>(autonomie)</i><br>
          • <b>Classe 1 (Moyen 6-12m) :</b> 44% <i>(parcours standard)</i><br>
          • <b>Classe 2 (Risque &gt; 12m) :</b> <b style="color: #c62828;">18% (critique)</b>
        </li>
      </ul>
    </div>
    <div style="margin-top: 8px; padding: 6px 10px; background: #eef2f6; border-left: 3px solid #1565c0; border-radius: 4px; font-size: 12.5px; color: #263238; line-height: 1.3;">
      <b>Objectif opérationnel :</b> Déclencher l'accompagnement renforcé dès le 1<sup>er</sup> jour pour éviter l'enlisement dans le chômage longue durée.
    </div>
  </div>

  <div class="meta-card">
    <div style="font-weight: bold; color: #1565c0; margin-bottom: 4px; font-size: 15px;">
      ⚖️ Matrice d'Impact Métier & Asymétrie des Coûts
    </div>
<table class="matrix-table">
  <thead>
    <tr>
      <th style="width: 32%; background: transparent; border: none;"></th>
      <th style="background: #e3f2fd; color: #0d47a1; font-weight: bold; font-size: 12.5px;">L'IA prédit "Risque"</th>
      <th style="background: #f5f5f5; color: #424242; font-weight: bold; font-size: 12.5px;">L'IA prédit "Rapide"</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background: #ffebee; color: #b71c1c; font-weight: bold; font-size: 12.5px;">
        Réel : Risque Long<br><span style="font-size: 10.5px; font-weight: normal; color: #666;">(Classe 2 — 18%)</span>
      </td>
      <td style="background: #e8f5e9; border: 1.5px solid #2e7d32; color: #1b5e20;">
        <b>Vrai Positif (VP)</b><br>
        <span style="font-size: 11.5px;">✅ Usager orienté & sauvé</span>
      </td>
      <td style="background: #ffebee; border: 2px solid #c62828; color: #b71c1c;">
        <b>Faux Négatif (FN)</b><br>
        <span style="font-size: 11.5px; font-weight: bold;">🚨 DANGER ABSOLU</span><br>
        <span style="font-size: 10.5px;">Perte de chance critique</span>
      </td>
    </tr>
    <tr>
      <td style="background: #e8f5e9; color: #1b5e20; font-weight: bold; font-size: 12.5px;">
        Réel : Retour Rapide<br><span style="font-size: 10.5px; font-weight: normal; color: #666;">(Classe 0 — 37%)</span>
      </td>
      <td style="background: #fff8e1; border: 1.5px solid #f57c00; color: #e65100;">
        <b>Faux Positif (FP)</b><br>
        <span style="font-size: 11.5px;">⚠️ Aide inutile</span><br>
        <span style="font-size: 10.5px;">Coût financier acceptable</span>
      </td>
      <td style="background: #e8f5e9; border: 1.5px solid #2e7d32; color: #1b5e20;">
        <b>Vrai Négatif (VN)</b><br>
        <span style="font-size: 11.5px;">✅ Usager autonome</span>
      </td>
    </tr>
  </tbody>
</table>
<div style="font-size: 12px; margin-top: 4px; padding: 5px 8px; line-height: 1.25; border-left: 3px solid #c62828; background-color: #fff5f5; border-radius: 3px;">
  <b style="color: #b71c1c;">Doctrine "No Mercy" sur le Risque (Priorité au Rappel Classe 2) :</b><br>
  Prédire 0 pour un vrai 2 prive l'usager d'aides vitales. Notre modèle sur-pénalise les Faux Négatifs : mieux vaut accompagner préventivement que d'abandonner un usager à risque.
</div>
  </div>
</div>

---

## Cadre Réglementaire, RGPD & Responsabilité Juridique

<style scoped> section { font-size: 19px; padding-top: 75px; } </style>

L'usage de l'IA dans l'orientation professionnelle impose un cadre de conformité strict :

1. **AI Act Européen (Classification Haut Risque — Annexe III) :**
   - Les systèmes d'IA utilisés dans l'emploi et l'orientation relèvent de la catégorie **Haut Risque**.
   - Exigences impératives : traçabilité des données, explicabilité, gouvernance des biais et **supervision humaine obligatoire (*Human-In-The-Loop*)**.
2. **Loi pour une République Numérique (Art. L311-3-1) & RGPD :**
   - Droit pour l'usager à l'information et à l'explicabilité individuelle des règles algorithmiques appliquées.
   - **Précision juridique RGPD :** L'âge et la nationalité sont des *données personnelles ordinaires* (Art. 4), mais constituent des critères protégés majeurs contre la discrimination au travail. Le texte libre (`synthese_entretien`) est surveillé pour éviter les données sensibles au sens strict de l'Art. 9 (santé, handicap).
3. **Responsabilité Juridique & Notion de "Perte de Chance" :**
   - Si un usager vulnérable est mal orienté (classé en retour rapide par erreur), il subit un préjudice (privation d'aides ou de formations). Devant le Tribunal Administratif, la **perte de chance** engage la responsabilité de l'administration.
   - **Protection juridique par conception :** L'outil est strictement qualifié d'**aide à la décision consultative**. L'agent public valide et endosse souverainement la décision finale.

---

# 2. Audit & Ingénierie des Données

---

## Le Défi de la Donnée : "Small Data", Cardinalité & Prétraitement

<style scoped>
section { font-size: 17px; padding-top: 52px; padding-bottom: 45px; }
.top-box {
  background: #f0f4f8;
  border-left: 4px solid #1565c0;
  padding: 5px 12px;
  margin-bottom: 8px;
  font-size: 14.5px;
  line-height: 1.3;
  color: #0d47a1;
}
.prep-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.9rem;
  margin-top: 4px;
}
.prep-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 8px 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.prep-card h3 {
  margin: 0 0 5px 0;
  font-size: 14.5px;
  color: #1565c0;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 3px;
}
ul { margin: 0; padding-left: 17px; font-size: 13.5px; line-height: 1.3; }
li { margin-bottom: 3px; }
</style>

<div class="top-box">
  <b>Jeu de données & contraintes :</b> 2 500 usagers, 10 variables, valeurs manquantes (âge, diplôme, allocataire, texte). Défi majeur : cardinalité extrême (2 400 communes, 50 métiers) ➔ Risque d'overfitting immédiat.
</div>

<div class="prep-grid">
  <div class="prep-card">
    <h3>1. Feature Engineering (Macro-Tendances)</h3>
    <ul>
      <li><b>Département :</b> 2 premiers chiffres du code INSEE (réduit de 2 400 à ~95 catégories).</li>
      <li><b>Famille ROME :</b> 1<sup>ère</sup> lettre du code ROME (réduit à 14 grands secteurs).</li>
      <li><b>Compromis assumé :</b> On sacrifie l'hyper-local pour garantir la capacité de généralisation sur 2 500 profils.</li>
    </ul>
  </div>

  <div class="prep-card">
    <h3>2. Variables Numériques (Âge, Ancienneté)</h3>
    <ul>
      <li><b>Cases vides (Imputation) :</b> Remplacement par la valeur médiane pour ne pas être faussé par les cas extrêmes.</li>
      <li><b>Mise à la même échelle (Standardisation) :</b> Ajuste l'âge et les années d'expérience sur un pied d'égalité, évitant qu'un grand chiffre n'écrase les autres données.</li>
    </ul>
  </div>

  <div class="prep-card">
    <h3>3. Catégorielles Ordinales (Diplôme)</h3>
    <ul>
      <li><b>Ordre d'études respecté :</b> Traduction en score croissant selon le niveau :<br>
        <i>Sans diplôme (0) &lt; Bac (1) &lt; Bac+2 (2) &lt; Bac+5 (3)</i>.</li>
      <li><b>Valeurs manquantes ou imprévues :</b> Remplacées par le diplôme le plus fréquent, avec filet de sécurité si un profil inédit arrive.</li>
    </ul>
  </div>

  <div class="prep-card">
    <h3>4. Catégorielles Nominales (OHE)</h3>
    <ul>
      <li><b>Variables :</b> Allocataire, nationalité, département, famille ROME.</li>
      <li><b>Conversion en cases à cocher (0 ou 1) :</b> Chaque choix devient une option binaire indépendante, sans créer de doublon d'information ni bloquer si une nouvelle option apparaît.</li>
    </ul>
  </div>
</div>

<div class="tech-box" style="font-size: 12.5px; margin-top: 6px; padding: 5px 10px; line-height: 1.25;">
  <b>Architecture Scikit-Learn :</b> Toutes ces briques sont isolées dans un <code>ColumnTransformer</code> unifié, combiné au NLP (TF-IDF), garantissant <b>zéro fuite de données (Data Leakage)</b> entre Train et Test.
</div>

---

## La Sélection des Variables : Éthique & Biais (AI Act)

<style scoped>
section { font-size: 19px; padding-top: 75px; }
ul { margin: 6px 0 10px 0; }
li { margin-bottom: 3px; }
</style>

- **Biais historiques constatés (EDA) :**
  - **Âge :** 29% des seniors (45-65 ans) en risque long vs 9% des 25-45 ans.
  - **Nationalité hors UE :** 38% en risque long vs 15% pour les ressortissants UE.
- **Indicateur d'équité (Disparate Impact) :** Utilisation de la règle des 4/5 (issue de l'EEOC américaine) comme repère statistique empirique pour évaluer les disparités de traitement.
- **Transparence :** Rédaction d'une **Datasheet for Datasets** (*Gebru et al.*) dans `data/DATASHEET.md`.

<div class="tech-box" style="font-size: 16px; margin-top: 8px; padding: 8px 12px; line-height: 1.35;">
<b>Décision Stratégique (Privacy by Design — Scénario S2) :</b> Retrait de l'Âge et de la Nationalité pour forcer le modèle à chercher les causes objectives (freins textuels, secteur, parcours).<br>
<b>Constat lucide (Échec du <i>Fairness through Blindness</i>) :</b> Les variables proxy (département, diplôme) réintroduisent un biais résiduel. D'où l'impératif du filet humain (HITL).
</div>

---

## Analyse du Texte (NLP) : Problématique & Benchmark des Approches

<style scoped>
section { font-size: 17px; padding-top: 50px; padding-bottom: 45px; }
.top-box {
  background: #f0f4f8;
  border-left: 4px solid #1565c0;
  padding: 5px 12px;
  margin-bottom: 8px;
  font-size: 14px;
  line-height: 1.3;
  color: #0d47a1;
}
.nlp-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.8rem;
  margin-top: 4px;
}
.nlp-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 8px 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.nlp-card h3 {
  margin: 0 0 5px 0;
  font-size: 14px;
  padding-bottom: 3px;
  border-bottom: 1.5px solid #e0e0e0;
}
ul { margin: 0; padding-left: 16px; font-size: 12.8px; line-height: 1.3; }
li { margin-bottom: 3px; }
.badge {
  display: inline-block;
  padding: 2px 7px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: bold;
  margin-bottom: 4px;
}
</style>

<div class="top-box">
  <b>La Problématique Métier :</b> Le champ libre <code>synthese_entretien</code> est le <b>prédicteur n°1</b> du jeu de données (signaux faibles : <i>"freins périphériques", "perte de confiance", "autonome"</i>). Le défi : convertir ces verbatims hétérogènes en représentations exploitables en temps réel.
</div>

<div class="nlp-grid">
  <div class="nlp-card">
    <div>
      <span class="badge" style="background: #ffebee; color: #c62828;">❌ Écarté : Trop naïf</span>
      <h3 style="color: #c62828;">1. Bag of Words (Comptage brut)</h3>
      <ul>
        <li><b>Principe :</b> Simple comptage de la fréquence brute des mots.</li>
        <li><b>Limite majeure :</b> Les mots fréquents et vides ("le", "de", "usager") écrasent le signal utile.</li>
        <li><b>Impact :</b> Bruit statistique massif, faible discrimination des situations fragiles.</li>
      </ul>
    </div>
    <div style="font-size: 11.5px; color: #757575; border-top: 1px dashed #ccc; padding-top: 4px; margin-top: 4px;">
      <i>Inadapté aux textes courts et bruités.</i>
    </div>
  </div>

  <div class="nlp-card">
    <div>
      <span class="badge" style="background: #fff3e0; color: #e65100;">⚠️ Écarté : Surdimensionné</span>
      <h3 style="color: #e65100;">2. Deep Learning (CamemBERT / LLM)</h3>
      <ul>
        <li><b>Principe :</b> Plongements sémantiques contextuels denses (Transformers).</li>
        <li><b>Forces :</b> Analyse fine des nuances linguistiques et des négations.</li>
        <li><b>Obstacles :</b> "Boîte noire" difficilement explicable (AI Act), sur-apprentissage sur 2 500 textes courts, coût GPU prohibitif.</li>
      </ul>
    </div>
    <div style="font-size: 11.5px; color: #757575; border-top: 1px dashed #ccc; padding-top: 4px; margin-top: 4px;">
      <i>À réévaluer sur &gt; 500k textes avec GPU.</i>
    </div>
  </div>

  <div class="nlp-card" style="border: 2px solid #2e7d32; background: #f9fbe7;">
    <div>
      <span class="badge" style="background: #e8f5e9; color: #2e7d32;">✅ Retenu : Le Compromis Idéal</span>
      <h3 style="color: #1b5e20;">3. TF-IDF avec Stopwords</h3>
      <ul>
        <li><b>Principe :</b> Valorise les mots discriminants et pénalise les termes banals.</li>
        <li><b>Explicabilité totale (AI Act) :</b> Poids direct et traçable pour chaque mot-clé (ex: <i>"barrière", "santé"</i>).</li>
        <li><b>Sobriété (Green IT) :</b> Inférence ultra-rapide (&lt; 0.1 ms sur CPU simple), 0 surcoût infra.</li>
      </ul>
    </div>
    <div style="font-size: 11.5px; color: #1b5e20; border-top: 1px dashed #a5d6a7; padding-top: 4px; margin-top: 4px; font-weight: 500;">
      <i>Intégration directe dans le ColumnTransformer.</i>
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 12.5px; margin-top: 6px; padding: 5px 10px; line-height: 1.25;">
  <b>Bilan de l'arbitrage NLP :</b> Conformément au principe KISS et aux exigences de transparence publique, le TF-IDF surpasse les modèles complexes en garantissant auditabilité immédiate, sobriété énergétique et robustesse sur un petit corpus.
</div>

---

## Le Pipeline Scikit-Learn End-to-End (Anti-Data Leakage)

<style scoped>
section { font-size: 17px; padding-top: 52px; padding-bottom: 45px; }
.pipe-flow {
  display: flex;
  align-items: stretch;
  justify-content: space-between;
  gap: 0.5rem;
  margin: 10px 0 12px 0;
}
.pipe-step {
  flex: 1;
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 8px 10px;
  text-align: center;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.pipe-step h4 {
  margin: 0 0 4px 0;
  font-size: 13.5px;
  color: #1565c0;
}
.pipe-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: #1565c0;
  font-weight: bold;
}
.pillar-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 0.8rem;
}
.pillar-card {
  background: #f8fafc;
  border: 1.5px solid #d0d7de;
  border-radius: 6px;
  padding: 8px 10px;
  font-size: 12.8px;
  line-height: 1.35;
}
.pillar-card b {
  color: #0d47a1;
}
</style>

<div class="pipe-flow">
  <div class="pipe-step" style="border-left: 4px solid #546e7a;">
    <div>
      <h4>1. Données Brutes</h4>
      <div style="font-size: 11.5px; color: #455a64;">JSON usager direct</div>
    </div>
    <div style="font-size: 11px; background: #eceff1; padding: 3px 5px; border-radius: 4px; margin-top: 4px;">
      INSEE, ROME, Âge, Notes textuelles
    </div>
  </div>

  <div class="pipe-arrow">➔</div>

  <div class="pipe-step" style="border-left: 4px solid #1e88e5;">
    <div>
      <h4>2. Feature Eng.</h4>
      <div style="font-size: 11.5px; color: #1565c0;">FunctionTransformer</div>
    </div>
    <div style="font-size: 11px; background: #e3f2fd; padding: 3px 5px; border-radius: 4px; margin-top: 4px;">
      Département (95) + Famille ROME (14)
    </div>
  </div>

  <div class="pipe-arrow">➔</div>

  <div class="pipe-step" style="border-left: 4px solid #8e24aa;">
    <div>
      <h4>3. Prétraitement</h4>
      <div style="font-size: 11.5px; color: #6a1b9a;">ColumnTransformer</div>
    </div>
    <div style="font-size: 11px; background: #f3e5f5; padding: 3px 5px; border-radius: 4px; margin-top: 4px;">
      Scaler + Ordinal + OHE + TF-IDF
    </div>
  </div>

  <div class="pipe-arrow">➔</div>

  <div class="pipe-step" style="border-left: 4px solid #2e7d32; background: #f9fbe7;">
    <div>
      <h4>4. Modèle IA</h4>
      <div style="font-size: 11.5px; color: #2e7d32;">LightGBM Classifier</div>
    </div>
    <div style="font-size: 11px; background: #e8f5e9; padding: 3px 5px; border-radius: 4px; margin-top: 4px;">
      Probabilités [0, 1, 2] + Décision
    </div>
  </div>
</div>

<div class="pillar-grid">
  <div class="pillar-card">
    <b>🛡️ Zéro Fuite (Data Leakage) :</b><br>
    La chaîne est entraînée (<code>fit</code>) strictement sur le jeu d'entraînement après split stratifié. Les statistiques (médianes, échelles, IDF) ne voient jamais le jeu de test.
  </div>
  <div class="pillar-card">
    <b>📦 Artefact Unique (555 Ko) :</b><br>
    L'intégralité du traitement et de l'estimateur est sérialisée dans <code>pipeline_production.joblib</code>. Finis les scripts annexes de nettoyage en vrac.
  </div>
  <div class="pillar-card">
    <b>🚀 Prêt pour la Production :</b><br>
    L'API FastAPI reçoit la requête HTTP brute, l'injecte dans le pipeline en 1 ligne (<code>pipeline.predict_proba()</code>) et renvoie la prédiction en <b>&lt; 1 ms</b>.
  </div>
</div>

<div class="tech-box" style="font-size: 12.5px; margin-top: 8px; padding: 5px 10px; line-height: 1.25;">
  <b>Garantie logicielle :</b> En encapsulant feature engineering, imputations, encodages et inférence dans un seul objet standardisé, nous éliminons tout écart entre l'expérimentation en notebook et le service déployé en production.
</div>

---

# 3. Modélisation, Scénarios & Explicabilité

---

## Le Défi du Déséquilibre : La Réalité des Données

<style scoped>
section { font-size: 17.5px; padding-top: 52px; padding-bottom: 45px; }
.hero-box {
  background: #f0f4f8;
  border-left: 4px solid #1565c0;
  padding: 5px 12px;
  margin-bottom: 10px;
  font-size: 14px;
  line-height: 1.3;
  color: #0d47a1;
}
.imbalance-grid {
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 1.1rem;
  align-items: stretch;
}
.stat-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 8px 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.stat-card h3 {
  margin: 0 0 5px 0;
  font-size: 14px;
  color: #1565c0;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 3px;
}
.chart-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 8px 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}
</style>

<div class="hero-box">
  <b>Constat terrain :</b> Les situations de vulnérabilité extrême ne représentent qu'une minorité des usagers. L'enjeu data science est d'empêcher l'algorithme d'optimiser une performance de façade en ignorant les plus fragiles.
</div>

<div class="imbalance-grid">
  <div style="display: flex; flex-direction: column; justify-content: space-between; gap: 8px;">
    <div class="stat-card" style="border-left: 4px solid #c62828;">
      <h3 style="color: #c62828;">⚠️ Le Piège de l'Accuracy (81% de fausse réussite)</h3>
      <div style="font-size: 13px; line-height: 1.35; color: #263238;">
        Dans un jeu à 3 classes déséquilibré, un modèle paresseux qui prédirait <b>systématiquement un retour rapide ou moyen (0 ou 1)</b> afficherait un taux de bonne prédiction de <b>81%</b>... tout en abandonnant <b>100% des personnes en détresse</b> !
      </div>
    </div>
    <div class="stat-card" style="border-left: 4px solid #2e7d32;">
      <h3 style="color: #1b5e20;">🧭 Notre Boussole : Le F1-Score Macro</h3>
      <div style="font-size: 13px; line-height: 1.35; color: #263238;">
        Moyenne arithmétique non pondérée des scores F1 des 3 classes :
        <div style="text-align: center; margin: 3px 0; font-weight: bold; color: #0d47a1; font-size: 13px;">
          F1-Macro = (F1_0 + F1_1 + F1_2) / 3
        </div>
        Chaque classe pèse exactement <b>33.3%</b> dans la note finale : si l'IA sacrifie la classe minoritaire à risque (2), le score global s'effondre.
      </div>
    </div>
  </div>

  <div class="chart-card">
    <div style="width: 100%; font-size: 13px; font-weight: bold; color: #1565c0; text-align: left; margin-bottom: 2px;">
      📊 Répartition Réelle des Usagers (N = 2 500)
    </div>
    <img src="assets/imbalance_pie.png" alt="Déséquilibre" width="370" style="max-width: 100%; border-radius: 4px;"/>
    <div style="font-size: 12px; color: #546e7a; text-align: center; line-height: 1.25; margin-top: 2px;">
      La <b>Classe 2 (18.4%)</b> requiert un sur-échantillonnage de pénalité (<code>class_weight='balanced'</code>).
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 12.5px; margin-top: 7px; padding: 5px 10px; line-height: 1.25;">
  <b>Règle de conduite MLOps :</b> L'Accuracy globale est formellement bannie comme critère de sélection de nos modèles au profit exclusif du <b>F1-Score Macro</b> et du <b>Rappel sur la Classe 2</b>.
</div>

---

## Asymétrie des Coûts : Deux Leviers pour Réduire les Erreurs Critiques

<style scoped>
section { font-size: 19px; padding-top: 75px; }
.cost-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; margin-top: 8px; }
.cost-card { background: #ffffff; border: 2px solid #1565c0; border-radius: 8px; padding: 10px 12px; }
.cost-card h3 { margin: 0 0 6px 0; font-size: 17px; color: #0d47a1; }
ul { margin: 0; padding-left: 18px; }
li { margin-bottom: 4px; font-size: 14.5px; line-height: 1.35; }
</style>

Classer un profil en risque (2) en retour rapide (0) est bien plus grave qu'une fausse alerte. Deux leviers :

<div class="cost-grid">
  <div class="cost-card">
    <h3>1. En Amont : À l'Entraînement (Cost-Sensitive Learning)</h3>
    <ul>
      <li><b>Pondération automatique — <code>class_weight='balanced'</code> (Retenu) :</b><br>
        Chaque profil à risque pèse ~2,4× plus lourd, forçant l'algorithme à ne pas l'ignorer.</li>
      <li><b>Poids personnalisés — <i>Custom Sample Weights</i> :</b><br>
        Possibilité de sur-pénaliser davantage les erreurs sur les demandeurs vulnérables.</li>
    </ul>
  </div>
  <div class="cost-card" style="border-color: #2e7d32;">
    <h3 style="color: #1b5e20;">2. En Aval : À la Décision (Cost-Sensitive Thresholding)</h3>
    <ul>
      <li><b>Seuil d'alerte préventif abaissé — <i>Decision Threshold Tuning</i> :</b><br>
        Déclencher l'aide dès 25% de risque détecté, sans attendre une certitude absolue.</li>
      <li><b>Seuil d'abstention (65%) — <i>Rejection Threshold (HITL)</i> :</b><br>
        En cas de doute, l'IA passe la main au conseiller humain (<i>Human-in-the-Loop</i>).</li>
    </ul>
  </div>
</div>

<div class="tech-box" style="font-size: 15px; margin-top: 10px; padding: 6px 12px; line-height: 1.3;">
<b>Synthèse :</b> On combine une pondération à l'apprentissage et un filet d'alerte précoce à la décision pour protéger les usagers fragiles sans alourdir le modèle.
</div>

---

## Le Benchmark : Duel sous Validation Croisée Stratifiée
<style scoped> section { font-size: 21px; } </style>

- **Méthodologie :** 5-Fold Stratified Cross-Validation sur `X_train` avec traçabilité complète sous **MLflow**.
- **Comparatif des familles :**

| Modèle | F1-Macro CV (Moyenne) | Écart-type | Atouts | Limites |
| :--- | :---: | :---: | :--- | :--- |
| **Régression Logistique** | ~0.664 | 0.016 | Baseline rapide, poids linéaires directs | Moins apte aux interactions non-linéaires |
| **Random Forest** | ~0.660 | **0.012** | Très stable, robuste aux outliers | Forêt volumineuse en RAM, latence plus élevée |
| **LightGBM** | **~0.680** | 0.014 | **Meilleure performance**, gestion native matrices creuses | Risque fort de sur-apprentissage (overfitting) sur petit volume |

---

## Optimisation des Hyperparamètres (GridSearchCV + MLflow)

Duel final entre **Random Forest** et **LightGBM** avec régularisation ciblée pour contrer l'overfitting :

- **Hyperparamètres retenus (LightGBM sélectionné) :**
  - `n_estimators = 100` : Nombre d'arbres maîtrisé.
  - `learning_rate = 0.05` : Apprentissage doux pour une meilleure généralisation.
  - `num_leaves = 15` & `min_child_samples = 20` : Interdiction formelle de créer des branches pour un groupe d'usagers trop restreint.
  - `class_weight = 'balanced'` : Protection active de la classe minoritaire.

<div class="tech-box" style="font-size: 17px;">
<b>Gouvernance MLOps & Limite POC :</b> Paramètres optimisés sur S1 et conservés sur les 4 scénarios pour isoler l'effet des variables sans introduire de variance. En V2 industrielle, un <code>GridSearchCV</code> dédié spécifiquement à S2 sera reconduit.
</div>

---

## Analyse Comparée des 4 Scénarios 

<style scoped>
section { font-size: 19px; padding-top: 75px; }
table { font-size: 16px; margin-bottom: 8px; }
table th, table td { padding: 4px 10px; }
.tech-box { font-size: 16px; padding: 6px 12px; margin-top: 6px; }
</style>

| Scénario | Périmètre | F1-Macro | FN (Classe 2) | Disparate Impact | Conformité AI Act | Verdict |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **S1 (Complet)** | Tabulaire + Texte + Variables sensibles | **0.716** | **24** | 2.53 (Fort biais) | ❌ Non conforme | Rejeté prod |
| **S2 (Éthique)** | S1 **sans âge ni nationalité** | **0.627** | **33** | 1.41 (Proxy réduit) | ✅ Conforme (*PbD*) | 🏆 **Retenu prod** |
| **S3 (NLP seul)** | Synthèse entretien seule | 0.637 | 32 | 1.62 (Biais verbatims) | ⚠️ Trop fragile | Rejeté prod |
| **S4 (Tabulaire)** | Sans analyse textuelle | 0.614 | 39 | 2.40 (Biais âge/territoire)| ❌ Aveugle aux freins | Rejeté prod |

<div class="tech-box">
<b>L'arbitrage responsable :</b> Nous assumons le "coût de l'éthique" (9 erreurs supplémentaires entre S1 et S2) comme une <b>prime d'assurance réglementaire</b>, sécurisée par notre filet d'escalade humaine.
</div>

---

## Explicabilité Locale et Globale (SHAP sur S2)

<style scoped>
section { font-size: 19px; padding-top: 75px; }
.columns { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 1.2rem; align-items: center; }
ul { margin: 4px 0 8px 0; padding-left: 20px; }
li { margin-bottom: 4px; font-size: 14.5px; line-height: 1.35; }
</style>

<div class="columns">
  <div>
    <b>L'audit TreeExplainer valide l'hybridation :</b>
    <ul>
      <li><b>Explicabilité Globale (Population) :</b>
        <ul>
          <li><b>Ancienneté d'inscription :</b> Ancre administrative n°1 (forte ancienneté $\rightarrow$ pousse vers le risque long).</li>
          <li><b>Mots-clés NLP (TF-IDF) :</b> Les termes signalant des freins périphériques déclenchent l'alerte.</li>
          <li><b>Minimisation des données (Privacy by Design) :</b> Zéro variable démographique discriminatoire (âge, nationalité) dans les entrées du modèle.</li>
        </ul>
      </li>
      <li><b>Explicabilité Locale (UI Streamlit) :</b><br>
        Restitution unitaire au conseiller (force plot / waterfall) expliquant précisément chaque recommandation (RGPD Art. 22).</li>
    </ul>
    <div class="tech-box" style="font-size: 14px; margin-top: 6px; padding: 6px 10px; line-height: 1.3;">
      <b>Transparence totale (AI Act) :</b> Le modèle n'est plus une boîte noire : chaque prédiction est justifiable mot par mot.
    </div>
  </div>
  <div align="center">
    <img src="assets/shap.png" alt="Graphique SHAP" width="370" style="max-height: 480px; object-fit: contain; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.12);"/>
  </div>
</div>

---

# 4. Architecture Backend & Industrialisation

---

## De la Modélisation à la Production

Le passage de l'expérimentation vers un service industriel sécurisé :

1. **Sérialisation unifiée :** Export d'un artefact unique `pipeline_production.joblib` contenant la fonction d'extraction, les transformateurs et le LightGBM entraîné.
2. **Model Card Technique :** Fichier `pipeline_production.json` traçant les versions d'OS/Python, l'empreinte MD5 du dataset source (`2605ca...`), les hyperparamètres et la matrice de confusion.
3. **Suite de Tests Automatisée :** 6 tests unitaires et d'intégration validant le chargement du modèle, les formats d'inférence et le rejet des entrées invalides (Pytest).

---

## L'API FastAPI : Typage Strict & Validation Pydantic

<style scoped>
section { font-size: 18px; padding-top: 65px; }
.columns { display: grid; grid-template-columns: 1fr 1.05fr; gap: 1rem; align-items: start; margin-top: 4px; }
ul { margin: 0; padding-left: 18px; }
li { margin-bottom: 4px; font-size: 13.5px; line-height: 1.3; }
pre { margin: 0; font-size: 12px; line-height: 1.2; padding: 8px; }
</style>

<div class="columns">
<div>

<b>4 routes RESTful asynchrones :</b>

- `GET /health` : Diagnostic & disponibilité modèle.
- `POST /predict` : Inférence unitaire + probas + Fallback.
- `POST /predict/batch` : Traitement par lot pour le SI.
- `POST /train` : Réentraînement sécurisé (API Key).

<div class="tech-box" style="font-size: 13.5px; margin-top: 8px; padding: 6px 8px; line-height: 1.25;">
  <b>Robustesse :</b> Toute donnée non conforme (ex: ancienneté &lt; 0) est rejetée avec un code <code>422 Unprocessable Entity</code>.
</div>

</div>
<div>

```python
# Validation Pydantic automatique
class UsagerInput(BaseModel):
    anciennete_poste_ans: float = Field(..., ge=0, le=50)
    niveau_diplome: str
    code_insee_commune: str = Field(..., min_length=5, max_length=5)
    code_rome_vise: str = Field(..., min_length=5, max_length=5)
    est_allocataire: int = Field(..., ge=0, le=1)
    synthese_entretien: str = Field(default="")
```

</div>
</div>

---

## L'Interface Conseiller (Streamlit) & Intégration SI

<style scoped>
section { font-size: 17.5px; padding-top: 65px; }
h2 { margin-bottom: 6px; }
.si-flow { display: flex; justify-content: space-between; align-items: stretch; margin: 6px 0 10px 0; gap: 6px; }
.si-card { background: #ffffff; border: 1.5px solid #1565c0; border-radius: 6px; padding: 6px 8px; text-align: center; }
.si-arrow { display: flex; align-items: center; justify-content: center; font-size: 18px; color: #0d47a1; font-weight: bold; }
ul { margin: 0; padding-left: 20px; }
li { margin-bottom: 4px; font-size: 14px; line-height: 1.3; }
</style>

<div class="si-flow">
  <div class="si-card" style="flex: 1.1;">
    <b style="font-size: 13px; color: #0d47a1;">UI Streamlit</b><br>
    <span style="font-size: 10px; color: #555;">Jauge 65% + SHAP</span>
  </div>
  <div class="si-arrow">➔</div>
  <div class="si-card" style="flex: 1; border-color: #e65100; background: #fff3e0;">
    <b style="font-size: 13px; color: #bf360c;">Pipeline S2 (.joblib)</b><br>
    <span style="font-size: 10px; color: #333;">TF-IDF + LightGBM</span>
  </div>
  <div class="si-arrow">➔</div>
  <div class="si-card" style="flex: 1.2; border-color: #2e7d32; background: #f1f8e9;">
    <b style="font-size: 13px; color: #1b5e20;">API FastAPI (CPU)</b><br>
    <span style="font-size: 10px; color: #333;">Pydantic · Inférence &lt; 1ms</span>
  </div>
  <div class="si-arrow">➔</div>
  <div class="si-card" style="flex: 1;">
    <b style="font-size: 13px; color: #0d47a1;">Portail Guichet</b><br>
    <span style="font-size: 10px; color: #555;">Référentiel National (BDD)</span>
  </div>
</div>

<div class="columns" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 4px;">
  <div class="tech-box" style="font-size: 13.5px; margin: 0; padding: 8px 10px; line-height: 1.3;">
    <b>Hébergement Souverain (SecNumCloud) :</b><br>
    Cloud souverain (OVHcloud, Outscale) pour concilier élasticité, résilience et conformité aux données publiques de l'emploi (vs On-Premise rigide).
  </div>
  <div class="tech-box" style="font-size: 13.5px; margin: 0; padding: 8px 10px; line-height: 1.3; border-left-color: #2e7d32; background-color: #f1f8e9;">
    <b>IHM Conseiller Ergonomique :</b><br>
    Code couleur métier (Vert, Orange, Rouge), jauge de confiance et alerte d'escalade humaine immédiate si la confiance est &lt; 65%.
  </div>
</div>

---

## Démarche CI/CD & Déploiement Reproductible (GitHub Actions)

<style scoped> section { font-size: 21px; } </style>

Le projet intègre un cycle d'ingénierie logicielle continu automatisé sur GitHub Actions :

<div class="columns">
  <div>
    <b>Pipeline Automatisé sur <code>master</code> :</b>
    <ol style="font-size: 15px; margin-top: 6px;">
      <li><b>Contrôle Qualité & Linting :</b> Analyse statique du code Python via <code>flake8</code> / <code>black</code>.</li>
      <li><b>Tests Automatisés (Pytest) :</b>
        <ul style="font-size: 13px;">
          <li><code>test_api.py</code> : Santé, validation Pydantic (422), batch et réponses unitaires.</li>
          <li><code>test_pipeline.py</code> : Présence modèle, prédiction probas = 1.0 sur données brutes.</li>
        </ul>
      </li>
      <li><b>Construction Conteneur Docker :</b>
        <ul style="font-size: 13px;">
          <li>Multi-stage build Python 3.12-slim (&lt; 300 Mo).</li>
          <li>Sécurité : exécution non-root, sans cache de build.</li>
        </ul>
      </li>
      <li><b>Orchestration :</b> <code>docker-compose.yml</code> multiservices (FastAPI, Streamlit, Prometheus, Grafana).</li>
    </ol>
  </div>
  <div class="tech-box" style="font-size: 16px;">
    <b>Garanties pour le Jury :</b><br>
    ✅ <b>100% Reproductible :</b> Un clone + <code>docker compose up</code> suffit pour monter le SI complet.<br>
    ✅ <b>Zéro Régression :</b> La CI bloque toute mise en production si un test ou un schéma échoue.<br>
    ✅ <b>Conformité MLOps :</b> Cycle de vie tracé du code au conteneur.
  </div>
</div>

---

# 5. Supervision MLOps & Amélioration Continue

---

## Le Monitoring en Temps Réel (Prometheus & Grafana)

<style scoped>
section { font-size: 19px; padding-top: 75px; }
ul { margin: 4px 0; }
li { margin-bottom: 4px; font-size: 15px; }
</style>

<div class="columns">
  <div style="font-size: 18px;">
    Architecture conteneurisée via <b>Docker-Compose</b> intégrant nativement la métrologie :
    <br><br>
    <ul>
      <li><b>Métriques Système :</b> Latence p95 (&lt; 100 ms) et taux d'erreurs HTTP.</li>
      <li><b>Métriques Métier :</b>
        <ul>
          <li>Volume de prédictions par classe (détection d'anomalies de répartition).</li>
          <li>Histogramme des scores de certitude.</li>
          <li><b>Taux d'escalade (Fallback rate)</b>.</li>
        </ul>
      </li>
      <li><b>Alerting MLOps :</b> Dérive relative &gt; 20% du taux d'abstention sur 4 semaines.</li>
    </ul>
  </div>
  <div align="center">
    <img src="assets/architecture_mlops.png" alt="Architecture MLOps" width="360"/>
  </div>
</div>

---

## Le Fallback : Seuil de Rejet (65%) & Biais d'Automatisation

<style scoped>
section { font-size: 20px; padding-top: 70px; }
.columns { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; align-items: start; margin-top: 8px; }
ul { margin: 0; padding-left: 18px; }
li { margin-bottom: 5px; font-size: 14.5px; line-height: 1.35; }
</style>

- **Le Risque UX :** Face à un flux tendu, un conseiller peut subir le *biais d'automatisation* (suivre aveuglément l'avis de la machine).

<div class="columns">
  <div>
    <b style="font-size: 16px; color: #0d47a1;">Pourquoi fixer le seuil à 65% ? (Calibration)</b>
    <ul>
      <li><b>Seuil de coupure opérationnel :</b> Les scores <code>predict_proba</code> d'un modèle d'arbres ne sont pas des probabilités calibrées pures (Brier Score = 0.48). Le seuil agit comme filtre de sécurité.</li>
      <li><b>Efficacité empirique mesurée :</b><br>
        • Score &ge; 65% : <b>76% d'exactitude</b> (automatisation sûre).<br>
        • Score &lt; 65% : <b>46% d'exactitude</b> (l'IA doute &rarr; escalade).</li>
      <li><b>Perspective V2 :</b> Calibration formelle via <code>CalibratedClassifierCV</code> pour aligner scores et probabilités.</li>
    </ul>
  </div>
  <div>
    <div style="background: #ffffff; border: 2px solid #1565c0; border-radius: 8px; padding: 12px; box-shadow: 2px 2px 8px rgba(0,0,0,0.06);">
      <b style="font-size: 15px; color: #0d47a1; display: block; margin-bottom: 8px;">Logique du Filet de Sécurité (API)</b>
      <div style="background: #f1f8e9; border-left: 4px solid #2e7d32; padding: 6px 10px; margin-bottom: 8px; border-radius: 4px;">
        <span style="font-weight: bold; color: #1b5e20; font-size: 13.5px;">🟢 Confiance &ge; 65% : Feu Vert</span><br>
        <span style="font-size: 13px; color: #333;">L'IA affiche la recommandation d'orientation au conseiller.</span>
      </div>
      <div style="background: #fff3e0; border-left: 4px solid #e65100; padding: 6px 10px; border-radius: 4px;">
        <span style="font-weight: bold; color: #bf360c; font-size: 13.5px;">🟡 Confiance &lt; 65% : Abstention (Fallback)</span><br>
        <span style="font-size: 13px; color: #333;">L'API renvoie <code>fallback: true</code>. L'IHM invite le conseiller à décider en autonomie (<i>Human-In-The-Loop</i>).</span>
      </div>
    </div>
  </div>
</div>

---

## Alerte Dérive (&gt; 20%) : Le Signal d'Alarme Précoce

<style scoped>
section { font-size: 20px; padding-top: 70px; }
.columns { display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 1.2rem; align-items: start; margin-top: 8px; }
ul { margin: 0; padding-left: 18px; }
li { margin-bottom: 5px; font-size: 14.5px; line-height: 1.35; }
</style>

La vérité terrain (retour à l'emploi effectif) n'est connue que 6 à 12 mois plus tard. **Comment détecter une panne du modèle dès aujourd'hui ?**

<div class="columns">
  <div>
    <b style="font-size: 16px; color: #0d47a1;">Pourquoi une alerte sur une hausse relative de &gt; 20% ?</b>
    <ul>
      <li><b>Taux nominal baseline :</b> ~38-40% des dossiers sont sous 65%.</li>
      <li><b>Filtrage du bruit statistique :</b> Une variation de ±10% est une fluctuation normale (saisonnalité, congés).</li>
      <li><b>Seuil critique (+20% relatif) :</b> Si le taux de rejet dépasse <b>48% sur 4 semaines glissantes</b>, c'est une dérive structurelle :
        • <i>Data Drift sémantique :</i> vocabulaire des conseillers qui a changé.<br>
        • <i>Choc économique :</i> afflux de profils inédits post-crise sectorielle.
      </li>
    </ul>
  </div>
  <div>
    <div class="tech-box" style="font-size: 14px; margin: 0; padding: 10px 12px; line-height: 1.35; border-left-color: #e65100; background-color: #fff3e0;">
      <b>Plan d'Action MLOps (Playbook) :</b><br>
      1. <b>Contrôle PSI :</b> Vérifier quelles variables d'entrée ont dérivé.<br>
      2. <b>Recalibration :</b> Ajuster les probabilités (Platt/Isotonique) sans réentraîner si seule la confiance s'est tassée.<br>
      3. <b>Réentraînement déclenché :</b> Appel de l'endpoint <code>POST /train</code> si le drift persiste.
    </div>
  </div>
</div>

---

## Cycle de Vie : Boucle de Rétroaction & Dérive (Drift)

<style scoped>
section { font-size: 21px; padding-top: 70px; }
ul { margin: 6px 0 10px 0; padding-left: 24px; }
li { margin-bottom: 8px; font-size: 18px; line-height: 1.4; }
</style>

- **Le Piège de la Prophétie Auto-Réalisatrice :**  
  L'IA classe un usager en *Risque long* $\rightarrow$ L'agence lui offre un suivi renforcé $\rightarrow$ Il retrouve un emploi en 4 mois.  
  *Le piège lors du réentraînement :* Le modèle conclut à tort qu'il s'agissait d'un profil "rapide" et le privera d'aide la fois suivante !
- **Solution par conception :** Enregistrement obligatoire de la variable `a_beneficie_aide_renforcee` pour neutraliser ce biais.

<div align="center" style="margin: 14px 0;">
  <img src="assets/feedback_loop.png" alt="Boucle de Rétroaction" width="1050" style="max-width: 100%; border-radius: 6px; box-shadow: 0 3px 10px rgba(0,0,0,0.12);"/>
</div>

- **Surveillance du Data Drift :** Calcul mensuel du **PSI (Population Stability Index)** sur les données entrantes. Si $PSI > 0.20$ sur les variables clés (métier, vocabulaire), déclenchement d'un réentraînement supervisé.

---

# 6. Bilan Économique, Perspectives & Conclusion

---

## Comparatif Économique & ROI (FinOps & Métier)

1. **Coût d'Inférence & Empreinte Numérique (FinOps) :**
   - LightGBM + TF-IDF : Consommation RAM &lt; 200 Mo, latence &lt; 1 ms sur simple CPU.
   - Économie de 80% par rapport à un cluster GPU dédié à des LLMs ou Transformers.

2. **L'Économie de l'Erreur :**
   - **Faux Positif (Alarme inutile) :** Coût modéré = un entretien approfondi de 30 min (~25€ de temps conseiller).
   - **Faux Négatif (Risque raté) :** Coût sociétal majeur = 12 à 24 mois d'indemnisation chômage, perte de cotisations et rupture sociale (> 15 000€).
   - *Le modèle maximise le ROI social en tolérant des fausses alarmes pour éradiquer les abandons.*

---

## Perspectives de Passage à l'Échelle (Scale-up)

| Axe | Échelle MVP (2 500 profils) | Échelle Nationale (1 000 000 profils) |
| :--- | :--- | :--- |
| **Données Géographiques** | Agrégation par département (anti-overfitting) | Exploitation du code commune INSEE brut (bassins d'emploi fins) |
| **Analyse NLP** | TF-IDF avec Stop Words (léger, explicable) | Modèles d'embeddings CamemBERT fine-tunés avec surcouche LIME/SHAP |
| **Pipeline MLOps** | SQLite MLflow local | Feature Store centralisé (Feast), Registry MLflow distant & Model Monitoring en continu |

---

## Conclusion

✅ **Système de bout en bout opérationnel :** Du cadrage métier et audit des données jusqu'à l'API FastAPI, l'UI Streamlit, Docker et la CI/CD GitHub Actions.  
✅ **Conformité stricte AI Act :** Modèle S2 éthique, explicabilité SHAP prouvée, politique d'abstention sous 65% et supervision humaine garantie.  
✅ **Pragmatisme d'ingénierie :** Solution sobre (Green IT), réactive (&lt; 1 ms) et alignée sur la réalité du service public de l'emploi.

---

<!-- _class: lead -->
# Merci de votre attention.
