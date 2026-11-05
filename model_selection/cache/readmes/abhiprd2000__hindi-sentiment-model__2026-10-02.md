---
language:
- hi
- en
license: apache-2.0
tags:
- sentiment-analysis
- text-classification
- hindi
- devanagari
- indic-nlp
- cross-lingual-transfer
metrics:
- accuracy
- f1
datasets:
- iam-tsr/hindi-sentiments
---

# Hindi Sentiment Analysis Model

**Author:** Abhimanyu Prasad | [@abhiprd20](https://huggingface.co/abhiprd20)

Fine-tuned XLM-RoBERTa model for 3-class sentiment analysis on Hindi text in Devanagari script, trained as part of a cross-lingual transfer study across English, Hindi, Maithili, and Bhojpuri.

---

## Model Description

This model is part of a cross-lingual transfer study examining how well NLP models transfer across languages of varying resource levels — from high-resource English to extremely low-resource Maithili and Bhojpuri.

Hindi serves as the pivot language in this study: it is the highest-resource of the three Indic languages, pre-trained into XLM-RoBERTa, and linguistically related to both Maithili and Bhojpuri. Comparing Hindi results against Maithili and Bhojpuri reveals how linguistic proximity and resource availability interact in cross-lingual transfer.

**Base model:** `cardiffnlp/twitter-xlm-roberta-base-sentiment`

**Task:** 3-class sentiment classification — Positive, Negative, Neutral

**Language:** Hindi (हिन्दी) — Devanagari script

**Training data:** 20,000 sentences (balanced, sampled from iam-tsr/hindi-sentiments)

**Training dataset citation:** [iam-tsr/hindi-sentiments](https://huggingface.co/datasets/iam-tsr/hindi-sentiments) — MIT License

---

## Performance

| Model | Accuracy | F1 (Macro) |
|-------|----------|------------|
| English BERT (zero-shot) | 35.33% | 0.2263 |
| XLM-RoBERTa (zero-shot) | 63.07% | 0.6339 |
| mBERT (fine-tuned) | 67.86% | 0.6778 |
| **XLM-RoBERTa (fine-tuned) ← this model** | **70.66%** | **0.7063** |
| Out-of-distribution (30 new sentences) | **90.00%** | **0.9017** |

Evaluated on a fixed balanced test set of 501 sentences (167 per class).

---

## Notable Finding — OOD Generalisation

Hindi shows an unusual pattern compared to Maithili and Bhojpuri: lower in-distribution accuracy (70.66%) but significantly higher out-of-distribution accuracy (90.00%). This suggests the model generalises better to naturally written Hindi despite being trained on translated data.

| Language | Fine-tuned (in-dist) | OOD (real-world) |
|----------|--------------------|------------------|
| Hindi | 70.66% | **90.00%** |
| Bhojpuri | 97.60% | 70.00% |
| Maithili | 85.63% | 64.00% |

---

## Cross-Lingual Comparison

| Language | English Zero-Shot | XLM Zero-Shot | Fine-tuned |
|----------|-------------------|---------------|------------|
| Hindi | 35.33% | 63.07% | 70.66% |
| Maithili | 33.33% | 69.86% | 85.63% |
| Bhojpuri | 33.13% | 76.45% | 97.60% |

English BERT drops to ~33-35% across all three Indic languages, confirming the language barrier. XLM-RoBERTa recovers substantially in all cases due to multilingual pretraining on Devanagari script.

---

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="abhiprd20/hindi-sentiment-model"
)

# Example Hindi sentences
texts = [
    "यह खाना बहुत स्वादिष्ट है।",        # positive
    "आज बहुत थकान महसूस हो रही है।",      # negative
    "मैं कल दिल्ली जाऊंगा।",             # neutral
]

for text in texts:
    result = classifier(text)[0]
    print(f"{text}")
    print(f"  → {result['label']} ({result['score']*100:.1f}%)\n")
```

**Output:**
```
यह खाना बहुत स्वादिष्ट है।
  → positive (94.3%)

आज बहुत थकान महसूस हो रही है।
  → negative (91.7%)

मैं कल दिल्ली जाऊंगा।
  → neutral (88.5%)
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
| Training samples | 20,000 (balanced, ~6,666 per class) |
| Epochs | 3 |
| Batch size | 16 |
| Max sequence length | 128 |
| Warmup steps | 200 |
| Weight decay | 0.01 |
| Mixed precision | fp16 |
| Best model metric | F1 macro |

---

## Dataset

Training data sampled from [iam-tsr/hindi-sentiments](https://huggingface.co/datasets/iam-tsr/hindi-sentiments) (MIT License) — 127,000 Hindi sentences translated from English social media text with 3-class sentiment labels. 20,000 balanced rows used for training.

Test set: Fixed balanced set of 501 sentences (167 per class), held out before training with zero leakage verified by assertion.


---

## Related Models

- [`abhiprd20/nlp-sentiment-model`](https://huggingface.co/abhiprd20/nlp-sentiment-model) — English baseline
- [`abhiprd20/maithili-sentiment-model`](https://huggingface.co/abhiprd20/maithili-sentiment-model) — Maithili
- [`abhiprd20/bhojpuri-sentiment-model`](https://huggingface.co/abhiprd20/bhojpuri-sentiment-model) — Bhojpuri

---

## Citation

If you use this model, please cite:

```
@misc{prasad2026hindi,
  author    = {Abhimanyu Prasad},
  title     = {Hindi Sentiment Analysis: Cross-Lingual Transfer Study},
  year      = {2026},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/abhiprd20/hindi-sentiment-model}
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
| ⭐ **Hindi model** _(this model)_ | 60.0% | **68.0%** ✓ | 63.3% | 61.7% |
| **Maithili model** | 63.0% | 59.0% | **90.3%** ✓ | 75.0% |
| **Bhojpuri model** | 59.0% | 47.3% | 47.3% | **98.0%** ✓ |

### F1 Matrix (macro)

| Model | English | Hindi | Maithili | Bhojpuri |
|---|---|---|---|---|
| **English model** | **0.5424** ✓ | 0.1912 | 0.1667 | 0.1654 |
| ⭐ **Hindi model** _(this model)_ | 0.4362 | **0.6778** ✓ | 0.6319 | 0.6042 |
| **Maithili model** | 0.4443 | 0.5757 | **0.9035** ✓ | 0.7458 |
| **Bhojpuri model** | 0.4250 | 0.4166 | 0.4114 | **0.9801** ✓ |

### Key Findings

- Hindi transfers significantly better than English to both Maithili (**63.3%**) and Bhojpuri (**61.7%**), nearly doubling English performance.
- Supports the hypothesis that **linguistic proximity** (Hindi → Bihari languages) aids cross-lingual transfer.
- Hindi model performs reasonably on English (60%), suggesting partial bidirectional transfer.

> **Full paper:** This cross-evaluation is part of a research study on cross-lingual transfer for low-resource Bihari languages. See the companion datasets and models: [Maithili](https://huggingface.co/abhiprd20/maithili-sentiment-model) | [Bhojpuri](https://huggingface.co/abhiprd20/bhojpuri-sentiment-model) | [Hindi](https://huggingface.co/abhiprd20/hindi-sentiment-model) | [English](https://huggingface.co/abhiprd20/nlp-sentiment-model)
