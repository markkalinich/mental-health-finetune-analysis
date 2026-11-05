---
base_model: answerdotai/ModernBERT-base
library_name: transformers
pipeline_tag: text-classification
tags:
  - emotion
  - multi-label
  - goemotions
  - modernbert
datasets:
  - google-research-datasets/go_emotions
license: apache-2.0
---

# Opus Emotion 1

A multi-label emotion classifier over 28 labels, fine-tuned from
`answerdotai/ModernBERT-base` on GoEmotions.

Trained in **13.6 minutes on a consumer AMD RX 7600** (8GB, gfx1102) under WSL2
with ROCm. No datacentre, no rented GPU.

| | |
|---|---|
| macro F1 | **0.490** |
| micro F1 | 0.582 |
| classes never predicted | **0 / 28** |
| training time | 13.6 min |
| throughput | 213 samples/s |
| peak VRAM | 4.59 GB |

Macro F1 of 0.49 is in line with published GoEmotions baselines; the original
paper reports 0.46 macro F1 with a BERT-base model.

![Per-class results](goemotions_chart.png)

## The interesting part is not the average

A single macro-F1 number hides what actually happened. Per-class F1 ranges from
**0.90 to 0.09**, and the obvious explanation — rare labels do worse — only
holds up halfway (r = 0.40 between log support and F1).

The clearer pattern is **lexical distinctiveness**:

| label | support | F1 | |
|---|---|---|---|
| gratitude | 358 | **0.90** | announced by the word "thanks" |
| approval | 397 | **0.35** | a judgement call, no marker word |
| remorse | 68 | **0.70** | "sorry", "my fault" |
| annoyance | 303 | **0.26** | overlaps anger, disapproval, disappointment |

`gratitude` and `approval` have near-identical support and a 2.5× gap in F1.
More data would not close it. Emotions with a reliable surface marker are easy;
emotions that are inferences about intent are hard, and human annotators
disagree about them too — which puts a ceiling on what any model can score.

`relief` (F1 0.09, n=18) is the floor case: rare *and* subjective.

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

name = "opus-research/opus-emotion-1"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name).eval()

text = "FUCK YOU BRO WHY ARE YOU SO FUCKING RETARDED"
with torch.no_grad():
    probs = torch.sigmoid(model(**tok(text, return_tensors="pt")).logits)[0]

for i, p in enumerate(probs):
    if p > 0.5:
        print(model.config.id2label[i], f"{p:.1%}")
# anger 97.2%
```

**Multi-label, so use `sigmoid` and a threshold — not `softmax`.** A comment can
be both `admiration` and `amusement`.

**Tune the threshold to your task.** 0.5 is the reported operating point;
dropping to 0.3 raises recall on the rare classes at some cost to precision,
which is usually the right trade if you are filtering rather than labelling.

## Training

| | |
|---|---|
| Base | `answerdotai/ModernBERT-base` (149M) |
| Epochs / LR | 4 / 5e-5, cosine, 6% warmup |
| Batch / max_len | 32 / 96 |
| Precision | bf16 |
| Loss | BCEWithLogits (multi-label) |
| Hardware | AMD RX 7600 8GB, ROCm 7.13 via ROCDXG on WSL2 |

Three epochs gave macro F1 0.483; four gave 0.490. It was still improving
slowly, so more epochs may add a little.

### Note on the hardware

The RX 7600 is not on AMD's supported list for ROCm under WSL. It works via
ROCDXG with a device-ID override in `/opt/rocm/share/rocdxg/dids.conf`, and by
capping torch's VRAM so the Windows desktop compositor keeps a slice — without
that cap, filling 8GB freezes the screen.

## Limitations

- **English Reddit comments.** Register-specific; expect degradation elsewhere.
- **Rare, subjective labels are weak** — `relief`, `grief`, `pride` sit below
  0.40 and should not be relied on individually.
- **Annotator disagreement is the ceiling**, not model capacity, for several of
  the low scorers.
- Trained on 128-token inputs, truncated at 96 during training.
