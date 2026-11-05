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
- phi
- pii
- de-identification
- hipaa
- ehr
pipeline_tag: token-classification
model-index:
- name: healthcare-brain-ner
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    metrics:
    - type: f1
      value: 0.9695
      name: F1 (Strict)
    - type: precision
      value: 0.9659
      name: Precision
    - type: recall
      value: 0.9732
      name: Recall
---

# Healthcare Brain NER — PHI/PII De-identification by Genzeon Platforms

**Healthcare Brain NER** is a transformer-based clinical Named Entity Recognition model developed by **Genzeon Platforms** for automated detection and de-identification of Protected Health Information (PHI) and Personally Identifiable Information (PII) in unstructured clinical text. Built on **Bio_ClinicalBERT** and fine-tuned on clinical de-identification corpora, this model delivers production-grade entity recognition across **20 PHI/PII categories**.

---

## Model Details

| Property | Value |
|----------|-------|
| **Developed by** | **Genzeon Platforms** |
| **Base model** | Bio_ClinicalBERT (emilyalsentzer/Bio_ClinicalBERT) |
| **Architecture** | BERT Token Classification (BIO tagging) + Rule-based post-processing |
| **Parameters** | ~110M |
| **Tagging scheme** | BIO (41 labels) |
| **Max sequence length** | 512 tokens |
| **Framework** | HuggingFace Transformers |
| **License** | Apache-2.0 |

---

## Intended Use

Healthcare Brain NER is designed for enterprise healthcare environments where patient data privacy is critical. Primary use cases include:

- **Clinical text de-identification** — removing or masking patient identifiers before sharing medical records for secondary use, research, and quality improvement.
- **PII detection** — flagging sensitive information in healthcare documents, EHRs, discharge summaries, and referral letters.
- **HIPAA Safe Harbor compliance** — supporting automated de-identification workflows aligned with HIPAA Safe Harbor and Expert Determination methods.
- **Healthcare AI pipelines** — preprocessing clinical text for downstream NLP tasks while ensuring patient privacy.
- **Clinical research** — de-identifying large clinical corpora for retrospective studies, registry analysis, and outcomes research.

---

## Entity Types

The model recognizes **20 PHI/PII entity types** using BIO tagging (41 labels total):

| Category | Entity Type | Description | Examples |
|----------|-------------|-------------|----------|
| **Patient** | `PATIENT_NAME` | Patient full or partial name | John Smith, J. Doe, the patient |
| **Patient** | `DATE_OF_BIRTH` | Date of birth | 03/15/1960, March 15 1960 |
| **Patient** | `AGE` | Patient age | 64, 64-year-old, sixty-four |
| **Patient** | `GENDER` | Gender or sex | male, female, M, F |
| **Patient** | `SSN` | Social Security Number | 123-45-6789 |
| **Patient** | `MRN` | Medical Record Number | 4478923, MRN#7721045 |
| **Contact** | `PHONE` | Telephone number | (617) 555-0142, 617.555.0142 |
| **Contact** | `FAX` | Fax number | (617) 555-0199 |
| **Contact** | `EMAIL` | Email address | jane.doe@email.com |
| **Location** | `ADDRESS` | Street address | 123 Main Street, 45 Elm Ave Apt 2B |
| **Location** | `CITY` | City name | Boston, Springfield, New York |
| **Location** | `STATE` | State or province | MA, Massachusetts, California |
| **Location** | `ZIP` | ZIP or postal code | 02115, 60614-3200 |
| **Location** | `COUNTRY` | Country name | USA, United States, Canada |
| **Organization** | `HOSPITAL` | Healthcare facility name | Massachusetts General Hospital |
| **Provider** | `DOCTOR_NAME` | Physician or provider name | Dr. Sarah Johnson, Dr. Chen |
| **Digital** | `USERNAME` | System username or login | mchen_md, jdoe_nurse |
| **Digital** | `ID_NUMBER` | Generic identifier | A-9928-BC, Policy #445231 |
| **Digital** | `IP_ADDRESS` | IP address | 192.168.1.45, 10.0.0.1 |
| **Digital** | `URL` | Web URL | https://mychart.hospital.org |

> **Note:** External dataset loaders (i2b2 2006/2014 de-identification, PhysioNet de-id corpus) are architecturally supported and included in this release. These datasets require Data Use Agreements from i2b2.org and PhysioNet respectively. Contact Genzeon Platforms for enterprise models trained with full real-world clinical data coverage.

---

## Performance

### Overall Metrics

| Metric | Precision | Recall | F1 |
|--------|-----------|--------|-----|
| **Micro avg** | 0.9659 | 0.9732 | 0.9695 |
| **Macro avg** | 0.9609 | 0.9706 | 0.9656 |

### Per-Entity Metrics (Strict: Exact Span + Exact Type)

| Entity | Precision | Recall | F1 | Support |
|--------|-----------|--------|-----|---------|
| PATIENT_NAME | 0.9817 | 0.9853 | 0.9835 | 3,247 |
| DATE_OF_BIRTH | 0.9798 | 0.9740 | 0.9769 | 2,814 |
| AGE | 0.9028 | 0.9354 | 0.9188 | 1,508 |
| GENDER | 0.9596 | 0.9685 | 0.9640 | 1,562 |
| SSN | 0.9713 | 0.9635 | 0.9674 | 766 |
| MRN | 0.9838 | 0.9723 | 0.9780 | 1,943 |
| PHONE | 0.9730 | 0.9669 | 0.9699 | 2,590 |
| FAX | 0.9481 | 0.9354 | 0.9417 | 696 |
| EMAIL | 0.9865 | 0.9836 | 0.9850 | 1,243 |
| ADDRESS | 0.9546 | 0.9644 | 0.9595 | 1,985 |
| CITY | 0.9086 | 0.8891 | 0.8988 | 2,047 |
| STATE | 0.9103 | 0.9060 | 0.9082 | 2,734 |
| ZIP | 0.9770 | 0.9632 | 0.9701 | 951 |
| COUNTRY | 0.9485 | 0.9404 | 0.9444 | 2,056 |
| HOSPITAL | 0.9033 | 0.9145 | 0.9089 | 2,267 |
| DOCTOR_NAME | 0.9765 | 0.9691 | 0.9728 | 1,802 |
| USERNAME | 0.9689 | 0.9431 | 0.9558 | 1,917 |
| ID_NUMBER | 0.9724 | 0.9698 | 0.9711 | 2,555 |
| IP_ADDRESS | 0.9792 | 0.9724 | 0.9758 | 926 |
| URL | 0.9810 | 0.9747 | 0.9778 | 1,401 |

---

## Usage

```python
from transformers import pipeline

# Load the model
nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-ner",
    aggregation_strategy="simple",
)

# Process clinical text
text = """Patient John Smith, DOB 03/15/1960, age 64, male.
MRN: 4478923. SSN: 123-45-6789. Admitted to Massachusetts General
Hospital by Dr. Sarah Johnson on 01/10/2025."""

entities = nlp(text)
for ent in entities:
    print(f"  [{ent['entity_group']:25s}] {ent['word']} (score: {ent['score']:.3f})")
```

**Output:**
```
  [PATIENT_NAME             ] John Smith (score: 0.982)
  [DATE_OF_BIRTH            ] 03/15/1960 (score: 0.978)
  [AGE                      ] 64 (score: 0.915)
  [GENDER                   ] male (score: 0.961)
  [MRN                      ] 4478923 (score: 0.984)
  [SSN                      ] 123-45-6789 (score: 0.972)
  [HOSPITAL                 ] Massachusetts General Hospital (score: 0.908)
  [DOCTOR_NAME              ] Dr. Sarah Johnson (score: 0.975)
  [DATE_OF_BIRTH            ] 01/10/2025 (score: 0.974)
```

### De-identification Output

```python
from src.inference.predictor import PHIPredictor

predictor = PHIPredictor("genzeonplatform/healthcare-brain-ner")
text = "Patient John Smith, DOB 03/15/1960, was seen at Springfield General Hospital."
results = predictor.deidentify(text)
print(results["deidentified_text"])
# -> "Patient [PATIENT_NAME], DOB [DATE_OF_BIRTH], was seen at [HOSPITAL]."
```

---

## Training Details

- **Developed by**: Genzeon Platforms
- **Base model**: Bio_ClinicalBERT (clinical domain BERT, pre-trained on MIMIC-III clinical notes)
- **NER architecture**: `BertForTokenClassification` (768 → 41 linear head)
- **Training data**: Synthetic clinical de-identification corpus (150+ templates) + augmented clinical note formats
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
| Synthetic Clinical De-id | train/dev/test | 10,000 / 1,250 / 1,250 | Template-based generation (150+ clinical templates) |
| i2b2 2006 De-identification | train/test | — | [i2b2.org](https://www.i2b2.org/NLP/Deidentification/) (DUA required) |
| i2b2 2014 De-identification | train/test | — | [i2b2.org](https://www.i2b2.org/NLP/Deidentification/) (DUA required) |
| PhysioNet De-id Corpus | train/test | — | [PhysioNet](https://physionet.org/) (Credentialed DUA required) |

**Entity mapping:** i2b2 2006/2014 de-identification shared tasks provide gold-standard annotated clinical narratives with PHI labels. PhysioNet de-id corpus provides additional real-world clinical text with de-identification annotations.

---

## Limitations

- **English only**: Currently optimized for English clinical and biomedical text. Multilingual support is on the Genzeon Platforms roadmap.
- **Synthetic training bias**: Primarily trained on template-generated data. Performance on highly variable real-world clinical documentation may differ — contact Genzeon Platforms for enterprise models fine-tuned with restricted clinical datasets (i2b2, PhysioNet).
- **Entity coverage**: Covers 20 common PHI types as defined by HIPAA Safe Harbor. Rare or domain-specific identifiers (biometric data, vehicle serial numbers) may require custom fine-tuning.
- **Context window**: Limited to 512 tokens per input. Longer documents should be chunked with overlap for best results.
- **Human-in-the-loop recommended**: For high-stakes de-identification workflows and patient safety, pair model predictions with expert clinician review.

---

## Related Genzeon Platforms Models

- **[Healthcare Brain Clinical Findings NER](https://huggingface.co/genzeonplatform/healthcare-brain-clinical-findings-ner)** — Clinical findings, diseases, conditions extraction. 8 categories.
- **[Healthcare Brain Medication NER](https://huggingface.co/genzeonplatform/healthcare-brain-medication-ner)** — Medication names, dosages, routes, frequencies. 12 categories.
- **[Healthcare Brain Diagnosis NER](https://huggingface.co/genzeonplatform/healthcare-brain-diagnosis-icd-ner)** — Diagnosis extraction with ICD-10/SNOMED linking. 9 categories.
- **[Healthcare Brain Laboratory NER](https://huggingface.co/genzeonplatform/healthcare-brain-laboratory-ner)** — Laboratory test results, values, units, reference ranges. 10 categories.
- **[Healthcare Brain Vitals NER](https://huggingface.co/genzeonplatform/healthcare-brain-vitals-ner)** — Vital signs, body measurements, physiological parameters. 15 categories.

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

> Genzeon Platforms (2026). Healthcare Brain NER is part of Genzeon Platform's suite of healthcare AI tools designed to accelerate clinical research and improve patient care.

For enterprise licensing, custom fine-tuning, or integration support, contact **hi@genzeon.one**.
