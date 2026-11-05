---
base_model: distilbert/distilbert-base-uncased
base_model_relation: finetune
datasets:
- takala/financial_phrasebank
license: apache-2.0
language:
- en
pipeline_tag: text-classification
library_name: transformers
widget:
- text: The company's quarterly earnings surpassed all estimates, indicating strong growth.
- text: Operating profit fell to EUR 35.4 mn from EUR 68.8 mn.
- text: The annual general meeting will be held on April 12.
tags:
- financial-sentiment-analysis
- sentiment-analysis
- financial-news
- finance
- stocks
- trading
- distilbert
- finbert-alternative
- text-classification
- sentiment
- fintech
- news
---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ankit-aglawe/parable-assets/main/finsense_header_dark.png">
  <img alt="FinSense" src="https://raw.githubusercontent.com/ankit-aglawe/parable-assets/main/finsense_header.png">
</picture>

# 🐂 FinSense distilbert **v2** — financial news sentiment, tiny and fast

### v2 — retrained on a cleaner recipe with a published split. Same 67M-parameter speed your pipelines already rely on, more accurate than v1 on a properly held-out benchmark.

```python
from transformers import pipeline

clf = pipeline("text-classification", model="AnkitAI/distilbert-base-uncased-financial-news-sentiment-analysis")
clf("The company's quarterly earnings surpassed all estimates.")
# [{'label': 'positive', 'score': 0.99}]
```

**positive / neutral / negative** for headlines, news wires, analyst sentences. Built on [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) — Flash-Attention-fast, 149M params, runs happily on CPU.

---

## Benchmarks

Financial PhraseBank (the standard benchmark for this task), held-out test set, identical harness for every row:

| Model | Accuracy | Macro-F1 |
|---|---|---|
| 🐂 **This model (v2)** | **0.8447** | **0.8316** |
| v1 (previous weights) | 0.8323 | 0.8064 |
| ProsusAI/finbert¹ | 0.8799 | 0.8761 |

**+1.2 accuracy / +2.5 F1 over v1**, at a third of FinBERT's size. We do not claim to beat FinBERT: it scores higher on this table, having been trained on effectively the whole corpus this split comes from.¹ Want maximum accuracy? The [ModernBERT flagship](https://huggingface.co/AnkitAI/FinSense-ModernBERT-Financial-News-Sentiment-Analysis) scores 0.8675.

<sub>¹ Measured by us on the identical split — not quoted from another paper. FinBERT was trained on effectively all of Financial PhraseBank, so its score here reflects memorisation of the corpus rather than generalisation; a fair comparison needs data neither model has seen. A previous version of this card reported FinBERT at 0.8423/0.8439 citing an independent replication that could not be verified; both the number and the claim resting on it have been removed.</sub>

## Labels

| id | label | example |
|---|---|---|
| 0 | negative | "Operating profit fell to EUR 35.4 mn from EUR 68.8 mn." |
| 1 | neutral | "The annual general meeting will be held on April 12." |
| 2 | positive | "Quarterly earnings surpassed all estimates." |

**Batch scoring** (thousands of headlines):

```python
headlines = ["Shares jumped 8% after the guidance raise.",
             "The company filed its annual report on Thursday.",
             "Regulators fined the bank EUR 20 mn."]
for h, r in zip(headlines, clf(headlines, batch_size=32)):
    print(f"{r['label']:<9} {r['score']:.2f}  {h}")
```

## Built for

- **Trading & research pipelines** — score news flow at scale (fast batch inference, CPU-friendly)
- **Fintech products** — sentiment tags for news feeds, alerts, dashboards
- **Quant & academic work** — reproducible split + eval script included, cite with confidence

## Good to know

- Tuned for financial *news* register — tweets and Reddit are a different dialect
- English, sentence-level, three classes
- Errors concentrate on positive-vs-neutral — the same boundary human annotators disagree on 25% of the time (structural ceiling of this task, affects every model including FinBERT)

## Training details

Full fine-tune of distilbert-base-uncased on Financial PhraseBank (`sentences_50agree`, 4,846 expert-annotated sentences): 5 epochs, lr 2e-5, batch 16, max length 128, fp32, best checkpoint by validation macro-F1. Stratified 80/10/10 split with a fixed, published seed — the split script and raw evaluation outputs are in this repo, so every number above is reproducible end-to-end.

## Support the Project

If this model is useful in your work, you can support independent research:

<p align="left">
  <a href="https://www.buymeacoffee.com/AnkitAI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" height="60" width="217" /></a>
</p>

## Citation

```bibtex
@misc{finsense2026,
  author = {Aglawe, Ankit},
  title = {FinSense: Financial News Sentiment Models},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/AnkitAI/FinSense-ModernBERT-Financial-News-Sentiment-Analysis}
}
```

## Base & license

**Apache-2.0** weights ([ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base), Answer.AI). Trained on [Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank) (Malo et al., 2014 — CC BY-NC-SA; commercial users, check dataset terms).

## The FinSense family

| Model | Size | Accuracy | Pick it for |
|---|---|---|---|
| [FinSense ModernBERT](https://huggingface.co/AnkitAI/FinSense-ModernBERT-Financial-News-Sentiment-Analysis) | 149M | **0.8675** | best accuracy, modern stack |
| **This model (v2)** | 67M | 0.8447 | smallest & fastest |

More sizes and a multilingual variant are on the roadmap. Sibling series: [Parable](https://huggingface.co/collections/AnkitAI/parable-6a4fac60f4b35afca3019621) — local agent LLMs from the same maker.

## Version history

- **v2** (2026-07-17) — this release, in place: cleaner recipe, published stratified split (seed 42), honest held-out benchmark. Same labels, same API — drop-in for v1 users.
- **v1** (2024-11) — original release (0.9669 self-reported on the small allagree subset — not comparable to the held-out 50agree numbers above). Preserved in revision history.

More on the FinSense models: [ankitaglawe.com/finsense](https://ankitaglawe.com/finsense)
