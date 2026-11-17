import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
wb.remove(wb.active) # Remove default sheet

# Colors
navy_header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
data_font = Font(name="Calibri", size=10)
bold_font = Font(name="Calibri", size=10, bold=True)
thin_border = Border(
    left=Side(style='thin', color='D9D9D9'),
    right=Side(style='thin', color='D9D9D9'),
    top=Side(style='thin', color='D9D9D9'),
    bottom=Side(style='thin', color='D9D9D9')
)

# -------------------------------------------------------------------------
# Sheet 1: Suresh Papers Matrix (9 Unique Papers)
# -------------------------------------------------------------------------
ws1 = wb.create_sheet(title="Suresh Papers Matrix")
ws1.views.sheetView[0].showGridLines = True

headers1 = [
    "Paper ID", "Paper Title", "Authors", "Year", "Venue / Publication", 
    "DOI / Permanent URL", "Publication Type", "Time Window (2021-2026)", "Category / Approach", 
    "Problem Addressed", "Method / Model Architecture", "Dataset / Testbed Used", 
    "Evaluation Measures / Metrics", "Reported Findings / Performance", 
    "Limitations / Critical Notes", "Adapts to Change / New Attacks?", 
    "Honest Reading Status", "Day 3 Verification Status", "Source Cross-Reference"
]
ws1.append(headers1)

suresh_matrix_rows = [
    (
        "SG01",
        "A Review of Machine Learning-Based Zero-Day Attack Detection: Challenges and Future Directions",
        "Yang Guo",
        2023,
        "Computer Communications, vol. 198, pp. 175–185",
        "https://doi.org/10.1016/j.comcom.2022.11.001",
        "Journal Article (Survey)",
        "Yes (2021-2026 Window)",
        "Signature Limits & ML Overview (Survey)",
        "Signature-based detection cannot catch zero-day attacks because no signature exists in advance; reviews machine learning alternatives, operational challenges, and open research directions.",
        "Systematic survey comparing supervised, unsupervised, and hybrid ML models applied to zero-day network attack detection across published studies.",
        "Comparative survey across benchmark datasets reported in reviewed studies; no new experiments.",
        "Comparative qualitative review of reported accuracy, recall, and detection metrics.",
        "Existing ML methods face severe challenges in detection consistency and recall across diverse attack types; provides background taxonomy for signature limitations.",
        "Survey paper; provides no new empirical experiments or benchmark evaluations; claim regarding ML lacking consistency removed from draft until full text verified.",
        "No (survey of static and dynamic approaches)",
        "Abstract and catalogue record verified; full text to be read by Suresh",
        "Fully Verified against journal catalogue record (Day 3 Audit)",
        "Suresh Day 1 (P1), Suresh Day 2 ([P1]), Suresh Day 3 (P1), Consolidated (SG01), Existing Draft ([1])"
    ),
    (
        "SG02",
        "usfAD Based Effective Unknown Attack Detection Focused IDS Framework",
        "Md. Ashraf Uddin, Sunil Aryal, Mohamed Reda Bouadjenek, Muna Al-Hawawreh, Md. Alamin Talukder",
        2024,
        "arXiv preprint arXiv:2403.11180",
        "https://arxiv.org/abs/2403.11180",
        "Preprint (arXiv)",
        "Yes (2021-2026 Window)",
        "Supervised Blind Spot vs. One-Class usfAD",
        "Supervised IDSs require massive attack samples and fail catastrophically on unknown/zero-day attacks; investigates whether semi-supervised and one-class models trained without attack samples perform better.",
        "Random Forest with attack classes removed from training; RF with synthetic noise labelled as attacks; one-class models (LOF, One-Class SVM, Isolation Forest, AE, VAE) and usfAD (stochastic-forest anomaly detector) plus ensembles.",
        "10 benchmark IDS datasets (NSL-KDD, UNSW-NB15, CIC-DDoS2019, ToN-IoT-Network, XIIoTID, Malmem2022, ISCXURL2016, etc.); stratified 80/20 splits across 10 runs.",
        "Accuracy, precision, recall, F1-score (evaluated on attack class).",
        "Verified: RF F1 falls to 0% (accuracy 51.88%) on NSL-KDD when 4 attack classes are withheld (RF simply labels unknown attacks as normal). usfAD maintains steady performance: 99.43% on ToN-IoT-Network. Note internal paper discrepancy: text reports 80.23% accuracy on UNSW-NB15 while Table 2 reports 82.15%.",
        "usfAD recall is limited on UNSW-NB15 (74.33%), Darknet2020 (70.40%), and XIIoTID (87.92%); authors' actual limitation: random noise does not cover the high-dimensional binary space and is computationally costly.",
        "Yes (one-class anomaly framework detects deviations without attack-class training)",
        "Checked by AI and verified against arXiv text/tables; full reading by Suresh pending",
        "Verified with corrections (51.88% accuracy added; noise limitation corrected; 80.23% vs 82.15% noted)",
        "Suresh Day 1 (P2), Suresh Day 2 ([P2]), Suresh Day 3 (P2), Consolidated (SG02), Existing Draft ([3])"
    ),
    (
        "SG03",
        "Comparing Autoencoder and Isolation Forest in Network Anomaly Detection",
        "Timotej Smolen, Lenka Benova",
        2023,
        "Proc. 33rd Conf. Open Innovations Association (FRUCT)",
        "https://www.fruct.org/files/publications/volume-33/fruct33/Smo.pdf",
        "Conference Proceeding",
        "Yes (Year to confirm from printed volume)",
        "Unsupervised Anomaly Detection (Unlabelled Data)",
        "Detect cyber-attacks and novel anomalies in real-world unlabelled network traffic without ground-truth labels; directly compare autoencoders against tree-based Isolation Forest.",
        "LSTM-based Recurrent Autoencoder (RAE, reconstruction error) vs. Isolation Forest (200 trees, contamination factor 0.05).",
        "Private web-server request logs from an antivirus vendor: 1 day, 90,910,622 requests, 11 attributes, unlabelled; evaluation on 1,000,000-sample test slice.",
        "Score distributions, mean absolute difference of anomaly scores (0.17), manual qualitative review of top-100 anomalies, prediction latency.",
        "Verified: Autoencoder is significantly faster at 0.099 s vs. 0.468 s per 1,000 samples (due to GPU acceleration). Verified: zero overlap in top-100 anomaly lists between the two models. RAE excels on missing features; IF on extreme numerical outliers.",
        "Without ground-truth labels, standard classification metrics (accuracy, precision, recall, F1, AUROC) could not be computed; zero-day detection effectiveness is inferred from anomaly score properties rather than proven against attack labels.",
        "Partially (unsupervised scoring flags outliers but produces uncalibrated alerts)",
        "Verified against FRUCT PDF; full text understanding to be completed by Suresh",
        "Verified with caveats (90.9M records, latency, GPU note verified; publication year 2023 marked to confirm)",
        "Suresh Day 1 (P3), Suresh Day 2 ([P3]), Suresh Day 3 (P3), Consolidated (SG03), Existing Draft ([4])"
    ),
    (
        "SG04",
        "Combining Unsupervised Approaches for Near Real-Time Network Traffic Anomaly Detection",
        "Francesco Carrera, Vincenzo Dentamaro, Stefano Galantucci, Andrea Iannacone, Donato Impedovo, Giuseppe Pirlo",
        2022,
        "Applied Sciences (MDPI), vol. 12, no. 3, Art. no. 1759",
        "https://doi.org/10.3390/app12031759",
        "Journal Article (Open Access)",
        "Yes (2021-2026 Window)",
        "Hybrid Unsupervised Anomaly Pipelines",
        "Detect zero-day network attacks in near real-time using strictly unsupervised learning while maintaining high throughput and low false alarm rates.",
        "Three deep autoencoder hybrids: DAGMM-EIF, DA-EIF, and MemAE-EIF (Memory-augmented Autoencoder feeding Extended Isolation Forest); SHAP feature explainability.",
        "KDDCUP99, NSL-KDD, CIC-IDS2017; 10-fold cross-validation on numerical features.",
        "Precision, recall, F1-score, AUROC, accuracy, prediction latency.",
        "Verified exact F1 values: MemAE-EIF achieved 0.9234 on KDDCUP99, 0.9172 on NSL-KDD, and 0.7146 on CIC-IDS2017 (CIC value inferred from text as table was truncated). Adding EIF improved detection accuracy over standalone autoencoders but increased inference latency.",
        "Requires GPU for real-time inference; Extended Isolation Forest is memory-heavy and non-parallelisable; anomaly decision threshold was calibrated using the known share of anomalies in the test set (unrealistic for operational deployment).",
        "Partially (unsupervised anomaly detection; static thresholds)",
        "Verified against MDPI article page; full text to be read by Suresh",
        "Fully Verified (Exact F1 values 0.9234/0.9172/0.7146 enforced; GPU/EIF memory caveats confirmed)",
        "Suresh Day 1 (P4), Suresh Day 2 ([P4]), Suresh Day 3 (P4), Consolidated (SG04), Existing Draft ([5])"
    ),
    (
        "SG05",
        "A Novel Open Set Energy-Based Flow Classifier for Network Intrusion Detection",
        "Manuela M. C. Souza, Camila Pontes, Joao Gondim, Luis P. F. Garcia, Luiz DaSilva, Marcelo A. Marotta",
        2021,
        "arXiv preprint arXiv:2109.11224 (published Computers & Security 2025)",
        "https://arxiv.org/abs/2109.11224",
        "Preprint / Journal",
        "Yes (2021-2026 Window)",
        "Statistical Open-Set Recognition (EFC)",
        "Most NIDS assume train and test traffic share identical distributions; real networks encounter new attack classes. Existing open-set classifiers exhibit severe latency and low throughput.",
        "Multi-class Energy-based Flow Classifier (EFC) derived from the Potts model; flows with energy exceeding the 95th percentile threshold are classified as 'suspicious' (potential novel attack). Compared against DT, MLP, SVM, ODIN, and OCN.",
        "CICIDS2017 (original version plus corrected version by Zhang et al.).",
        "Macro F1 (closed-set 5-fold CV); unknown-attack classification; AUROC and AUPRC for open-set evaluation.",
        "Verified closed-set: best macro F1 of 0.752 (vs DT 0.731, MLP 0.693, SVM 0.490) and third-best weighted F1 (0.940). Verified open-set: average AUROC 0.859 (vs OCN 0.938) and average AUPRC 0.993 (vs OCN 0.935).",
        "Verified: Bot, PortScan, and Web Attack classes were almost totally misclassified when held out as unknown; relies on a static 95th-percentile energy threshold; severe class imbalance in rare classes.",
        "Yes (open-set thresholding identifies flows outside known class energy boundaries)",
        "Verified against arXiv page and tables; full text to be read by Suresh",
        "Verified with corrections (6 arXiv authors confirmed; venue/2025 date removed from arXiv record; 'almost totally misclassified' enforced)",
        "Suresh Day 1 (P5), Suresh Day 2 ([P5]), Suresh Day 3 (P5), Consolidated (SG05), Existing Draft ([7])"
    ),
    (
        "SG06",
        "Detecting Unknown Attacks in IoT Environments: An Open Set Classifier for Enhanced Network Intrusion Detection",
        "Yasir Ali Farrukh, Syed Wali, Irfan Khan, Nathaniel D. Bastian",
        2023,
        "arXiv preprint arXiv:2309.07461",
        "https://arxiv.org/abs/2309.07461",
        "Preprint (arXiv)",
        "Yes (2021-2026 Window)",
        "Payload-Based Open-Set Recognition",
        "Closed-world NIDS fail to detect previously unseen attacks in resource-constrained IoT environments; requires an open-set classifier operating directly on packet payloads.",
        "Packet payloads transformed into serialized RGB image arrays; benign traffic partitioned into 7 clusters via K-means; 7 parallel CNN base learners; meta-classifiers (RF, Logistic Regression, XGBoost, LightGBM) with ensemble voting.",
        "CIC-IDS2017 packet payload captures (processed via Payload-Byte tool); five held-out attack classes claimed in notes (DoS Hulk, DoS slowloris, DoS Slowhttptest, Web Attack-SQLi, Bot) - TO VERIFY from full text.",
        "Sensitivity (detection rate on unseen attacks) and specificity on benign traffic.",
        "Verified: 88% detection rate on unknown attack traffic. Note: Day 3 audit removed older claims of 37% higher specificity than ECOD and 17% higher sensitivity than PReNet as they were not found in accessible text.",
        "Foundational/preliminary study; comparisons with ECOD/PReNet derived from unverified figures; evaluation across varying openness ratios left as future work; five held-out classes flagged for full-text confirmation.",
        "Yes (open-set meta-classifier detects unseen attack payloads)",
        "Abstract verified; full text to be read by Suresh to confirm held-out classes",
        "Verified with corrections (88% verified; ECOD/PReNet percentages removed; 5 held-out classes flagged as pending proof)",
        "Suresh Day 1 (P6), Suresh Day 2 ([P6]), Suresh Day 3 (P6), Consolidated (SG06), Existing Draft ([8])"
    ),
    (
        "SG07",
        "Neuro-symbolic Integration for Open Set Recognition in Network Intrusion Detection",
        "Alice Bizzarri, Chung-En Yu, Brian Jalaian, Fabrizio Riguzzi, Nathaniel D. Bastian",
        2025,
        "Springer LNCS vol. 15450, pp. 50–63 (AIxIA 2024)",
        "https://doi.org/10.1007/978-3-031-80607-0_5",
        "Conference / Book Chapter",
        "Yes (2021-2026 Window)",
        "Deep Clustering + XGBoost Open-Set Recognition",
        "Detect previously unknown network attacks (open set) while overcoming covariate shift between heterogeneous network environments.",
        "TEX-DEC: Deep Embedding for Clustering (DEC) trained with a composite loss (KL divergence, supervised contrastive, classification), followed by an XGBoost classifier trained on latent embeddings to separate known from novel samples.",
        "CIC-IDS2017 packet data (known, novelty 1, novelty 2 splits); UNSW-NB15 used for cross-dataset covariate-shift evaluation; MNIST non-network baseline.",
        "Area Under the Receiver Operating Characteristic (AUROC).",
        "Verified exact AUROC values: Infiltration (0.9843), SSH-Patator (0.9939), FTP-Patator (0.9950, vs. 0.9957 for Matejek et al.); achieved 0.9939 on UNSW-NB15 cross-dataset covariate shift (vs. 0.9583 for Matejek et al.).",
        "XGBoost stage is trained with a small set of novel-class examples (Novelty 1 split), meaning the framework requires access to some novel attack instances; only 3 novel attack types evaluated on CIC-IDS2017.",
        "Yes (latent clustering isolates novel traffic; cross-dataset shift evaluated)",
        "Verified against ml.unife.it PDF; full text to be read by Suresh",
        "Fully Verified (Venue corrected to Springer LNCS vol. 15450; exact AUROC values and Matejek comparison confirmed)",
        "Suresh Day 1 (P7), Suresh Day 2 ([P7]), Suresh Day 3 (P7), Consolidated (SG07), Existing Draft ([9])"
    ),
    (
        "SG08",
        "A Hybrid Machine Learning Approach for Enhancing Intrusion Detection Systems Using CICIDS2017 Dataset",
        "Ara Zozan Miran, Govand Salih Kadir",
        2026,
        "Dasinya Journal for Engineering and Informatics, vol. 2, no. 2, pp. 16–25",
        "https://doi.org/10.65542/djei.v2i2.49",
        "Journal Article",
        "Yes (2021-2026 Window)",
        "Supervised vs. Unsupervised ML Comparison",
        "Signature-based IDSs suffer from high false-positive rates; evaluate classical ML algorithms using OSI layer 2 and layer 3 features for detecting known threats and anomalies.",
        "Random Forest and XGBoost (supervised) vs. Isolation Forest and One-Class SVM (unsupervised); PCA feature reduction, SMOTE class balancing, and grid search hyperparameter tuning.",
        "CICIDS2017: 1,668,530 records (1,402,023 benign, 266,507 attack); stated 60/20/20 split.",
        "Accuracy, precision, recall, F1-score; paired t-test statistical validation.",
        "Verified: XGBoost achieved best performance (99.3% accuracy, 99.4% F1); Random Forest reached 98.8% accuracy (99.0% F1). Verified: One-Class SVM achieved 92.1% accuracy and 59.2% recall (70.5% F1); Isolation Forest achieved 91.6% accuracy and 59.7% recall (69.5% F1).",
        "Discrepancies flagged: stated 60/20/20 split does not match record counts (yields 56.2/18.8/25.0%); article number cited inconsistently as 16 and 17 on different PDF pages; peer-review status not explicitly stated; class-level holdout not described (closed-set evaluation).",
        "No (standard random train/test split; class holdout not described)",
        "Verified against Dasinya PDF; full reading by Suresh pending",
        "Verified with discrepancies flagged (Split mismatch 56/19/25 noted; article 16/17 flagged; holdout wording corrected)",
        "Suresh Day 1 (P8), Suresh Day 2 ([P8]), Suresh Day 3 (P8), Consolidated (SG08)"
    ),
    (
        "SG09",
        "A Novel Contrastive Loss for Zero-Day Network Intrusion Detection",
        "Jack Wilkie, Hanan Hindy, Craig Michie, Christos Tachtatzis, James Irvine, Robert Atkinson",
        2026,
        "IEEE Transactions on Network and Service Management (arXiv:2601.09902)",
        "https://arxiv.org/abs/2601.09902",
        "Journal Article / Preprint",
        "Yes (2021-2026 Window)",
        "Contrastive Open-Set Learning (CLAD / CLOSR)",
        "Supervised classifiers fail catastrophically on zero-day attacks; unsupervised anomaly detectors produce excessive false alarms.",
        "Contrastive Loss for Anomaly Detection (CLAD, models benign traffic as a von Mises-Fisher distribution on a hypersphere) and its multi-class open-set extension CLOSR (incorporates known attack boundaries); evaluated against 9 baselines (IF, SVM, AEs, Deep SVDD, OpenMax, DOC, CROSR, Siamese).",
        "Lycos2017 (standardized CIC-IDS2017): 1,789,954 flows, 14 classes; Heartbleed and SQL Injection held out strictly as zero-day attacks.",
        "Open-set AUROC, FPR@95, closed-set accuracy, OpenAUC, precision, recall, F1.",
        "Verified exact metrics: CLAD reached mean open-set AUROC of 0.9966 (0.996627) vs. 0.9357 (0.935744) for best baseline (DUAD). Verified: CLOSR reached OpenAUC of 0.9694 (0.969420) vs. 0.7985 (0.798537) for multi-stage baseline.",
        "Network structure requires one projection head per class, increasing complexity with category count; not tested against deliberate adversarial attacks or noisy training data; IEEE TNSM venue inferred from DOI prefix.",
        "Yes (contrastive hyperspherical boundaries isolate zero-day attacks in open set)",
        "Verified against arXiv PDF; full text to be read by Suresh",
        "Verified with corrections (Held-out classes and exact AUROC confirmed; IEEE TNSM venue pending; unsupported claims removed)",
        "Suresh Day 1 (P9), Suresh Day 2 ([P9]), Suresh Day 3 (P9), Consolidated (SG09), Existing Draft ([10])"
    )
]

for row in suresh_matrix_rows:
    ws1.append(row)

# -------------------------------------------------------------------------
# Sheet 2: Verification Audit Log (All 51 Claims from Day 3 Report)
# -------------------------------------------------------------------------
ws2 = wb.create_sheet(title="Verification Audit Log")
ws2.views.sheetView[0].showGridLines = True

headers2 = [
    "Claim ID", "Paper Ref", "Audited Claim / Metric", "Checked Against", 
    "Verification Result", "Enforced Action / Status"
]
ws2.append(headers2)

import docx
doc3 = docx.Document('source_material/original_member_submissions/Suresh_Day3_Verification_Report.docx')
t_claims = doc3.tables[0]
for idx, r in enumerate(t_claims.rows[1:], 1):
    ref = r.cells[0].text.strip()
    claim = r.cells[1].text.strip()
    source = r.cells[2].text.strip()
    res = r.cells[3].text.strip()
    act = r.cells[4].text.strip()
    ws2.append([f"CLM{idx:02d}", ref, claim, source, res, act])

# -------------------------------------------------------------------------
# Sheet 3: Search Log Audit
# -------------------------------------------------------------------------
ws3 = wb.create_sheet(title="Search Log Audit")
ws3.views.sheetView[0].showGridLines = True

headers3 = [
    "Log ID", "Date of Search", "Search Tool / Engine", "Exact Search String", 
    "Reported Hit Count", "Audit Status / Caveat", "Required Action for Final Submission"
]
ws3.append(headers3)

search_log_rows = [
    ("LOG-S01", "15 Nov 2026", "General web search", "open-set recognition network intrusion detection unknown attacks", "not recorded", "Historical search query without result counts", "Execute repeat search in IEEE Xplore / ACM DL / Google Scholar and record real hit counts."),
    ("LOG-S02", "15 Nov 2026", "General web search", "unsupervised anomaly detection isolation forest network intrusion zero-day", "not recorded", "Historical search query without result counts", "Execute repeat search in IEEE Xplore / ACM DL / Google Scholar and record real hit counts."),
    ("LOG-S03", "15 Nov 2026", "General web search", "supervised machine learning random forest XGBoost unknown attack detection IDS", "not recorded", "Historical search query without result counts", "Execute repeat search in IEEE Xplore / ACM DL / Google Scholar and record real hit counts."),
    ("LOG-S04", "15 Nov 2026", "General web search", "zero-day attack detection machine learning survey network intrusion", "not recorded", "Historical search query without result counts", "Execute repeat search in IEEE Xplore / ScienceDirect and record real hit counts."),
    ("LOG-S05", "15 Nov 2026", "General web search", "VAEMax Open-Set Intrusion Detection OpenMax Variational Autoencoder arxiv", "not recorded", "Candidate seen but excluded: arXiv 2403.04193 (insufficient text read)", "Tracked in excluded candidates pool."),
    ("LOG-S06", "15 Nov 2026", "General web search", "RPM-Net Recurrent Prototype Matching network intrusion detection arxiv", "not recorded", "Candidate seen but excluded: arXiv 2604.06638 (insufficient text read)", "Tracked in excluded candidates pool."),
    ("LOG-S07", "15 Nov 2026", "General web search", "anomaly detection algorithms comparison network security benchmark 2020", "not recorded", "Candidate seen but excluded: arXiv 2012.11354 (published 2020, falls outside 2021-2026 window)", "Tracked in excluded candidates pool.")
]

for row in search_log_rows:
    ws3.append(row)

# -------------------------------------------------------------------------
# Sheet 4: Gaps & Future Directions
# -------------------------------------------------------------------------
ws4 = wb.create_sheet(title="Gaps & Future Directions")
ws4.views.sheetView[0].showGridLines = True

headers4 = [
    "Gap ID", "Research Gap Title", "Supporting Evidence from Suresh Category", "Proposed Research Direction"
]
ws4.append(headers4)

gaps_directions_rows = [
    (
        "SG-G1",
        "Closed-set classification metrics are frequently conflated with true zero-day detection",
        "SG08 reports high overall accuracy (99.3% XGBoost) but does not isolate attack classes during training; in SG02, Random Forest dropped from 99%+ to 0% F1 on NSL-KDD once four attack types were removed, simply classifying unknown traffic as normal.",
        "Enforce standardized leave-attack-family-out (LAFO) experimental splits, mandating open-set metrics (OpenAUC, AUROC, FPR@95) rather than closed-set accuracy or weighted F1."
    ),
    (
        "SG-G2",
        "Unsupervised anomaly detection suffers from severe false alarms and model disagreement",
        "In SG03, Autoencoder and Isolation Forest flagged completely disjoint top-100 anomaly sets (0% overlap) across 90.9M requests; in SG08, One-Class SVM achieved only 59.2% recall on anomaly detection; SG04 relies on an artificial threshold tuned on known anomaly shares.",
        "Calibrate decision thresholds using only deployable benign validation distributions, and develop calibrated uncertainty estimation for anomaly scoring."
    ),
    (
        "SG-G3",
        "Open-set classifiers fail to detect subtle, low-footprint attack categories",
        "In SG05, the Energy-based Flow Classifier (EFC) almost totally misclassified Bot, PortScan, and Web Attack categories when held out as unknowns; open-set recognition exhibits high variance across attack modalities.",
        "Combine representation learning with multi-view feature projections to separate stealthy, multi-packet attacks from benign variations in flow energy."
    ),
    (
        "SG-G4",
        "Architectural scalability and deployment overhead in multi-class open-set models",
        "SG09 (CLAD/CLOSR) requires a distinct projection head for every known class, causing parameter growth as classes expand; SG04 requires dedicated GPU hardware for inference and suffers from high memory consumption in Extended Isolation Forest.",
        "Design lightweight projection spaces and dynamic head architectures that scale sub-linearly with known attack categories on resource-constrained network appliances."
    )
]

for row in gaps_directions_rows:
    ws4.append(row)

# Formatting for all sheets
for ws in wb.worksheets:
    for col_num in range(1, ws.max_column + 1):
        cell = ws.cell(row=1, column=col_num)
        cell.fill = navy_header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 28
    
    for row_num in range(2, ws.max_row + 1):
        ws.row_dimensions[row_num].height = 22
        for col_num in range(1, ws.max_column + 1):
            cell = ws.cell(row=row_num, column=col_num)
            cell.font = data_font
            cell.border = thin_border
            val_str = str(cell.value or '')
            if col_num in [1, 4, 7, 8, 16] and len(val_str) < 25:
                cell.alignment = Alignment(horizontal="center", vertical="center")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=False)
                
    for col in ws.columns:
        max_len = 0
        col_letter = get_column_letter(col[0].column)
        for cell in col:
            val_str = str(cell.value or '')
            if '\n' in val_str:
                val_str = max(val_str.split('\n'), key=len)
            max_len = max(max_len, len(val_str))
        ws.column_dimensions[col_letter].width = min(max(max_len + 3, 12), 48)

wb.save("literature-matrix/suresh-papers.xlsx")
print("literature-matrix/suresh-papers.xlsx generated successfully!")
