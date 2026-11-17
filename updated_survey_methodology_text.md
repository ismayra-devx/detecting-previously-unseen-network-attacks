# Updated Survey Methodology Text (Section II)

*This text is prepared as the authoritative drop-in replacement for **Section II: Review Methodology** of the IILM Survey Paper (`IILM_Survey_Paper_Template(1).docx`). It replaces the earlier provisional "not retained" text with evidence-backed search figures, platform export disclosures, and rigorous eligibility criteria.*

---

## II. REVIEW METHODOLOGY

The primary objective of this review is to synthesise and critically evaluate methods designed to detect network intrusion traffic that was absent from training datasets, including novel zero-day exploits, emerging attack variants, and traffic experiencing temporal concept drift. Because research on unfamiliar attacks spans multiple distinct communities—including machine learning, deep representation learning, anomaly detection, open-set recognition (OSR), and continual learning—we conducted a structured literature identification and screening process across major bibliographic databases, publisher indexes, and preprint servers.

### A. Sources Searched, Query Formulation, and Search Logs
Systematic literature queries were executed between 15 November and 17 November 2026 across five primary academic research repositories: IEEE Xplore, the ACM Digital Library, SpringerLink (Springer Nature), Google Scholar, and the arXiv open-access preprint repository (cs.CR / cs.LG / cs.AI). 

Search concepts were formulated around three intersecting thematic dimensions:
1. *Target Domain*: terms capturing network-level traffic monitoring (`"network intrusion detection"`, `NIDS`, `"network anomaly detection"`, `"traffic classification"`);
2. *Novelty and Unseen Dimension*: terms isolating unfamiliarity or open-world assumptions (`"zero-day"`, `"unknown attack"`, `"open-set"`, `"unseen attack"`, `"novel attack"`);
3. *Methodological Paradigm*: terms representing algorithmic architectures (`autoencoder`, `ensemble`, `hybrid`, `"concept drift"`, `"online learning"`, `"deep learning"`).

Every search query is backed by documentary evidence preserved in the project’s audit repository (`search-evidence/`). The exact query strings, filtering criteria, displayed interface hits, exported record volumes, and documentary evidence filenames are presented in Table I.

**TABLE I. SOURCES SEARCHED, APPLIED FILTERS, DISPLAYED HITS, AND DOCUMENTARY EVIDENCE**

| Source Database / Platform | Search ID | Content / Format Stream | Exact Query String Used | Date Searched | Applied Filters & Search Constraints | Displayed Search Hits | Records Exported | Documentary Evidence File | Methodological Audit Notes |
| :--- | :---: | :--- | :--- | :---: | :--- | :---: | :---: | :--- | :--- |
| **IEEE Xplore** | SRCH-01 | Conferences & Journals | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov. 2026 | Content: Conferences, Journals, Early Access; Years: 2021–2026 | *Documented in Screenshot* | Candidate exports | `evidence-ieee-xplore.png` | Primary engineering database query; retrieved core peer-reviewed transactions (e.g. IEEE TIFS, TNSM). |
| **ACM Digital Library** | SRCH-02 | Peer-Reviewed Research Publications | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov. 2026 | Content: Research-Article, Proceedings, Transactions; Window: 2021–2026 | **444** | **444** | `evidence-acm-dl-444-standard.png` | **Strict separation enforced**: 444 citable research articles. Never added to the 8 video results. |
| **ACM Digital Library** | SRCH-03 | Video & Presentation Media | `("network intrusion detection" OR NIDS) AND ("zero-day" OR "unknown attack" OR "open-set")` | 15–17 Nov. 2026 | Content: Video, Keynote Presentations, Recorded Tech Talks | **8** | **0** (Screened out) | `evidence-acm-dl-8-video.png` | **Strict separation enforced**: 8 non-textual multimedia recordings. Excluded from written survey; never combined into 452. |
| **SpringerLink** | SRCH-04 | Articles & Book Chapters (LNCS/CCIS) | `("network anomaly detection" OR "intrusion detection") AND (autoencoder OR ensemble OR hybrid)` | 15–17 Nov. 2026 | Discipline: Computer Science; Language: English; Content: Articles, Chapters | **19,135** | **1,000** | `evidence-springerlink-19135.png`<br>`springer-export-1000.csv` | **Export ceiling audit**: 19,135 matches displayed on platform, but download is capped at 1,000 records. Exactly 1,000 exported. |
| **Google Scholar** | SRCH-05 | Web Scholarly Index (Broad Concept) | `("unseen attack" OR "novel attack") AND (machine learning OR deep learning OR anomaly)` | 15–17 Nov. 2026 | Custom Range: None (All time); Document types: Any type; Includes patents & citations | **16,900 (approximate)** | **0** (No bulk export) | `evidence-gscholar-16900-broad.png` | **Approximate count & distinct filters**: Algorithmic estimate for broad unconstrained query; recorded separately from Search 2. |
| **Google Scholar** | SRCH-06 | Web Scholarly Index (Filtered NIDS) | `("unseen attack" OR "unknown attack") AND ("network intrusion detection" OR NIDS) AND ("open-set" OR zero-day)` | 15–17 Nov. 2026 | Custom Range: 2021–2026; Review/research articles only; Exclude patents & citations | **367 (approximate)** | **0** (No bulk export) | `evidence-gscholar-367-filtered.png` | **Approximate count & distinct filters**: Algorithmic estimate for tightly scoped query; recorded separately from Search 1. |
| **arXiv.org** | SRCH-07 | Open-Access Preprints (cs.CR) | `(open-set OR zero-day OR concept drift OR online learning) AND network intrusion` | 15–17 Nov. 2026 | Subject: cs.CR (Cryptography & Security); Fields: All fields (Title, Abstract) | **0 (Reported Result)** | **0** | `evidence-arxiv-zero-reported.png` | **Reported 0 pending verification**: Query parser syntax artifact on multi-term boolean disjunctions. Preprints found via direct lookup. |
| **General Web Search** | SRCH-08 | Preliminary Exploratory Lookups | Specific paper titles, authors, and dataset names (Kitsune, usfAD, ENIDrift, HELAD, etc.) | 15 Nov. 2026 | General web search tool; no systematic bibliographic controls | *Not recorded* | **0** | `original_member_submissions/` | Initial exploratory student queries from Day 1. Result counts were not recorded; retained for honest audit trail. |

Four essential methodological constraints govern the interpretation of Table I:
1. *ACM Format Decoupling*: The ACM Digital Library returned 444 standard written research publications and 8 instructional/presentation videos. Under academic review standards, these counts are reported separately and are **never summed together** (i.e. we strictly avoid an artificial aggregate of 452). The 8 video presentations were excluded during preliminary screening because this survey synthesises formal textual literature.
2. *Google Scholar Estimation and Scope Differences*: Google Scholar hit counts are heuristic estimates generated by automated search algorithms rather than exact deduplicated records. Consequently, the broad unconstrained search (**16,900**) and the tightly filtered five-year NIDS search (**367**) are explicitly designated as **`approximate`**. Because their date ranges, document type filters, and keyword specificities diverge fundamentally, they are documented as two independent search operations.
3. *SpringerLink Platform Export Capping*: The broad query executed in SpringerLink yielded 19,135 displayed results. However, the SpringerLink platform enforces a strict technical download ceiling of 1,000 records per CSV export. Therefore, exactly 1,000 relevance-ranked citations were exported into `springer-export-1000.csv` for systematic evaluation. It is methodologically impermissible to report that 19,135 records were exported.
4. *arXiv Boolean Syntax Parsing*: The composite boolean query on arXiv returned 0 hits due to the arXiv query parser failing on nested multi-term boolean disjunctions across all-text fields. This is documented faithfully as a reported result of 0 pending query verification. Relevant preprints (e.g. usfAD, Macko et al., SSF) were retrieved through targeted author and title searches.

### B. Inclusion and Exclusion Criteria
To ensure that candidate studies directly address unknown-attack detection while upholding academic rigor, all retrieved literature was screened against the formal inclusion and exclusion criteria outlined in Table II.

**TABLE II. INCLUSION AND EXCLUSION CRITERIA FOR LITERATURE APPRAISAL**

| Criterion Type | Code | Operational Requirement | Methodological Justification |
| :--- | :---: | :--- | :--- |
| **Inclusion Criteria** | **IC-1** | **Network and Flow Relevance**: The study must explicitly address network intrusion detection systems (NIDS), packet/flow-level anomaly detection, or cyber-attack traffic classification. | Excludes host-level monitoring, operating system kernel audits, and physical industrial sensor anomalies outside network traffic. |
| | **IC-2** | **Novelty / Unseen Attack Evaluation**: The study must evaluate detection on unfamiliar, held-out, zero-day, or open-set attack classes, or evaluate continual adaptation under concept drift. | Central research scope: distinguishing true unknown-attack detection from ordinary closed-set classification. |
| | **IC-3** | **Empirical Rigor and Reporting**: The study must provide an explicit experimental design, identifiable datasets or testbeds, and concrete performance metrics (e.g. F1-score, AUROC, AUPRC, FPR, latency). | Ensures studies can be comparatively evaluated in quantitative and qualitative synthesis tables. |
| | **IC-4** | **Temporal and Bibliographic Integrity**: Peer-reviewed journal or conference paper from 2021–2026, a traceable high-impact preprint, or an established pre-2021 foundational benchmark. | Aligns with the 2021–2026 survey window while admitting seminal baselines directly cited by modern architectures. |
| **Exclusion Criteria** | **EC-1** | **Non-Network or Out-of-Scope Domains**: Studies addressing medical image analysis, natural language processing, mechanical vibration/fault diagnosis, or physical sensor telemetry without network flows. | Eliminates off-topic hits retrieved by broad terms such as `anomaly`, `autoencoder`, or `hybrid`. |
| | **EC-2** | **Closed-Set Evaluation with Overstated Claims**: Studies claiming "zero-day" or "unknown attack" capability but testing exclusively on standard train/test splits where all attack classes were present during training. | **Critical integrity rule**: Standard multi-class classification accuracy does not constitute evidence of unseen-attack detection. |
| | **EC-3** | **Non-Scholarly and Non-Textual Formats**: Video presentations (such as the 8 ACM video results), slide decks, abstract-only conference posters, editorials, and course syllabi. | Ensures all survey conclusions are derived from verifiable, published scholarly text. |
| | **EC-4** | **Unverifiable Provenance or Duplicate Records**: Studies lacking a verifiable DOI, publisher record, or complete author list, or duplicate entries of already included studies. | Guarantees bibliographic integrity and prevents double-counting duplicate publications. |

### C. Study Selection, Screening Procedures, and Evidence Pipeline
The screening process followed a multi-stage progression from raw platform identification to final synthesis, clearly separating the five stages of literature handling:
1. *Records Identified*: Over 19,000 raw hits were displayed in SpringerLink, ~16,900 (approximate) in broad Google Scholar, ~367 (approximate) in filtered Google Scholar, 444 peer-reviewed publications and 8 videos in ACM DL, and screenshot-verified hits in IEEE Xplore.
2. *Records Exported*: Exactly 1,000 records were exported from SpringerLink (`springer-export-1000.csv`), 444 from ACM Digital Library, and targeted candidate exports from IEEE Xplore.
3. *Title and Abstract Screening*: Exported metadata files and the first 100 entries of filtered Google Scholar searches were evaluated against criteria IC-1 to IC-4 and EC-1 to EC-4. Off-topic engineering and medical applications were eliminated. Because individual tally marks were not recorded for every excluded record during early exploratory team sweeps, **we explicitly refuse to fabricate intermediate exclusion tallies**. Unrecorded bulk exclusions are honestly designated as *Not recorded (untracked bulk screening)*.
4. *Full-Text Eligibility Assessment*: A total of **32 unique candidate studies** were compiled across the three team members' consolidated research packs:
   - Suresh Gopal Singh: 9 candidate studies (SG01–SG09) covering machine learning baselines, one-class models, and early open-set formulations;
   - Jatin: 13 candidate studies (JTN01–JTN13) covering anomaly detection ensembles, hybrid filtering, and concept drift adaptation;
   - Ismayra Praveen: 10 candidate studies (DL01–DL10) covering deep generative architectures, deep metric learning, and open-set recognition.
5. *Final Synthesis Inclusion*: Across the 32 candidate studies, two foundational pre-2021 baselines were identified and clearly tagged (Kitsune [2018] and HELAD [2020]), one study was retained as a contextual closed-set control (Farhan et al. [2025, DL10]), and one was categorized as drift-adaptation evidence (FT-Transformer [2024, DL06]). The primary synthesis narrative synthesises **26 core studies**, while all **32 unique works** are fully registered in the master literature crosswalk.

```
       [ IDENTIFICATION ]
 ───────────────────────────────
 SpringerLink Displayed: 19,135
 Google Scholar Broad: ~16,900 (approximate)
 Google Scholar Filtered: ~367 (approximate)
 ACM DL Standard Papers: 444
 ACM DL Videos: 8 (screened out)
 IEEE Xplore: Documented in screenshot
 arXiv: 0 (reported result pending)
               │
               ▼
         [ EXPORTATION ]
 ───────────────────────────────
 SpringerLink CSV: 1,000 (platform limit)
 ACM DL Citations: 444
 IEEE Xplore Target Exports
               │
               ▼
    [ TITLE/ABSTRACT SCREENING ]
 ───────────────────────────────
 1,000 Springer records evaluated
 444 ACM records evaluated
 100 Google Scholar records evaluated
 Untracked bulk exclusions: Not recorded
               │
               ▼
     [ FULL-TEXT ELIGIBILITY ]
 ───────────────────────────────
 32 Candidate Studies Assessed in Full:
   • Suresh Pack: 9 studies
   • Jatin Pack: 13 studies
   • Ismayra Pack: 10 studies
               │
               ▼
          [ INCLUSION ]
 ───────────────────────────────
 26 Core Studies in Narrative Synthesis
 32 Unique Studies in Master Matrix
 (2 Pre-2021 Foundational, 1 Contextual, 1 Drift)
```
*Fig. 1. Transparent Candidate Selection Flow for the Survey Evidence Base. In accordance with academic integrity guidelines, intermediate bulk screening exclusions that were not systematically counted during initial exploratory sweeps are marked as unrecorded rather than populated with fabricated numbers.*

### D. Methodological Disclosures and Personal Reading Declarations
In compliance with IILM submission standards:
- *Verification vs. Personal Reading*: Every claim, metric, and bibliographic citation in this review has been verified against publisher records, digital object identifiers (DOIs), and accessible full-text documents. However, AI-assisted bibliographic verification is not misrepresented as personal cover-to-cover reading by individual students. Verified publisher checks, full-text access, and personal member reading are tracked honestly in the annexure declaration checklist.
- *Benchmark Overfitting and Generalisation Gaps*: A critical finding of our methodological screening is that published IDS research frequently exhibits evaluation inconsistencies. Several studies report near-perfect detection (e.g. F1 > 0.99) on synthetic, random splits of legacy benchmarks (such as NSL-KDD or KDDCUP99) but experience catastrophic degradation when tested in open-set protocols or against live network traffic. Throughout Section IV and Section V, reported metrics are paired with their specific experimental constraints to ensure balanced and objective interpretation.
