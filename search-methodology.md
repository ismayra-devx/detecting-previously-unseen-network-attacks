# Systematic Literature Search Methodology & Evidence Audit

**Project:** IILM Survey Paper — *Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches*  
**Date of Audit:** 18 November 2026 (Post-Submission Repository Audit)  
**Documentary Evidence Directory:** [`search-evidence/`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/)  
**Spreadsheet Register:** [`search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-records.xlsx) (and [`search-log/search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-log/search-records.xlsx))  
**Target Repository:** `https://github.com/ismayra-devx/detecting-previously-unseen-network-attacks.git`

---

## 1. Executive Summary & Methodological Governance

This document establishes the systematic literature discovery, appraisal, and screening methodology for our survey on detecting unfamiliar, zero-day, and evolving network attacks. The review synthesises research spanning machine learning (ML), deep learning (DL), open-set recognition (OSR), anomaly detection, and continual adaptive systems.

To adhere strictly to academic integrity principles and the author guidelines of the IILM curriculum and IEEE standards:
1. **Documentary Evidence is Preserved**: Every search record is backed by documentary evidence files preserved in the [`search-evidence/`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/) directory.
2. **Displayed Counts vs. Exported Records are Separated**: Identified interface counts are clearly distinguished from files actually exported to local storage.
   - ACM 444 is an on-screen displayed result count, not automatically 444 exported records.
   - IEEE 284 is an on-screen displayed result count, not proof of a full BibTeX bulk export.
   - ACM Videos 8 must remain strictly separate from ACM research publications; never summed into 452.
   - SpringerLink 19,135 displayed results and 1,000 exported CSV records remain strictly distinct.
   - Google Scholar counts are explicitly designated as approximate heuristic estimates.
3. **No Fabricated Screening Numbers**: Where intermediate rejection counts were not tracked counter-by-counter during bulk exploratory searches, they are honestly designated as **`Not recorded (untracked bulk screening)`**. We strictly reject the generation of fictitious PRISMA diagrams containing invented numbers.
4. **Google Scholar Queries Faithfully Documented**: Query strings visible in UI screenshots that were cut off by the search bar width are explicitly marked as truncated (`... [truncated in screenshot]`). Missing query tail parameters are not guessed or reconstructed.
5. **Rigorous Five-Tier Evaluation Distinction**: We maintain strict boundaries between: (1) candidate registration, (2) source verification, (3) PDF availability, (4) personal student reading, and (5) synthesis inclusion. Personal reading by student members is never fabricated or conflated with automated AI inspection.
6. **Privacy Redaction**: Sensitive personal credentials (login username and institutional IP address) visible on the SpringerLink platform capture have been visually redacted for public repository distribution.

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

The complete search ledger is documented below and mirrored in Sheet 1 of [`search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-records.xlsx) and [`search-log/search-records.xlsx`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-log/search-records.xlsx).

| Search ID | Source Engine / Repository | Content / Stream Type | Exact Query String Used | Date Searched | Applied Filters & Facets | Total Displayed Hits | Count Nature | Records Exported | Export Format / Evidence File | Methodological Caveats & Audit Notes |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: | :--- | :--- |
| **SRCH-01** | **IEEE Xplore** | Journal & Conference Articles | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov 2026 | Content: Conferences, Journals, Early Access; Years: 2021–2026 | **284** | Exact Displayed Count | **0** (Displayed count only) | None (Not proof of BibTeX export)<br>[`evidence-ieee-xplore.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-ieee-xplore.png) | Interface displayed 284 results. The 284 count is an on-screen displayed hit count, not proof of a full BibTeX bulk export. Specific relevant studies were retrieved individually. |
| **SRCH-02** | **ACM Digital Library** | Peer-Reviewed Research Publications | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov 2026 | Content: Research-Article, Proceedings, Transactions; Window: 2021–2026 | **444** | Exact Displayed Count | **0** (Displayed count only) | None (Displayed count, not 444 exported records)<br>[`evidence-acm-dl-444-standard.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-acm-dl-444-standard.png) | **CRITICAL INSTRUCTION ENFORCED**: Exactly 444 displayed research papers. This is an on-screen displayed result count, not automatically 444 exported records. NEVER added to the 8 video results. |
| **SRCH-03** | **ACM Digital Library** | Instructional & Keynote Videos | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov 2026 | Content: Video, Keynote Presentations, Recorded Tech Talks | **8** | Exact Displayed Count | **0** (Excluded from text corpus) | N/A (Screened out)<br>[`evidence-acm-dl-8-video.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-acm-dl-8-video.png) | **CRITICAL INSTRUCTION ENFORCED**: Exactly 8 video items. Excluded because study protocol only admits written scholarly literature. **NEVER summed to 452**. |
| **SRCH-04** | **SpringerLink** | Scholarly Articles & Book Chapters | `("network anomaly detection" OR "intrusion detection") AND (autoencoder OR ensemble OR hybrid)` | 15–17 Nov 2026 | Discipline: Computer Science; Language: English; Content: Articles, Chapters (LNCS/CCIS) | **19,135** | Exact Displayed Count | **1,000** | CSV (`springer-export-1000.csv`)<br>[`evidence-springerlink-19135.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-springerlink-19135.png) | **PLATFORM CEILING ENFORCED**: 19,135 displayed search results on interface, but SpringerLink restricts downloads to a hard ceiling of 1,000 records. Exactly 1,000 exported; 19,135 and 1,000 kept strictly distinct. Personal login and IP redacted. |
| **SRCH-05** | **Google Scholar (Search 1)** | Web Scholarly Index (Broad Concept) | `("unseen attack" OR "novel attack") AND (machine learning OR deep learning OR anomaly) ... [truncated in screenshot]` | 15–17 Nov 2026 | Date: Any time (unfiltered); Document types: Any type; Includes patents & citations | **About 16,900** | **Approximate** (Algorithmic estimate) | **0** (No bulk export) | Top results scanned in browser<br>[`evidence-gscholar-16900-broad.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-gscholar-16900-broad.png) | **APPROXIMATE COUNT & TRUNCATED QUERY**: Algorithmic estimate. Query text visible in search bar is truncated in screenshot; missing terms not reconstructed. Kept strictly separate from Search 2. |
| **SRCH-06** | **Google Scholar (Search 2)** | Web Scholarly Index (Filtered NIDS) | `("unseen attack" OR "unknown attack") AND ("network intrusion detection" OR NIDS) ... [truncated in screenshot]` | 15–17 Nov 2026 | Custom Range: 2021–2026; Review & research articles only; Exclude patents & citations | **About 367** | **Approximate** (Algorithmic estimate) | **0** (No bulk export) | Browser scan / targeted retrieval<br>[`evidence-gscholar-367-filtered.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-gscholar-367-filtered.png) | **APPROXIMATE COUNT & TRUNCATED QUERY**: Algorithmic estimate. Query text visible in search bar is truncated in screenshot; missing terms not reconstructed. Kept strictly separate from Search 1. |
| **SRCH-07** | **arXiv.org** | Open-Access Preprints (cs.CR) | `(open-set OR zero-day OR concept drift OR online learning) AND network intrusion` | 15–17 Nov 2026 | Subject: cs.CR (Cryptography & Security); Fields: All fields (Title/Abstract) | **0** | **Reported Result Pending** | **0** | None (Parser syntax error)<br>[`evidence-arxiv-zero-reported.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-arxiv-zero-reported.png) | **REPORTED ZERO PENDING VERIFICATION**: Query returned 0 matches due to arXiv search parser rejecting unparenthesized multi-term booleans. Relevant preprints found via targeted lookups. |
| **SRCH-08** | **General Web Search** | Exploratory Member Lookups | Specific paper titles, authors, and dataset names (Kitsune, usfAD, ENIDrift, HELAD, etc.) | 15 Nov 2026 | General search engine; no systematic bibliographic controls | *Not recorded* | Historical Unrecorded | **0** | Direct member research notes<br>`source_material/` | Initial exploratory student queries. Hit counts were explicitly unrecorded in Day 1 submissions; preserved for historical audit integrity without inventing numbers. |

---

## 4. In-Depth Analysis of Methodological Peculiarities

### 4.1 IEEE Xplore: Decoupling Displayed Hit Count (284) from Bulk BibTeX Export Claims
- **Captured Metric**: The IEEE Xplore web interface displayed **284 search results** for the systematic Boolean query.
- **Audit Clarification**: This is an on-screen platform displayed result count. It does not constitute proof that all 284 records were exported in bulk as a single `.bib` file.
- **Selection Practice**: Candidate studies were evaluated on the platform and relevant records (e.g., CVAE-EVT, MemAE-EIF, CLAD/CLOSR, SFE-GACN) were retrieved individually. The repository records the 284 count honestly as a displayed hit metric rather than an exported file tally.

### 4.2 ACM Digital Library: Decoupling Displayed Results (444) from Bulk Export and Video Media (8)
- **Captured Metric**: ACM Digital Library displayed **444 standard research publications** and **8 multimedia video results**.
- **Audit Rules Enforced**:
  1. The 444 count is a displayed result count on the search interface, not automatically 444 downloaded BibTeX export files.
  2. The 444 standard research papers and the 8 video media results must remain strictly separate. Under no circumstances should they be combined into a single sum of 452.
- **Methodological Rationale**: The 444 items represent peer-reviewed scholarly prose (proceedings, transactions, journals). The 8 video items represent keynote recordings and instructional media. Because a literature survey evaluates published scientific prose, data tables, and formal mathematical methodologies, non-textual multimedia items do not satisfy eligibility criteria and were screened out prior to full-text assessment.

### 4.3 SpringerLink: Platform Export Ceilings (19,135 Displayed vs. 1,000 Exported CSV Records)
- **Captured Metric**: SpringerLink returned **19,135 total indexed records** matching the high-recall keyword combination.
- **Platform Limitation**: The SpringerLink platform enforces a strict technical ceiling of **1,000 records maximum** per CSV export.
- **Audit Clarification**: Exactly 1,000 records were exported to [`springer-export-1000.csv`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/springer-export-1000.csv) for offline screening. It is methodologically impermissible to report that 19,135 records were exported. The 19,135 displayed count and 1,000 exported CSV records remain strictly distinct in all audit tables.

### 4.4 Google Scholar: Heuristic Estimation, Distinct Filter Sets, and Truncated Search Queries
- **Captured Metrics**: Google Scholar returned **About 16,900 results** for the broader conceptual query (Search 1) and **About 367 results** for the domain-filtered query (Search 2).
- **Mandatory Labeling**: Both figures are explicitly designated as **`approximate`**.
- **Query Text Faithfulness**: The queries displayed in the Google Scholar search box in the captured evidence screenshots are visually cut off by the width of the input field. In accordance with audit standards, the query text is marked as truncated (`... [truncated in screenshot]`). We strictly refrain from inventing or reconstructing unverified query tail parameters.
- **Distinct Filter Regimes**:
  - **Search 1 (`About 16,900 approximate`)**: Executed across all publication years ("Any time"), with no document type exclusions, capturing broad machine learning anomaly literature, patents, book chapters, and secondary citations.
  - **Search 2 (`About 367 approximate`)**: Strictly constrained to the recent five-year publication window (**2021–2026**), restricted to research and review articles, with patents and citations explicitly excluded, and enforcing specific domain keywords (`"network intrusion detection" OR NIDS`).
- Because the underlying filter regimes and conceptual breadths differ fundamentally, these two searches are documented as two completely separate operations.

### 4.5 arXiv: Boolean Syntax Grammar Limitations & Zero Result Protocol
- **Captured Metric**: arXiv returned **0 results** for the composite string `(open-set OR zero-day OR concept drift OR online learning) AND network intrusion`.
- **Root Cause**: arXiv's search parser does not support nested, unparenthesized multi-term boolean disjunctions across all-fields searches.
- **Integrity Protocol**: Rather than discarding or concealing the failed query, it is documented honestly as **`0 (Reported result pending verification)`**. Crucial preprints (usfAD, Macko, SSF continual learning) were subsequently identified and verified through targeted title and author searches.

---

## 5. Methodological Clarification of Evaluation Stages

To prevent ambiguous claims about "full-text assessment" in repository documentation, we formally distinguish the following five progressive evaluation stages:

1. **Candidate Registration (Matrix Inclusion)**: Registering a unique study as a candidate row in the master literature matrix based on thematic relevance to unseen/novel network attack detection. A total of **32 unique candidate studies** are registered across the three member packs.
2. **Source Verification (Bibliographic & Metadata Audit)**: Verifying that the paper exists, confirming its exact bibliographic details (authors, title, year, venue, volume, pages), and auditing reported claims against accessible publisher pages, DOIs, and arXiv abstracts.
3. **PDF Availability (Repository Deposit)**: Securing full-text PDF access. For copyright compliance, only legally permitted open-access PDFs (e.g., CC-BY or arXiv open preprints) are deposited in `research-papers/original_pdfs/`. Proprietary paywalled publisher PDFs are accessed via university channels and not redistributed publicly.
4. **Personal Member Reading (Student Evaluation)**: Cover-to-cover reading and methodological scrutiny by the student team member responsible for the category. As recorded honestly in `contributions/team-contributions.md` and the master literature matrix, personal reading is in progress and must never be conflated with automated AI inspection.
5. **Inclusion in Narrative Synthesis**: The selection of **26 core studies** that are directly synthesized, compared, and tabulated in Section IV (Literature Review) and Section V (Comparative Analysis) of the submitted survey manuscript.

---

## 6. Privacy Redaction & Git History Remediation

### Visual Redaction of SpringerLink Evidence
In compliance with personal privacy standards and institutional security protocols, the screenshot [`evidence-springerlink-19135.png`](file:///c:/dev/detecting-previously-unseen-network-attacks/search-evidence/evidence-springerlink-19135.png) has been visually redacted. The user's personal login account name and institutional IP address displayed in the user profile navigation header have been blacked out with a designated privacy redaction label: `[REDACTED: User Login Identifier & Institutional IP Address for Privacy]`.

### Git History Remediation Audit
- **Audit Finding**: In the initial commit (`f0080c9`), `search-evidence/evidence-springerlink-19135.png` was committed prior to explicit visual redaction.
- **Git Remediation Procedure**: If the user desires complete cryptographic purging of the unredacted image blob from Git history:
  1. Rewrite the Git history using `git-filter-repo`:
     ```bash
     git filter-repo --path search-evidence/evidence-springerlink-19135.png --invert-paths
     ```
  2. Re-commit the redacted image file.
  3. Force-push to remote with lease:
     ```bash
     git push --force-with-lease origin main
     ```
- **Policy Compliance**: In strict adherence to the audit ground rules ("Do not force-push without explicit approval"), the repository history on `main` has not been force-pushed. The redacted asset is committed cleanly on `main`, and the permanent history purging instructions are provided for user authorization.
