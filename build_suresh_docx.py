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

    run_sub = title_p.add_run("School of Computer Science and Engineering\nMember Research Record — Suresh Gopal Singh (258100001)")
    run_sub.font.name = 'Times New Roman'
    run_sub.font.size = Pt(12)
    run_sub.font.bold = True
    run_sub.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

    # Meta table
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Member Name & Enrolment", "Suresh Gopal Singh (Enrolment No. 258100001)"),
        ("Assigned Category", "Machine Learning and Open-Set Detection (9 Papers: SG01–SG09)"),
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

    # Section 1: Purpose & Correction Hierarchy
    add_h1("1. Purpose and Correction Hierarchy")
    doc.add_paragraph(
        "This document establishes the authoritative member research record for Suresh Gopal Singh (258100001), "
        "covering the category 'Machine Learning and Open-Set Detection' (9 studies: SG01–SG09). "
        "It integrates Suresh's Day 1 literature matrix, Day 2 drafts of Section I (Introduction) and Section IV-A, "
        "and the Day 3 Verification Report, which serves as the highest auditing authority.\n\n"
        "Correction Hierarchy Enforced:\n"
        "1. Suresh Day 3 Verification Report: Overrides all preliminary or unverified claims in Day 1 and Day 2 drafts.\n"
        "2. Suresh Consolidated Research Pack: Primary narrative and tabular basis for category review.\n"
        "3. Raw Source Audit Trail (Day 1 & Day 2 files): Historical baseline retained for traceability.\n\n"
        "Honest Reading Status Rule: Checking publisher catalogues, arXiv pages, and accessible PDF sections during the Day 3 audit "
        "does NOT constitute personal end-to-end reading of every paper. Suresh must personally read the methodology, results, and conclusion "
        "sections before final submission and viva defense. Declared reading statuses are preserved honestly."
    )

    # Section 2: Methods Found Across the Nine Papers
    add_h1("2. Methods Found Across the Nine Papers")
    doc.add_paragraph(
        "Suresh's review examined machine learning methods designed to detect attacks absent from training data, "
        "grouped across four architectural paradigms:\n\n"
        "• Supervised Methods: Random Forest (SG02, SG06 meta-classifier, SG08), XGBoost (SG06, SG07, SG08), Decision Tree (SG05 baseline), "
        "Multilayer Perceptron (SG05 baseline, SG09 baseline), Support Vector Machine (SG05 baseline, SG09 baseline).\n\n"
        "• Unsupervised and One-Class Methods: Isolation Forest (SG02, SG03, SG08, SG09 baseline), Extended Isolation Forest (SG04), "
        "One-Class SVM (SG02, SG08), Local Outlier Factor (SG02), usfAD stochastic-forest anomaly detector (SG02), "
        "Recurrent Autoencoder / LSTM autoencoder (SG03), deep autoencoder hybrids DAGMM-EIF and MemAE-EIF (SG04), Variational Autoencoder (SG02).\n\n"
        "• Open-Set Recognition Methods: Potts-model Multi-Class Energy-based Flow Classifier (SG05), serially connected CNN base learners "
        "with multi-model voting meta-classifiers on packet payload images (SG06), deep embedding clustering with XGBoost latent separation (TEX-DEC, SG07), "
        "hyperspherical contrastive loss for anomaly detection (CLAD) and open-set recognition (CLOSR) (SG09).\n\n"
        "• Signature-Based Detection Baseline: Reviewed in Guo (SG01), Smolen & Benova (SG03), and Miran & Kadir (SG08) as the conventional "
        "baseline whose fundamental inability to detect novel attack patterns motivates machine learning and open-set detection.\n\n"
        "Overlap Note: Autoencoder architectures and contrastive learning methods interface directly with Ismayra's Deep Learning category. "
        "By agreement, Suresh's category focuses on the classical machine learning, one-class, and decision-boundary open-set properties of these models."
    )

    # Section 3: Review Questions & Difficulty Analysis
    add_h1("3. Review Questions and Difficulty Analysis")
    doc.add_paragraph(
        "A. Consolidated Review Questions:\n"
        "• RQ1: Which machine-learning and open-set approaches have been proposed to detect previously unseen network attacks, and how can they be grouped?\n"
        "• RQ2: Which datasets and evaluation measures do these studies use, and do their experiments actually evaluate attacks missing from training data?\n"
        "• RQ3: What limitations remain unresolved in false-alarm suppression, labelled-data requirements, computational cost, and cross-network generalisation?\n\n"
        "B. Why Previously Unseen Attacks Are Difficult to Detect:\n"
        "1. Nothing to Match: Signature-based systems require a known rule; an unfamiliar attack with no matching signature passes undetected (SG01, SG03, SG08).\n"
        "2. Supervised Blind Spot: Supervised classifiers learn closed-world decision boundaries. When an unfamiliar attack class appears, "
        "the classifier forces it into the most similar known class or labels it normal. In SG02, Random Forest attack F1 fell to 0% (accuracy 51.88%) on NSL-KDD "
        "once four attack types were removed from training.\n"
        "3. Attack Scarcity vs. Benign Diversity: Malicious traffic comprises a tiny fraction of network flows, while benign traffic exhibits vast diversity. "
        "Consequently, unfamiliar benign traffic frequently triggers false alerts in anomaly detectors (SG06, SG09).\n"
        "4. Unusual Does Not Mean Malicious: Unsupervised anomaly detectors flag traffic that deviates from normal profiles, but anomalous flows are frequently "
        "benign system updates or protocol bursts, resulting in high false alarm rates (SG04, SG09).\n"
        "5. Detectors Disagree: In SG03, an Autoencoder and an Isolation Forest applied to 90.9 million unlabelled web requests flagged completely disjoint sets "
        "of anomalies (0% overlap in their top-100 lists), proving there is no uniform operational definition of an anomaly.\n"
        "6. Dishonest / Conflated Testing: Many published studies evaluate models using standard random train/test splits where instances of all attack classes "
        "appear in training data (e.g. SG08). Only studies enforcing strict leave-attack-family-out splits (SG02, SG05, SG06, SG07, SG09) genuinely test unseen attacks."
    )

    # Section 4: 9 Paper Records
    add_h1("4. Nine Paper Records (Incorporating Day 3 Corrections)")
    doc.add_paragraph(
        "The following structured records document Suresh's nine candidate studies. All metrics and findings reflect the verified corrections "
        "established in the Day 3 Verification Report:"
    )

    import generate_suresh_matrix
    s_rows = generate_suresh_matrix.suresh_matrix_rows

    for r in s_rows:
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
            ("Limitations & Reading Status", f"Limitations: {lim}\nReading: {read_st}\nDay 3 Audit: {ver_st}")
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

    # Section 5: Revised Section I Draft
    add_h1("5. Revised Introduction Draft (Section I)")
    doc.add_paragraph(
        "The draft text below provides the complete Section I (Introduction) for the final survey paper, "
        "integrating Suresh's Day 2 text with Day 3 corrections:"
    )

    intro_paras = [
        "A. Background\n"
        "A network intrusion detection system (IDS) monitors network activity and raises alerts when traffic exhibits patterns indicative of malicious activity. "
        "Historically, the majority of deployed network intrusion detection systems relied on signature-based detection mechanisms. Signature-based systems inspect packet "
        "payloads and protocol headers against pre-compiled databases of known exploit patterns. When an observed sequence matches an established signature rule, an alert is raised. "
        "This design provides deterministic detection for previously documented threats, allows network operators to inspect the exact rule that fired, and operates with minimal false-alarm overhead. "
        "However, signature-based architectures suffer from an inherent design limitation: a signature rule must be manually crafted, tested, and distributed before an attack can be intercepted. "
        "If an adversary modifies the packet ordering, encrypts the payload, or employs a previously undocumented zero-day vulnerability, the attack passes through the inspection boundary completely unnoticed [SG01].",

        "Machine learning approaches offer a fundamentally different detection methodology. Rather than depending on pre-programmed rules, machine learning models infer classification "
        "boundaries from network traffic feature distributions. Supervised learning algorithms, such as Random Forest and XGBoost, train on labelled datasets containing benign flows and "
        "documented attack instances, achieving exceptional classification accuracy on benchmark datasets [SG08]. Nevertheless, supervised classifiers operate under a closed-world assumption: "
        "they assume that the classes encountered during live deployment are identical to those represented in the training set. When confronted with unfamiliar network attacks, supervised models "
        "consistently misclassify malicious traffic as normal benign activity [SG02]. Conversely, unsupervised anomaly detection approaches—such as Isolation Forest, One-Class SVM, and deep autoencoders—"
        "attempt to circumvent this blind spot by learning representation boundaries solely from benign traffic profiles [SG03], [SG04]. While unsupervised anomaly detectors can flag unfamiliar deviations, "
        "they frequently generate high false-alarm rates because anomalous network activity is not necessarily malicious, and their alerts lack explanatory attack classifications.",

        "B. Need for the Review\n"
        "Numerous investigations published between 2021 and 2026 have proposed machine learning, deep learning, and hybrid architectures to overcome the zero-day detection barrier. "
        "However, existing literature exhibits substantial inconsistency in experimental evaluation protocols and terminology. Studies frequently use the term 'unknown attack' interchangeably "
        "to describe three distinct phenomena: (1) closed-set cross-validation where all attack classes were present during training [SG08]; (2) concept drift, where known attack distributions shift "
        "gradually over time; and (3) genuine open-set detection, where entire attack classes or families are strictly withheld from training and validation datasets [SG02], [SG09]. "
        "Furthermore, evaluation measures vary widely across studies—spanning closed-set accuracy, F1-score, area under the ROC curve (AUROC), and open-set AUC (OpenAUC)—making direct comparative "
        "assessment difficult for practitioners. This survey provides a structured review of nine candidate studies in machine learning and open-set detection, evaluating their methodologies, "
        "experimental holdout protocols, reported findings, and operational trade-offs under a unified critical framework.",

        "C. Review Questions\n"
        "This review is structured around three core research questions:\n"
        "• RQ1: Which machine-learning and open-set approaches have been proposed to detect previously unseen network attacks, and how can they be grouped?\n"
        "• RQ2: Which datasets and evaluation measures do these studies use, and do their experiments actually evaluate attacks missing from training data?\n"
        "• RQ3: What limitations remain unresolved in false-alarm suppression, labelled-data requirements, computational cost, and cross-network generalisation?",

        "D. Contributions\n"
        "This survey makes three primary contributions:\n"
        "1. It provides a structured comparative summary of nine machine-learning and open-set studies published between 2021 and 2026, documenting architectures, datasets, metrics, verified findings, and operational limitations (Table 1).\n"
        "2. It rigorously categorizes studies based on experimental integrity, separating investigations that enforce strict class-level holdout protocols from those evaluating conventional closed-set classifications.\n"
        "3. It traces identified research gaps directly to empirical evidence from reviewed papers, formulating concrete research directions for deployable zero-day intrusion detection.",

        "E. Paper Organisation\n"
        "Section II details the search and selection methodology. Section III establishes the taxonomy of detection approaches. Section IV provides the literature review across three core categories: "
        "Machine Learning and Open-Set Detection (Section IV-A), Deep Learning-Based Detection (Section IV-B), and Anomaly-Based, Hybrid and Adaptive Detection (Section IV-C). Section V presents a comparative analysis. "
        "Section VI discusses research gaps, Section VII outlines future directions, and Section VIII concludes the paper."
    ]

    for p_text in intro_paras:
        p = doc.add_paragraph(p_text)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15

    # Section 6: Revised Section IV-A Draft
    add_h1("6. Revised Section IV-A Synthesis Draft")
    doc.add_paragraph(
        "The following draft text provides the complete synthesis for Section IV-A of the survey paper, "
        "incorporating all verified Day 3 corrections and Table 1:"
    )

    iva_paras = [
        "IV-A. Machine Learning and Open-Set Detection\n"
        "This subsection reviews machine learning approaches that aim to detect network attacks missing from training data. "
        "It examines signature-based detection as the conventional baseline, analyses the supervised classification blind spot, "
        "evaluates unsupervised one-class pipelines, and details recent advances in open-set recognition (Table 1).",

        "1) Signature-Based Detection and Its Limits\n"
        "Signature-based detection remains widely deployed in commercial and enterprise intrusion detection systems due to its high processing throughput, "
        "deterministic matching logic, and transparent alert explainability. However, its fundamental vulnerability is structural: an attack signature cannot be generated "
        "until an exploit has been observed, analysed by security researchers, and distributed via rule updates. In the comprehensive review by Guo [SG01], signature-based systems "
        "are shown to be structurally incapable of catching zero-day threats, underscoring the necessity of machine learning alternatives while noting that learning-based methods "
        "face significant operational challenges in classification consistency across disparate attack types.",

        "2) Supervised Models and Their Blind Spot\n"
        "Supervised classifiers achieve near-perfect classification performance on static benchmark datasets when test traffic mirrors training distributions. "
        "In Miran and Kadir [SG08], XGBoost achieved 99.3% accuracy and a 99.4% F1-score on CICIDS2017, while Random Forest achieved 98.8% accuracy. However, because the study did not describe "
        "a class-level holdout protocol, these metrics reflect closed-set classification of known attacks rather than zero-day detection. The study by Uddin et al. [SG02] demonstrates "
        "the catastrophic failure mode of supervised models under real-world zero-day conditions: when four attack categories were withheld from the training set of a Random Forest on NSL-KDD, "
        "its F1-score for detecting attacks collapsed to 0% (overall accuracy 51.88%). The classifier did not indicate uncertainty; it simply assigned the unfamiliar attack traffic to the normal class.",

        "3) Unsupervised and One-Class Models\n"
        "Unsupervised and one-class anomaly detectors avoid closed-world assumptions by profiling only benign traffic distributions, flagging any flow that deviates from normal representations. "
        "The trade-off lies in recall and false-positive control. In [SG08], One-Class SVM reached 92.1% accuracy but only 59.2% recall on anomaly detection, missing more than 40% of malicious flows, "
        "while Isolation Forest reached 91.6% accuracy and a 69.5% F1-score (recall 59.7%). The usfAD stochastic-forest framework in [SG02] maintains stable accuracy across 10 benchmark datasets "
        "(e.g., 99.43% on ToN-IoT-Network and 80.23% to 82.15% on UNSW-NB15), though its recall dropped on UNSW-NB15 (74.33%), Darknet2020 (70.40%), and XIIoTID (87.92%). "
        "Furthermore, unlabelled evaluation severely constrains empirical validation: Smolen and Benova [SG03] compared an LSTM-based recurrent autoencoder against Isolation Forest on 90.9 million "
        "unlabelled web requests. The two models flagged entirely disjoint anomaly sets with 0% overlap in their top-100 anomaly lists; while the autoencoder was faster (0.099 s vs. 0.468 s per 1,000 samples "
        "due to GPU acceleration), the absence of ground-truth labels prevented direct calculation of precision, recall, or zero-day detection rates.",

        "4) Hybrid Unsupervised Pipelines\n"
        "Hybrid pipelines combine multi-stage unsupervised learners to balance detection latency and accuracy. Carrera et al. [SG04] deployed a deep autoencoder as a fast first-stage filter, "
        "passing suspicious residual flows to an Extended Isolation Forest (EIF) for second-tier anomaly verification. Their MemAE-EIF configuration achieved verified F1-scores of 0.9234 on KDDCUP99 "
        "and 0.9172 on NSL-KDD, but performance dropped to 0.7146 on CIC-IDS2017. The authors note significant deployment constraints: EIF is memory-intensive and non-parallelisable, real-time inference "
        "requires GPU acceleration, and the anomaly threshold was artificially derived from the known percentage of anomalies in the test set, an assumption that cannot be made in operational networks.",

        "5) Open-Set Recognition\n"
        "Open-set recognition formalizes unknown attack detection by explicitly training classifiers to identify when an input belongs to none of the known training classes. "
        "The Potts-model Energy-based Flow Classifier (EFC) in [SG05] assigns flow energy scores, labelling samples as suspicious when energy exceeds a 95th-percentile threshold. "
        "On CICIDS2017, EFC achieved the highest macro F1 (0.752) among compared baselines, but open-set testing revealed that Bot, PortScan, and Web Attack categories were almost totally misclassified "
        "when held out as unknown. Farrukh et al. [SG06] transformed packet payloads into serialized RGB images, clustering benign traffic into seven groups to train parallel CNN base learners "
        "combined with meta-classifier voting, achieving an 88% detection rate on unseen attack payloads [VERIFY held-out classes]. Bizzarri et al. [SG07] developed TEX-DEC, combining deep embedding "
        "clustering with XGBoost; on CIC-IDS2017, it achieved AUROCs of 0.9843 (Infiltration), 0.9939 (SSH-Patator), and 0.9950 (FTP-Patator), and maintained 0.9939 under cross-dataset covariate shift on UNSW-NB15, "
        "though XGBoost training requires access to some novel-class instances. Wilkie et al. [SG09] proposed CLAD, using a contrastive loss to model benign traffic as a von Mises-Fisher distribution on a hypersphere. "
        "With Heartbleed and SQL Injection strictly held out as zero-day attacks on Lycos2017 (1.79M flows), CLAD reached a mean open-set AUROC of 0.9966 (vs. 0.9357 for DUAD), while its multi-class extension CLOSR "
        "reached an OpenAUC of 0.9694 (vs. 0.7985 for multi-stage baselines). The architectural constraint is that CLOSR requires a separate projection head per known class, scaling model complexity with category count.",

        "6) Comparison Within the Category\n"
        "Table 1 summarizes the nine candidate studies. Three distinct patterns emerge: (1) CICIDS2017 is the primary evaluation benchmark across supervised, unsupervised, and open-set studies; "
        "(2) reported metrics differ fundamentally between closed-set accuracy and open-set AUROC/OpenAUC, preventing direct scalar ranking; and (3) high headline accuracy from closed-set splits (e.g. [SG08]) "
        "masks complete failure under true unseen-class holdout conditions (e.g. [SG02]). Section VI traces these trade-offs to broader research gaps."
    ]

    for p_text in iva_paras:
        p = doc.add_paragraph(p_text)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15

    # Table 1: Category Comparison
    add_h2("Table 1. Machine Learning and Open-Set Papers Reviewed (Verified Source Basis)")
    t_comp = doc.add_table(rows=10, cols=5)
    t_comp.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_headers = ["Ref.", "Approach", "Dataset", "Main Verified Result", "Key Limitations Noted"]
    for c_idx, h_text in enumerate(t_headers):
        cell = t_comp.rows[0].cells[c_idx]
        cell.text = h_text
        set_cell_background(cell, "1F497D")
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_margins(cell, 60, 60, 80, 80)

    t_data = [
        ("SG01", "Survey of ML zero-day detection", "Multi-dataset survey review", "Survey of challenges; no new experiments", "No empirical benchmark; claim regarding ML consistency removed until full text verified"),
        ("SG02", "usfAD one-class anomaly framework", "10 benchmarks (NSL-KDD, UNSW-NB15, ToN-IoT, etc.)", "RF F1 0% (acc 51.88%) on NSL with 4 attacks removed; usfAD acc 99.43% (ToN-IoT)", "usfAD recall limited on UNSW (74.33%), Darknet (70.40%); noise trick limited in high dimensions"),
        ("SG03", "LSTM autoencoder vs. Isolation Forest", "Web-server logs (90,910,622 requests, unlabelled)", "RAE faster (0.099 s vs. 0.468 s per 1k flows, GPU); top-100 lists 0% overlap", "No ground-truth labels; standard accuracy/F1 not computable; year 2023 marked to confirm"),
        ("SG04", "MemAE-EIF deep unsupervised hybrid", "KDDCUP99, NSL-KDD, CIC-IDS2017", "Verified MemAE-EIF F1: KDDCUP99 0.9234, NSL-KDD 0.9172, CIC-IDS 0.7146", "Requires GPU for real-time inference; EIF memory-heavy; threshold uses known anomaly share"),
        ("SG05", "Energy-based Flow Classifier (EFC)", "CICIDS2017 (original and corrected)", "Closed-set macro F1 0.752; open-set AUROC 0.859 (OCN 0.938), AUPRC 0.993", "Bot, PortScan, Web Attack almost totally misclassified; static 95th-percentile energy threshold"),
        ("SG06", "Stacked CNNs + meta-classifiers", "CIC-IDS2017 packet payloads", "Verified 88% detection rate on unknown attack payloads", "ECOD/PReNet percentages removed; 5 held-out classes flagged pending full-text proof"),
        ("SG07", "TEX-DEC (deep clustering + XGBoost)", "CIC-IDS2017, UNSW-NB15 (covariate shift)", "AUROC: Infiltration 0.9843, SSH 0.9939, FTP 0.9950; UNSW shift 0.9939", "XGBoost requires small set of novel-class training instances; only 3 novel attacks tested"),
        ("SG08", "Supervised vs. unsupervised comparison", "CICIDS2017 (1,668,530 records)", "XGBoost acc 99.3%, F1 99.4%; One-Class SVM acc 92.1%, recall 59.2%", "Split mismatch (56/19/25% vs stated 60/20/20%); article 16/17 flagged; class holdout not described"),
        ("SG09", "CLAD / CLOSR contrastive loss", "Lycos2017 (1,789,954 flows; Heartbleed & SQLi held out)", "Open-set mean AUROC 0.9966 (DUAD 0.9357); CLOSR OpenAUC 0.9694 (0.7985)", "One projection head per class; untested on adversarial/noisy data; IEEE TNSM venue pending")
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

    # Section 7: Day 3 Verification Corrections Log
    add_h1("7. Day 3 Verification Corrections Log (51 Claims Audited)")
    doc.add_paragraph(
        "Suresh's Day 3 Verification Report audited 51 specific claims across the nine candidate papers against publisher records, "
        "arXiv pages, and accessible PDF sections. The complete audit log is documented below, showing the verified outcomes and enforced corrections:"
    )

    doc_day3 = docx.Document('source_material/original_member_submissions/Suresh_Day3_Verification_Report.docx')
    t_claims = doc_day3.tables[0]

    t_log = doc.add_table(rows=52, cols=5)
    t_log.alignment = WD_TABLE_ALIGNMENT.CENTER
    log_headers = ["Ref", "Claim Checked", "Checked Against", "Audit Result", "Enforced Action"]
    for c_idx, h_text in enumerate(log_headers):
        cell = t_log.rows[0].cells[c_idx]
        cell.text = h_text
        set_cell_background(cell, "1F497D")
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell.paragraphs[0].runs[0].font.size = Pt(9)
        set_cell_margins(cell, 50, 50, 60, 60)

    for idx, r in enumerate(t_claims.rows[1:], 1):
        ref = r.cells[0].text.strip()
        claim = r.cells[1].text.strip()
        source = r.cells[2].text.strip()
        res = r.cells[3].text.strip()
        act = r.cells[4].text.strip()
        row = t_log.rows[idx]
        row.cells[0].text = ref
        row.cells[1].text = claim
        row.cells[2].text = source
        row.cells[3].text = res
        row.cells[4].text = act
        for c_idx in range(5):
            cell = row.cells[c_idx]
            cell.paragraphs[0].runs[0].font.size = Pt(8.5)
            if idx % 2 == 1:
                set_cell_background(cell, "F9F9F9")
            set_cell_margins(cell, 30, 30, 40, 40)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section 8: Research Gaps and Future Directions
    add_h1("8. Research Gaps & Future Directions (Suresh Category)")
    doc.add_paragraph(
        "Based on the empirical findings across the nine papers, four core research gaps and corresponding future directions are established:"
    )

    t_gaps = doc.add_table(rows=5, cols=4)
    t_gaps.alignment = WD_TABLE_ALIGNMENT.CENTER
    gap_headers = ["Gap ID", "Research Gap Title", "Evidence from Suresh Category", "Proposed Research Direction"]
    for c_idx, h_text in enumerate(gap_headers):
        cell = t_gaps.rows[0].cells[c_idx]
        cell.text = h_text
        set_cell_background(cell, "1F497D")
        cell.paragraphs[0].runs[0].font.bold = True
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell.paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_margins(cell, 60, 60, 80, 80)

    for idx, (gid, gtitle, gevid, gdir) in enumerate(generate_suresh_matrix.gaps_directions_rows, 1):
        row = t_gaps.rows[idx]
        row.cells[0].text = gid
        row.cells[1].text = gtitle
        row.cells[2].text = gevid
        row.cells[3].text = gdir
        for c_idx in range(4):
            cell = row.cells[c_idx]
            cell.paragraphs[0].runs[0].font.size = Pt(9)
            if idx % 2 == 1:
                set_cell_background(cell, "F9F9F9")
            set_cell_margins(cell, 40, 40, 60, 60)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Section 9: Search Log & Candidate Tracking
    add_h1("9. Search Log Audit & Excluded Candidate Tracking")
    doc.add_paragraph(
        "A. Historical Search Log Audit:\n"
        "Suresh conducted initial candidate searches on 15 November 2026 using general web search engines. "
        "The exact search queries were recorded, but hit counts were left as 'not recorded'. "
        "To satisfy the IILM template and PRISMA selection flow requirements, reproducible searches must be run in IEEE Xplore, "
        "ACM DL, SpringerLink, Google Scholar, and arXiv with exact dates and recorded hit counts prior to final paper compilation.\n\n"
        "B. Candidate Studies Examined but Excluded:\n"
        "1. VAEMax (arXiv:2403.04193): Variational autoencoder open-set intrusion detection; excluded due to insufficient text access.\n"
        "2. RPM-Net (arXiv:2604.06638): Recurrent prototype matching; excluded due to unverified methodology and future timestamp anomaly.\n"
        "3. Anomaly Algorithm Benchmark (arXiv:2012.11354): Published in 2020; excluded because it falls outside the 2021–2026 five-year window."
    )

    # Section 10: Contribution & Reading Declaration
    add_h1("10. Contribution Statement & Honest Reading Declaration")
    doc.add_paragraph(
        "A. Actual Member Contributions (Suresh Gopal Singh, Enrolment 258100001):\n"
        "• Located and catalogued nine candidate papers in machine learning and open-set network intrusion detection.\n"
        "• Formulated the three central review questions (RQ1–RQ3) and the analytical framework explaining why unknown attacks are difficult to detect.\n"
        "• Drafted Section I (Introduction) and Section IV-A (Machine Learning and Open-Set Detection).\n"
        "• Conducted a rigorous Day 3 claims verification audit, checking 51 specific claims against publisher catalogues, arXiv pages, and accessible PDF sections.\n"
        "• Formulated category research gaps SG-G1 to SG-G4 and traced each gap to empirical evidence.\n\n"
        "B. Honest Reading Declaration Status:\n"
        "In strict adherence to academic integrity and IILM instructions, checking publisher catalogues, arXiv pages, and accessible PDF sections "
        "during the Day 3 audit does NOT constitute personal end-to-end reading of every paper. Suresh must personally open and read the methodology, "
        "results, and conclusion sections of all nine papers before signing the final IILM Annexure contribution table and defending the work in the viva examination.\n\n"
        "C. Search Log Caveat:\n"
        "Search hit counts are disclosed as unrecorded for historical web searches; formal database search logs will be populated during final survey compilation."
    )

    # Section 11: Corrected References
    add_h1("11. Corrected IEEE-Style References (Suresh Category)")
    doc.add_paragraph("The following nine references reflect all verified bibliographic corrections:")

    refs_data = [
        ("[SG01]", "Y. Guo, \"A review of machine learning-based zero-day attack detection: Challenges and future directions,\" Comput. Commun., vol. 198, pp. 175–185, Jan. 2023, doi: 10.1016/j.comcom.2022.11.001."),
        ("[SG02]", "M. A. Uddin, S. Aryal, M. R. Bouadjenek, M. Al-Hawawreh, and M. A. Talukder, \"usfAD based effective unknown attack detection focused IDS framework,\" 2024, arXiv:2403.11180. [Preprint]"),
        ("[SG03]", "T. Smolen and L. Benova, \"Comparing autoencoder and isolation forest in network anomaly detection,\" in Proc. 33rd Conf. Open Innov. Assoc. (FRUCT), 2023, doi: 10.23919/FRUCT58615.2023.10143005. [Publication year to confirm]"),
        ("[SG04]", "F. Carrera, V. Dentamaro, S. Galantucci, A. Iannacone, D. Impedovo, and G. Pirlo, \"Combining unsupervised approaches for near real-time network traffic anomaly detection,\" Appl. Sci., vol. 12, no. 3, Art. no. 1759, Feb. 2022, doi: 10.3390/app12031759."),
        ("[SG05]", "M. M. C. Souza, C. Pontes, J. Gondim, L. P. F. Garcia, L. DaSilva, and M. A. Marotta, \"A novel open set energy-based flow classifier for network intrusion detection,\" 2021, arXiv:2109.11224. [Preprint; published in Comput. Secur., vol. 157, Art. no. 104569, 2025]"),
        ("[SG06]", "Y. A. Farrukh, S. Wali, I. Khan, and N. D. Bastian, \"Detecting unknown attacks in IoT environments: An open set classifier for enhanced network intrusion detection,\" 2023, arXiv:2309.07461. [Preprint]"),
        ("[SG07]", "A. Bizzarri, C.-E. Yu, B. Jalaian, F. Riguzzi, and N. D. Bastian, \"Neuro-symbolic integration for open set recognition in network intrusion detection,\" in AIxIA 2024 -- Advances in Artificial Intelligence, Lecture Notes in Computer Science, vol. 15450, pp. 50–63. Cham, Switzerland: Springer, 2025, doi: 10.1007/978-3-031-80607-0_5."),
        ("[SG08]", "A. Z. Miran and G. S. Kadir, \"A hybrid machine learning approach for enhancing intrusion detection systems using CICIDS2017 dataset,\" Dasinya J. Eng. Inform., vol. 2, no. 2, pp. 16–25, May 2026, doi: 10.65542/djei.v2i2.49."),
        ("[SG09]", "J. Wilkie, H. Hindy, C. Michie, C. Tachtatzis, J. Irvine, and R. Atkinson, \"A novel contrastive loss for zero-day network intrusion detection,\" IEEE Trans. Netw. Serv. Manag., 2026, doi: 10.1109/TNSM.2026.3652529. [arXiv:2601.09902; venue pending final issue confirmation]")
    ]

    for tag, ref_str in refs_data:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.first_line_indent = Inches(-0.4)
        p.paragraph_format.space_after = Pt(3)
        run_tag = p.add_run(f"{tag} ")
        run_tag.bold = True
        p.add_run(ref_str)

    doc.save("research-papers/Suresh_Research_Record.docx")
    print("research-papers/Suresh_Research_Record.docx generated successfully!")

if __name__ == "__main__":
    create_document()
