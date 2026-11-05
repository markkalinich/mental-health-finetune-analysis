---
license: apache-2.0
language:
- nso
base_model: distilbert-base-uncased
library_name: transformers
pipeline_tag: text-classification
tags:
- sepedi
- sesotho-sa-leboa
- northern-sotho
- south-africa
- low-resource
- sentiment-analysis
- cross-lingual
- distilbert
---

# distilbert-crosslingual-sentiment — Sepedi 3-class sentiment (cross-lingual)

DistilBERT fine-tuned for 3-class Sepedi (Sesotho sa Leboa) sentiment classification by **Sediba AI**.

## What is actually in this repo

Read from `config.json` in this repository:

| | |
|---|---|
| Architecture | `DistilBertForSequenceClassification` |
| Labels | 3 — `0: negative`, `1: neutral`, `2: positive` |
| Problem type | `single_label_classification` |
| Hidden size / layers | 768 / 6 |
| Vocab size | 30,522 (stock DistilBERT English) |
| Weights | ~255 MB (`model.safetensors`, fp32) |

## Evaluation — reported honestly

Held-out Sepedi sample, n=300, balanced 100 negative / 100 neutral / 100 positive
(SAfriSenti-Corpus-Mini `sepedi_sample_300`). Metric is **weighted F1**, 3-class.

| Model | Weighted F1 |
|---|---|
| Zero-shot baseline (no fine-tuning) | 0.2305 |
| **This model** (DistilBERT cross-lingual, Sepedi+Sesotho+Setswana) | **0.6144** |
| zabantu + LoRA adapter | 0.3793 |

**This is the strongest Sepedi sentiment result in the Sediba vault — about 1.6× the zabantu
adapter's 0.3793.** It is published here for the first time because the weaker adapter was
previously the only public variant. The headline finding: **cross-lingual transfer across the
three related Sotho-Tswana languages outperforms single-language adaptation.**

**Provenance:** `research_steps/step5_crosslingual_train.py`, scored to
`results/step5_results.json` in the Sediba vault.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification",
               model="Sediba-AI/distilbert-crosslingual-sentiment")
clf("Ke rata thuto ye kudu.")
# -> [{'label': 'positive', 'score': ...}]
```

Labels map as `0 → negative`, `1 → neutral`, `2 → positive`. There is **no** `__max_length__
sentiment` — use `num_labels=3` if loading directly.

## Limitations — read before using

- **n=300 is small.** Confidence intervals on a balanced 3-class task at this size are wide;
  treat the ranking as indicative, not settled.
- **No per-class F1 reported in this card.** The baseline's classification report shows neutral
  is the hardest class (F1 0.00 in zero-shot). Per-class breakdown for this model is not
  available — request it if you need it.
- **Stock English tokenizer.** The 30,522-token DistilBERT vocabulary is English; Sepedi
  fragments into more sub-words than necessary.
- **Final checkpoint, not best.** Training recorded no per-epoch validation
  (`best_metric: None` in `trainer_state.json`), so checkpoint-204 is the final state at
  epoch 3.0, not a selected best.
- **Dialect coverage unmeasured.** Sepedi varies substantially across the five Sediba zones.
- **Sentiment is culturally situated.** Labels inherited from English-language sentiment
  conventions may not reflect Sepedi expression.
- **No safety tuning.**

## Out of scope

Content moderation, hiring, lending, health, or any decision affecting a person's interests.

## Sediba Sepedi model family

| Model | Type | Use | Status |
|---|---|---|---|
| **[Sedibaai/SedibaLM](https://huggingface.co/Sedibaai/SedibaLM)** | Generative (Qwen2.5-1.5B + QLoRA) | Sepedi text generation, chat | **Shipped — validated vs base** |
| **distilbert-crosslingual-sentiment** (this repo) | 3-class classifier | Sepedi sentiment | **Shipped — F1 0.6144, best in vault** |
| **[Sediba-AI/zabantu-nso-sentiment](https://huggingface.co/Sediba-AI/zabantu-nso-sentiment)** | LoRA adapter, 3-class | Sepedi sentiment | Shipped — F1 0.3793 |
| **[Sediba-AI/xlmr-sepedi](https://huggingface.co/Sediba-AI/xlmr-sepedi)** | Masked LM | Fill-mask, NLU encoder | Shipped |

## Licence

**Apache 2.0** for these weights, inheriting from distilbert-base-uncased upstream.

Evaluation data is SAfriSenti-Corpus-Mini, under its own terms. Sediba corpus material is
governed separately (NOODL, in legal review).

## About

Built by **Sediba AI** — sovereign AI for South African languages, starting with Sepedi
(~4.7 million speakers).
