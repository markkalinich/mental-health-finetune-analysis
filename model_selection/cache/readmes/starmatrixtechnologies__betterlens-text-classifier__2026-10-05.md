---
language:
- en
license: mit
tags:
- text-classification
- sentiment-analysis
- multi-task
- distilbert
- onnx
- betterlens
- starmatrix
base_model: distilbert-base-uncased
library_name: transformers
pipeline_tag: text-classification
---

# BetterLens Text Classifier (Star Matrix Technologies)

A **dual-head DistilBERT text classifier** that, in a single forward pass,
labels a short piece of text for **sentiment** and scores it for **vagueness** —
how specific vs. diffuse its content is.

- **Sentiment head** (primary): 3-class classification — `positive` / `neutral` / `negative`
- **Vagueness head** (secondary): regression score in `[0, 1]` (0 = specific, 1 = vague/diffuse)

The two signals compose into BetterLens's core rule for feed filtering — *act on
a post only when it is both negative AND vague* — but each head is independently
useful for any short-text classification pipeline.

> This model uses a **custom architecture** (`trust_remote_code=True` required)
> because it has two heads. The custom code is small and fully visible in this
> repo (`modeling_betterlens_dual_head.py`, `configuration_betterlens_dual_head.py`).
> An ONNX export is included for browser / on-device / edge use.

## Try it

🕶️ **[Live in-browser demo → huggingface.co/spaces/starmatrixtechnologies/betterlens-text-classifier-demo](https://huggingface.co/spaces/starmatrixtechnologies/betterlens-text-classifier-demo)** —
paste a single post or upload a CSV batch (with optional `expected_label` to
score accuracy). Runs client-side via ONNX Runtime Web; no data leaves your machine.

## Architecture

![BetterLens Text Classifier architecture](architecture.png)

- Backbone: `distilbert-base-uncased` (FP32 weights, `model.safetensors`)
- Pooling: `[CLS]` token
- Heads (after shared Dropout 0.1):
  - `sentiment_head`: `Linear(768 → 3)` → logits
  - `vagueness_head`: `Linear(768 → 1)` → logit, sigmoid at inference
- Max sequence length: **128 tokens**
- Trained with combined loss `0.6·CE(sentiment) + 0.4·MSE(vagueness)`

## Use cases

The two heads compose into BetterLens's core feed rule — *hide a post when it is
both negative AND vague* — but each head is independently useful.

![BetterLens feed filter decision flow](filter-flow.png)

| Use case | How the model is used |
|---|---|
| **Feed filtering** | Rank/hide posts that are *negative and vague* ("something's wrong with everything") instead of *specific and negative* ("this update broke my build") — the latter is actionable feedback and stays visible. |
| **Comment-moderation triage** | Score a queue of comments: high negative + high vagueness = low-value noise, auto-demote; specific complaints go to humans first. |
| **Feedback routing** | Route product feedback by sentiment, and flag vague complaints for follow-up questions instead of dismissing them. |
| **Brand / community monitoring** | Continuous sentiment + vagueness signal over streams: a spike in vague negativity is an early warning that is easier to spot than raw negative counts. |
| **Research / scoring** | General short-text classification with an extra "specificity" axis for any NLP pipeline. |

## Results

### Sentiment (held-out test split, 13,000 samples — verified 2026-09-19)

| Metric | Value |
|---|---|
| Accuracy | **82.7%** |
| F1 (macro) | 82.6% |

Per-class (rows = true, `P` = precision, `R` = recall):

| Class | Support | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| positive | 4,030 | 0.881 | 0.955 | 0.916 |
| neutral | 4,923 | 0.798 | 0.820 | 0.809 |
| negative | 4,047 | 0.801 | 0.708 | 0.751 |

Negative is the weakest class — it's the boundary where diffuse / low-intensity
negativity gets absorbed into neutral. That is exactly the regime the vagueness
head is designed to disambiguate (see Limitations).

Confusion matrix (rows = true, cols = predicted; order: positive/neutral/negative):

```
              positive  neutral  negative
positive        3847      73      110
neutral          284     4037      602
negative         236      947     2864
```

### Vagueness (same split)

| Metric | Value |
|---|---|
| MAE | 0.061 |
| R² | 0.676 |

### Latency (CPU, single post)

~19 ms FP32 ONNX (see `benchmark_results.json`).

## Usage

### Python (transformers, `trust_remote_code`)

```python
import torch
from transformers import AutoModel, AutoTokenizer

MODEL = "starmatrixtechnologies/betterlens-text-classifier"
tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL, trust_remote_code=True)
model.eval()

text = "Something about this whole situation just feels off lately."
enc = tok(text, return_tensors="pt", max_length=128,
          padding="max_length", truncation=True)
with torch.no_grad():
    out = model(**enc)

names = ["positive", "neutral", "negative"]
probs = torch.softmax(out.sentiment_logits, dim=-1)[0]
print({n: round(float(p), 3) for n, p in zip(names, probs)})
print("vagueness:", round(float(out.vagueness_score[0, 0]), 3))
```

`modeling_betterlens_dual_head.py` is the custom model class;
`loading_utils.py` wraps the load+predict loop for convenience.

### ONNX (browser / on-device / edge)

Included at [`onnx/model.onnx`](onnx/model.onnx) (~253 MB, FP32, opset 14).

- Inputs: `input_ids` `[batch, 128]` int64, `attention_mask` `[batch, 128]` int64
- Outputs:
  - `sentiment_logits` `[batch, 3]` — softmax over `[positive, neutral, negative]`
  - `vagueness_score` `[batch, 1]` — already sigmoided, in `[0, 1]`

```python
import onnxruntime as ort
sess = ort.InferenceSession("onnx/model.onnx")
# ... tokenize (DistilBERT WordPiece, max_length=128, pad to 128) ...
sent, vag = sess.run(None, {"input_ids": ids, "attention_mask": mask})
```

A live, in-browser demo that runs this ONNX model on the client (no server) is
available at
[huggingface.co/spaces/starmatrixtechnologies/betterlens-text-classifier-demo](https://huggingface.co/spaces/starmatrixtechnologies/betterlens-text-classifier-demo)
(paste text or upload a CSV batch).

## Label order

**`sentiment_logits` columns are `[positive, neutral, negative]`** (index
0/1/2) — matching the training CSVs (label 0/1/2).

## Training data

Built from public HF short-text corpora, relabeled into the 3-class scheme
(0=positive, 1=neutral, 2=negative) with a derived `vague_score` in `[0,1]`:

- **Civil Comments (graded toxicity)** — toxicity ≥0.15 → negative, <0.15 → neutral
- **Yelp reviews** — star ratings → positive/neutral/negative
- **SetFit `toxic_conversations`** — overt toxicity → negative
- **Synthetic "vaguepost" examples** — generated across the vagueness spectrum
  (concrete → abstract/filler) with hand-tuned `vague_score` targets

Vagueness is a derived heuristic signal (hedging words, generic nouns,
abstract sentiment without a referent, filler phrases), not a human annotation —
treat the `[0,1]` score as a soft prior, not a ground-truth measure.

## Limitations

- Dual-head models need `trust_remote_code=True` (weights + custom code are
  yours to audit in this repo).
- **Negative recall is the weak spot (0.708)** — diffuse, low-intensity
  negativity gets absorbed into neutral. The vagueness head helps disambiguate
  exactly this regime, but it is a heuristic-derived score, not a human label,
  so it should be treated as a soft prior.
- 128-token context only (short-form text: posts, comments, reviews).
- Trained on English social/review text; expect degradation on out-of-domain
  language, sarcasm, multilingual, or highly niche technical content.

## License

MIT (code & weights). Base model `distilbert-base-uncased` is Apache-2.0.

## Project

Built by **Star Matrix Technologies**. Part of the BetterLens on-device
text-classification / feed-filtering stack.
