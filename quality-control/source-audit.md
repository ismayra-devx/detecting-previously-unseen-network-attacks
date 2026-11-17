# Quality Control & Source Audit Report

**Project:** IILM Survey Paper — *Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches*  
**Audit Date:** 18 November 2026 (Post-Submission Repository Audit)  
**Audited Artifacts:**
- Master Survey Paper: [`survey/final-survey.docx`](file:///c:/dev/detecting-previously-unseen-network-attacks/survey/final-survey.docx) / [`survey/final-survey.pdf`](file:///c:/dev/detecting-previously-unseen-network-attacks/survey/final-survey.pdf) (**FROZEN & UNTOUCHED**)
- Master Literature Matrix: [`literature-matrix/master-literature-matrix.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/literature-matrix/master-literature-matrix.xlsx)
- Master Reference Library: [`references/references.bib`](file:///c:/dev/detecting-previously-unseen-network-attacks/references/references.bib) / [`references/references.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/references/references.md)
- Search Log & Evidence: [`search-log/search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-log/search-records.xlsx) & [`search-evidence/`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/)

---

## 1. Quality Assurance Verification Matrix (13 Mandatory Checklist Dimensions)

| QC Dimension | Audit Requirement | Verified Result / Finding | Status |
| :--- | :--- | :--- | :---: |
| **1. Unique Paper Count** | $\ge 25$ unique works required by IILM guidelines. | **32 Unique Candidate Studies** assessed across the three member packs; **26 Core Studies** synthesized in paper narrative. | **PASS** |
| **2. Recency Window** | $\ge 15$ works within the recent five-year window (2021–2026). | **30 Studies** published between 2021 and 2026. Only 2 pre-2021 foundational baselines (Kitsune 2018, HELAD 2020) retained. *(Corrected previous 28-study count caused by crosswalk row offset).* | **PASS** |
| **3. Duplicate DOIs / Titles** | Zero duplicate works across member packs; matching by DOI/title. | **0 Duplicates**. Reconciled older duplicates: Carrera (MemAE-EIF) and Souza (Energy-based OSR) unified into single master records. | **PASS** |
| **4. Citation Traceability** | Every reference cited in text, in strict numerical order of appearance. | All 28 references (`[1]` to `[28]`) are cited in the body text in ascending order ($[1] \rightarrow [28]$). Every citation links to a real entry. | **PASS** |
| **5. DOI & URL Integrity** | Every reference must have a valid official publisher DOI or arXiv URL. | **100% Verified**. All 28 references carry confirmed DOIs, official conference proceedings links, or arXiv persistent URLs. | **PASS** |
| **6. Peer-Review Disclosures** | Preprints, conferences, journals, and book chapters clearly labeled. | Preprints (usfAD, Macko, SSF, Farrukh, Soltani) are explicitly labeled as preprints; peer-reviewed journals/conferences distinguished. | **PASS** |
| **7. Reading Status Integrity** | No AI inspection claimed as personal reading; transparent tracking. | Declared honestly in Annexure Table XI and Table XII: personal full-text reading in progress; publisher records audited; five evaluation tiers distinguished. | **PASS** |
| **8. Search Log Fidelity** | Real search counts; no invented screening tallies; ACM separation. | IEEE 284 displayed hits; ACM 444 standard and 8 video decoupled; Springer 1,000 export ceiling audited; Scholar labeled approximate; unrecorded tallies marked. | **PASS** |
| **9. Figure & Table Numbering** | Figures in Arabic numerals; Tables in Roman numerals; cited in text. | Figs. 1–3 and Tables I–IX (and Tables X–XIII in Annexure) consecutively numbered and cited in the text. | **PASS** |
| **10. Resolution of [VERIFY]** | No unverified claims or conflicting metrics presented as established facts. | Suresh Day 3 corrections enforced: RF 51.88% drop, 80.23% vs 82.15% inconsistency, LNCS 15450, exact MemAE F1 values reported. | **PASS** |
| **11. Paper Length & Form** | Main paper 8–12 pages, excluding cover page and annexure. | **11 Pages** for Block C (Pages 2–12), satisfying the 8–12 page target. Total document is 13 pages including cover and annexure. | **PASS** |
| **12. Template Formatting** | Preserves A4 page size, 2 cm margins, Times New Roman 10.5 pt body. | Preserved directly inside `IILM_Survey_Paper_Template(1).docx`. Margins set to $20\text{ mm}$; body text Times New Roman 10.5 pt. | **PASS** |
| **13. Cover Page Metadata** | Verified details populated; unknown institutional data marked pending. | B.Tech. CSE (AI & ML) Semester III populated; unknown course code, supervisor, and emails marked `[Pending Confirmation]`. | **PASS** |

---

## 2. In-Depth Verification of Critical Audit Findings

### A. Literature Matrix & Candidate Count Reconciliation
- **Total Unique Studies Assessed**: Exactly **32 studies** are registered in `literature-matrix/master-literature-matrix.xlsx` (M01 to M32).
- **Recency Reconciliation**:
  - **Recent Studies (2021–2026)**: **30 studies** ($32 - 2 = 30$).
  - **Foundational Baselines (Pre-2021)**: **2 studies** (M20: Mirsky et al., Kitsune 2018; M21: Wu et al., HELAD 2020).
  - *Audit Resolution*: A previous document draft cited "28 recent studies". Investigation revealed that `build_master_literature_matrix.py` had previously iterated over `range(4, max_row + 1)` in `source-to-paper crosswalk.xlsx`, skipping M01 (Guo 2023) and M02 (Uddin 2024). The script was corrected to read from row 2, restoring all 32 candidate studies and confirming exactly 30 recent studies and 2 foundational baselines.
- **Synthesized Core Studies**: **26 studies** are directly synthesized and compared across Sections IV-A, IV-B, IV-C, and Section V of the submitted manuscript.

### B. Search Evidence & Export Claims Audit
- **IEEE Xplore**: The search interface displayed **284 search results**. We corrected earlier unsupported documentation to clarify that 284 is an on-screen displayed hit count, not proof of a full BibTeX bulk export. Specific relevant studies were retrieved individually.
- **ACM Digital Library**: The search interface displayed **444 standard research publications** and **8 multimedia video recordings**.
  - Earlier documentation stating "444 records exported" was corrected to clarify that 444 is a displayed result count, not automatically 444 downloaded bibliographic export files.
  - The 8 video presentations were excluded during preliminary screening because the survey strictly synthesizes written scholarly texts. Summing to 452 is an invalid literature practice and is strictly rejected.
- **SpringerLink**: The platform displayed **19,135 results**, but enforces a strict platform ceiling of **1,000 records maximum** per CSV export. Exactly 1,000 records were exported to `springer-export-1000.csv`. The 19,135 displayed count and 1,000 exported CSV records remain strictly distinct in all logs.
- **Google Scholar**: Displays heuristic estimates (**About 16,900** for broad search; **About 367** for filtered search). Both counts are explicitly labeled as `approximate`. The query strings displayed in the search box are visually truncated in the screenshot captures and are honestly recorded as `... [truncated in screenshot]`; missing query terms are not guessed or reconstructed.
- **arXiv.org**: Returned **0 results** due to query parser boolean syntax limitations; recorded honestly as `0 (Reported result pending verification)`. Key preprints were retrieved via targeted title searches.
- **Screening Counts**: Intermediate rejection numbers across thousands of bulk results were not tracked counter-by-counter; they are marked **`Not recorded (untracked bulk screening)`** rather than populated with fabricated numbers.

### C. Suresh Day 3 Verification Audit Implementation
All 51 audited corrections from Suresh's Day 3 Verification Report were enforced in Section IV-A, Table IV, and Table VII:
- **usfAD Holdout Degradation**: Explicitly reported that when four attack types were removed from NSL-KDD, supervised Random Forest accuracy fell to 51.88% with an F1-score of 0.0%, demonstrating the catastrophic failure of closed-set models on unseen threats.
- **Reporting Discrepancy Disclosed**: Disclosed the internal reporting inconsistency in [3] regarding UNSW-NB15 accuracy (80.23% in text versus 82.15% in Table 2).
- **Exact Metric Precision**: Preserved exact MemAE-EIF F1-scores: 0.9234 (KDDCUP99), 0.9172 (NSL-KDD), and 0.7146 (CICIDS2017).
- **Venue & Citation Corrections**: TEX-DEC cited to Springer *Lecture Notes in Computer Science* (LNCS), vol. 15450, pp. 50–63; CLAD/CLOSR cited to *IEEE Transactions on Network and Service Management* / arXiv:2407.03780.

### D. Reading Status & Evaluation Stage Clarity
We maintain five unambiguous, progressive evaluation tiers:
1. *Candidate Registration*: Included as candidate entry in literature matrix (32 unique studies).
2. *Source Verification*: Bibliographic metadata, publisher pages, and abstracts audited against official sources.
3. *PDF Availability*: Legally permitted open-access PDFs downloaded to `research-papers/original_pdfs/`.
4. *Personal Reading*: Cover-to-cover reading by student members (Ismayra, Suresh, Jatin). Currently recorded honestly as in progress; never marked as complete without student confirmation.
5. *Inclusion in Synthesis*: Synthesized into Section IV/V comparative tables and narrative (26 core studies).

### E. Privacy Redaction & Git History Audit
- **Asset Redacted**: `search-evidence/evidence-springerlink-19135.png` was visually redacted to cover personal login username and institutional IP address before public release.
- **Git History Audit**: Commit `f0080c9` contains the original unredacted image blob in Git history.
- **Remediation Procedure**: Detailed instructions using `git-filter-repo` and `git push --force-with-lease` are provided in `search-evidence/README.md` and `quality-control/post-submission-audit.md`. In compliance with audit constraints ("Do not force-push without explicit approval"), Git history has not been rewritten without user permission.
