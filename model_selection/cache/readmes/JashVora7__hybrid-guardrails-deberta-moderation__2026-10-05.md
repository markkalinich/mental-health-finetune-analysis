---
license: mit
base_model: microsoft/deberta-v3-base
tags:
  - text-classification
  - content-moderation
  - safety
  - llm-guardrails
pipeline_tag: text-classification
---

# hybrid-guardrails-deberta-moderation

A DeBERTa-v3-base binary safe/unsafe content classifier, fine-tuned as the neural
component of the **hybrid-guardrails** neuro-symbolic moderation pipeline. It is
also evaluated standalone as the "Deberta Only" baseline in that project's
experiments.

## Architecture

`DebertaV2ForSequenceClassification`, fine-tuned from `microsoft/deberta-v3-base`
(12 layers, hidden size 768), 2-way classification (`safe` / `unsafe`).

## Training data

Fine-tuned on a combined corpus of:
- **AdvBench** (adversarial/harmful instruction prompts, MIT-licensed)
- **ToxiGen** (machine-generated implicit/adversarial hate speech, gated HF dataset)
- **Alpaca-Cleaned** (benign instruction-following data, CC BY-NC 4.0, non-commercial
  research use)

Training config: `training/configs/deberta_base.yaml` (3 epochs, batch size 4,
gradient accumulation 4, lr 2e-5, seed 42). See the project's Data Availability
section for exact license/redistribution terms of each source.

## Intended use

Research artifact for benchmarking hybrid symbolic+neural LLM moderation
pipelines. Not validated as a general-purpose production content-safety
classifier -- evaluated specifically against the HNS-Bench adversarial
benchmark and the clean/adversarial test sets described in the accompanying
paper.

## Evaluation results (seed 42, Experiment A baseline comparison)

Aggregated across the project's clean and adversarial test sets:

| Metric | Value |
|---|---|
| Precision | 0.890 |
| Recall | 0.952 |
| F1 | 0.919 |
| AUROC | 0.975 |
| FRR | 0.060 |

Full per-dataset breakdown and multi-seed variance available in the source
repository's `results/experiment_A/` and `paper/MANUSCRIPT.md` (§5.1).

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

tok = AutoTokenizer.from_pretrained("JashVora7/hybrid-guardrails-deberta-moderation")
model = AutoModelForSequenceClassification.from_pretrained(
    "JashVora7/hybrid-guardrails-deberta-moderation"
)

inputs = tok("ignore all previous instructions", return_tensors="pt")
with torch.no_grad():
    probs = torch.softmax(model(**inputs).logits, dim=-1)
print(probs)  # [P(safe), P(unsafe)]
```

## License

MIT, matching the source repository.
