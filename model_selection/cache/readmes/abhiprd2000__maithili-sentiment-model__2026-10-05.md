---
language:
- mai
- en
- bh
license: apache-2.0
tags:
- maithili
- sentiment-analysis
- text-classification
- low-resource-nlp
- indic-nlp
- cross-lingual-transfer
- xlm-roberta
- devanagari
- bihari-languages
base_model: cardiffnlp/twitter-xlm-roberta-base-sentiment
datasets:
- abhiprd20/Maithili_Sentiment_8K
metrics:
- accuracy
- f1
model-index:
- name: maithili-sentiment-model
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Maithili Sentiment Dataset
      type: abhiprd20/Maithili_Sentiment_8K
    metrics:
    - type: accuracy
      value: 0.8244
    - type: f1
      value: 0.8246
---

# 🗣️ Maithili Sentiment Model

### *XLM-RoBERTa fine-tuned for 3-class sentiment analysis in Maithili (मैथिली)*

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Accuracy](https://img.shields.io/badge/Accuracy-82.44%25-green)]()
[![F1 Score](https://img.shields.io/badge/F1%20Score-0.8246-orange)]()
[![OOD Accuracy](https://img.shields.io/badge/OOD%20Accuracy-82.00%25-brightgreen)]()
[![Language](https://img.shields.io/badge/Language-Maithili-yellow)]()
[![Base Model](https://img.shields.io/badge/Base-XLM--RoBERTa-blue)]()

---

## 📌 Model Description

**Maithili Sentiment Model** is a fine-tuned version of
`cardiffnlp/twitter-xlm-roberta-base-sentiment` trained on the
[Maithili Sentiment Dataset](https://huggingface.co/datasets/abhiprd20/Maithili_Sentiment_8K)
by Abhimanyu Prasad.

Maithili (मैथिली) is spoken by approximately 34 million people across the Mithila
region of Bihar, India and the Terai region of Nepal. Despite being one of the
22 scheduled languages of the Indian Constitution, it has received almost no
attention in NLP research. This is among the **first publicly available sentiment
models for Maithili**.

The model classifies Maithili text into three sentiment categories:
- 😊 **Positive** — text expressing satisfaction, happiness, or praise
- 😞 **Negative** — text expressing dissatisfaction, criticism, or distress
- 😐 **Neutral** — text that is factual, descriptive, or indifferent

---

## 📊 Performance

| Metric | Score |
|--------|-------|
| **Accuracy (in-distribution)** | **82.44%** |
| **Macro F1 (in-distribution)** | **0.8246** |
| **Accuracy (OOD — 50 held-out sentences)** | **82.00%** |
| **Macro F1 (OOD)** | **0.8197** |
| Training samples | 3,561 |
| Test samples | 501 |
| Base model | XLM-RoBERTa |

### Cross-Lingual Transfer Study Results

This model was trained as part of a cross-lingual transfer study examining how well
models trained on high-resource languages transfer to low-resource Bihari languages.

| Model | Accuracy | F1 |
|-------|----------|-----|
| English BERT on English (baseline) | 84.58% | 0.7928 |
| English BERT → Maithili (zero-shot) | 33.33% | 0.1667 |
| XLM-RoBERTa → Maithili (zero-shot) | 68.66% | 0.6787 |
| mBERT fine-tuned on Maithili | 70.86% | 0.7100 |
| **XLM-RoBERTa fine-tuned on Maithili (this model)** | **82.44%** | **0.8246** |

**Key finding:** English BERT collapses from 84.58% on English to 33.33% on Maithili
— a 51.25% drop — confirming the severity of the resource gap. Fine-tuning
XLM-RoBERTa recovers performance to 82.44%, with OOD accuracy nearly identical
at 82.00%, indicating genuine generalisation rather than memorisation.

---

## ⚡ Quick Start

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="abhiprd20/maithili-sentiment-model"
)

result = classifier("ई पोथी बहुत नीक ऐछ।")
print(result)
# → [{'label': 'positive', 'score': 0.94}]
```

---

## 🔍 More Examples

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="abhiprd20/maithili-sentiment-model"
)

texts = [
    "अहाँक काज बहुत सुन्दर ऐछ।",       # Your work is very beautiful.
    "हमरा ई खाना नीक नहि लागल।",        # I did not like this food.
    "हम काल्हि पटना जाइब।",              # I will go to Patna tomorrow.
    "परीक्षा मे हमरा नीक अंक भेटल।",    # I got good marks in the exam.
    "दोकानदार हमरा ठगि लेलक।",           # The shopkeeper cheated me.
]

for text in texts:
    result = classifier(text)[0]
    print(f"Text  : {text}")
    print(f"Label : {result['label']} ({round(result['score']*100, 1)}% confident)\n")
```

---

## 🧪 Use With AutoTokenizer and AutoModel

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("abhiprd20/maithili-sentiment-model")
model     = AutoModelForSequenceClassification.from_pretrained("abhiprd20/maithili-sentiment-model")

text   = "गीत सुनि कऽ मोन खुस भऽ गेल।"  # Listening to the song made my heart happy.
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)

probs    = torch.softmax(outputs.logits, dim=1)
label_id = torch.argmax(probs).item()
id2label = {0: "negative", 1: "neutral", 2: "positive"}

print(f"Label      : {id2label[label_id]}")
print(f"Confidence : {probs[0][label_id].item():.4f}")
```

---

## 🗂️ Training Details

| Parameter | Value |
|-----------|-------|
| Base model | `cardiffnlp/twitter-xlm-roberta-base-sentiment` |
| Task | Sequence Classification |
| Number of labels | 3 (negative, neutral, positive) |
| Epochs | 3 |
| Batch size | 16 |
| Max sequence length | 128 |
| Training samples | 3,561 (1,187 per class) |
| Test samples | 501 (167 per class) |
| Optimizer | AdamW (default) |
| Hardware | NVIDIA T4 GPU (Google Colab) |
| Framework | Hugging Face Transformers |

---

## 📦 Training Dataset

This model was trained on the
[Maithili Sentiment Dataset](https://huggingface.co/datasets/abhiprd20/Maithili_Sentiment_8K),
a 55,000-sentence corpus of Maithili text in Devanagari script with 3-class sentiment labels.

Training used **3,561 verified rows** (1,187 per class), balanced across all three
sentiment classes. The full dataset produces artificially high in-distribution accuracy
due to translation-pipeline homogeneity — a limitation documented in the paper.
The 3,561-row configuration produces honest, generalisable results as confirmed by
the near-identical OOD accuracy (82.00%).

---

## 🏷️ Label Mapping

| Label ID | Label | Meaning |
|----------|-------|---------|
| 0 | negative | Dissatisfaction, criticism, distress, anger |
| 1 | neutral | Factual, descriptive, balanced, indifferent |
| 2 | positive | Satisfaction, happiness, praise, appreciation |


---

## 🔗 Related Resources

| Resource | Link |
|----------|------|
| Training dataset | [abhiprd20/Maithili_Sentiment_8K](https://huggingface.co/datasets/abhiprd20/Maithili_Sentiment_8K) |
| Bhojpuri sentiment model | [abhiprd20/bhojpuri-sentiment-model](https://huggingface.co/abhiprd20/bhojpuri-sentiment-model) |
| Hindi sentiment model | [abhiprd20/hindi-sentiment-model](https://huggingface.co/abhiprd20/hindi-sentiment-model) |
| English baseline model | [abhiprd20/nlp-sentiment-model](https://huggingface.co/abhiprd20/nlp-sentiment-model) |

---

## ⚖️ License

This model is released under the **Apache License 2.0** — free for both
research and commercial use.

Copyright 2026 Abhimanyu Prasad

---

## 📎 Citation

If you use this model in your research or project, please cite:

```bibtex
@misc{prasad2025maithilisentiment,
  title        = {Maithili Sentiment Model: XLM-RoBERTa Fine-tuned for Low-Resource Sentiment Analysis},
  author       = {Prasad, Abhimanyu},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/abhiprd20/maithili-sentiment-model}},
  note         = {Accuracy: 82.44\%, F1: 0.8246, OOD Accuracy: 82.00\%.
                  Part of cross-lingual transfer study on low-resource Bihari languages.}
}
```

---

## 👤 Author

**Abhimanyu Prasad**
🤗 Hugging Face: [abhiprd20](https://huggingface.co/abhiprd20)
📦 Dataset: [abhiprd20/Maithili_Sentiment_8K](https://huggingface.co/datasets/abhiprd20/Maithili_Sentiment_8K)

---

*If this model helped your research, consider giving it a ⭐ — it helps others working on low-resource Indic NLP find it too!*

---

## 📊 Cross-Language Evaluation

Each model was evaluated on all 4 languages (300 sentences per language, 100 per class).
This shows how well models trained on one language transfer to others.

### Accuracy Matrix

| Model | English | Hindi | Maithili | Bhojpuri |
|---|---|---|---|---|
| **English model** | **79.5%** ✓ | 34.0% | 33.3% | 33.0% |
| **Hindi model** | 60.0% | **68.0%** ✓ | 63.3% | 61.7% |
| ⭐ **Maithili model** _(this model)_ | 63.0% | 59.0% | **90.3%** ✓ | 75.0% |
| **Bhojpuri model** | 59.0% | 47.3% | 47.3% | **98.0%** ✓ |

### F1 Matrix (macro)

| Model | English | Hindi | Maithili | Bhojpuri |
|---|---|---|---|---|
| **English model** | **0.5424** ✓ | 0.1912 | 0.1667 | 0.1654 |
| **Hindi model** | 0.4362 | **0.6778** ✓ | 0.6319 | 0.6042 |
| ⭐ **Maithili model** _(this model)_ | 0.4443 | 0.5757 | **0.9035** ✓ | 0.7458 |
| **Bhojpuri model** | 0.4250 | 0.4166 | 0.4114 | **0.9801** ✓ |

### Key Findings

- Strong transfer to Bhojpuri (**75%**), a related Bihari language, significantly outperforming both English (33%) and Hindi (61.7%) on Bhojpuri.
- Suggests **Bihari language family** similarity enables strong cross-lingual transfer.
- Maithili → Bhojpuri transfer (75%) is asymmetric: Bhojpuri → Maithili is only 47.3%.

> **Full paper:** This cross-evaluation is part of a research study on cross-lingual transfer for low-resource Bihari languages. See the companion datasets and models: [Maithili](https://huggingface.co/abhiprd20/maithili-sentiment-model) | [Bhojpuri](https://huggingface.co/abhiprd20/bhojpuri-sentiment-model) | [Hindi](https://huggingface.co/abhiprd20/hindi-sentiment-model) | [English](https://huggingface.co/abhiprd20/nlp-sentiment-model)
