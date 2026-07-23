import json

with open("cas-usage.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# Find the cell index where id == "2c841210" or "Interprétation pour la communication client"
index = -1
for i, cell in enumerate(nb["cells"]):
    if cell.get("id") == "2c841210":
        index = i
        break

if index != -1:
    markdown_cell = {
        "cell_type": "markdown",
        "id": "persistance-metadata-md",
        "metadata": {},
        "source": [
            "### 6.9 Sauvegarde des artefacts locaux (Joblib + JSON)\n",
            "\n",
            "Pour assurer une traçabilité complète de l'artefact (Model Card technique), nous exportons le modèle final ainsi que ses métadonnées et performances dans un fichier JSON."
        ]
    }
    
    code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "id": "persistance-metadata-code",
        "metadata": {},
        "outputs": [],
        "source": [
            "print(\"\\n\" + \"=\"*50)\n",
            "print(\"💾 Sauvegarde de l'artefact S2 et de ses métadonnées...\")\n",
            "print(\"=\"*50)\n",
            "\n",
            "import json\n",
            "from datetime import datetime\n",
            "import sklearn\n",
            "import sys\n",
            "import hashlib\n",
            "from pathlib import Path\n",
            "import joblib\n",
            "\n",
            "# Récupération de l'empreinte du dataset source\n",
            "dataset_path = Path(\"data/dataset_synthetique_parcours_emploi.csv\")\n",
            "dataset_hash = hashlib.md5(dataset_path.read_bytes()).hexdigest() if dataset_path.exists() else \"non_disponible\"\n",
            "\n",
            "# Récupération des noms des features du scénario S2\n",
            "num_s2, cat_nom_s2, cat_ord_s2, text_s2 = get_scenario_features(\"S2\")\n",
            "\n",
            "metadata = {\n",
            "    \"model_name\": \"modele_risque_chomage_S2\",\n",
            "    \"model_version\": \"v1.0.0\",\n",
            "    \"config_name\": \"S2_Ethique\",\n",
            "    \"created_at\": datetime.now().isoformat(),\n",
            "    \"sklearn_version\": sklearn.__version__,\n",
            "    \"python_version\": sys.version.split()[0],\n",
            "    \"dataset_md5\": dataset_hash,\n",
            "    \"hyperparameters\": best_lgb_params,\n",
            "    \"metrics_test_internal\": {\n",
            "        \"f1_macro\": float(f1_test_s2),\n",
            "        \"accuracy\": float(acc_s2),\n",
            "        \"fn_classe2\": int(fn_classe2_s2),\n",
            "        \"confusion_matrix\": cm_s2.tolist()\n",
            "    },\n",
            "    \"feature_columns\": {\n",
            "        \"numeric\": num_s2,\n",
            "        \"categorical_nominal\": cat_nom_s2,\n",
            "        \"categorical_ordinal\": cat_ord_s2,\n",
            "        \"text\": text_s2\n",
            "    },\n",
            "    \"target\": {\n",
            "        \"column\": \"classe_retour_emploi\",\n",
            "        \"mapping\": {\n",
            "            \"Rapide\": 0,\n",
            "            \"Moyen\": 1,\n",
            "            \"Risque longue durée\": 2\n",
            "        }\n",
            "    }\n",
            "}\n",
            "\n",
            "# Sauvegarde du modèle (Joblib)\n",
            "joblib.dump(final_pipeline_s2, \"models/pipeline_production.joblib\")\n",
            "\n",
            "# Sauvegarde des métadonnées (JSON)\n",
            "with open(\"models/pipeline_production.json\", \"w\", encoding=\"utf-8\") as f:\n",
            "    json.dump(metadata, f, indent=4, ensure_ascii=False)\n",
            "\n",
            "print(\"✅ Modèle sauvegardé : models/pipeline_production.joblib\")\n",
            "print(\"✅ Métadonnées sauvegardées : models/pipeline_production.json\")\n"
        ]
    }
    nb["cells"].insert(index, code_cell)
    nb["cells"].insert(index, markdown_cell)
    
    with open("cas-usage.ipynb", "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Notebook updated successfully.")
else:
    print("Could not find the target cell to insert before.")
