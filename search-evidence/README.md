# Search Evidence Repository & Documentary Manifest

This directory (`search-evidence/`) preserves the official documentary evidence files supporting the literature search and identification phase of the research survey: **"Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches"**.

All documentary artifacts in this directory are directly referenced in `search-records.xlsx`, `search-methodology.md`, and the survey paper (Section II: Review Methodology).

---

## 1. Inventory of Evidence Files

| Evidence Filename | File Type | Target Engine / Repository | Displayed Metric / Captured Content | Status & Audit Note |
| :--- | :--- | :--- | :--- | :--- |
| **`evidence-ieee-xplore.png`** | PNG Image | IEEE Xplore Digital Library | Engineering transactions & conference search query interface | **Verified Documentary Evidence** |
| **`evidence-acm-dl-444-standard.png`** | PNG Image | ACM Digital Library | **444 Results** (Standard Research Publications & Proceedings) | **Verified Documentary Evidence** (Must NEVER be added to video results) |
| **`evidence-acm-dl-8-video.png`** | PNG Image | ACM Digital Library (Media Facet) | **8 Results** (Instructional & Presentation Video Media) | **Verified Documentary Evidence** (Screened out as multimedia; NEVER combined into 452) |
| **`evidence-springerlink-19135.png`** | PNG Image | SpringerLink / Springer Nature | **19,135 Results** displayed on platform search interface | **Verified Documentary Evidence** (High-recall query banner) |
| **`springer-export-1000.csv`** | CSV Data | SpringerLink / Springer Nature | **1,000 Records Exported** (Platform Maximum Export Cap) | **Verified Data Export** (Must NOT be reported as 19,135 exported records) |
| **`evidence-gscholar-16900-broad.png`** | PNG Image | Google Scholar (Search 1) | **About 16,900 results** (Broad Unfiltered Query) | **Verified Documentary Evidence** (Labeled *approximate*; recorded separately) |
| **`evidence-gscholar-367-filtered.png`** | PNG Image | Google Scholar (Search 2) | **About 367 results** (Filtered NIDS 2021–2026 Query) | **Verified Documentary Evidence** (Labeled *approximate*; recorded separately) |
| **`evidence-arxiv-zero-reported.png`** | PNG Image | arXiv.org (cs.CR / cs.LG) | **0 Results** (Query parser boolean limitation) | **Reported Result Pending Verification** (Syntax artifact; preprints found via direct lookup) |

---

## 2. Strict Methodological Protocols Enforced

1. **Strict Separation of ACM Formats**:
   - ACM Digital Library returned **444 peer-reviewed research papers** and **8 multimedia video presentations**.
   - These two counts are recorded as separate rows. Under academic review standards, they are **NEVER summed together** into 452. The 8 video presentations were excluded during preliminary screening because the survey strictly synthesizes written scholarly texts.

2. **SpringerLink Display vs. Export Capping**:
   - The query `("network anomaly detection" OR "intrusion detection") AND (autoencoder OR ensemble OR hybrid)` yielded **19,135 total indexed records** on the SpringerLink web interface.
   - However, the SpringerLink platform enforces a strict technical download ceiling of **1,000 records maximum** per CSV export.
   - Consequently, exactly **1,000 records** were retrieved into `springer-export-1000.csv` for systematic offline evaluation. It is methodologically impermissible to claim that 19,135 records were exported.

3. **Google Scholar Heuristic Estimates**:
   - Google Scholar does not report deterministic deduplicated record counts; its counter reflects an algorithmic estimate of matching web pages.
   - Both Search 1 (**16,900**) and Search 2 (**367**) are explicitly marked as **`approximate`**.
   - Search 1 (broad concept family, all-time, any document type) and Search 2 (tightly filtered to 2021–2026, research articles only, excluding patents and citations) used fundamentally different filter sets and are documented as separate searches.

4. **arXiv Zero Result**:
   - arXiv returned **0 results** for the composite string `(open-set OR zero-day OR concept drift OR online learning) AND network intrusion`.
   - This was recorded honestly as **`0 (Reported result pending verification)`**. Technical audit revealed that arXiv's query parser does not support unparenthesized multi-operator boolean expressions across title/abstract fields. Preprints were subsequently identified through targeted title/author searches.

5. **No Fabricated Screening Numbers**:
   - While the 1,000 Springer records and top 100 Google Scholar records underwent title/abstract appraisal, intermediate exclusion tallies across thousands of bulk hits were not tracked counter-by-counter during initial member sweeps.
   - In accordance with academic integrity guidelines, unrecorded intermediate tallies are marked **`Not recorded (untracked bulk screening)`** rather than filled with fabricated numbers.
