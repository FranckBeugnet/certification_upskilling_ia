import sys
import json
import os
import subprocess

def merge_notebooks(main_path, journal_path, out_path):
    if not os.path.exists(main_path):
        print(f"Erreur : Le fichier principal '{main_path}' n'existe pas.")
        sys.exit(1)
        
    if not os.path.exists(journal_path):
        print(f"Erreur : Le fichier journal '{journal_path}' n'existe pas.")
        sys.exit(1)

    print(f"Chargement de {main_path}...")
    with open(main_path, 'r', encoding='utf-8') as f:
        main_nb = json.load(f)

    print(f"Chargement de {journal_path}...")
    with open(journal_path, 'r', encoding='utf-8') as f:
        journal_nb = json.load(f)

    # 1. Extraire les cellules du journal (en ignorant le titre principal si c'est le 1er)
    journal_cells = journal_nb.get('cells', [])
    if journal_cells and journal_cells[0]['cell_type'] == 'markdown' and '# Journal de bord' in "".join(journal_cells[0]['source']):
        journal_cells = journal_cells[1:]

    # 2. Trouver la section "C. Journal de bord" dans le main
    start_idx = -1
    end_idx = -1
    
    for i, cell in enumerate(main_nb['cells']):
        if cell['cell_type'] == 'markdown':
            source = "".join(cell['source'])
            if '### C. Journal de bord' in source:
                start_idx = i
            # On cherche la fin de la section (soit l'Annexe C, soit la ligne de séparation --- après l'export PDF)
            elif start_idx != -1 and end_idx == -1 and ('## Annexe C' in source or (source.strip() == '---' and i > start_idx + 1)):
                end_idx = i

    if start_idx == -1:
        print("Erreur : Impossible de trouver '### C. Journal de bord' dans le notebook principal.")
        sys.exit(1)
        
    if end_idx == -1:
        end_idx = start_idx + 1 # Au pire, on insère juste après

    print(f"Section trouvée entre les cellules {start_idx} et {end_idx}.")
    
    # 3. Préparer les cellules finales
    # On garde la cellule de titre "C. Journal de bord" mais on la nettoie de ses instructions
    title_cell = main_nb['cells'][start_idx]
    title_cell['source'] = ['### C. Journal de bord\n', '\n', '*Journal de bord intégré automatiquement pour la certification.*\n']

    final_cells = main_nb['cells'][:start_idx + 1] + journal_cells + main_nb['cells'][end_idx:]
    
    main_nb['cells'] = final_cells

    print(f"Sauvegarde du notebook fusionné vers {out_path}...")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(main_nb, f, indent=1, ensure_ascii=False)
        
    print("Fusion terminée avec succès ! Lancement de la conversion HTML...")
    
    # 4. Générer la version HTML du fichier fusionné
    try:
        subprocess.run([sys.executable, "-m", "jupyter", "nbconvert", "--to", "html", out_path], check=True)
        print(f"Export HTML réussi : {out_path.replace('.ipynb', '.html')}")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la conversion HTML : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_for_certif.py <main_notebook> <journal_notebook> <output_notebook>")
        sys.exit(1)
        
    merge_notebooks(sys.argv[1], sys.argv[2], sys.argv[3])
