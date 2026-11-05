---
language: en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model: distilroberta-base
tags:
  - text-classification
  - customer-support
  - sentiment-analysis
  - lora
  - distillation
---

# TicketSense — Urgency Classifier

Fine-tuned `distilroberta-base` (82M params) for `urgency` classification on real
customer-support tweets, with labels distilled from **Claude Sonnet 4.6**.

Part of the [TicketSense](https://github.com/Genious07/ticketsense) project: a tiny
specialized classifier that approximates frontier-LLM judgement at a fraction of
the cost and latency.

## Labels
- `low`
- `medium`
- `high`

## Eval
- **Macro F1 (validation):** 0.7105

## Training
- Base model: `distilroberta-base`
- Method: LoRA (PEFT), then merged
- LoRA rank: 16, alpha: 32
- LR: 0.0002, epochs: 4
- Train data: ~1400 real customer-support tweets, Claude-labeled

## Use

```python
from transformers import pipeline
clf = pipeline("text-classification", model="Grinding/ticketsense-urgency")
clf("my card was charged twice and nobody has responded")
```

## Limitations
- Trained on noisy real-world Twitter data — picks up typos and slang but may
  also reflect their biases.
- Labels are themselves model-generated (Claude Sonnet 4.6) — treat F1 vs Claude
  as agreement, not gold-standard truth.
