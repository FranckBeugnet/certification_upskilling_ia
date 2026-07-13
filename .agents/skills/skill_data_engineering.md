# Skill : Data Engineering & Base de Données 🗄️

**Agent référent :** Data Engineer / Tech Lead

## 🎯 Objectif
Assurer une manipulation, une structuration et une ingestion optimales des données, depuis leurs sources brutes jusqu'à leur mise à disposition pour la modélisation ou l'API.

## 🛠️ Règles d'implémentation

### 1. Ingestion et Stockage
- **Ingestion Idempotente :** Construire des pipelines d'ingestion qui peuvent être rejoués sans créer de doublons ou de conflits. L'ingestion doit être robuste aux redémarrages.
- **Format Parquet :** Privilégier le format Parquet (avec `pyarrow`) pour le stockage intermédiaire des DataFrames volumineux (plus rapide, typé, et compressé par rapport au CSV).

### 2. Modélisation de Données (ORM)
- **SQLAlchemy :** Utiliser SQLAlchemy (v2.0+) pour modéliser les tables SQL sous forme de classes Python.
- **Migrations Alembic :** Gérer toute évolution du schéma de base de données via Alembic. Ne jamais altérer la base de production manuellement.

### 3. Architecture des flux
- **Cartographie des sources :** Identifier clairement toutes les sources hétérogènes (API, CSV, bases relationnelles).
- **Documentation visuelle :** Maintenir des schémas Mermaid pour documenter les flux de données (du requêtage à la mise en base).
