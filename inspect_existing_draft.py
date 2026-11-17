import docx, re

doc = docx.Document('source_material/existing_draft_non_authoritative/IILM_Survey_Detecting_Previously_Unseen_Network_Attacks.docx')
print(f"Existing draft paragraphs: {len(doc.paragraphs)}, tables: {len(doc.tables)}")

# Check references in existing draft
refs = []
in_refs = False
for p in doc.paragraphs:
    t = p.text.strip()
    if 'REFERENCES' in t.upper() or 'BIBLIOGRAPHY' in t.upper():
        in_refs = True
        continue
    if in_refs:
        if t.startswith('[') and ']' in t:
            refs.append(t)
        elif t and len(refs) > 0 and not t.startswith('ANNEXURE'):
            # continuation or new ref
            if t.startswith('['):
                refs.append(t)

print(f"Total references found in existing draft: {len(refs)}")
for r in refs[:10]:
    print(r[:100])

# Also check tables in existing draft
for i, t in enumerate(doc.tables):
    title = t.rows[0].cells[0].text.strip().replace('\n', ' ') if len(t.rows)>0 else ''
    print(f"Table {i}: {len(t.rows)}x{len(t.columns)} | {title[:60]}")
