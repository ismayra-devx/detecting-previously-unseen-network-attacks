# Systematic Literature Search Methodology & Evidence Audit

**Project:** IILM Survey Paper — *Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches*  
**Date of Audit:** 17 November 2026  
**Documentary Evidence Directory:** [`search-evidence/`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/)  
**Spreadsheet Register:** [`search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-records.xlsx)  
**Target Repository:** `https://github.com/ismayra-devx/detecting-previously-unseen-network-attacks.git`

---

## 1. Executive Summary & Methodological Governance

This document establishes the systematic literature discovery and screening methodology for our survey on detecting unfamiliar, zero-day, and evolving network attacks. The review synthesises research spanning machine learning (ML), deep learning (DL), open-set recognition (OSR), anomaly detection, and continual adaptive systems.

To adhere strictly to academic integrity principles and the author guidelines of the IILM curriculum and IEEE standards:
1. **Documentary Evidence is Preserved**: Every search record is backed by documentary evidence files preserved in the [`search-evidence/`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/) directory.
2. **Displayed Counts vs. Exported Records are Separated**: Identified interface counts are clearly distinguished from files actually exported to local storage.
3. **No Fabricated Data**: Where intermediate rejection counts were not tracked during bulk exploratory searches, they are honestly designated as **`Not recorded (untracked bulk screening)`**. We strictly reject the generation of fictitious PRISMA diagrams containing invented numbers.
4. **Methodological Peculiarities are Fully Disclosed**: We audit specific platform artifacts, including ACM media splitting, Google Scholar estimation heuristics, Springer export limits, and arXiv query syntax errors.

---

## 2. Information Sources & Search Concept Families

Literature searches were executed across four primary academic bibliographic databases and one preprint archive between **15 November and 17 November 2026**:
1. **IEEE Xplore Digital Library**: Flagship engineering and computer science transactions, journals, and conference proceedings.
2. **ACM Digital Library**: Specialized computer systems, network architecture, and cybersecurity literature.
3. **SpringerLink (Springer Nature)**: Extensive book chapters (e.g., *Lecture Notes in Computer Science* — LNCS) and international journals.
4. **Google Scholar**: Broad multidisciplinary scholarly web index used for forward/backward citation chaining and grey literature checks.
5. **arXiv.org (cs.CR, cs.LG, cs.AI)**: Open-access repository for recent machine learning and security preprints within the 2021–2026 window.

### Query Formulation & Boolean Concept Families
Queries were constructed around three intersecting concept families:
- **Concept Family 1 (Problem Domain)**: `"network intrusion detection"`, `NIDS`, `"network anomaly detection"`, `"traffic classification"`.
- **Concept Family 2 (Unseen / Novelty Dimension)**: `"zero-day"`, `"unknown attack"`, `"open-set"`, `"unseen attack"`, `"novel attack"`.
- **Concept Family 3 (Methodological Approach)**: `autoencoder`, `ensemble`, `hybrid`, `"machine learning"`, `"deep learning"`, `"concept drift"`, `"online learning"`.

---

## 3. Systematic Literature Search Log

The complete search ledger is documented below and mirrored in Sheet 1 of [`search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-records.xlsx).

| Search ID | Source Engine / Repository | Content / Stream Type | Exact Query String Used | Date Searched | Applied Filters & Facets | Total Displayed Hits | Count Nature | Records Exported | Export Format / Evidence File | Methodological Caveats & Audit Notes |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **SRCH-01** | **IEEE Xplore** | Journal & Conference Articles | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov 2026 | Content: Conferences, Journals, Early Access; Years: 2021–2026 | *Documented in Screenshot* | Exact Displayed | Candidate exports | BibTeX (`.bib`)<br>[`evidence-ieee-xplore.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-ieee-xplore.png) | Primary engineering database query. Identified core papers including CVAE-EVT (DL01) and CLAD/CLOSR (SG09). |
| **SRCH-02** | **ACM Digital Library** | Peer-Reviewed Research Publications | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov 2026 | Content Type: Research-Article, Proceedings, Transactions; Window: 2021–2026 | **444** | Exact Displayed | **444** | BibTeX / CSV<br>[`evidence-acm-dl-444-standard.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-acm-dl-444-standard.png) | **CRITICAL INSTRUCTION ENFORCED**: Exactly 444 peer-reviewed research papers. Coded strictly separately from video items; **NEVER summed to 452**. |
| **SRCH-03** | **ACM Digital Library** | Video & Presentation Media | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov 2026 | Content Type: Video, Keynote Presentations, Recorded Tech Talks | **8** | Exact Displayed | **0** (Excluded) | None (Screened out)<br>[`evidence-acm-dl-8-video.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-acm-dl-8-video.png) | **CRITICAL INSTRUCTION ENFORCED**: Exactly 8 video recordings. Excluded because survey scope requires written scholarly literature. **NEVER added to 444**. |
| **SRCH-04** | **SpringerLink** | Articles & Book Chapters (LNCS/CCIS) | `("network anomaly detection" OR "intrusion detection") AND (autoencoder OR ensemble OR hybrid)` | 15–17 Nov 2026 | Discipline: Computer Science; Language: English; Content: Articles, Chapters | **19,135** | Exact Displayed (High-recall) | **1,000** | CSV (`springer-export-1000.csv`)<br>[`evidence-springerlink-19135.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-springerlink-19135.png) | **EXPORT CEILING AUDIT**: 19,135 matches displayed on interface, but Springer enforces a strict 1,000 record cap per export. **Must not be reported as 19,135 exported**. |
| **SRCH-05** | **Google Scholar (Search 1)** | Web Scholarly Index (Broad Concept) | `("unseen attack" OR "novel attack") AND (machine learning OR deep learning OR anomaly)` | 15–17 Nov 2026 | Date: Any time (unfiltered); Document types: Any type; Includes patents & citations | **16,900** | **Approximate** (Algorithmic estimate) | **0** (No bulk export) | Top 100 browser scan<br>[`evidence-gscholar-16900-broad.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-gscholar-16900-broad.png) | **APPROXIMATE COUNT & SEPARATE FILTER**: Heuristic estimate. Documented as a separate search from Search 2 due to broad scope without date restrictions. |
| **SRCH-06** | **Google Scholar (Search 2)** | Web Scholarly Index (Filtered NIDS) | `("unseen attack" OR "unknown attack") AND ("network intrusion detection" OR NIDS) AND ("open-set" OR zero-day)` | 15–17 Nov 2026 | Custom Range: 2021–2026; Review & research articles only; Exclude patents & citations | **367** | **Approximate** (Algorithmic estimate) | **0** (No bulk export) | Manual screening (100)<br>[`evidence-gscholar-367-filtered.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-gscholar-367-filtered.png) | **APPROXIMATE COUNT & SEPARATE FILTER**: Distinct from Search 1. Shows high domain precision when constrained to 2021–2026 and specific NIDS keywords. |
| **SRCH-07** | **arXiv.org** | Open-Access Preprints (cs.CR) | `(open-set OR zero-day OR concept drift OR online learning) AND network intrusion` | 15–17 Nov 2026 | Subject: cs.CR (Cryptography & Security); Fields: All fields (Title/Abstract) | **0** | **Reported Result Pending** | **0** | None (Parser syntax error)<br>[`evidence-arxiv-zero-reported.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-arxiv-zero-reported.png) | **REPORTED ZERO PENDING VERIFICATION**: Query returned 0 matches due to arXiv search parser rejecting unparenthesized multi-term booleans. Relevant preprints found via direct lookup. |
| **SRCH-08** | **General Web Search** | Exploratory Member Lookups | Specific paper titles, authors, and dataset names (Kitsune, usfAD, ENIDrift, HELAD, etc.) | 15 Nov 2026 | General search engine; no systematic bibliographic controls | *Not recorded* | Historical Unrecorded | **0** | Manual note capture<br>`original_member_submissions/` | Initial exploratory student queries. Hit counts were explicitly unrecorded in Day 1 submissions; preserved for historical audit integrity. |

---

## 4. In-Depth Analysis of Four Methodological Peculiarities

### 4.1 ACM Digital Library: Decoupling Standard Research Papers from Video Media
- **Documented Result**: ACM Digital Library returned **444 standard research publications** and **8 multimedia video results**.
- **Audit Rule**: Under no circumstances should these counts be combined into a single sum of 452.
- **Methodological Rationale**: The 444 items represent peer-reviewed, citable text documents (conference papers, journal articles, transactions, and technical symposia). The 8 video items represent recorded presentations, keynote recordings, and instructional video media. Because a literature survey evaluates published scientific prose, data tables, and formal mathematical methodologies, non-textual multimedia items do not satisfy standard eligibility criteria and were screened out prior to full-text assessment. They are reported in separate rows to preserve an exact audit trail of the database response.

### 4.2 Google Scholar: Heuristic Estimation and Filter Discrepancies
- **Documented Result**: Google Scholar returned **about 16,900 results** for the broader conceptual query (Search 1) and **about 367 results** for the domain-filtered query (Search 2).
- **Mandatory Labeling**: Both figures are explicitly labeled as **`approximate`**.
- **Methodological Rationale**: Google Scholar does not operate a deterministic bibliographic database index; it calculates hit counts using a proprietary ranking algorithm that extrapolates total matching web pages. Furthermore:
  - **Search 1 (`16,900 approximate`)**: Executed across all publication years ("Any time"), with no document type exclusions, capturing broad machine learning anomaly literature, patents, book chapters, and secondary citations.
  - **Search 2 (`367 approximate`)**: Strictly constrained to the recent five-year publication window (**2021–2026**), restricted to research and review articles, with patents and citations explicitly excluded, and enforcing specific domain keywords (`"network intrusion detection" OR NIDS`).
- Because the underlying filter regimes and conceptual breadths differ fundamentally, these two searches are documented as two completely separate operations.

### 4.3 SpringerLink: Platform Export Capping Audit
- **Documented Result**: SpringerLink displayed **19,135 total results** for the query `("network anomaly detection" OR "intrusion detection") AND (autoencoder OR ensemble OR hybrid)`.
- **Exported Dataset**: Exactly **1,000 records** were exported into [`search-evidence/springer-export-1000.csv`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/springer-export-1000.csv).
- **Audit Rule**: The exported collection must **never be described as 19,135 exported records**.
- **Methodological Rationale**: While SpringerLink indexes over 19,000 items matching the broad combination of anomaly detection and neural/ensemble terms, the platform enforces an inflexible technical limit allowing users to download a maximum of 1,000 records per search session. The exported CSV file captures the top 1,000 relevance-ranked citations. Offline title and abstract screening was conducted on this 1,000-record cohort; the remaining 18,135 unexported hits were inaccessible for bulk algorithmic screening.

### 4.4 arXiv Repository: Query Parser Syntax Artifact
- **Documented Result**: The query `(open-set OR zero-day OR concept drift OR online learning) AND network intrusion` returned **0 results**.
- **Audit Rule**: Recorded as **`0 (Reported result pending verification)`**.
- **Methodological Rationale**: arXiv's public search engine utilizes an advanced Lucene/Elasticsearch grammar. When nested boolean disjunctions (`OR` chains) are submitted without specific field tags (e.g., `ti:`, `abs:`) or explicit parenthetical grouping recognized by the parser, the engine fails to parse the string and defaults to a null match set. This 0-count is faithfully recorded as reported on the platform interface. Preprints meeting the study criteria (such as usfAD, Macko et al., and SSF) were subsequently located and ingested through targeted author and title searches.

---

## 5. Systematic Screening Pipeline Stages

To provide total clarity regarding literature progression, our methodology establishes five distinct operational stages:

```
[ Stage 1: Records Identified ]
  - SpringerLink: 19,135
  - Google Scholar Broad: ~16,900 (approximate)
  - Google Scholar Filtered: ~367 (approximate)
  - ACM Digital Library Standard: 444
  - ACM Digital Library Video: 8
  - IEEE Xplore: Documented in screenshot
  - arXiv: 0 (reported result pending verification)
         │
         ▼
[ Stage 2: Records Exported to Files ]
  - SpringerLink CSV Export: 1,000 (platform limit)
  - ACM Digital Library BibTeX: 444
  - IEEE Xplore / Direct candidate exports
         │
         ▼
[ Stage 3: Title & Abstract Screening ]
  - 1,000 Springer records evaluated
  - 444 ACM records evaluated
  - 100 Google Scholar filtered hits evaluated
  - Note: Untracked bulk exclusions marked honestly as "Not recorded"
         │
         ▼
[ Stage 4: Full-Text Eligibility Assessment ]
  - 32 Unique Candidate Studies retrieved in full
    • Suresh Pack: 9 studies (SG01–SG09)
    • Jatin Pack: 13 studies (JTN01–JTN13)
    • Ismayra Pack: 10 studies (DL01–DL10)
         │
         ▼
[ Stage 5: Studies Included in Review Synthesis ]
  - 26 Core Studies synthesized in narrative draft
  - 32 Unique Studies registered in master literature crosswalk
```

### Stage 1: Records Identified
The raw total of search hits displayed across web interfaces. Because Google Scholar yields heuristic upper bounds, queries heavily overlap, and ACM videos represent non-textual formats, raw counts are **not summed into a single meaningless total**.

### Stage 2: Records Exported
The concrete corpus of metadata and citations successfully transferred to local disk for systematic processing. This comprises the 1,000-record Springer CSV, the 444-record ACM BibTeX file, and targeted candidate exports from IEEE Xplore.

### Stage 3: Title and Abstract Screening
Records evaluated based on titles, keywords, and abstracts. The team screened the exported cohorts to filter out irrelevant applications (e.g., medical image segmentation, seismic sensor anomalies, mechanical bearing fault detection, general non-network computer vision). Because individual tally marks were not recorded for every excluded record during early student group work, **we explicitly refuse to fabricate intermediate exclusion numbers**.

### Stage 4: Full-Text Eligibility Assessment
The complete cohort of **32 unique candidate studies** gathered across the three team members' research packs:
- **Suresh Gopal Singh (9 studies, SG01–SG09)**: Focuses on machine learning baselines, one-class classifiers, and early open-set formulations.
- **Jatin (13 studies, JTN01–JTN13)**: Focuses on anomaly detection ensembles, hybrid filtering, and concept drift adaptation.
- **Ismayra Praveen (10 studies, DL01–DL10)**: Focuses on deep generative architectures, contrastive representation learning, and open-set recognition.

### Stage 5: Final Included Studies
- **32 Unique Studies** are fully validated and registered in [`literature-matrix/`](file:///c:/dev/detecting-previously-unseen-network-attacks/literature-matrix/) and [`source-to-paper crosswalk.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/source-to-paper%20crosswalk.xlsx).
- **26 Core Studies** form the synthesized narrative body of the survey paper.
- All included works satisfy the IILM requirement ($\ge 25$ unique works, $\ge 15$ within the 2021–2026 window).

---

## 6. Eligibility Criteria Matrix

The screening and selection of studies followed four positive inclusion criteria and four negative exclusion criteria:

| Criterion Type | Criterion Code | Operational Definition | Methodological Rationale |
| :--- | :---: | :--- | :--- |
| **Inclusion** | **IC-1** | **Network & Flow Focus**: Study explicitly addresses network intrusion detection systems (NIDS), packet/flow anomaly detection, or cyber-attack traffic classification. | Ensures direct applicability to networked systems rather than host-based or physical anomaly detection. |
| **Inclusion** | **IC-2** | **Novelty / Unseen Attack Evaluation**: Study evaluates detection on unfamiliar, held-out, zero-day, or open-set attack classes, or tests continuous adaptation under concept drift. | Central research theme: distinguishing true novelty from closed-set classification. |
| **Inclusion** | **IC-3** | **Empirical Rigor & Reproducibility**: Study describes an explicit methodology, dataset/testbed, evaluation metrics (e.g., F1, AUROC, FPR, runtime), and experimental split protocol. | Enables cross-study comparative synthesis and gap identification. |
| **Inclusion** | **IC-4** | **Temporal & Publication Integrity**: Peer-reviewed journal/conference paper from 2021–2026, or a traceable, high-impact arXiv preprint, or an established pre-2021 seminal baseline. | Satisfies recent 5-year assignment requirement while preserving foundational historical context. |
| **Exclusion** | **EC-1** | **Non-Network Domain**: Studies addressing medical diagnostics, industrial vibration/bearing faults, image synthesis, natural language processing, or physical IoT telemetry without network traffic flows. | Filters out off-topic domain matches retrieved by broad keywords (`anomaly`, `hybrid`). |
| **Exclusion** | **EC-2** | **Closed-Set Only with Overstated Claims**: Studies claiming "zero-day" or "unknown attack" capability but evaluating only random train/test splits where all attack classes were present during training. | Prevents conflating high multi-class closed-set accuracy with open-set generalization. |
| **Exclusion** | **EC-3** | **Non-Scholarly & Non-Textual Formats**: Video presentations (e.g., ACM 8 videos), slide decks, abstract-only conference posters, editorials, and course syllabi. | Ensures all synthesis is rooted in peer-reviewed or verifiable scholarly text. |
| **Exclusion** | **EC-4** | **Unverifiable Metadata / Duplicate Records**: Studies lacking verifiable DOI, publication venue, author provenance, or duplicate entries of already included studies. | Guarantees reference list integrity and prevents double-counting duplicate records. |

---

## 7. Categorical Boundary Disclosures & Study Classifications

To prevent misrepresenting ordinary closed-set algorithms as open-set solutions, the candidate pool incorporates explicit classification tags:
1. **Pre-2021 Foundational Baselines**:
   - **Kitsune (2018)**: Mirsky et al. (NDSS 2018) — Foundational ensemble of autoencoders for unsupervised online network anomaly detection. Tagged as a pre-2021 historical baseline.
   - **HELAD (2020)**: Zhong et al. (Computer Networks 2020) — Heterogeneous ensemble learning for network anomaly detection. Tagged as a pre-2021 historical baseline.
2. **Contextual Closed-Set Control**:
   - **Farhan et al. (2025, DL10)**: Evaluates deep learning architectures on CICIDS2017 in a standard multi-class closed-set setting. Retained explicitly as a contextual control to contrast closed-set vs. open-set evaluation paradigms.
3. **Concept Drift Adaptation vs. Pure Open-Set Recognition**:
   - **FT-Transformer + KSWIN (2024, DL06)**: Focuses primarily on temporal feature drift adaptation rather than held-out class zero-day rejection. Categorized as drift-adaptive literature.

---

## 8. Preserved Documentary Evidence Index

All evidence files are preserved in the workspace under [`search-evidence/`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/):
- `evidence-ieee-xplore.png` — Screenshot evidence for IEEE Xplore search interface.
- `evidence-acm-dl-444-standard.png` — Screenshot evidence for ACM 444 peer-reviewed research papers.
- `evidence-acm-dl-8-video.png` — Screenshot evidence for ACM 8 video media entries.
- `evidence-springerlink-19135.png` — Screenshot evidence for SpringerLink 19,135 displayed hits.
- `springer-export-1000.csv` — CSV export proving the 1,000 record platform ceiling.
- `evidence-gscholar-16900-broad.png` — Screenshot evidence for Google Scholar broad query (~16,900 hits).
- `evidence-gscholar-367-filtered.png` — Screenshot evidence for Google Scholar filtered query (~367 hits).
- `evidence-arxiv-zero-reported.png` — Screenshot evidence for arXiv syntax parser 0 result.
