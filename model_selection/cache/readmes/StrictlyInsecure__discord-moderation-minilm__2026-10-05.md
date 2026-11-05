---
license: apache-2.0
base_model: sentence-transformers/all-MiniLM-L6-v2
datasets:
  - google/jigsaw_toxicity_pred
language:
  - en
pipeline_tag: text-classification
library_name: transformers
tags:
  - moderation
  - content-moderation
  - toxicity
  - discord
  - chat
  - onnx
  - int8
  - edge
widget:
  - text: "i'm gonna destroy you in rocket league tonight lmao"
    example_title: Gaming banter (benign)
  - text: "gg everyone, good games tonight"
    example_title: Normal chat (benign)
  - text: "FREE NITRO for everyone, claim here bit.ly/x9k2"
    example_title: Spam
  - text: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    example_title: Flood
---

# discord-moderation-minilm

A **23 MB INT8 ONNX** text classifier for chat moderation, built for edge deployment — it runs on
a Raspberry Pi, not just a GPU box.

This is the **speed** variant of a pair (numbers are **in-domain**, on held-out data the model
never trained on — see Results):

| | size | latency | false positives | missed abuse |
|---|---|---|---|---|
| **this model (L6)** | **23 MB** | **~1.9 ms** | **2.7%** | 3.5% |
| [`discord-moderation-minilm-l12`](https://huggingface.co/strictlyinsecure/discord-moderation-minilm-l12) | 33 MB | ~4.1 ms | 3.9% | **2.2%** |

Use this one on a Pi or at very high volume — it flags fewer innocent messages at the default
threshold. Use L12 for a lower miss rate. Both are honest generalization numbers; the threshold is
a knob (see Thresholding).

|  |  |
|---|---|
| **Classes** | `benign` · `abusive` · `spam` · `flood` |
| **Size** | **23 MB** (INT8 ONNX) · 91 MB (fp32 safetensors) |
| **Latency** | ~1.9 ms/message, INT8 ONNX desktop CPU |
| **Base** | [`sentence-transformers/all-MiniLM-L6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) (22M params) |
| **Context** | 200 tokens |

## Why this exists

Most open toxicity classifiers have two problems for chat moderation:

1. **No spam or flood class.** They're toxicity-only, so a moderation pipeline has to bolt on a
   separate heuristic. This model predicts all four classes natively.
2. **They over-flag competitive banter.** *"I'm gonna destroy you in Rocket League"* is not a
   threat, but a model trained on Wikipedia edit-war comments often thinks it is. False positives
   punish innocent users, and they're the reason moderation bots get uninstalled.

## Results

Measured on a held-out test set the model **never trained on** (excluded from training by
construction), split by domain because register matters. Counts are FP/FN, threshold 0.85, INT8 ONNX.

**In-domain** — chat-register text (Wikipedia/Jigsaw + synthetic chat), what this model is for:

| metric | count | rate |
|---|---|---|
| false positives (innocent flagged) | 30/1,124 | **2.7%** |
| false negatives (abuse missed) | 51/1,462 | **3.5%** |
| per-class recall | harassment 98% · spam 100% · flood 100% · toxicity ~87% | |
| identity-term bias probe (`bias_test.py`, 592 benign identity sentences) | 11 flagged | **1.9%** |
| surface-form robustness (casing, markdown, punctuation) | 107/110 | |
| out-of-distribution suite (39 hand-written: short messages, banter, threats) | 38/39 | |
| latency | INT8 ONNX, desktop CPU | ~1.9 ms |

**Out-of-domain — real game chat** (CONDA, a register this model was NOT trained on):

| metric | count | rate |
|---|---|---|
| false positives | 152/718 | 21.2% |
| false negatives | 261/680 | 38.4% |

Game chat is the **honest weakness** — this model is Wikipedia/Jigsaw-register, not gaming slang.
The larger [L12](https://huggingface.co/strictlyinsecure/discord-moderation-minilm-l12) is cleaner
on the identity probe (0/592 vs this model's 11/592); at 22M params, L6 has less capacity to fully
absorb the debiasing. If identity fairness is critical for your deployment, prefer L12.

> **Note on prior revisions.** Earlier uploads reported ~2.7% FP / 1.9% FN. Those were
> **train-on-test inflated** (the eval set overlapped the training data) and the weights carried an
> identity-term bias. This revision excludes the holdout from training (so the numbers above are
> real generalization) and applies counterfactual augmentation to cut identity bias to 1.9%.

For scale: general-purpose LLM judges prompted for moderation measured far worse on the same
yardsticks at 40–100× the size (`phi3:mini`, 2.2 GB: F1 ~48 on game chat; `llama-guard3:1b`: missed
~84% of interpersonal abuse).

## Usage

### ONNX (recommended — this is the 23 MB path)

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline

REPO = "strictlyinsecure/discord-moderation-minilm"
model = ORTModelForSequenceClassification.from_pretrained(REPO, subfolder="onnx", file_name="model.onnx")
tok = AutoTokenizer.from_pretrained(REPO)
clf = pipeline("text-classification", model=model, tokenizer=tok, top_k=None, device=-1)

clf("i'm gonna destroy you in rocket league tonight lmao")
# → benign  (0.992)
clf("FREE NITRO for everyone, claim here bit.ly/x9k2")
# → spam    (0.993)
clf("shut up you idiot nobody likes you")
# → abusive (0.991)
```

Requires `pip install optimum[onnxruntime]`.

### PyTorch (fp32)

```python
from transformers import pipeline

clf = pipeline("text-classification", model="strictlyinsecure/discord-moderation-minilm", top_k=None)
clf("FREE NITRO click here bit.ly/x9k2")
# [{'label': 'spam', 'score': 0.99}, ...]
```

### Thresholding

The model is **bimodal** — it outputs ~0.99 or ~0.003 and little in between. On the held-out set,
the trade-off curve is nearly flat between 0.3 and 0.9, so the threshold is not a delicate choice:

| threshold | abuse caught | false positives |
|---|---|---|
| 0.30 | 98.8% | 38 / 399 |
| **0.85** | **97.4%** | **26 / 399** |
| 0.95 | 95.6% | 20 / 399 |

## Training

* **Base:** `all-MiniLM-L6-v2`, 4-class sequence classification head, `max_length=200`.
* **Data:** ~35k rows — stratified [Jigsaw Toxic Comment
  Classification](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) (CC0),
  length-filtered to chat-sized messages, plus synthetic chat-register rows (evasion, sarcasm,
  spam, flood, hard benign negatives) and counterfactual identity augmentation. **CC0 + owned
  synthetic only — no CONDA** (which has no license).
* **The held-out test set is excluded from training** (a prior revision did not do this, which
  inflated its reported scores). Numbers above are real generalization.
* **Identity-bias fix.** Counterfactual augmentation (term-swapping within identity groups +
  both-polarity templates in contracted and expanded forms) decorrelates identity terms from the
  label. On L6 this cuts the 592-sentence probe to 11 flagged (1.9%); the larger L12 reaches 0.
* **Class-weighted loss** (inverse frequency). Without it the model collapses to predicting
  `abusive` for everything.
* 70/15/15 split, early stopping on validation macro F1, INT8 dynamic quantization for export
  (effectively free — the INT8 cost is within measurement noise).

`toxicity` and `harassment` are **merged into one `abusive` class**. On the labeled corpus, two
annotators (Jigsaw's humans and an LLM judge) disagreed about which of those two buckets an
abusive message belonged in **48% of the time**. That boundary was training noise, not signal, and
most moderation pipelines take the same action for both.

## Limitations — please read before deploying

* **The spam and flood scores are optimistic.** Those classes were trained on *templated synthetic
  data*, and the evaluation set draws from the same template families. They score ~100% here.
  Real-world spam is far more varied. Read this as "learned these patterns", not "solved spam".
* **Never trained on real chat logs.** The training data is Wikipedia comments plus synthetic
  chat. The register gap is real and measurable — see
  [ToxBuster](https://arxiv.org/abs/2305.12542), which found **+57 points of recall** from
  training on actual game chat instead of Wikipedia. **Expect degradation on live traffic.**
* **English only.** Slurs and abuse in other languages will likely be missed.
* **Evasion is only lightly covered.** Leetspeak, unicode homoglyphs and spaced-out letters appear
  in training, but only from a synthetic generator — a determined evader will get through.
* Evaluated on the author's own held-out split, not a public benchmark. Numbers are not directly
  comparable to models evaluated elsewhere.

## Intended use

A **fast first-pass filter** in a moderation pipeline — cheap enough to run on every message, with
a human or a stronger model handling escalation. It is not a substitute for human moderators, and
it should not be the sole basis for automated bans.

## License & attribution

Apache-2.0. See `NOTICE` for the attribution required on redistribution.

Trained on the Jigsaw Toxic Comment Classification dataset (**CC0**). The underlying comment text
originates from Wikipedia and is licensed **CC-BY-SA-3.0**.

Base model `sentence-transformers/all-MiniLM-L6-v2` is Apache-2.0.
