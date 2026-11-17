import docx, openpyxl, re
from pathlib import Path

# Load Jatin consolidated papers
doc_j = docx.Document('source_material/Jatin_Consolidated_Research_Pack.docx')
headings_j = [p.text.strip() for p in doc_j.paragraphs if p.text.strip().startswith('JTN')]
jatin_list = []
for i in range(1, 14):
    t = doc_j.tables[i]
    d = {r.cells[0].text.strip(): r.cells[1].text.strip() for r in t.rows}
    title = headings_j[i-1].split('.', 1)[1].strip() if i-1 < len(headings_j) else f'JTN{i:02d}'
    d['id'] = f'JTN{i:02d}'
    d['title'] = title
    d['member'] = 'Jatin'
    jatin_list.append(d)

# Load Suresh consolidated papers
doc_s = docx.Document('source_material/Suresh_Gopal_Consolidated_Research_Pack.docx')
headings_s = [p.text.strip() for p in doc_s.paragraphs if p.text.strip().startswith('SG')]
suresh_list = []
for i in range(1, 10):
    t = doc_s.tables[i]
    d = {r.cells[0].text.strip(): r.cells[1].text.strip() for r in t.rows}
    title = headings_s[i-1].split('.', 1)[1].strip() if i-1 < len(headings_s) else f'SG{i:02d}'
    d['id'] = f'SG{i:02d}'
    d['title'] = title
    d['member'] = 'Suresh'
    suresh_list.append(d)

# Load Ismayra papers
wb = openpyxl.load_workbook('source_material/Ismayra_Deep_Learning_Research/Ismayra_Deep_Learning_Research_Matrix.xlsx', data_only=True)
ws = wb['Deep Learning Papers']
headers = [str(ws.cell(1, c).value or '').strip() for c in range(1, ws.max_column+1)]
ismayra_list = []
for r in range(2, ws.max_row+1):
    vals = [str(ws.cell(r, c).value or '').strip() for c in range(1, ws.max_column+1)]
    if any(vals):
        row_dict = dict(zip(headers, vals))
        d = {
            'id': row_dict['ID'],
            'title': row_dict['Title'],
            'Authors': row_dict['Authors'],
            'DOI / source link': row_dict.get('DOI') or row_dict.get('Publisher URL'),
            'Year / venue / status': f"{row_dict.get('Year')} {row_dict.get('Venue')}",
            'Reading / verification status': row_dict.get('Team reading status'),
            'member': 'Ismayra'
        }
        ismayra_list.append(d)

print(f"Counts: Jatin={len(jatin_list)}, Suresh={len(suresh_list)}, Ismayra={len(ismayra_list)}")

all_papers = jatin_list + suresh_list + ismayra_list

def norm(s):
    if not s: return ''
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s

def extract_doi(s):
    if not s: return ''
    m = re.search(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+', s)
    if m:
        doi = m.group(0).rstrip('.;,')
        return doi.lower()
    m2 = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', s, re.I)
    if m2:
        return f"arxiv:{m2.group(1)}"
    return ''

matches = []
for i in range(len(all_papers)):
    p1 = all_papers[i]
    doi1 = extract_doi(p1.get('DOI / source link', ''))
    t1 = norm(p1.get('title', ''))
    for j in range(i+1, len(all_papers)):
        p2 = all_papers[j]
        doi2 = extract_doi(p2.get('DOI / source link', ''))
        t2 = norm(p2.get('title', ''))
        
        doi_match = bool(doi1 and doi2 and doi1 == doi2)
        title_match = bool(t1 and t2 and (t1 == t2 or (len(t1) > 20 and len(t2) > 20 and (t1 in t2 or t2 in t1))))
        
        if doi_match or title_match:
            matches.append((p1, p2, doi_match, title_match, doi1, doi2))

print(f"Total cross-member matches found: {len(matches)}")
for p1, p2, dm, tm, d1, d2 in matches:
    print(f"MATCH: [{p1['member']} {p1['id']}] '{p1['title'][:40]}' <==> [{p2['member']} {p2['id']}] '{p2['title'][:40]}'")
    print(f"   DOI Match: {dm} ({d1} vs {d2}) | Title Match: {tm}")

# Also check reserve papers in Jatin's files or original submissions
