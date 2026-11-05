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
- bio-clinical-bert
- named-entity-recognition
- token-classification
- medication
- drug
- pharmacy
- ehr
- hipaa
- rxnorm
- ndc
datasets:
- synthetic-clinical-medication
- n2c2-2018
- i2b2-2009
- bc5cdr
pipeline_tag: token-classification
model-index:
- name: healthcare-brain-medication-ner
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    metrics:
    - type: f1
      value: 0.9272
      name: F1 (Strict)
    - type: precision
      value: 0.9271
      name: Precision
    - type: recall
      value: 0.9274
      name: Recall
---

# Healthcare Brain Medication NER — Medication & Drug Entity Extraction by Genzeon Platform

**Healthcare Brain Medication NER** is a transformer-based clinical Named Entity Recognition model developed by **Genzeon Platforms** for automated extraction of medication names, dosages, routes, frequencies, and administration details from unstructured clinical text. Built on **Bio_ClinicalBERT** and fine-tuned on clinical medication corpora, this model delivers production-grade entity recognition across **12 medication and drug entity categories**.

---

## Model Details

| Property | Value |
|----------|-------|
| **Developed by** | **Genzeon Platforms** |
| **Base model** | Bio_ClinicalBERT |
| **Architecture** | BERT Token Classification (BIO tagging) |
| **Parameters** | ~110M |
| **Tagging scheme** | BIO (25 labels) |
| **Max sequence length** | 512 tokens |
| **Framework** | HuggingFace Transformers |
| **License** | Apache-2.0 |

---

## Intended Use

Healthcare Brain Medication NER is designed for healthcare AI pipelines that need to extract structured medication information from unstructured clinical text. Primary use cases include:

- **Medication extraction** — extracting drug names, dosages, routes, and frequencies from EHRs, discharge summaries, progress notes, and clinical narratives.
- **Prescription parsing** — automated order entry and clinical decision support from free-text medication orders.
- **Adverse drug event detection** — identifying medication-related adverse reactions for pharmacovigilance and safety surveillance workflows.
- **Medication reconciliation** — structured extraction across care transitions, enabling automated reconciliation between inpatient and outpatient regimens.
- **Clinical research** — extracting medication-related entities from large corpora of clinical narratives for retrospective drug utilization studies.

---

## Entity Types

The model recognizes **12 medication and drug entity types** using BIO tagging (25 labels total):

| Category | Entity Type | Description | Examples |
|----------|-------------|-------------|----------|
| **Drug** | `DRUG_NAME` | Brand or generic medication name | Metformin, Lipitor, amoxicillin |
| **Dosing** | `DOSAGE` | Amount to administer | 1 tablet, 2 puffs, 10 mL |
| **Potency** | `STRENGTH` | Drug concentration/potency | 500 mg, 10 mg/5 mL, 0.5% |
| **Administration** | `ROUTE` | Route of administration | oral, IV, PO, topical, inhaled |
| **Schedule** | `FREQUENCY` | Dosing schedule | BID, once daily, q6h, PRN |
| **Temporal** | `DURATION` | Length of therapy | for 7 days, x 2 weeks, indefinitely |
| **Formulation** | `FORM` | Physical dosage form | tablet, capsule, injection, cream |
| **Status** | `DRUG_STATUS` | Current medication status | active, discontinued, on hold |
| **Indication** | `REASON` | Clinical indication for use | for hypertension, for pain |
| **Safety** | `ADVERSE_REACTION` | Side effects or adverse drug events | rash, nausea, anaphylaxis |
| **Identifier** | `NDC_CODE` | National Drug Code | 00093-7214-01 |
| **Identifier** | `RxNorm_CODE` | RxNorm concept identifier | 197361 |

> **Note:** External dataset loaders (n2c2 2018 Track 2, i2b2 2009 Medication) are architecturally supported and included in this release. These datasets require Data Use Agreements from Harvard DBMI and i2b2.org respectively. Contact Genzeon Platforms for enterprise models trained with full real-world clinical data coverage.

---

## Performance

### Overall Metrics

| Metric | Precision | Recall | F1 |
|--------|-----------|--------|-----|
| **Micro avg** | 0.9271 | 0.9274 | 0.9272 |
| **Macro avg** | 0.9186 | 0.9076 | 0.9130 |

### Per-Entity Metrics (Strict: Exact Span + Exact Type)

| Entity | Precision | Recall | F1 | Support |
|--------|-----------|--------|-----|---------|
| DRUG_NAME | 0.9487 | 0.9610 | 0.9548 | 1,000 |
| STRENGTH | 0.9426 | 0.9513 | 0.9469 | 986 |
| FORM | 0.9398 | 0.9483 | 0.9440 | 831 |
| ROUTE | 0.9341 | 0.9406 | 0.9373 | 909 |
| FREQUENCY | 0.9274 | 0.9357 | 0.9315 | 887 |
| DOSAGE | 0.9312 | 0.9165 | 0.9238 | 767 |
| NDC_CODE | 0.9215 | 0.8967 | 0.9089 | 242 |
| DURATION | 0.9080 | 0.8908 | 0.8993 | 348 |
| RxNorm_CODE | 0.9185 | 0.8741 | 0.8957 | 135 |
| DRUG_STATUS | 0.8945 | 0.8818 | 0.8881 | 330 |
| REASON | 0.8853 | 0.8654 | 0.8752 | 416 |
| ADVERSE_REACTION | 0.8714 | 0.8291 | 0.8497 | 199 |

---

## Usage

```python
from transformers import pipeline

# Load the model
nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-medication-ner",
    aggregation_strategy="simple",
)

# Process clinical text
text = """Discharge medications: Continue Metformin 500 mg tablet by mouth twice daily
for diabetes. New: Amoxicillin 500 mg capsule PO TID for 7 days for sinusitis.
Discontinue Lisinopril due to persistent cough."""

entities = nlp(text)
for ent in entities:
    print(f"  [{ent['entity_group']:20s}] {ent['word']} (score: {ent['score']:.3f})")
```

**Output:**
```
  [DRUG_NAME           ] Metformin (score: 0.987)
  [STRENGTH            ] 500 mg (score: 0.993)
  [FORM                ] tablet (score: 0.991)
  [ROUTE               ] by mouth (score: 0.989)
  [FREQUENCY           ] twice daily (score: 0.994)
  [REASON              ] for diabetes (score: 0.986)
  [DRUG_NAME           ] Amoxicillin (score: 0.992)
  [STRENGTH            ] 500 mg (score: 0.995)
  [FORM                ] capsule (score: 0.988)
  [ROUTE               ] PO (score: 0.979)
  [FREQUENCY           ] TID (score: 0.991)
  [DURATION            ] for 7 days (score: 0.987)
  [REASON              ] for sinusitis (score: 0.983)
  [DRUG_NAME           ] Lisinopril (score: 0.990)
  [ADVERSE_REACTION    ] persistent cough (score: 0.871)
```

### Batch Processing

```python
from transformers import pipeline

nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-medication-ner",
    aggregation_strategy="simple",
)

clinical_notes = [
    "Start Atorvastatin 40 mg tablet PO at bedtime for high cholesterol.",
    "ADR: Patient developed rash after Penicillin IV. Drug discontinued.",
    "Albuterol 90 mcg inhaler 2 puffs inhaled Q4-6H PRN for bronchospasm.",
    "MAR: Administered Vancomycin 1 g IV Q12H. NDC: 00409-6509-01.",
]

for note in clinical_notes:
    entities = nlp(note)
    print(f"Text: {note[:70]}...")
    for ent in entities:
        print(f"  [{ent['entity_group']:18s}] {ent['word']}")
    print()
```

### Structured Output

```python
from transformers import pipeline
import json

nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-medication-ner",
    aggregation_strategy="simple",
)

text = "Rx: Omeprazole 20 mg capsule PO once daily for GERD x 30 days. NDC: 00186-5020-31."
entities = nlp(text)

# Structured extraction
structured = [
    {
        "text": ent["word"],
        "type": ent["entity_group"],
        "score": round(ent["score"], 4),
        "start": ent["start"],
        "end": ent["end"],
    }
    for ent in entities
]

print(json.dumps(structured, indent=2))
```

---

## Training Details

- **Developed by**: Genzeon Platforms
- **Base model**: Bio_ClinicalBERT (domain-specialized BERT for clinical text, pre-trained on PubMed + MIMIC-III)
- **NER architecture**: `BertForTokenClassification` (768 → 25 linear head)
- **Training data**: Synthetic clinical medication corpus + BC5CDR-Chemical
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
| Synthetic Clinical Medication | train/dev/test | 8,000 / 1,000 / 1,000 | Template-based generation (110+ clinical templates) |
| n2c2 2018 Track 2 | train/test | — | [Harvard DBMI](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/) (DUA required) |
| i2b2 2009 Medication | train/test | — | [i2b2.org](https://www.i2b2.org/NLP/Medication/) (DUA required) |
| BC5CDR-Chemical | train/dev/test | 1,500 | [BioCreative V CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) |

**Entity mapping:** n2c2 2018 entity types are mapped to target categories (Drug→DRUG_NAME, Strength→STRENGTH, Dosage→DOSAGE, Route→ROUTE, Frequency→FREQUENCY, Duration→DURATION, Form→FORM, ADE→ADVERSE_REACTION, Reason→REASON). BC5CDR Chemical entities map to DRUG_NAME.

---

## Limitations

- **English only**: Currently optimized for English clinical and biomedical text. Multilingual support is on the Genzeon Platforms roadmap.
- **Synthetic training bias**: Primarily trained on template-generated data. Performance on highly variable real-world clinical documentation may differ — contact Genzeon Platforms for enterprise models fine-tuned with restricted clinical datasets (n2c2, i2b2).
- **Multi-word drug names**: Compound drug names (e.g., "amoxicillin/clavulanate", "Advair Diskus") may have partial boundary detection depending on WordPiece tokenization.
- **Contextual ambiguity**: REASON vs. ADVERSE_REACTION can be contextually ambiguous (e.g., "nausea" as an indication for antiemetics vs. a side effect of another drug). Context window and surrounding entities improve disambiguation.
- **Code entities**: NDC_CODE and RxNorm_CODE require specific formatting context (typically preceded by "NDC:" or "RxNorm:"); isolated numeric strings may not be recognized.
- **Human-in-the-loop recommended**: For clinical decision-making and patient safety workflows, pair model predictions with expert pharmacist or clinician review.

---

## Related Genzeon Platforms Models

- **[Healthcare Brain NER](https://huggingface.co/genzeonplatform/healthcare-brain-ner)** — PHI/PII detection and de-identification. 20 PHI categories.
- **[Healthcare Brain Clinical Findings NER](https://huggingface.co/genzeonplatform/healthcare-brain-clinical-findings-ner)** — Clinical findings, diseases, conditions extraction. 8 categories.
- **[Healthcare Brain Medication NER](https://huggingface.co/genzeonplatform/healthcare-brain-medication-ner)** — Medication names, dosages, routes, frequencies. 12 categories.
- **[Healthcare Brain Diagnosis NER](https://huggingface.co/genzeonplatform/healthcare-brain-diagnosis-icd-ner)** — Diagnosis extraction with ICD-10/SNOMED linking. 9 categories.
- **[Healthcare Brain Laboratory NER](https://huggingface.co/genzeonplatform/healthcare-brain-laboratory-ner)** — Laboratory test results, values, units, reference ranges. 10 categories.
- **[Healthcare Brain Vitals NER](https://huggingface.co/genzeonplatform/healthcare-brain-vitals-ner)** — Vital signs, body measurements, physiological parameters. 15 categories.

- **[Healthcare Brain Clinical Findings NER](https://huggingface.co/genzeonplatform/healthcare-brain-clinical-findings-ner)** — Transformer-based clinical NER model for extraction of clinical findings, diseases, conditions, anatomical locations, and clinical modifiers from clinical text. 8 clinical finding categories, F1: 0.6209 (strict) / 0.968 (relaxed).

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

> Genzeon Platforms (2026). Healthcare Brain Medication NER is part of Genzeon Platform's suite of healthcare AI tools designed to accelerate clinical research and improve patient care.

For enterprise licensing, custom fine-tuning, or integration support, contact **hi@genzeon.one**.
