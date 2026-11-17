import docx, openpyxl, json
from pathlib import Path

# 1. Jatin Consolidated Pack
doc_j = docx.Document('source_material/Jatin_Consolidated_Research_Pack.docx')
jatin_papers = []
# Find the paragraphs before each table to get the title
headings = [p.text.strip() for p in doc_j.paragraphs if p.text.strip().startswith('JTN')]

for i in range(1, 14):
    t = doc_j.tables[i]
    d = {r.cells[0].text.strip(): r.cells[1].text.strip() for r in t.rows}
    title = headings[i-1] if i-1 < len(headings) else f'JTN{i:02d}'
    d['Title_Heading'] = title
    jatin_papers.append(d)

print(f"=== JATIN PAPERS (Consolidated): {len(jatin_papers)} ===")
for idx, p in enumerate(jatin_papers, 1):
    print(f"JTN{idx:02d}: {p['Title_Heading']}")
    print(f"   Authors: {p.get('Authors')}")
    print(f"   DOI/Link: {p.get('DOI / source link')}")
    print(f"   Year/Venue: {p.get('Year / venue / status')}")
    print(f"   Reading Status: {p.get('Reading / verification status')}")

# 2. Suresh Consolidated Pack
doc_s = docx.Document('source_material/Suresh_Gopal_Consolidated_Research_Pack.docx')
suresh_papers = []
s_headings = [p.text.strip() for p in doc_s.paragraphs if p.text.strip().startswith('SG')]

for i in range(1, 10):
    t = doc_s.tables[i]
    d = {r.cells[0].text.strip(): r.cells[1].text.strip() for r in t.rows}
    title = s_headings[i-1] if i-1 < len(s_headings) else f'SG{i:02d}'
    d['Title_Heading'] = title
    suresh_papers.append(d)

print(f"\n=== SURESH PAPERS (Consolidated): {len(suresh_papers)} ===")
for idx, p in enumerate(suresh_papers, 1):
    print(f"SG{idx:02d}: {p['Title_Heading']}")
    print(f"   Authors: {p.get('Authors')}")
    print(f"   DOI/Link: {p.get('DOI / source link')}")
    print(f"   Year/Venue: {p.get('Year / venue / status')}")
    print(f"   Reading Status: {p.get('Reading / verification status')}")

# 3. Ismayra Pack
wb = openpyxl.load_workbook('source_material/Ismayra_Deep_Learning_Research/Ismayra_Deep_Learning_Research_Matrix.xlsx', data_only=True)
ws = wb['Deep Learning Papers']
headers = [str(ws.cell(1, c).value or '').strip() for c in range(1, ws.max_column+1)]
ismayra_papers = []
for r in range(2, ws.max_row+1):
    vals = [str(ws.cell(r, c).value or '').strip() for c in range(1, ws.max_column+1)]
    if any(vals):
        row_dict = dict(zip(headers, vals))
        ismayra_papers.append(row_dict)

print(f"\n=== ISMAYRA PAPERS: {len(ismayra_papers)} ===")
for p in ismayra_papers:
    print(f"{p.get('ID')}: {p.get('Title')}")
    print(f"   Authors: {p.get('Authors')}")
    print(f"   DOI/URL: {p.get('DOI / URL')}")
    print(f"   Year/Venue: {p.get('Year')} | {p.get('Venue')}")
    print(f"   Reading Status: {p.get('Reading Status')}")
