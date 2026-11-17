import docx, openpyxl, re
from pathlib import Path

# Load Jatin consolidated papers
doc_j = docx.Document('source_material/Jatin_Consolidated_Research_Pack.docx')
headings_j = [p.text.strip() for p in doc_j.paragraphs if p.text.strip().startswith('JTN')]
jatin_papers = []
for i in range(1, 14):
    t = doc_j.tables[i]
    d = {r.cells[0].text.strip(): r.cells[1].text.strip() for r in t.rows}
    title = headings_j[i-1].split('.', 1)[1].strip() if i-1 < len(headings_j) else f'JTN{i:02d}'
    d['Paper_ID'] = f'JTN{i:02d}'
    d['Title'] = title
    d['Member'] = 'Jatin (258100003)'
    d['Category'] = 'Anomaly-Based, Hybrid and Adaptive Detection'
    jatin_papers.append(d)

# Load Suresh consolidated papers
doc_s = docx.Document('source_material/Suresh_Gopal_Consolidated_Research_Pack.docx')
headings_s = [p.text.strip() for p in doc_s.paragraphs if p.text.strip().startswith('SG')]
suresh_papers = []
for i in range(1, 10):
    t = doc_s.tables[i]
    d = {r.cells[0].text.strip(): r.cells[1].text.strip() for r in t.rows}
    title = headings_s[i-1].split('.', 1)[1].strip() if i-1 < len(headings_s) else f'SG{i:02d}'
    d['Paper_ID'] = f'SG{i:02d}'
    d['Title'] = title
    d['Member'] = 'Suresh Gopal Singh (258100001)'
    d['Category'] = 'Machine Learning and Open-Set Detection'
    suresh_papers.append(d)

# Load Ismayra papers
wb = openpyxl.load_workbook('source_material/Ismayra_Deep_Learning_Research/Ismayra_Deep_Learning_Research_Matrix.xlsx', data_only=True)
ws = wb['Deep Learning Papers']
headers = [str(ws.cell(1, c).value or '').strip() for c in range(1, ws.max_column+1)]
ismayra_papers = []
for r in range(2, ws.max_row+1):
    vals = [str(ws.cell(r, c).value or '').strip() for c in range(1, ws.max_column+1)]
    if any(vals):
        row_dict = dict(zip(headers, vals))
        d = {
            'Paper_ID': row_dict['ID'],
            'Title': row_dict['Title'],
            'Member': 'Ismayra Praveen (258100002)',
            'Category': 'Deep Learning-Based Detection',
            'Authors': row_dict['Authors'],
            'Year / venue / status': f"{row_dict.get('Year')} | {row_dict.get('Venue')}",
            'DOI / source link': row_dict.get('DOI') or row_dict.get('Publisher URL'),
            'Problem addressed': row_dict.get('Scope'),
            'Method / model': f"{row_dict.get('Method family')}: {row_dict.get('Method summary')}",
            'Dataset / test bed': row_dict.get('Dataset / testbed'),
            'Evaluation measures': 'Accuracy, F1, open-set metrics' if 'open' in row_dict.get('Scope','').lower() else 'Classification metrics',
            'Main findings': row_dict.get('Reported findings'),
            'Limitations': row_dict.get('Limitations / caveats'),
            'Adapts to change / new attacks?': row_dict.get('Unseen test?'),
            'Reading / verification status': row_dict.get('Team reading status'),
            'Source review status': row_dict.get('Source review status'),
            'Relevance': row_dict.get('Relevance'),
            'Publication status': row_dict.get('Publication status')
        }
        ismayra_papers.append(d)

print(f"Jatin papers: {len(jatin_papers)}")
print(f"Suresh papers: {len(suresh_papers)}")
print(f"Ismayra papers: {len(ismayra_papers)}")
print(f"Total: {len(jatin_papers) + len(suresh_papers) + len(ismayra_papers)}")

# Let's inspect all fields of Jatin and Suresh to see what keys they have
print("\nJatin fields:", list(jatin_papers[0].keys()))
print("Suresh fields:", list(suresh_papers[0].keys()))
