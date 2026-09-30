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
<style scoped>
section {
  text-align: center;
  padding-top: 100px;
}
.hero-title {
  color: #0d47a1;
  font-size: 42px;
  margin-bottom: 8px;
  font-weight: 800;
}
.hero-sub {
  color: #1565c0;
  font-size: 26px;
  margin-bottom: 24px;
  font-weight: 600;
}
.hero-author {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  border-radius: 8px;
  display: inline-block;
  padding: 12px 28px;
  margin-bottom: 20px;
  text-align: left;
}
.stack-bar {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 8px;
}
.stack-tag {
  background: #e3f2fd;
  color: #0d47a1;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 15px;
  border: 1px solid #bbdefb;
}
</style>

<div class="hero-title">Projet de Certification IA</div>
<div class="hero-sub">Système d'Orientation et de Prévention du Chômage Longue Durée</div>

<div class="hero-author">
  <div style="font-size: 20px; color: #0d47a1; font-weight: bold; margin-bottom: 4px;">
    🧑‍💻 Franck Beugnet — Promo ATOS Atlas IA (Parcours 2 : Pros IT)
  </div>
  <div style="font-size: 16px; color: #455a64;">
    Conception, industrialisation et audit d'un produit Data de bout en bout
  </div>
</div>

<div class="stack-bar">
  <span class="stack-tag">Python 3.12</span>
  <span class="stack-tag">Scikit-Learn</span>
  <span class="stack-tag">LightGBM</span>
  <span class="stack-tag">FastAPI</span>
  <span class="stack-tag">Streamlit</span>
  <span class="stack-tag">MLflow</span>
  <span class="stack-tag">Prometheus</span>
  <span class="stack-tag">Docker</span>
</div>

---

# Plan de la Soutenance (30 minutes cadencées)

<style scoped>
section { font-size: 19px; padding-top: 55px; padding-bottom: 40px; }
.plan-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.1rem;
  margin-top: 14px;
}
.plan-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-left: 5px solid #1565c0;
  border-radius: 8px;
  padding: 10px 14px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.plan-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}
.plan-num {
  font-size: 16px;
  font-weight: bold;
  color: #0d47a1;
}
.plan-badge {
  background: #e3f2fd;
  color: #0d47a1;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 13px;
}
.plan-title {
  font-size: 16.5px;
  font-weight: 700;
  color: #263238;
}
.plan-desc {
  font-size: 13.5px;
  color: #607d8b;
  margin-top: 2px;
}
</style>

<div class="plan-grid">
  <div class="plan-card">
    <div class="plan-header">
      <span class="plan-num">Partie 1</span>
      <span class="plan-badge">⏱️ 5 min (00:00 - 05:00)</span>
    </div>
    <div class="plan-title">Cadrage Métier, Éthique & Objectifs</div>
    <div class="plan-desc">Enjeux du guichet, cible à 3 classes, doctrine No Mercy & conformité AI Act.</div>
  </div>

  <div class="plan-card" style="border-left-color: #0288d1;">
    <div class="plan-header">
      <span class="plan-num" style="color: #0288d1;">Partie 2</span>
      <span class="plan-badge">⏱️ 5 min (05:00 - 10:00)</span>
    </div>
    <div class="plan-title">Audit, Qualité & Pipeline End-to-End</div>
    <div class="plan-desc">Prétraitements, arbitage NLP TF-IDF vs Deep Learning, étanchéité Scikit-Learn.</div>
  </div>

  <div class="plan-card" style="border-left-color: #2e7d32;">
    <div class="plan-header">
      <span class="plan-num" style="color: #2e7d32;">Partie 3</span>
      <span class="plan-badge">⏱️ 7 min (10:00 - 17:00)</span>
    </div>
    <div class="plan-title">Modélisation, 4 Scénarios & SHAP</div>
    <div class="plan-desc">Benchmark CV, GridSearchCV, audit d'équité S1 à S4, explicabilité locale/globale.</div>
  </div>

  <div class="plan-card" style="border-left-color: #e65100;">
    <div class="plan-header">
      <span class="plan-num" style="color: #e65100;">Partie 4</span>
      <span class="plan-badge">⏱️ 5 min (17:00 - 22:00)</span>
    </div>
    <div class="plan-title">Architecture Cible, Flux SI & API</div>
    <div class="plan-desc">Flux guichet unique, contrat FastAPI, dimensionnement infra & souveraineté.</div>
  </div>

  <div class="plan-card" style="border-left-color: #7b1fa2;">
    <div class="plan-header">
      <span class="plan-num" style="color: #7b1fa2;">Partie 5</span>
      <span class="plan-badge">⏱️ 5 min (22:00 - 27:00)</span>
    </div>
    <div class="plan-title">Supervision MLOps & Dérive (Drift)</div>
    <div class="plan-desc">Métrologie Prometheus/Grafana, seuil de repli (65%), alerte précoce (+20%) & audit PSI.</div>
  </div>

  <div class="plan-card" style="border-left-color: #c2185b;">
    <div class="plan-header">
      <span class="plan-num" style="color: #c2185b;">Partie 6</span>
      <span class="plan-badge">⏱️ 3 min (27:00 - 30:00)</span>
    </div>
    <div class="plan-title">Bilan Économique & Démonstration</div>
    <div class="plan-desc">ROI financier et sociétal, démo interactive Streamlit & perspectives V2.</div>
  </div>
</div>

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

<style scoped>
section { font-size: 19px; padding-top: 48px; padding-bottom: 40px; }
.legal-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 8px 16px;
  margin-bottom: 12px;
  font-size: 16px;
  line-height: 1.35;
  color: #0d47a1;
}
.legal-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}
.legal-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 12px 14px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.legal-card h4 {
  margin: 0 0 6px 0;
  font-size: 16.5px;
  color: #1565c0;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 4px;
}
.legal-card ul {
  margin: 0;
  padding-left: 17px;
  font-size: 14.5px;
  line-height: 1.38;
}
.legal-card li {
  margin-bottom: 5px;
}
</style>

<div class="legal-box">
  <b>Exigences réglementaires :</b> L'utilisation d'algorithmes prédictifs dans les politiques publiques de l'emploi impose une conformité stricte et vérifiable sur trois piliers juridiques complémentaires.
</div>

<div class="legal-grid">
  <div class="legal-card" style="border-top: 5px solid #c62828;">
    <div>
      <h4 style="color: #c62828;">1. AI Act Européen</h4>
      <div style="font-size: 13.5px; font-weight: bold; color: #b71c1c; margin-bottom: 6px;">
        Classification Haut Risque (Annexe III)
      </div>
      <ul>
        <li><b>Champ d'application :</b> Systèmes d'IA utilisés dans l'emploi, le recrutement et l'orientation.</li>
        <li><b>Exigences :</b> Traçabilité des données d'entraînement, audit des biais, explicabilité formelle.</li>
        <li><b>Obligation clé :</b> <b>Supervision humaine continue</b> (<i>Human-In-The-Loop</i>). Aucune décision automatique sans contrôle.</li>
      </ul>
    </div>
    <div style="font-size: 12.5px; color: #b71c1c; background: #ffebee; padding: 5px 8px; border-radius: 5px; margin-top: 8px; font-weight: 500;">
      Sanction : jusqu'à 35 M€ ou 7% du CA.
    </div>
  </div>

  <div class="legal-card" style="border-top: 5px solid #1565c0;">
    <div>
      <h4>2. RGPD & Rép. Numérique</h4>
      <div style="font-size: 13.5px; font-weight: bold; color: #0d47a1; margin-bottom: 6px;">
        Transparence & Données Sensibles
      </div>
      <ul>
        <li><b>Loi République Numérique :</b> Droit pour l'usager à l'explicabilité individuelle des motifs.</li>
        <li><b>Précision juridique :</b> Âge et nationalité sont des <i>données ordinaires</i> (Art. 4) mais des critères protégés majeurs.</li>
        <li><b>Texte libre surveillé (Art. 9) :</b> Empêcher la captation de données de santé ou handicap.</li>
      </ul>
    </div>
    <div style="font-size: 12.5px; color: #0d47a1; background: #e3f2fd; padding: 5px 8px; border-radius: 5px; margin-top: 8px; font-weight: 500;">
      Principe : <i>Privacy by Design</i> (S2).
    </div>
  </div>

  <div class="legal-card" style="border-top: 5px solid #2e7d32;">
    <div>
      <h4 style="color: #1b5e20;">3. Responsabilité & Perte de Chance</h4>
      <div style="font-size: 13.5px; font-weight: bold; color: #1b5e20; margin-bottom: 6px;">
        Contentieux Administratif
      </div>
      <ul>
        <li><b>Préjudice de l'usager :</b> Un profil vulnérable classé par erreur en "retour rapide" perd ses aides.</li>
        <li><b>Responsabilité publique :</b> Devant le juge administratif, cette <b>perte de chance</b> engage l'État.</li>
        <li><b>Protection par conception :</b> IA qualifiée d'<b>aide consultative</b>. Le conseiller valide souverainement.</li>
      </ul>
    </div>
    <div style="font-size: 12.5px; color: #1b5e20; background: #e8f5e9; padding: 5px 8px; border-radius: 5px; margin-top: 8px; font-weight: 500;">
      Garantie : Validation humaine systématique.
    </div>
  </div>
</div>

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
section { font-size: 17px; padding-top: 50px; padding-bottom: 40px; }
.top-box {
  background: #f0f4f8;
  border-left: 4px solid #1565c0;
  padding: 5px 12px;
  margin-bottom: 10px;
  font-size: 14px;
  line-height: 1.3;
  color: #0d47a1;
}
.bias-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 8px;
}
.bias-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 10px 12px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.bias-card h4 {
  margin: 0 0 6px 0;
  font-size: 14.5px;
  color: #1565c0;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 3px;
}
.bias-card ul {
  margin: 0;
  padding-left: 17px;
  font-size: 13.5px;
  line-height: 1.35;
}
.bias-card li {
  margin-bottom: 4px;
}
</style>

<div class="top-box">
  <b>Audit d'Équité & Transparence (AI Act) :</b> L'analyse exploratoire a mis en lumière des disparités structurelles fortes dans les données historiques qu'il est impératif d'auditer et de corriger par conception.
</div>

<div class="bias-grid">
  <div class="bias-card" style="border-left: 4px solid #c62828;">
    <div>
      <h4 style="color: #c62828;">📊 Biais Historiques Constatés (EDA)</h4>
      <ul>
        <li><b>Âgisme statistique :</b> <b>29% des seniors (45-65 ans)</b> sont en risque long (Classe 2) contre seulement <b>9%</b> des 25-45 ans.</li>
        <li><b>Origine géographique :</b> <b>38% des usagers hors UE</b> sont en risque long contre <b>15%</b> pour les ressortissants de l'Union Européenne.</li>
        <li><b>Indicateur d'équité (Disparate Impact) :</b> Utilisation empirique de la règle des 4/5 de l'EEOC comme signal d'alarme opérationnel face aux déséquilibres.</li>
      </ul>
    </div>
    <div style="font-size: 12px; background: #ffebee; color: #b71c1c; padding: 4px 8px; border-radius: 4px; margin-top: 6px;">
      Danger : Un modèle naïf apprendrait à discriminer directement sur l'état civil.
    </div>
  </div>

  <div class="bias-card" style="border-left: 4px solid #1565c0;">
    <div>
      <h4>📋 Gouvernance & Traçabilité des Données</h4>
      <ul>
        <li><b>Datasheet for Datasets (Gebru et al.) :</b> Rédaction d'une fiche d'identité complète du jeu de données dans <code>data/DATASHEET.md</code>.</li>
        <li><b>Objectifs documentés :</b> Motivation de la collecte, composition de l'échantillon, prétraitements appliqués et usages recommandés/interdits.</li>
        <li><b>Conformité AI Act :</b> Traçabilité vérifiable exigée pour tout système classé à Haut Risque.</li>
      </ul>
    </div>
    <div style="font-size: 12px; background: #e3f2fd; color: #0d47a1; padding: 4px 8px; border-radius: 4px; margin-top: 6px;">
      Garantie : Auditabilité complète du cycle de vie de la donnée.
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 13px; margin-top: 6px; padding: 6px 12px; line-height: 1.35;">
  <b>Décision Stratégique (Privacy by Design — Scénario S2) :</b> Retrait formel de l'Âge et de la Nationalité pour contraindre l'IA à se baser sur les causes objectives (freins textuels, compétences, secteur ROME).<br>
  <b>Constat lucide (Échec du <i>Fairness through Blindness</i>) :</b> Les corrélations indirectes (territoire, diplôme) réinjectent un biais résiduel, justifiant le rôle central du conseiller humain.
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

<style scoped>
section { font-size: 16.5px; padding-top: 50px; padding-bottom: 42px; }
.top-box {
  background: #f0f4f8;
  border-left: 4px solid #1565c0;
  padding: 5px 12px;
  margin-bottom: 8px;
  font-size: 13.8px;
  line-height: 1.3;
  color: #0d47a1;
}
.bench-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 13px;
  border: 1.5px solid #d0d7de;
  border-radius: 6px;
  overflow: hidden;
  margin-bottom: 8px;
}
.bench-table th {
  background: #1565c0;
  color: #ffffff;
  padding: 6px 8px;
  font-weight: 600;
  text-align: left;
}
.bench-table td {
  padding: 6px 8px;
  border-top: 1px solid #e0e0e0;
  vertical-align: middle;
}
.badge-bench {
  display: inline-block;
  font-size: 10.5px;
  font-weight: bold;
  padding: 1px 6px;
  border-radius: 3px;
  margin-left: 4px;
}
.duel-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.8rem;
}
.duel-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 7px 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  font-size: 12.8px;
  line-height: 1.3;
}
.duel-card h4 {
  margin: 0 0 4px 0;
  font-size: 13.5px;
}
</style>

<div class="top-box">
  <b>Méthodologie d'évaluation rigoureuse :</b> 5-Fold Stratified Cross-Validation sur <code>X_train</code> pour préserver strictement la proportion des 3 classes (18% de risque critique). Traçabilité intégrale sous <b>MLflow</b> (paramètres, métriques de chaque pli et courbes).
</div>

<table class="bench-table">
  <thead>
    <tr>
      <th style="width: 24%;">Modèle & Famille</th>
      <th style="width: 15%; text-align: center;">F1-Macro CV</th>
      <th style="width: 15%; text-align: center;">Dispersion ($\sigma$)</th>
      <th style="width: 25%;">Atouts Opérationnels</th>
      <th style="width: 21%;">Limites & Risques</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #f9fbe7;">
      <td>
        <b>LightGBM</b><br>
        <span style="font-size: 11px; color: #555;">Gradient Boosting</span>
        <span class="badge-bench" style="background: #c8e6c9; color: #1b5e20;">🏆 Top F1</span>
      </td>
      <td style="text-align: center; font-weight: bold; color: #1b5e20; font-size: 14px;">~0.680</td>
      <td style="text-align: center; color: #37474f;">0.014</td>
      <td>Capacité prédictive maximale, gestion native et rapide des matrices creuses TF-IDF</td>
      <td>Risque élevé d'overfitting sur 2 500 profils (nécessite régularisation)</td>
    </tr>
    <tr style="background: #ffffff;">
      <td>
        <b>Random Forest</b><br>
        <span style="font-size: 11px; color: #555;">Bagging d'arbres</span>
        <span class="badge-bench" style="background: #e3f2fd; color: #0d47a1;">🛡️ Top Stabilité</span>
      </td>
      <td style="text-align: center; font-weight: bold; color: #0d47a1; font-size: 14px;">~0.660</td>
      <td style="text-align: center; font-weight: bold; color: #0d47a1;">0.012</td>
      <td>Excellente robustesse aux outliers, décision collective lisse et reproductible</td>
      <td>Artefact lourd en mémoire RAM (&gt; 50 Mo), latence d'inférence plus élevée</td>
    </tr>
    <tr style="background: #fafafa;">
      <td>
        <b>Régression Logistique</b><br>
        <span style="font-size: 11px; color: #555;">Linéaire régularisée</span>
        <span class="badge-bench" style="background: #eeeeee; color: #616161;">⚖️ Baseline</span>
      </td>
      <td style="text-align: center; color: #424242; font-size: 13.5px;">~0.664</td>
      <td style="text-align: center; color: #757575;">0.016</td>
      <td>Baseline ultra-rapide, explicabilité directe via les coefficients linéaires</td>
      <td>Rigide : incapable de capturer les interactions croisées complexes (texte × profil)</td>
    </tr>
  </tbody>
</table>

<div class="duel-grid">
  <div class="duel-card" style="border-left: 3px solid #f57c00;">
    <h4 style="color: #e65100;">🔬 Enseignement du Benchmark</h4>
    Le texte apporte un gain sensible de séparabilité que les arbres de décision exploitent mieux que les modèles linéaires. La Régression Logistique plafonne et est écartée pour l'inférence cible.
  </div>
  <div class="duel-card" style="border-left: 3px solid #2e7d32;">
    <h4 style="color: #1b5e20;">🎯 Qualification pour le Duel Final (GridSearchCV)</h4>
    Ne pas éliminer sur paramètres par défaut : qualification conjointe de <b>LightGBM</b> (puissance) et <b>Random Forest</b> (stabilité) pour un réglage fin anti-overfitting monitoré sous MLflow.
  </div>
</div>

---

## Optimisation des Hyperparamètres (GridSearchCV + MLflow)

<style scoped>
section { font-size: 16.5px; padding-top: 50px; padding-bottom: 42px; }
.top-box {
  background: #f0f4f8;
  border-left: 4px solid #1565c0;
  padding: 5px 12px;
  margin-bottom: 8px;
  font-size: 13.8px;
  line-height: 1.3;
  color: #0d47a1;
}
.duel-summary {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 1rem;
  margin-bottom: 8px;
}
.param-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 8px 10px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.param-card h4 {
  margin: 0 0 5px 0;
  font-size: 14px;
  color: #1565c0;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 3px;
}
.param-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12.5px;
}
.param-table td {
  padding: 3px 4px;
  border-bottom: 1px solid #f0f0f0;
}
.param-table code {
  font-weight: bold;
  color: #0d47a1;
}
.mlflow-box {
  background: #ffffff;
  border: 1.5px solid #2e7d32;
  border-radius: 6px;
  padding: 8px 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.mlflow-box h4 {
  margin: 0 0 4px 0;
  font-size: 14px;
  color: #1b5e20;
}
</style>

<div class="top-box">
  <b>Duel Final sous MLflow :</b> Exploration systématique par <code>GridSearchCV</code> (5-Fold CV) pour brider le sur-apprentissage induit par les 1 000 features textuelles du TF-IDF sur un petit échantillon (2 500 profils).
</div>

<div class="duel-summary">
  <div class="param-card">
    <h4>🏆 Réglages Retenus — LightGBM (Vainqueur du Duel)</h4>
    <table class="param-table">
      <tr>
        <td style="width: 42%;"><code>n_estimators = 100</code></td>
        <td>Nombre d'arbres maîtrisé pour fixer les règles générales sans bruit.</td>
      </tr>
      <tr>
        <td><code>learning_rate = 0.05</code></td>
        <td>Vitesse douce (vs 0.1 par défaut) forçant une correction prudente.</td>
      </tr>
      <tr>
        <td><code>num_leaves = 15</code></td>
        <td>Limite le nombre de feuilles (au lieu de 31) pour contrer la dimensionnalité.</td>
      </tr>
      <tr>
        <td><code>min_child_samples = 20</code></td>
        <td><b>Anti-par cœur :</b> interdit toute règle s'appliquant à moins de 20 usagers.</td>
      </tr>
      <tr>
        <td><code>class_weight = 'balanced'</code></td>
        <td>Sur-pénalise les erreurs sur la classe 2 (poids $\times 2.4$) contre le déséquilibre.</td>
      </tr>
    </table>
  </div>

  <div class="mlflow-box">
    <div>
      <h4>📊 Arbitrage Automatisé MLflow</h4>
      <div style="font-size: 12.8px; line-height: 1.35; color: #263238;">
        • <b>LightGBM :</b> F1-Macro CV optimisé à <b>~0.70</b> avec une inférence &lt; 0.5 ms.<br>
        • <b>Random Forest :</b> F1-Macro CV à ~0.67, éliminé pour lourdeur mémoire et moindre captation des signaux TF-IDF.<br>
        • <b>Traçabilité :</b> Artefacts, hyperparamètres et signatures sérialisés sous <code>mlflow.sklearn</code>.
      </div>
    </div>
    <div style="margin-top: 6px; padding: 4px 8px; background: #e8f5e9; border-radius: 4px; font-size: 11.5px; color: #1b5e20; font-weight: 500;">
      ✅ Sélectionné comme moteur de prédiction pour les 4 scénarios d'audit.
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 12.5px; margin-top: 4px; padding: 5px 10px; line-height: 1.25;">
  <b>Gouvernance MLOps & Limite assumée (POC) :</b> Hyperparamètres calés sur le jeu complet pour comparer équitablement les scénarios sans biaiser par le tuning. En V2 industrielle, un <code>GridSearchCV</code> dédié au scénario S2 sera exécuté avant mise en production.
</div>

---

## Analyse Comparée des 4 Scénarios 

<style scoped>
section { font-size: 19px; padding-top: 50px; padding-bottom: 45px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 8px 16px;
  margin-bottom: 12px;
  font-size: 16.5px;
  line-height: 1.35;
  color: #0d47a1;
}
.scen-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 16.5px;
  border: 2px solid #cfd8dc;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 14px;
}
.scen-table th {
  background: #1565c0;
  color: #ffffff;
  padding: 10px 12px;
  font-weight: 600;
  text-align: left;
  font-size: 16.5px;
}
.scen-table td {
  padding: 10px 12px;
  border-top: 1px solid #e0e0e0;
  vertical-align: middle;
}
.verdict-tag {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 5px;
  font-size: 14.5px;
  font-weight: bold;
}
.insight-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.1rem;
}
.insight-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 10px 14px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  font-size: 15.5px;
  line-height: 1.4;
}
.insight-card h4 {
  margin: 0 0 6px 0;
  font-size: 16.5px;
}
</style>

<div class="top-box">
  <b>Audit d'impact des modalités de données :</b> Évaluation sur le jeu de test ($N = 500$) de l'impact des données sensibles (RGPD) et de l'apport respectif du texte et des données administratives.
</div>

<table class="scen-table">
  <thead>
    <tr>
      <th style="width: 17%;">Scénario</th>
      <th style="width: 27%;">Périmètre des Features</th>
      <th style="width: 11%; text-align: center;">F1-Macro</th>
      <th style="width: 12%; text-align: center;">Erreurs FN (C2)</th>
      <th style="width: 15%; text-align: center;">Disparate Impact</th>
      <th style="width: 18%; text-align: center;">Arbitrage</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #fafafa;">
      <td><b>S1 (Complet)</b></td>
      <td>Tabulaire + Texte + Âge + Nationalité</td>
      <td style="text-align: center; font-weight: bold; color: #455a64; font-size: 17.5px;">0.716</td>
      <td style="text-align: center; font-weight: bold; color: #1b5e20; font-size: 17.5px;">24</td>
      <td style="text-align: center; color: #c62828; font-weight: 600;">2.53 (Biais fort)</td>
      <td style="text-align: center;"><span class="verdict-tag" style="background: #ffebee; color: #c62828;">❌ Non conforme</span></td>
    </tr>
    <tr style="background: #f9fbe7; border: 2.5px solid #2e7d32;">
      <td><b>S2 (Éthique)</b></td>
      <td>S1 <b>sans âge ni nationalité</b></td>
      <td style="text-align: center; font-weight: bold; color: #1b5e20; font-size: 18.5px;">0.627</td>
      <td style="text-align: center; font-weight: bold; color: #d84315; font-size: 18.5px;">33</td>
      <td style="text-align: center; color: #e65100; font-weight: 600;">1.41 (Proxy résiduel)</td>
      <td style="text-align: center;"><span class="verdict-tag" style="background: #e8f5e9; color: #1b5e20; font-size: 15.5px;">🏆 Retenu Prod</span></td>
    </tr>
    <tr style="background: #ffffff;">
      <td><b>S3 (NLP seul)</b></td>
      <td>Synthèse entretien seule (TF-IDF)</td>
      <td style="text-align: center; color: #37474f; font-size: 17.5px;">0.637</td>
      <td style="text-align: center; color: #e65100; font-size: 17.5px;">32</td>
      <td style="text-align: center; color: #e65100; font-weight: 600;">1.62 (Biais verbatims)</td>
      <td style="text-align: center;"><span class="verdict-tag" style="background: #fff3e0; color: #e65100;">⚠️ Trop fragile</span></td>
    </tr>
    <tr style="background: #fafafa;">
      <td><b>S4 (Tabulaire)</b></td>
      <td>Données contextuelles (sans texte)</td>
      <td style="text-align: center; color: #757575; font-size: 17.5px;">0.614</td>
      <td style="text-align: center; color: #c62828; font-size: 17.5px;">39</td>
      <td style="text-align: center; color: #c62828; font-weight: 600;">2.40 (Biais indirect)</td>
      <td style="text-align: center;"><span class="verdict-tag" style="background: #ffebee; color: #c62828;">❌ Aveugle freins</span></td>
    </tr>
  </tbody>
</table>

<div class="insight-grid">
  <div class="insight-card" style="border-left: 4px solid #2e7d32;">
    <h4 style="color: #1b5e20;">🛡️ Le "Coût de l'Éthique" (Prime d'assurance)</h4>
    Passer de S1 à S2 coûte <b>9 erreurs critiques de plus</b> (33 FN vs 24). C'est un compromis assumé face au risque juridique : ce différentiel est absorbé par le <b>filet d'escalade humaine (HITL)</b>.
  </div>
  <div class="insight-card" style="border-left: 4px solid #e65100;">
    <h4 style="color: #e65100;">⚖️ L'illusion du « Fairness through Blindness »</h4>
    Même sans âge ni nationalité, S2 conserve un Disparate Impact de <b>1.41</b>. Les <b>variables proxy</b> (département, diplôme) réinjectent un biais résiduel, rendant l'arbitrage humain indispensable.
  </div>
</div>

---

## Explicabilité Locale et Globale (SHAP sur S2)

<style scoped>
section { font-size: 14.5px; padding-top: 55px; padding-bottom: 50px; }
.top-box {
  background: #f0f4f8;
  border-left: 4px solid #1565c0;
  padding: 4px 10px;
  margin-bottom: 6px;
  font-size: 12.8px;
  line-height: 1.25;
  color: #0d47a1;
}
.shap-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 0.8rem;
  align-items: stretch;
}
.shap-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 6px 9px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.shap-card h4 {
  margin: 0 0 3px 0;
  font-size: 13px;
  color: #1565c0;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 2px;
}
.shap-card ul {
  margin: 0;
  padding-left: 15px;
  font-size: 12px;
  line-height: 1.25;
}
.shap-card li {
  margin-bottom: 2px;
}
.img-container {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 4px 6px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}
</style>

<div class="top-box">
  <b>Audit d'Interprétabilité (AI Act Art. 13) :</b> Décomposition des décisions par valeurs de Shapley (<code>TreeExplainer</code>) sur S2. Chaque prédiction devient explicable et justifiable.
</div>

<div class="shap-grid">
  <div class="shap-card">
    <div>
      <h4>🔍 Enseignements Clés du Summary Plot</h4>
      <ul>
        <li><b>Ancienneté au dernier poste :</b> Socle n°1. Les points rouges à droite indiquent qu'une forte ancienneté tire vers le <b>risque long (+SHAP)</b>.</li>
        <li><b>Mots-clés textuels décisifs :</b> Des termes comme <i>"santé", "barrière", "complexe"</i> ou <i>"isolé"</i> agissent comme des déclencheurs d'alerte.</li>
        <li><b>Absence de biais direct :</b> Preuve visuelle que l'âge et la nationalité sont totalement absents des facteurs d'influence.</li>
      </ul>
    </div>
    <div style="background: #eef2f6; border-left: 3px solid #1565c0; padding: 4px 8px; border-radius: 4px; font-size: 11.8px; line-height: 1.25; margin-top: 4px;">
      <b>Explicabilité Locale (Streamlit) :</b> Graphique en cascade (<i>Waterfall plot</i>) unitaire pour chaque dossier, offrant au conseiller un argumentaire opposable.
    </div>
  </div>

  <div class="img-container">
    <div style="width: 100%; font-size: 12px; font-weight: bold; color: #1565c0; text-align: left; margin-bottom: 2px;">
      📊 Summary Plot SHAP (Classe 2 - Risque)
    </div>
    <img src="assets/shap.png" alt="Graphique SHAP" width="280" style="max-width: 100%; max-height: 185px; object-fit: contain; border-radius: 4px;"/>
    <div style="font-size: 10px; color: #546e7a; text-align: center; line-height: 1.15; margin-top: 1px;">
      <span style="color: #d32f2f; font-weight: bold;">Rouge = Valeur élevée</span> · <span style="color: #1976d2; font-weight: bold;">Bleu = Valeur basse</span>
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 11.5px; margin-top: 5px; padding: 4px 8px; line-height: 1.2;">
  <b>Garantie de transparence :</b> L'algorithme n'est plus une boîte noire. Le conseiller dispose pour chaque usager des 3 critères prépondérants motivant la décision.
</div>

---

# 4. Architecture Backend & Industrialisation

---

## De la Modélisation au Déploiement API (FastAPI & Pydantic)

<style scoped>
section { font-size: 16px; padding-top: 50px; padding-bottom: 40px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 6px 14px;
  margin-bottom: 10px;
  font-size: 14.5px;
  line-height: 1.35;
  color: #0d47a1;
}
.api-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 1rem;
  align-items: stretch;
}
.api-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 10px 12px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.api-card h4 {
  margin: 0 0 6px 0;
  font-size: 15px;
  color: #1565c0;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 3px;
}
.routes-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  margin-bottom: 6px;
}
.routes-table td {
  padding: 4px 6px;
  border-bottom: 1px solid #f0f0f0;
}
.routes-table code {
  font-weight: bold;
  color: #0d47a1;
}
.code-box {
  background: #263238;
  color: #eceff1;
  border-radius: 6px;
  padding: 8px 10px;
  font-family: monospace;
  font-size: 11.5px;
  line-height: 1.25;
}
</style>

<div class="top-box">
  <b>Passage en production :</b> L'artefact sérialisé <code>pipeline_production.joblib</code> (555 Ko) et sa <b>Model Card</b> (<code>pipeline_production.json</code>) sont exposés via un microservice <b>FastAPI</b> asynchrone, typé et testé (Pytest).
</div>

<div class="api-grid">
  <div class="api-card">
    <div>
      <h4>🔌 Contrat d'Interface & Routes RESTful</h4>
      <table class="routes-table">
        <tr>
          <td style="width: 44%;"><code>GET /health</code></td>
          <td>Contrôle de santé du service et présence du modèle en RAM.</td>
        </tr>
        <tr>
          <td><code>POST /predict</code></td>
          <td>Inférence unitaire, probabilités et décision de <b>Fallback (&lt; 65%)</b>.</td>
        </tr>
        <tr>
          <td><code>POST /predict/batch</code></td>
          <td>Traitement de masse pour l'alimentation nocturne du SI.</td>
        </tr>
        <tr>
          <td><code>POST /train</code></td>
          <td>Réentraînement tracé sous MLflow sécurisé par <code>X-API-Key</code>.</td>
        </tr>
      </table>
    </div>
<div style="background: #eef2f6; border-left: 3px solid #1565c0; padding: 6px 10px; border-radius: 4px; font-size: 12.5px; line-height: 1.3;">
  <b>Robustesse par conception :</b> Validation stricte Pydantic à l'entrée. Tout champ aberrant (ancienneté &lt; 0, code INSEE $\neq$ 5 car.) renvoie immédiatement une erreur <code>422 Unprocessable Entity</code> documentée.
</div>
  </div>

  <div class="api-card" style="border-top: 4px solid #009688;">
    <div>
      <h4 style="color: #00796b;">🛡️ Validation de Schéma Pydantic</h4>
      <div class="code-box">
<span style="color: #80cbc4;">class</span> <span style="color: #ffcb6b;">UsagerInput</span>(BaseModel):<br>
&nbsp;&nbsp;anciennete_poste_ans: float = Field(..., ge=0, le=50)<br>
&nbsp;&nbsp;niveau_diplome: str<br>
&nbsp;&nbsp;code_insee_commune: str = Field(..., min_length=5, max_length=5)<br>
&nbsp;&nbsp;code_rome_vise: str = Field(..., min_length=5, max_length=5)<br>
&nbsp;&nbsp;est_allocataire: int = Field(..., ge=0, le=1)<br>
&nbsp;&nbsp;synthese_entretien: str = Field(default="")
      </div>
    </div>
    <div style="font-size: 12px; color: #37474f; line-height: 1.3; margin-top: 6px;">
      ⚡ <b>Performance CPU :</b> Temps d'inférence moyen <b>&lt; 1 ms</b>, parfaitement transparent pour un conseiller en entretien de face-à-face.
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 12.5px; margin-top: 8px; padding: 5px 12px; line-height: 1.25;">
  <b>Qualité logicielle :</b> 6 tests d'intégration automatisés (<code>test_api.py</code>, <code>test_pipeline.py</code>) vérifient le rejet d'entrées corrompues et la conformité des prédictions avant tout déploiement.
</div>

---

## Intégration SI, IHM Conseiller & CI/CD Docker

<style scoped>
section { font-size: 16.5px; padding-top: 50px; padding-bottom: 42px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 6px 14px;
  margin-bottom: 10px;
  font-size: 14.5px;
  line-height: 1.35;
  color: #0d47a1;
}
.si-flow {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  margin: 6px 0 12px 0;
  gap: 8px;
}
.si-card {
  background: #ffffff;
  border: 1.5px solid #1565c0;
  border-radius: 8px;
  padding: 8px 10px;
  text-align: center;
  box-shadow: 0 1px 4px rgba(0,0,0,0.04);
}
.si-arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  color: #0d47a1;
  font-weight: bold;
}
.dual-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.1rem;
}
.dual-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 10px 14px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  font-size: 13.8px;
  line-height: 1.38;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.dual-card h4 {
  margin: 0 0 6px 0;
  font-size: 15.5px;
  color: #1565c0;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 3px;
}
.dual-card ul {
  margin: 0;
  padding-left: 17px;
}
.dual-card li {
  margin-bottom: 5px;
}
</style>

<div class="top-box">
  <b>Urbanisation du SI & Déploiement :</b> L'application métier s'insère sans rupture dans l'environnement du conseiller, hébergée sur Cloud souverain et industrialisée par un pipeline CI/CD reproductible.
</div>

<div class="si-flow">
  <div class="si-card" style="flex: 1.1; border-color: #1565c0;">
    <b style="font-size: 14px; color: #0d47a1;">1. UI Streamlit</b><br>
    <span style="font-size: 11.5px; color: #555;">Saisie profil & notes</span>
  </div>
  <div class="si-arrow">➔</div>
  <div class="si-card" style="flex: 1.2; border-color: #2e7d32; background: #f1f8e9;">
    <b style="font-size: 14px; color: #1b5e20;">2. API FastAPI (CPU)</b><br>
    <span style="font-size: 11.5px; color: #333;">Inférence S2 &lt; 1 ms</span>
  </div>
  <div class="si-arrow">➔</div>
  <div class="si-card" style="flex: 1.1; border-color: #e65100; background: #fff3e0;">
    <b style="font-size: 14px; color: #bf360c;">3. Décision & Explication</b><br>
    <span style="font-size: 11.5px; color: #333;">Jauge 65% + SHAP</span>
  </div>
  <div class="si-arrow">➔</div>
  <div class="si-card" style="flex: 1; border-color: #546e7a;">
    <b style="font-size: 14px; color: #37474f;">4. BDD & Guichet</b><br>
    <span style="font-size: 11.5px; color: #555;">Traçabilité décision</span>
  </div>
</div>

<div class="dual-grid">
  <div class="dual-card" style="border-left: 4px solid #1565c0;">
    <div>
      <h4>🖥️ Expérience Conseiller & Cloud Souverain</h4>
      <ul>
        <li><b>Ergonomie & Décision :</b> Code couleur métier (Vert, Orange, Rouge) + alerte visuelle si certitude &lt; 65% (relais humain immédiat).</li>
        <li><b>Explicabilité intégrée :</b> Restitution des 3 causes majeures (SHAP waterfall) directement sur le poste agent.</li>
        <li><b>Cloud Souverain (SecNumCloud) :</b> Hébergement français (OVHcloud / Outscale) assurant élasticité et confidentialité des données publiques de l'emploi.</li>
      </ul>
    </div>
    <div style="font-size: 12.5px; color: #0d47a1; background: #e3f2fd; padding: 4px 8px; border-radius: 4px; margin-top: 6px;">
      Garantie : Outil consultatif préservant la souveraineté de l'agent public.
    </div>
  </div>

  <div class="dual-card" style="border-left: 4px solid #2e7d32;">
    <div>
      <h4 style="color: #1b5e20;">🚀 Pipeline CI/CD & Déploiement Reproductible</h4>
      <ul>
        <li><b>GitHub Actions sur <code>master</code> :</b> Linting automatique (<code>flake8</code>, <code>black</code>) + 6 tests unitaires/intégration Pytest.</li>
        <li><b>Image Docker optimisée :</b> Multi-stage build Python 3.12-slim (&lt; 300 Mo), sécurité non-root, sans cache de build.</li>
        <li><b>Stack complet :</b> <code>docker compose up</code> monte en 1 commande FastAPI, Streamlit, Prometheus et Grafana.</li>
      </ul>
    </div>
    <div style="font-size: 12.5px; color: #1b5e20; background: #e8f5e9; padding: 4px 8px; border-radius: 4px; margin-top: 6px;">
      Garantie : Zéro régression, 100% reproductible du code à la production.
    </div>
  </div>
</div>

---

# 5. Supervision MLOps & Amélioration Continue

---

## Le Monitoring en Temps Réel (Prometheus & Grafana)

<style scoped>
section { font-size: 14.5px; padding-top: 65px; padding-bottom: 45px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 4px 12px;
  margin-bottom: 6px;
  font-size: 13px;
  line-height: 1.25;
  color: #0d47a1;
}
.mon-grid {
  display: grid;
  grid-template-columns: 1.12fr 0.88fr;
  gap: 0.8rem;
  align-items: stretch;
}
.mon-cards {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 5px;
}
.card-m {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 5px 9px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
.card-m h4 {
  margin: 0 0 2px 0;
  font-size: 13px;
}
.card-m ul {
  margin: 0;
  padding-left: 15px;
  font-size: 11.8px;
  line-height: 1.25;
}
.card-m li {
  margin-bottom: 2px;
}
.img-box {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 6px;
  padding: 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
}
</style>

<div class="top-box">
  <b>Supervision continue en production :</b> Stack intégrée dans <code>docker-compose.yml</code> associant <b>Prometheus</b> (métriques temps réel), <b>Grafana</b> (tableaux de bord) et <b>MLflow</b> (registre de modèles).
</div>

<div class="mon-grid">
  <div class="mon-cards">
    <div class="card-m" style="border-left: 4px solid #1565c0;">
      <h4 style="color: #0d47a1;">⚙️ Métriques Système (Disponibilité & SLAs)</h4>
      <ul>
        <li><b>Latence d'inférence (p95) :</b> Temps de réponse &lt; 100 ms sous charge.</li>
        <li><b>Disponibilité & Codes HTTP :</b> Taux d'erreurs 5xx (&lt; 0.01%) et rejets Pydantic 422.</li>
        <li><b>Ressources :</b> Consommation CPU/RAM de l'API (empreinte &lt; 200 Mo).</li>
      </ul>
    </div>
    <div class="card-m" style="border-left: 4px solid #2e7d32;">
      <h4 style="color: #1b5e20;">🎯 Métriques Métier & Santé du Modèle</h4>
      <ul>
        <li><b>Distribution des prédictions :</b> Suivi des parts relatives (Classes 0, 1, 2) pour détecter les bascules anormales de population.</li>
        <li><b>Confiance du modèle :</b> Histogramme glissant des probabilités maximales.</li>
        <li><b>Taux d'escalade humaine (Fallback) :</b> Part de dossiers où la certitude est &lt; 65% (nominal : ~38-40%).</li>
      </ul>
    </div>
  </div>

  <div class="img-box">
    <div style="width: 100%; font-size: 12px; font-weight: bold; color: #1565c0; text-align: left; margin-bottom: 2px;">
      🏗️ Architecture de Métrologie Conteneurisée
    </div>
    <img src="assets/architecture_mlops.png" alt="Architecture MLOps" width="270" style="max-width: 100%; max-height: 175px; object-fit: contain; border-radius: 4px;"/>
    <div style="font-size: 10px; color: #546e7a; text-align: center; line-height: 1.15; margin-top: 1px;">
      FastAPI expose <code>/metrics</code> ➔ Scraped par Prometheus ➔ Grafana
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 11px; margin-top: 4px; padding: 4px 10px; line-height: 1.2;">
  <b>Principe MLOps :</b> Le monitoring ne se limite pas aux pannes serveur ; il surveille en continu la pertinence décisionnelle de l'IA pour garantir un service public équitable.
</div>

---

## Filet Humain (Seuil 65%) & Alerte Dérive Précoce (+20%)

<style scoped>
section { font-size: 16px; padding-top: 50px; padding-bottom: 40px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 6px 14px;
  margin-bottom: 10px;
  font-size: 14px;
  line-height: 1.35;
  color: #0d47a1;
}
.oper-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
.oper-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 10px 12px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.03);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.oper-card h4 {
  margin: 0 0 6px 0;
  font-size: 14.5px;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 3px;
}
.oper-card ul {
  margin: 0;
  padding-left: 17px;
  font-size: 13px;
  line-height: 1.35;
}
.oper-card li {
  margin-bottom: 4px;
}
</style>

<div class="top-box">
  <b>Garde-fou éthique & Détection temps réel :</b> La vérité terrain (retour à l'emploi) n'étant connue qu'à 6-12 mois, le <b>seuil de rejet à 65%</b> protège l'usager et sert d'<b>indicateur avancé de dérive</b> immédiat.
</div>

<div class="oper-grid">
  <div class="oper-card" style="border-left: 4px solid #1565c0;">
    <div>
      <h4 style="color: #0d47a1;">🛡️ Seuil de Rejet à 65% (Anti-Biais d'Automatisation)</h4>
      <ul>
        <li><b>Calibration imparfaite :</b> Les scores <code>predict_proba</code> du LightGBM ne sont pas des probabilités pures (Brier Score = 0.48). Le seuil agit en filtre opérationnel.</li>
        <li><b>Bascule empirique mesurée :</b><br>
          • Score $\ge$ 65% : <b>76% d'exactitude</b> (recommandation fiable).<br>
          • Score &lt; 65% : <b>46% d'exactitude</b> (l'IA doute ➔ abstention).</li>
      </ul>
      <div style="margin-top: 6px; display: flex; flex-direction: column; gap: 4px; font-size: 12px;">
        <div style="background: #e8f5e9; border-left: 3px solid #2e7d32; padding: 3px 6px; border-radius: 3px;">
          <b>🟢 Confiance $\ge$ 65% :</b> L'IHM affiche le conseil au conseiller.
        </div>
        <div style="background: #fff3e0; border-left: 3px solid #e65100; padding: 3px 6px; border-radius: 3px;">
          <b>🟡 Confiance &lt; 65% :</b> <code>fallback: true</code>, l'agent décide souverainement.
        </div>
      </div>
    </div>
  </div>

  <div class="oper-card" style="border-left: 4px solid #e65100;">
    <div>
      <h4 style="color: #bf360c;">🚨 Alerte Dérive (+20% relatif) & Playbook MLOps</h4>
      <ul>
        <li><b>Taux nominal de fallback :</b> En rythme de croisière, ~38-40% des dossiers sont sous 65%.</li>
        <li><b>Signal précoce (+20%) :</b> Si le taux de rejet dépasse <b>48% sur 4 semaines glissantes</b>, c'est une dérive structurelle (choc économique, changement de verbatims).</li>
      </ul>
      <div style="background: #fbe9e7; border-left: 3px solid #d84315; padding: 6px 8px; border-radius: 4px; margin-top: 6px; font-size: 12px; line-height: 1.3;">
        <b>Playbook d'action gradué :</b><br>
        1. <b>Contrôle PSI :</b> Identifier les variables d'entrée ayant dérivé.<br>
        2. <b>Recalibration :</b> Ajuster les scores (Platt/isotonique) sans réentraîner.<br>
        3. <b>Réentraînement ciblé :</b> Appel <code>POST /train</code> si le drift persiste.
      </div>
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 12.5px; margin-top: 8px; padding: 5px 12px; line-height: 1.25;">
  <b>Bénéfice majeur :</b> Grâce au taux de fallback, l'administration est alertée dès la 3ᵉ semaine d'une anomalie de modèle, sans devoir attendre un an le constat d'échec sur le terrain.
</div>

---

## Cycle de Vie : Boucle de Rétroaction & Dérive (Drift)

<style scoped>
section { font-size: 15.5px; padding-top: 50px; padding-bottom: 40px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 5px 12px;
  margin-bottom: 8px;
  font-size: 13.5px;
  line-height: 1.3;
  color: #0d47a1;
}
.img-wrap {
  text-align: center;
  margin: 6px 0 8px 0;
}
.drift-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 0.9rem;
}
.drift-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 8px 12px;
  font-size: 12.8px;
  line-height: 1.35;
}
.drift-card h4 {
  margin: 0 0 4px 0;
  font-size: 14px;
}
</style>

<div class="top-box">
  <b>Pérénité du produit IA :</b> Éviter le piège de la prophétie auto-réalisatrice lors des réentraînements et superviser mathématiquement la dérive de distribution des données entrantes.
</div>

<div class="img-wrap">
  <img src="assets/feedback_loop.png" alt="Boucle de Rétroaction" width="940" style="max-width: 100%; max-height: 195px; object-fit: contain; border-radius: 6px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);"/>
</div>

<div class="drift-grid">
  <div class="drift-card" style="border-left: 4px solid #c62828;">
    <h4 style="color: #b71c1c;">🔄 Le Piège de la Prophétie Auto-Réalisatrice</h4>
    Si un usager classé <i>Risque long</i> retrouve un emploi en 4 mois grâce à l'aide renforcée, le modèle naïf le requalifie en "retour rapide" lors du réentraînement et désapprend son utilité !<br>
    ➔ <b>Solution par conception :</b> Enregistrement obligatoire de la variable <code>a_beneficie_aide_renforcee</code> pour isoler l'effet causal de l'accompagnement.
  </div>

  <div class="drift-card" style="border-left: 4px solid #2e7d32;">
    <h4 style="color: #1b5e20;">📈 Surveillance Mathématique du Data Drift (PSI)</h4>
    Calcul mensuel du <b>Population Stability Index (PSI)</b> sur les entrées :<br>
    • $PSI &lt; 0.10$ : Distribution stable.<br>
    • $0.10 \le PSI \le 0.20$ : Dérive modérée sous surveillance.<br>
    • <b>$PSI &gt; 0.20$ : Dérive critique</b> (déclenchement automatique du réentraînement supervisé sous MLflow).
  </div>
</div>

---

# 6. Bilan Économique, Perspectives & Conclusion

---

## Comparatif Économique & ROI (FinOps & Métier)

<style scoped>
section { font-size: 16px; padding-top: 50px; padding-bottom: 40px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 6px 14px;
  margin-bottom: 10px;
  font-size: 14.5px;
  line-height: 1.35;
  color: #0d47a1;
}
.roi-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.1rem;
}
.roi-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 12px 14px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.roi-card h4 {
  margin: 0 0 8px 0;
  font-size: 16px;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 4px;
}
.roi-card ul {
  margin: 0;
  padding-left: 17px;
  font-size: 13.8px;
  line-height: 1.38;
}
.roi-card li {
  margin-bottom: 5px;
}
</style>

<div class="top-box">
  <b>Arbitrage Valeur & Sobriété :</b> La viabilité d'un projet IA en service public repose sur deux piliers : la frugalité d'infrastructure (FinOps) et la maximisation du retour sur investissement humain et social.
</div>

<div class="roi-grid">
  <div class="roi-card" style="border-left: 5px solid #1565c0;">
    <div>
      <h4 style="color: #0d47a1;">⚡ Frugalité Numérique & FinOps (CPU vs GPU)</h4>
      <ul>
        <li><b>Empreinte RAM minime :</b> Pipeline complet &lt; 200 Mo en mémoire vive.</li>
        <li><b>Inférence ultra-rapide sur CPU :</b> Temps de réponse moyen &lt; 1 ms, sans recourir à des accélérateurs matériels énergivores.</li>
        <li><b>Économie directe &gt; 80% :</b> Zéro dépendance aux clusters GPU coûteux nécessaires aux LLMs ou architectures Transformers lourdes.</li>
      </ul>
    </div>
    <div style="font-size: 12px; color: #0d47a1; background: #e3f2fd; padding: 4px 8px; border-radius: 4px; margin-top: 6px; font-weight: 500;">
      🌱 Alignement Green IT & sobriété budgétaire publique.
    </div>
  </div>

  <div class="roi-card" style="border-left: 5px solid #2e7d32;">
    <div>
      <h4 style="color: #1b5e20;">⚖️ L'Économie de l'Erreur & Limites du Rappel</h4>
      <ul>
        <li><b>Faux Positif (Sur-accompagnement) :</b> Coût marginal = un entretien approfondi de 30 min (~25€ de temps conseiller).</li>
        <li><b>Faux Négatif (Risque long ignoré) :</b> Coût sociétal majeur = 12 à 24 mois d'allocation et rupture sociale (<b>&gt; 15 000€</b>).</li>
        <li><b>Pourquoi ne pas viser 95% de Rappel ?</b><br>
          Forcer 95% ferait s'effondrer la précision (explosion des faux positifs), saturant les dispositifs renforcés, débordant les conseillers et diluant l'aide pour les vrais cas critiques.</li>
      </ul>
    </div>
    <div style="font-size: 11.5px; color: #1b5e20; background: #e8f5e9; padding: 4px 8px; border-radius: 4px; margin-top: 6px; font-weight: 500;">
      🎯 Arbitrage réaliste : protection maximale sans saturer les capacités d'accueil.
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 12px; margin-top: 6px; padding: 4px 10px; line-height: 1.25;">
  <b>Synthèse économique & opérationnelle :</b> En combinant un coût machine quasi nul et un rappel équilibré (~75-80%), notre modèle protège les demandeurs vulnérables tout en restant soutenable pour les agents et le budget public.
</div>

---

## Perspectives de Passage à l'Échelle (Scale-up)

<style scoped>
section { font-size: 16px; padding-top: 50px; padding-bottom: 40px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 6px 14px;
  margin-bottom: 10px;
  font-size: 14.5px;
  line-height: 1.35;
  color: #0d47a1;
}
.scale-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 14px;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 10px;
}
.scale-table th {
  background: #1565c0;
  color: #ffffff;
  padding: 8px 12px;
  font-weight: 600;
  text-align: left;
  font-size: 14.5px;
}
.scale-table td {
  padding: 8px 12px;
  border-top: 1px solid #e0e0e0;
  vertical-align: middle;
  line-height: 1.35;
}
.scale-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
.scale-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 8px 12px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  font-size: 13px;
  line-height: 1.35;
}
.scale-card h4 {
  margin: 0 0 4px 0;
  font-size: 14px;
}
</style>

<div class="top-box">
  <b>Trajectoire d'industrialisation (Scale-up) :</b> Feuille de route technique pour faire évoluer le système du cadre expérimental (2 500 usagers) vers un déploiement national à grande échelle (1 million de profils).
</div>

<table class="scale-table">
  <thead>
    <tr>
      <th style="width: 22%;">Dimension Clé</th>
      <th style="width: 38%;">Échelle MVP (2 500 profils) — Actuel</th>
      <th style="width: 40%;">Échelle Nationale (1 000 000 profils) — Cible</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #fafafa;">
      <td><b>Données Territoriales</b></td>
      <td>Agrégation par département (anti-overfitting)</td>
      <td>Exploitation du code commune INSEE brut (bassins d'emploi fins)</td>
    </tr>
    <tr style="background: #f9fbe7;">
      <td><b>Traitement NLP</b></td>
      <td>TF-IDF avec stop words (léger, explicable, CPU)</td>
      <td>Embeddings sémantiques CamemBERT fins avec surcouche LIME/SHAP</td>
    </tr>
    <tr style="background: #ffffff;">
      <td><b>Pipeline MLOps</b></td>
      <td>SQLite MLflow local + Docker-Compose</td>
      <td>Feature Store (Feast), Registry MLflow distribué & monitoring continu</td>
    </tr>
  </tbody>
</table>

<div class="scale-grid">
  <div class="scale-card" style="border-left: 4px solid #1565c0;">
    <h4 style="color: #0d47a1;">🗺️ Granularité Géographique & Bassins d'Emploi</h4>
    Avec un volume massif, la cardinalité INSEE devient un atout prédictif majeur plutôt qu'un risque de mémorisation par cœur, permettant de modéliser les dynamiques de l'emploi bassin par bassin.
  </div>

  <div class="scale-card" style="border-left: 4px solid #2e7d32;">
    <h4 style="color: #1b5e20;">🧠 Richesse Sémantique & Modèles de Langage</h4>
    Sur 500 000 verbatims, un modèle de type CamemBERT capte les tournures subtiles et les négations tout en restant auditable grâce aux bibliothèques d'explicabilité post-hoc.
  </div>
</div>

---

## Conclusion & Bilan de la Soutenance

<style scoped>
section { font-size: 16px; padding-top: 50px; padding-bottom: 40px; }
.top-box {
  background: #f0f4f8;
  border-left: 5px solid #1565c0;
  padding: 6px 14px;
  margin-bottom: 12px;
  font-size: 14.5px;
  line-height: 1.35;
  color: #0d47a1;
}
.concl-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1rem;
}
.concl-card {
  background: #ffffff;
  border: 1.5px solid #cfd8dc;
  border-radius: 8px;
  padding: 12px 14px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.concl-card h4 {
  margin: 0 0 6px 0;
  font-size: 15.5px;
  border-bottom: 1.5px solid #e0e0e0;
  padding-bottom: 3px;
}
.concl-card ul {
  margin: 0;
  padding-left: 17px;
  font-size: 13.5px;
  line-height: 1.35;
}
.concl-card li {
  margin-bottom: 4px;
}
</style>

<div class="top-box">
  <b>Bilan Synthétique du Projet :</b> Réalisation complète, robuste et éthique d'un produit d'IA d'aide à la décision pour le service public de l'emploi, prêt pour l'expérimentation terrain.
</div>

<div class="concl-grid">
  <div class="concl-card" style="border-top: 5px solid #1565c0;">
    <div>
      <h4 style="color: #0d47a1;">🚀 Produit End-to-End</h4>
      <ul>
        <li><b>Chaîne complète :</b> Du cadrage métier et audit des données jusqu'à l'inférence.</li>
        <li><b>Microservices :</b> API FastAPI asynchrone, UI Streamlit ergonomique et conteneurs Docker.</li>
        <li><b>Reproductibilité :</b> Pipeline CI/CD GitHub Actions automatisé (100% testé).</li>
      </ul>
    </div>
    <div style="font-size: 12px; color: #0d47a1; background: #e3f2fd; padding: 4px 6px; border-radius: 4px; margin-top: 6px; font-weight: 500;">
      ✅ Livrable déployable en 1 commande.
    </div>
  </div>

  <div class="concl-card" style="border-top: 5px solid #2e7d32;">
    <div>
      <h4 style="color: #1b5e20;">🛡️ Éthique & AI Act</h4>
      <ul>
        <li><b>Privacy by Design :</b> Retrait préventif de l'âge et de la nationalité (Scénario S2).</li>
        <li><b>Explicabilité totale :</b> Décomposition unitaire et collective SHAP intégrée à l'IHM.</li>
        <li><b>Human-In-The-Loop :</b> Seuil de repli à 65% préservant la souveraineté de l'agent public.</li>
      </ul>
    </div>
    <div style="font-size: 12px; color: #1b5e20; background: #e8f5e9; padding: 4px 6px; border-radius: 4px; margin-top: 6px; font-weight: 500;">
      ✅ Conforme aux normes Haut Risque.
    </div>
  </div>

  <div class="concl-card" style="border-top: 5px solid #e65100;">
    <div>
      <h4 style="color: #bf360c;">💡 Sobriété & Métier</h4>
      <ul>
        <li><b>Frugalité Green IT :</b> Inférence ultra-rapide &lt; 1 ms sur simple CPU sans GPU coûteux.</li>
        <li><b>Doctrine métier :</b> Priorité absolue au rappel classe 2 pour éradiquer les abandons.</li>
        <li><b>Supervision MLOps :</b> Détection précoce du drift via le taux de fallback et le PSI.</li>
      </ul>
    </div>
    <div style="font-size: 12px; color: #bf360c; background: #fff3e0; padding: 4px 6px; border-radius: 4px; margin-top: 6px; font-weight: 500;">
      ✅ Impact public et budgétaire maximisé.
    </div>
  </div>
</div>

<div class="tech-box" style="font-size: 12.5px; margin-top: 8px; padding: 5px 12px; line-height: 1.25;">
  <b>Message de conclusion :</b> L'intelligence artificielle au service de l'emploi n'a de valeur que si elle conjugue rigueur mathématique, humilité éthique et intégration fluide au service des conseillers humains.
</div>

---

<!-- _class: lead -->
# Merci de votre attention.
