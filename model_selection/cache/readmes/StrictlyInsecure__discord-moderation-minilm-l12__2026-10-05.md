---
license: apache-2.0
base_model: sentence-transformers/all-MiniLM-L12-v2
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

# discord-moderation-minilm-l12

A **33 MB INT8 ONNX** classifier for chat moderation. This is the larger variant of a pair
(numbers are **in-domain**, on held-out data the model never trained on — see Results):

| | size | latency | false positives | missed abuse |
|---|---|---|---|---|
| [`discord-moderation-minilm`](https://huggingface.co/strictlyinsecure/discord-moderation-minilm) (L6) | 23 MB | ~1.9 ms | 2.7% | 3.5% |
| **this model (L12)** | **33 MB** | **~4.1 ms** | 3.9% | **2.2%** |

At the default threshold the two trade precision for recall: L6 flags fewer innocent messages, L12
misses less abuse. Pick L6 on a Raspberry Pi or at high volume; pick L12 for the lower miss rate.
The threshold is a knob (see Thresholding) — compare them at a matched false-positive budget, not
at the same raw cutoff.

|  |  |
|---|---|
| **Classes** | `benign` · `abusive` · `spam` · `flood` |
| **Base** | [`sentence-transformers/all-MiniLM-L12-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2) (33M params) |
| **Context** | 200 tokens |

## Why this exists

Most open toxicity classifiers have two problems for chat moderation:

1. **No spam or flood class.** They're toxicity-only, so a pipeline has to bolt on a separate
   heuristic. This model predicts all four classes natively.
2. **They over-flag competitive banter.** *"I'm gonna destroy you in Rocket League"* is not a
   threat. False positives punish innocent users, and they're what gets a moderation bot
   uninstalled.

## Results

Measured on a held-out test set the model **never trained on** (the holdout is excluded from
training by construction), split by domain because register matters. Counts are FP/FN, threshold
0.85, INT8 ONNX.

**In-domain** — chat-register text (Wikipedia/Jigsaw + synthetic chat), what this model is for:

| metric | count | rate |
|---|---|---|
| false positives (innocent flagged) | 44/1,124 | **3.9%** |
| false negatives (abuse missed) | 32/1,462 | **2.2%** |
| per-class recall | harassment 99% · spam 100% · flood 100% · toxicity ~90% | |
| identity-term bias probe (`bias_test.py`, 592 benign identity sentences) | 0 flagged | **0.0%** |
| surface-form robustness (casing, markdown, punctuation, `k y s`-style) | 110/110 | |
| out-of-distribution suite (39 hand-written: short messages, banter, threats) | 38/39 | |
| latency | INT8 ONNX, desktop CPU | ~4.1 ms |

**Out-of-domain — real game chat** (CONDA, a register this model was NOT trained on):

| metric | count | rate |
|---|---|---|
| false positives | 204/718 | 28.4% |
| false negatives | 224/680 | 32.9% |

Game chat is the **honest weakness**: this model is Wikipedia/Jigsaw-register and transfers to
Reddit-like text, **not** to gaming slang. In our experiments ~9k rows of real game chat lifted
implicit game-toxicity recall from 14% → 77% — but that data (CONDA) has no license and is *not*
in these weights (this model's diet is strictly CC0 Jigsaw + owned synthetic). If you moderate a
gaming community, fine-tune on your own domain data.

> **Note on prior revisions.** Earlier uploads of this repo reported ~2.1% false positives. That
> figure was **train-on-test inflated** — the evaluation set overlapped the training data — and the
> weights also carried an identity-term bias (benign sentences like *"there are a lot of gay people
> here"* were flagged). Both are fixed in this revision: the holdout is now excluded from training
> (so the 3.9% above is real generalization), and counterfactual augmentation drove the identity
> probe to 0/592. Numbers here are honest.

For scale: general-purpose LLM judges prompted for moderation measured far worse on the same
yardsticks at 30–70× the size (`phi3:mini`, 2.2 GB: F1 ~48 on game chat; `llama-guard3:1b`: missed
~84% of interpersonal abuse).

## Usage

```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer, pipeline

REPO = "strictlyinsecure/discord-moderation-minilm-l12"
model = ORTModelForSequenceClassification.from_pretrained(REPO, subfolder="onnx", file_name="model.onnx")
tok = AutoTokenizer.from_pretrained(REPO)
clf = pipeline("text-classification", model=model, tokenizer=tok, top_k=None, device=-1)

clf("i'm gonna destroy you in rocket league tonight lmao")   # → benign
clf("FREE NITRO for everyone, claim here bit.ly/x9k2")       # → spam
clf("shut up you idiot nobody likes you")                    # → abusive
```

Requires `pip install optimum[onnxruntime]`. A PyTorch fp32 checkpoint (`model.safetensors`) is
also included if you want to fine-tune further.

### Thresholding

The model is bimodal — it outputs ~0.99 or ~0.00 and little in between, so the threshold is not a
delicate choice. 0.85 is a good default; raise it toward 0.95 if a false positive triggers a
severe action (ban), lower it toward 0.6 if a human reviews every flag.

## Training

* 4-class head on `all-MiniLM-L12-v2`, `max_length=200`, class-weighted loss (inverse frequency —
  without it the model collapses to predicting `abusive` for everything).
* ~35k rows: stratified Jigsaw ([CC0](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge))
  + synthetic chat-register data (spam, flood, evasion, short messages, hard benign negatives),
  plus counterfactual identity augmentation (below). **CC0 + owned synthetic only — no CONDA**,
  which has no license.
* **The held-out test set is excluded from training** (a prior revision did not do this, which
  inflated its reported scores). Reported numbers are real generalization.
* **Identity-bias fix.** Jigsaw over-represents identity terms in its toxic examples, so a naive
  model flags *"i'm gay"* as abusive. Counterfactual augmentation (term-swapping within identity
  groups + both-polarity templates in contracted and expanded forms) decorrelates the term from the
  label, driving a 592-sentence identity probe to 0 false positives.
* **Length-matched sampling.** An early version learned "short message ⇒ abusive" because
  Wikipedia's toxic comments are short and its clean ones are long — it scored 97% held-out while
  classifying *"great job everyone"* as abusive. Every class is now sampled to the same length
  distribution, and a hand-written out-of-distribution suite exists to catch exactly this.
* **Label denoising.** 2,466 Jigsaw rows whose human label was confidently contradicted by an LLM
  second-annotator across the benign/abusive boundary were dropped. This measurably lowered false
  positives without hurting recall at matched operating points.

`toxicity` and `harassment` are **merged into one `abusive` class**: two annotators (Jigsaw's
humans and an LLM judge) disagreed about which bucket an abusive message belonged in 48% of the
time. That boundary is noise, and most pipelines take the same action for both.

## Limitations

* **Spam/flood scores are optimistic** — trained and evaluated on templated synthetic data. Read
  them as "learned these patterns", not "solved spam".
* **Never trained on real chat logs.** See the game-chat numbers above.
* **English only.**
* **Evasion coverage is synthetic-only** (leetspeak, homoglyphs, spacing) — a determined evader
  will get through.
* Evaluated on the author's own held-out split, not a public benchmark.

## Intended use

A **fast first-pass filter** in a moderation pipeline — cheap enough to run on every message, with
a human or a stronger model handling escalation. Not a substitute for human moderators, and not a
sound basis for automated bans on its own.

## License & attribution

Apache-2.0. See `NOTICE` for the attribution required on redistribution.

Trained on the Jigsaw Toxic Comment Classification dataset (**CC0**); underlying comment text
originates from Wikipedia and is licensed **CC-BY-SA-3.0**. Base model is Apache-2.0.
