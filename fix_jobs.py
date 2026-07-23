import json

with open("cas-usage.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

changed = False
for cell in nb.get("cells", []):
    if cell.get("cell_type") == "code":
        for i, line in enumerate(cell["source"]):
            if "n_jobs=-1" in line:
                cell["source"][i] = line.replace("n_jobs=-1", "n_jobs=1")
                changed = True

if changed:
    with open("cas-usage.ipynb", "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print("Notebook updated successfully.")
else:
    print("No changes made.")
