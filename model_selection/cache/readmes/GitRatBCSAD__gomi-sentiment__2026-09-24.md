---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - text-classification
  - sentiment-analysis
  - commit-messages
  - technical-debt
  - gomi
---

# Gomi Sentiment Model

Fine-tuned **DistilBERT** (`distilbert-base-uncased`) for **commit-message sentiment** in the Gomi technical-debt risk pipeline.

Classifies short commit text into four labels:

| Label | Meaning | Risk signal in Gomi |
| ----- | ------- | ------------------- |
| `satisfaction` | Positive / constructive tone | No |
| `neutral` | Neutral tone | No |
| `caution` | Hedging, workaround, “revisit later” | Yes |
| `frustration` | Negative / stressed tone | Yes |

At runtime, Gomi aggregates per-file **sentiment score** as  
`(frustration + caution) / non–low-info commits`.

## Training

| Item | Detail |
| ---- | ------ |
| Base model | [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) |
| Training data | [GitRatBCSAD/gomi-datasets](https://huggingface.co/datasets/GitRatBCSAD/gomi-datasets) → `openreview/openreview_labeled_2k.csv` |
| Script | `scripts/train_sentiment.py` in the Gomi ML repo |

> **Prototype** — Early checkpoint. Pin a revision tag (e.g. `v1.0.0`) for reproducible runs.

## Files in this repo

| File | Description |
| ---- | ----------- |
| `config.json` | Model config (4 labels) |
| `model.safetensors` | Fine-tuned weights |
| `tokenizer.json` | Tokenizer |
| `tokenizer_config.json` | Tokenizer config |

Inference needs the files above. The `checkpoints/` folder may be present from training uploads; it is not required at runtime.

## Download

### Hugging Face CLI

```bash
pip install huggingface_hub
huggingface-cli login   # if private

hf download GitRatBCSAD/gomi-sentiment \
  --local-dir ./distilbert_sentiment \
  --revision v1.0.0
```

### Python

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

repo = "GitRatBCSAD/gomi-sentiment"
revision = "v1.0.0"  # or None for main

tokenizer = AutoTokenizer.from_pretrained(repo, revision=revision)
model = AutoModelForSequenceClassification.from_pretrained(repo, revision=revision)
```

### Git + LFS

```bash
git lfs install
git clone https://huggingface.co/GitRatBCSAD/gomi-sentiment
cd gomi-sentiment && git lfs pull
```

## Use with Gomi

In the Gomi ML project `.env`:

```bash
GOMI_SENTIMENT_MODEL_REPO=GitRatBCSAD/gomi-sentiment
GOMI_SENTIMENT_MODEL_REVISION=v1.0.0
HF_TOKEN=your_token_if_private
```

Or download into `scripts/datasets/distilbert_sentiment/` and run `gomi.py` without the env var.

Training data lives in [gomi-datasets](https://huggingface.co/datasets/GitRatBCSAD/gomi-datasets), not in this repo.

## Related repos

| Repo | Role |
| ---- | ---- |
| [gomi-datasets](https://huggingface.co/datasets/GitRatBCSAD/gomi-datasets) | CSV / JIT training data |
| [gomi-risk](https://huggingface.co/GitRatBCSAD/gomi-risk) | Logistic regression + SHAP background |

## License

Apache 2.0. Respect licenses of `distilbert-base-uncased` and the OpenReview training data when redistributing.
