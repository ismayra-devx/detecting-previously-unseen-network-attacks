# Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches

**Academic Course:** B.Tech. (CSE - AI & ML), Semester III | End-Semester Project Survey  
**Department:** School of Computer Science and Engineering, IILM University, Gurugram, India  
**Date of Submission:** 17 November 2026  
**Target Repository:** `https://github.com/ismayra-devx/detecting-previously-unseen-network-attacks.git`

---

## 1. Executive Summary

This repository contains the complete evidence base, research packs, search logs, comparative literature matrices, BibTeX bibliographic libraries, and final manuscript deliverables for our survey paper: **"Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches"**.

The survey evaluates **32 unique candidate studies** (including **26 core synthesised studies**) published between 2018 and 2026, investigating how modern learning systems detect zero-day exploits, novel attack variants, and traffic experiencing temporal concept drift. We classify the field into a tripartite taxonomy:
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
│   ├── final-survey.docx                      # Complete survey manuscript in official IILM template
│   └── final-survey.pdf                       # 13-page publication-grade PDF manuscript
├── figures/
│   ├── selection-flow.png                     # Fig. 1: Audited candidate selection flow diagram
│   ├── research-taxonomy.png                  # Fig. 2: Conceptual taxonomy of detection paradigms
│   └── publication-trends.png                 # Fig. 3: Publication chronology & trend chart (2018–2026)
├── literature-matrix/
│   ├── master-literature-matrix.xlsx          # Master cross-paradigm matrix (32 unique studies)
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
│   ├── README.md                              # Documentary evidence manifest
│   ├── springer-export-1000.csv               # 1,000-record export from SpringerLink (platform limit)
│   ├── evidence-ieee-xplore.png               # IEEE Xplore interface screenshot
│   ├── evidence-acm-dl-444-standard.png       # ACM DL 444 peer-reviewed research papers
│   ├── evidence-acm-dl-8-video.png            # ACM DL 8 video recordings (screened out)
│   ├── evidence-springerlink-19135.png        # SpringerLink 19,135 displayed hits
│   ├── evidence-gscholar-16900-broad.png      # Google Scholar broad query (~16,900 approximate)
│   ├── evidence-gscholar-367-filtered.png     # Google Scholar filtered query (~367 approximate)
│   └── evidence-arxiv-zero-reported.png       # arXiv query parser 0 result
├── research-papers/
│   ├── paper-links.md                         # Complete DOI/URL index for all 32 studies
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
    ├── source-audit.md                        # Exhaustive 13-point quality assurance verification
    └── unresolved-items.md                    # Transparent register of pending items
```

---

## 3. Systematic Search Evidence Summary

In accordance with strict academic guidelines:
- **ACM Digital Library**: 444 standard written research papers and 8 video presentations were recorded separately and **never summed to 452**.
- **SpringerLink**: 19,135 displayed hits recorded; export ceiling of **1,000 records** verified via [`search-evidence/springer-export-1000.csv`](search-evidence/springer-export-1000.csv).
- **Google Scholar**: Labeled explicitly as **approximate** (`16,900 approx` for broad search; `367 approx` for filtered search).
- **arXiv.org**: Recorded as **`0 (Reported result pending verification)`** due to boolean query parser syntax limitations.
- **Screening Counts**: Untracked bulk exploratory exclusions are marked **`Not recorded`** rather than populated with fabricated numbers.

---

## 4. Academic Integrity & Ethics

- **Open-Access Licensing**: Only legally permitted open-access PDFs are redistributed in `research-papers/original_pdfs/`. Proprietary paywalled publisher PDFs are accessed through authorized university channels and are not hosted here.
- **Personal Reading Declarations**: Automated AI ingestion and metadata cross-checking are explicitly distinguished from personal cover-to-cover reading by student members.
- **Confidentiality**: The `source_material/` folder containing private notes and raw uploads is excluded via `.gitignore`.
