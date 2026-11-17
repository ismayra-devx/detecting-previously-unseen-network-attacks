import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb_src = openpyxl.load_workbook('source-to-paper crosswalk.xlsx')
ws_src = wb_src['Master Crosswalk']

wb_out = openpyxl.Workbook()
wb_out.remove(wb_out.active)

# Styling palette
font_title = Font(name="Calibri", size=15, bold=True, color="1E293B")
font_subtitle = Font(name="Calibri", size=10, italic=True, color="475569")
font_header = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
font_regular = Font(name="Calibri", size=9.5, color="0F172A")
font_mono = Font(name="Consolas", size=9, color="0F172A")
font_bold = Font(name="Calibri", size=9.5, bold=True, color="0F172A")
font_pre2021 = Font(name="Calibri", size=9.5, bold=True, color="B45309")
font_recent = Font(name="Calibri", size=9.5, bold=True, color="15803D")

fill_header = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
thin_border = Border(
    left=Side(border_style="thin", color="CBD5E1"),
    right=Side(border_style="thin", color="CBD5E1"),
    top=Side(border_style="thin", color="CBD5E1"),
    bottom=Side(border_style="thin", color="CBD5E1")
)

# SHEET 1: Master Literature Matrix
ws1 = wb_out.create_sheet(title="Master Literature Matrix")
ws1.views.sheetView[0].showGridLines = True

ws1.cell(row=1, column=1, value="MASTER LITERATURE MATRIX — COMPLETE EVIDENCE REGISTER").font = font_title
ws1.cell(row=2, column=1, value="Project: IILM Survey Paper — Detecting Previously Unseen Network Attacks | 32 Unique Studies Across Three Member Packs").font = font_subtitle

headers = [
    "Master ID", "Member ID", "Reviewer / Lead Member", "Assigned Category", "Paper Title",
    "Authors", "Year", "Publication Venue & Details", "Official DOI / URL", "Publication Type",
    "Recency Window (2021–2026)", "Novelty / OSR Task Formulation", "Datasets & Testbeds Evaluated",
    "Evaluation Metrics Used", "Reported Quantitative Results", "Limitations & Audit Caveats",
    "Member Reading Status", "Publisher Verification Status"
]

row_num = 4
for col_num, h in enumerate(headers, 1):
    c = ws1.cell(row=row_num, column=col_num, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = thin_border
ws1.row_dimensions[row_num].height = 28

# Read rows from crosswalk and write
for r in range(4, ws_src.max_row + 1):
    vals = [ws_src.cell(row=r, column=c).value for c in range(1, 19)]
    if not vals[0]:
        continue
    row_num += 1
    ws1.row_dimensions[row_num].height = 36
    is_zebra = (row_num % 2 == 1)
    
    for col_num, val in enumerate(vals, 1):
        c = ws1.cell(row=row_num, column=col_num, value=str(val) if val is not None else "")
        c.border = thin_border
        c.fill = fill_zebra if is_zebra else PatternFill(fill_type=None)
        
        if col_num in [1, 2, 7, 10]:
            c.font = font_mono
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col_num == 11:
            c.alignment = Alignment(horizontal="center", vertical="center")
            if "pre-2021" in str(val).lower() or str(vals[6]) in ['2018', '2020']:
                c.font = font_pre2021
            else:
                c.font = font_recent
        elif col_num in [3, 4, 17, 18]:
            c.font = font_bold if col_num in [3, 4] else font_regular
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        else:
            c.font = font_regular
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

col_widths = [12, 12, 24, 28, 36, 32, 10, 32, 32, 18, 20, 28, 32, 24, 38, 38, 30, 28]
for idx, width in enumerate(col_widths, 1):
    ws1.column_dimensions[get_column_letter(idx)].width = width

# SHEET 2: Category Breakdown
ws2 = wb_out.create_sheet(title="Category Distribution")
ws2.views.sheetView[0].showGridLines = True
ws2.cell(row=1, column=1, value="LITERATURE DISTRIBUTION ACROSS RESEARCH CATEGORIES").font = font_title

cat_headers = ["Category Name", "Reviewing Member", "Candidate Studies Assessed", "Core Focus & Mathematical Boundary"]
for col_num, h in enumerate(cat_headers, 1):
    c = ws2.cell(row=3, column=col_num, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = thin_border

cat_data = [
    ("Category A: Machine Learning and One-Class Detection", "Suresh Gopal Singh (258100001)", "9 Studies (SG01–SG09)", "Distance-based boundaries, density scoring, and reconstruction error residuals on benign baselines."),
    ("Category B: Deep Learning and Open-Set Recognition", "Ismayra Praveen (258100002)", "10 Studies (DL01–DL10)", "Deep generative modeling, extreme value theory tail modeling, metric centroids, and explicit reject decisions."),
    ("Category C: Anomaly, Hybrid and Adaptive Drift Detection", "Jatin (258100003)", "13 Studies (JTN01–JTN13)", "Streaming autoencoders, multi-stage signature/anomaly pipelines, statistical drift tracking, and continual learning.")
]

for r_idx, r_data in enumerate(cat_data, 4):
    for c_idx, val in enumerate(r_data, 1):
        c = ws2.cell(row=r_idx, column=c_idx, value=val)
        c.font = font_regular
        c.border = thin_border
        c.alignment = Alignment(horizontal="left", vertical="center")

ws2.column_dimensions['A'].width = 45
ws2.column_dimensions['B'].width = 30
ws2.column_dimensions['C'].width = 25
ws2.column_dimensions['D'].width = 50

# Save
wb_out.save('literature-matrix/master-literature-matrix.xlsx')
print("Saved literature-matrix/master-literature-matrix.xlsx successfully.")
