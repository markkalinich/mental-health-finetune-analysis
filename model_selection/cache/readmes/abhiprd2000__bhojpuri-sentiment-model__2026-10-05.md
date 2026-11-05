---
language:
- bho
- en
- bh
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- bhojpuri
- devanagari
- low-resource-nlp
- cross-lingual-transfer
metrics:
- accuracy
- f1
---

# Bhojpuri Sentiment Analysis Model

**Author:** Abhimanyu Prasad | [@abhiprd20](https://huggingface.co/abhiprd20)

Fine-tuned XLM-RoBERTa model for 3-class sentiment analysis on Bhojpuri text in Devanagari script. This is the first publicly available sentiment model for the Bhojpuri language.

---

## Model Description

This model is part of a cross-lingual transfer study comparing sentiment analysis across English, Hindi, Maithili, and Bhojpuri — four languages spanning high-resource to extremely low-resource.

**Base model:** `cardiffnlp/twitter-xlm-roberta-base-sentiment`

**Task:** 3-class sentiment classification — Positive, Negative, Neutral

**Language:** Bhojpuri (भोजपुरी) — Devanagari script

**Training data:** 18,049 unique Bhojpuri sentences (balanced across 3 classes)

---

## Performance

| Model | Accuracy | F1 (Macro) |
|-------|----------|------------|
| English BERT (zero-shot) | 33.13% | 0.1659 |
| XLM-RoBERTa (zero-shot) | 76.45% | 0.7630 |
| mBERT (fine-tuned) | 94.81% | 0.9481 |
| **XLM-RoBERTa (fine-tuned) ← this model** | **97.60%** | **0.9761** |
| Out-of-distribution (30 new sentences) | 70.00% | 0.6777 |

Evaluated on a fixed balanced test set of 501 sentences (167 per class).

---

## Cross-Lingual Findings

The zero-shot results reveal a clear pattern: English BERT fails on all three Indic languages at nearly identical rates (~33%), while multilingual models recover significantly, with Bhojpuri showing the strongest zero-shot transfer (76.45%) — likely due to its closer lexical proximity to Hindi compared to Maithili.

| Language | English Zero-Shot | XLM Zero-Shot | Fine-tuned |
|----------|-------------------|---------------|------------|
| Maithili | 33.33% | 69.86% | 85.63% |
| **Bhojpuri** | **33.13%** | **76.45%** | **97.60%** |

---

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="abhiprd20/bhojpuri-sentiment-model"
)

# Example Bhojpuri sentences
texts = [
    "ई खाना बहुत स्वादिष्ट बा।",       # positive
    "आज बहुत थकान लागत बा।",            # negative
    "हम कल पटना जाइब।",                 # neutral
]

for text in texts:
    result = classifier(text)[0]
    print(f"{text}")
    print(f"  → {result['label']} ({result['score']*100:.1f}%)\n")
```

**Output:**
```
ई खाना बहुत स्वादिष्ट बा।
  → positive (97.2%)

आज बहुत थकान लागत बा।
  → negative (95.8%)

हम कल पटना जाइब।
  → neutral (91.4%)
```

---

## Labels

| Label | Integer | Meaning |
|-------|---------|---------|
| negative | 0 | Negative sentiment |
| neutral | 1 | Neutral / factual |
| positive | 2 | Positive sentiment |

---

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | cardiffnlp/twitter-xlm-roberta-base-sentiment |
| Epochs | 3 |
| Batch size | 16 |
| Max sequence length | 128 |
| Warmup steps | 200 |
| Weight decay | 0.01 |
| Mixed precision | fp16 |
| Best model metric | F1 macro |

---

## Dataset

Training data: 18,049 unique Bhojpuri sentences in Devanagari script with balanced 3-class sentiment labels. Note: Dataset contains translated content from English, acknowledged as a limitation.

Test set: Fixed balanced set of 501 sentences (167 per class), held out before training with zero leakage verified.

---


## Related Models

- [`abhiprd20/nlp-sentiment-model`](https://huggingface.co/abhiprd20/nlp-sentiment-model) — English baseline
- [`abhiprd20/maithili-sentiment-model`](https://huggingface.co/abhiprd20/maithili-sentiment-model) — Maithili
- [`abhiprd20/hindi-sentiment-model`](https://huggingface.co/abhiprd20/hindi-sentiment-model) — Hindi

---

## Citation

If you use this model, please cite:

```
@misc{prasad2026bhojpuri,
  author    = {Abhimanyu Prasad},
  title     = {Bhojpuri Sentiment Analysis: Cross-Lingual Transfer Study},
  year      = {2026},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/abhiprd20/bhojpuri-sentiment-model}
}
```

---

## 📊 Cross-Language Evaluation

Each model was evaluated on all 4 languages (300 sentences per language, 100 per class).
This shows how well models trained on one language transfer to others.

### Accuracy Matrix

| Model | English | Hindi | Maithili | Bhojpuri |
|---|---|---|---|---|
| **English model** | **79.5%** ✓ | 34.0% | 33.3% | 33.0% |
| **Hindi model** | 60.0% | **68.0%** ✓ | 63.3% | 61.7% |
| **Maithili model** | 63.0% | 59.0% | **90.3%** ✓ | 75.0% |
| ⭐ **Bhojpuri model** _(this model)_ | 59.0% | 47.3% | 47.3% | **98.0%** ✓ |

### F1 Matrix (macro)

| Model | English | Hindi | Maithili | Bhojpuri |
|---|---|---|---|---|
| **English model** | **0.5424** ✓ | 0.1912 | 0.1667 | 0.1654 |
| **Hindi model** | 0.4362 | **0.6778** ✓ | 0.6319 | 0.6042 |
| **Maithili model** | 0.4443 | 0.5757 | **0.9035** ✓ | 0.7458 |
| ⭐ **Bhojpuri model** _(this model)_ | 0.4250 | 0.4166 | 0.4114 | **0.9801** ✓ |

### Key Findings

- Excellent in-language performance (**98%**) but weak cross-lingual transfer.
- Bhojpuri → Maithili transfer is only **47.3%**, worse than the reverse direction (Maithili → Bhojpuri: 75%).
- **Asymmetric transfer** between Maithili and Bhojpuri is a key finding of this research — despite linguistic similarity, transfer is not bidirectional.

> **Full paper:** This cross-evaluation is part of a research study on cross-lingual transfer for low-resource Bihari languages. See the companion datasets and models: [Maithili](https://huggingface.co/abhiprd20/maithili-sentiment-model) | [Bhojpuri](https://huggingface.co/abhiprd20/bhojpuri-sentiment-model) | [Hindi](https://huggingface.co/abhiprd20/hindi-sentiment-model) | [English](https://huggingface.co/abhiprd20/nlp-sentiment-model)
