# Post-Submission GitHub Repository Audit & Documentary Reconciliation Report

**Project:** IILM Survey Paper — *Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches*  
**Date of Audit:** 18 November 2026  
**Auditor / System:** Antigravity AI Assistant & Quality Control System  
**Audit Scope:** Supporting repository documentation, literature matrices, search logs, and evidence manifests.  
**Repository:** `https://github.com/ismayra-devx/detecting-previously-unseen-network-attacks.git`

---

## 1. Executive Governance & Submitted Manuscript Lock

> [!IMPORTANT]
> **ABSOLUTE RULE: THE SUBMITTED PAPER WAS NOT MODIFIED.**
> The survey paper has already been submitted to the university and the submission deadline is closed.
> In strict accordance with the user's instructions and institutional academic governance:
> - `survey/final-survey.docx` — **FROZEN & UNTOUCHED**
> - `survey/final-survey.pdf` — **FROZEN & UNTOUCHED**
> - `IILM_Survey_Detecting_Previously_Unseen_Network_Attacks_Final.docx` — **FROZEN & UNTOUCHED**
> - `IILM_Survey_Detecting_Previously_Unseen_Network_Attacks_Final.pdf` — **FROZEN & UNTOUCHED**
> No manuscript text, headings, figures, tables, bibliography citations, or annexure pages were edited, regenerated, reformatted, or replaced.

### Cryptographic Hash Verification of Submitted Files
To guarantee that the submitted deliverables have not been altered in any way, their SHA-256 cryptographic hashes were recorded at the start and completion of this repository audit:

| Submitted Artifact Filename | File Size (Bytes) | SHA-256 Cryptographic Hash | Lock Status |
| :--- | :---: | :--- | :---: |
| **`survey/final-survey.docx`** | 303,412 | `c47ff26f90271675a01d43a53479f1676024b9271a8ef51ae828df80839c250c` | **VERIFIED UNCHANGED** |
| **`survey/final-survey.pdf`** | 298,543 | `887774eb2c34e3fec472e9c4357d856367ede1533e5c6f12cee7506dbc642076` | **VERIFIED UNCHANGED** |
| **`IILM_Survey_..._Final.docx`** | 303,412 | `c47ff26f90271675a01d43a53479f1676024b9271a8ef51ae828df80839c250c` | **VERIFIED UNCHANGED** |
| **`IILM_Survey_..._Final.pdf`** | 298,543 | `887774eb2c34e3fec472e9c4357d856367ede1533e5c6f12cee7506dbc642076` | **VERIFIED UNCHANGED** |

---

## 2. Exhaustive Audit Findings & Corrective Actions

### Finding 1: Master Literature Matrix Row Offset & Recency Count Reconciliation
- **Issue Discovered**: In the initial repository release, `literature-matrix/master-literature-matrix.xlsx` contained 30 study rows instead of the expected 32 unique candidate studies, and some supporting documentation cited "28 recent studies".
- **Root Cause Analysis**: The generator script `build_master_literature_matrix.py` previously iterated over `range(4, ws_src.max_row + 1)` of `source-to-paper crosswalk.xlsx`. Because the crosswalk data begins at row 2 (row 1 being headers), this loop accidentally bypassed row 2 (M01: Guo 2023) and row 3 (M02: Uddin et al. 2024 / usfAD).
- **Corrective Action**:
  - `build_master_literature_matrix.py` was corrected to iterate over `range(2, ws_src.max_row + 1)`.
  - Regenerated `literature-matrix/master-literature-matrix.xlsx`, successfully restoring all **32 unique candidate studies** (M01 through M32).
  - Recency classification was audited:
    - **Recent Studies (2021–2026)**: Exactly **30 studies** ($32 - 2 = 30$).
    - **Pre-2021 Foundational Baselines**: Exactly **2 studies** (M20: Mirsky et al., Kitsune 2018; M21: Wu et al., HELAD 2020).
    - **Core Synthesized Studies in Paper**: Exactly **26 studies** synthesized in Sections IV and V.
  - All occurrences of "28 recent studies" in `README.md`, `quality-control/source-audit.md`, and `contributions/team-contributions.md` were corrected to **30 recent studies**.

### Finding 2: Unsupported Search Export Claims in Database Logs
- **Issue Discovered**: Previous search documentation contained unsupported export claims, specifically claiming that 444 records were exported from ACM Digital Library and describing IEEE Xplore results as BibTeX candidate exports.
- **Audit Clarifications & Corrections**:
  - **ACM Digital Library**: The search interface displayed **444 peer-reviewed research papers**. In `search-records.xlsx` (both root and `search-log/`) and `search-methodology.md`, the "Records Exported" field was corrected from `444` to `0 (Not exported in bulk / displayed count only)`. The notes explicitly state: *"This is a platform displayed result count, not automatically 444 exported records."*
  - **ACM Video Decoupling**: The **8 multimedia video recordings** remain strictly separated on a dedicated row (SRCH-03). Under no circumstances are they combined with the 444 research papers (rejecting any 452 aggregate).
  - **IEEE Xplore**: The search interface displayed **284 search results**. The log was updated to record the exact displayed count of **284** and to clarify that this is an on-screen platform displayed hit count, not proof of a full BibTeX bulk export. Specific relevant studies were retrieved individually.
  - **SpringerLink Hard Export Ceiling**: The interface displayed **19,135 results**, but the platform restricts downloads to a hard ceiling of 1,000 records. Exactly 1,000 records were exported to `search-evidence/springer-export-1000.csv`. The 19,135 displayed count and 1,000 exported CSV records remain strictly distinct in all tables.
  - **Google Scholar Heuristic Estimates**: Counts of `About 16,900` (broad search) and `About 367` (filtered search) are explicitly labeled as `approximate`.
  - **No Fabricated Screening Numbers**: Intermediate exclusion counts during bulk exploratory passes were not tracked counter-by-counter; they are marked honestly as **`Not recorded (untracked bulk screening)`** rather than generating fabricated numbers.

### Finding 3: Google Scholar Search Queries Truncated in Screenshots
- **Issue Discovered**: Earlier drafts attempted to provide long, fully expanded boolean query strings for Google Scholar searches, whereas the browser interface search bar visually cut off the query text.
- **Audit Requirement**: Reconcile queries strictly against screenshots. Mark truncated query text as truncated; do not reconstruct missing query terms.
- **Corrective Action**:
  - In `search-records.xlsx`, `search-methodology.md`, and the evidence card images (`evidence-gscholar-16900-broad.png` and `evidence-gscholar-367-filtered.png`), the queries were updated to:
    - Search 1: `("unseen attack" OR "novel attack") AND (machine learning OR deep learning OR anomaly) ... [truncated in screenshot]`
    - Search 2: `("unseen attack" OR "unknown attack") AND ("network intrusion detection" OR NIDS) ... [truncated in screenshot]`
  - Explanatory notes confirm that missing query terms were not guessed or reconstructed.

### Finding 4: Clarification of Full-Text Assessment vs. Reading Statuses
- **Issue Discovered**: Loose terminology in preliminary notes risked conflating candidate registration or automated source checks with personal reading by students.
- **Corrective Action**: A formal progressive 5-tier evaluation framework was codified in `search-methodology.md`, `quality-control/source-audit.md`, `quality-control/unresolved-items.md`, and `contributions/team-contributions.md`:
  1. *Candidate Registration*: 32 unique candidate studies cataloged in the master matrix.
  2. *Source Verification*: Bibliographic metadata, publisher pages, and abstracts audited against official sources.
  3. *PDF Availability*: Legally permitted open-access PDFs downloaded to `research-papers/original_pdfs/`.
  4. *Personal Member Reading*: Cover-to-cover reading by student members (Ismayra, Suresh, Jatin). Recorded honestly as in progress; never marked as complete without student confirmation.
  5. *Inclusion in Synthesis*: 26 core studies synthesized in Section IV/V comparative tables and narrative.

### Finding 5: Preservation of Honest Member Reading Declarations
- **Audit Verification**:
  - **Suresh Gopal Singh (258100001)**: 9 candidate studies. 51 individual claims audited against primary publisher pages and preprints (Day 3 Report); personal cover-to-cover reading in progress.
  - **Ismayra Praveen (258100002)**: 10 candidate studies. Publisher records, abstracts, and accessible sections examined; 3 OA PDFs downloaded; personal cover-to-cover reading in progress.
  - **Jatin (258100003)**: 13 candidate studies. Reconciled register; abstracts and key method sections examined; personal reading in progress.
- **Integrity Rule**: Antigravity has not marked any paper as personally read without explicit human member confirmation.

### Finding 6: Privacy Redaction of Springer Screenshot & Git History Remediation (COMPLETED)
- **Issue Discovered**: The captured evidence card/screenshot `search-evidence/evidence-springerlink-19135.png` contained visible personal login account name and institutional IP address in the header.
- **Immediate Corrective Action**:
  - `build_search_evidence.py` was updated to render a prominent, opaque privacy redaction banner: `[REDACTED: User Login Identifier & Institutional IP Address for Privacy]` directly covering the sensitive header area.
  - The image was regenerated and saved to `search-evidence/evidence-springerlink-19135.png`.
- **Git History Permanent Remediation Executed**:
  - Upon receiving explicit user authorization, Git history was rewritten using `git-filter-repo --path search-evidence/evidence-springerlink-19135.png --invert-paths --force`.
  - The sensitive historical unredacted blob (`c6fdc73831decace726a583a16539fb2cfdda392`) was permanently purged and scrubbed from all commits in the repository.
  - The clean redacted screenshot (`evidence-springerlink-19135.png`) was restored into `search-evidence/` and committed to `main`.
  - Verification confirmed that the unredacted image does not exist in any reachable commit or Git object. All submitted survey manuscript files (`final-survey.docx`, `final-survey.pdf`) maintained verified identical SHA-256 hashes before and after the operation.

### Finding 7: Repository Hygiene & .gitignore Audit
- **Audit Verification**: `.gitignore` was inspected and verified to contain:
  - `source_material/` (private/local originals)
  - `Antigravity_Source_Material_Package/` (raw zip distribution)
  - `temp_zip/`
  - `__pycache__/` and `*.pyc`
  - Temporary testing scripts (`test_*.docx`, `test_*.ps1`, `test_*.py`)
- **Git Tree Check**: `git ls-files` confirmed that no private source material files, raw zip files, or unneeded temporary test scripts are tracked in Git.

---

## 3. Summary of Files Changed vs. Left Untouched

### Files Changed (Supporting Documentation & Registers Only)
1. [`literature-matrix/master-literature-matrix.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/literature-matrix/master-literature-matrix.xlsx) — Rebuilt to include all 32 candidate studies (M01–M32), 30 recent, 2 foundational.
2. [`build_master_literature_matrix.py`](file:///c:/dev/detecting-previously-unseen-network-attacks/build_master_literature_matrix.py) — Fixed loop range from row 2.
3. [`search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-records.xlsx) & [`search-log/search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-log/search-records.xlsx) — Corrected unsupported export claims (ACM 444 displayed, IEEE 284 displayed, Google Scholar truncated queries, Springer export ceiling).
4. [`build_search_records_xlsx.py`](file:///c:/dev/detecting-previously-unseen-network-attacks/build_search_records_xlsx.py) — Updated generator script with corrected values.
5. [`search-evidence/evidence-springerlink-19135.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-springerlink-19135.png) — Redacted personal login name and IP address.
6. [`search-evidence/evidence-ieee-xplore.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-ieee-xplore.png) — Updated displayed hits banner to 284.
7. [`search-evidence/evidence-acm-dl-444-standard.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-acm-dl-444-standard.png) — Clarified displayed count only.
8. [`search-evidence/evidence-gscholar-16900-broad.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-gscholar-16900-broad.png) — Marked truncated query.
9. [`search-evidence/evidence-gscholar-367-filtered.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-gscholar-367-filtered.png) — Marked truncated query.
10. [`build_search_evidence.py`](file:///c:/dev/detecting-previously-unseen-network-attacks/build_search_evidence.py) — Updated evidence generator with redaction and query clarifications.
11. [`search-evidence/README.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/README.md) — Updated evidence inventory, protocols, and Git history remediation details.
12. [`search-methodology.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-methodology.md) — Comprehensive methodology text updated with corrected counts, 5-tier evaluation framework, and privacy audit.
13. [`quality-control/source-audit.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/quality-control/source-audit.md) — Updated 13-point checklist, 30 recent studies count, and search log audit.
14. [`quality-control/unresolved-items.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/quality-control/unresolved-items.md) — Updated pending registers, 5-tier evaluation clarification, and manuscript lock statement.
15. [`contributions/team-contributions.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/contributions/team-contributions.md) — Reconciled study counts (32 candidate, 30 recent, 2 foundational, 26 core) and honest reading declarations.
16. [`README.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/README.md) — Synchronized all counts, evidence summaries, evaluation tiers, and added reference to this audit document.
17. [`quality-control/post-submission-audit.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/quality-control/post-submission-audit.md) — Newly created dedicated post-submission audit document.

### Files Intentionally Left Untouched (Submitted Deliverables & Audit Trail)
1. `survey/final-survey.docx` — **SUBMITTED MANUSCRIPT (STRICTLY FROZEN)**
2. `survey/final-survey.pdf` — **SUBMITTED PDF (STRICTLY FROZEN)**
3. `IILM_Survey_Detecting_Previously_Unseen_Network_Attacks_Final.docx` — **SUBMITTED COPY (STRICTLY FROZEN)**
4. `IILM_Survey_Detecting_Previously_Unseen_Network_Attacks_Final.pdf` — **SUBMITTED COPY (STRICTLY FROZEN)**
5. `source-to-paper crosswalk.xlsx` — **ORIGINAL AUDIT BASE (PRESERVED)**
6. `source_inventory.md` — **ORIGINAL INVENTORY REPORT (PRESERVED)**
7. `literature-matrix/jatin-papers.xlsx` — Individual member matrix (preserved as submitted)
8. `literature-matrix/suresh-papers.xlsx` — Individual member matrix (preserved as submitted)
9. `literature-matrix/ismayra-papers.xlsx` — Individual member matrix (preserved as submitted)
10. `research-papers/Jatin_Research_Record.docx` — Member research record (preserved)
11. `research-papers/Suresh_Research_Record.docx` — Member research record (preserved)
12. `research-papers/Ismayra_Research_Record.docx` — Member research record (preserved)
13. `references/references.bib` & `references/references.md` — Master bibliography (preserved)
14. `figures/selection-flow.png`, `figures/research-taxonomy.png`, `figures/publication-trends.png` — Submitted figures (preserved)
15. `research-papers/original_pdfs/` — Downloaded legal open-access PDFs (preserved)

---

## 4. Unresolved Items Requiring Human Decision

1. **Git History Purging (Force-Push Authorization)**:
   - *Status*: **COMPLETED**. The historical unredacted screenshot was purged from Git history using `git-filter-repo`. The redacted screenshot was restored and committed to `main`.
2. **Cover Page Pending Institutional Inputs**:
   - *Status*: Course title, course code, team number, supervisor details, coordinator name, and student institutional emails remain marked `[Pending Confirmation]` on the submitted cover page.
   - *Decision*: These items must be confirmed by the human student team prior to oral viva examination.
3. **Personal Full-Text Reading Completion**:
   - *Status*: Student members' personal cover-to-cover reading is in progress.
   - *Decision*: Students will complete their personal reading before the end-semester oral defense.
