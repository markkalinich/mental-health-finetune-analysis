---
license: apache-2.0
language:
- nso
base_model: FacebookAI/xlm-roberta-base
library_name: transformers
pipeline_tag: text-classification
tags:
- sepedi
- sesotho-sa-leboa
- northern-sotho
- south-africa
- low-resource
- sentiment-analysis
- xlm-roberta
---

# xlmr-sepedi-sentiment — Sepedi binary sentiment classifier

XLM-RoBERTa-base fine-tuned for **binary sentiment classification** on Sepedi
(Sesotho sa Leboa) text, by **Sediba AI**.

## What is actually in this repo

Read from `config.json` in this repository:

| | |
|---|---|
| Architecture | `XLMRobertaForSequenceClassification` |
| Labels | 2 — `0: negative`, `1: positive` |
| Problem type | `single_label_classification` |
| Hidden size / layers | 768 / 12 |
| Vocab size | 250,002 (stock XLM-R multilingual) |
| Weights | 1.11 GB (`model.safetensors`, fp32) |

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Sediba-AI/xlmr-sepedi-sentiment")
clf("Ke rata thuto ye kudu.")
# -> [{'label': 'positive', 'score': ...}]
```

Labels map as `0 → negative`, `1 → positive`.

## Limitations — read before using

- **⚠️ No published evaluation. This is the most important caveat.** No accuracy, F1, precision
  or recall figures were recorded at publication time, and no test set is documented in this
  card. **Do not deploy this in anything consequential without evaluating it on your own
  labelled Sepedi data first.**
- **Binary only.** No neutral class. Genuinely neutral Sepedi text will be forced into positive
  or negative, which is frequently the wrong answer for factual or informational sentences.
- **Stock multilingual tokenizer.** The 250,002-token XLM-R vocabulary is not Sepedi-optimised.
- **Dialect coverage undocumented.** Sepedi has substantial dialectal variation across the five
  Sediba zones; per-dialect performance is unmeasured.
- **Training data not documented in this card.** Size, sourcing and label provenance are held in
  the Sediba vault; no formal data-licence audit has been completed.
- **Sentiment is culturally situated.** Labels transferred from English-language sentiment
  conventions may not reflect how sentiment is expressed in Sepedi.

## Intended use

- Research on low-resource African-language sentiment
- A baseline to beat, not a production classifier
- Exploratory analysis where errors are cheap and reviewable

## Out of scope

Content moderation, hiring, lending, health, or any decision affecting a person's interests.
An unevaluated binary classifier must not sit in such a path.

## Sediba Sepedi model family

| Model | Type | Use | Status |
|---|---|---|---|
| **[Sedibaai/SedibaLM](https://huggingface.co/Sedibaai/SedibaLM)** | Generative (Qwen2.5-1.5B + QLoRA) | Sepedi text generation, chat | **Shipped — validated vs base** |
| **[xlmr-sepedi](https://huggingface.co/Sediba-AI/xlmr-sepedi)** | Masked LM | Fill-mask, NLU encoder | Shipped — unevaluated |
| **xlmr-sepedi-sentiment** (this repo) | Binary classifier | Sepedi sentiment | Shipped — unevaluated |
| **[sepedi-sentiment-classifier](https://huggingface.co/Sediba-AI/sepedi-sentiment-classifier)** | Classifier | Sepedi sentiment | Shipped |

## Licence

**Apache 2.0** for these weights, inheriting from XLM-RoBERTa-base upstream.

Training data and labels are **not** released under this licence — Sediba corpus material is
governed separately (NOODL, in legal review). Open weights, restricted corpus.

## About

Built by **Sediba AI** — sovereign AI for South African languages, starting with Sepedi
(~4.7 million speakers).
