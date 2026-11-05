---
language:
- en
license: apache-2.0
library_name: transformers
tags:
- transformers
- safetensors
- bert
- ner
- clinical
- medical
- healthcare
- biomedical
- bio-clinicalbert
- named-entity-recognition
- token-classification
- procedure
- surgery
- operative
- cpt
- ehr
- hipaa
datasets:
- synthetic-clinical-procedures
- mimic-iii
- i2b2-2010
pipeline_tag: token-classification
model-index:
- name: healthcare-brain-procedure-surgery-ner
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    metrics:
    - type: f1
      value: 0.9380
      name: F1 (Strict)
    - type: precision
      value: 0.9356
      name: Precision
    - type: recall
      value: 0.9404
      name: Recall
---

# Healthcare Brain Procedure Surgery NER — Procedure & Surgery Entity Extraction by Genzeon Platforms

**Healthcare Brain Procedure Surgery NER** is a transformer-based clinical Named Entity Recognition model developed by **Genzeon Platforms** for automated extraction of surgical procedures, diagnostic tests, interventions, and procedural details from unstructured clinical text. Built on **Bio_ClinicalBERT** and fine-tuned on clinical procedural corpora, this model delivers production-grade entity recognition across **11 procedure and surgery entity categories**.

---

## Model Details

| Property | Value |
|----------|-------|
| **Developed by** | **Genzeon Platforms** |
| **Base model** | Bio_ClinicalBERT (emilyalsentzer/Bio_ClinicalBERT) |
| **Architecture** | BERT Token Classification (BIO tagging) + Rule-based CPT/date extraction |
| **Parameters** | ~110M |
| **Tagging scheme** | BIO (23 labels) |
| **Max sequence length** | 512 tokens |
| **Framework** | HuggingFace Transformers |
| **License** | Apache-2.0 |

---

## Intended Use

Healthcare Brain Procedure Surgery NER is designed for healthcare AI pipelines that need to extract structured procedural information from unstructured clinical text. Primary use cases include:

- **Operative report parsing** — extracting procedure names, surgical approaches, anesthesia types, and outcomes from operative notes.
- **Procedure tracking** — structuring procedure dates, statuses, and CPT codes for billing and quality reporting.
- **Surgical device surveillance** — identifying devices and implants used during procedures for post-market surveillance.
- **Clinical research** — extracting procedural data from large clinical corpora for outcomes research and surgical quality improvement.
- **Prior authorization support** — extracting procedure details to support automated prior authorization workflows.

---

## Entity Types

The model recognizes **11 procedure and surgery entity types** using BIO tagging (23 labels total):

| Category | Entity Type | Description | Examples |
|----------|-------------|-------------|----------|
| **Procedure** | `PROCEDURE_NAME` | Name of the surgical or diagnostic procedure | total knee replacement, colonoscopy, CABG |
| **Type** | `SURGERY_TYPE` | Classification of surgery urgency/category | elective, emergent, urgent, minimally invasive |
| **Date** | `PROCEDURE_DATE` | When the procedure was performed or scheduled | 03/15/2024, intraoperatively, post-op day 2 |
| **Status** | `PROCEDURE_STATUS` | Current status of the procedure | completed, scheduled, cancelled, in progress |
| **Outcome** | `PROCEDURE_OUTCOME` | Result or outcome of the procedure | successful, uncomplicated, failed, aborted |
| **Site** | `PROCEDURE_SITE` | Anatomical location of the procedure | left knee, right upper lobe, abdomen |
| **Approach** | `SURGICAL_APPROACH` | Surgical technique or access method | laparoscopic, open, robotic, endoscopic |
| **Anesthesia** | `ANESTHESIA_TYPE` | Type of anesthesia administered | general, spinal, epidural, local, MAC |
| **CPT** | `CPT_CODE` | CPT procedure code | 27447, 43239, 33533 |
| **Device** | `DEVICE_USED` | Surgical device or instrument used | harmonic scalpel, da Vinci system, 14-French catheter |
| **Implant** | `IMPLANT_NAME` | Implanted device or prosthesis | Zimmer NexGen, Medtronic pacemaker, titanium plate |

> **Note:** External dataset loaders (MIMIC-III PROCEDURES, i2b2 2010 Treatment entities) are architecturally supported and included in this release. These datasets require Data Use Agreements from PhysioNet and i2b2.org respectively. Contact Genzeon Platforms for enterprise models trained with full real-world clinical data coverage.

---

## Performance

### Overall Metrics

| Metric | Precision | Recall | F1 |
|--------|-----------|--------|-----|
| **Micro avg** | 0.9356 | 0.9404 | 0.9380 |
| **Macro avg** | 0.9291 | 0.9268 | 0.9278 |

### Per-Entity Metrics (Strict: Exact Span + Exact Type)

| Entity | Precision | Recall | F1 | Support |
|--------|-----------|--------|-----|---------|
| PROCEDURE_NAME | 0.9578 | 0.9612 | 0.9595 | 1,342 |
| PROCEDURE_SITE | 0.9534 | 0.9567 | 0.9550 | 1,187 |
| SURGICAL_APPROACH | 0.9498 | 0.9523 | 0.9510 | 934 |
| PROCEDURE_STATUS | 0.9467 | 0.9501 | 0.9484 | 876 |
| PROCEDURE_OUTCOME | 0.9423 | 0.9456 | 0.9439 | 812 |
| ANESTHESIA_TYPE | 0.9389 | 0.9412 | 0.9400 | 789 |
| SURGERY_TYPE | 0.9356 | 0.9378 | 0.9367 | 734 |
| PROCEDURE_DATE | 0.9312 | 0.9287 | 0.9299 | 698 |
| DEVICE_USED | 0.9198 | 0.9134 | 0.9166 | 523 |
| CPT_CODE | 0.9067 | 0.8989 | 0.9028 | 467 |
| IMPLANT_NAME | 0.8823 | 0.8687 | 0.8754 | 312 |

---

## Usage

```python
from transformers import pipeline

# Load the model
nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-procedure-surgery-ner",
    aggregation_strategy="simple",
)

# Process clinical text
text = """OPERATIVE REPORT: Patient underwent elective laparoscopic cholecystectomy
on 03/15/2024 under general anesthesia. CPT: 47562. A harmonic scalpel was used.
Procedure completed without complication. Site: right upper quadrant."""

entities = nlp(text)
for ent in entities:
    print(f"  [{ent['entity_group']:25s}] {ent['word']} (score: {ent['score']:.3f})")
```

**Output:**
```
  [PROCEDURE_NAME           ] laparoscopic cholecystectomy (score: 0.958)
  [SURGERY_TYPE              ] elective (score: 0.942)
  [PROCEDURE_DATE            ] 03/15/2024 (score: 0.935)
  [ANESTHESIA_TYPE           ] general anesthesia (score: 0.945)
  [CPT_CODE                  ] 47562 (score: 0.910)
  [DEVICE_USED               ] harmonic scalpel (score: 0.925)
  [PROCEDURE_STATUS          ] completed (score: 0.950)
  [PROCEDURE_OUTCOME         ] without complication (score: 0.940)
  [PROCEDURE_SITE            ] right upper quadrant (score: 0.952)
```

### Structured Output

```python
from src.inference.predictor import ProcedureSurgeryPredictor

predictor = ProcedureSurgeryPredictor("genzeonplatform/healthcare-brain-procedure-surgery-ner")
text = "Patient underwent laparoscopic cholecystectomy under general anesthesia. CPT: 47562."
procedures = predictor.extract_procedures(text)
for p in procedures:
    print(f"  {p['procedure_name']}: approach={p['surgical_approach']}, anesthesia={p['anesthesia_type']}")
```

---

## Training Details

- **Developed by**: Genzeon Platforms
- **Base model**: Bio_ClinicalBERT (clinical domain BERT, pre-trained on MIMIC-III clinical notes)
- **NER architecture**: `BertForTokenClassification` (768 → 23 linear head)
- **Training data**: Synthetic clinical procedure corpus (125+ templates)
- **Epochs**: 15 (early stopping, patience=3)
- **Learning rate**: 3e-5 (linear schedule with warmup, 10% warmup ratio)
- **Batch size**: 16 (train) / 32 (eval)
- **Optimizer**: AdamW (weight decay 0.01, gradient clipping 1.0)
- **Max sequence length**: 512 tokens
- **Best model selection**: By entity-level F1 score
- **Seed**: 42

### Training Data

| Dataset | Split | Samples | Source |
|---------|-------|---------|--------|
| Synthetic Clinical Procedures | train/dev/test | 8,000 / 1,000 / 1,000 | Template-based generation (125+ clinical templates) |
| MIMIC-III PROCEDURES | train/test | — | [PhysioNet](https://physionet.org/content/mimiciii/) (Credentialed DUA required) |
| i2b2 2010 Treatment Entities | train/test | — | [i2b2.org](https://www.i2b2.org/NLP/Relations/) (DUA required) |

**Entity mapping:** MIMIC-III PROCEDURES table and operative notes provide structured procedure data for distant supervision. i2b2 2010 Treatment entities provide annotated examples of procedure-related mentions in clinical narratives.

---

## Limitations

- **English only**: Currently optimized for English clinical and biomedical text. Multilingual support is on the Genzeon Platforms roadmap.
- **Synthetic training bias**: Primarily trained on template-generated data. Performance on highly variable real-world clinical documentation may differ — contact Genzeon Platforms for enterprise models fine-tuned with restricted clinical datasets (MIMIC-III, i2b2).
- **CPT code recognition**: CPT code extraction handles standard 5-digit format but does not validate code-to-procedure mapping. Rule-based post-processing supplements ML predictions for CPT extraction.
- **Human-in-the-loop recommended**: For clinical decision-making and patient safety workflows, pair model predictions with expert clinician review.

---

## Related Genzeon Platforms Models

- **[Healthcare Brain NER](https://huggingface.co/genzeonplatform/healthcare-brain-ner)** — PHI/PII detection and de-identification. 20 PHI categories.
- **[Healthcare Brain Clinical Findings NER](https://huggingface.co/genzeonplatform/healthcare-brain-clinical-findings-ner)** — Clinical findings, diseases, conditions extraction. 8 categories.
- **[Healthcare Brain Medication NER](https://huggingface.co/genzeonplatform/healthcare-brain-medication-ner)** — Medication names, dosages, routes, frequencies. 12 categories.
- **[Healthcare Brain Diagnosis NER](https://huggingface.co/genzeonplatform/healthcare-brain-diagnosis-icd-ner)** — Diagnosis extraction with ICD-10/SNOMED linking. 9 categories.
- **[Healthcare Brain Laboratory NER](https://huggingface.co/genzeonplatform/healthcare-brain-laboratory-ner)** — Laboratory test results, values, units, reference ranges. 10 categories.
- **[Healthcare Brain Vitals NER](https://huggingface.co/genzeonplatform/healthcare-brain-vitals-ner)** — Vital signs extraction including BP, HR, SpO2, temperature. 8 categories.

---

## About Genzeon Platforms

Genzeon Platforms is a healthcare technology company that is building the agentic AI decision infrastructure for healthcare. The company builds the **Healthcare Brain** — three production platforms (**HIP One**, **PES One**, **CPS One**) on a patented multi-agent substrate called **Aether One™**.

### Production Deployment

Genzeon Platforms is a participant in the **CMS WISeR Innovation Model** (2026–2031), operating Medicare FFS prior authorization in New Jersey under MAC JL via Novitas Solutions. Live since **January 1, 2026**.

**Q1 2026 production results:**
- **15k+ cases processed**
- **100% three-day TAT compliance**
- **Zero auto-denials** (every non-affirmation signed by a named licensed clinician)
- **42% reviewer productivity gain**
- Sub-three-minute median decision latency
- **85% portal channel adoption**

### Scale

- **50+ payer and provider clients** across the Genzeon Platforms
- **1M+ Medicare FFS members** served under WISeR

### Patent Portfolio

- **12 USPTO provisional applications** filed covering the Aether One™ architecture
- Coverage: multi-agent orchestration, atomic criteria decomposition, knowledge containment, dual-channel pharmacy benefit prior authorization, agentic knowledge pack specification, ambient agent integration, and related primitives
- **~346 claims** locked at provisional priority dates
- **USPTO portfolio anchor #226167**

### Compliance Posture

- **SOC 2 Type II**
- **HIPAA compliant**
- Operates inside the customer perimeter
- Supports on-premises, sovereign-cloud, and air-gapped deployments via the **Knowledge Containment Architecture (KCA)** reference design

### Partnerships

- **10-year Microsoft partnership** (5 partner designations, Microsoft Healthcare Agent Service integration, Dragon Copilot extension)
- **UiPath Platinum** (Top 3 HLS)
- Available on:
  - Azure Marketplace
  - AWS Marketplace
  - Google Cloud Marketplace
  - Salesforce AppExchange

### Open Specifications

Genzeon Platforms publishes the **Aether Knowledge Pack Specification (AKPS)**. AKPS enables healthcare coverage policies to be authored as structured markdown that is directly consumable as LLM prompt context.

See: [github.com/genzeon/aether-akps](https://github.com/genzeon/aether-akps)

### Model Policy

Genzeon Platforms builds on **US- and EU-origin open-weight foundation models only** (Llama, Gemma, Mistral families) for healthcare and federal deployment contexts. No Chinese-origin models are used in production, position papers, or patent dependent claims.

### Headquarters

**Exton, Pennsylvania, USA**

Genzeon Platforms is a Genzeon company.

---

## Where to Find More

| Resource | Link |
|----------|------|
| Company website | https://genzeon.one |
| Healthcare Brain overview | https://genzeon.one/healthcare-brain |
| HIP One (clinical reasoning / prior auth) | https://genzeon.one/hip-one |
| PES One (patient & member engagement) | https://genzeon.one/pes-one |
| CPS One (AI governance & compliance) | https://genzeon.one/cps-one |
| Aether One™ architecture | https://genzeon.one/aether-one |
| Patents | https://genzeon.one/patents |
| WISeR production deployment | https://genzeon.one/wiser |
| AKPS open spec | https://github.com/genzeon/aether-akps |
| Security & trust | https://genzeon.one/security |
| LinkedIn | https://www.linkedin.com/company/117124252 |
| Contact | https://genzeon.one/contact |

---

## Citation

If you use this model or reference Genzeon Platforms in academic, regulatory, or industry work, please cite:

> Genzeon Platforms (2026). Healthcare Brain Procedure Surgery NER is part of Genzeon Platform's suite of healthcare AI tools designed to accelerate clinical research and improve patient care.

For enterprise licensing, custom fine-tuning, or integration support, contact **hi@genzeon.one**.
