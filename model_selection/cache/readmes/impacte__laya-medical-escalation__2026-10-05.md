---
license: apache-2.0
base_model:
- convaiinnovations/laya
tags:
- laya
- clinical
- emergency-medicine
- triage
- emergency-severity-index
- esi
- decision-model
- calibrated-decisions
- rlcd
- text-classification
library_name: laya
pipeline_tag: text-classification
---

# Laya Medical Escalation (`impacte/laya-medical-escalation`)

> ## ⚠️ NOT A MEDICAL DEVICE — NOT FOR CLINICAL USE
> This is a **research and educational artifact**. It was trained to reproduce the acuity levels
> recorded in a historical, de-identified dataset. It must **never** be used to triage, diagnose,
> or make care decisions for real patients. Acuity assessment is subjective and population
> dependent; a model that under-triages can cause serious harm.

**Laya Medical Escalation** is
[convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya) (421M, ModernBERT-large +
typed decision head) fine-tuned to assign the **Emergency Severity Index (ESI 1–5)** from an
emergency-department triage record. Laya is non-autoregressive: it scores each ESI level at its
own `[MASK]` marker and softmaxes over the levels in one forward pass (~23 ms), returning a
calibrated distribution rather than free text.

| | |
|---|---|
| **Base** | `convaiinnovations/laya` (Apache-2.0) |
| **Architecture** | ModernBERT-large encoder + 2-layer decision head + option-marker scorer (421M) |
| **Task** | `choice` over ESI 1–5, from a text triage record |
| **Training** | RLCD (GRPO + strictly proper scoring rule + soft cross-entropy) with inverse-frequency class weights |
| **License** | Apache-2.0 (inherited from Laya) |
| **Latency** | ~23 ms p50, single request, RTX 5060 Ti |

## Usage

```python
import laya

router = laya.load("impacte/laya-medical-escalation")

criteria = {
    "esi-1": "ESI 1 Resuscitation: requires immediate life-saving intervention "
             "(e.g. cardiac arrest, intubation, severe respiratory distress).",
    "esi-2": "ESI 2 Emergent: high-risk, drowsy/confused, severe pain; should not wait.",
    "esi-3": "ESI 3 Urgent: needs two or more resources (labs, imaging, IV fluids); vitals stable.",
    "esi-4": "ESI 4 Less urgent: needs one resource (x-ray, prescription, simple procedure).",
    "esi-5": "ESI 5 Non-urgent: needs no resources; can be referred or discharged.",
}

res = router.predict(
    "Emergency department triage record. Patient: 58-year-old male. "
    "Chief complaint: chest pain, shortness of breath. "
    "Triage vitals: HR 118, BP 88/54, RR 28, SpO2 89% on room air, temperature 98.4 F. "
    "Arrival: ambulance. History: 3 prior ED visits.",
    {"route": {
        "type": "choice",
        "instructions": "You are an emergency department triage nurse. Based only on the triage "
                        "record, assign the correct Emergency Severity Index (ESI) level.",
        "criteria": criteria,
    }},
)
print(res["answers"]["route"]["choice"])         # -> esi-2
print(res["answers"]["route"]["probabilities"])
```

## Results

**Held-out evaluation — 2500 rows, class-balanced (chance 0.20):**

| Accuracy | Macro-F1 | Under-triage ↓ | Within ±1 level | Ordinal MAE | ECE ↓ | p50 latency |
|---|---|---|---|---|---|---|
| **0.6860** | **0.6829** | **0.1564** | 0.9476 | 0.3852 | **0.0223** | 22.87 ms |

| ESI level | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| esi-1 | 0.769 | 0.860 | 0.812 | 500 |
| esi-2 | 0.666 | 0.570 | 0.614 | 500 |
| esi-3 | 0.618 | 0.566 | 0.591 | 500 |
| esi-4 | 0.621 | 0.674 | 0.646 | 500 |
| esi-5 | 0.742 | 0.760 | 0.751 | 500 |

*Under-triage* = predicted a less urgent ESI level than gold (the dangerous error); the high-acuity (gold ESI-1/2) under-triage rate is 0.189.

### Accuracy & response time vs local LLMs (same 300 held-out rows)

| System | Accuracy | Macro-F1 | Under-triage ↓ | p50 latency |
|---|---|---|---|---|
| **Laya Medical Escalation** | 0.7033 | 0.6978 | 0.1600 | 22.8 ms |
| gemma4:e4b | 0.4333 | 0.4279 | 0.3933 | 173.5 ms |
| oamazonasgabriel/qwen3.8-27b:iq4-xs-64k-text-q4kv | 0.3233 | 0.3347 | 0.2925 | 943.9 ms |
| oamazonasgabriel/minicpm-2b:bf16 | 0.2967 | 0.2880 | 0.4735 | 2538.9 ms |
| random | 0.2200 | 0.2175 | 0.3733 | — |
| always esi-3 | 0.2000 | 0.0667 | 0.4000 | — |
| laya-base (zero-shot) | 0.2133 | 0.1336 | 0.2533 | 23.6 ms |

LLMs were given a 192-token budget and a parser that strips thinking/tool-call wrappers, so this is not a formatting strawman.

### Same-dataset baselines (identical train/test split)

| Method | Features | Accuracy | Macro-F1 | Under-triage ↓ | High-acuity under-triage ↓ | Ordinal MAE |
|---|---|---|---|---|---|---|
| **Laya Medical Escalation** | text template | **0.6860** | **0.6829** | 0.1564 | 0.1890 | 0.3852 |
| xgboost (laya) | 214 | 0.6072 | 0.5969 | 0.1624 | 0.2730 | 0.5016 |
| xgboost (full) | 970 | 0.6136 | 0.6018 | 0.1524 | 0.2650 | 0.5116 |
| deterministic ESI v5 (full) | cc + vitals rules | 0.4176 | 0.3963 | 0.2724 | 0.5820 | 0.752 |

XGBoost uses the full 970-column table; the deterministic model is the partial ESI v5 clinical algorithm (resource count inferred — the dataset has no resource, pain, or mental-status fields, so this is a lower bound on it).


## Dataset

Trained on the **Yale School of Medicine** emergency-department triage dataset:

> Hong WS, Haimovich AD, Taylor RA. *Predicting hospital admission at emergency department triage
> using machine learning.* **PLOS ONE** 13(7): e0201016 (2018).
> DOI [10.1371/journal.pone.0201016](https://doi.org/10.1371/journal.pone.0201016)

560,486 de-identified ED visits × 972 variables. The model consumes a **text state** built only
from at-triage fields — chief complaint (from 200 chief-complaint one-hots), triage vitals
(HR, BP, RR, SpO2, temperature), age, sex, arrival mode, prior ED visits, previous disposition and
outpatient medication count. HF mirror used:
`kondratevakate/hospital-triage-and-patient-history-data` (lossless RData→Parquet re-host).
**Citation is required for any use of this data; do not redistribute it.**

## Training

- 57,271 training rows (ESI-1 4,771 · ESI-2 15,000 · ESI-3 15,000 · ESI-4 15,000 · ESI-5 7,500).
- 2 epochs, bf16 + gradient checkpointing, one RTX 5060 Ti 16 GB, ~75 min.
- Temperature calibrated to 1.046 on held-out logits.
- No leakage: `esi` / `disposition` never enter the state text.

## Limitations

- **Research artifact only — not for clinical use** (see the banner above).
- English only; the base Laya checkpoint is English.
- The state is a *template* over structured fields, not free-text clinician notes.
- ESI is a nurse-assigned, partly subjective label; class boundaries are fuzzy.
- ESI-2/3 are the hardest classes; under-triage is the metric that matters and it is not zero.
- Performance may not transfer to other hospitals, populations, or triage protocols.

## Credits

- [convaiinnovations/laya](https://huggingface.co/convaiinnovations/laya) — base model and RLCD
  recipe (Apache-2.0).
- Hong, Haimovich & Taylor (Yale) / PLOS ONE — the triage dataset.

## Citation

```bibtex
@misc{laya_medical_escalation2026,
  title  = {Laya Medical Escalation: a calibrated ESI decision model},
  author = {oamazonasgabriel},
  year   = {2026},
  url    = {https://huggingface.co/impacte/laya-medical-escalation}
}
```
