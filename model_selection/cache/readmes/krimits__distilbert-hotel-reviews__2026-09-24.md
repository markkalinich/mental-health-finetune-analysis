---
license: mit
base_model: distilbert-base-uncased
tags:
  - sentiment-analysis
  - text-classification
  - hotel-reviews
library_name: transformers
pipeline_tag: text-classification
---

# DistilBERT hotel-review sentiment classifier (full fine-tune)

Full fine-tune of `distilbert-base-uncased` for binary sentiment classification of hotel
reviews (labels derived from the Booking.com review schema, not a score threshold).
This checkpoint is the strongest model of the
[`krimits/hotel-review-nlp`](https://github.com/krimits/hotel-review-nlp) project.

## Metrics (frozen test set, 13,278 reviews)

| Metric | Value |
| :--- | ---: |
| Macro-F1 | **0.9634** |
| Accuracy | **97.27%** |
| Negative / positive F1 | 0.9449 / 0.9818 |
| Training rows | 118,990 |
| Trainable params | 66,955,010 (100%) |
| Best dev macro-F1 | 0.9602 |

Statistical comparison (exact McNemar, same frozen test set): full fine-tune > scratch-LoRA
(p ≈ 5.0×10⁻⁶); scratch-LoRA ≈ Qwen2.5-0.5B QLoRA (p = 0.525). Full 10-pair benchmark:
[`runs/benchmark/results.json`](https://huggingface.co/datasets/krimits/hotel-review-nlp-frozen-splits/blob/main/runs/benchmark/results.json).

## Provenance

- Weights are byte-identical to the Colab notebook `05_distilbert_full_and_lora_colab.ipynb`
  run `distilbert_legacy_full_v1` (commit `530cf9e14eea7e527a240ea470ae3a8e222c4d3f`):
  `model.safetensors` sha256 `f30daa44e795b7015151892ff5ec285e14a916e122902aa0617a15bf96ec54b7`.
- Known legacy limitation: the historical splits contain small normalized cross-split text
  overlap (train-test 170 rows); disclosed and fingerprinted in the experiment log.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tok = AutoTokenizer.from_pretrained("krimits/distilbert-hotel-reviews")
model = AutoModelForSequenceClassification.from_pretrained("krimits/distilbert-hotel-reviews")
inputs = tok("The room was spotless and the staff was wonderful.", return_tensors="pt")
print(model(**inputs).logits.argmax(-1).item())  # 1 = positive, 0 = negative
```

CPU latency: ~15–25 ms/review (single request); ~20.5 req/s under 20-user load (p50 360 ms
under concurrency). Live demo:
[`krimits/hotel-review-demo`](https://huggingface.co/spaces/krimits/hotel-review-demo).