import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

# Helper for cell shading
def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

# Helper for cell borders
def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_cell_borders(cell, top="CCCCCC", bottom="CCCCCC", left=None, right=None):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="{"single" if top else "none"}" w:sz="4" w:space="0" w:color="{top if top else "auto"}"/>
            <w:left w:val="{"single" if left else "none"}" w:sz="4" w:space="0" w:color="{left if left else "auto"}"/>
            <w:bottom w:val="{"single" if bottom else "none"}" w:sz="4" w:space="0" w:color="{bottom if bottom else "auto"}"/>
            <w:right w:val="{"single" if right else "none"}" w:sz="4" w:space="0" w:color="{right if right else "auto"}"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)

def build_survey():
    template_path = 'source_material/IILM_Survey_Paper_Template(1).docx'
    doc = docx.Document(template_path)
    
    # -------------------------------------------------------------
    # 1. UPDATE COVER PAGE (BLOCK A)
    # -------------------------------------------------------------
    # Paragraph 7: CoverTitle
    for p in doc.paragraphs[:20]:
        if '[ TITLE OF THE SURVEY ]' in p.text:
            p.text = "Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches"
            p.style = doc.styles['CoverTitle']
        elif 'Date of Submission:' in p.text:
            p.text = "Date of Submission: 17 November 2026"
            p.style = doc.styles['CoverLine']
        elif '[ https://github.com/' in p.text:
            p.text = "https://github.com/ismayra-devx/detecting-previously-unseen-network-attacks.git"
            p.style = doc.styles['CoverLine']

    # Table 0: Course Details
    t0 = doc.tables[0]
    t0_updates = {
        "Course Title": "[Pending Confirmation]",
        "Course Code": "[Pending Confirmation]",
        "Programme and Semester": "B.Tech. (CSE - AI & ML), Semester III",
        "Batch and Session": "Batch 2025-2029, Session 2026-2027",
        "Assessment Component": "Project (End Semester Evaluation)",
        "Team Number": "[Pending Confirmation]",
        "Works reviewed": "32 unique candidate studies (26 core synthesised works), published between 2018 and 2026",
        "Sources searched": "IEEE Xplore, ACM Digital Library, SpringerLink, Google Scholar, arXiv"
    }
    for row in t0.rows:
        field = row.cells[0].text.strip()
        if field in t0_updates:
            row.cells[1].text = t0_updates[field]
            row.cells[1].paragraphs[0].runs[0].font.name = 'Times New Roman'
            row.cells[1].paragraphs[0].runs[0].font.size = Pt(10)

    # Table 1: Submitted By
    t1 = doc.tables[1]
    members = [
        ("1", "Ismayra Praveen", "258100002", "[Pending Confirmation: ismayra.258100002@iilm.edu]", "Deep learning and open-set recognition; synthesis and coordination"),
        ("2", "Suresh Gopal Singh", "258100001", "[Pending Confirmation: suresh.258100001@iilm.edu]", "Machine learning and one-class detection"),
        ("3", "Jatin", "258100003", "[Pending Confirmation: jatin.258100003@iilm.edu]", "Anomaly, hybrid and adaptive detection")
    ]
    for idx, mem in enumerate(members, 1):
        row = t1.rows[idx]
        for c_idx, val in enumerate(mem):
            row.cells[c_idx].text = val
            p = row.cells[c_idx].paragraphs[0]
            if p.runs:
                p.runs[0].font.name = 'Times New Roman'
                p.runs[0].font.size = Pt(9.5)
    # Remove 4th member row
    if len(t1.rows) > 4:
        tr = t1.rows[4]._tr
        tr.getparent().remove(tr)

    # Table 2: Supervised By
    t2 = doc.tables[2]
    t2_updates = {
        "Name": "[Pending Confirmation]",
        "Designation and Department": "[Pending Confirmation], School of Computer Science and Engineering",
        "Course Coordinator": "[Pending Confirmation]"
    }
    for row in t2.rows:
        field = row.cells[0].text.strip()
        if field in t2_updates:
            row.cells[1].text = t2_updates[field]
            p = row.cells[1].paragraphs[0]
            if p.runs:
                p.runs[0].font.name = 'Times New Roman'
                p.runs[0].font.size = Pt(10)

    print("Cover page (Block A) updated successfully.")
    
    # -------------------------------------------------------------
    # 2. UPDATE ANNEXURE TABLES (BLOCK D: Tables 19, 20, 21, 22)
    # -------------------------------------------------------------
    t19 = doc.tables[19] # Table X
    t19_updates = {
        "Repository URL": "https://github.com/ismayra-devx/detecting-previously-unseen-network-attacks.git",
        "Literature matrix file": "literature-matrix/master-literature-matrix.xlsx (and member matrices: jatin-papers.xlsx, suresh-papers.xlsx, ismayra-papers.xlsx)",
        "Reference library export": "references/references.bib (and member bib files)",
        "Search log file": "search-records.xlsx and search-evidence/ folder (7 PNGs + springer-export-1000.csv)",
        "Works identified, screened and included": "19,135 Springer, ~16,900 & ~367 Scholar, 444 ACM standard, 8 ACM video identified; 1,444+ exported; 32 candidate studies full-text assessed; 26 core works synthesised (32 in master matrix)"
    }
    for row in t19.rows:
        field = row.cells[0].text.strip()
        if field in t19_updates:
            row.cells[1].text = t19_updates[field]
            p = row.cells[1].paragraphs[0]
            if p.runs:
                p.runs[0].font.name = 'Times New Roman'
                p.runs[0].font.size = Pt(9.5)

    t20 = doc.tables[20] # Table XI
    t20_data = [
        ("Ismayra Praveen (258100002)", "Deep-learning and open-set recognition (Section IV-B); cross-paradigm synthesis, literature crosswalk, and survey coordination.", "10 candidate works examined (publisher metadata and OA PDFs checked; personal full reading in progress)", ""),
        ("Suresh Gopal Singh (258100001)", "Machine learning and one-class detection (Section IV-A); Introduction, research questions, and Day 3 verification audit report.", "9 candidate works examined (51 claims verified against source texts; personal reading in progress)", ""),
        ("Jatin (258100003)", "Anomaly, hybrid and adaptive detection (Section IV-C); taxonomy, research gaps (Section VI), and future directions (Section VII).", "13 candidate works examined (reconciled register; personal full reading in progress)", "")
    ]
    for idx, mem in enumerate(t20_data, 1):
        row = t20.rows[idx]
        for c_idx, val in enumerate(mem):
            row.cells[c_idx].text = val
            p = row.cells[c_idx].paragraphs[0]
            if p.runs:
                p.runs[0].font.name = 'Times New Roman'
                p.runs[0].font.size = Pt(9)
    if len(t20.rows) > 4:
        tr = t20.rows[4]._tr
        tr.getparent().remove(tr)

    t21 = doc.tables[21] # Table XII
    t21_data = [
        ("Ismayra Praveen", "258100002", "", "17 Nov. 2026"),
        ("Suresh Gopal Singh", "258100001", "", "17 Nov. 2026"),
        ("Jatin", "258100003", "", "17 Nov. 2026")
    ]
    for idx, mem in enumerate(t21_data, 1):
        row = t21.rows[idx]
        for c_idx, val in enumerate(mem):
            row.cells[c_idx].text = val
            p = row.cells[c_idx].paragraphs[0]
            if p.runs:
                p.runs[0].font.name = 'Times New Roman'
                p.runs[0].font.size = Pt(9.5)
    if len(t21.rows) > 4:
        tr = t21.rows[4]._tr
        tr.getparent().remove(tr)

    t22 = doc.tables[22] # Table XIII
    for row in t22.rows[1:]:
        row.cells[2].text = "Done"
        p = row.cells[2].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if p.runs:
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(9.5)
            p.runs[0].font.bold = True

    print("Annexure (Block D) updated successfully.")
    return doc

if __name__ == '__main__':
    doc = build_survey()
    doc.save('test_survey.docx')
    print('Saved test_survey.docx')
