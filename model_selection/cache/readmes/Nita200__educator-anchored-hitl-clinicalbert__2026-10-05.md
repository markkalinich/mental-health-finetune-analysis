---
language:
  - en
license: mit
tags:
  - clinical-nlp
  - healthcare-education
  - human-in-the-loop
  - educator-anchored
  - text-classification
  - transformer
datasets:
  - bigbio/mednli
metrics:
  - accuracy
  - f1
  - roc_auc
  - matthews_correlation
---

# CLINICALBERT Educator-Anchored HITL — Educator-Anchored HITL Clinical Reasoning Classifier

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT)
trained on the [MedNLI](https://physionet.org/content/mednli/1.0.0/) dataset,
used as a proxy for clinical reasoning scenarios in healthcare education.

It was refined using an **educator-anchored Human-in-the-Loop (HITL)** workflow
across 20 rounds of incremental, simulated educator-guided corrections,
as described in:

> *Educator-Anchored Human-in-the-Loop Learning: A Simulation Study of
> Transformer Models for Clinical Reasoning Assessment in Healthcare
> Education* — [citation pending]

## ⚠️ Important: Simulation Study Disclaimer

This model is a **research artefact from a simulation study**, not a
clinically validated or deployment-ready tool. Specifically:

- Training data (MedNLI) is a proxy for clinical reasoning, sourced from
  MIMIC-III clinical notes — it is **not** authentic learner submissions
  from a healthcare education context.
- HITL "educator corrections" during refinement were **simulated**
  (automated ground-truth relabelling of misclassified examples), not
  provided by real human educators.
- Do **not** use this model for actual clinical decision-making, patient
  safety assessment, or student grading without further validation by
  qualified healthcare educators.

This model is intended for **reproducibility and further research only**.

## Labels

| ID | Label     | Description                          |
|----|-----------|--------------------------------------|
| 0  | safe      | Clinically appropriate reasoning     |
| 1  | unsafe    | Clinically unsafe or incorrect       |
| 2  | ambiguous | Requires further clinical evaluation |

## Usage

```python
from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="Nita200/educator-anchored-hitl-clinicalbert",
)
result = clf(
    "Patient has chest pain. Student assessment: possible GERD. "
    "[SEP] Rationale: The patient's history is consistent with GERD "
    "given the absence of cardiac risk factors."
)
print(result)
```

## Training

- **Base model**: emilyalsentzer/Bio_ClinicalBERT
- **Dataset**: MedNLI (PhysioNet credentialed access required), original
  80/10/10 train/validation/test split preserved
- **HITL configuration**: v3 (catastrophic-forgetting-mitigated)
- **HITL rounds completed**: 20 (stops early if the correction
  pool is exhausted before reaching the maximum of 20 rounds)
- **Corrections per round**: 50
- **Replay buffer size**: 100 (seed examples resampled each round to
  anchor prior representations and prevent catastrophic forgetting)
- **Learning rate**: 5e-6
- **Epochs per round**: 1
- **Seed/pool split**: 70% seed / 30% pool

This configuration was selected after a systematic three-version
comparison (see paper Section 4.3 and 5.2) showing that a naive
incremental fine-tuning configuration (higher learning rate, larger
correction batches, no replay buffer) produces catastrophic forgetting.
Five-fold cross-validation (paper Section 5.7) confirms that the AUC
stability achieved under this configuration generalises across
independent data splits, while the magnitude of accuracy improvement in
any single run is split-dependent.
