import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import docx, re
from pathlib import Path

# Create Workbook
wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# Color palettes
header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid") # Dark Navy
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
sub_header_fill = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid") # Light Blue
sub_header_font = Font(name="Calibri", size=11, bold=True, color="1F497D")

data_font = Font(name="Calibri", size=10)
bold_font = Font(name="Calibri", size=10, bold=True)
italic_font = Font(name="Calibri", size=10, italic=True)

thin_border = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

# -------------------------------------------------------------
# Sheet 1: File Inventory
# -------------------------------------------------------------
ws1 = wb.create_sheet(title="File Inventory")
ws1.views.sheetView[0].showGridLines = True

headers1 = [
    "File Index", "Relative Path", "File Name", "Extension", "Size (Bytes)", 
    "Member Owner", "Category / Scope", "Source Purpose", "Authority Level", "Open Status"
]
ws1.append(headers1)

file_inventory_data = [
    (1, "source_material/IILM_Survey_Paper_Template(1).docx", "IILM_Survey_Paper_Template(1).docx", ".docx", 90622,
     "Institutional / IILM School of CSE", "Shared Submission Baseline", 
     "Official institutional survey paper template defining layout, A4 margins (2cm), Times New Roman 10.5pt typography, section order, Block A cover page, and Block D annexure.",
     "AUTHORITATIVE FORMAT BASELINE (Highest formatting priority)", "OPENED_OK (198 paras, 23 tables)"),
    
    (2, "source_material/Jatin_Consolidated_Research_Pack.docx", "Jatin_Consolidated_Research_Pack.docx", ".docx", 51419,
     "Jatin (258100003)", "Anomaly-Based, Hybrid and Adaptive Detection", 
     "Consolidated member research pack reconciling Day 1 (9 papers) and Section Pack (8 papers) into 13 unique papers (JTN01–JTN13), with confirmed bibliographic corrections, Section IV-C draft, 5 research gaps, and future directions.",
     "AUTHORITATIVE MEMBER PACK (Jatin)", "OPENED_OK (70 paras, 16 tables)"),
    
    (3, "source_material/Suresh_Gopal_Consolidated_Research_Pack.docx", "Suresh_Gopal_Consolidated_Research_Pack.docx", ".docx", 51423,
     "Suresh Gopal Singh (258100001)", "Machine Learning and Open-Set Detection", 
     "Consolidated member research pack integrating Day 1 matrix, Day 2 draft (Intro & IV-A), and Day 3 verification audit across 9 candidate papers (SG01–SG09).",
     "AUTHORITATIVE MEMBER PACK (Suresh)", "OPENED_OK (68 paras, 13 tables)"),
    
    (4, "source_material/existing_draft_non_authoritative/IILM_Survey_Detecting_Previously_Unseen_Network_Attacks.docx", "IILM_Survey_Detecting_Previously_Unseen_Network_Attacks.docx", ".docx", 210358,
     "Team (Coordinated by Ismayra Praveen)", "Full Survey (Preliminary Draft)", 
     "Early working draft compiling a 26-paper synthesis across all three categories with pre-rendered tables and reference list [1]–[26].",
     "NON-AUTHORITATIVE WORKING REFERENCE", "OPENED_OK (169 paras, 16 tables)"),
    
    (5, "source_material/existing_draft_non_authoritative/IILM_Survey_Detecting_Previously_Unseen_Network_Attacks.pdf", "IILM_Survey_Detecting_Previously_Unseen_Network_Attacks.pdf", ".pdf", 503967,
     "Team (Coordinated by Ismayra Praveen)", "Full Survey (Preliminary Draft)", 
     "Compiled 14-page PDF rendering of the early working draft, providing visual and layout context.",
     "NON-AUTHORITATIVE WORKING REFERENCE", "OPENED_OK (14 pages)"),
    
    (6, "source_material/Ismayra_Deep_Learning_Research/ANTIGRAVITY_IMPORT_INSTRUCTIONS.txt", "ANTIGRAVITY_IMPORT_INSTRUCTIONS.txt", ".txt", 1539,
     "Ismayra Praveen (258100002)", "Deep Learning-Based Detection", 
     "Workflow guidelines specifying import rules for Ismayra's research pack, handling open-access PDFs, and preserving pending reading and verification statuses.",
     "AUTHORITATIVE PROCEDURAL GUIDANCE", "OPENED_OK (20 lines, 1537 chars)"),
    
    (7, "source_material/Ismayra_Deep_Learning_Research/Ismayra_Deep_Learning_References.bib", "Ismayra_Deep_Learning_References.bib", ".bib", 4957,
     "Ismayra Praveen (258100002)", "Deep Learning-Based Detection", 
     "Clean BibTeX database containing full bibliographic entries for 10 deep learning studies (DL01–DL10).",
     "AUTHORITATIVE BIBLIOGRAPHIC SOURCE (Ismayra)", "OPENED_OK (111 lines, 4957 chars)"),
    
    (8, "source_material/Ismayra_Deep_Learning_Research/Ismayra_Deep_Learning_Research_Matrix.xlsx", "Ismayra_Deep_Learning_Research_Matrix.xlsx", ".xlsx", 19888,
     "Ismayra Praveen (258100002)", "Deep Learning-Based Detection", 
     "Structured multi-sheet research matrix covering 10 deep learning papers (DL01–DL10), method families, unseen testing protocols, findings, limitations, and reading checklists.",
     "AUTHORITATIVE MEMBER PACK (Ismayra)", "OPENED_OK (4 sheets: Read Me, DL Papers, Method Comp, Checklist)"),
    
    (9, "source_material/Ismayra_Deep_Learning_Research/Ismayra_Deep_Learning_Research_Notes.md", "Ismayra_Deep_Learning_Research_Notes.md", ".md", 19133,
     "Ismayra Praveen (258100002)", "Deep Learning-Based Detection", 
     "Detailed analytical notes on deep learning detection, paper syntheses (DL01–DL10), research gaps, and future directions for Section IV-B.",
     "AUTHORITATIVE SYNTHESIS NOTES (Ismayra)", "OPENED_OK (164 lines, 19101 chars)"),
    
    (10, "source_material/original_member_submissions/Jatin_Day1_Literature_Review(1).docx", "Jatin_Day1_Literature_Review(1).docx", ".docx", 25033,
     "Jatin (258100003)", "Anomaly-Based, Hybrid and Adaptive Detection", 
     "Initial Day 1 literature review covering 9 candidate papers ([1]–[9]), preliminary technique summary, and initial reading declaration (only [1] read in full).",
     "AUDIT TRAIL / HISTORICAL SUBMISSION", "OPENED_OK (52 paras, 14 tables)"),
    
    (11, "source_material/original_member_submissions/Jatin_Day2_Day3_Deliverables.docx", "Jatin_Day2_Day3_Deliverables.docx", ".docx", 52966,
     "Jatin (258100003)", "Anomaly-Based, Hybrid and Adaptive Detection", 
     "Day 2/3 deliverable drafting Section IV-C, Table I, Table II, 4 research gaps, 4 future directions, draft trend chart, and declaration templates based on Day 1's 9 papers.",
     "AUDIT TRAIL / HISTORICAL SUBMISSION", "OPENED_OK (51 paras, 6 tables)"),
    
    (12, "source_material/original_member_submissions/Jatin_Literature_Matrix.xlsx", "Jatin_Literature_Matrix.xlsx", ".xlsx", 10979,
     "Jatin (258100003)", "Anomaly-Based, Hybrid and Adaptive Detection", 
     "Jatin's second literature matrix spreadsheet containing 8 papers ([J1]–[J8]), 3 reserve papers, and initial web search log with unrecorded hit counts.",
     "AUDIT TRAIL / HISTORICAL SUBMISSION", "OPENED_OK (3 sheets: Matrix, Reserve_papers, Search_log)"),
    
    (13, "source_material/original_member_submissions/Jatin_Matrix_Rows_for_Team.xlsx", "Jatin_Matrix_Rows_for_Team.xlsx", ".xlsx", 7012,
     "Jatin (258100003)", "Anomaly-Based, Hybrid and Adaptive Detection", 
     "Condensed spreadsheet extract containing Jatin's Day 1 nine-paper matrix rows intended for team matrix integration.",
     "AUDIT TRAIL / HISTORICAL SUBMISSION", "OPENED_OK (1 sheet: Matrix_Jatin)"),
    
    (14, "source_material/original_member_submissions/Jatin_Section_IVC_Gaps_Directions.docx", "Jatin_Section_IVC_Gaps_Directions.docx", ".docx", 63208,
     "Jatin (258100003)", "Anomaly-Based, Hybrid and Adaptive Detection", 
     "Jatin's Section Pack drafting Section IV-C based on the 8-paper list ([J1]–[J8]), with 5 research gaps, 5 future directions, draft trend chart, and references.",
     "AUDIT TRAIL / HISTORICAL SUBMISSION", "OPENED_OK (43 paras, 5 tables)"),
    
    (15, "source_material/original_member_submissions/Suresh_Day1_ML_OpenSet_Literature_Matrix.docx", "Suresh_Day1_ML_OpenSet_Literature_Matrix.docx", ".docx", 48198,
     "Suresh Gopal Singh (258100001)", "Machine Learning and Open-Set Detection", 
     "Suresh's Day 1 literature matrix covering 9 papers (P1–P9) drafted with AI assistance, with review questions, search log (counts not recorded), and reading status notice.",
     "AUDIT TRAIL / HISTORICAL SUBMISSION", "OPENED_OK (43 paras, 4 tables)"),
    
    (16, "source_material/original_member_submissions/Suresh_Day2_Introduction_and_Section_IV-A.docx", "Suresh_Day2_Introduction_and_Section_IV-A.docx", ".docx", 43560,
     "Suresh Gopal Singh (258100001)", "Machine Learning and Open-Set Detection", 
     "Suresh's Day 2 draft containing Section I (Introduction) and Section IV-A (Machine Learning and Open-Set Detection) with Table 1 and placeholder citations [P1]–[P9].",
     "AUDIT TRAIL / HISTORICAL SUBMISSION", "OPENED_OK (42 paras, 3 tables)"),
    
    (17, "source_material/original_member_submissions/Suresh_Day3_Verification_Report.docx", "Suresh_Day3_Verification_Report.docx", ".docx", 43184,
     "Suresh Gopal Singh (258100001)", "Machine Learning and Open-Set Detection", 
     "Rigorous verification audit checking 51 specific claims across P1–P9 against publisher records and accessible PDFs/pages (33 verified, 14 not verified or partly verified, 4 corrected).",
     "HIGHEST AUDIT AUTHORITY FOR SURESH DRAFTS", "OPENED_OK (31 paras, 2 tables)")
]

for row in file_inventory_data:
    ws1.append(row)

# -------------------------------------------------------------
# Sheet 2: Master Crosswalk (32 Unique Papers)
# -------------------------------------------------------------
ws2 = wb.create_sheet(title="Master Crosswalk")
ws2.views.sheetView[0].showGridLines = True

headers2 = [
    "Master ID", "Consolidated ID", "Member Owner", "Review Category", "Title", "Authors", 
    "Year", "Venue / Publication", "DOI / Permanent Link", "Publication Type", "Time Window (2021-2026)",
    "Unseen Attack / Drift Capability", "Datasets Used", "Evaluation Metrics", 
    "Reported Performance", "Stated / Observed Limitations", "Member Reading Status", 
    "Verification Status (Claim Audit)", "Appears In Raw Source Files"
]
ws2.append(headers2)

# Load Jatin, Suresh, Ismayra parsed papers from earlier
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

wb_ism = openpyxl.load_workbook('source_material/Ismayra_Deep_Learning_Research/Ismayra_Deep_Learning_Research_Matrix.xlsx', data_only=True)
ws_ism = wb_ism['Deep Learning Papers']
h_ism = [str(ws_ism.cell(1, c).value or '').strip() for c in range(1, ws_ism.max_column+1)]
ismayra_papers = []
for r in range(2, ws_ism.max_row+1):
    vals = [str(ws_ism.cell(r, c).value or '').strip() for c in range(1, ws_ism.max_column+1)]
    if any(vals):
        row_dict = dict(zip(h_ism, vals))
        ismayra_papers.append(row_dict)

master_rows = []
m_idx = 1

# Process Suresh papers (SG01 - SG09)
suresh_sources_map = {
    'SG01': "Suresh_Day1 (P1), Suresh_Day2 ([P1]), Suresh_Day3 (P1), Suresh_Consolidated (SG01), Existing_Draft ([1])",
    'SG02': "Suresh_Day1 (P2), Suresh_Day2 ([P2]), Suresh_Day3 (P2), Suresh_Consolidated (SG02), Existing_Draft ([3])",
    'SG03': "Suresh_Day1 (P3), Suresh_Day2 ([P3]), Suresh_Day3 (P3), Suresh_Consolidated (SG03), Existing_Draft ([4])",
    'SG04': "Suresh_Day1 (P4), Suresh_Day2 ([P4]), Suresh_Day3 (P4), Suresh_Consolidated (SG04), Existing_Draft ([5])",
    'SG05': "Suresh_Day1 (P5), Suresh_Day2 ([P5]), Suresh_Day3 (P5), Suresh_Consolidated (SG05), Existing_Draft ([7])",
    'SG06': "Suresh_Day1 (P6), Suresh_Day2 ([P6]), Suresh_Day3 (P6), Suresh_Consolidated (SG06), Existing_Draft ([8])",
    'SG07': "Suresh_Day1 (P7), Suresh_Day2 ([P7]), Suresh_Day3 (P7), Suresh_Consolidated (SG07), Existing_Draft ([9])",
    'SG08': "Suresh_Day1 (P8), Suresh_Day2 ([P8]), Suresh_Day3 (P8), Suresh_Consolidated (SG08)",
    'SG09': "Suresh_Day1 (P9), Suresh_Day2 ([P9]), Suresh_Day3 (P9), Suresh_Consolidated (SG09), Existing_Draft ([10])",
}

for p in suresh_papers:
    pid = p['Paper_ID']
    year_str = p.get('Year / venue / status', '')
    m_year = re.search(r'20\d\d', year_str)
    year = int(m_year.group(0)) if m_year else 2024
    in_win = "Yes (2021-2026)" if year >= 2021 else "No (Foundational)"
    
    pub_type = "Journal" if "vol" in year_str.lower() or "journal" in year_str.lower() or "applied sciences" in year_str.lower() or "symmetry" in year_str.lower() else ("Conference" if "proc" in year_str.lower() or "conf" in year_str.lower() or "lncs" in year_str.lower() else "Preprint")
    if "preprint" in year_str.lower() or "arxiv" in year_str.lower():
        pub_type = "Preprint (arXiv)"
        
    master_rows.append([
        f"M{m_idx:02d}", pid, p['Member'], p['Category'], p['Title'], p.get('Authors'),
        year, year_str, p.get('DOI / source link'), pub_type, in_win,
        "Open-set / Unknown class holdout" if pid in ['SG02','SG05','SG06','SG07','SG09'] else ("Unsupervised anomaly (no holdout)" if pid in ['SG03','SG04'] else ("Survey (background)" if pid=='SG01' else "Closed-set evaluation (no holdout)")),
        p.get('Dataset / test bed'), p.get('Evaluation measures'),
        p.get('Reported findings'), p.get('Limitations / critical note'),
        p.get('Reading / verification status'),
        "Day 3 Verified (Audited against source)" if pid in ['SG01','SG02','SG03','SG04','SG05','SG07','SG09'] else "Partially Verified / Discrepancy Flagged (Day 3 Report)",
        suresh_sources_map.get(pid, "Suresh Consolidated Pack")
    ])
    m_idx += 1

# Process Ismayra papers (DL01 - DL10)
ismayra_sources_map = {
    'DL01': "Ismayra_Matrix (DL01), Ismayra_Notes (DL01), Ismayra_Bib (yang2021conditional)",
    'DL02': "Ismayra_Matrix (DL02), Ismayra_Notes (DL02), Ismayra_Bib (liu2021sfe)",
    'DL03': "Ismayra_Matrix (DL03), Ismayra_Notes (DL03), Ismayra_Bib (ahmad2022deep)",
    'DL04': "Ismayra_Matrix (DL04), Ismayra_Notes (DL04), Ismayra_Bib (soltani2023adaptable), Existing_Draft ([6])",
    'DL05': "Ismayra_Matrix (DL05), Ismayra_Notes (DL05), Ismayra_Bib (hore2024sequential)",
    'DL06': "Ismayra_Matrix (DL06), Ismayra_Notes (DL06), Ismayra_Bib (zhang2024online)",
    'DL07': "Ismayra_Matrix (DL07), Ismayra_Notes (DL07), Ismayra_Bib (fang2025unknown)",
    'DL08': "Ismayra_Matrix (DL08), Ismayra_Notes (DL08), Ismayra_Bib (zhang2025unknown)",
    'DL09': "Ismayra_Matrix (DL09), Ismayra_Notes (DL09), Ismayra_Bib (yuan2026expert), Existing_Draft ([12])",
    'DL10': "Ismayra_Matrix (DL10), Ismayra_Notes (DL10), Ismayra_Bib (farhan2025network)"
}

for p in ismayra_papers:
    pid = p['ID']
    year = int(p.get('Year', 2024))
    in_win = "Yes (2021-2026)" if year >= 2021 else "No (Foundational)"
    pub_type = "Journal" if "journal" in p.get('Venue','').lower() or "transactions" in p.get('Venue','').lower() or "reports" in p.get('Venue','').lower() or "computers & security" in p.get('Venue','').lower() or "concurrency" in p.get('Venue','').lower() else ("Conference" if "conference" in p.get('Venue','').lower() or "iccea" in p.get('Venue','').lower() else "Journal")
    
    master_rows.append([
        f"M{m_idx:02d}", pid, "Ismayra Praveen (258100002)", "Deep Learning-Based Detection",
        p.get('Title'), p.get('Authors'), year, p.get('Venue'),
        p.get('DOI') or p.get('Publisher URL'), pub_type, in_win,
        p.get('Unseen test?'), p.get('Dataset / testbed'),
        "Accuracy, F1, open-set / ROC metrics",
        p.get('Reported findings'), p.get('Limitations / caveats'),
        p.get('Team reading status'),
        p.get('Source review status'),
        ismayra_sources_map.get(pid, "Ismayra Research Pack")
    ])
    m_idx += 1

# Process Jatin papers (JTN01 - JTN13)
jatin_sources_map = {
    'JTN01': "Jatin_Lit_Matrix (J1), Jatin_Section_Pack (J1), Jatin_Consolidated (JTN01), Existing_Draft ([2])",
    'JTN02': "Jatin_Lit_Matrix (J2), Jatin_Section_Pack (J2), Jatin_Consolidated (JTN02)",
    'JTN03': "Jatin_Lit_Matrix (J3), Jatin_Section_Pack (J3), Jatin_Consolidated (JTN03), Existing_Draft ([17])",
    'JTN04': "Jatin_Day1 ([2]), Jatin_Team_Rows (2), Jatin_Day2_3 ([2]), Jatin_Lit_Matrix (J4), Jatin_Section_Pack (J4), Jatin_Consolidated (JTN04), Existing_Draft ([21])",
    'JTN05': "Jatin_Day1 ([3]), Jatin_Team_Rows (3), Jatin_Day2_3 ([3]), Jatin_Lit_Matrix (J5), Jatin_Section_Pack (J5), Jatin_Consolidated (JTN05), Existing_Draft ([22])",
    'JTN06': "Jatin_Day1 ([9]), Jatin_Team_Rows (9), Jatin_Day2_3 ([9]), Jatin_Lit_Matrix (J6), Jatin_Section_Pack (J6), Jatin_Consolidated (JTN06), Existing_Draft ([19])",
    'JTN07': "Jatin_Lit_Matrix (J7), Jatin_Section_Pack (J7), Jatin_Consolidated (JTN07), Existing_Draft ([11])",
    'JTN08': "Jatin_Day1 ([5]), Jatin_Team_Rows (5), Jatin_Day2_3 ([5]), Jatin_Lit_Matrix (J8), Jatin_Section_Pack (J8), Jatin_Consolidated (JTN08), Existing_Draft ([23])",
    'JTN09': "Jatin_Day1 ([1]), Jatin_Team_Rows (1), Jatin_Day2_3 ([1]), Jatin_Consolidated (JTN09), Existing_Draft ([18])",
    'JTN10': "Jatin_Day1 ([4]), Jatin_Team_Rows (4), Jatin_Day2_3 ([4]), Jatin_Lit_Matrix (Reserve), Jatin_Consolidated (JTN10), Existing_Draft ([24])",
    'JTN11': "Jatin_Day1 ([6]), Jatin_Team_Rows (6), Jatin_Day2_3 ([6]), Jatin_Consolidated (JTN11), Existing_Draft ([16])",
    'JTN12': "Jatin_Day1 ([7]), Jatin_Team_Rows (7), Jatin_Day2_3 ([7]), Jatin_Consolidated (JTN12), Existing_Draft ([15])",
    'JTN13': "Jatin_Day1 ([8]), Jatin_Team_Rows (8), Jatin_Day2_3 ([8]), Jatin_Consolidated (JTN13), Existing_Draft ([20])"
}

for p in jatin_papers:
    pid = p['Paper_ID']
    year_str = p.get('Year / venue / status', '')
    m_year = re.search(r'20\d\d', year_str)
    year = int(m_year.group(0)) if m_year else (2018 if pid=='JTN01' else 2020)
    in_win = "Yes (2021-2026)" if year >= 2021 else "No (Foundational)"
    
    pub_type = "Journal" if "vol" in year_str.lower() or "journal" in year_str.lower() or "symmetry" in year_str.lower() or "electronics" in year_str.lower() or "advances" in year_str.lower() or "systems" in year_str.lower() or "computer networks" in year_str.lower() or "frontiers" in year_str.lower() or "transactions" in year_str.lower() else ("Conference" if "proc" in year_str.lower() or "ndss" in year_str.lower() or "acsac" in year_str.lower() else "Preprint")
    if "preprint" in year_str.lower() or "arxiv" in year_str.lower():
        pub_type = "Preprint (arXiv)"
        
    master_rows.append([
        f"M{m_idx:02d}", pid, p['Member'], p['Category'], p['Title'], p.get('Authors'),
        year, year_str, p.get('DOI / source link'), pub_type, in_win,
        "Incremental online / drift" if pid in ['JTN01','JTN04','JTN05','JTN08','JTN10'] else ("Unseen class holdout (static)" if pid=='JTN09' else ("Statistical / Entropy (no drift)" if pid in ['JTN11','JTN12'] else "Hybrid ensemble")),
        p.get('Dataset / test bed'), p.get('Evaluation measures'),
        p.get('Reported findings'), p.get('Limitations / critical note'),
        p.get('Reading / verification status'),
        "Verified from full text (Day 1 read in full)" if pid=='JTN09' else ("Partially Verified (Abstract + method read)" if pid=='JTN08' else "Unverified / Pending full-text audit ([VERIFY])"),
        jatin_sources_map.get(pid, "Jatin Consolidated Pack")
    ])
    m_idx += 1

for row in master_rows:
    ws2.append(row)

# -------------------------------------------------------------
# Sheet 3: Duplicate Analysis
# -------------------------------------------------------------
ws3 = wb.create_sheet(title="Duplicate Analysis")
ws3.views.sheetView[0].showGridLines = True

headers3 = [
    "Reconciliation Type", "Item / Work Title", "Source 1 & Identifier", "Source 2 & Identifier", 
    "DOI / Match Key", "Overlap Resolution / Reconciliation Action"
]
ws3.append(headers3)

duplicate_analysis_data = [
    ("Cross-Member Duplicate Check", "All candidate papers across Jatin (13), Suresh (9), and Ismayra (10)", 
     "Jatin Consolidated Pack (JTN01–JTN13)", "Suresh Consolidated Pack (SG01–SG09) & Ismayra Matrix (DL01–DL10)",
     "Matched by DOI, arXiv ID, and normalized title", 
     "ZERO cross-member duplicates identified across the 32 candidate papers. Each member submission covers a distinct set of studies tailored to their assigned category."),
    
    ("Internal Member Reconciliation (Jatin)", "Learn to Adapt: Robust Drift Detection in Security Domain",
     "Jatin Day 1 Review & Team Rows: Ref [2]", "Jatin Literature Matrix & Section Pack: Ref [J4]",
     "10.1016/j.compeleceng.2022.108239 (arXiv:2206.07581)",
     "DUPLICATE RESOLVED: Merged into single master entry JTN04 (Master ID M23). Volume 102 and open-access status confirmed in consolidated pack."),
    
    ("Internal Member Reconciliation (Jatin)", "ENIDrift: A Fast and Adaptive Ensemble System for Network Intrusion Detection under Real-world Drift",
     "Jatin Day 1 Review & Team Rows: Ref [3]", "Jatin Literature Matrix & Section Pack: Ref [J5]",
     "10.1145/3564625.3567992",
     "DUPLICATE RESOLVED: Merged into single master entry JTN05 (Master ID M24). Page range confirmed as pp. 785–789 in consolidated pack."),
    
    ("Internal Member Reconciliation (Jatin)", "Assessing the Impact of a Supervised Classification Filter on Flow-based Hybrid Network Anomaly Detection",
     "Jatin Day 1 Review & Team Rows: Ref [9]", "Jatin Literature Matrix & Section Pack: Ref [J6]",
     "arXiv:2310.06656",
     "DUPLICATE RESOLVED: Merged into single master entry JTN06 (Master ID M25). Dataset identified as UGR'16 flow data in consolidated pack."),
    
    ("Internal Member Reconciliation (Jatin)", "Continual Learning with Strategic Selection and Forgetting for Network Intrusion Detection",
     "Jatin Day 1 Review & Team Rows: Ref [5]", "Jatin Literature Matrix & Section Pack: Ref [J8]",
     "arXiv:2412.16264 (INFOCOM 2025)",
     "DUPLICATE RESOLVED: Merged into single master entry JTN08 (Master ID M27). Retained as preprint in Jatin pack; INFOCOM DOI noted in later drafts."),
    
    ("Internal Member Reconciliation (Jatin)", "Concept Drift-Based Intrusion Detection for Evolving Data Stream Classification in IDS",
     "Jatin Day 1 Review & Team Rows: Ref [4]", "Jatin Literature Matrix: Sheet 'Reserve_papers' (Row 4)",
     "10.1093/comjnl/bxae023",
     "DUPLICATE RESOLVED: Seth et al. was listed as Ref [4] on Day 1 but placed in reserve on Day 2; consolidated pack retains it as core entry JTN10 (Master ID M29)."),
    
    ("Foundational Pre-2021 Separation (Jatin)", "Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection",
     "Jatin Literature Matrix & Section Pack: Ref [J1]", "Jatin Consolidated Pack: Ref JTN01",
     "10.14722/ndss.2018.23204 (arXiv:1802.09089)",
     "LABELLED FOUNDATIONAL: Published in 2018 (outside the 2021–2026 5-year window). Retained as seminal online autoencoder baseline, not counted towards recent 15."),
    
    ("Foundational Pre-2021 Separation (Jatin)", "HELAD: A Novel Network Anomaly Detection Model Based on Heterogeneous Ensemble Learning",
     "Jatin Literature Matrix & Section Pack: Ref [J2]", "Jatin Consolidated Pack: Ref JTN02",
     "10.1016/j.comnet.2019.107049",
     "LABELLED FOUNDATIONAL: Published in 2020 (outside the 2021–2026 5-year window). Retained as seminal heterogeneous ensemble baseline, not counted towards recent 15."),
    
    ("Reserve Candidate Tracking (Jatin)", "Network anomaly detection via similarity-aware ensemble learning with ADSim (Chen et al. 2024)",
     "Jatin Literature Matrix: Sheet 'Reserve_papers' (Row 2)", "Existing Draft: Ref [26]",
     "10.1016/j.comnet.2024.110423",
     "RESERVE CANDIDATE: Maintained in reserve pool. Added to draft references [26]; distinct from JTN01–JTN13."),
    
    ("Reserve Candidate Tracking (Jatin)", "Generative Active Adaptation for Drifting and Imbalanced Network Intrusion Detection (NetGuard) (Gupta et al. 2025)",
     "Jatin Literature Matrix: Sheet 'Reserve_papers' (Row 3)", "Existing Draft: Ref [25]",
     "arXiv:2503.03022",
     "RESERVE CANDIDATE: Maintained in reserve pool. Added to draft references [25]; distinct from JTN01–JTN13."),
    
    ("Existing Draft Synthesis Crosswalk", "Existing Working Draft 26-Reference Set vs Consolidated 32-Paper Master Set",
     "Existing Draft DOCX/PDF: References [1]–[26]", "Master Crosswalk: 32 Candidate Papers",
     "DOI / Author matching",
     "22 of the 26 references in the draft map directly to the 32 master papers. 4 references in the draft represent additional sources: [13] Martins et al. 2025 (SLR), [14] Neto et al. 2025 (Survey), [25] NetGuard 2025 (Jatin reserve), [26] ADSim 2024 (Jatin reserve). 10 papers in the master pack (DL01, DL02, DL03, DL05, DL06, DL07, DL08, DL10, SG08, JTN02) provide rich expansion capacity.")
]

for row in duplicate_analysis_data:
    ws3.append(row)

# -------------------------------------------------------------
# Sheet 4: Claim Verification & Conflicts
# -------------------------------------------------------------
ws4 = wb.create_sheet(title="Claim Verification & Conflicts")
ws4.views.sheetView[0].showGridLines = True

headers4 = [
    "Paper ID", "Member", "Claim Subject", "Older Draft Claim", "Later Verification / Actual Source Finding", 
    "Status Result", "Required Reconciliation Action"
]
ws4.append(headers4)

doc3 = docx.Document('source_material/original_member_submissions/Suresh_Day3_Verification_Report.docx')
t_claims = doc3.tables[0]
suresh_claim_rows = []
for r in t_claims.rows[1:]:
    ref = r.cells[0].text.strip()
    claim = r.cells[1].text.strip()
    source = r.cells[2].text.strip()
    res = r.cells[3].text.strip()
    act = r.cells[4].text.strip()
    ws4.append([ref, "Suresh Gopal Singh", claim, "Stated in Day 1 / Day 2", f"Checked against {source}: {act}", res, act])

# Add Jatin and Ismayra specific verification / conflict items
additional_claim_rows = [
    ("JTN05 / ENIDrift", "Jatin", "Publication Page Range", "ACSAC 2022, pp. 785– (Day 1 / Section Pack)", "ACSAC 2022 proceedings, pp. 785–789", "Verified & Corrected", "Use exact range pp. 785–789 in final references."),
    ("JTN04 / Kuppa", "Jatin", "Journal Volume & Number", "Comput. Electr. Eng. (vol to confirm)", "Computers & Electrical Engineering, vol. 102, article 108239", "Verified & Corrected", "Add vol. 102 to reference."),
    ("JTN03 / Kwon", "Jatin", "Article DOI & Metadata", "Search MDPI Electronics 2022, 11(6), 867", "DOI confirmed: 10.3390/electronics11060867", "Verified & Corrected", "Full DOI recorded in consolidated pack."),
    ("JTN06 / Macko", "Jatin", "Dataset Name", "Real large-scale network traffic (name to confirm)", "UGR'16 flow-based network traffic dataset", "Verified & Corrected", "Record UGR'16 dataset in matrix."),
    ("JTN11 / Ibrahim", "Jatin", "Article Page Range", "CSIS vol. 19, no. 1 (pages to confirm)", "Computer Science and Information Systems, vol. 19, no. 1, pp. 87–116", "Verified & Corrected", "Add pp. 87–116 to citation."),
    ("JTN12 / Timcenko", "Jatin", "Article Page Range", "AECE vol. 21, no. 4 (pages 51–60)", "Advances in Electrical and Computer Engineering, vol. 21, no. 4, pp. 51–60", "Verified", "Confirmed from journal record."),
    ("DL06 / Z. Zhang", "Ismayra", "Scope Classification", "Concept drift detection with KSWIN", "FT-Transformer adaptation to concept drift; unknown-attack holdout not proven", "Flagged Caveat", "Mark as drift-adaptation rather than verified open-set unseen-attack testing."),
    ("DL10 / Farhan", "Ismayra", "Relevance & Scope", "Deep learning NIDS on UNSW-NB15", "Binary/multiclass split on UNSW-NB15 with SMOTE; no held-out attack classes", "Contextual Baseline Only", "Do not cite as evidence of unknown/zero-day detection; keep as contextual baseline only."),
    ("DL07 / Fang", "Ismayra", "Full Text Access", "Scientific Reports 2025", "Full open-access article available via PMC (PMC12081525)", "Fully Accessible OA", "Download open-access PDF into research-papers/original_pdfs/."),
    ("DL05 / Hore", "Ismayra", "Full Text Access", "Computers & Security 2024", "Creative Commons open-access article via ScienceDirect", "Fully Accessible OA", "Verify open-access licence and store permitted copy.")
]

for row in additional_claim_rows:
    ws4.append(row)

# -------------------------------------------------------------
# Sheet 5: Missing Inputs & Readiness
# -------------------------------------------------------------
ws5 = wb.create_sheet(title="Missing Inputs & Readiness")
ws5.views.sheetView[0].showGridLines = True

headers5 = [
    "Requirement Category", "Required Field / Item", "Template / Institutional Rule", 
    "Current Status in Workspace", "Source Authority / Origin", "Action Required for Final Paper"
]
ws5.append(headers5)

missing_inputs_data = [
    ("Cover Page (Block A)", "Course Title", "Template Table 0: Course Title", "PENDING ([ Course Title ] placeholder)", "IILM Official Template", "Obtain exact course title from course coordinator / faculty supervisor."),
    ("Cover Page (Block A)", "Course Code", "Template Table 0: Course Code", "PENDING ([ Course Code ] placeholder)", "IILM Official Template", "Obtain exact course code from course coordinator."),
    ("Cover Page (Block A)", "Programme and Semester", "Template Table 0: Programme and Semester", "Draft has 'B.Tech. (CSE - AI & ML), Semester III'", "Existing Draft Table 0", "Confirm semester and specialization with Ismayra / team."),
    ("Cover Page (Block A)", "Batch and Session", "Template Table 0: Batch and Session", "Draft has 'Batch 2025-2029, Session 2026-2027'", "Existing Draft Table 0", "Confirm academic session details."),
    ("Cover Page (Block A)", "Assessment Component", "Template Table 0: Assessment Component", "Project (End Semester Evaluation)", "IILM Official Template", "Confirm whether specific marks (e.g. 100 Marks) should be stated."),
    ("Cover Page (Block A)", "Team Number", "Template Table 0: Team Number", "PENDING ([ T-00 ] / [Confirm team number])", "IILM Official Template", "Obtain official allocated team number (e.g., T-05)."),
    ("Cover Page (Block A)", "Student Institute Emails", "Template Table 1: Institute E-mail", "PENDING ([Insert institute email] for all 3 members)", "IILM Official Template", "Collect @iilm.edu student email addresses for Ismayra, Suresh, and Jatin."),
    ("Cover Page (Block A)", "Faculty Supervisor Name", "Template Table 2: Name", "PENDING ([Dr. / Mr. / Ms. Full Name])", "IILM Official Template", "Confirm faculty supervisor name; do NOT copy sample supervisor."),
    ("Cover Page (Block A)", "Faculty Designation & Dept", "Template Table 2: Designation and Department", "PENDING ([Designation], School of CSE)", "IILM Official Template", "Confirm designation of the allocated faculty supervisor."),
    ("Cover Page (Block A)", "Course Coordinator Name", "Template Table 2: Course Coordinator", "PENDING ([Insert course coordinator name])", "IILM Official Template", "Confirm name of the Course Coordinator."),
    ("Cover Page (Block A)", "Evidence Repository URL", "Template Cover Page & Annexure", "https://github.com/ismayra-devx/detecting-previously-unseen-network-attacks.git", "User Request / Git URL", "Verify public accessibility and push evidence files prior to evaluation."),
    ("Cover Page (Block A)", "Date of Submission", "Template Cover Page: Date of Submission", "PENDING ([ DD Month YYYY ] or November 2026)", "IILM Official Template", "Confirm exact submission date (e.g., 20 November 2026)."),
    ("Annexure (Block D)", "Works Read Count per Member", "Template Table 20: Works read", "Only 1 paper read in full by Jatin; Suresh verified 51 claims; Ismayra pending", "Member Declarations", "Members must personally read their assigned papers before signing actual read counts."),
    ("Annexure (Block D)", "Search String Hit Counts", "Template Table 22 / Selection Flow Figure", "PENDING (Day 1 web search hit counts 'not recorded')", "Member Search Logs", "Execute repeat queries in IEEE Xplore, ACM DL, SpringerLink, Google Scholar, arXiv with recorded dates and counts."),
    ("Annexure (Block D)", "Member Signatures", "Template Tables 20 & 21: Signatures", "PENDING (Physical / digital signatures required for final submission)", "IILM Official Template", "Sign contribution and AI-use declarations upon verified reading completion."),
    ("Survey Body (Block C)", "Publication Trend Chart", "Template Figure 3 & Section V", "Preliminary charts exist for individual members; full team chart pending", "Consolidated Packs", "Generate unified publication trend chart from the 32-paper master matrix."),
    ("Survey Body (Block C)", "Selection Flow Diagram", "Template Figure 1 & Section II", "Draft flowchart exists with estimated screening counts", "Existing Draft Fig. 1", "Update flowchart numbers to match the executed search log hit counts."),
    ("Survey Body (Block C)", "Taxonomy Figure", "Template Figure 2 & Section III", "3-category taxonomy (ML/Open-Set, Deep Learning, Anomaly/Hybrid/Adaptive)", "Consolidated Packs", "Generate clean taxonomy diagram reflecting all three sub-domains.")
]

for row in missing_inputs_data:
    ws5.append(row)

# Apply Styling to all sheets
for ws in wb.worksheets:
    # Header row
    for col_num in range(1, ws.max_column + 1):
        cell = ws.cell(row=1, column=col_num)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 28
    
    # Data rows
    for row_num in range(2, ws.max_row + 1):
        ws.row_dimensions[row_num].height = 20
        for col_num in range(1, ws.max_column + 1):
            cell = ws.cell(row=row_num, column=col_num)
            cell.font = data_font
            cell.border = thin_border
            # Left align text, center codes/IDs/numbers
            val_str = str(cell.value or '')
            if col_num in [1, 4, 7, 10, 11] and len(val_str) < 20:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=False)
                
    # Auto-fit column widths
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            val_str = str(cell.value or '')
            if '\n' in val_str:
                val_str = max(val_str.split('\n'), key=len)
            max_len = max(max_len, len(val_str))
        ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 50)

# Save Workbook
wb.save("source-to-paper crosswalk.xlsx")
print("source-to-paper crosswalk.xlsx generated successfully!")
