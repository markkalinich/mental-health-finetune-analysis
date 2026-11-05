---
license: apache-2.0
language:
- multilingual
tags:
- typed-decision
- text-classification
- topic-classification
- sentiment-analysis
- language-identification
- calibrated-probabilities
- sib-200
metrics:
- accuracy
- ece
---

# Fragment-1-multilingual (v1, sandbox proof run)

An **11.04M-parameter typed-decision model covering 204 languages**, trained from
scratch on the FrameXlabs Fragment contract: read a question and a text, score
every candidate marker, and report a **calibrated probability distribution** —
honest uncertainty, not just verdicts.

This v1 was trained end-to-end on a sandbox CPU (1,680 steps, batch 20,
fixed-seed 16.8k-record subset) as a small-scale proof of the full pipeline:
proper scoring rules (log + spherical + RPS) → post-hoc per-question-type
temperature calibration → full held-out evaluation → export. It is the live
release model on the FrameXlabs release page; the Colab notebook retrains the
same architecture at full scale on GPU.

## Held-out test results (n = 26,080, 204 languages)

| Family | n | Accuracy | ECE |
|---|---|---|---|
| translation verification (noul, 2-way) | 6,120 | **0.4824** | 0.269 |
| SIB topic (choice, 7-way, chance 0.143) | 18,360 | **0.2501** | 0.068 |
| sentiment (score, 3-way) | 1,600 | **0.3600** | 0.078 |
| **overall** | 26,080 | **0.3113** | **0.1151** |

- topic macro accuracy: **0.2501** (204 languages)
- calibration temperatures (choice / score / noul): 0.8502 / 7.1097 / 8.0
- auxiliary language-ID head top-1: 0.0307 (weak at this scale, kept honest)

## Files

| File | Content |
|---|---|
| `model.safetensors` | trained weights (44 MB) |
| `modeling_fragment1m.py` | standalone model code (torch + safetensors only) |
| `config.json` | architecture + calibrated temperatures + criteria text |
| `tokenizer.json` | 24k byte-level BPE over all 204 languages |
| `languages.json` | language index (order of the LID head) |
| `eval_results.json` | summary + per-language topic accuracy |

## Usage

```python
# pip install torch safetensors
from modeling_fragment1m import load_fragment1m

model, cfg = load_fragment1m(".")      # path to this folder
# forward(ids, marker_pos, marker_mask, qtype) -> marker logits
# divide logits by model.temperature[qtype], then softmax
# model.lid(ids) -> 204-way language logits (auxiliary, weak)
```

Sequence layout (matches training): `[CLS] "choice question: <instructions>" [SEP]
[MRK] opt0 [MRK] opt1 … [SEP] <text> [SEP]`, truncation to 128 tokens.

## Training data

- **SIB-200** (public, 204 languages): 7-way topic choice + parallel
  translation-verification (noul)
- **Tweet Sentiment Multilingual** (public, 8 languages): 3-level sentiment score
- English anchors from AG News / BoolQ / SST-5 for the shared question formats

