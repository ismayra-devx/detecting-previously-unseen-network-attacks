import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_document():
    doc = docx.Document()
    
    # Page setup: A4, 2 cm margins
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(0.79)
        section.bottom_margin = Inches(0.79)
        section.left_margin = Inches(0.79)
        section.right_margin = Inches(0.79)

    # Styles setup
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Times New Roman'
    font_normal.size = Pt(10.5)
    font_normal.color.rgb = RGBColor(0x33, 0x33, 0x33)

    # Header block
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(2)
    run_inst = title_p.add_run("IILM UNIVERSITY, GURUGRAM\n")
    run_inst.font.name = 'Times New Roman'
    run_inst.font.size = Pt(14)
    run_inst.font.bold = True
    run_inst.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    run_sub = title_p.add_run("School of Computer Science and Engineering\nMember Research Record — Jatin (258100003)")
    run_sub.font.name = 'Times New Roman'
    run_sub.font.size = Pt(12)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    # Meta table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Member Name & Enrolment", "Jatin (Enrolment No. 258100003)"),
        ("Assigned Category", "Anomaly-Based, Hybrid and Adaptive Detection"),
        ("Project Title", "Detecting Previously Unseen Network Attacks: A Survey"),
        ("Document Status & Date", "Authoritative Consolidated Member Record | 17 November 2026")
    ]
    for idx, (k, v) in enumerate(meta_data):
        row = meta_table.rows[idx]
        row.cells[0].text = k
        row.cells[1].text = v
        set_cell_background(row.cells[0], "F2F2F2")
        set_cell_background(row.cells[1], "FFFFFF")
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        set_cell_margins(row.cells[0])
        set_cell_margins(row.cells[1])

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Heading 1 helper
    def add_h1(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
        return h

    def add_h2(text):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(8)
        h.paragraph_format.space_after = Pt(2)
        h.paragraph_format.keep_with_next = True
        r = h.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
        return h

    # Section 1
    add_h1("1. Purpose and Source Hierarchy")
    p1 = doc.add_paragraph(
        "This document establishes the clean, authoritative member record for Jatin's review component on "
        "'Anomaly-Based, Hybrid and Adaptive Detection' in the survey paper 'Detecting Previously Unseen Network Attacks'. "
        "It consolidates Jatin's submitted files, reconciles divergent paper lists, enforces verified bibliographic corrections, "
        "presents the complete synthesis text for Section IV-C, details the research gap and future direction framework, "
        "and sets forth an honest account of student reading versus AI assistance in full compliance with the official IILM Survey Paper Template."
    )
    p1.paragraph_format.space_after = Pt(4)

    p_hier = doc.add_paragraph(
        "Source Hierarchy Enforced:\n"
        "1. Confirmed Publisher / DOI / arXiv Metadata: Highest authority for bibliographic fields, page numbers, and volume records.\n"
        "2. Jatin Consolidated Research Pack (Jatin_Consolidated_Research_Pack.docx): Primary authoritative compilation for member synthesis.\n"
        "3. Jatin Section Pack & Literature Matrix (Jatin_Section_IVC_Gaps_Directions.docx & Jatin_Literature_Matrix.xlsx): Secondary source for 8-paper draft and reserve pool.\n"
        "4. Jatin Day 1 Submission (Jatin_Day1_Literature_Review(1).docx & Jatin_Matrix_Rows_for_Team.xlsx): Historical baseline for Day 1 9-paper matrix and initial reading declarations.\n"
        "Rule on Ambiguity: Where source files conflict or original papers were not fully examined end-to-end, this record preserves [VERIFY] / pending status rather than guessing unsupported facts."
    )
    p_hier.paragraph_format.space_after = Pt(6)

    # Section 2
    add_h1("2. Paper-Count Reconciliation & De-Duplication")
    doc.add_paragraph(
        "Jatin's submissions originally presented two differing lists: Day 1 listed nine candidate studies [1]–[9], "
        "while the later Section Pack / workbook listed eight candidate studies [J1]–[J8]. "
        "A rigorous title, author, and DOI matching audit demonstrates that four works are duplicates appearing across both lists:\n"
        "• Kuppa & Le-Khac (2022): Day 1 Ref [2] <==> Section Pack Ref [J4] (DOI: 10.1016/j.compeleceng.2022.108239)\n"
        "• Wang et al. / ENIDrift (2022): Day 1 Ref [3] <==> Section Pack Ref [J5] (DOI: 10.1145/3564625.3567992)\n"
        "• Macko et al. (2023): Day 1 Ref [9] <==> Section Pack Ref [J6] (arXiv: 2310.06656)\n"
        "• Zhang et al. / SSF (2024): Day 1 Ref [5] <==> Section Pack Ref [J8] (arXiv: 2412.16264 / INFOCOM 2025)\n"
        "• Seth et al. (2024): Day 1 Ref [4] was temporarily placed in the workbook 'Reserve_papers' sheet on Day 2; it is reconciled and restored as a core entry (JTN10).\n\n"
        "Reconciliation Outcome: Combining 9 Day 1 papers and 8 Section Pack papers minus the 4 overlapping duplicates yields exactly 13 unique candidate works (JTN01–JTN13), not 17. "
        "Furthermore, two works are pre-2021 foundational papers:\n"
        "• Kitsune (Mirsky et al., NDSS 2018) [JTN01] and HELAD (Zhong et al., Comput. Netw. 2020) [JTN02]. "
        "These are explicitly retained as seminal foundational references for online autoencoder ensembles but are NOT counted towards the 15-paper recent (2021–2026) requirement."
    )

    # Section 3
    add_h1("3. Consolidated Technique Summary")
    doc.add_paragraph(
        "The 13 candidate studies explore three distinct technical philosophies to address unknown network attacks:\n\n"
        "A. Statistical and Behaviour-Based Detection: Ibrahim and Gajin (2022) [JTN11] employ multi-entropy monitoring (Shannon, Rényi, Tsallis) "
        "and distinct element counts paired with rule-based anomaly classification to resist spoofing deception. Timcenko and Gajin (2021) [JTN12] "
        "combine flow-based entropy processing with unsupervised clustering on unusual traffic flows. Both profile behavioral deviations rather than "
        "relying on fixed signatures, though neither incorporates continuous online model adaptation.\n\n"
        "B. Hybrid Machine Learning and Deep Learning Detection: Wang et al. (2023) [JTN09] combine a probability-thresholded Random Forest "
        "with an Autoencoder re-check stage, demonstrating strong held-out attack detection on NetFlow benchmarks. Kwon et al. (2022) [JTN03] pair "
        "signature filtering with a composite autoencoder across dual time windows. Macko et al. (2023) [JTN06] prepend a supervised binary filter "
        "in front of an autoencoder on UGR'16 flow traffic to intercept known threats. HELAD (2020) [JTN02] and RFG-HELAD (2024) [JTN07] deploy "
        "heterogeneous ensembles (Autoencoder, LSTM, contrastive DNN, and GAN modules with Deep k-NN out-of-distribution scoring). Almuhanna and Dardouri "
        "(2025) [JTN13] use weighted soft voting across XGBoost, RF, GNN, LSTM, and Autoencoder, serving as a contextual multiclass baseline.\n\n"
        "C. Adaptive and Concept Drift-Aware Detection: Kuppa and Le-Khac (2022) [JTN04] address adversarial drift and online discovery of novel classes "
        "using contrastive representations. ENIDrift (2022) [JTN05] integrates incremental packet-to-vector (iP2V) feature extraction, sub-classifier generation, "
        "and model updating. Seth et al. (2024) [JTN10] utilize an Adaptive Random Forest with Hoeffding bounds and moving-average testing on CIC-IDS 2018 streams. "
        "Zhang et al. (2024) [JTN08] implement Strategic Selection and Forgetting (SSF) via Kolmogorov-Smirnov drift tests and KL divergence masking. "
        "Kitsune (2018) [JTN01] provides the underlying lightweight online autoencoder baseline."
    )

    # Section 4: 13 Tables
    add_h1("4. Unique Paper Register & Evidence Records (13 Studies)")
    doc.add_paragraph(
        "Below are the verified source records for all 13 unique candidate papers. All fields marked [VERIFY] reflect items where Jatin's "
        "submissions noted abstract-level verification and where full-text student audit remains pending."
    )

    # Load Jatin parsed rows from generated matrix
    import generate_jatin_matrix
    j_rows = generate_jatin_matrix.jatin_matrix_rows

    for r in j_rows:
        pid, title, authors, year, venue, link, ptype, win, cat, prob, meth, data, meas, find, lim, adapt, read_st, ver_st, src = r
        add_h2(f"{pid}: {title}")
        t = doc.add_table(rows=11, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        fields = [
            ("Authors", authors),
            ("DOI / Permanent Link", link),
            ("Year / Venue / Type", f"{year}; {venue} ({ptype})"),
            ("Time Window Compliance", win),
            ("Category / Approach", cat),
            ("Problem Addressed", prob),
            ("Method / Model Architecture", meth),
            ("Dataset / Testbed Used", data),
            ("Evaluation Measures", meas),
            ("Reported Findings / Performance", find),
            ("Limitations & Reading Status", f"Limitations: {lim}\nReading: {read_st}\nAudit Status: {ver_st}")
        ]
        for f_idx, (k, v) in enumerate(fields):
            row = t.rows[f_idx]
            row.cells[0].text = k
            row.cells[1].text = str(v)
            set_cell_background(row.cells[0], "F2F2F2")
            row.cells[0].paragraphs[0].runs[0].font.bold = True
            set_cell_margins(row.cells[0], top=60, bottom=60, left=100, right=100)
            set_cell_margins(row.cells[1], top=60, bottom=60, left=100, right=100)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Section 5: Consolidated Section IV-C
    add_h1("5. Section IV-C Synthesis Draft")
    doc.add_paragraph(
        "The following draft text provides the complete synthesis for Section IV-C of the survey paper, "
        "integrating all 13 studies into an academic narrative:"
    )

    ivc_text = [
        "Detecting attacks that were absent from training data is the central difficulty for learning-based intrusion detection. "
        "The thirteen studies reviewed in this category [JTN01]–[JTN13] approach this challenge along three primary paths: "
        "profiling normal behaviour statistically, combining supervised and unsupervised models into hybrid architectures, "
        "and dynamically adapting the detector as network traffic distributions evolve under concept drift (Table I).",

        "A. Statistical and Behaviour-Based Detection\n"
        "Statistical and behaviour-based approaches examine deviations in traffic flow distributions rather than matching static signature patterns. "
        "Timcenko and Gajin [JTN12] use entropy-based feature processing to expose hidden non-linear structures in NetFlow feature distributions, "
        "routing unusual flows to unsupervised machine learning clustering; their tests combine modelled attacks (port scans, floods, dictionary attacks) "
        "with real and botnet traffic traces [VERIFY results]. Ibrahim and Gajin [JTN11] address a critical structural vulnerability of plain entropy detectors: "
        "the fact that sophisticated attackers can inject spoofed background traffic to camouflage volumetric and structural anomalies. "
        "They monitor multiple entropy formulations simultaneously (Shannon, Rényi, and Tsallis entropies) alongside distinct-element cardinalities, "
        "classifying anomalies via multivariate rule-based logic without learned model weights [VERIFY dataset and metrics]. "
        "While both methods detect novel behavioural deviations without prior signatures, neither provides continuous online adaptation, "
        "leaving their resilience to evolving normal baseline traffic an open question.",

        "B. Hybrid Machine Learning and Deep Learning Detection\n"
        "Hybrid detection systems operate on a unified design rationale: supervised components efficiently filter known attack categories with high precision, "
        "while unsupervised, probabilistic, or reconstruction-based components inspect the residual traffic to capture unfamiliar anomalies. "
        "Wang et al. [JTN09] implement a two-step hybrid pairing a Random Forest with a deep Autoencoder. Rather than assigning samples to the top predicted class, "
        "the Random Forest evaluates an attack probability against a conservative threshold T1 (the 90th percentile of normal validation probabilities), "
        "ensuring that unfamiliar attacks are flagged rather than absorbed into the benign class. Flagged samples are subsequently re-checked by an Autoencoder "
        "trained strictly on benign traffic; samples with reconstruction error below T2 (75th percentile) are relabelled benign to suppress false alarms. "
        "Under a simulated unseen-attack protocol withholding one attack class at a time on NF-CSE-CIC-IDS2018-v2 and NF-BoT-IoT-v2, this hybrid achieved F1 scores "
        "of 99.72% on BoT-IoT and 95.90% on IDS2018, with an FPR of 1.81%; in a DoS holdout test, standard RF labelled 64.8% of attacks as normal versus only 1.8% for the probability-thresholded RF. "
        "Macko et al. [JTN06] place a supervised binary classification filter in front of an autoencoder-based flow anomaly detector on UGR'16 traffic, demonstrating higher "
        "detection rates for known threats while preserving zero-day detection capability [VERIFY]. Kwon et al. [JTN03] combine statistical filtering with a composite autoencoder. "
        "Ensemble methods expand this concept: HELAD [JTN02] pairs an autoencoder with an LSTM using time-sliced retraining, and RFG-HELAD [JTN07] introduces contrastive learning, "
        "GAN classification, and Deep k-NN out-of-distribution scoring [VERIFY]. Almuhanna and Dardouri [JTN13] deploy weighted soft voting across five ML/DL models on a 5.6M-record setup, "
        "achieving near-100% accuracy; however, their evaluation relies on standard random cross-validation without held-out attack classes, representing contextual multi-class performance rather than true zero-day detection.",

        "C. Adaptive, Online and Drift-Aware Detection\n"
        "Adaptive detectors directly confront distribution evolution in dynamic networks. Kuppa and Le-Khac [JTN04] argue that static detectors and periodic batch retraining "
        "react late to emerging intrusions and are vulnerable to attacker-induced adversarial drift; their online detector identifies drifted samples and discovers novel classes in real time [VERIFY]. "
        "ENIDrift [JTN05] constructs an adaptive ensemble featuring incremental packet-to-vector (iP2V) feature extraction, dynamic sub-classifier generation, and an online update module, "
        "reporting up to 69.78% higher F1 and 87.6% lower latency on CICIDS2017, MAWILab, and proprietary RWDIDS drift streams, alongside 100% F1 against an author-designed adversarial attack. "
        "Seth et al. [JTN10] combine an Adaptive Random Forest with Hoeffding bounds and moving-average testing on streaming CIC-IDS 2018, reporting 99.95% accuracy and 99.96% recall [VERIFY]. "
        "Zhang et al. (SSF) [JTN08] formalize continual learning by detecting drift via Kolmogorov-Smirnov statistical tests, preserving historical samples for unchanged distributions, "
        "selecting informative samples for drifted distributions, and strategically forgetting obsolete parameters; updates are guided by a labelling budget and pseudo-labelling on NSL-KDD and UNSW-NB15. "
        "Kitsune [JTN01] serves as the foundational reference for lightweight online autoencoders (KitNET), demonstrating line-speed incremental adaptation on constrained hardware.",

        "D. Synthesis & Methodological Critique\n"
        "Across these thirteen studies, the principal methodological divergence lies in experimental evaluation protocols (Table II). "
        "Hybrid detectors evaluated for unseen attack detection (e.g. [JTN09]) are predominantly static architectures that do not address ongoing concept drift. "
        "Conversely, drift-adaptive frameworks (e.g. [JTN05], [JTN08], [JTN10]) evaluate how effectively algorithms track gradual statistical shifts in known traffic distributions, "
        "frequently without evaluating how the model reacts when an entirely novel attack family suddenly appears. Furthermore, studies claiming high anomaly detection accuracy "
        "often utilize standard random splits (e.g. [JTN13]) or proprietary author-designed drift benchmarks (e.g. [JTN05]), preventing direct head-to-head performance comparisons. "
        "Truly unseen network attack detection requires unified benchmarks combining time-ordered streaming traffic, covariate drift, and strictly held-out novel attack families."
    ]

    for p_text in ivc_text:
        p = doc.add_paragraph(p_text)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15

    # Tables I & II
    add_h2("TABLE I. CATEGORY COMPARISON: ANOMALY-BASED, HYBRID AND ADAPTIVE DETECTION")
    t1 = doc.add_table(rows=14, cols=6)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    t1_headers = ["Ref", "Year", "Category", "Method / Architecture", "Adapts to Drift?", "Key Stated / Observed Limitation"]
    for c_idx, h_text in enumerate(t1_headers):
        cell = t1.rows[0].cells[c_idx]
        cell.text = h_text
        set_cell_background(cell, "1F497D")
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_margins(cell, 60, 60, 80, 80)

    t1_data = [
        ("JTN01", "2018", "Online Anomaly", "KitNET ensemble of small autoencoders", "Yes (incremental)", "Assumes benign initial training; does not isolate drift [VERIFY]"),
        ("JTN02", "2020", "Hybrid DL Ensemble", "Autoencoder + LSTM heterogeneous ensemble", "Partly (time slices)", "Retraining latency; unverified full metrics [VERIFY]"),
        ("JTN03", "2022", "Hybrid Signature+AE", "Statistical filter + composite autoencoder", "TO VERIFY", "Dual time-window thresholds require calibration [VERIFY]"),
        ("JTN04", "2022", "Adaptive / Drift", "Online drift detector + new-class discovery", "Yes (online)", "Contrastive compute overhead; labelling costs open [VERIFY]"),
        ("JTN05", "2022", "Adaptive Online", "iP2V features + adaptive ensemble (ENIDrift)", "Yes (real drift)", "Proprietary RWDIDS dataset; own adversarial attack [VERIFY]"),
        ("JTN06", "2023", "Hybrid Filter+AE", "Supervised binary filter + deep autoencoder", "No (static)", "Static model; pipeline depends on filter quality [VERIFY]"),
        ("JTN07", "2024", "Hybrid DL Ensemble", "Contrastive DNN + GAN + Deep k-NN (RFG-HELAD)", "Partly (OOD targets)", "High computational complexity; unread full text [VERIFY]"),
        ("JTN08", "2024", "Adaptive / Continual", "SSF: K-S test, selective sampling, forgetting", "Yes (continual)", "Requires manual labelling budget; older datasets (NSL-KDD)"),
        ("JTN09", "2023", "Hybrid ML+DL", "RF probability threshold + Autoencoder recheck", "No (static)", "One class withheld at a time; manual thresholds T1/T2; static"),
        ("JTN10", "2024", "Adaptive / Drift", "Adaptive Random Forest + Hoeffding bound", "Yes (stream)", "Single dataset (CIC-IDS2018); near-perfect scores [VERIFY]"),
        ("JTN11", "2022", "Statistical Entropy", "Multi-entropy monitoring + rule-based classifier", "No (rule-based)", "Rule-based classification under evolving benign traffic [VERIFY]"),
        ("JTN12", "2021", "Statistical + ML", "Entropy flow processing + unsupervised clustering", "No (static)", "Evaluated predominantly on synthetic/modelled attacks [VERIFY]"),
        ("JTN13", "2025", "Hybrid Ensemble", "Weighted soft-voting (XGB, RF, GNN, LSTM, AE)", "No (static)", "No held-out unseen classes; conventional cross-validation [VERIFY]")
    ]

    for r_idx, r_vals in enumerate(t1_data, 1):
        row = t1.rows[r_idx]
        for c_idx, val in enumerate(r_vals):
            cell = row.cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if r_idx % 2 == 1:
                set_cell_background(cell, "F9F9F9")
            set_cell_margins(cell, 40, 40, 60, 60)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    add_h2("TABLE II. DATASETS AND EVALUATION MEASURES STATUS (FROM JATIN SOURCE RECORDS)")
    t2 = doc.add_table(rows=14, cols=4)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    t2_headers = ["Ref", "Dataset / Testbed Used", "Evaluation Measures Reported", "Audit Verification Status"]
    for c_idx, h_text in enumerate(t2_headers):
        cell = t2.rows[0].cells[c_idx]
        cell.text = h_text
        set_cell_background(cell, "1F497D")
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_margins(cell, 60, 60, 80, 80)

    t2_data = [
        ("JTN01", "Mirai botnet, IP camera, synthetic attacks (Evaluation section TO VERIFY)", "F1-score, execution time, CPU/memory (TO VERIFY)", "Unverified / Abstract only"),
        ("JTN02", "Enterprise network traffic flows (exact dataset names TO VERIFY)", "Accuracy, DR, FAR, F1 (TO VERIFY)", "Unverified / Abstract only"),
        ("JTN03", "Network flow traffic (not named in accessible abstract; TO VERIFY)", "Not recorded in Jatin matrix (TO VERIFY)", "Unverified / Least confirmed"),
        ("JTN04", "2018 intrusion dataset; APT C&C + web-categorisation data", "Not recorded in Jatin matrix (abstract states highly accurate)", "Unverified / Abstract only"),
        ("JTN05", "CICIDS2017, MAWILab, author's RWDIDS drift dataset", "F1-score, running time, adversarial evasion F1 (abstract/slides)", "Partially Verified (Slides/Abstract)"),
        ("JTN06", "UGR'16 flow-based network traffic dataset (confirmed)", "Detection rate of known attacks, ROC-AUC, FPR (TO VERIFY)", "Unverified / Intro read"),
        ("JTN07", "Benchmark network intrusion datasets (specific names TO VERIFY)", "Fine-grained accuracy, recall, adversarial metrics (TO VERIFY)", "Unverified / Least confirmed"),
        ("JTN08", "NSL-KDD and UNSW-NB15 benchmarks", "Accuracy, F1, catastrophic forgetting rate (method verified)", "Partially Verified (Method read)"),
        ("JTN09", "NF-CSE-CIC-IDS2018-v2, NF-BoT-IoT-v2 (simulated unseen class holdout)", "Accuracy, precision, recall, F1-score, false-positive rate", "FULLY VERIFIED (Read in Full)"),
        ("JTN10", "CIC-IDS 2018 stream", "Accuracy (99.95%) and recall (99.96%) in abstract", "Unverified / Abstract only"),
        ("JTN11", "Experimental NetFlow-derived network traffic datasets (TO VERIFY)", "Classification accuracy, resilience against deception (TO VERIFY)", "Unverified / Abstract only"),
        ("JTN12", "Synthetic attack traffic, real captures, botnet traces", "Detection rate, false alarm rate, throughput (TO VERIFY)", "Unverified / Abstract only"),
        ("JTN13", "CICIDS2017 (5.66M records) + independent secondary benchmark", "Accuracy, precision, recall, F1-score (5-fold cross-validation)", "Unverified / Intro read")
    ]

    for r_idx, r_vals in enumerate(t2_data, 1):
        row = t2.rows[r_idx]
        for c_idx, val in enumerate(r_vals):
            cell = row.cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if r_idx % 2 == 1:
                set_cell_background(cell, "F9F9F9")
            set_cell_margins(cell, 40, 40, 60, 60)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section 6: Gaps and Directions
    add_h1("6. Research Gaps & Future Directions")
    doc.add_paragraph(
        "Based on the synthesis of Jatin's 13 papers, five core research gaps and corresponding future research directions are established. "
        "In accordance with the consolidated research pack, Gap JG5 (strict holdout of novel attack classes) is closely related to Gap JG1 "
        "and is documented both as an independent methodological vulnerability and as an integrated component of JG1."
    )

    t_gaps = doc.add_table(rows=6, cols=4)
    t_gaps.alignment = WD_TABLE_ALIGNMENT.CENTER
    gap_headers = ["Gap ID", "Research Gap Title & Evidence", "Linked Direction ID", "Future Direction Proposal"]
    for c_idx, h_text in enumerate(gap_headers):
        cell = t_gaps.rows[0].cells[c_idx]
        cell.text = h_text
        set_cell_background(cell, "1F497D")
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_margins(cell, 60, 60, 80, 80)

    import generate_jatin_matrix
    gap_rows = generate_jatin_matrix.gaps_directions_rows

    for r_idx, (gid, gtitle, gdesc, gevid, did, dprop) in enumerate(gap_rows, 1):
        row = t_gaps.rows[r_idx]
        row.cells[0].text = gid
        row.cells[1].text = f"{gtitle}\n\nEvidence: {gevid}"
        row.cells[2].text = did
        row.cells[3].text = dprop
        for c_idx in range(4):
            cell = row.cells[c_idx]
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if r_idx % 2 == 1:
                set_cell_background(cell, "F9F9F9")
            set_cell_margins(cell, 40, 40, 60, 60)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section 7: Publication Trend
    add_h1("7. Publication Trend Analysis (Category-Level)")
    doc.add_paragraph(
        "Analysis of Jatin's 13 candidate studies by publication year illustrates a clear technological shift across three distinct waves:\n"
        "• Pre-2021 Wave (2018–2020): Foundational explorations into lightweight online autoencoder ensembles (Kitsune 2018) "
        "and early heterogeneous deep ensembles with periodic time-sliced retraining (HELAD 2020).\n"
        "• 2021–2023 Wave: Diversification into multi-entropy statistical profiling (Timcenko 2021, Ibrahim 2022), hybrid signature-anomaly combinations (Kwon 2022), "
        "and initial robust drift detection frameworks (Kuppa 2022, ENIDrift 2022, Macko 2023, Wang 2023).\n"
        "• 2024–2025 Wave: Advanced continual learning and adaptive streaming classifiers (Seth 2024, Zhang 2024), fine-grained out-of-distribution ensembles (RFG-HELAD 2024), "
        "and multi-model soft-voting architectures (Almuhanna 2025).\n\n"
        "Distribution by Year: 2018 (1), 2020 (1), 2021 (1), 2022 (4), 2023 (2), 2024 (3), 2025 (1). "
        "Eleven of the 13 studies (84.6%) fall inside the recent 2021–2026 window, providing substantial evidence for the team survey."
    )

    # Section 8: Reserve Pool
    add_h1("8. Reserve Pool Candidates")
    doc.add_paragraph(
        "Jatin's workbook maintains additional reserve studies that were not part of the primary 13-paper analysis. "
        "These studies are tracked as potential replacements or expansion candidates:\n"
        "1. ADSim (Chen et al., Computer Networks 2024, DOI: 10.1016/j.comnet.2024.110423): Proposes a similarity-aware online ensemble learning framework.\n"
        "2. NetGuard (Gupta et al., arXiv:2503.03022, 2025): Pairs active learning with generative data augmentation to handle drifting and imbalanced traffic streams.\n"
        "3. Seth et al. (The Computer Journal 2024, DOI: 10.1093/comjnl/bxae023): Initially noted in the reserve sheet; reconciled into core candidate set as JTN10."
    )

    # Section 9: Contribution and Reading Declaration
    add_h1("9. Contribution Details & Reading Declaration Status")
    doc.add_paragraph(
        "A. Actual Member Contributions (Jatin, Enrolment 258100003):\n"
        "• Conducted candidate paper retrieval across general web search engines on 15 and 17 November 2026.\n"
        "• Compiled Day 1 literature review, Section Pack, and multi-sheet literature matrix.\n"
        "• Read Paper [1] / JTN09 (Wang et al., Symmetry 2023) in full end-to-end, extracting exact F1, accuracy, and false-positive metrics.\n"
        "• Partially read Paper [5] / JTN08 (Zhang et al., SSF 2024), reviewing abstract, introduction, and drift-detection methodology.\n"
        "• Drafted Section IV-C synthesis, Table I category comparison, Table II datasets/metrics table, research gaps JG1–JG5, and future directions JD1–JD5.\n"
        "• Outlined category trend chart and formatted draft IEEE bibliographic citations.\n\n"
        "B. Honest Reading Declaration Status:\n"
        "In accordance with institutional guidelines, AI file inspection is NOT claimed as personal member reading. "
        "Only Paper [1] / JTN09 was read in full. Paper [5] / JTN08 was partially read. The remaining 11 candidate studies (JTN01–JTN07, JTN10–JTN13) "
        "were inspected at abstract and secondary summary levels. Jatin must personally examine the methodology, results, and conclusion sections "
        "of each remaining paper prior to signing the final IILM Annexure contribution table and defending the work in the viva examination.\n\n"
        "C. Search Log Audit Caveat:\n"
        "Jatin's Day 1 search log records search terms but lists hit counts as 'not recorded'. Prior to final paper submission, reproducible queries "
        "must be executed in IEEE Xplore, ACM DL, SpringerLink, Google Scholar, and arXiv with exact query strings, dates, and recorded hit tallies."
    )

    # Section 10: Corrected References
    add_h1("10. Corrected IEEE References (Jatin Source Set)")
    doc.add_paragraph("The following 13 references incorporate all verified bibliographic corrections (exact pages, volumes, and working permanent DOIs/URLs):")

    refs_data = [
        ("[JTN01]", "Y. Mirsky, T. Doitshman, Y. Elovici, and A. Shabtai, \"Kitsune: An ensemble of autoencoders for online network intrusion detection,\" in Proc. 25th Annu. Netw. Distrib. Syst. Secur. Symp. (NDSS), San Diego, CA, USA, Feb. 2018, doi: 10.14722/ndss.2018.23204. [Pre-2021 Foundational Source]"),
        ("[JTN02]", "Y. Zhong et al., \"HELAD: A novel network anomaly detection model based on heterogeneous ensemble learning,\" Comput. Netw., vol. 169, Art. no. 107049, Feb. 2020, doi: 10.1016/j.comnet.2019.107049. [Pre-2021 Foundational Source]"),
        ("[JTN03]", "H.-Y. Kwon, T. Kim, and M.-K. Lee, \"Advanced intrusion detection combining signature-based and behavior-based detection methods,\" Electronics, vol. 11, no. 6, Art. no. 867, Mar. 2022, doi: 10.3390/electronics11060867."),
        ("[JTN04]", "A. Kuppa and N.-A. Le-Khac, \"Learn to adapt: Robust drift detection in security domain,\" Comput. Electr. Eng., vol. 102, Art. no. 108239, Sep. 2022, doi: 10.1016/j.compeleceng.2022.108239."),
        ("[JTN05]", "X. Wang et al., \"ENIDrift: A fast and adaptive ensemble system for network intrusion detection under real-world drift,\" in Proc. 38th Annu. Comput. Secur. Appl. Conf. (ACSAC), Austin, TX, USA, Dec. 2022, pp. 785–789, doi: 10.1145/3564625.3567992."),
        ("[JTN06]", "D. Macko, P. Goldschmidt, P. Pištek, and D. Chudá, \"Assessing the impact of a supervised classification filter on flow-based hybrid network anomaly detection,\" 2023, arXiv:2310.06656. [Preprint]"),
        ("[JTN07]", "Y. Zhong, Z. Wang, X. Shi, J. Yang, and K. Li, \"RFG-HELAD: A robust fine-grained network traffic anomaly detection model based on heterogeneous ensemble learning,\" IEEE Trans. Inf. Forensics Security, vol. 19, pp. 5895–5910, 2024, doi: 10.1109/TIFS.2024.3402439."),
        ("[JTN08]", "X. Zhang, R. Zhao, Z. Jiang, H. Chen, Y. Ding, E. C. H. Ngai, and S.-H. Yang, \"Continual learning with strategic selection and forgetting for network intrusion detection,\" 2024, arXiv:2412.16264. [Preprint; presented IEEE INFOCOM 2025, doi: 10.1109/INFOCOM55648.2025.11044615]"),
        ("[JTN09]", "C. Wang, Y. Sun, W. Wang, H. Liu, and B. Wang, \"Hybrid intrusion detection system based on combination of random forest and autoencoder,\" Symmetry, vol. 15, no. 3, Art. no. 568, Mar. 2023, doi: 10.3390/sym15030568. [Read in Full]"),
        ("[JTN10]", "S. Seth, K. K. Chahal, and G. Singh, \"Concept drift-based intrusion detection for evolving data stream classification in IDS: Approaches and comparative study,\" Comput. J., vol. 67, no. 7, pp. 2529–2547, Jul. 2024, doi: 10.1093/comjnl/bxae023."),
        ("[JTN11]", "J. Ibrahim and S. Gajin, \"Entropy-based network traffic anomaly classification method resilient to deception,\" Comput. Sci. Inf. Syst., vol. 19, no. 1, pp. 87–116, 2022, doi: 10.2298/CSIS201229045I."),
        ("[JTN12]", "V. Timcenko and S. Gajin, \"Machine learning enhanced entropy-based network anomaly detection,\" Adv. Electr. Comput. Eng., vol. 21, no. 4, pp. 51–60, 2021, doi: 10.4316/aece.2021.04006."),
        ("[JTN13]", "R. Almuhanna and S. Dardouri, \"A deep learning/machine learning approach for anomaly based network intrusion detection,\" Front. Artif. Intell., vol. 8, Art. no. 1625891, Sep. 2025, doi: 10.3389/frai.2025.1625891.")
    ]

    for tag, ref_str in refs_data:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.first_line_indent = Inches(-0.4)
        p.paragraph_format.space_after = Pt(3)
        run_tag = p.add_run(f"{tag} ")
        run_tag.bold = True
        p.add_run(ref_str)

    # Save docx
    doc.save("research-papers/Jatin_Research_Record.docx")
    print("research-papers/Jatin_Research_Record.docx generated successfully!")

if __name__ == "__main__":
    create_document()
