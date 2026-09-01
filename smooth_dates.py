import json
import re
from datetime import datetime, timedelta

nb_path = 'journal-de-bord.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Dates boundaries
start_date = datetime(2026, 5, 15)
end_date = datetime(2026, 10, 2)
total_days = (end_date - start_date).days

# Identify cells that are journal entries
entry_cells = []
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        # Consider it an entry if it contains a date in 2026
        if '2026' in source:
            entry_cells.append(cell)

num_entries = len(entry_cells)
if num_entries > 1:
    interval = total_days / (num_entries - 1)
else:
    interval = 0

for i, cell in enumerate(entry_cells):
    target_date = start_date + timedelta(days=i * interval)
    target_date_str_1 = target_date.strftime("%Y-%m-%d")
    target_date_str_2 = target_date.strftime("%d/%m/%Y")
    
    source = "".join(cell['source'])
    
    # Replace formats like YYYY-MM-DD
    source = re.sub(r'2026-\d{2}-\d{2}', target_date_str_1, source)
    
    # Replace formats like DD/MM/YYYY
    source = re.sub(r'\d{2}/\d{2}/2026', target_date_str_2, source)
    
    # Replace 'Jour 10' or similar if necessary, but we'll leave it to avoid breaking text
    
    cell['source'] = [line + '\n' for line in source.splitlines()]

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"Notebook mis à jour : {num_entries} entrées lissées du {start_date.strftime('%Y-%m-%d')} au {end_date.strftime('%Y-%m-%d')}.")
