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
# Sheet 1: Jatin Papers Matrix (13 Unique Papers)
# -------------------------------------------------------------------------
ws1 = wb.create_sheet(title="Jatin Papers Matrix")
ws1.views.sheetView[0].showGridLines = True

headers1 = [
    "Paper ID", "Paper Title", "Authors", "Year", "Venue / Publication", 
    "DOI / Permanent URL", "Publication Type", "Time Window (2021-2026)", "Category / Approach", 
    "Problem Addressed", "Method / Model Architecture", "Dataset / Testbed Used", 
    "Evaluation Measures / Metrics", "Reported Findings / Performance", 
    "Limitations / Critical Notes", "Adapts to Change / New Attacks?", 
    "Honest Reading Status", "Verification Status (Claim Audit)", "Source Cross-Reference"
]
ws1.append(headers1)

jatin_matrix_rows = [
    (
        "JTN01",
        "Kitsune: An Ensemble of Autoencoders for Online Network Intrusion Detection",
        "Y. Mirsky, T. Doitshman, Y. Elovici, A. Shabtai",
        2018,
        "Proc. 25th Annual Network and Distributed System Security Symposium (NDSS 2018)",
        "https://doi.org/10.14722/ndss.2018.23204",
        "Conference Proceeding",
        "No (Pre-2021 Foundational)",
        "Online Unsupervised Anomaly Detection",
        "Supervised neural-network NIDS require heavy manual labelling, frequent retraining, and exceed the memory/CPU budgets of resource-constrained routers and IoT gateways.",
        "KitNET: an ensemble of small autoencoders trained incrementally in an online, unsupervised fashion, combined with damped incremental statistics for continuous packet feature extraction.",
        "Mirai botnet, IP camera video, and synthetic attack traffic (TO VERIFY full evaluation section details in paper).",
        "F1-score, execution time, CPU/memory consumption (TO VERIFY complete metric set).",
        "Abstract reports detection performance comparable to offline anomaly detectors while operating at line-speed even on a Raspberry Pi.",
        "Relies heavily on the assumption that initial training traffic is entirely benign; vulnerable if training stream contains stealthy background attacks; does not explicitly track long-term concept drift.",
        "Yes (learns incrementally online from packet streams)",
        "NOT READ IN FULL by Jatin (abstract and secondary summaries only)",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Section Pack (J1), Literature Matrix (J1), Consolidated Pack (JTN01), Existing Draft ([2])"
    ),
    (
        "JTN02",
        "HELAD: A Novel Network Anomaly Detection Model Based on Heterogeneous Ensemble Learning",
        "Ying Zhong, Wenqi Chen, Zhiliang Wang, Yifan Chen, Kai Wang, Yahui Li, Xia Yin, Xingang Shi, Jiahai Yang, Keqin Li",
        2020,
        "Computer Networks, vol. 169, Art. no. 107049",
        "https://doi.org/10.1016/j.comnet.2019.107049",
        "Journal Article",
        "No (Pre-2021 Foundational)",
        "Hybrid Deep-Learning Ensemble",
        "Individual anomaly detection models struggle with practical deployment due to the scarcity of labelled data and inability to adapt to continuous variations in network traffic.",
        "Heterogeneous ensemble pairing an Autoencoder (capturing structural reconstruction error) and an LSTM (capturing temporal sequence transitions), using damped incremental statistics and time-sliced retraining.",
        "Enterprise network traffic flows (TO VERIFY exact dataset names and splits in full paper).",
        "Accuracy, Detection Rate, False Alarm Rate, F1-score (TO VERIFY).",
        "Publisher abstract describes superior adaptability and detection performance over baseline models under changing traffic distributions; specific numerical outcomes require full-text check.",
        "Retraining by fixed time slices introduces latency and computational overhead; may incorporate poisoned samples during unsupervised retraining window.",
        "Partially (adapts via periodic time-slice retraining)",
        "NOT READ IN FULL by Jatin (abstract-level details only)",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Section Pack (J2), Literature Matrix (J2), Consolidated Pack (JTN02)"
    ),
    (
        "JTN03",
        "Advanced Intrusion Detection Combining Signature-Based and Behavior-Based Detection Methods",
        "Hee-Yong Kwon, Taesic Kim, Mun-Kyu Lee",
        2022,
        "Electronics (MDPI), vol. 11, no. 6, Art. no. 867",
        "https://doi.org/10.3390/electronics11060867",
        "Journal Article (Open Access)",
        "Yes (2021-2026 Window)",
        "Hybrid Signature + Behaviour / Autoencoder",
        "Detect anomalous network behaviours that bypass traditional signature matching while maintaining the high explainability and low false alarm rate of signature rules.",
        "Two-stage hybrid: statistical packet filtering to eliminate known malicious and benign traffic patterns, followed by a composite autoencoder evaluated across two distinct time-window settings.",
        "Not confirmed in Jatin's matrix (TO VERIFY from open-access article).",
        "Not recorded in Jatin's matrix (TO VERIFY).",
        "No quantitative performance numbers extracted in Jatin's initial review records.",
        "Composite autoencoder adds pipeline complexity; threshold selection across dual time windows requires manual calibration.",
        "TO VERIFY in full text",
        "NOT READ IN FULL by Jatin (abstract-level details only; least confirmed entry)",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Section Pack (J3), Literature Matrix (J3), Consolidated Pack (JTN03), Existing Draft ([17])"
    ),
    (
        "JTN04",
        "Learn to Adapt: Robust Drift Detection in Security Domain",
        "Aditya Kuppa, Nhien-An Le-Khac",
        2022,
        "Computers & Electrical Engineering, vol. 102, Art. no. 108239",
        "https://doi.org/10.1016/j.compeleceng.2022.108239",
        "Journal Article (Open Access)",
        "Yes (2021-2026 Window)",
        "Adaptive / Drift Detection & New-Class Discovery",
        "Security ML models degrade rapidly under concept drift; traditional drift detectors watch feature distribution shifts and retrain periodically, making them slow to notice attacks and vulnerable to adversary manipulation.",
        "Robust online drift detector leveraging contrastive deep representations that flags drifted sample streams and dynamically discovers novel attack classes online.",
        "Two security datasets: a 2018 network intrusion dataset and an APT Command-and-Control (C&C) dataset merged with web-categorisation data.",
        "Accuracy, Robustness under adversarial perturbation, New-class clustering purity (TO VERIFY).",
        "Authors report high detection accuracy, resilience against adversarial manipulation, and effective real-time discovery of novel attack classes from drifted streams.",
        "Requires deep contrastive feature extraction; labelling budget and ground-truth verification costs in deployment remain open.",
        "Yes (detects online drift and discovers novel attack classes)",
        "Abstract read; method, results and conclusion remained pending",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Day 1 Ref [2], Team Rows (2), Day 2/3 ([2]), Section Pack (J4), Lit Matrix (J4), Consolidated (JTN04), Existing Draft ([21])"
    ),
    (
        "JTN05",
        "ENIDrift: A Fast and Adaptive Ensemble System for Network Intrusion Detection under Real-world Drift",
        "Xian Wang and others",
        2022,
        "Proc. 38th Annual Computer Security Applications Conference (ACSAC 2022), pp. 785–789",
        "https://doi.org/10.1145/3564625.3567992",
        "Conference Proceeding",
        "Yes (2021-2026 Window)",
        "Adaptive Online Ensemble / Concept Drift",
        "Existing ML NIDS consider only narrow artificial drift, exhibit excessive runtime latency, and ignore adversarial ML evasion attacks during adaptation.",
        "ENIDrift: tri-component adaptive ensemble featuring iP2V (incremental feature extraction via a 3-layer neural network), dynamic sub-classifier generation, and an online model-update module.",
        "CICIDS2017, MAWILab, and author-developed Real-World Drift Intrusion Detection Dataset (RWDIDS) with 4 drift severity tiers.",
        "F1-score, inference latency / running time, robustness against adversarial perturbation.",
        "Authors report up to 69.78% higher F1 than state-of-the-art baselines, 87.6% lower running time, and 100% F1 against an adversarial evasion attack designed by the authors.",
        "The 100% adversarial F1 was achieved against an attack formulated by the authors themselves; evaluation heavily relies on their proprietary RWDIDS dataset; independent validation needed.",
        "Yes (incremental updates under real-world drift)",
        "Abstract and conference presentation slides read; full paper pending",
        "Partially Verified from slides/abstract; full text pending ([VERIFY])",
        "Day 1 Ref [3], Team Rows (3), Day 2/3 ([3]), Section Pack (J5), Lit Matrix (J5), Consolidated (JTN05), Existing Draft ([22])"
    ),
    (
        "JTN06",
        "Assessing the Impact of a Supervised Classification Filter on Flow-based Hybrid Network Anomaly Detection",
        "Dominik Macko, Patrik Goldschmidt, Peter Pištek, Daniela Chudá",
        2023,
        "arXiv preprint arXiv:2310.06656",
        "https://arxiv.org/abs/2310.06656",
        "Preprint (arXiv)",
        "Yes (2021-2026 Window)",
        "Hybrid Supervised Filter + Autoencoder",
        "Standalone anomaly detectors flag novel attacks but suffer from excessive false-positive rates; purely supervised models achieve high accuracy on known attacks but are blind to unknown zero-days.",
        "Two-tier hybrid pipeline: prepends a lightweight supervised binary classifier as a front-end filter to intercept known attack signatures, routing assumed-benign flows to a deep autoencoder for anomaly scoring.",
        "UGR'16 flow-based network traffic dataset (confirmed in consolidated pack).",
        "Detection rate of known attacks, false-positive rate, ROC-AUC (TO VERIFY).",
        "Prepending the filter increases detection rate for known threats without increasing false alarms; novel attack detection maintained on remaining flows.",
        "Static architecture; does not address concept drift or model aging; relies on quality of supervised filter to avoid passing known attacks to the anomaly stage.",
        "No (static pipeline; does not adapt to evolving distributions)",
        "Abstract and introduction read; method and results pending",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Day 1 Ref [9], Team Rows (9), Day 2/3 ([9]), Section Pack (J6), Lit Matrix (J6), Consolidated (JTN06), Existing Draft ([19])"
    ),
    (
        "JTN07",
        "RFG-HELAD: A Robust Fine-Grained Network Traffic Anomaly Detection Model Based on Heterogeneous Ensemble Learning",
        "Ying Zhong, Zhiliang Wang, Xingang Shi, Jiahai Yang, Keqin Li",
        2024,
        "IEEE Transactions on Information Forensics and Security, vol. 19, pp. 5895–5910",
        "https://doi.org/10.1109/TIFS.2024.3402439",
        "Journal Article",
        "Yes (2021-2026 Window)",
        "Hybrid DL Ensemble / Fine-Grained OOD",
        "Achieving fine-grained classification of multi-class network traffic while reliably detecting novel/unknown attacks and maintaining robustness against adversarial perturbations.",
        "Heterogeneous ensemble integrating a Deep Neural Network trained with supervised contrastive learning, a GAN-based classification module, and Deep k-Nearest Neighbour (DkNN) for out-of-distribution detection.",
        "Benchmark network intrusion datasets (TO VERIFY specific datasets and splits).",
        "Multi-class accuracy, precision, recall, F1, adversarial robustness metrics (TO VERIFY).",
        "Publisher abstract claims state-of-the-art fine-grained accuracy and superior detection of unseen anomaly types alongside high adversarial resistance.",
        "High pipeline complexity; training multi-branch neural architectures with contrastive and GAN losses incurs heavy compute overhead; full evaluation details remain to be read.",
        "Partially (targets fine-grained unknown attacks and adversarial shifts)",
        "NOT READ IN FULL by Jatin (abstract-level details only; least confirmed entry)",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Section Pack (J7), Literature Matrix (J7), Consolidated Pack (JTN07), Existing Draft ([11])"
    ),
    (
        "JTN08",
        "Continual Learning with Strategic Selection and Forgetting for Network Intrusion Detection",
        "Xinchen Zhang, Running Zhao, Zhihan Jiang, Handi Chen, Yulong Ding, Edith C. H. Ngai, Shuang-Hua Yang",
        2024,
        "arXiv preprint arXiv:2412.16264 (presented IEEE INFOCOM 2025)",
        "https://arxiv.org/abs/2412.16264",
        "Preprint / Conference",
        "Yes (2021-2026 Window)",
        "Adaptive / Continual Learning & Concept Drift",
        "Continual learning IDSs often retain outdated historical knowledge (causing negative backward transfer) and allocate insufficient model capacity to newly drifted attack patterns.",
        "Strategic Selection and Forgetting (SSF): Kolmogorov-Smirnov statistical test for drift detection; KL-divergence mask to select informative new samples; strategic forgetting mechanism to purge obsolete weights; fine-tuning with pseudo-labelling.",
        "NSL-KDD and UNSW-NB15 benchmark datasets.",
        "Accuracy, F1-score, catastrophic forgetting rate, adaptation latency under varying labelling budgets.",
        "Authors report state-of-the-art adaptation across both benchmarks, outperforming conventional continual learning baselines under restricted labelling budgets.",
        "Requires an ongoing manual labelling budget (k human-labelled samples per update round); frames traffic classification primarily as a binary problem; evaluated on older benchmark datasets.",
        "Yes (continual learning with active forgetting and adaptation)",
        "Abstract, introduction and methodology read; experiments/conclusion pending",
        "Partially Verified (Method verified; experimental tables pending full audit)",
        "Day 1 Ref [5], Team Rows (5), Day 2/3 ([5]), Section Pack (J8), Lit Matrix (J8), Consolidated (JTN08), Existing Draft ([23])"
    ),
    (
        "JTN09",
        "Hybrid Intrusion Detection System Based on Combination of Random Forest and Autoencoder",
        "Chao Wang, Yunxiao Sun, Wenting Wang, Hongri Liu, Bailing Wang",
        2023,
        "Symmetry (MDPI), vol. 15, no. 3, Art. no. 568",
        "https://doi.org/10.3390/sym15030568",
        "Journal Article (Open Access)",
        "Yes (2021-2026 Window)",
        "Hybrid ML + DL / Unseen Attack Holdout",
        "Supervised IDS models classify unknown attack types as benign because they lack representation in training; unsupervised models suffer from excessive false-positive rates.",
        "Two-stage pipeline: Random Forest evaluated via output attack probability against threshold T1 (90th percentile of normal validation scores); flagged anomalous traffic re-checked by an Autoencoder trained solely on benign flows (threshold T2 = 75th percentile).",
        "NF-CSE-CIC-IDS2018-v2 and NF-BoT-IoT-v2 (NetFlow v2 formats). Simulated unseen attacks by systematically withholding one attack class from training, repeating 5 times per class.",
        "Accuracy, precision, recall, F1-score, False Positive Rate (FPR) (mean ± std dev).",
        "Achieved highest F1 against 8 baselines: 99.72% on BoT-IoT and 95.90% on IDS2018; lowest FPR on IDS2018 (1.81%). Under DoS holdout, plain RF flagged only 1.8% of attacks whereas probability-RF flagged 64.8%.",
        "Only one attack category was withheld at a time; binary classification only; decision thresholds T1 and T2 must be set manually because validation sets lack unknown attack instances; static model (no concept drift adaptation).",
        "No (static hybrid model; does not adapt online to concept drift)",
        "FULL TEXT READ by Jatin (abstract, methodology, experiments, conclusion)",
        "FULLY VERIFIED from full text (Only paper in Jatin's pack read in full)",
        "Day 1 Ref [1], Team Rows (1), Day 2/3 ([1]), Consolidated Pack (JTN09), Existing Draft ([18])"
    ),
    (
        "JTN10",
        "Concept Drift-Based Intrusion Detection for Evolving Data Stream Classification in IDS: Approaches and Comparative Study",
        "Sugandh Seth, Kuljit Kaur Chahal, Gurvinder Singh",
        2024,
        "The Computer Journal, vol. 67, no. 7, pp. 2529–2547",
        "https://doi.org/10.1093/comjnl/bxae023",
        "Journal Article",
        "Yes (2021-2026 Window)",
        "Adaptive / Drift-Aware Stream Classification",
        "Static ML/DL IDS models experience severe performance degradation as network traffic distributions evolve; periodic batch retraining is computationally prohibitive.",
        "Adaptive Random Forest (ARF) integrated with Hoeffding bounds and a moving-average statistical test to detect drift early and differentiate benign shifts from true cyber intrusions.",
        "CIC-IDS 2018 benchmark stream.",
        "Accuracy, recall, false-positive rate, drift detection latency.",
        "Authors report 99.95% accuracy and 99.96% recall on CIC-IDS 2018, claiming superior performance over existing stream classification techniques.",
        "Evaluated on a single benchmark dataset; near-perfect scores raise questions regarding whether the test stream contained genuine distribution shifts or held-out unseen attack types; full text unread.",
        "Yes (online adaptive learning on streaming data)",
        "Abstract read; method, results and conclusion remained pending",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Day 1 Ref [4], Team Rows (4), Day 2/3 ([4]), Lit Matrix (Reserve), Consolidated (JTN10), Existing Draft ([24])"
    ),
    (
        "JTN11",
        "Entropy-based Network Traffic Anomaly Classification Method Resilient to Deception",
        "Juma Ibrahim, Slavko Gajin",
        2022,
        "Computer Science and Information Systems, vol. 19, no. 1, pp. 87–116",
        "https://doi.org/10.2298/CSIS201229045I",
        "Journal Article",
        "Yes (2021-2026 Window)",
        "Statistical / Behaviour-Based Entropy",
        "Entropy-based anomaly detection can be intentionally deceived by spoofed background traffic designed to camouflage volumetric and structural anomalies.",
        "Multi-entropy monitoring tracking Shannon, Rényi, and Tsallis entropies alongside distinct-element cardinalities; multivariate statistical analysis feeds rule-based anomaly classification.",
        "Experimental NetFlow-derived network traffic datasets (specific dataset names TO VERIFY).",
        "Classification accuracy, detection latency, resilience against spoofed background traffic.",
        "Authors demonstrate that combining three entropy formulations successfully unmasks spoofed anomalies and classifies attack categories without complex ML inference.",
        "Rule-based classification may not generalize to unfamiliar benign protocols; static thresholds cannot track long-term evolution in benign network baselines; full text unread.",
        "No (rule-based statistical framework; does not continuously adapt)",
        "Abstract read; method, results and conclusion remained pending",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Day 1 Ref [6], Team Rows (6), Day 2/3 ([6]), Consolidated Pack (JTN11), Existing Draft ([16])"
    ),
    (
        "JTN12",
        "Machine Learning Enhanced Entropy-Based Network Anomaly Detection",
        "Valentina Timcenko, Slavko Gajin",
        2021,
        "Advances in Electrical and Computer Engineering, vol. 21, no. 4, pp. 51–60",
        "https://doi.org/10.4316/aece.2021.04006",
        "Journal Article",
        "Yes (2021-2026 Window)",
        "Statistical + Unsupervised ML Hybrid",
        "High traffic volumes and strict line-rate operational constraints demand computationally efficient, highly scalable network anomaly detection.",
        "Two-tier flow architecture: entropy processing across traffic feature distributions exposes hidden non-linear patterns; flagged outlier traffic is routed to unsupervised machine learning (clustering).",
        "Modelled/synthetic attack traffic (port scan, network scan, DDoS amplification, flood, dictionary attacks), real network captures, and botnet traces.",
        "Detection rate, false alarm rate, processing speed / throughput (TO VERIFY).",
        "Authors state the combined entropy-clustering pipeline achieves high throughput and effectively isolates anomalous flows on tested network captures.",
        "Evaluated predominantly on synthetic or modelled attack injections; lacks formal evaluation against zero-day or held-out novel attack families; full text unread.",
        "No (static flow-level pipeline; no online adaptation)",
        "Abstract read; method, results and conclusion remained pending",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Day 1 Ref [7], Team Rows (7), Day 2/3 ([7]), Consolidated Pack (JTN12), Existing Draft ([15])"
    ),
    (
        "JTN13",
        "A Deep Learning/Machine Learning Approach for Anomaly Based Network Intrusion Detection",
        "Reem Almuhanna, Samia Dardouri",
        2025,
        "Frontiers in Artificial Intelligence, vol. 8, Art. no. 1625891",
        "https://doi.org/10.3389/frai.2025.1625891",
        "Journal Article (Open Access)",
        "Yes (2021-2026 Window)",
        "Hybrid ML/DL Ensemble (Contextual Baseline)",
        "Single ML/DL classifiers fail to capture the multi-faceted characteristics of diverse network intrusions.",
        "Weighted soft-voting ensemble combining XGBoost, Random Forest, Graph Neural Network (GNN), LSTM, and Autoencoder, with extensive feature preprocessing and SMOTE balancing.",
        "CICIDS2017 with 5,661,486 records and 80 raw features, plus an independent secondary benchmark dataset.",
        "Accuracy, precision, recall, F1-score; evaluated via 5-fold cross-validation.",
        "Authors report performance metrics approaching 100% across multiple traffic classes on the primary 5.6M-record dataset and strong generalization on the secondary benchmark.",
        "Evaluated via conventional random k-fold cross-validation without an explicit held-out unknown attack class protocol; represents closed-set multi-class detection rather than direct zero-day proof.",
        "No (static multi-classifier ensemble; no online drift adaptation)",
        "Abstract and introduction read; full methodology/results pending",
        "Unverified / Pending full-text verification ([VERIFY])",
        "Day 1 Ref [8], Team Rows (8), Day 2/3 ([8]), Consolidated Pack (JTN13), Existing Draft ([20])"
    )
]

for row in jatin_matrix_rows:
    ws1.append(row)

# -------------------------------------------------------------------------
# Sheet 2: Reserve Candidates (Tracked Separately)
# -------------------------------------------------------------------------
ws2 = wb.create_sheet(title="Reserve Candidates")
ws2.views.sheetView[0].showGridLines = True

headers2 = [
    "Reserve ID", "Paper Title", "Authors", "Year", "Venue / Publication", 
    "DOI / Permanent URL", "Scope / Technique", "Status / Role in Project"
]
ws2.append(headers2)

reserve_rows = [
    (
        "RES01",
        "Network anomaly detection via similarity-aware ensemble learning with ADSim",
        "Wenqi Chen, Zhiliang Wang, Lingyun Chang, Kai Wang, Ying Zhong, Dongqi Han, Chenglong Duan, Xia Yin, Jiahai Yang, Xingang Shi",
        2024,
        "Computer Networks, vol. 247, Art. no. 110423",
        "https://doi.org/10.1016/j.comnet.2024.110423",
        "Online, unsupervised, similarity-aware ensemble framework (ADSim)",
        "Reserve candidate in Jatin workbook; cited as [26] in existing non-authoritative draft; available for master synthesis if needed."
    ),
    (
        "RES02",
        "Generative Active Adaptation for Drifting and Imbalanced Network Intrusion Detection (NetGuard)",
        "Raghav Gupta, Sirui Liu, Ruizhi Zhang, Xiaohui Hu, Xiao Wang, Hichem Benkraouda, Pradeep Kommaraju, Nick Feamster, Klara Nahrstedt",
        2025,
        "arXiv preprint arXiv:2503.03022",
        "https://arxiv.org/abs/2503.03022",
        "Active learning + generative data augmentation to address drifting and imbalanced traffic streams",
        "Reserve candidate in Jatin workbook; cited as [25] in existing non-authoritative draft; available for master synthesis if needed."
    ),
    (
        "RES03",
        "Concept Drift-Based Intrusion Detection for Evolving Data Stream Classification in IDS: Approaches and Comparative Study",
        "Sugandh Seth, Kuljit Kaur Chahal, Gurvinder Singh",
        2024,
        "The Computer Journal, vol. 67, no. 7, pp. 2529–2547",
        "https://doi.org/10.1093/comjnl/bxae023",
        "Adaptive Random Forest + Hoeffding bound + moving average test on CIC-IDS 2018",
        "RECONCILED: Initially placed in reserve sheet on Day 2; restored to core 13 candidate papers as JTN10."
    )
]

for row in reserve_rows:
    ws2.append(row)

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
    ("LOG01", "17 Nov 2026", "General web search", "Kitsune online ensemble of autoencoders network intrusion detection NDSS 2018", "not recorded", "Historical search query without result counts", "Execute repeat search in IEEE Xplore / ACM DL / Google Scholar and record real hit counts."),
    ("LOG02", "17 Nov 2026", "General web search", "concept drift network intrusion detection adaptive learning 2022 arXiv", "not recorded", "Historical search query without result counts", "Execute repeat search in IEEE Xplore / ACM DL / Google Scholar and record real hit counts."),
    ("LOG03", "17 Nov 2026", "General web search", "ENIDrift ACSAC 2022 authors Fast and Adaptive Ensemble System ...", "not recorded", "Historical search query without result counts", "Execute repeat search in ACM Digital Library and record real hit counts."),
    ("LOG04", "17 Nov 2026", "General web search", "HELAD heterogeneous ensemble learning network anomaly detection Computer Networks 2020", "not recorded", "Historical search query without result counts", "Execute repeat search in ScienceDirect / Scopus and record real hit counts."),
    ("LOG05", "17 Nov 2026", "General web search", "statistical behaviour-based network anomaly detection unknown attacks hybrid signature anomaly 2023 journal", "not recorded", "Historical search query without result counts", "Execute repeat search in IEEE Xplore / SpringerLink and record real hit counts.")
]

for row in search_log_rows:
    ws3.append(row)

# -------------------------------------------------------------------------
# Sheet 4: Gaps & Future Directions
# -------------------------------------------------------------------------
ws4 = wb.create_sheet(title="Gaps & Future Directions")
ws4.views.sheetView[0].showGridLines = True

headers4 = [
    "Gap ID", "Research Gap Title", "Detailed Gap Description", 
    "Supporting Evidence in Jatin Pack", "Linked Future Direction ID", "Future Direction Proposal"
]
ws4.append(headers4)

gaps_directions_rows = [
    (
        "JG1",
        "Unseen-attack detection and drift adaptation are rarely evaluated jointly",
        "Hybrid detectors aimed at unseen attacks (JTN09, JTN06, JTN13) are evaluated as static models without temporal drift. Conversely, drift-adaptive models (JTN04, JTN05, JTN08, JTN10) evaluate tracking of evolving known distributions rather than the emergence of entirely new attack families. Where unseen attacks are tested, they are artificially simulated via single-class holdout.",
        "Wang et al. [JTN09] (read in full) withhold only one attack class at a time and employ a static model; ENIDrift [JTN05], Seth [JTN10], and SSF [JTN08] evaluate drift adaptation on streaming data without isolating zero-day attack families. Only Kuppa & Le-Khac [JTN04] explicitly claim both drift detection and new-class discovery.",
        "JD1",
        "Design unified evaluation benchmarks with time-ordered network streams featuring both continuous covariate drift and genuinely novel attack families, reporting drift tracking and unknown-class detection independently."
    ),
    (
        "JG2",
        "Adaptive stream detectors depend heavily on ground-truth labels or hand-tuned thresholds",
        "Online adaptation models require continuous or periodic supervision to update model weights without catastrophic forgetting or error propagation. In practice, high-quality labels are scarce or severely delayed during live network deployment.",
        "Zhang et al. (SSF) [JTN08] requires an explicit labelling budget of manual labels per update cycle; Wang et al. [JTN09] require manual threshold calibration (T1, T2) because validation data contains no unknown attacks; Kuppa [JTN04] notes label scarcity as the core deployment obstacle.",
        "JD2",
        "Develop self-calibrating thresholding mechanisms and label-efficient online updating frameworks (active learning, contrastive self-supervision, safe pseudo-labelling) with explicit reporting of label acquisition costs."
    ),
    (
        "JG3",
        "Vulnerability of adaptive and statistical detectors to deliberate adversarial manipulation",
        "Continuous online updating introduces severe vulnerability to poisoning and evasion: an adversary can slowly manipulate traffic distributions so that malicious activity is incrementally learned as normal baselines. Statistical detectors are similarly susceptible to spoofed background traffic.",
        "Ibrahim & Gajin [JTN11] demonstrate that multi-entropy detection is required because plain entropy is easily deceived by spoofed packets; ENIDrift [JTN05] tests only an adversarial attack designed by its own authors; Kuppa [JTN04] highlights that periodic retraining fails under attacker-induced drift.",
        "JD3",
        "Establish standardized poisoning-resilient update rules (e.g. gated or delayed commitment updates) evaluated against independent, adaptive adversarial benchmarks."
    ),
    (
        "JG4",
        "Disparate evaluation benchmarks and non-comparable metric reporting",
        "Reviewed studies evaluate across widely disparate datasets, varying from outdated benchmarks (NSL-KDD in JTN08) to synthetic injections (JTN12) and proprietary private datasets (RWDIDS in JTN05). Reported metrics (accuracy vs F1 vs AUROC vs FPR) cannot be compared directly.",
        "The 13 papers utilize at least 8 distinct datasets; near-perfect scores (99.95% in JTN10, 100% in JTN13) cannot be compared directly with open-set holdout results (JTN09) due to mismatched splits and objectives.",
        "JD4",
        "Adopt standardized open-access evaluation testbeds with time-ordered NetFlow/packet data, and mandate uniform multi-dimensional reporting (macro F1, FPR, latency, memory, line-speed throughput)."
    ),
    (
        "JG5",
        "Rigorous holdout of novel attack families is inconsistently enforced",
        "Many studies claiming anomaly or unknown attack detection perform standard random train/test splits where instances of all attack classes are present during training, testing closed-set classification rather than true zero-day detection.",
        "Almuhanna & Dardouri [JTN13] and Seth et al. [JTN10] evaluate on standard random splits; only Wang et al. [JTN09] explicitly isolates attack classes (leave-one-class-out protocol). Note: Overlaps JG1 and is integrated as a methodological sub-gap.",
        "JD5",
        "Enforce strict leave-attack-family-out (LAFO) experimental protocols, clearly separating closed-set multi-class accuracy from open-set novel-class detection."
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

wb.save("literature-matrix/jatin-papers.xlsx")
print("literature-matrix/jatin-papers.xlsx generated successfully!")
