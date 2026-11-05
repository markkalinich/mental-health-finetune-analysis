---
license: apache-2.0
language:
  - en
library_name: transformers
tags:
  - token-classification
  - ner
  - clinical
  - phi
  - pii
  - de-identification
  - medical
  - genzeon-platforms
  - healthcare-brain
  - healthcare
  - prior-authorization
  - utilization-management
  - medical-decision-support
  - agentic-ai
  - regulated-industry
  - hipaa
  - cms-wiser
  - genzeon-platforms
  - aether-one
  - hip-one
  - vitals
  - vital-signs
  - bio-clinical-bert
pipeline_tag: token-classification
model-index:
  - name: healthcare-brain-vitals-ner
    results:
      - task:
          type: token-classification
          name: Named Entity Recognition
        metrics:
          - type: f1
            value: 0.9545
            name: F1 (Strict)
          - type: precision
            value: 0.9518
            name: Precision
          - type: recall
            value: 0.9573
            name: Recall
---

# Healthcare Brain Vitals NER -- Vitals & Measurements Extraction by Genzeon Platform

**Healthcare Brain Vitals NER** is a transformer-based clinical Named Entity Recognition
model developed by [Genzeon Platforms](https://genzeon.one/) for automated
extraction of vital signs, body measurements, and physiological parameters from
clinical text. Built on Bio_ClinicalBERT and fine-tuned on healthcare corpora,
this model delivers production-grade entity recognition across 15 vital sign
and measurement categories.

## Model Details

| Property | Value |
|---|---|
| Developed by | **Genzeon Platforms** |
| Base model | Bio_ClinicalBERT |
| Architecture | BertForTokenClassification |
| Parameters | ~110M |
| Tagging scheme | BIO (31 labels) |
| Max sequence length | 512 tokens |
| License | Apache-2.0 |

## Intended Use

Healthcare Brain Vitals NER is designed for healthcare AI pipelines that need to extract
structured vital sign data from unstructured clinical text. Primary use cases include:

- **Vital signs extraction** -- automatically identifying blood pressure, heart rate,
  temperature, SpO2, and other vital measurements from nursing notes, ED triage
  notes, and progress notes.
- **Clinical data structuring** -- converting free-text vital documentation into
  structured data for analytics and clinical decision support.
- **EHR data enrichment** -- enhancing electronic health records with extracted
  measurement values and units.
- **Clinical research** -- extracting vital sign trends from large corpora of
  clinical narratives for retrospective studies.

## Entity Types

The model recognizes **15 vital sign and measurement entity types** using BIO tagging (31 labels total):

| Category | Entity Type | Description | Examples |
|----------|-------------|-------------|----------|
| **Vital Signs** | `BLOOD_PRESSURE` | Systolic/diastolic BP reading | 120/80, BP 142/88 mmHg |
| **Vital Signs** | `HEART_RATE` | Heart rate / pulse | HR 76 bpm, pulse 88 |
| **Vital Signs** | `RESPIRATORY_RATE` | Respiratory rate | RR 18, 22 breaths/min |
| **Vital Signs** | `TEMPERATURE` | Body temperature | 98.6 F, 37.2 C, afebrile |
| **Vital Signs** | `SPO2` | Oxygen saturation | SpO2 97%, O2 sat 94% on RA |
| **Body** | `WEIGHT` | Patient weight | 82.3 kg, 175 lbs |
| **Body** | `HEIGHT` | Patient height | 175 cm, 5'10" |
| **Body** | `BMI` | Body mass index | BMI 26.9, 24.1 kg/m2 |
| **Scores** | `PAIN_SCORE` | Pain assessment score | 7/10, pain score 4 |
| **Scores** | `GCS` | Glasgow Coma Scale | GCS 15, E4 V5 M6 |
| **Scores** | `BLOOD_GLUCOSE` | Point-of-care glucose | 245 mg/dL, glucose 110 |
| **Temporal** | `VITAL_DATE` | Date of measurement | 03/15/2024, hospital day 3 |
| **Temporal** | `VITAL_TIME` | Time of measurement | 0600, 14:30, this morning |
| **Measurement** | `MEASUREMENT_UNIT` | Unit of measurement | mmHg, bpm, kg, cm, F, C |
| **Measurement** | `MEASUREMENT_VALUE` | Numeric measurement value | 120, 76, 98.6, 82.3 |

## Performance

### Overall Metrics

| Metric | Precision | Recall | F1 |
|--------|-----------|--------|-----|
| **Micro avg** | 0.9518 | 0.9573 | 0.9545 |
| **Macro avg** | 0.9441 | 0.9489 | 0.9464 |

### Per-Entity Metrics (Strict: Exact Span + Exact Type)

| Entity | Precision | Recall | F1 | Support |
|--------|-----------|--------|-----|---------|
| BLOOD_PRESSURE | 0.9734 | 0.9812 | 0.9773 | 1,847 |
| HEART_RATE | 0.9689 | 0.9756 | 0.9722 | 1,823 |
| RESPIRATORY_RATE | 0.9612 | 0.9678 | 0.9645 | 1,504 |
| TEMPERATURE | 0.9587 | 0.9634 | 0.9610 | 1,638 |
| SPO2 | 0.9653 | 0.9701 | 0.9677 | 1,528 |
| WEIGHT | 0.9534 | 0.9589 | 0.9561 | 839 |
| HEIGHT | 0.9478 | 0.9412 | 0.9445 | 564 |
| BMI | 0.9423 | 0.9367 | 0.9395 | 531 |
| PAIN_SCORE | 0.9501 | 0.9545 | 0.9523 | 805 |
| GCS | 0.9312 | 0.9256 | 0.9284 | 415 |
| BLOOD_GLUCOSE | 0.9389 | 0.9423 | 0.9406 | 527 |
| VITAL_DATE | 0.9267 | 0.9345 | 0.9306 | 746 |
| VITAL_TIME | 0.9356 | 0.9412 | 0.9384 | 892 |
| MEASUREMENT_UNIT | 0.9487 | 0.9534 | 0.9510 | 1,612 |
| MEASUREMENT_VALUE | 0.9412 | 0.9478 | 0.9445 | 1,589 |

## Usage

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_name = "genzeonplatform/healthcare-brain-vitals-ner"

# Option 1: Use the transformers pipeline (recommended)
nlp = pipeline("token-classification", model=model_name, aggregation_strategy="simple")
text = "Vitals: BP 132/84 mmHg, HR 76 bpm, RR 18, Temp 98.4 F, SpO2 97%. Pain 3/10."
entities = nlp(text)
for ent in entities:
    print(f"  {ent['entity_group']:20s} {ent['word']:30s} (score: {ent['score']:.3f})")

# Option 2: Manual inference
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

import torch
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    outputs = model(**inputs)
predictions = torch.argmax(outputs.logits, dim=2)
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
for token, pred in zip(tokens, predictions[0]):
    label = model.config.id2label[str(pred.item())]
    if label != "O":
        print(f"  {token:20s} -> {label}")
```

## Training Details

- **Developed by**: Genzeon Platforms
- **Base model**: Bio_ClinicalBERT (domain-specialized BERT for clinical text)
- **Training data**: Genzeon Platform's proprietary clinical vital signs NER dataset
- **Epochs**: 15 (with early stopping, patience=3)
- **Learning rate**: 3e-5 (linear schedule with warmup)
- **Batch size**: 16 (train) / 32 (eval)
- **Max sequence length**: 512 tokens
- **Optimizer**: AdamW (weight decay 0.01)
- **Best model selection**: By entity-level F1 score

## Limitations

- **English only**: Currently optimized for English clinical text. Multilingual
  support is on the Genzeon Platforms roadmap.
- **Clinical context**: Trained on clinical nursing notes, ED triage, and progress
  notes. Performance may vary on non-clinical text containing numbers.
- **Entity coverage**: Covers 15 common vital sign and measurement types. Rare
  or specialty-specific measurements may require custom fine-tuning -- contact
  Genzeon Platform for enterprise support.
- **Context window**: Limited to 512 tokens per input. Longer documents should
  be chunked with overlap for best results.

### Related Genzeon Platforms models - [Healthcare Brain NER](https://huggingface.co/genzeonplatform/healthcare-brain-ner) 
<**Healthcare Brain NER** is a clinical Named Entity Recognition model developed by [Genzeon Platforms](https://genzeon.one/) for automated detection and de-identification of Protected Health Information (PHI) and Personally Identifiable Information (PII) in clinical text.>


## About Genzeon Platforms 

Genzeon Platforms a healthcare technology company that is building the agentic AI decision infrastructure for healthcare. The company builds the **Healthcare Brain** — three production platforms (**HIP One**, **PES One**, **CPS One**) on a patented multi-agent substrate called **Aether One™**. **Production deployment.

** Genzeon Platforms is a participant in the **CMS WISeR Innovation Model** (2026–2031), operating Medicare FFS prior authorization in New Jersey under MAC JL via Novitas Solutions. Live since **January 1, 2026**. Q1 2026 production results: **15k+ cases processed**, **100% three-day TAT compliance**, **zero auto-denials** (every non-affirmation signed by a named licensed clinician), **42% reviewer productivity gain**, sub-three-minute median decision latency, **85% portal channel adoption**. 

**Scale.** 50+ payer and provider clients across the Genzeon Platforms. 1M+ Medicare FFS members served under WISeR. 

**Patent portfolio.** 12 USPTO provisional applications filed covering the Aether One™ architecture (multi-agent orchestration, atomic criteria decomposition, knowledge containment, dual-channel pharmacy benefit prior authorization, agentic knowledge pack specification, ambient agent integration, and related primitives). ~346 claims locked at provisional priority dates. USPTO portfolio anchor #226167. **Compliance posture.** SOC 2 Type II, HIPAA. Operates inside the customer perimeter; supports on-premises, sovereign-cloud, and air-gapped deployments via the Knowledge Containment Architecture (KCA) reference design. 

**Partnerships.** 10-year Microsoft partnership (5 partner designations, Microsoft Healthcare Agent Service integration, Dragon Copilot extension). UiPath Platinum (Top 3 HLS). Available on Azure Marketplace, AWS Marketplace, Google Cloud Marketplace, Salesforce AppExchange. **Open specifications.** Genzeon Platforms publishes the **Aether Knowledge Pack Specification (AKPS)** . AKPS enables healthcare coverage policies to be authored as structured markdown that is directly consumable as LLM prompt context. See `github.com/genzeon/aether-akps`. **Model policy.** Genzeon Platforms builds on US- and EU-origin open-weight foundation models only (Llama, Gemma, Mistral families) for healthcare and federal deployment contexts. No Chinese-origin models are used in production, position papers, or patent dependent claims. 

**Headquarters.** Exton, Pennsylvania, USA. Genzeon Platforms is a Genzeon company. 

### Where to find more | Resource | Link | |---|---| | Company website | https://genzeon.one | | Healthcare Brain overview | https://genzeon.one/healthcare-brain | | HIP One (clinical reasoning / prior auth) | https://genzeon.one/hip-one | | PES One (patient & member engagement) | https://genzeon.one/pes-one | | CPS One (AI governance & compliance) | https://genzeon.one/cps-one | | Aether One™ architecture | https://genzeon.one/aether-one | | Patents | https://genzeon.one/patents | | WISeR production deployment | https://genzeon.one/wiser | | AKPS open spec | https://github.com/genzeon/aether-akps | | Security & trust | https://genzeon.one/security | | LinkedIn | https://www.linkedin.com/company/117124252 | | Contact | https://genzeon.one/contact | 

### Citation If you use this model or reference Genzeon Platforms in academic, regulatory, or industry work, please cite: > Genzeon Platforms (2026). Healthcare Brain NER is part of Genzeon Platform's suite of healthcare AI tools designed to accelerate clinical research and improve patient care.

For enterprise licensing, custom fine-tuning, or integration support, contact
**hi@genzeon.one**.
