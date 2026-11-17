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
# Sheet 1: Deep Learning Papers (10 Unique Studies)
# -------------------------------------------------------------------------
ws1 = wb.create_sheet(title="Deep Learning Papers")
ws1.views.sheetView[0].showGridLines = True

headers1 = [
    "ID", "Evidence Category / Scope", "Title", "Authors", "Year", "Venue / Journal", 
    "DOI", "Publisher / Permanent Link", "OA-PDF Status & Archive Link", 
    "Method Family", "Method Architecture Summary", "Dataset / Testbed Used", 
    "Unseen Attack Holdout Protocol?", "Reported Findings / Performance", 
    "Limitations / Critical Caveats", "Publication Status", 
    "Source Review Status (Publisher Check)", "Team Reading Status (Declared by Ismayra)"
]
ws1.append(headers1)

dl_matrix_rows = [
    (
        "DL01",
        "Core: Direct Unknown-Attack Evidence",
        "Conditional Variational Auto-Encoder and Extreme Value Theory Aided Two-Stage Learning Approach for Intelligent Fine-Grained Known/Unknown Intrusion Detection",
        "Jian Yang; Xiang Chen; Shuangwu Chen; Xiaofeng Jiang; Xiaobin Tan",
        2021,
        "IEEE Transactions on Information Forensics and Security, vol. 16, pp. 3538–3553",
        "10.1109/TIFS.2021.3083422",
        "https://doi.org/10.1109/TIFS.2021.3083422",
        "Restricted / Paywalled (Store official DOI link; no legal OA PDF)",
        "Generative CVAE + Statistical EVT",
        "Two-stage pipeline: class-conditioned variational autoencoders (CVAE) represent known attack categories; Extreme Value Theory (EVT) models reconstruction error tails to flag novel/unknown attacks; benign clustering suppresses false alarms.",
        "CICIDS2017, UNSW-NB15 (Exact splits and holdout classes TO VERIFY from full paper).",
        "Yes (explicit known/unknown intrusion separation via EVT tail thresholding)",
        "Publisher abstract and secondary records report superior unknown attack detection rate with low false-positive rate compared to conventional autoencoders.",
        "Requires access to class-conditional latent distributions; EVT tail parameter estimation is sensitive to outlier contamination; exact metrics pending full-text extraction.",
        "Peer-reviewed Journal (IEEE TIFS)",
        "Bibliographic metadata verified; abstract and secondary full-paper record reviewed; complete experimental tables pending.",
        "Not yet confirmed by Ismayra; team member must personally read abstract, method, results and conclusion."
    ),
    (
        "DL02",
        "Core: Direct Unknown-Attack Evidence",
        "SFE-GACN: A Novel Unknown Attack Detection under Insufficient Data via Intra Categories Generation in Embedding Space",
        "Ao Liu; Yunpeng Wang; Tao Li",
        2021,
        "Computers & Security, vol. 105, article 102262 (June 2021)",
        "10.1016/j.cose.2021.102262",
        "https://doi.org/10.1016/j.cose.2021.102262",
        "Restricted / Subscription (Store official DOI link; no legal OA PDF)",
        "Session Embedding + Generative Adversarial Networks",
        "Session Feature Embedding (SFE) extracts sequential session context; Generative Adversarial Cooperative Network (GACN) generates intra-category synthetic samples in latent space to prevent boundary collapse under few-shot data.",
        "UNSW-NB15, CICIDS2017 (Specific few-shot splits and attack holdouts TO VERIFY).",
        "Yes (evaluates unknown attack detection under few-shot data constraints)",
        "Authors report average True Positive Rate (TPR) 8.38% higher and average False Positive Rate (FPR) 12.77% lower than baseline comparison methods.",
        "Results are strictly specific to the evaluated few-shot session embedding protocol; GAN training instability in high dimensions; full-text reading pending.",
        "Peer-reviewed Journal (Computers & Security)",
        "Bibliographic metadata and abstract reviewed; exact dataset splits and full experiment details pending.",
        "Not yet confirmed by Ismayra; team member must personally read abstract, method, results and conclusion."
    ),
    (
        "DL03",
        "Core: Direct Unknown-Attack Evidence",
        "A Deep Learning Ensemble Approach to Detecting Unknown Network Attacks",
        "Rasheed Ahmad; Izzat Alsmadi; Wasim Alhamdani; Lo'ai Tawalbeh",
        2022,
        "Journal of Information Security and Applications, vol. 67, article 103196 (June 2022)",
        "10.1016/j.jisa.2022.103196",
        "https://doi.org/10.1016/j.jisa.2022.103196",
        "Restricted / Subscription (Store official DOI link; no legal OA PDF)",
        "Deep Learning Ensemble",
        "Multi-model deep learning ensemble explicitly designed to flag network attacks never introduced during training.",
        "NSL-KDD, UNSW-NB15, CICIDS2017 (Exact architectures and benchmark splits TO VERIFY from full text).",
        "Yes (explicitly formulates detection of unintroduced attack categories)",
        "Publisher abstract confirms unknown-threat objective; reports improved detection across unseen attack injections over standalone models.",
        "Abstract does not expose individual per-class metrics or ensemble weighting schemes; full experimental extraction required from article.",
        "Peer-reviewed Journal (JISA)",
        "Bibliographic details and abstract verified; full experimental extraction pending.",
        "Not yet confirmed by Ismayra; team member must personally read abstract, method, results and conclusion."
    ),
    (
        "DL04",
        "Core: Direct Open-Set & Adaptation Evidence",
        "An Adaptable Deep Learning-Based Intrusion Detection System to Zero-Day Attacks",
        "Mahdi Soltani; Behzad Ousat; Mahdi Jafari Siavoshani; Amir Hossein Jahangir",
        2023,
        "Journal of Information Security and Applications, vol. 76, article 103516 (August 2023)",
        "10.1016/j.jisa.2023.103516",
        "https://doi.org/10.1016/j.jisa.2023.103516",
        "Permitted Author Preprint Available: research-papers/original_pdfs/DL04_Soltani_Preprint_2021.pdf (arXiv:2108.09199)",
        "Open-Set Recognition + Clustering + Adaptation",
        "Multi-stage pipeline: deep open-set classifier (DOC++) identifies novel samples outside known class bounds; clustering groups unknown samples for expert verification; verified groups are integrated via incremental retraining.",
        "CICIDS2017 and CSE-CIC-IDS2018 (Evaluated against DOC, OpenMax, and AutoSVM).",
        "Yes (evaluates open-set unknown attack detection and incremental class adaptation)",
        "Publisher abstract and preprint confirm DOC++ outperforms standard DOC, OpenMax, and AutoSVM on open-set novel-attack recognition.",
        "Separates detection from adaptation: safe updating still requires expert ground-truth validation; labelling latency in live networks; cite final 2023 journal version.",
        "Peer-reviewed Journal (JISA 2023; arXiv 2021 preprint archived)",
        "Journal metadata and arXiv preprint record verified; exact quantitative outcomes pending journal check.",
        "Not yet confirmed by Ismayra; read journal version where possible; preprint supports access."
    ),
    (
        "DL05",
        "Core: Unknown / OOD / Zero-Day & Adversarial",
        "A Sequential Deep Learning Framework for a Robust and Resilient Network Intrusion Detection System",
        "Soumyadeep Hore; Jalal Ghadermazi; Ankit Shah; Nathaniel D. Bastian",
        2024,
        "Computers & Security, vol. 144, article 103928 (September 2024)",
        "10.1016/j.cose.2024.103928",
        "https://doi.org/10.1016/j.cose.2024.103928",
        "Open Access (ScienceDirect CC-BY license; store publisher URL)",
        "Sequential Deep Architecture (Deep ResNIDS)",
        "Three-stage sequential pipeline: malicious-packet deep classifier handles known threats; anomaly autoencoder filters suspicious deviations; novelty autoencoder isolates true novel attacks from perturbed/adversarial variants; one-shot transfer learning.",
        "CICIDS2017, CSE-CIC-IDS2018 (used for OOD testing relative to 2017), botnet data, and generated adversarial samples.",
        "Yes (out-of-distribution, zero-day, and adversarial evasion tests)",
        "Authors report 98.5% average accuracy across evaluated attacks in sequential pipeline; effective discrimination of adversarial noise from new attacks.",
        "Critical Caveat: 98.5% is overall classification accuracy, NOT a standalone zero-day recall or open-set AUROC; individual OOD and retraining conditions must be reported separately.",
        "Peer-reviewed Journal (Computers & Security - Open Access)",
        "Publisher metadata, abstract, methodology, experimental setup, and conclusion text reviewed.",
        "Not yet confirmed by Ismayra; download/read full open-access article and record verified details."
    ),
    (
        "DL06",
        "Adjacent: Deep Learning Drift Adaptation",
        "An Online Transfer Learning Model for Intrusion Detection using FT-Transformer and KSWIN-Driven Concept Drift Detection Mechanism",
        "Zhaozhe Zhang; Hongpo Zhang",
        2024,
        "Proc. 5th International Conference on Computer Engineering and Application (ICCEA 2024), pp. 421–426",
        "10.1109/ICCEA62105.2024.10603489",
        "https://doi.org/10.1109/ICCEA62105.2024.10603489",
        "Restricted / IEEE Xplore (Store official DOI link; no legal OA PDF)",
        "FT-Transformer + Online Transfer Learning",
        "Feature Tokenizer Transformer (FT-Transformer) fine-tuned online when Kolmogorov-Smirnov Windowing (KSWIN) detects concept drift in continuous network streams.",
        "KDDCUP99, NSL-KDD, CIC-IDS dataset, NetFlow V2 (Exact splits TO VERIFY from full paper).",
        "No explicit unknown attack holdout (evaluates concept drift tracking)",
        "Abstract reports average accuracy of 99.46% on CIC-IDS and 96.79% on NetFlow V2 under concept drift adaptation.",
        "Critical Scope Caveat: Concept drift in feature distributions is NOT equivalent to holding out novel attack classes; categorized as drift adaptation, NOT proof of open-set zero-day detection.",
        "Peer-reviewed Conference (IEEE ICCEA 2024)",
        "IEEE metadata and abstract verified; full methods independently cross-checked against conference contents.",
        "Not yet confirmed by Ismayra; full-text reading required."
    ),
    (
        "DL07",
        "Core: Direct Open-Set Unknown-Traffic Evidence",
        "Unknown Intrusion Traffic Detection Method Based on Unsupervised Learning and Open-Set Recognition",
        "Jun Fang; Cunxiang Xie",
        2025,
        "Scientific Reports, vol. 15, article 17001 (16 May 2025)",
        "10.1038/s41598-025-01084-1",
        "https://doi.org/10.1038/s41598-025-01084-1",
        "Legally Downloaded & Archived: research-papers/original_pdfs/DL07_Fang_Xie_2025.pdf (Nature/PMC OA, 6.7 MB)",
        "Generative InfoGAN + OpenMax Scoring",
        "Information-Maximizing GAN (InfoGAN) learns disentangled latent representations of network traffic; OpenMax recalibrates activation vectors using Weibull distributions to calculate unknown-class probability.",
        "CICIDS2017 and NSL-KDD benchmark datasets.",
        "Yes (explicit open-set evaluation withholding attack categories; OpenMax vs. SoftMax)",
        "On CICIDS2017, reported open-set accuracy exceeds 88.5% for misuse detection and 88.2% for anomaly detection; NSL-KDD tables demonstrate OpenMax superiority over SoftMax for unknown classes.",
        "Per-class detection varies widely across attack modalities; Weibull tail parameter estimation requires careful tuning; exact held-out class breakdown must be reported from article tables.",
        "Peer-reviewed Journal (Nature Scientific Reports - Open Access)",
        "Full PMC/Nature article available; metadata, abstract, method, and experiment tables reviewed.",
        "Not yet confirmed by Ismayra; read original full text and note exact open-set split."
    ),
    (
        "DL08",
        "Core: Direct Open-Set Unknown-Attack Evidence",
        "Unknown Attack Detection Method Based on Deep Metric Learning",
        "Jianwei Zhang; Qinglong Wang; Zengyu Cai; Kejun Wang; Liang Zhu",
        2025,
        "Concurrency and Computation: Practice and Experience, vol. 37, issue 18–20, article e70193",
        "10.1002/cpe.70193",
        "https://doi.org/10.1002/cpe.70193",
        "Restricted / Wiley (Store official DOI link; no legal OA PDF)",
        "1D CNN + Deep Metric Learning",
        "1D Convolutional Neural Network trained with a composite loss (improved triplet loss + cross-entropy) to map traffic into compact hyperspherical clusters; class centroids updated via Weiszfeld algorithm; Mahalanobis distance threshold flags unknowns.",
        "CICIDS2017 and UNSW-NB15 benchmark datasets.",
        "Yes (metric clustering threshold identifies unknown attack samples outside class centroids)",
        "Publisher abstract reports average accuracy of 97.28% on CICIDS2017 and 85.47% on UNSW-NB15.",
        "Average accuracy figures reflect specific experimental openness ratios; Mahalanobis covariance estimation can be unstable under severe class imbalance; full-text check required.",
        "Peer-reviewed Journal (CCPE - Wiley)",
        "Publisher record, authors, abstract, DOI, datasets, and reported average accuracies verified.",
        "Not yet confirmed by Ismayra; full paper reading required."
    ),
    (
        "DL09",
        "Core: Direct Open-Set & Continuous Learning Evidence",
        "An Expert-in-the-Loop Framework for Unknown Attack Detection via Open-Set Recognition",
        "Xinjing Yuan; Peiran Yu; Song Liu; Zhe Sun; Yu Zhang; Jingdong Xu",
        2026,
        "Journal of Computer Security, vol. 34, issue 3, pp. 193–210 (First published online 10 Feb 2026)",
        "10.1177/0926227X251414058",
        "https://doi.org/10.1177/0926227X251414058",
        "Restricted / SAGE-IOS Press (Store official DOI link; no legal OA PDF)",
        "OpenPN + Human-in-the-Loop Clustering",
        "OpenPN open-set classifier flags novel traffic; density-based k-reciprocal nearest-neighbour clustering groups candidate attacks for human expert verification; verified new classes are incorporated via continual learning.",
        "Three public benchmark network intrusion datasets (names withheld in accessible abstract).",
        "Yes (open-set novel attack identification combined with continuous learning)",
        "Publisher abstract reports consistent gains in both closed-set accuracy and open-set recognition performance over state-of-the-art baselines.",
        "Publisher access is restricted; dataset names, openness ratios, and numerical confusion matrices are not exposed in abstract; requires institutional access.",
        "Peer-reviewed Journal (Journal of Computer Security)",
        "Publisher metadata and abstract verified; full author list extracted; numerical tables pending full text.",
        "Not yet confirmed by Ismayra; obtain institutional access or author copy before relying on details."
    ),
    (
        "DL10",
        "Contextual Only: Conventional Deep Learning Baseline",
        "Network-Based Intrusion Detection Using Deep Learning Technique",
        "Muhammad Farhan; Hafiz Waheed ud din; Saadat Ullah; Muhammad Sajjad Hussain; Muhammad Amir Khan; Tehseen Mazhar; Umar Farooq Khattak; Ines Hilali Jaghdam",
        2025,
        "Scientific Reports, vol. 15, article 25550 (15 July 2025)",
        "10.1038/s41598-025-08770-0",
        "https://doi.org/10.1038/s41598-025-08770-0",
        "Legally Downloaded & Archived: research-papers/original_pdfs/DL10_Farhan_2025.pdf (Nature Open Access, 2.3 MB)",
        "Conventional Deep Learning Classifier (Baseline)",
        "Standard deep neural network classifier evaluated on UNSW-NB15 with SMOTE class balancing and Extra Trees feature selection.",
        "UNSW-NB15: 175,341 records, 70/30 train/test split, binary and multi-class setups.",
        "NO (Standard closed-set evaluation; NO held-out attack classes)",
        "Achieves high classification metrics on standard closed-set splits of UNSW-NB15.",
        "Critical Interpretation Rule: Conventional closed-set classification; instances of all evaluated attack classes were present during training. Must NOT be presented as evidence of previously unseen attack detection. Contextual baseline only.",
        "Peer-reviewed Journal (Nature Scientific Reports - Open Access)",
        "Publisher metadata and accessible dataset/method snippet reviewed; full open-access PDF archived.",
        "Not yet confirmed by Ismayra; optional contextual paper, use only if full text checked."
    )
]

for row in dl_matrix_rows:
    ws1.append(row)

# -------------------------------------------------------------------------
# Sheet 2: Method Comparison
# -------------------------------------------------------------------------
ws2 = wb.create_sheet(title="Method Comparison")
ws2.views.sheetView[0].showGridLines = True

headers2 = [
    "Method Paradigm", "Paper ID", "Key Architecture / Mechanism", "Unknown Detection Principle", 
    "Reported Benchmark Evidence", "Key Operational Limitations"
]
ws2.append(headers2)

comparison_rows = [
    ("Generative & Reconstruction", "DL01", "CVAE + Extreme Value Theory (EVT)", "Reconstruction error modeled by EVT tail distribution; benign clustering prevents false alarms.", "Improved unknown attack detection and low FPR reported on benchmarks.", "EVT tail parameter estimation is sensitive to contaminated training samples; full metrics pending."),
    ("Few-Shot Generative", "DL02", "Session Feature Embedding (SFE) + GACN", "Generates intra-category latent samples to clarify boundaries under limited attack data.", "TPR +8.38%, FPR -12.77% over baselines in few-shot session evaluation.", "GAN training instability; gains tied to specific session-embedding assumptions."),
    ("Sequential Hybrid", "DL03", "Deep Learning Multi-Model Ensemble", "Combines complementary neural representations to flag unintroduced threats.", "Abstract confirms unknown threat detection superior to single models.", "Per-model weighting and per-class metrics unavailable in accessible abstract."),
    ("Open-Set + Adaptation", "DL04", "DOC++ Open-Set Classifier + Clustering", "1-vs-rest deep representations isolate novel samples; clustering groups them for expert review.", "DOC++ beats DOC, OpenMax, AutoSVM on CICIDS2017/2018 open-set holdout.", "Detection is automated, but model updating requires human labelling; latency in live streams."),
    ("Multi-Stage Sequential", "DL05", "Deep ResNIDS (Classifier + Anomaly AE + Novelty AE)", "Three-stage filtering: known classifier -> anomaly AE -> novelty AE (separates noise from attacks).", "98.5% overall accuracy; evaluates OOD, zero-day, and adversarial attacks.", "98.5% is overall accuracy across test sets, NOT dedicated zero-day recall; compute overhead."),
    ("Transfer Learning (Drift)", "DL06", "FT-Transformer + KSWIN Drift Detector", "Fine-tunes transformer weights online when statistical drift is detected.", "99.46% and 96.79% average accuracy on CIC-IDS and NetFlow streams under drift.", "Concept drift is not equivalent to unseen attack holdout; adjacent drift evidence only."),
    ("Generative Open-Set", "DL07", "InfoGAN + OpenMax Probability Scoring", "InfoGAN learns disentangled representations; OpenMax calculates unknown-class probability.", "CICIDS2017 open-set accuracy >88.5% (misuse) and >88.2% (anomaly); beats SoftMax on NSL.", "Weibull tail fitting requires tuning; high performance variance across attack modalities."),
    ("Deep Metric Learning", "DL08", "1D-CNN + Triplet Loss + Mahalanobis Threshold", "Learns compact class clusters; Mahalanobis distance flags outliers outside class centroids.", "Average accuracy 97.28% on CICIDS2017 and 85.47% on UNSW-NB15.", "Performance averages depend on experimental openness ratio; covariance matrix inversion cost."),
    ("Continual Open-Set", "DL09", "OpenPN + Expert Loop + Continual Learning", "OpenPN flags unknowns; reciprocal clustering groups them; expert verifies before continual update.", "Abstract reports superior closed-set and open-set recognition on 3 public datasets.", "Publisher access restricted; numerical matrices and dataset names unexposed in abstract."),
    ("Closed-Set Baseline", "DL10", "Conventional Deep Learning NIDS (CNN/LSTM)", "Standard multi-class probability output via SoftMax; forces input into known classes.", "High closed-set accuracy on UNSW-NB15 (70/30 split, SMOTE).", "NO unseen attack holdout; fails on zero-day attacks; included strictly as contextual baseline.")
]

for row in comparison_rows:
    ws2.append(row)

# -------------------------------------------------------------------------
# Sheet 3: Scope Demarcation & Evidence
# -------------------------------------------------------------------------
ws3 = wb.create_sheet(title="Scope Demarcation")
ws3.views.sheetView[0].showGridLines = True

headers3 = [
    "Evidence Category", "Eligible Papers", "Operational Definition & Criteria", 
    "Survey Paper Role (Section IV-B)", "Strict Interpretation Rule"
]
ws3.append(headers3)

scope_rows = [
    (
        "(a) Direct Open-Set / Unknown Attack Evidence",
        "DL01, DL02, DL03, DL04, DL05, DL07, DL08, DL09 (8 Studies)",
        "Models that explicitly incorporate an architectural mechanism (reconstruction error, EVT, OpenMax, metric distance, novelty autoencoder, 1-vs-rest DOC++) to identify samples belonging to none of the training classes, evaluated with held-out attack classes.",
        "Primary empirical evidence for Section IV-B analyzing how deep learning identifies previously unseen network attacks.",
        "Report exact openness ratios, held-out attack categories, and open-set metrics (AUROC, AUPRC, OpenAUC); do not conflate with closed-set accuracy."
    ),
    (
        "(b) Concept Drift Adaptation Evidence",
        "DL06 (Zhang & Zhang 2024)",
        "Models that detect and adapt to temporal distribution changes (covariate shift) in streaming network traffic without establishing that entire attack classes were withheld.",
        "Secondary adjacent evidence in Section IV-B discussing deep learning adaptation to dynamic network conditions.",
        "Must NOT be presented as direct proof of zero-day attack detection. Drift tracking and unknown class discovery are distinct operational problems."
    ),
    (
        "(c) Contextual Closed-Set IDS Evidence",
        "DL10 (Farhan et al. 2025)",
        "Standard deep learning intrusion detection models evaluated on conventional random train/test splits where all attack classes were present during training.",
        "Contextual baseline in Section IV-B illustrating conventional deep learning capabilities on benchmark datasets.",
        "Strict Directive: Do NOT present high accuracy from an ordinary multi-class split as proof of unseen-attack detection. Closed-world classifiers are fundamentally blind to zero-days."
    )
]

for row in scope_rows:
    ws3.append(row)

# -------------------------------------------------------------------------
# Sheet 4: Member Reading Checklist
# -------------------------------------------------------------------------
ws4 = wb.create_sheet(title="Member Reading Checklist")
ws4.views.sheetView[0].showGridLines = True

headers4 = [
    "Paper ID", "Short Title", "Abstract Checked", "Method Checked", 
    "Results Checked", "Conclusion Checked", "Full-Text Availability", "Current Honest Reading Status"
]
ws4.append(headers4)

checklist_rows = [
    ("DL01", "CVAE + EVT Unknown Intrusion Detection (Yang 2021)", "Publisher record", "Pending", "Pending", "Pending", "Restricted / IEEE Xplore", "Not yet confirmed by Ismayra; full reading pending."),
    ("DL02", "SFE-GACN Few-Shot Generation (Liu 2021)", "Publisher record", "Pending", "Pending", "Pending", "Restricted / Computers & Security", "Not yet confirmed by Ismayra; full reading pending."),
    ("DL03", "Deep Learning Ensemble Unknown Attacks (Ahmad 2022)", "Publisher record", "Pending", "Pending", "Pending", "Restricted / JISA", "Not yet confirmed by Ismayra; full reading pending."),
    ("DL04", "Adaptable Deep Learning Zero-Day (Soltani 2023)", "Publisher record", "Preprint checked", "Preprint checked", "Preprint checked", "OA Preprint Archived (arXiv:2108.09199)", "Preprint accessible; journal version reading pending."),
    ("DL05", "Sequential Deep ResNIDS (Hore 2024)", "Publisher record", "Publisher OA", "Publisher OA", "Publisher OA", "Open Access via ScienceDirect (CC-BY)", "Not yet confirmed by Ismayra; full OA reading pending."),
    ("DL06", "FT-Transformer Concept Drift (Zhang 2024)", "Publisher record", "Pending", "Pending", "Pending", "Restricted / IEEE ICCEA", "Not yet confirmed by Ismayra; full reading pending."),
    ("DL07", "InfoGAN + OpenMax Open-Set (Fang 2025)", "PMC/Nature OA", "PMC/Nature OA", "PMC/Nature OA", "PMC/Nature OA", "Full OA PDF Archived (Nature Sci Rep, 6.7 MB)", "Full PDF archived; personal reading pending by Ismayra."),
    ("DL08", "Deep Metric Learning Unknown Attacks (Zhang 2025)", "Publisher record", "Pending", "Pending", "Pending", "Restricted / Wiley CCPE", "Not yet confirmed by Ismayra; full reading pending."),
    ("DL09", "OpenPN Expert Loop Continual (Yuan 2026)", "Publisher record", "Pending", "Pending", "Pending", "Restricted / J. Computer Security", "Not yet confirmed by Ismayra; full reading pending."),
    ("DL10", "Network Deep Learning Baseline (Farhan 2025)", "Nature OA", "Nature OA", "Nature OA", "Nature OA", "Full OA PDF Archived (Nature Sci Rep, 2.3 MB)", "Contextual paper; personal reading pending by Ismayra.")
]

for row in checklist_rows:
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
            if col_num in [1, 5, 7, 13, 16] and len(val_str) < 25:
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

wb.save("literature-matrix/ismayra-papers.xlsx")
print("literature-matrix/ismayra-papers.xlsx generated successfully!")
