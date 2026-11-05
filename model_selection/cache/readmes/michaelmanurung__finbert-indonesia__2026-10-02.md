---
license: mit
tags:
- indonesian
- finance
- sentiment
- text-classification
- finbert
- pytorch
language: id
datasets:
- custom
base_model: ProsusAI/finbert
model-index:
- name: FinBERT Indonesia
  results: []
---

# 🇮🇩 FinBERT Indonesia — Sentiment Classification for Financial News in Bahasa Indonesia

This model is a fine-tuned version of [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert) on a custom dataset of ~500 financial news headlines written in Bahasa Indonesia. The task is **3-class sentiment classification**: `positive`, `neutral`, and `negative`.

---

## 🚀 Live Demo
Try it here: https://huggingface.co/spaces/michaelmanurung/finbert-indonesia-demo

## 🏗️ Model Architecture

The base model is [FinBERT](https://huggingface.co/ProsusAI/finbert), which itself is a BERT model pre-trained on financial texts. It has been fine-tuned using the Hugging Face `transformers` library with the following modifications:

- Multilingual financial context adaptation via custom labeled data in Bahasa Indonesia
- Classification head for 3 sentiment labels

---

## 🧾 Dataset

The training dataset consists of **500 manually labeled financial news titles** from Indonesian sources. Each entry is categorized as:

- `positive` – bullish or growth-related headlines
- `neutral` – factual or event-based reporting
- `negative` – bearish or risk-indicative headlines

Example:

| Title | Label |
|-------|-------|
| IHSG diperkirakan rebound minggu ini | positive |
| BI umumkan suku bunga tetap | neutral |
| Rupiah melemah terhadap dolar AS | negative |

---

## 🧪 Evaluation

Evaluation was conducted on the `intanm/indonesian-financial-sentiment-analysis` benchmark dataset using accuracy, F1 score, precision, and recall metrics.

The benchmark compares:
- `michaelmanurung/finbert-indonesia` (Indonesian financial sentiment model)
- `ProsusAI/finbert` (English financial sentiment model)
- `ayameRushia/bert-base-indonesian-1.5G-sentiment-analysis-smsa` (general Indonesian sentiment model)

| Model                                                         | Accuracy | F1 Score | Precision | Recall |
|---------------------------------------------------------------|----------|----------|-----------|--------|
| michaelmanurung/finbert-indonesia                             | 0.299    | 0.276    | 0.347     | 0.299  |
| ProsusAI/finbert                                              | 0.285    | 0.134    | 0.560     | 0.285  |
| ayameRushia/bert-base-indonesian-1.5G-sentiment-analysis-smsa | 0.334    | 0.238    | 0.669     | 0.334  |

> Metrics are reported using weighted averaging.

---

## 🧪 Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="michaelmanurung/finbert-indonesia",
    tokenizer="michaelmanurung/finbert-indonesia"
)

result = classifier("IHSG turun tipis karena aksi ambil untung investor.")
print(result)
# Output: [{'label': 'LABEL_2', 'score': 0.89}] -> e.g. 'positive'