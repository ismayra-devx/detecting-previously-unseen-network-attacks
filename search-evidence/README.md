# Search Evidence Repository & Documentary Manifest

This directory (`search-evidence/`) preserves the official documentary evidence files supporting the literature search and identification phase of the research survey: **"Detecting Previously Unseen Network Attacks: A Survey of Machine Learning, Deep Learning, and Adaptive Approaches"**.

All documentary artifacts in this directory are directly referenced in `search-records.xlsx`, `search-methodology.md`, and the survey paper (Section II: Review Methodology).

---

## 1. Inventory of Evidence Files

| Evidence Filename | File Type | Target Engine / Repository | Displayed Metric / Captured Content | Status & Audit Note |
| :--- | :--- | :--- | :--- | :--- |
| **`evidence-ieee-xplore.png`** | PNG Image | IEEE Xplore Digital Library | **284 Results** displayed on platform interface | **Verified Documentary Evidence** (Platform displayed result count; not proof of a full BibTeX export) |
| **`evidence-acm-dl-444-standard.png`** | PNG Image | ACM Digital Library | **444 Results** displayed on platform interface | **Verified Documentary Evidence** (Standard research papers; displayed result count, not automatically 444 exported records; NEVER added to video results) |
| **`evidence-acm-dl-8-video.png`** | PNG Image | ACM Digital Library (Media Facet) | **8 Results** (Instructional & Presentation Video Media) | **Verified Documentary Evidence** (Screened out as multimedia; NEVER combined into 452) |
| **`evidence-springerlink-19135.png`** | PNG Image | SpringerLink / Springer Nature | **19,135 Results** displayed on platform search interface | **Verified Documentary Evidence & Redacted** (Personal login name and institutional IP address redacted prior to public release) |
| **`springer-export-1000.csv`** | CSV Data | SpringerLink / Springer Nature | **1,000 Records Exported** (Platform Maximum Export Cap) | **Verified Data Export** (Must NOT be reported as 19,135 exported records; 19,135 displayed and 1,000 exported kept distinct) |
| **`evidence-gscholar-16900-broad.png`** | PNG Image | Google Scholar (Search 1) | **About 16,900 results** (Broad Unfiltered Query) | **Verified Documentary Evidence** (Labeled *approximate*; query text in UI search box is truncated in screenshot; recorded separately) |
| **`evidence-gscholar-367-filtered.png`** | PNG Image | Google Scholar (Search 2) | **About 367 results** (Filtered NIDS 2021–2026 Query) | **Verified Documentary Evidence** (Labeled *approximate*; query text in UI search box is truncated in screenshot; recorded separately) |
| **`evidence-arxiv-zero-reported.png`** | PNG Image | arXiv.org (cs.CR / cs.LG) | **0 Results** (Query parser boolean limitation) | **Reported Result Pending Verification** (Syntax artifact; preprints found via targeted direct lookups) |

---

## 2. Strict Methodological Protocols Enforced

1. **Decoupling Displayed Result Counts from Bulk Export Claims**:
   - **ACM Digital Library**: The platform displayed **444 peer-reviewed research papers**. This is an on-screen displayed search count, not automatically 444 exported bibliographic records. Furthermore, 8 multimedia video presentations are recorded as a separate row and **NEVER summed together** into 452.
   - **IEEE Xplore**: The platform displayed **284 search results**. This is an on-screen displayed result count, not proof of a full BibTeX bulk export. Specific relevant studies were retrieved individually.
   - **SpringerLink**: The web interface displayed **19,135 total indexed records**. The platform enforces a strict technical ceiling of **1,000 records maximum** per CSV export. Consequently, exactly **1,000 records** were retrieved into `springer-export-1000.csv` for systematic offline evaluation. The 19,135 displayed results and 1,000 exported CSV records remain strictly distinct.

2. **Google Scholar Heuristic Estimates & Truncated Queries**:
   - Google Scholar does not report deterministic deduplicated record counts; its counter reflects an algorithmic estimate of matching web pages.
   - Both Search 1 (**About 16,900**) and Search 2 (**About 367**) are explicitly marked as **`approximate`**.
   - The query strings displayed in the Google Scholar search box in the captured evidence are visually truncated (`... [truncated in screenshot]`). Missing query tail parameters have NOT been reconstructed or guessed; they are recorded strictly as displayed.
   - Search 1 (broad concept family, all-time, any document type) and Search 2 (tightly filtered to 2021–2026, research articles only, excluding patents and citations) used fundamentally different filter sets and are documented as separate searches.

3. **arXiv Zero Result**:
   - arXiv returned **0 results** for the composite string `(open-set OR zero-day OR concept drift OR online learning) AND network intrusion`.
   - This was recorded honestly as **`0 (Reported result pending verification)`**. Technical audit revealed that arXiv's query parser does not support unparenthesized multi-operator boolean expressions across title/abstract fields. Preprints were subsequently identified through targeted title/author searches.

4. **No Fabricated Screening Numbers**:
   - While the 1,000 Springer records and top Google Scholar records underwent title/abstract appraisal, intermediate exclusion tallies across thousands of bulk hits were not tracked counter-by-counter during initial exploratory sweeps.
   - In accordance with academic integrity guidelines, unrecorded intermediate tallies are marked **`Not recorded (untracked bulk screening)`** rather than filled with fabricated numbers.

---

## 3. Privacy Redaction & Git History Remediation

### Visual Redaction
- In accordance with institutional data protection and privacy requirements, **`evidence-springerlink-19135.png`** has been visually redacted.
- The personal login username and institutional IP address displayed in the user banner have been covered with an opaque redaction block labeled: `[REDACTED: User Login Identifier & Institutional IP Address for Privacy]`.

### Git History Remediation Audit
- **Audit Finding**: In the initial commit (`f0080c9`), `search-evidence/evidence-springerlink-19135.png` was committed prior to explicit redaction.
- **Git Remediation Procedure**: To permanently purge sensitive personal identifiers and IP addresses from the Git object history:
  1. Use `git-filter-repo` or BFG Repo-Cleaner to rewrite history:
     ```bash
     git filter-repo --path search-evidence/evidence-springerlink-19135.png --invert-paths
     ```
  2. Re-add the redacted image and commit.
  3. Perform a force-push with lease:
     ```bash
     git push --force-with-lease origin main
     ```
- **Policy Compliance**: In strict adherence to audit instructions ("Do not force-push without explicit approval"), the repository history on `main` has not been rewritten without user permission. The updated, redacted asset is staged on the current commit, and the complete remediation procedure is submitted for explicit user authorization.
