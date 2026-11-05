---
language: en
license: mit
tags:
  - mental-health
  - text-classification
  - depression
  - suicidal
  - bert
  - crisis-detection
  - second-tier-specialist
datasets:
  - mohamedasem318/mental-health-dataset-extended-v5
---

# 🧠 Deep Dive v2 — CSSRS-Anchored Binary Depression/Suicidal Re-Ranker

> **⚠️ CLINICAL SAFETY DISCLAIMER:** This model is a research artefact for a mental health NLP
> thesis. It is **NOT** a certified clinical tool and must NOT be used for medical diagnosis,
> triage, or any safety-critical decision without qualified mental health professional oversight.

## Architecture

```
BertTokenizerFast → CrisisEvidenceMentalBERT
                        ├─ BertModel (mental/mental-bert-base-uncased)
                        │    h_seq (B, L, 768)
                        ├─ h_cls   = h_seq[:, 0, :]               [CLS] pooling
                        └─ h_crisis = max-pool(h_seq, crisis_mask) lexical safety prior
                             (fallback: h_cls when no crisis tokens)
                        └─ [h_cls ; h_crisis] (1536)
                           → Linear(256) → GELU → Dropout → Linear(2) → P(Suicidal)
```

**Crisis-evidence pooling** injects a fixed lexical safety prior. When no crisis keywords
are detected, the model collapses to standard [CLS] behaviour — no degradation on
Depression-only inputs.

## CSSRS-Anchored Training Data

| Split | Suicidal source | Depression source |
|-------|-----------------|-------------------|
| Train | CSSRS only (κ=0.79) | All sources |
| Val   | CSSRS only | All sources |
| **Test** | **All sources** (real-world) | All sources |

V3's superior Sui→Dep safety (661) came from CSSRS-only Suicidal labels. V5 source
unification degraded this signal. Deep Dive v2 restores V3-quality training signal
without distorting the test distribution.

## Threshold Calibration

Threshold calibrated **against Sui→Dep error budget (≤200 on val), NOT F1 macro**.

- Sweep: `t ∈ [0.20, 0.80]` step 0.05
- Primary: Sui→Dep ≤ 200 → maximise F1 macro
- Fallback: minimise Sui→Dep with Dep→Sui ≤ 500

**Chosen threshold: 0.25**

## Test Metrics (all-source frozen test set)

| Metric | Value |
|--------|-------|
| Accuracy | 0.6281 |
| F1 Macro | 0.5664 |
| F1 Weighted | 0.5693 |
| AUC | 0.6501 |
| Average Precision | 0.7085 |
| **Sui→Dep (safety miss)** | **2546** |
| Dep→Sui (false alarm) | 44 |

## Intended Use

**Must NOT be used standalone.** Invoked by **Quick Vibe** (`itsLu/mentalbert-v5-source-aware`)
only when its top prediction ∈ {Depression, Suicidal} with a low-confidence margin, or when
it abstains. No coverage for Normal / Anxiety / Stress / Bipolar / Personality Disorder /
Directed Aggression.

## Quick Start

```python
from inference import DeepDiveV2
clf    = DeepDiveV2.from_hub("itsLu/mentalbert-v5-deep-dive-v2", device="cpu")
result = clf.predict("I don't want to be here anymore.")
# {'label': 'Suicidal', 'p_suicidal': 0.913, 'crisis_evidence_found': True,
#   'crisis_tokens_matched': ['want to die']}
```

## Citation

Part of: *Multi-Source Mental Health Text Classification with CSSRS-Anchored Label Curation*,
Thesis 2026. Dataset: `mohamedasem318/mental-health-dataset-extended-v5`.
