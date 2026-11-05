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
- laboratory
- lab-results
- loinc
- ehr
- hipaa
datasets:
- synthetic-clinical-laboratory
- mimic-iii
- i2b2-2010
pipeline_tag: token-classification
model-index:
- name: healthcare-brain-laboratory-ner
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    metrics:
    - type: f1
      value: 0.9412
      name: F1 (Strict)
    - type: precision
      value: 0.9389
      name: Precision
    - type: recall
      value: 0.9435
      name: Recall
---

# Healthcare Brain Laboratory NER — Laboratory Results Entity Extraction by Genzeon Platform

**Healthcare Brain Laboratory NER** is a transformer-based clinical Named Entity Recognition model developed by **Genzeon Platforms** for automated extraction of laboratory test results, values, units, reference ranges, and abnormality flags from unstructured clinical text. Built on **Bio_ClinicalBERT** and fine-tuned on clinical laboratory corpora, this model delivers production-grade entity recognition across **10 laboratory result entity categories**.

---

## Model Details

| Property | Value |
|----------|-------|
| **Developed by** | **Genzeon Platforms** |
| **Base model** | Bio_ClinicalBERT (emilyalsentzer/Bio_ClinicalBERT) |
| **Architecture** | BERT Token Classification (BIO tagging) + Rule-based numeric extraction |
| **Parameters** | ~110M |
| **Tagging scheme** | BIO (21 labels) |
| **Max sequence length** | 512 tokens |
| **Framework** | HuggingFace Transformers |
| **License** | Apache-2.0 |

---

## Intended Use

Healthcare Brain Laboratory NER is designed for healthcare AI pipelines that need to extract structured laboratory result information from unstructured clinical text. Primary use cases include:

- **Lab result extraction** — extracting test names, numeric values, units, and reference ranges from lab reports, progress notes, and discharge summaries.
- **Critical value detection** — identifying critically abnormal lab values requiring immediate clinical attention.
- **Lab trending** — structuring serial lab results for temporal analysis and clinical decision support.
- **LOINC mapping support** — extracting LOINC codes for standardized lab result interoperability.
- **Clinical research** — extracting laboratory data from large clinical corpora for outcomes research and epidemiological studies.

---

## Entity Types

The model recognizes **10 laboratory result entity types** using BIO tagging (21 labels total):

| Category | Entity Type | Description | Examples |
|----------|-------------|-------------|----------|
| **Test** | `LAB_TEST_NAME` | Name of the laboratory test | hemoglobin, glucose, troponin I |
| **Value** | `LAB_VALUE` | Numeric or qualitative result | 7.2, 145, positive, trace |
| **Unit** | `LAB_UNIT` | Unit of measurement | mg/dL, g/dL, mEq/L, x10^3/uL |
| **Range** | `REFERENCE_RANGE` | Normal reference range | 12.0-17.5, < 200, 3.5-5.0 |
| **Flag** | `ABNORMALITY_FLAG` | Abnormality indicator | H, L, Critical High, Normal |
| **Specimen** | `SPECIMEN_TYPE` | Type of specimen | blood, serum, urine, CSF |
| **Date** | `LAB_DATE` | Collection date/time | 03/15/2024, this morning, hospital day 3 |
| **LOINC** | `LOINC_CODE` | LOINC identifier code | 718-7, 2345-7, 2160-0 |
| **Panel** | `TEST_PANEL` | Panel/order set name | CBC, BMP, CMP, lipid panel |
| **Status** | `LAB_STATUS` | Result status | final, preliminary, pending |

> **Note:** External dataset loaders (MIMIC-III LABEVENTS, i2b2 2010 Test entities) are architecturally supported and included in this release. These datasets require Data Use Agreements from PhysioNet and i2b2.org respectively. Contact Genzeon Platforms for enterprise models trained with full real-world clinical data coverage.

---

## Performance

### Overall Metrics

| Metric | Precision | Recall | F1 |
|--------|-----------|--------|-----|
| **Micro avg** | 0.9389 | 0.9435 | 0.9412 |
| **Macro avg** | 0.9324 | 0.9301 | 0.9311 |

### Per-Entity Metrics (Strict: Exact Span + Exact Type)

| Entity | Precision | Recall | F1 | Support |
|--------|-----------|--------|-----|---------|
| LAB_TEST_NAME | 0.9587 | 0.9621 | 0.9604 | 1,247 |
| LAB_VALUE | 0.9543 | 0.9578 | 0.9560 | 1,198 |
| LAB_STATUS | 0.9512 | 0.9549 | 0.9530 | 683 |
| LAB_UNIT | 0.9478 | 0.9523 | 0.9500 | 1,142 |
| ABNORMALITY_FLAG | 0.9456 | 0.9501 | 0.9478 | 1,089 |
| LAB_DATE | 0.9421 | 0.9387 | 0.9404 | 934 |
| REFERENCE_RANGE | 0.9334 | 0.9362 | 0.9348 | 1,076 |
| SPECIMEN_TYPE | 0.9298 | 0.9241 | 0.9269 | 812 |
| TEST_PANEL | 0.9187 | 0.9103 | 0.9145 | 426 |
| LOINC_CODE | 0.8924 | 0.8743 | 0.8833 | 289 |

---

## Usage

```python
from transformers import pipeline

# Load the model
nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-laboratory-ner",
    aggregation_strategy="simple",
)

# Process clinical text
text = \"\"\"Lab Results: Hemoglobin: 7.2 g/dL (Reference: 12.0-17.5) [Critical Low].
Specimen: blood. Status: final. CBC panel. LOINC: 718-7.\"\"\"

entities = nlp(text)
for ent in entities:
    print(f"  [{ent['entity_group']:25s}] {ent['word']} (score: {ent['score']:.3f})")
```

**Output:**
```
  [LAB_TEST_NAME            ] Hemoglobin (score: 0.950)
  [LAB_VALUE                ] 7.2 (score: 0.945)
  [LAB_UNIT                 ] g/dL (score: 0.960)
  [REFERENCE_RANGE          ] 12.0-17.5 (score: 0.940)
  [ABNORMALITY_FLAG         ] Critical Low (score: 0.955)
  [SPECIMEN_TYPE            ] blood (score: 0.935)
  [LAB_STATUS               ] final (score: 0.950)
  [TEST_PANEL               ] CBC (score: 0.940)
  [LOINC_CODE               ] 718-7 (score: 0.930)
```

### Structured Output

```python
from src.inference.predictor import LabResultPredictor

predictor = LabResultPredictor("genzeonplatform/healthcare-brain-laboratory-ner")
text = "Hemoglobin: 7.2 g/dL (ref 12.0-17.5) [Critical Low]. Specimen: blood."
results = predictor.extract_lab_results(text)
for r in results:
    print(f"  {r['test_name']}: {r['value']} {r['unit']} (flag: {r['abnormality_flag']})")
```

---

## Training Details

- **Developed by**: Genzeon Platforms
- **Base model**: Bio_ClinicalBERT (clinical domain BERT, pre-trained on MIMIC-III clinical notes)
- **NER architecture**: `BertForTokenClassification` (768 → 21 linear head)
- **Training data**: Synthetic clinical laboratory corpus (120+ templates)
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
| Synthetic Clinical Laboratory | train/dev/test | 8,000 / 1,000 / 1,000 | Template-based generation (120+ clinical templates) |
| MIMIC-III LABEVENTS | train/test | — | [PhysioNet](https://physionet.org/content/mimiciii/) (Credentialed DUA required) |
| i2b2 2010 Test Entities | train/test | — | [i2b2.org](https://www.i2b2.org/NLP/Relations/) (DUA required) |

**Entity mapping:** MIMIC-III LABEVENTS table provides structured lab data for distant supervision. i2b2 2010 Test entities provide annotated examples of lab-related mentions in clinical narratives.

---

## Limitations

- **English only**: Currently optimized for English clinical and biomedical text. Multilingual support is on the Genzeon Platforms roadmap.
- **Synthetic training bias**: Primarily trained on template-generated data. Performance on highly variable real-world clinical documentation may differ — contact Genzeon Platforms for enterprise models fine-tuned with restricted clinical datasets (MIMIC-III, i2b2).
- **Numeric precision**: Lab value extraction handles common numeric formats but may miss non-standard representations. Rule-based post-processing supplements ML predictions for numeric extraction.
- **Human-in-the-loop recommended**: For clinical decision-making and patient safety workflows, pair model predictions with expert clinician review.

---

## Related Genzeon Platforms Models

- **[Healthcare Brain NER](https://huggingface.co/genzeonplatform/healthcare-brain-ner)** — PHI/PII detection and de-identification. 20 PHI categories.
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

> Genzeon Platforms (2026). Healthcare Brain Laboratory NER is part of Genzeon Platform's suite of healthcare AI tools designed to accelerate clinical research and improve patient care.

For enterprise licensing, custom fine-tuning, or integration support, contact **hi@genzeon.one**.
