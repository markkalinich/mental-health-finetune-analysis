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
- pubmedbert
- named-entity-recognition
- token-classification
- diagnosis
- icd-10
- icd-coding
- snomed
- sapbert
- entity-linking
- disease
- ehr
- hipaa
datasets:
- synthetic-clinical-diagnosis
- mimic-iii
- ncbi-disease
- share-clef
- i2b2-2010
pipeline_tag: token-classification
model-index:
- name: healthcare-brain-diagnosis-icd-ner
  results:
  - task:
      type: token-classification
      name: Named Entity Recognition
    metrics:
    - type: f1
      value: 0.9347
      name: F1 (Strict)
    - type: precision
      value: 0.9341
      name: Precision
    - type: recall
      value: 0.9353
      name: Recall
---

# Healthcare Brain Diagnosis ICD NER — Diagnosis & ICD Coding Entity Extraction by Genzeon Platform

**Healthcare Brain Diagnosis ICD NER** is a transformer-based clinical Named Entity Recognition model developed by **Genzeon Platforms** for automated extraction of diagnoses, conditions, and support for ICD-10/SNOMED code mapping from unstructured clinical text. Built on **PubMedBERT** and fine-tuned on clinical diagnosis corpora, this model delivers production-grade entity recognition across **9 diagnosis and coding entity categories**.

The model implements a **two-stage pipeline**: (1) NER extraction of diagnosis mentions, (2) Entity linking using **SapBERT** for automated ICD-10/SNOMED code mapping.

---

## Model Details

| Property | Value |
|----------|-------|
| **Developed by** | **Genzeon Platforms** |
| **Base model** | PubMedBERT (microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) |
| **Architecture** | BERT Token Classification (BIO tagging) + SapBERT Entity Linking |
| **Parameters** | ~110M (NER) + ~110M (SapBERT linker) |
| **Tagging scheme** | BIO (19 labels) |
| **Max sequence length** | 512 tokens |
| **Framework** | HuggingFace Transformers |
| **License** | Apache-2.0 |

---

## Intended Use

Healthcare Brain Diagnosis ICD NER is designed for healthcare AI pipelines that need to extract structured diagnosis information from unstructured clinical text. Primary use cases include:

- **Diagnosis extraction** — extracting primary, secondary, differential, and comorbid diagnoses from discharge summaries, progress notes, and clinical narratives.
- **ICD-10/SNOMED coding support** — automated mapping of extracted diagnosis mentions to standardized medical codes using SapBERT entity linking.
- **Clinical documentation improvement (CDI)** — identifying diagnosis specificity gaps for coding accuracy and DRG optimization.
- **Complication detection** — identifying hospital-acquired complications and comorbidities for quality reporting.
- **Clinical research** — extracting diagnosis-related entities from large clinical corpora for epidemiological and outcomes studies.

---

## Entity Types

The model recognizes **9 diagnosis and coding entity types** using BIO tagging (19 labels total):

| Category | Entity Type | Description | Examples |
|----------|-------------|-------------|----------|
| **Primary** | `PRIMARY_DIAGNOSIS` | Principal reason for encounter | acute myocardial infarction, pneumonia |
| **Secondary** | `SECONDARY_DIAGNOSIS` | Additional diagnoses | type 2 diabetes, hypertension |
| **Differential** | `DIFFERENTIAL_DIAGNOSIS` | Diagnoses under consideration | pulmonary embolism vs pneumonia |
| **Comorbidity** | `COMORBIDITY` | Co-existing conditions | hyperlipidemia, obesity |
| **Complication** | `COMPLICATION` | Hospital-acquired or treatment complications | acute kidney injury, sepsis |
| **Chronic** | `CHRONIC_CONDITION` | Long-term conditions | COPD, coronary artery disease |
| **Acute** | `ACUTE_CONDITION` | Acute episodes or events | acute respiratory failure, DKA |
| **Status** | `DIAGNOSIS_STATUS` | Current clinical status | active, resolved, improving |
| **Temporal** | `DIAGNOSIS_DATE` | Date of diagnosis or onset | 03/15/2024, on admission, 2 weeks ago |

> **Note:** External dataset loaders (MIMIC-III, NCBI Disease, ShARe/CLEF, i2b2 2010 Problems) are architecturally supported and included in this release. These datasets require Data Use Agreements from PhysioNet, i2b2.org, and CLEF respectively. Contact Genzeon Platforms for enterprise models trained with full real-world clinical data coverage.

---

## Performance

### Overall Metrics

| Metric | Precision | Recall | F1 |
|--------|-----------|--------|-----|
| **Micro avg** | 0.9341 | 0.9353 | 0.9347 |
| **Macro avg** | 0.9286 | 0.9240 | 0.9262 |

### Per-Entity Metrics (Strict: Exact Span + Exact Type)

| Entity | Precision | Recall | F1 | Support |
|--------|-----------|--------|-----|---------|
| DIAGNOSIS_STATUS | 0.9523 | 0.9571 | 0.9547 | 903 |
| PRIMARY_DIAGNOSIS | 0.9487 | 0.9513 | 0.9500 | 757 |
| COMORBIDITY | 0.9434 | 0.9494 | 0.9464 | 908 |
| DIAGNOSIS_DATE | 0.9401 | 0.9418 | 0.9410 | 653 |
| CHRONIC_CONDITION | 0.9365 | 0.9397 | 0.9381 | 614 |
| COMPLICATION | 0.9241 | 0.9189 | 0.9215 | 407 |
| ACUTE_CONDITION | 0.9189 | 0.9073 | 0.9131 | 259 |
| SECONDARY_DIAGNOSIS | 0.9056 | 0.8898 | 0.8976 | 118 |
| DIFFERENTIAL_DIAGNOSIS | 0.8873 | 0.8609 | 0.8739 | 115 |

---

## Two-Stage Pipeline: NER + Entity Linking

### Stage 1: Named Entity Recognition
PubMedBERT-based token classification extracts diagnosis mentions from clinical text.

### Stage 2: SapBERT Entity Linking
Extracted mentions are encoded using [SapBERT](https://huggingface.co/cambridgeltl/SapBERT-from-PubMedBERT-fulltext) and matched to ICD-10/SNOMED concept embeddings via nearest-neighbor lookup.

```python
from src.inference.predictor import DiagnosisEntityLinker

linker = DiagnosisEntityLinker(
    model_dir="genzeonplatform/healthcare-brain-diagnosis-icd-ner",
    code_index_path="path/to/icd10_index.json",
)

text = "Patient admitted with acute myocardial infarction. PMH: type 2 diabetes."
results = linker.link(text, top_k=3)
for r in results:
    print(f"{r['diagnosis']} -> {r['linked_codes'][0]['code']} ({r['linked_codes'][0]['description']})")
```

---

## Usage

```python
from transformers import pipeline

# Load the model
nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-diagnosis-icd-ner",
    aggregation_strategy="simple",
)

# Process clinical text
text = \"\"\"Discharge Diagnosis: Primary: acute myocardial infarction.
Secondary: type 2 diabetes mellitus, essential hypertension.
Status: improving. Complication: acute kidney injury.\"\"\"

entities = nlp(text)
for ent in entities:
    print(f"  [{ent['entity_group']:25s}] {ent['word']} (score: {ent['score']:.3f})")
```

**Output:**
```
  [PRIMARY_DIAGNOSIS        ] acute myocardial infarction (score: 0.951)
  [SECONDARY_DIAGNOSIS      ] type 2 diabetes mellitus (score: 0.912)
  [COMORBIDITY              ] essential hypertension (score: 0.944)
  [DIAGNOSIS_STATUS         ] improving (score: 0.957)
  [COMPLICATION             ] acute kidney injury (score: 0.929)
```

### Batch Processing

```python
from transformers import pipeline

nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-diagnosis-icd-ner",
    aggregation_strategy="simple",
)

clinical_notes = [
    "Admitting Diagnosis: community-acquired pneumonia. PMH: COPD, CHF.",
    "Assessment: sepsis is worsening. Complication: acute kidney injury.",
    "CDI query: Principal Dx congestive heart failure with acute respiratory failure.",
    "Differential: pulmonary embolism vs pneumonia. Status: suspected.",
]

for note in clinical_notes:
    entities = nlp(note)
    print(f"Text: {note[:70]}...")
    for ent in entities:
        print(f"  [{ent['entity_group']:23s}] {ent['word']}")
    print()
```

### Structured Output

```python
from transformers import pipeline
import json

nlp = pipeline(
    "token-classification",
    model="genzeonplatform/healthcare-brain-diagnosis-icd-ner",
    aggregation_strategy="simple",
)

text = "Patient with congestive heart failure and acute kidney injury. Status: worsening. Date: 03/15/2024."
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
- **Base model**: PubMedBERT (domain-specialized BERT, pre-trained on PubMed abstracts and full-text articles)
- **NER architecture**: `BertForTokenClassification` (768 → 19 linear head)
- **Entity linking**: SapBERT (cambridgeltl/SapBERT-from-PubMedBERT-fulltext) for ICD-10/SNOMED mapping
- **Training data**: Synthetic clinical diagnosis corpus + NCBI Disease
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
| Synthetic Clinical Diagnosis | train/dev/test | 8,000 / 1,000 / 1,000 | Template-based generation (120+ clinical templates) |
| MIMIC-III Discharge Summaries | train/test | — | [PhysioNet](https://physionet.org/content/mimiciii/) (Credentialed DUA required) |
| NCBI Disease Corpus | train/dev/test | 793 | [NCBI](https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/) (freely available) |
| ShARe/CLEF eHealth | train/test | — | [CLEF](https://clefehealth.imag.fr/) (Organizational DUA required) |
| i2b2 2010 Problems | train/test | — | [i2b2.org](https://www.i2b2.org/NLP/Relations/) (DUA required) |

**Entity mapping:** MIMIC-III ICD codes provide weak supervision for diagnosis extraction. NCBI Disease entities map to PRIMARY_DIAGNOSIS. ShARe/CLEF disorder mentions map to diagnosis categories. i2b2 2010 problem entities are mapped to target categories using clinical context.

---

## Limitations

- **English only**: Currently optimized for English clinical and biomedical text. Multilingual support is on the Genzeon Platforms roadmap.
- **Synthetic training bias**: Primarily trained on template-generated data. Performance on highly variable real-world clinical documentation may differ — contact Genzeon Platforms for enterprise models fine-tuned with restricted clinical datasets (MIMIC, i2b2, ShARe/CLEF).
- **Diagnosis categorization**: Distinguishing PRIMARY_DIAGNOSIS from SECONDARY_DIAGNOSIS and COMORBIDITY depends on contextual cues in the clinical narrative. Ambiguous documentation may affect categorization accuracy.
- **Entity linking coverage**: SapBERT-based ICD-10/SNOMED linking requires a pre-built code index. Coverage depends on the completeness of the index.
- **Temporal expressions**: DIAGNOSIS_DATE extraction handles common clinical date formats but may miss non-standard temporal references.
- **Human-in-the-loop recommended**: For clinical decision-making, coding compliance, and patient safety workflows, pair model predictions with expert clinician or coder review.

---

## Related Genzeon Platforms Models

- **[Healthcare Brain NER](https://huggingface.co/genzeonplatform/healthcare-brain-ner)** — PHI/PII detection and de-identification. 20 PHI categories.
- **[Healthcare Brain Clinical Findings NER](https://huggingface.co/genzeonplatform/healthcare-brain-clinical-findings-ner)** — Clinical findings, diseases, conditions extraction. 8 categories.
- **[Healthcare Brain Medication NER](https://huggingface.co/genzeonplatform/healthcare-brain-medication-ner)** — Medication names, dosages, routes, frequencies. 12 categories.
- **[Healthcare Brain Diagnosis NER](https://huggingface.co/genzeonplatform/healthcare-brain-diagnosis-icd-ner)** — Diagnosis extraction with ICD-10/SNOMED linking. 9 categories.
- **[Healthcare Brain Laboratory NER](https://huggingface.co/genzeonplatform/healthcare-brain-laboratory-ner)** — Laboratory test results, values, units, reference ranges. 10 categories.
- **[Healthcare Brain Vitals NER](https://huggingface.co/genzeonplatform/healthcare-brain-vitals-ner)** — Vital signs, body measurements, physiological parameters. 15 categories.

- **[Healthcare Brain Clinical Findings NER](https://huggingface.co/genzeonplatform/healthcare-brain-clinical-findings-ner)** — Transformer-based clinical NER model for extraction of clinical findings, diseases, conditions, anatomical locations, and clinical modifiers from clinical text. 8 clinical finding categories, F1: 0.6209 (strict) / 0.968 (relaxed).

- **[Healthcare Brain Medication NER](https://huggingface.co/genzeonplatform/healthcare-brain-medication-ner)** — Transformer-based clinical NER model for extraction of medication names, dosages, routes, frequencies, and administration details from clinical text. 12 medication categories, F1: 0.9272.

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

> Genzeon Platforms (2026). Healthcare Brain Diagnosis ICD NER is part of Genzeon Platform's suite of healthcare AI tools designed to accelerate clinical research and improve patient care.

For enterprise licensing, custom fine-tuning, or integration support, contact **hi@genzeon.one**.
