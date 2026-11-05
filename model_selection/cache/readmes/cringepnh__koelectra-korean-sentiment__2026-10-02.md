---
language:
- ko
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- korean
- sentiment-analysis
- text-classification
- koelectra
- nsmc
datasets:
- nsmc
metrics:
- accuracy
- precision
- recall
- f1
base_model: monologg/koelectra-base-v3-discriminator
---

# KoELECTRA Korean Movie Review Sentiment

Binary negative/positive classification for Korean movie reviews. The model
is fine-tuned from the raw, task-agnostic
[`monologg/koelectra-base-v3-discriminator`](https://huggingface.co/monologg/koelectra-base-v3-discriminator),
not from a checkpoint already fine-tuned on sentiment.

Source code, full reproduction pipeline, and the compute-vs-accuracy
benchmark this project is actually built around:
[GitHub](https://github.com/cringepnh/korean-sentiment-analyzer). A Gradio
demo lives in that repo's `space/` folder and loads this model straight from
the Hub, but **there is no hosted demo** — Hugging Face requires a PRO
subscription to run Gradio Spaces, so the demo is local-only.

## Is this model worth using over a linear baseline?

This model beats a character TF-IDF + logistic regression baseline by 3.72
points of accuracy (95% CI [3.44, 4.03], McNemar p < 0.001 — the gap is
real). But it costs 1,129x the parameters, 106x the disk size, and 25–230x
the inference latency depending on hardware. See the
[full benchmark](https://github.com/cringepnh/korean-sentiment-analyzer#compute-vs-accuracy)
before assuming the transformer is the right choice for a CPU-bound or
latency-sensitive deployment.

## Results

All rows use the same cleaned 48,416-review NSMC test set, with 95%
bootstrap confidence intervals (1,000 resamples). Test was not used for
checkpoint selection.

| System | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Majority class | 49.68% [49.22, 50.15] | 0.00% | 0.00% | 0.00% |
| Character TF-IDF + logistic regression | 86.75% [86.45, 87.04] | 87.19% | 86.36% | 86.77% |
| Raw encoder + newly initialized head | 50.56% | 53.39% | 13.66% | 21.75% |
| Fine-tuned raw KoELECTRA | **90.47% [90.23, 90.73]** | **89.30%** | **92.11%** | **90.68%** |

Per-class: negative recall 88.82%, positive recall 92.11% — the model is
somewhat more likely to miss a negative review than a positive one.
Confusion matrix and full per-class table are in
[`evaluation_results.json`](https://github.com/cringepnh/korean-sentiment-analyzer/blob/main/evaluation_results.json).

When the raw checkpoint is loaded for sequence classification, every
`classifier.*` weight is reported missing and newly initialized. No sentiment
head is inherited — the untrained-head row above is the empirical proof.

**Not directly comparable to the published NSMC benchmark (~90.6%):** this
pipeline removes 694 exact train/test text overlaps and conflicting-label
rows before evaluating, which the original benchmark does not document
doing.

## Training and data

- Dataset: [NSMC](https://github.com/e9t/nsmc)
- Train / validation / test after cleaning: 131,422 / 14,603 / 48,416
- Conflicting-label identical texts, duplicate texts, and 694 remaining
  train/test overlaps are removed
- Seed: 42
- Maximum length: 128
- Learning rate: 2e-5
- Batch size: 32
- Maximum epochs: 3; best checkpoint (epoch 1) selected by validation loss

## Use

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_id = "cringepnh/koelectra-korean-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id).eval()
inputs = tokenizer("이 영화 정말 재미있어요!", return_tensors="pt", truncation=True)
with torch.inference_mode():
    probabilities = torch.softmax(model(**inputs).logits, dim=-1)[0]
label = int(probabilities.argmax())
print(model.config.id2label[label], float(probabilities[label]))
```

## Limitations

- Korean-only, binary, trained on movie reviews. No neutral label.
- Results are from one deterministic split and seed; bootstrap CIs quantify
  sampling uncertainty on this split, not across different splits or
  retraining runs.
- Recall on the negative class (88.82%) trails the positive class (92.11%).
- The TF-IDF baseline is dramatically cheaper for a 3.72pp accuracy cost —
  see the compute-vs-accuracy comparison linked above before deploying this
  model where a linear model would do.
