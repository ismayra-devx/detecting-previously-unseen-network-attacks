import docx

doc = docx.Document('source_material/existing_draft_non_authoritative/IILM_Survey_Detecting_Previously_Unseen_Network_Attacks.docx')

print("=== EXISTING DRAFT COVER PAGE TABLES ===")
for i in [0, 1, 2]:
    t = doc.tables[i]
    print(f"--- Table {i} ---")
    for r in t.rows:
        print(" | ".join([c.text.strip().replace("\n", " ") for c in r.cells]))

print("\n=== EXISTING DRAFT ANNEXURE TABLES ===")
for i in [13, 14, 15]:
    t = doc.tables[i]
    print(f"--- Table {i} ---")
    for r in t.rows:
        print(" | ".join([c.text.strip().replace("\n", " ") for c in r.cells]))

print("\n=== ALL 26 REFERENCES IN EXISTING DRAFT ===")
in_refs = False
for p in doc.paragraphs:
    t = p.text.strip()
    if 'REFERENCES' in t.upper():
        in_refs = True
        continue
    if in_refs:
        if t.startswith('[') and ']' in t:
            print(t)
        elif t.startswith('ANNEXURE'):
            break
