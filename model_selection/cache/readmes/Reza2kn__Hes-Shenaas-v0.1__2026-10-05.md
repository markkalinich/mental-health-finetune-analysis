---
license: apache-2.0
language:
- fa
library_name: transformers
pipeline_tag: text-classification
tags:
- persian
- farsi
- emotion-classification
- social-media
metrics:
- accuracy
- f1
base_model: FacebookAI/xlm-roberta-large
---

# Hes Shenaas v0.1

Hes Shenaas v0.1 is a single-model Persian emotion classifier based on XLM-RoBERTa Large. It predicts one of seven labels:

| Label | Meaning |
|---|---|
| `ANGRY` | anger |
| `FEAR` | fear or anxiety |
| `HAPPY` | happiness or joy |
| `HATE` | hate or strong aversion |
| `SAD` | sadness |
| `SURPRISE` | surprise |
| `OTHER` | neutral, unclear, or outside the six emotions |

## Evaluation

The checkpoint was selected using a fixed 1,232-example validation split. The protected 1,151-example test split was evaluated after checkpoint selection.

| Split | Examples | Accuracy | Macro F1 | Weighted F1 |
|---|---:|---:|---:|---:|
| Validation | 1,232 | 73.94% | 75.05% | 73.76% |
| Test | 1,151 | **77.58%** | 76.27% | 77.64% |

Test F1 by class:

| ANGRY | FEAR | HAPPY | HATE | SAD | SURPRISE | OTHER |
|---:|---:|---:|---:|---:|---:|---:|
| 68.47% | 81.03% | 86.04% | 70.83% | 79.77% | 72.66% | 75.11% |

These numbers describe the project's frozen Persian emotion benchmark and should not be assumed to transfer unchanged to other domains.

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Reza2kn/Hes-Shenaas-v0.1",
    tokenizer="Reza2kn/Hes-Shenaas-v0.1",
)

print(classifier("امروز واقعاً روز فوق‌العاده‌ای بود"))
```

For complete class probabilities:

```python
print(classifier("از این وضعیت خیلی عصبانی‌ام", top_k=None))
```

The model truncates inputs to 128 tokens, matching training and evaluation.

## Training

- Base model: `FacebookAI/xlm-roberta-large`
- Base revision: `c23d21b0620b635a76227c604d44e43a9f0ee389`
- Training rows: 8,471
- Original cleaned rows: 4,862
- Added public Persian tweets: 3,609
- Added rows were accepted only when two Gemini 3.8 Flash passes agreed and both marked the text self-contained, natural Persian, supported by exact textual evidence, and at least 0.85 confidence.
- Gemini labels were used for training only. Validation and test texts were excluded from API payloads.
- Selection: maximum validation accuracy with earlier epoch retained on ties
- Selected epoch: 5

## Limitations

The model is intended for research and product prototyping, especially short informal Persian text. Emotion labels are subjective, and performance can vary on formal writing, code-switching, sarcasm, dialects, long documents, or domains unlike the evaluation data. The `OTHER` label combines neutral and ambiguous cases. Do not use predictions as the sole basis for high-impact decisions about people.

## Integrity

The published `model.safetensors` SHA-256 is:

`43737d1933dd36966f541e9155aa02be1d394ff9f7ff2e475515fc9ed1413030`

The metrics and checkpoint were independently rechecked before release.

## Licensing and attribution

The Reza2kn fine-tuning modifications are released under the Apache License, Version 2.0. The underlying XLM-RoBERTa Large model remains subject to its MIT license. Both notices apply to this distribution.
See [LICENSE](LICENSE). Existing third-party copyright, license, and attribution notices remain applicable.

- Upstream: [FacebookAI/xlm-roberta-large](https://huggingface.co/FacebookAI/xlm-roberta-large/tree/c23d21b0620b635a76227c604d44e43a9f0ee389); declared license: `mit`.
  - Retained notice: [LICENSE-MIT](UPSTREAM_LICENSES/FacebookAI--xlm-roberta-large/LICENSE-MIT).
