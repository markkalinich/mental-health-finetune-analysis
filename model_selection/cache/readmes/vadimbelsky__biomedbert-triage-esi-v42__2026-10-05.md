---
license: apache-2.0
language:
  - en
library_name: transformers
tags:
  - medical-llm
  - clinical
  - healthcare
  - medicine
  - medical-ai
  - clinical-decision-support
  - medical
  - triage
  - esi
  - emergency-medicine
  - clinical-nlp
  - biomedbert
  - bert
  - multi-label-classification
pipeline_tag: text-classification
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
metrics:
  - accuracy
  - f1
  - recall
model-index:
  - name: BiomedBERT-Triage-ESI-v42
    results:
      - task:
          type: text-classification
          name: ESI Triage Classification
        metrics:
          - name: Accuracy (algorithm-correct)
            type: accuracy
            value: 0.917
          - name: Accuracy (expert-labeled)
            type: accuracy
            value: 0.861
          - name: High-risk recall (ESI 1-2)
            type: recall
            value: 0.920
          - name: Within-1 accuracy
            type: accuracy
            value: 0.972
          - name: Under-triage rate
            type: accuracy
            value: 0.083
---

# BiomedBERT-Triage-ESI v42

A BiomedBERT-based clinical field extractor for Emergency Severity Index (ESI) triage classification. The model extracts structured clinical fields from free-text triage notes, which are then processed by a deterministic ESI v5 algorithm to produce ESI levels 1-5.

## Key Results

| Metric | Value |
|--------|-------|
| **Algorithm-correct accuracy** | **91.7%** (33/36) |
| Expert-labeled accuracy | 86.1% (31/36) |
| Within-1 accuracy | 97.2% (35/36) |
| High-risk recall (ESI 1-2) | 92.0% |
| Under-triage rate | 8.3% |
| Over-triage rate | 5.6% |
| Inference speed | 21ms/sample (MPS) |

> **91.7% algorithm-correct**: 2 of 5 "errors" are cases where the model correctly follows ESI algorithm rules, but the expert applied clinical judgment that overrides the algorithm (CHF-related chest pain scored ESI 3 by expert vs ESI 2 by algorithm; isolated pelvic pain with stable vitals scored ESI 3 by expert vs ESI 2 by algorithm).

### Per-ESI Performance

| ESI Level | Accuracy | Cases | Description |
|-----------|----------|-------|-------------|
| ESI 1 (Resuscitation) | **92.9%** | 13/14 | Cardiac arrest, respiratory failure, septic shock |
| ESI 2 (Emergent) | **81.8%** | 9/11 | Chest pain, stroke, active seizure, sepsis |
| ESI 3 (Urgent) | 60.0% | 3/5 | 2+ resources: labs, imaging, IV |
| ESI 4 (Less urgent) | **100%** | 4/4 | 1 resource: X-ray or simple procedure |
| ESI 5 (Non-urgent) | **100%** | 2/2 | 0 resources: med refill, suture removal |

## Architecture

```
Triage Note (free text)
    │
    ▼
┌─────────────────────────────────┐
│  BiomedBERT Encoder (110M)      │
│  [CLS] token → hidden state     │
└─────────┬───────────────────────┘
          │
    ┌─────┼─────┬─────┬─────┬─────┐
    ▼     ▼     ▼     ▼     ▼     ▼
 Symptom Flag  Pain  Arrival Resource
 Head   Head  Head   Head   Head
 (50)   (5)   (1)    (5)   (11)
    │     │     │     │     │
    ▼     ▼     ▼     ▼     ▼
┌─────────────────────────────────┐
│  Deterministic ESI v5 Engine    │
│  Step A → B1 → B2 → B3 → C → D │
│  (~250 lines pure Python)       │
└─────────────┬───────────────────┘
              ▼
         ESI 1-5 + reasoning
```

The model **never predicts ESI directly**. It extracts structured fields, and a transparent, auditable ESI algorithm makes the final decision. Every prediction comes with step-by-step reasoning.

### Extraction Heads

| Head | Output | Val Accuracy |
|------|--------|-------------|
| **Symptom** | 50 binary labels (chest_pain, fracture, sepsis_signs, ...) | 99.7% |
| **Resource** | 11 binary labels (labs, ecg, xray, iv_fluids, ...) | 99.9% |
| **Flag** | 5 binary flags (altered_mentation, needs_immediate_airway, ...) | — |
| **Pain** | Regression 0-10 | MAE 0.09 |
| **Arrival** | 5-class (ambulance, walk-in, helicopter, wheelchair, unknown) | — |

### ESI Algorithm (Deterministic)

The ESI v5 algorithm is implemented as ~250 lines of pure Python with no text extraction:

- **Step A**: Immediate lifesaving intervention? (airway, IV resuscitation, GCS ≤ 8, SBP < 80, SpO2 < 85) → **ESI 1**
- **Step B1**: High-risk symptoms? (chest_pain, sepsis_signs, stroke, seizure, GI bleed, ...) → **ESI 2**
- **Step B2**: Altered mental status? → **ESI 2**
- **Step B3**: Severe pain/distress? (pain 10/10, systemic pain ≥ 9) → **ESI 2**
- **Step C**: Resource counting (2+ → ESI 3, 1 → ESI 4, 0 → ESI 5)
- **Step D**: Vital sign danger zones → uptriage

## Training

### Dataset

113,801 records from multiple sources:

| Source | Records | Format |
|--------|---------|--------|
| MIMIC-IV-ED structured (gold ESI) | 96,099 | Compact |
| MIETIC narrative (from MIMIC-IV-ED) | 9,629 | Narrative |
| MIMIC-IV-ED generated narrative | 5,000 | Narrative |
| Targeted augmentation (critical care) | 3,073 | Narrative |

**Key insight**: Training data must include both compact and narrative formats. A model trained only on compact text ("CC: Chest pain | HR 110 BP 130/80...") fails on narrative clinical notes ("A 63-year-old male presents to the ED via ambulance with palpitations and dizziness...") — the real-world format.

### Training Configuration

- **Base model**: `microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext`
- **Epochs**: 5
- **Batch size**: 32
- **Learning rate**: 2e-5 (with linear warmup)
- **Max sequence length**: 256 tokens
- **Hardware**: NVIDIA DGX Spark (GB10 GPU)
- **Training time**: ~2.5 hours (114K records)

### Training Approach

1. **Multi-head extraction**: Single BERT encoder with 5 classification heads trained jointly
2. **Gold labels from MIMIC-IV-ED**: ESI labels from real nurse triage decisions (acuity field), not synthetic
3. **Arrival mode from text**: Labels derived from text cues in training data ("ambulance", "transferred", "walk-in")
4. **Intervention flags from ICD codes**: `needs_immediate_airway` labeled based on ICD codes for respiratory failure (J96), cardiac arrest (I46); `needs_immediate_iv_resuscitation` from sepsis (A41/R65), shock (R57)
5. **Iterative surgical augmentation**: 40+ experiments targeting specific extraction errors with MIMIC-IV-ED data

### Key Findings from 40+ Experiments

- **Data quality > model architecture**: Label cleaning, format diversity, and targeted augmentation improved accuracy more than architectural changes (contrastive learning, fusion heads, ESI direct prediction all failed)
- **Multi-task dilution**: Every head beyond symptom + resource + flag + pain + arrival hurts accuracy. Diagnosis, severity, ESI, and resource-count heads all degraded extraction
- **Narrative format gap**: The single biggest improvement came from adding narrative-format training data (72.2% → 86.1%)
- **Rare label challenge**: Intervention flags (airway, IV resuscitation) at ~4% of data are hard for BERT-base to learn reliably
- **Two-stage fine-tuning fails**: Freezing extraction layers and training ESI head always corrupts extraction representations

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModel
import torch.nn as nn

# Load model
model_dir = "vadimbelsky/biomedbert-triage-esi-v42"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
encoder = AutoModel.from_pretrained(model_dir)
heads = torch.load(f"{model_dir}/classifier_heads.pt", map_location="cpu", weights_only=True)

# Build heads
SYMPTOM_LABELS = [
    "chest_pain", "diaphoresis", "syncope", "stroke_symptoms",
    "altered_mental_status", "anaphylaxis", "sepsis_signs", "active_seizure",
    "suicidal_ideation", "homicidal", "psychotic",
    "abdominal_pain", "gi_bleed", "testicular_pain", "ovarian_torsion",
    "ectopic_pregnancy", "dka_signs", "toxic_ingestion", "post_ictal",
    "respiratory_distress", "shortness_of_breath", "wheezing",
    "headache", "nausea_vomiting", "back_pain",
    "laceration", "sprain", "fracture", "uri", "rash",
    "eye_pain", "ear_pain", "dental_pain", "wound", "burn",
    "fever", "hypothermia", "vaginal_bleeding", "urinary_symptoms",
    "active_hemorrhage",
    "dizziness", "palpitations", "cough", "diarrhea", "weakness",
    "anxiety", "dehydration", "allergic_reaction", "limb_pain", "constipation",
]
FLAG_LABELS = ["altered_mentation", "severe_pain_distress", "active_hemorrhage",
               "needs_immediate_airway", "needs_immediate_iv_resuscitation"]

h = encoder.config.hidden_size
symptom_head = nn.Linear(h, len(SYMPTOM_LABELS))
symptom_head.load_state_dict(heads["symptom_head"])
flag_head = nn.Linear(h, len(FLAG_LABELS))
flag_head.load_state_dict(heads["flag_head"])

# Extract
note = "A 52-year-old male was brought to the ED via ambulance with sepsis and hypotension. Critically hypotensive, requiring mechanical ventilation."
enc = tokenizer(note, max_length=256, padding="max_length", truncation=True, return_tensors="pt")

encoder.eval()
with torch.no_grad():
    cls = encoder(**enc).last_hidden_state[:, 0, :]
    sym_probs = torch.sigmoid(symptom_head(cls)).squeeze()
    flag_probs = torch.sigmoid(flag_head(cls)).squeeze()

symptoms = [SYMPTOM_LABELS[i] for i, p in enumerate(sym_probs) if p > 0.5]
flags = {FLAG_LABELS[i]: bool(p > 0.5) for i, p in enumerate(flag_probs)}

print(f"Symptoms: {symptoms}")
print(f"Flags: {flags}")
# → Symptoms: ['sepsis_signs', 'respiratory_distress', 'shortness_of_breath', 'fever']
# → Flags: {'needs_immediate_airway': True, 'needs_immediate_iv_resuscitation': True, ...}
# → Feed into ESI algorithm → Step A → ESI 1
```

## Evaluation

Evaluated on 36 expert-labeled cases from MIETIC (narrative clinical cases derived from MIMIC-IV-ED, reviewed by 2-3 emergency medicine experts).

### Confusion Matrix

```
GT\Pred   1    2   3   4   5
──────────────────────────────
  1       13   0   1   0   0
  2        0  10   0   1   0
  3        0   2   2   1   0
  4        0   0   0   4   0
  5        0   0   0   0   2
```

### Error Analysis

| Error | GT→Pred | Root Cause |
|-------|---------|------------|
| Cardiac arrest | 1→2 | "Vital signs absent" — rare phrasing, model can't extract intervention flag |
| CHF chest pain | 3→2 | Chest pain genuinely in text. **Algorithm-correct**: ESI rules say chest_pain → B1 → ESI 2. Expert overrides with clinical context. |
| Pelvic pain | 3→2 | Pain 9/10 with stable vitals. **Algorithm-correct**: B3 fires on severe distress. Expert considers stable vitals → ESI 3. |
| Open fracture transfer | 2→4 | "Open fracture" compound term not understood. Model extracts fracture (1 resource) but misses hemorrhage severity. |
| Crohn's flare | 2→3 | Unstable extraction: sepsis_signs detection for IBD presentations is marginal at BERT-base capacity. |

## Limitations

- **Single-center data**: Based on MIMIC-IV-ED (Beth Israel Deaconess Medical Center)
- **BERT-base capacity**: 110M parameters limits rare pattern learning (intervention flags, compound medical terms)
- **Binary extraction**: Can't distinguish primary vs secondary symptoms (e.g., CHF chest pain vs ACS chest pain)
- **English only**: Trained on English clinical text
- **Not a medical device**: Research use only. Not validated for clinical deployment.

## Citation

```bibtex
@misc{belsky2026biomedbert-triage,
  title={BiomedBERT-Triage-ESI: Clinical Field Extraction for Emergency Triage},
  author={Belsky, Vadim},
  year={2026},
  url={https://huggingface.co/vadimbelsky/biomedbert-triage-esi-v42}
}
```
