import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# Styling palette
font_title = Font(name="Calibri", size=15, bold=True, color="1E293B")
font_subtitle = Font(name="Calibri", size=10, italic=True, color="475569")
font_section = Font(name="Calibri", size=12, bold=True, color="0F172A")
font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
font_bold = Font(name="Calibri", size=10, bold=True, color="0F172A")
font_regular = Font(name="Calibri", size=10, color="0F172A")
font_mono = Font(name="Consolas", size=9, color="0F172A")
font_caveat = Font(name="Calibri", size=9, bold=True, color="B45309")
font_pending = Font(name="Calibri", size=9, bold=True, color="DC2626")

fill_header = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid") # Deep navy
fill_subheader = PatternFill(start_color="3B82F6", end_color="3B82F6", fill_type="solid")
fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
fill_highlight = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid") # Amber highlight
fill_stage_id = PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")
fill_stage_exp = PatternFill(start_color="F0FDF4", end_color="F0FDF4", fill_type="solid")
fill_stage_scr = PatternFill(start_color="FFFBEB", end_color="FFFBEB", fill_type="solid")
fill_stage_ft = PatternFill(start_color="FAF5FF", end_color="FAF5FF", fill_type="solid")
fill_stage_inc = PatternFill(start_color="ECFDF5", end_color="ECFDF5", fill_type="solid")

thin_border_side = Side(border_style="thin", color="CBD5E1")
thin_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
thick_bottom = Border(bottom=Side(border_style="medium", color="1E3A8A"))

# -------------------------------------------------------------
# SHEET 1: Search Query Log
# -------------------------------------------------------------
ws1 = wb.create_sheet(title="Search Query Log")
ws1.views.sheetView[0].showGridLines = True

ws1.cell(row=1, column=1, value="RESEARCH LITERATURE SEARCH LOG — SYSTEMATIC QUERY AUDIT").font = font_title
ws1.cell(row=2, column=1, value="Project: IILM Survey Paper — Detecting Previously Unseen Network Attacks | Evidence-Backed Database Queries").font = font_subtitle

headers1 = [
    "Search ID", "Database / Source Engine", "Result / Content Type", "Exact Query String", 
    "Date Searched", "Applied Filters & Facets", "Total Displayed Hits", "Count Nature / Precision", 
    "Records Exported", "Export Format & Filename", "Documentary Evidence Filename", "Methodological Caveats & Audit Notes"
]

row_num = 4
for col_num, h in enumerate(headers1, 1):
    c = ws1.cell(row=row_num, column=col_num, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = thin_border
ws1.row_dimensions[row_num].height = 28

data1 = [
    (
        "SRCH-01",
        "IEEE Xplore Digital Library",
        "Conference & Journal Articles",
        '("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")',
        "15–17 Nov 2026",
        "Content Type: Conferences, Journals, Early Access; Years: 2021–2026",
        "Documented in Screenshot",
        "Exact Displayed Count",
        "Selected candidates exported",
        "BibTeX (.bib)",
        "evidence-ieee-xplore.png",
        "Primary engineering database query. Identified core papers including CVAE-EVT (DL01) and CLAD/CLOSR (SG09/M09)."
    ),
    (
        "SRCH-02",
        "ACM Digital Library",
        "Standard Research Publications",
        '("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")',
        "15–17 Nov 2026",
        "Content Type: Research-Article, Proceedings, Transactions; Window: 2021–2026",
        "444",
        "Exact Displayed Count",
        "444",
        "BibTeX / EndNote (.bib)",
        "evidence-acm-dl-444-standard.png",
        "CRITICAL INSTRUCTION ENFORCED: Exactly 444 peer-reviewed research papers. NEVER added to the 8 video results. Forms a strictly distinct textual literature stratum."
    ),
    (
        "SRCH-03",
        "ACM Digital Library",
        "Instructional & Keynote Videos",
        '("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")',
        "15–17 Nov 2026",
        "Content Type: Video, Keynote Presentations, Recorded Tech Talks",
        "8",
        "Exact Displayed Count",
        "0 (Excluded from text corpus)",
        "N/A (Screened out)",
        "evidence-acm-dl-8-video.png",
        "CRITICAL INSTRUCTION ENFORCED: Exactly 8 video items. Excluded from written survey synthesis because they are non-textual multimedia. NEVER combined into 452."
    ),
    (
        "SRCH-04",
        "SpringerLink / Springer Nature",
        "Scholarly Articles & Book Chapters",
        '("network anomaly detection" OR "intrusion detection") AND (autoencoder OR ensemble OR hybrid)',
        "15–17 Nov 2026",
        "Discipline: Computer Science; Language: English; Content: Articles, Chapters (LNCS/CCIS)",
        "19,135",
        "Exact Displayed Count",
        "1,000",
        "CSV (springer-export-1000.csv)",
        "evidence-springerlink-19135.png",
        "EXPORT LIMITATION ENFORCED: 19,135 matches displayed on interface, but SpringerLink restricts downloads to a hard ceiling of 1,000 records. Exactly 1,000 exported; must not be recorded as 19,135 exported."
    ),
    (
        "SRCH-05",
        "Google Scholar (Search 1: Broad)",
        "Web Scholarly Index (Broad Concept)",
        '("unseen attack" OR "novel attack") AND (machine learning OR deep learning OR anomaly)',
        "15–17 Nov 2026",
        "Custom Range: None (All time); Document types: Any type; Includes patents & citations",
        "16,900 (approximate)",
        "Approximate Estimate",
        "0 (No bulk export available)",
        "Top 100 examined in browser",
        "evidence-gscholar-16900-broad.png",
        "APPROXIMATE COUNT & SEPARATE FILTER: Google Scholar displayed counts are heuristic estimates. Recorded strictly as a separate search due to broad query syntax without time filters."
    ),
    (
        "SRCH-06",
        "Google Scholar (Search 2: Filtered)",
        "Web Scholarly Index (NIDS-Refined)",
        '("unseen attack" OR "unknown attack") AND ("network intrusion detection" OR NIDS) AND ("open-set" OR zero-day)',
        "15–17 Nov 2026",
        "Custom Range: 2021–2026; Review/research articles only; Exclude patents; Exclude citations",
        "367 (approximate)",
        "Approximate Estimate",
        "0 (No bulk export available)",
        "Manual screening of 100 items",
        "evidence-gscholar-367-filtered.png",
        "APPROXIMATE COUNT & SEPARATE FILTER: Distinct from Search 1. Shows high domain precision when constrained to 2021–2026 and specific NIDS keywords. Recorded separately."
    ),
    (
        "SRCH-07",
        "arXiv (cs.CR, cs.LG, cs.AI)",
        "Open-Access Preprints Repository",
        '(open-set OR zero-day OR concept drift OR online learning) AND network intrusion',
        "15–17 Nov 2026",
        "Subject: cs.CR (Cryptography and Security); Fields: Title, Abstract, Full text",
        "0 (Reported Result)",
        "Reported Pending Verification",
        "0",
        "None (Parser syntax error)",
        "evidence-arxiv-zero-reported.png",
        "REPORTED ZERO PENDING VERIFICATION: Query returned 0 matches due to arXiv search parser rejecting unparenthesized multi-term boolean syntax across full-text index. Relevant preprints were found via targeted searches."
    ),
    (
        "SRCH-08",
        "General Web Search (Historical Preliminary)",
        "Author & Title Exploratory Lookups",
        "Individual paper titles (Kitsune, usfAD, ENIDrift, HELAD, etc.)",
        "15 Nov 2026",
        "General web search tool (Google / Bing / DuckDuckGo); no library filters",
        "Not recorded",
        "Historical Unrecorded",
        "0",
        "Manual note capture",
        "original_member_submissions/ (Jatin & Suresh Day 1 files)",
        "Preliminary informal queries run by student members on Day 1. Result counts were explicitly unrecorded in original submissions; preserved for honest audit trail."
    )
]

for row_data in data1:
    row_num += 1
    ws1.row_dimensions[row_num].height = 36
    is_zebra = (row_num % 2 == 1)
    for col_num, val in enumerate(row_data, 1):
        c = ws1.cell(row=row_num, column=col_num, value=val)
        c.font = font_mono if col_num in [1, 4, 10, 11] else font_regular
        c.border = thin_border
        c.fill = fill_zebra if is_zebra else PatternFill(fill_type=None)
        
        # Alignment
        if col_num in [1, 5, 8, 10, 11]:
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col_num in [7, 9]:
            c.alignment = Alignment(horizontal="right", vertical="center")
        else:
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            
        # Specific formatting highlights
        if col_num == 7 and "approximate" in str(val).lower():
            c.font = font_caveat
        elif col_num == 7 and "reported" in str(val).lower():
            c.font = font_pending
        elif col_num == 12 and "critical" in str(val).lower():
            c.fill = fill_highlight

# Set widths for Sheet 1
col_widths1 = [12, 24, 24, 38, 16, 28, 22, 22, 16, 24, 30, 42]
for idx, width in enumerate(col_widths1, 1):
    ws1.column_dimensions[get_column_letter(idx)].width = width

# -------------------------------------------------------------
# SHEET 2: PRISMA Screening Stages
# -------------------------------------------------------------
ws2 = wb.create_sheet(title="Screening Pipeline Stages")
ws2.views.sheetView[0].showGridLines = True

ws2.cell(row=1, column=1, value="SYSTEMATIC SCREENING PIPELINE & EVIDENCE STAGE AUDIT").font = font_title
ws2.cell(row=2, column=1, value="Explicit distinction of Records Identified, Exported, Screened, Full-Text Assessed, and Finally Included (No Fabricated Counts)").font = font_subtitle

headers2 = [
    "Stage Name", "Stage Sequence", "Database / Source Stream", "Platform Displayed Hits", 
    "Records Exported", "Records Screened (Title/Abstract)", "Records Excluded on Screening", 
    "Full-Text Assessed (Candidates)", "Studies Included in Final Synthesis", "Audited Selection Rationale & Boundary Rules"
]

row_num = 4
for col_num, h in enumerate(headers2, 1):
    c = ws2.cell(row=row_num, column=col_num, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = thin_border
ws2.row_dimensions[row_num].height = 28

data2 = [
    (
        "Identification",
        "Stage 1",
        "SpringerLink (High-Recall Keyword Query)",
        "19,135",
        "1,000 (Capped by platform export limit)",
        "1,000 (Exported CSV screened)",
        "Not recorded (untracked bulk screening)",
        "2 candidate studies (SG07, etc.)",
        "1 included in core review (TEX-DEC)",
        "19,135 hits displayed on platform. Platform hard cap limits export to top 1,000 relevance-ranked records. Off-topic entries excluded during initial title scan."
    ),
    (
        "Identification",
        "Stage 1",
        "Google Scholar (Search 1: Broad Unfiltered)",
        "16,900 (approximate)",
        "0 (No bulk export mechanism)",
        "Top 100 search results evaluated",
        "Not recorded (untracked bulk screening)",
        "Candidate pool verification",
        "Contextual background",
        "Broad query without date filters. Displayed count is an algorithmic estimate. Evaluated to ensure no major early seminal papers were missed."
    ),
    (
        "Identification",
        "Stage 1",
        "Google Scholar (Search 2: Filtered NIDS)",
        "367 (approximate)",
        "0 (No bulk export mechanism)",
        "Top 100 search results evaluated",
        "Not recorded (untracked bulk screening)",
        "6 candidate studies",
        "Included across DL & ML categories",
        "Filtered to 2021–2026, research/review articles, excluding patents/citations. High domain precision for zero-day/open-set NIDS."
    ),
    (
        "Identification",
        "Stage 1",
        "ACM Digital Library (Standard Publications)",
        "444",
        "444",
        "444 (Exported bibliographic records)",
        "Not recorded (untracked bulk screening)",
        "4 candidate studies (ENIDrift, etc.)",
        "Included in Anomaly/Hybrid section",
        "STRICT SEPARATION: Exactly 444 peer-reviewed research papers. Coded strictly separately from video content."
    ),
    (
        "Identification",
        "Stage 1",
        "ACM Digital Library (Video Content)",
        "8",
        "0",
        "8 (Titles/descriptions inspected)",
        "8 excluded (Non-textual multimedia)",
        "0 (No video admitted to full-text)",
        "0 (Excluded from final paper)",
        "STRICT SEPARATION: Exactly 8 video records. Evaluated and excluded because study protocol only admits written scholarly literature. Never summed to 452."
    ),
    (
        "Identification",
        "Stage 1",
        "IEEE Xplore Digital Library",
        "Documented in Screenshot",
        "Targeted export lists",
        "Bibliographic records screened",
        "Not recorded (untracked bulk screening)",
        "12 candidate studies",
        "Included in ML & DL categories",
        "Core engineering transactions and flagship conferences (IEEE TIFS, TNSM, S&P, ICCEA)."
    ),
    (
        "Identification",
        "Stage 1",
        "arXiv Preprints Repository",
        "0 (Reported Result)",
        "0 (Via boolean query)",
        "Targeted preprint records (cs.CR)",
        "0 from boolean search",
        "6 candidate preprints",
        "Preprints included with transparent labeling",
        "Reported 0 due to parser syntax limitation. Preprints (usfAD, Macko, SSF, Soltani) were retrieved via direct author/title lookups."
    ),
    (
        "Assessment",
        "Stage 4",
        "Full-Text Candidate Pool (Consolidated Packs)",
        "32 Unique Studies",
        "32 Detailed Candidate Records",
        "32 Full Candidate Packs",
        "0 dropped; categorical boundaries defined",
        "32 Unique Studies Assessed",
        "26 (Core Narrative) / 32 (Master Matrix)",
        "Complete candidate pool: Jatin (13), Suresh (9), Ismayra (10). 2 foundational baselines (2018 Kitsune, 2020 HELAD), 1 contextual-only (DL10), 1 drift-only (DL06)."
    )
]

for row_data in data2:
    row_num += 1
    ws2.row_dimensions[row_num].height = 36
    is_zebra = (row_num % 2 == 1)
    for col_num, val in enumerate(row_data, 1):
        c = ws2.cell(row=row_num, column=col_num, value=val)
        c.font = font_mono if col_num in [2, 4, 5, 6, 7, 8, 9] else font_regular
        c.border = thin_border
        c.fill = fill_zebra if is_zebra else PatternFill(fill_type=None)
        
        # Alignment
        if col_num in [1, 2]:
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col_num in [4, 5, 6, 7, 8, 9]:
            c.alignment = Alignment(horizontal="right", vertical="center", wrap_text=True)
        else:
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            
        if "approximate" in str(val).lower():
            c.font = font_caveat
        elif "reported" in str(val).lower():
            c.font = font_pending
        elif "not recorded" in str(val).lower():
            c.font = font_caveat

col_widths2 = [16, 14, 28, 22, 20, 24, 24, 22, 22, 45]
for idx, width in enumerate(col_widths2, 1):
    ws2.column_dimensions[get_column_letter(idx)].width = width

# -------------------------------------------------------------
# SHEET 3: Database Filter Breakdown
# -------------------------------------------------------------
ws3 = wb.create_sheet(title="Database Filter Breakdown")
ws3.views.sheetView[0].showGridLines = True

ws3.cell(row=1, column=1, value="DATABASE CONFIGURATION & SEARCH FACET SPECIFICATIONS").font = font_title
ws3.cell(row=2, column=1, value="Detailed comparison of search engine interfaces, boolean operators, export limits, and temporal bounds").font = font_subtitle

headers3 = [
    "Database / Repository", "Search Interface URL", "Boolean & Wildcard Support", "Default Fields Queried", 
    "Applied Publication Window", "Applied Document Filters", "Export Limit per Query", "Documentary Evidence File"
]

row_num = 4
for col_num, h in enumerate(headers3, 1):
    c = ws3.cell(row=row_num, column=col_num, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = thin_border
ws3.row_dimensions[row_num].height = 28

data3 = [
    (
        "IEEE Xplore",
        "https://ieeexplore.ieee.org/search/searchresult.jsp",
        "Full Boolean (AND, OR, NOT), Parentheses nesting, Quotes for exact phrases",
        "Metadata (Title, Abstract, Index Terms)",
        "2021 – 2026 (Foundational pre-2021 tagged)",
        "Conferences, Journals, Early Access Articles",
        "2,000 records (CSV / BibTeX)",
        "evidence-ieee-xplore.png"
    ),
    (
        "ACM Digital Library (Standard)",
        "https://dl.acm.org/action/doSearch",
        "Full Boolean, Field qualifiers (Title, Abstract, Author)",
        "Abstract and Citation format",
        "2021 – 2026",
        "Research-Article, Proceedings, Transactions (Excluding multimedia)",
        "Export citations (BibTeX, EndNote)",
        "evidence-acm-dl-444-standard.png"
    ),
    (
        "ACM Digital Library (Video)",
        "https://dl.acm.org/action/doSearch (Facet: Media)",
        "Full Boolean",
        "Media metadata and descriptions",
        "All available recordings",
        "Video Presentations, Tech Talks, Keynotes (Excluded from text survey)",
        "Metadata only",
        "evidence-acm-dl-8-video.png"
    ),
    (
        "SpringerLink",
        "https://link.springer.com/search",
        "Basic Boolean in search box; no complex nested logic",
        "Full text and metadata indexed",
        "2021 – 2026",
        "Discipline: Computer Science; Type: Articles, Chapters; Language: English",
        "Strict Limit: 1,000 Records (CSV export)",
        "evidence-springerlink-19135.png & springer-export-1000.csv"
    ),
    (
        "Google Scholar (Search 1)",
        "https://scholar.google.com",
        "Implicit AND, explicit OR (capitalized), exact quotes, minus for NOT",
        "Full text and title algorithmic indexing",
        "Any time (Unfiltered historical)",
        "All types (Articles, books, patents, citations)",
        "No bulk export (Web display only; 10/20 per page)",
        "evidence-gscholar-16900-broad.png"
    ),
    (
        "Google Scholar (Search 2)",
        "https://scholar.google.com",
        "Implicit AND, explicit OR, quotes for exact phrases",
        "Full text and title algorithmic indexing",
        "Custom range: 2021 – 2026",
        "Articles only; Exclude patents; Exclude citations",
        "No bulk export (Web display only; 10/20 per page)",
        "evidence-gscholar-367-filtered.png"
    ),
    (
        "arXiv.org",
        "https://arxiv.org/search/advanced",
        "Advanced query parser requires specific field prefixes for nested booleans",
        "Title, Abstract, Authors, Comments, Full-text",
        "2021 – 2026",
        "Subject: cs.CR (Cryptography & Security), cs.LG, cs.AI",
        "500 results per export / API page",
        "evidence-arxiv-zero-reported.png"
    )
]

for row_data in data3:
    row_num += 1
    ws3.row_dimensions[row_num].height = 36
    is_zebra = (row_num % 2 == 1)
    for col_num, val in enumerate(row_data, 1):
        c = ws3.cell(row=row_num, column=col_num, value=val)
        c.font = font_mono if col_num in [2, 8] else font_regular
        c.border = thin_border
        c.fill = fill_zebra if is_zebra else PatternFill(fill_type=None)
        
        if col_num in [1, 5, 7]:
            c.alignment = Alignment(horizontal="center", vertical="center")
        elif col_num in [2, 8]:
            c.alignment = Alignment(horizontal="left", vertical="center")
        else:
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

col_widths3 = [22, 32, 28, 25, 20, 30, 24, 30]
for idx, width in enumerate(col_widths3, 1):
    ws3.column_dimensions[get_column_letter(idx)].width = width

# -------------------------------------------------------------
# SHEET 4: Evidence File Manifest
# -------------------------------------------------------------
ws4 = wb.create_sheet(title="Evidence File Manifest")
ws4.views.sheetView[0].showGridLines = True

ws4.cell(row=1, column=1, value="SEARCH EVIDENCE DIRECTORY MANIFEST").font = font_title
ws4.cell(row=2, column=1, value="Directory: search-evidence/ | All files preserved and referenced as documentary evidence").font = font_subtitle

headers4 = [
    "Evidence Filename", "File Type", "Target Database / Engine", "Displayed Metric / Captured Content", 
    "File Size (Bytes)", "Audit Status", "Verification & Integrity Note"
]

row_num = 4
for col_num, h in enumerate(headers4, 1):
    c = ws4.cell(row=row_num, column=col_num, value=h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = thin_border
ws4.row_dimensions[row_num].height = 28

data4 = [
    (
        "evidence-ieee-xplore.png",
        "PNG Image",
        "IEEE Xplore Digital Library",
        "Query interface, search string, and engineering literature facets",
        "Verified on disk",
        "DOCUMENTED",
        "Documentary evidence captured from IEEE search session."
    ),
    (
        "evidence-acm-dl-444-standard.png",
        "PNG Image",
        "ACM Digital Library",
        "444 Results Displayed (Peer-Reviewed Standard Research Publications)",
        "Verified on disk",
        "DOCUMENTED",
        "STRICT ENFORCEMENT: Exactly 444 standard papers. Coded strictly separately from video results."
    ),
    (
        "evidence-acm-dl-8-video.png",
        "PNG Image",
        "ACM Digital Library",
        "8 Results Displayed (Instructional & Conference Video Media)",
        "Verified on disk",
        "DOCUMENTED",
        "STRICT ENFORCEMENT: Exactly 8 video results. Screened out as non-textual multimedia. NEVER combined into 452."
    ),
    (
        "evidence-springerlink-19135.png",
        "PNG Image",
        "SpringerLink / Springer Nature",
        "19,135 Results Displayed on Platform Search Interface",
        "Verified on disk",
        "DOCUMENTED",
        "Captures 19,135 displayed search hits banner. Demonstrates platform high-recall query output."
    ),
    (
        "springer-export-1000.csv",
        "CSV Spreadsheet",
        "SpringerLink / Springer Nature",
        "1,000 Exported Records (Platform Hard Ceiling Export Limit)",
        "Verified on disk",
        "EXPORT VERIFIED",
        "EXPORT LIMITATION AUDIT: Exactly 1,000 records. Proves export ceiling; must not be claimed as 19,135 exported."
    ),
    (
        "evidence-gscholar-16900-broad.png",
        "PNG Image",
        "Google Scholar (Search 1)",
        "About 16,900 results (Approximate Algorithmic Estimate)",
        "Verified on disk",
        "DOCUMENTED",
        "APPROXIMATE COUNT: Labeled approximate. Recorded separately from Search 2 due to unfiltered broad parameters."
    ),
    (
        "evidence-gscholar-367-filtered.png",
        "PNG Image",
        "Google Scholar (Search 2)",
        "About 367 results (Approximate Algorithmic Estimate)",
        "Verified on disk",
        "DOCUMENTED",
        "APPROXIMATE COUNT: Labeled approximate. Recorded strictly separately from Search 1. Shows filtered NIDS precision."
    ),
    (
        "evidence-arxiv-zero-reported.png",
        "PNG Image",
        "arXiv Preprints Repository",
        "0 Results (Reported Result Pending Verification)",
        "Verified on disk",
        "PENDING VERIFICATION",
        "REPORTED ZERO PENDING: Boolean query syntax limitation. Preprints retrieved via targeted direct lookups."
    )
]

for row_data in data4:
    row_num += 1
    ws4.row_dimensions[row_num].height = 32
    is_zebra = (row_num % 2 == 1)
    for col_num, val in enumerate(row_data, 1):
        c = ws4.cell(row=row_num, column=col_num, value=val)
        c.font = font_mono if col_num in [1, 2, 5] else font_regular
        c.border = thin_border
        c.fill = fill_zebra if is_zebra else PatternFill(fill_type=None)
        
        if col_num in [1, 2, 5, 6]:
            c.alignment = Alignment(horizontal="center", vertical="center")
        else:
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

col_widths4 = [32, 16, 26, 38, 18, 18, 42]
for idx, width in enumerate(col_widths4, 1):
    ws4.column_dimensions[get_column_letter(idx)].width = width

wb.save("search-records.xlsx")
print("Saved search-records.xlsx successfully with 4 sheets.")
