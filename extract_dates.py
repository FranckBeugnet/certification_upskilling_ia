import json
import re

nb_path = 'journal-de-bord.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

entries = []
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        # Look for "*Date :" or similar
        match = re.search(r"\*Date\s*:\s*([^>]+?)\*", source, re.IGNORECASE)
        if match:
            entries.append((i, match.group(1).strip()))

print(f"Found {len(entries)} entries:")
for idx, date in entries:
    print(f"Cell {idx}: {date}")
