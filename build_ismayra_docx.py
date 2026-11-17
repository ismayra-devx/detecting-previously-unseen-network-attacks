import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
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

    # Base typography
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

    run_sub = title_p.add_run("School of Computer Science and Engineering\nMember Research Record — Ismayra Praveen (258100002)")
    run_sub.font.name = 'Times New Roman'
    run_sub.font.size = Pt(12)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    # Meta table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Member Name & Enrolment", "Ismayra Praveen (Enrolment No. 258100002) | Team Coordinator"),
        ("Assigned Category", "Deep Learning-Based Detection (10 Studies: DL01–DL10)"),
        ("Project Title", "Detecting Previously Unseen Network Attacks: A Survey"),
        ("Document Status & Date", "Authoritative Member Research Record | 17 November 2026")
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

    # Section 1: Purpose & Ingestion Scope
    add_h1("1. Purpose and Research Ingestion Scope")
    doc.add_paragraph(
        "This document establishes the authoritative member research record for Ismayra Praveen (258100002), "
        "covering the category 'Deep Learning-Based Detection' (Section IV-B) in the survey paper 'Detecting Previously Unseen Network Attacks'. "
        "It imports and formalizes Ismayra's research pack located in source_material/Ismayra_Deep_Learning_Research/, integrating the "
        "research matrix, analytical notes, and BibTeX database.\n\n"
        "Key Operational Directives Enforced:\n"
        "1. Scope Demarcation: Rigorously distinguishes between (a) direct open-set/unknown attack evidence, (b) concept drift adaptation, and (c) contextual baseline evidence.\n"
        "2. De-Duplication: Cross-checks candidate studies with Suresh's and Jatin's packs to ensure zero duplicate entries across the team master matrix.\n"
        "3. Copyright & Legal Open Access: Downloads permitted open-access PDFs into research-papers/original_pdfs/ (DL04 author preprint, DL07 Nature/PMC OA, DL10 Nature OA), "
        "while preserving permanent DOI/publisher links for paywalled sources without bypassing access controls.\n"
        "4. Academic Integrity: Antigravity AI does NOT mark Ismayra's papers as personally read; personal member reading remains honestly marked as PENDING."
    )

    # Section 2: Scope Demarcation
    add_h1("2. Evidence Scope Demarcation & Interpretation Rules")
    doc.add_paragraph(
        "To maintain rigorous scientific standards, the ten candidate deep learning studies are classified into three distinct evidential tiers:\n\n"
        "Tier A — Direct Open-Set / Unknown Attack Evidence (8 Studies: DL01, DL02, DL03, DL04, DL05, DL07, DL08, DL09):\n"
        "These investigations evaluate deep neural architectures explicitly designed to detect network traffic belonging to attack categories "
        "absent from training distributions. They employ dedicated novelty mechanisms such as extreme value reconstruction thresholding (Yang 2021), "
        "generative few-shot boundary synthesis (Liu 2021), ensemble anomaly routing (Ahmad 2022), open-set 1-vs-rest classifiers with clustering adaptation (Soltani 2023), "
        "multi-stage sequential novelty autoencoders (Hore 2024), InfoGAN with OpenMax activation Weibull calibration (Fang 2025), "
        "deep metric learning with Mahalanobis centroid thresholds (Zhang 2025), or open-set expert-in-the-loop continuous learning (Yuan 2026).\n\n"
        "Tier B — Concept Drift Adaptation Evidence (1 Study: DL06 — Zhang & Zhang 2024):\n"
        "This study combines FT-Transformers with KSWIN drift detection for online transfer learning. While highly relevant to dynamic networks, "
        "the accessible evidence evaluates continuous adaptation to shifting feature distributions rather than the strict holdout of novel attack categories. "
        "It is classified as drift adaptation, not direct proof of open-set zero-day detection.\n\n"
        "Tier C — Contextual Closed-Set Baseline Evidence (1 Study: DL10 — Farhan et al. 2025):\n"
        "This study evaluates deep neural networks on UNSW-NB15 with SMOTE balancing. However, its experimental setup is a conventional random 70/30 split "
        "where instances of all evaluated attack classes appear in training. It is included strictly as a contextual baseline to demonstrate conventional "
        "deep learning performance. CRITICAL DIRECTIVE: A high accuracy from an ordinary closed-set multi-class split must NEVER be presented as proof "
        "of previously unseen attack detection."
    )

    # Section 3: Deep Learning Detection Taxonomy
    add_h1("3. Deep Learning Architectural Taxonomy")
    doc.add_paragraph(
        "Deep learning approaches for unseen network attack detection depart fundamentally from manual feature engineering by learning "
        "hierarchical representations directly from high-dimensional network data. The reviewed literature reveals four architectural groupings:\n\n"
        "1. Deep Generative & Reconstruction-Based Models: Unsupervised generative architectures model benign traffic manifolds. "
        "In Yang et al. [DL01], class-conditioned autoencoders represent known attacks, while reconstruction errors are modeled using statistical "
        "Extreme Value Theory (EVT) to separate unknown attacks from benign outliers. In Liu et al. [DL02], Generative Adversarial Cooperative Networks (GACN) "
        "synthesize intra-category embeddings to prevent boundary collapse in few-shot intrusion settings. In Fang and Xie [DL07], InfoGAN learns "
        "disentangled traffic representations, feeding activation vectors to OpenMax.\n\n"
        "2. Open-Set Recognition with Calibrated Decision Boundaries: Standard SoftMax activation forces test inputs into one of the known classes, "
        "causing high-confidence misclassifications on unknown attacks. Open-set architectures replace SoftMax with calibrated novelty scores. "
        "Soltani et al. [DL04] employ DOC++ (1-vs-rest deep sigmoid classifiers with adaptive thresholds). Fang and Xie [DL07] use OpenMax to recalibrate "
        "penultimate activation vectors via Weibull distribution fitting, estimating an explicit unknown-class probability. Zhang et al. [DL08] deploy "
        "deep metric learning with triplet loss to cluster known classes tightly in latent space, using Mahalanobis distance thresholds to identify outliers.\n\n"
        "3. Sequential Multi-Stage & Ensemble Architectures: Recognizing that no single model covers known, unknown, and adversarial attacks simultaneously, "
        "multi-stage pipelines divide detection responsibilities. Ahmad et al. [DL03] evaluate multi-model deep learning ensembles for threats never introduced "
        "during training. Hore et al. [DL05] formulate Deep ResNIDS: a front-end deep classifier handles known threats, an anomaly autoencoder intercepts "
        "suspicious deviations, and a novelty autoencoder distinguishes true novel attack families from adversarially perturbed known traffic.\n\n"
        "4. Adaptive & Human-in-the-Loop Continual Learning: Detecting an unseen attack is only the initial operational step; adapting the IDS to incorporate "
        "the newly discovered threat without catastrophic forgetting is essential. Soltani et al. [DL04] cluster detected novel samples to assist human analysts "
        "in labelling, using confirmed clusters to update the model. Yuan et al. [DL09] deploy OpenPN with reciprocal-neighbour clustering in an expert-in-the-loop "
        "framework for continuous learning. Zhang and Zhang [DL06] demonstrate online transfer learning triggered by statistical KSWIN drift detection."
    )

    # Section 4: 10 Paper Records
    add_h1("4. Candidate Paper Register (Studies DL01–DL10)")
    doc.add_paragraph(
        "The structured records below document Ismayra's ten candidate studies, detailing verified publisher metadata, methods, datasets, "
        "unseen testing protocols, findings, caveats, and reading status:"
    )

    import generate_ismayra_matrix
    dl_rows = generate_ismayra_matrix.dl_matrix_rows

    for r in dl_rows:
        pid, scope, title, authors, year, venue, doi, link, oa_st, mfam, meth, data, unseen, find, lim, pub_st, s_rev, t_read = r
        add_h2(f"{pid}: {title}")
        t = doc.add_table(rows=11, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        fields = [
            ("Authors", authors),
            ("DOI / Permanent Link", f"DOI: {doi}\nURL: {link}"),
            ("Year / Venue / Status", f"{year}; {venue} ({pub_st})"),
            ("Evidence Scope", scope),
            ("Method Family & Architecture", f"{mfam}\nSummary: {meth}"),
            ("Dataset / Testbed Used", data),
            ("Unseen Holdout Protocol?", unseen),
            ("Reported Findings / Performance", find),
            ("Critical Limitations / Caveats", lim),
            ("Legal OA-PDF Status", oa_st),
            ("Verification & Reading Status", f"Publisher Audit: {s_rev}\nMember Reading: {t_read}")
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

    # Section 5: Section IV-B Synthesis Draft
    add_h1("5. Section IV-B Synthesis Draft (Deep Learning-Based Detection)")
    doc.add_paragraph(
        "The text below provides the complete third-person academic synthesis for Section IV-B of the survey paper, "
        "integrating the ten studies and concluding with Table 1:"
    )

    ivb_paras = [
        "IV-B. Deep Learning-Based Detection\n"
        "Deep learning approaches for detecting previously unseen network attacks depart fundamentally from shallow machine learning by learning "
        "hierarchical, non-linear representations directly from high-dimensional flow statistics and raw packet captures. "
        "The ten studies reviewed in this category [DL01]–[DL10] demonstrate that deep neural networks cannot reliably detect novel threats through "
        "conventional closed-world classification alone; rather, they succeed only when paired with explicit novelty mechanisms such as generative reconstruction, "
        "open-set probability calibration, deep metric clustering, or multi-stage filtering (Table 1).",

        "1) Generative and Reconstruction-Based Deep Models\n"
        "Generative architectures address the severe data imbalance between voluminous benign traffic and sparse novel attacks by modelling the underlying distribution "
        "of normal or known traffic. Yang et al. [DL01] formalize fine-grained intrusion detection as a two-stage learning problem. They train class-conditioned variational "
        "autoencoders (CVAEs) on known attack classes and utilize statistical Extreme Value Theory (EVT) to model the tail distribution of reconstruction errors; samples "
        "exceeding the EVT threshold are flagged as unknown anomalies, while benign-traffic clustering suppresses false alarms [VERIFY dataset splits and metrics]. "
        "Liu et al. [DL02] address the related few-shot challenge where novel attacks possess minimal training representation. Their SFE-GACN framework couples Session Feature "
        "Embedding (SFE) to capture temporal context with a Generative Adversarial Cooperative Network (GACN) that synthesizes intra-category latent embeddings, reporting an "
        "average True Positive Rate 8.38% higher and False Positive Rate 12.77% lower than baseline comparison models on evaluated benchmarks.",

        "2) Open-Set Recognition and Decision-Boundary Calibration\n"
        "Standard deep classifiers deploy SoftMax output layers that normalize logits into class probabilities summing to one, compelling the network to assign an unfamiliar "
        "zero-day exploit to whichever known class happens to receive the highest logit. Open-set deep learning overcomes this failure mode by calibrating activation vectors. "
        "Fang and Xie [DL07] integrate an Information-Maximizing GAN (InfoGAN) with OpenMax on CICIDS2017 and NSL-KDD. InfoGAN extracts disentangled representation vectors, "
        "and OpenMax fits Weibull distributions to activation distances to calculate explicit unknown-class probabilities. On CICIDS2017, their model achieved open-set accuracy "
        "exceeding 88.5% for misuse detection and 88.2% for anomaly detection, while NSL-KDD experiments confirmed OpenMax significantly outperformed SoftMax when entire attack "
        "categories were held out. Zhang et al. [DL08] take a metric-learning route: a 1D Convolutional Neural Network trained with triplet and cross-entropy loss maps flows into "
        "compact hyperspherical clusters, updating class centroids via the Weiszfeld algorithm. Flows falling outside a Mahalanobis distance threshold are isolated as novel threats, "
        "achieving reported average accuracies of 97.28% on CICIDS2017 and 85.47% on UNSW-NB15.",

        "3) Sequential Multi-Stage Pipelines and Adversarial Resilience\n"
        "Sequential deep architectures decompose detection into staged specialized networks to prevent adversarial manipulation and false alarms. "
        "Ahmad et al. [DL03] evaluate deep learning ensembles specifically targeted at network attacks never introduced during training [VERIFY]. "
        "Hore et al. [DL05] present Deep ResNIDS, a sequential three-stage framework comprising a deep malicious-packet classifier for known threats, an autoencoder-based anomaly "
        "detector for suspicious flows, and a specialized novelty autoencoder. By evaluating across CICIDS2017 and CSE-CIC-IDS2018 (with the latter serving as an out-of-distribution testbed), "
        "their architecture demonstrated that the novelty autoencoder successfully distinguishes true zero-day attack families from adversarially perturbed variants of known attacks, "
        "achieving 98.5% overall accuracy. However, this headline figure represents aggregate classification across all stages and should not be conflated with dedicated zero-day recall.",

        "4) Continuous Learning and Human-in-the-Loop Adaptation\n"
        "A critical operational insight across this literature is that detecting a novel attack and safely updating the IDS are distinct operational tasks. "
        "Soltani et al. [DL04] propose an adaptable deep learning IDS comparing DOC++, DOC, OpenMax, and AutoSVM on CICIDS2017 and CSE-CIC-IDS2018. DOC++ (deep 1-vs-rest sigmoidal classifiers) "
        "achieved the highest open-set recognition performance; detected unknown instances are subsequently grouped via clustering to assist security analysts in labelling, and confirmed "
        "attack classes are integrated via incremental retraining. Yuan et al. [DL09] formalize this workflow via OpenPN, using density-based k-reciprocal nearest-neighbour clustering "
        "in an expert-in-the-loop framework for continuous learning across three public benchmarks [VERIFY]. Conversely, Zhang and Zhang [DL06] demonstrate online transfer learning using "
        "FT-Transformers triggered by KSWIN concept drift detection (99.46% accuracy on CIC-IDS); while highly effective for distribution tracking, it evaluates concept drift rather than "
        "the appearance of held-out novel attack classes.",

        "5) Contextual Baselines and Methodological Critique\n"
        "To establish a clear baseline, Farhan et al. [DL10] evaluate a conventional deep learning NIDS on UNSW-NB15 using SMOTE class balancing. While achieving high accuracy on standard "
        "test splits, the study evaluates a closed-world protocol where all attack classes were present during training. As evidenced across [DL01]–[DL09], such closed-set models fail "
        "entirely when confronted with zero-day exploits. Truly effective zero-day deep learning requires: (1) open-set calibration to reject unknown inputs; (2) robust representation spaces "
        "that separate stealthy attacks from benign variance; and (3) verified human-in-the-loop adaptation pipelines to incorporate novel attack families without catastrophic forgetting."
    ]

    for p_text in ivb_paras:
        p = doc.add_paragraph(p_text)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15

    # Table 1: Category Comparison
    add_h2("Table 1. Deep Learning Studies Reviewed (Section IV-B Summary)")
    t_comp = doc.add_table(rows=11, cols=5)
    t_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_headers = ["ID", "Architecture / Method", "Dataset / Testbed", "Main Reported Result", "Evidential Scope & Limitations"]
    for c_idx, h_text in enumerate(t_headers):
        cell = t_comp.rows[0].cells[c_idx]
        cell.text = h_text
        set_cell_background(cell, "1F497D")
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_margins(cell, 60, 60, 80, 80)

    t_data = [
        ("DL01", "CVAE + EVT tail thresholding", "CICIDS2017, UNSW-NB15", "Improved unknown attack detection with low FPR reported", "Core: Direct unknown evidence; EVT tail sensitive to outliers; exact splits pending"),
        ("DL02", "Session Embedding (SFE) + GACN", "UNSW-NB15, CICIDS2017", "TPR +8.38%, FPR -12.77% vs. baseline in few-shot session tests", "Core: Direct unknown evidence; gains tied to few-shot session embedding assumptions"),
        ("DL03", "Deep Learning Ensemble", "NSL-KDD, UNSW-NB15, CICIDS2017", "Ensemble superior to single models on unintroduced threats", "Core: Direct unknown evidence; per-class metrics unexposed in accessible abstract"),
        ("DL04", "DOC++ Open-Set + Clustering Adaptation", "CICIDS2017, CSE-CIC-IDS2018", "DOC++ outperforms OpenMax, DOC, AutoSVM on open-set holdout", "Core: Direct open-set evidence; requires expert labelling for safe model updating"),
        ("DL05", "Deep ResNIDS (3-stage sequential)", "CICIDS2017, CICIDS2018, botnet, adversarial", "98.5% overall accuracy; evaluates OOD, zero-day, adversarial", "Core: Direct unknown/OOD evidence; 98.5% is overall accuracy, not single zero-day recall"),
        ("DL06", "FT-Transformer + KSWIN drift detection", "CIC-IDS, NetFlow V2 streams", "99.46% and 96.79% average accuracy under drift tracking", "Adjacent: Drift adaptation evidence; does NOT demonstrate held-out attack classes"),
        ("DL07", "InfoGAN + OpenMax Weibull scoring", "CICIDS2017, NSL-KDD", "CICIDS open-set acc >88.5% (misuse), >88.2% (anomaly); beats SoftMax", "Core: Direct open-set evidence; full OA PDF archived; high per-class variance"),
        ("DL08", "1D-CNN + Deep Metric Learning", "CICIDS2017, UNSW-NB15", "Average accuracy 97.28% (CICIDS) and 85.47% (UNSW-NB15)", "Core: Direct unknown evidence; Mahalanobis centroid threshold; openness ratios pending"),
        ("DL09", "OpenPN + Expert Loop Continual DL", "Three benchmark intrusion datasets", "Superior closed-set and open-set recognition reported", "Core: Direct open-set evidence; publisher access restricted; numerical matrices pending"),
        ("DL10", "Conventional Deep Learning NIDS", "UNSW-NB15 (175,341 records, SMOTE)", "High closed-set classification accuracy on standard split", "Contextual Baseline Only; conventional split; NOT evidence of zero-day detection")
    ]

    for r_idx, r_vals in enumerate(t_data, 1):
        row = t_comp.rows[r_idx]
        for c_idx, val in enumerate(r_vals):
            cell = row.cells[c_idx]
            cell.text = val
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if r_idx % 2 == 1:
                set_cell_background(cell, "F9F9F9")
            set_cell_margins(cell, 40, 40, 60, 60)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section 6: Cross-Reference & De-Duplication Audit
    add_h1("6. Cross-Reference and De-Duplication Audit")
    doc.add_paragraph(
        "A rigorous cross-member audit was conducted comparing Ismayra's 10 candidate studies with Suresh's 9 studies and Jatin's 13 studies:\n\n"
        "• Elimination of Overlap: Suresh's pack includes Farrukh et al. (2023) [SG06], an open-set IoT payload classifier. To prevent duplicate citation, "
        "Farrukh et al. is retained exclusively in Suresh's category and is NOT duplicated in Ismayra's pack.\n"
        "• Reconciliation with Existing Draft: Soltani et al. (2023) [DL04] was cited as reference [6] in the non-authoritative draft, and Yuan et al. (2026) [DL09] "
        "was cited as reference [12]. Both are fully incorporated into Ismayra's register.\n"
        "• Total Evidence Base: Ismayra's 10 distinct studies combine with Suresh's 9 studies and Jatin's 13 studies to establish a master evidence base of "
        "exactly 32 unique candidate papers, with zero cross-member duplicates."
    )

    # Section 7: Critical Survey Themes
    add_h1("7. Critical Survey Themes & Open Research Questions")
    doc.add_paragraph(
        "Ismayra's analytical notes identify five fundamental methodological themes that structure the comparative analysis in Section V and research gaps in Section VI:\n\n"
        "1. Open-Set Testing is Essential: Closed-world binary or multi-class classification accuracy (e.g. [DL10]) provides zero evidence of zero-day detection capability. "
        "Researchers must evaluate on leave-attack-family-out splits using open-set metrics (OpenAUC, AUROC, AUPRC).\n\n"
        "2. Novelty Scores Require Formal Calibration: Reconstruction error (Yang [DL01]), OpenMax probability (Fang [DL07]), Mahalanobis distance (Zhang [DL08]), "
        "and 1-vs-rest margins (Soltani [DL04]) each define 'novelty' differently. Decision thresholds set manually on validation sets fail in production because real zero-day attacks "
        "are absent from validation data.\n\n"
        "3. Human Review Remains Essential for Safe Adaptation: Finding an unknown anomaly and safely retraining an operational model are separate tasks. "
        "Frameworks such as DOC++ [DL04] and OpenPN [DL09] incorporate clustering and human expert review to label new attacks before updating model weights, preventing poisoning.\n\n"
        "4. Metrics Are Not Interchangeable: Reported headline metrics vary wildly. Average classification accuracy under random splits must never be ranked against open-set AUROC "
        "or dedicated unknown-class recall.\n\n"
        "5. Concept Drift and Unknown Attacks Are Distinct Phenomena: A distribution shift in benign traffic represents covariate drift (evaluated in Zhang [DL06]), whereas an unfamiliar "
        "attack represents a semantic novelty in the label space. Robust IDSs must decouple benign drift adaptation from novel-class discovery."
    )

    # Section 8: Verification Report & Honest Reading Declaration
    add_h1("8. Verification Report & Honest Reading Declaration")
    doc.add_paragraph(
        "A. Verification Report Across Three Evidential Tiers:\n"
        "1. Publisher-Record Checks (All 10 Studies): Confirmed titles, full author lists, publication years, venues, and official DOIs via IEEE Xplore, ScienceDirect, "
        "Nature Scientific Reports, Springer, and Wiley catalogues.\n"
        "2. Full-Text Access (4 Studies): Full open-access PDFs legally downloaded and archived in research-papers/original_pdfs/ for DL07 (Fang 2025, Nature/PMC, 6.7 MB), "
        "DL10 (Farhan 2025, Nature OA, 2.3 MB), and DL04 (Soltani 2021, arXiv preprint, 447 KB). Full text accessible for DL05 (Hore 2024 via ScienceDirect CC-BY).\n"
        "3. Paywalled / Subscription Access (6 Studies): Formal publisher DOI and permanent links archived for DL01, DL02, DL03, DL06, DL08, DL09 without bypassing access controls.\n\n"
        "B. Honest Reading Declaration Status:\n"
        "In strict adherence to academic integrity and the IILM guidelines: Antigravity AI file ingestion and automated publisher checks do NOT constitute personal member reading. "
        "Ismayra Praveen has NOT yet confirmed personal reading of the methodology, results, and conclusion sections for these papers. "
        "All ten studies remain explicitly marked as PENDING in the reading checklist. Ismayra must personally read the required sections before signing the final IILM contribution table."
    )

    # Section 9: Corrected References
    add_h1("9. Corrected IEEE References (Ismayra Category)")
    doc.add_paragraph("The following ten references reflect verified publisher metadata and permanent links:")

    refs_data = [
        ("[DL01]", "J. Yang, X. Chen, S. Chen, X. Jiang, and X. Tan, \"Conditional variational auto-encoder and extreme value theory aided two-stage learning approach for intelligent fine-grained known/unknown intrusion detection,\" IEEE Trans. Inf. Forensics Security, vol. 16, pp. 3538–3553, 2021, doi: 10.1109/TIFS.2021.3083422."),
        ("[DL02]", "A. Liu, Y. Wang, and T. Li, \"SFE-GACN: A novel unknown attack detection under insufficient data via intra categories generation in embedding space,\" Comput. Secur., vol. 105, Art. no. 102262, Jun. 2021, doi: 10.1016/j.cose.2021.102262."),
        ("[DL03]", "R. Ahmad, I. Alsmadi, W. Alhamdani, and L. Tawalbeh, \"A deep learning ensemble approach to detecting unknown network attacks,\" J. Inf. Secur. Appl., vol. 67, Art. no. 103196, Jun. 2022, doi: 10.1016/j.jisa.2022.103196."),
        ("[DL04]", "M. Soltani, B. Ousat, M. J. Siavoshani, and A. H. Jahangir, \"An adaptable deep learning-based intrusion detection system to zero-day attacks,\" J. Inf. Secur. Appl., vol. 76, Art. no. 103516, Aug. 2023, doi: 10.1016/j.jisa.2023.103516. [Author preprint: arXiv:2108.09199]"),
        ("[DL05]", "S. Hore, J. Ghadermazi, A. Shah, and N. D. Bastian, \"A sequential deep learning framework for a robust and resilient network intrusion detection system,\" Comput. Secur., vol. 144, Art. no. 103928, Sep. 2024, doi: 10.1016/j.cose.2024.103928. [Open Access]"),
        ("[DL06]", "Z. Zhang and H. Zhang, \"An online transfer learning model for intrusion detection using FT-Transformer and KSWIN-driven concept drift detection mechanism,\" in Proc. 5th Int. Conf. Comput. Eng. Appl. (ICCEA), 2024, pp. 421–426, doi: 10.1109/ICCEA62105.2024.10603489. [Drift Adaptation Context]"),
        ("[DL07]", "J. Fang and C. Xie, \"Unknown intrusion traffic detection method based on unsupervised learning and open-set recognition,\" Sci. Rep., vol. 15, Art. no. 17001, May 2025, doi: 10.1038/s41598-025-01084-1. [Open Access via Nature/PMC]"),
        ("[DL08]", "J. Zhang, Q. Wang, Z. Cai, K. Wang, and L. Zhu, \"Unknown attack detection method based on deep metric learning,\" Concurr. Comput. Pract. Exp., vol. 37, no. 18–20, Art. no. e70193, Jul. 2025, doi: 10.1002/cpe.70193."),
        ("[DL09]", "X. Yuan, P. Yu, S. Liu, Z. Sun, Y. Zhang, and J. Xu, \"An expert-in-the-loop framework for unknown attack detection via open-set recognition,\" J. Comput. Secur., vol. 34, no. 3, pp. 193–210, Feb. 2026, doi: 10.1177/0926227X251414058."),
        ("[DL10]", "M. Farhan et al., \"Network-based intrusion detection using deep learning technique,\" Sci. Rep., vol. 15, Art. no. 25550, Jul. 2025, doi: 10.1038/s41598-025-08770-0. [Contextual Baseline Only; Open Access]")
    ]

    for tag, ref_str in refs_data:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.first_line_indent = Inches(-0.4)
        p.paragraph_format.space_after = Pt(3)
        run_tag = p.add_run(f"{tag} ")
        run_tag.bold = True
        p.add_run(ref_str)

    doc.save("research-papers/Ismayra_Research_Record.docx")
    print("research-papers/Ismayra_Research_Record.docx generated successfully!")

if __name__ == "__main__":
    create_document()
