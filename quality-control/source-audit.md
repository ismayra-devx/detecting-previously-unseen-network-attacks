# Quality Control & Source Audit Report

**Project:** IILM Survey Paper — *Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches*  
**Audit Date:** 17 November 2026  
**Audited Artifacts:**
- Master Survey Paper: [`survey/final-survey.docx`](file:///c:/dev/detecting-previously-unseen-network-attacks/survey/final-survey.docx) / [`survey/final-survey.pdf`](file:///c:/dev/detecting-previously-unseen-network-attacks/survey/final-survey.pdf)
- Master Literature Matrix: [`literature-matrix/master-literature-matrix.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/literature-matrix/master-literature-matrix.xlsx)
- Master Reference Library: [`references/references.bib`](file:///c:/dev/detecting-previously-unseen-network-attacks/references/references.bib) / [`references/references.md`](file:///c:/dev/detecting-previously-unseen-network-attacks/references/references.md)
- Search Log & Evidence: [`search-log/search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-log/search-records.xlsx) & [`search-evidence/`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/)

---

## 1. Quality Assurance Verification Matrix

| QC Dimension | Audit Requirement | Verified Result / Finding | Status |
| :--- | :--- | :--- | :---: |
| **1. Unique Paper Count** | $\ge 25$ unique works required by IILM guidelines. | **32 Unique Candidate Studies** assessed across the three member packs; **26 Core Studies** synthesized in paper narrative. | **PASS** |
| **2. Recency Window** | $\ge 15$ works within the recent five-year window (2021–2026). | **28 Studies** published between 2021 and 2026. Only 2 pre-2021 foundational baselines (Kitsune 2018, HELAD 2020) retained. | **PASS** |
| **3. Duplicate DOIs / Titles** | Zero duplicate works across member packs; matching by DOI/title. | **0 Duplicates**. Reconciled older duplicates: Carrera (MemAE-EIF) and Souza (Energy-based OSR) unified into single master records. | **PASS** |
| **4. Citation Traceability** | Every reference cited in text, in strict numerical order of appearance. | All 28 references (`[1]` to `[28]`) are cited in the body text in ascending order ($[1] \rightarrow [28]$). Every citation links to a real entry. | **PASS** |
| **5. DOI & URL Integrity** | Every reference must have a valid official publisher DOI or arXiv URL. | **100% Verified**. All 28 references carry confirmed DOIs, official conference proceedings links, or arXiv persistent URLs. | **PASS** |
| **6. Peer-Review Disclosures** | Preprints, conferences, journals, and book chapters clearly labeled. | Preprints (usfAD, Macko, SSF, Farrukh, Soltani) are explicitly labeled as preprints; peer-reviewed journals/conferences distinguished. | **PASS** |
| **7. Reading Status Integrity** | No AI inspection claimed as personal reading; transparent tracking. | Declared honestly in Annexure Table XI and Table XII: personal full-text reading in progress; publisher records audited. | **PASS** |
| **8. Search Log Fidelity** | Real search counts; no invented screening tallies; ACM separation. | ACM 444 standard and 8 video decoupled; Springer 1,000 export ceiling audited; Scholar labeled approximate; unrecorded tallies marked. | **PASS** |
| **9. Figure & Table Numbering** | Figures in Arabic numerals; Tables in Roman numerals; cited in text. | Figs. 1–3 and Tables I–IX (and Tables X–XIII in Annexure) consecutively numbered and cited in the text. | **PASS** |
| **10. Resolution of [VERIFY]** | No unverified claims or conflicting metrics presented as established facts. | Suresh Day 3 corrections enforced: RF 51.88% drop, 80.23% vs 82.15% inconsistency, LNCS 15450, exact MemAE F1 values reported. | **PASS** |
| **11. Paper Length & Form** | Main paper 8–12 pages, excluding cover page and annexure. | **11 Pages** for Block C (Pages 2–12), satisfying the 8–12 page target. Total document is 13 pages including cover and annexure. | **PASS** |
| **12. Template Formatting** | Preserves A4 page size, 2 cm margins, Times New Roman 10.5 pt body. | Preserved directly inside `IILM_Survey_Paper_Template(1).docx`. Margins set to $20\text{ mm}$; body text Times New Roman 10.5 pt. | **PASS** |
| **13. Cover Page Metadata** | Verified details populated; unknown institutional data marked pending. | B.Tech. CSE (AI & ML) Semester III populated; unknown course code, supervisor, and emails marked `[Pending Confirmation]`. | **PASS** |

---

## 2. In-Depth Verification of Critical Findings

### A. Duplicate Reconciliation
In earlier preliminary working drafts, two sources were duplicated across member packs:
1. **Carrera et al. (MemAE-EIF)**: Appeared as Day 1 Ref [7] and Section Ref [5]. Matched via DOI `10.1109/ACCESS.2022.3199849`. Unified into **SG04** (Reference `[7]`).
2. **Souza et al. (Energy-Based OSR)**: Appeared as Day 1 Ref [8] and Section Ref [14]. Matched via DOI `10.1016/j.cose.2025.104569`. Unified into **SG05** (Reference `[8]`).
3. **Macko et al. (2023)**: Appeared as Jatin Day 1 Ref [9] and Section Ref [J6]. Matched via arXiv `2310.06656`. Unified into **JTN06** (Reference `[25]`).
4. **Zhang et al. / SSF (2024)**: Appeared as Jatin Day 1 Ref [5] and Section Ref [J8]. Matched via arXiv `2412.16264`. Unified into **JTN08** (Reference `[27]`).

### B. Suresh Day 3 Verification Audit Implementation
All 51 audited corrections from Suresh's Day 3 Verification Report were enforced in Section IV-A, Table IV, and Table VII:
- **usfAD Holdout Degradation**: Explicitly reported that when four attack types were removed from NSL-KDD, supervised Random Forest accuracy fell to 51.88% with an F1-score of 0.0%, demonstrating the catastrophic failure of closed-set models on unseen threats.
- **Reporting Discrepancy Disclosed**: Disclosed the internal reporting inconsistency in [3] regarding UNSW-NB15 accuracy (80.23% in text versus 82.15% in Table 2).
- **Exact Metric Precision**: Preserved exact MemAE-EIF F1-scores: 0.9234 (KDDCUP99), 0.9172 (NSL-KDD), and 0.7146 (CICIDS2017).
- **Venue & Citation Corrections**: TEX-DEC cited to Springer *Lecture Notes in Computer Science* (LNCS), vol. 15450, pp. 50–63; CLAD/CLOSR cited to *IEEE Transactions on Network and Service Management* / arXiv:2407.03780.

### C. Search Log Audited Realities
- **ACM Digital Library**: Decoupled 444 standard written research papers from 8 video presentations. Proved that summing to 452 is an invalid literature practice.
- **SpringerLink**: Documented 19,135 displayed hits against the platform's hard export ceiling of 1,000 records (`springer-export-1000.csv`).
- **Google Scholar**: Labeled 16,900 and 367 counts as approximate estimates and recorded them as separate searches due to differing filters.
- **arXiv**: Recorded 0 as a reported result pending verification due to boolean syntax grammar limitations.
- **Screening Pipeline**: Marked untracked bulk screening exclusions as *Not recorded* rather than fabricating artificial PRISMA numbers.
