---
base_model: answerdotai/ModernBERT-base
base_model_relation: finetune
datasets:
- nyu-mll/glue
license: apache-2.0
language:
- en
pipeline_tag: text-classification
library_name: transformers
widget:
- text: This movie was absolutely wonderful, a joy from start to finish.
- text: The plot was a mess and the acting felt phoned in.
- text: Support resolved my issue in minutes — genuinely impressed.
tags:
- sentiment-analysis
- sentiment
- text-classification
- sst-2
- sst2
- modernbert
- reviews
- english
- positive-negative
- distilbert-sst2-alternative
---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ankit-aglawe/parable-assets/main/sensible_header_dark.png">
  <img alt="Sensible" src="https://raw.githubusercontent.com/ankit-aglawe/parable-assets/main/sensible_header.png">
</picture>

# 🦉 Sensible — ModernBERT Sentiment Analysis

### The modern replacement for the classic SST-2 sentiment model — **0.946 vs 0.913** on the exact same benchmark, one `pipeline()` line.

```python
from transformers import pipeline

clf = pipeline("text-classification", model="AnkitAI/Sensible-ModernBERT-Sentiment-Analysis")
clf("This movie was absolutely wonderful!")
# [{'label': 'positive', 'score': 0.99}]
```

**positive / negative** for reviews, comments, feedback, social text. Built on [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) — Flash-Attention-fast, 149M params, CPU-friendly.

---

## Benchmarks

SST-2 official validation set (872 examples) — the same split every SST-2 model reports on:

| Model | Accuracy |
|---|---|
| 💬 **This model** | **0.9461** |
| distilbert-base-uncased-finetuned-sst-2-english (the 3.9M-downloads/month default) | 0.9130 |

**+3.3 points over the model most pipelines still default to** — from an encoder released five years later. Training script and raw eval outputs ship in this repo; the reported split was never used for training or checkpoint selection.

## Labels

| id | label |
|---|---|
| 0 | negative |
| 1 | positive |

**Batch scoring:**

```python
texts = ["Best purchase I've made all year.",
         "Waited 40 minutes and the order was still wrong."]
for t, r in zip(texts, clf(texts, batch_size=64)):
    print(f"{r['label']:<9} {r['score']:.2f}  {t}")
```

## Built for

- **Product & review analytics** — score feedback streams at scale
- **Social/comment moderation dashboards** — fast, CPU-deployable
- **Drop-in upgrade** — same task and label semantics as the distilbert-sst2 default your stack probably uses

## Good to know

- Two classes only (no neutral) — SST-2 convention; genuinely neutral text gets forced to a side
- English, sentence/short-paragraph level
- Trained on movie-review sentences (SST-2); transfers well to general reviews/comments, less so to domain jargon — for financial text use [FinSense](https://huggingface.co/AnkitAI/FinSense-ModernBERT-Financial-News-Sentiment-Analysis)

## Training details

Full fine-tune of ModernBERT-base on SST-2 (GLUE, 67k sentences): 2 epochs, lr 2e-5, batch 32, fp32, best checkpoint by held-back 5% of train — the official validation set stayed untouched until final reporting.

## Support the Project

If this model is useful in your work, you can support independent research:

<p align="left">
  <a href="https://www.buymeacoffee.com/AnkitAI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" height="60" width="217" /></a>
</p>

## Citation

```bibtex
@misc{sensiblesentiment2026,
  author = {Aglawe, Ankit},
  title = {Sensible: ModernBERT Sentiment Analysis},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/AnkitAI/Sensible-ModernBERT-Sentiment-Analysis}
}
```

## Base & license

**Apache-2.0** ([ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base), Answer.AI). Trained on [SST-2](https://huggingface.co/datasets/nyu-mll/glue) (Socher et al., 2013 / GLUE).

## More from AnkitAI

| Model | Task | Score |
|---|---|---|
| [FinSense ModernBERT](https://huggingface.co/AnkitAI/FinSense-ModernBERT-Financial-News-Sentiment-Analysis) | financial news sentiment (3-class) | 0.8675 |
| [FinSense distilbert v2](https://huggingface.co/AnkitAI/distilbert-base-uncased-financial-news-sentiment-analysis) | financial news sentiment, tiny | 0.8447 |
| [Parable](https://huggingface.co/collections/AnkitAI/parable-6a4fac60f4b35afca3019621) | local agent LLMs (GGUF) | — |

## Version history

- **v1** (2026-07-20) — initial release: ModernBERT-base, SST-2, seed 42.

More on the Sensible models: [ankitaglawe.com/sensible](https://ankitaglawe.com/sensible)
