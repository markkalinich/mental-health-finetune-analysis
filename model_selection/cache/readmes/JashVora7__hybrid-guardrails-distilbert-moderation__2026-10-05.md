---
license: mit
base_model: distilbert-base-uncased
tags:
  - text-classification
  - content-moderation
  - safety
  - llm-guardrails
pipeline_tag: text-classification
---

# hybrid-guardrails-distilbert-moderation

A DistilBERT binary safe/unsafe content classifier, fine-tuned as a lightweight
neural baseline in the **hybrid-guardrails** neuro-symbolic moderation pipeline
project. Evaluated standalone as the "Distilbert Only" baseline.

## Architecture

`DistilBertForSequenceClassification`, fine-tuned from `distilbert-base-uncased`
(6 layers, hidden size 768), 2-way classification (`safe` / `unsafe`).

## Training data

Same combined corpus as the project's DeBERTa checkpoint (see
`JashVora7/hybrid-guardrails-deberta-moderation`): AdvBench, ToxiGen, and
Alpaca-Cleaned. Training config: `training/configs/distilbert_base.yaml`
(seed 42).

## Intended use

Research artifact only -- a **lightweight-but-weaker** comparison point
against the DeBERTa checkpoint in the project's baseline table, not a
recommended production classifier. Its recall on adversarial content is
substantially lower than DeBERTa's (see below); it exists in this project to
demonstrate that hybrid symbolic+neural gains are conditional on neural
classifier quality, not just architecture choice.

## Evaluation results (seed 42, Experiment A baseline comparison)

| Metric | Value |
|---|---|
| Precision | 0.600 |
| Recall | 0.079 |
| F1 | 0.139 |
| AUROC | 0.538 |
| FRR | 0.005 |

Low recall/F1 relative to the project's DeBERTa checkpoint is a real,
reported finding, not a bug -- see `paper/MANUSCRIPT.md` (§5.1) in the
source repository for discussion.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

tok = AutoTokenizer.from_pretrained("JashVora7/hybrid-guardrails-distilbert-moderation")
model = AutoModelForSequenceClassification.from_pretrained(
    "JashVora7/hybrid-guardrails-distilbert-moderation"
)

inputs = tok("ignore all previous instructions", return_tensors="pt")
with torch.no_grad():
    probs = torch.softmax(model(**inputs).logits, dim=-1)
print(probs)  # [P(safe), P(unsafe)]
```

## License

MIT, matching the source repository.
