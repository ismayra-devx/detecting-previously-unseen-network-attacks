# Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches

**Academic Course:** B.Tech. (CSE - AI & ML), Semester III | End-Semester Project Survey  
**Department:** School of Computer Science and Engineering, IILM University, Gurugram, India  
**Date of Submission:** 17 November 2026  
**Target Repository:** `https://github.com/ismayra-devx/detecting-previously-unseen-network-attacks.git`

---

## 1. Executive Summary

This repository contains the complete evidence base, research packs, search logs, comparative literature matrices, BibTeX bibliographic libraries, and final manuscript deliverables for our survey paper: **"Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches"**.

The survey evaluates **32 unique candidate studies** across three member packs, comprising **30 recent studies (2021–2026)** and **2 pre-2021 foundational baselines** (Kitsune 2018, HELAD 2020). From this candidate corpus, **26 core studies** are synthesized in depth in the submitted paper narrative. The field is structured into a tripartite taxonomy:
1. **Category A: Machine Learning and One-Class / Boundary-Based Detection** (Lead: Suresh Gopal Singh, 258100001)
2. **Category B: Deep Learning and Open-Set Recognition (OSR)** (Lead: Ismayra Praveen, 258100002)
3. **Category C: Anomaly-Based, Hybrid, and Adaptive Concept Drift Systems** (Lead: Jatin, 258100003)

---

## 2. Repository Structure

```
detecting-previously-unseen-network-attacks/
├── README.md                                  # Repository overview and audit manifest
├── .gitignore                                 # Git ignore (excludes private source_material/ originals)
├── survey/
│   ├── final-survey.docx                      # Complete survey manuscript in official IILM template (FROZEN)
│   └── final-survey.pdf                       # 13-page publication-grade PDF manuscript (FROZEN)
├── figures/
│   ├── selection-flow.png                     # Fig. 1: Audited candidate selection flow diagram
│   ├── research-taxonomy.png                  # Fig. 2: Conceptual taxonomy of detection paradigms
│   └── publication-trends.png                 # Fig. 3: Publication chronology & trend chart (2018–2026)
├── literature-matrix/
│   ├── master-literature-matrix.xlsx          # Master cross-paradigm matrix (32 unique candidate studies)
│   ├── ismayra-papers.xlsx                    # Deep learning & OSR matrix (10 studies)
│   ├── suresh-papers.xlsx                     # Machine learning & one-class matrix (9 studies)
│   └── jatin-papers.xlsx                      # Anomaly & adaptive drift matrix (13 studies)
├── references/
│   ├── references.bib                         # Master BibTeX database (34 verified entries)
│   ├── references.md                          # IEEE-formatted reference register with DOIs
│   ├── Ismayra_References.bib                 # Deep learning BibTeX database
│   ├── Suresh_References.bib                  # Machine learning BibTeX database
│   └── Jatin_References.bib                   # Anomaly & adaptive BibTeX database
├── search-log/
│   └── search-records.xlsx                    # Multi-sheet systematic query ledger
├── search-evidence/
│   ├── README.md                              # Documentary evidence manifest & privacy audit
│   ├── springer-export-1000.csv               # 1,000-record export from SpringerLink (platform limit)
│   ├── evidence-ieee-xplore.png               # IEEE Xplore interface screenshot (284 displayed hits)
│   ├── evidence-acm-dl-444-standard.png       # ACM DL 444 displayed research papers (displayed count only)
│   ├── evidence-acm-dl-8-video.png            # ACM DL 8 video recordings (screened out; never summed)
│   ├── evidence-springerlink-19135.png        # SpringerLink 19,135 displayed hits (REDACTED for privacy)
│   ├── evidence-gscholar-16900-broad.png      # Google Scholar broad query (~16,900 approx; query truncated)
│   ├── evidence-gscholar-367-filtered.png     # Google Scholar filtered query (~367 approx; query truncated)
│   └── evidence-arxiv-zero-reported.png       # arXiv query parser 0 result (syntax limitation)
├── research-papers/
│   ├── paper-links.md                         # Complete DOI/URL index for all 32 candidate studies
│   ├── original_pdfs/                         # Permitted Open-Access PDFs only
│   │   ├── DL04_Soltani_Preprint_2021.pdf     # Soltani et al. (arXiv OA)
│   │   ├── DL07_Fang_Xie_2025.pdf             # Fang & Xie (Nature Sci. Rep. CC-BY 4.0 OA)
│   │   └── DL10_Farhan_2025.pdf               # Farhan et al. (IEEE Access CC-BY 4.0 OA)
│   ├── Ismayra_Research_Record.docx           # Ismayra's member research file
│   ├── Suresh_Research_Record.docx            # Suresh's member research file
│   └── Jatin_Research_Record.docx             # Jatin's member research file
├── contributions/
│   └── team-contributions.md                  # Member division of responsibilities & reading declarations
└── quality-control/
    ├── post-submission-audit.md               # Dedicated post-submission repository audit report
    ├── source-audit.md                        # Exhaustive 13-point quality assurance verification
    └── unresolved-items.md                    # Transparent register of pending items
```

---

## 3. Systematic Search Evidence Summary

In accordance with strict academic audit guidelines:
- **IEEE Xplore**: The search interface displayed **284 search results**. This count is documented as an on-screen displayed hit count, not proof of a full BibTeX bulk export.
- **ACM Digital Library**: The search interface displayed **444 standard research publications**. This is an on-screen displayed result count, not automatically 444 exported records. In addition, **8 multimedia video presentations** were recorded separately and **never summed to 452**.
- **SpringerLink**: 19,135 displayed search hits recorded on interface; platform export ceiling of **1,000 records** verified via [`search-evidence/springer-export-1000.csv`](search-evidence/springer-export-1000.csv). The 19,135 displayed hits and 1,000 exported CSV records remain strictly distinct. Personal login username and institutional IP address have been visually redacted for public repository distribution.
- **Google Scholar**: Labeled explicitly as **approximate** (`About 16,900` for broad search; `About 367` for filtered search). The query strings displayed in the search box in the captured evidence are visually truncated (`... [truncated in screenshot]`) and recorded as captured without guessing unverified query terms.
- **arXiv.org**: Recorded as **`0 (Reported result pending verification)`** due to boolean query parser syntax limitations.
- **Screening Counts**: Untracked bulk exploratory exclusions are marked **`Not recorded (untracked bulk screening)`** rather than populated with fabricated numbers.

---

## 4. Academic Integrity & Reading Status Principles

1. **Progressive Five-Tier Evaluation Framework**:
   The repository enforces strict separation between:
   - *Candidate Registration*: 32 unique candidate studies cataloged in the master matrix.
   - *Source Verification*: Bibliographic metadata, publisher pages, and abstracts audited against official sources.
   - *PDF Availability*: Legally permitted open-access PDFs downloaded to `research-papers/original_pdfs/`.
   - *Personal Member Reading*: Cover-to-cover reading by student members (Ismayra, Suresh, Jatin); recorded honestly as in progress.
   - *Inclusion in Synthesis*: 26 core studies synthesized in Section IV/V comparative tables and narrative.
2. **Honest Personal Reading Declarations**:
   Automated AI ingestion and metadata cross-checking are explicitly distinguished from personal cover-to-cover reading by student members. Antigravity does not mark papers as personally read without student confirmation.
3. **Open-Access Licensing**:
   Only legally permitted open-access PDFs are redistributed in `research-papers/original_pdfs/`. Proprietary paywalled publisher PDFs are accessed through authorized university channels and are not hosted here.
4. **Confidentiality & Privacy**:
   - The `source_material/` folder containing private notes and raw uploads is excluded via `.gitignore`.
   - Personal login name and institutional IP address have been visually redacted on public evidence images.

---

## 5. Post-Submission Manuscript Lock

The survey paper manuscript files (`survey/final-survey.docx` and `survey/final-survey.pdf`) represent the exact version submitted to the university at the deadline. **In accordance with strict post-submission governance, these files are completely frozen, locked, and untouched.** All post-submission audits and supporting documentation adjustments are recorded in [`quality-control/post-submission-audit.md`](quality-control/post-submission-audit.md).
