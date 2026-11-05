---
language:
- en
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- text-classification
- guardrail
- safety
- cbt
- mental-health
- academic-stress
pipeline_tag: text-classification
---

# ReframeBot-Guardrail-DistilBERT

A 3-class DistilBERT classifier for routing ReframeBot user turns:

| Label | Meaning |
|---|---|
| `TASK_1` | CBT / academic stress |
| `TASK_2` | Crisis / self-harm signal |
| `TASK_3` | Out-of-scope |

This version was retrained on `data/guardrail_dataset_clean.jsonl`, which
merges the original guardrail data with curated hard cases for CBT/Crisis
boundaries, Vietnamese text, pills/overdose language, and OOS work/mental
health informational prompts.

## Current System Threshold

The ReframeBot runtime uses the classifier's full probability vector and
routes to `TASK_2` when:

```text
P(TASK_2) >= 0.10
```

after academic-context/follow-up overrides and after the regex + semantic
crisis detector has already run.

## Evaluation

Hard out-of-domain eval set (`data/evaluation_test_data.json`, 60 samples):

| Mode | Accuracy | TASK_2 Precision | TASK_2 Recall | TASK_2 F1 |
|---|---:|---:|---:|---:|
| Argmax only | 0.9667 | 1.0000 | 0.9048 | 0.9500 |
| Tuned `P(TASK_2) >= 0.10` | 0.9833 | 0.9545 | 1.0000 | 0.9767 |

Threshold sweep artifact in the project repo:

- `reports/guardrail_threshold_sweep.csv`
- `reports/guardrail_threshold_sweep.png`

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Nhatminh1234/ReframeBot-Guardrail-DistilBERT",
    revision="v2-guardrail-clean",
)

classifier("I'm stressed about my final exam")
```

For full class probabilities:

```python
classifier("I bought pills to overdose", top_k=None)
```

## Safety Note

This classifier is a routing component, not a standalone crisis intervention
system. ReframeBot also uses regex + semantic crisis detection and crisis
response handling around this model.
