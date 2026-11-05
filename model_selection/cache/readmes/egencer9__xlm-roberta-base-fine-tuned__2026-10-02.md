---
language:
- tr
- en
- fr
- de
- es
- ru
- ja
- zh
- multilingual
license: mit
tags:
- sentiment-analysis
- text-classification
- sequence-classification
- pytorch
- xlm-roberta
metrics:
- f1
- accuracy
- precision
- recall
pipeline_tag: text-classification
widget:
- text: "Super vendeur ! Produit de très bonne qualidade."
  example_title: "French - Positive Review"
- text: "Bu ürünü kesinlikle tavsiye etmiyorum, çok kalitesiz."
  example_title: "Turkish - Negative Review"
- text: "Worst product ever. Stopped working after two days."
  example_title: "English - Negative Review"
- text: "本当に素晴らしい商品です！大満足。"
  example_title: "Japanese - Positive Review"
- text: "Das Gerät funktioniert einwandfrei und der Versand war blitzschnell."
  example_title: "German - Positive Review"
---

# XLM-RoBERTa for Multilingual Sentiment Analysis

This model is a fine-tuned version of [**`xlm-roberta-base`**](https://huggingface.co/xlm-roberta-base) for binary multilingual sentiment analysis. It classifies text reviews into **`positive`** (`LABEL_1`) and **`negative`** (`LABEL_0`) sentiment across multiple languages (including English, Turkish, French, German, Spanish, Russian, Japanese, Chinese, and more).

This model was trained as part of the **CMPE 346 - Multilingual Sentiment Analysis** course project.

## 🚀 Model Details

- **Model Type:** Multilingual Transformer-based Sequence Classification (`xlm-roberta-base`)
- **Number of Parameters:** ~270M
- **Task:** Binary Sentiment Analysis (Positive vs. Negative)
- **Primary Languages:** Multilingual (Pre-trained on 100+ languages, fine-tuned on a rich mixed-language review corpus)
- **License:** MIT

---

## 📊 Performance & Evaluation Results

The model was evaluated on a comprehensive multilingual validation dataset (`valid.csv`) comprising 17,500 samples. It successfully outperformed the assignment's baseline F1-score by a significant margin.

### Metric Comparison

| Metric | Baseline | **Our Fine-Tuned Model** | Status |
| :--- | :---: | :---: | :---: |
| **Validation F1-Score** | `0.7958` | **0.9100 (91.00%)** | **Passed (+11.42%)** ✅ |
| **Accuracy** | - | **90.96%** | ✅ |
| **Precision** | - | **90.87%** | ✅ |
| **Recall** | - | **91.13%** | ✅ |

---

## 🛠️ Training Configuration & Hyperparameters

The model was fine-tuned using Hugging Face's `Trainer` API with the following parameters:

| Hyperparameter | Value | Description |
| :--- | :--- | :--- |
| **Base Architecture** | `xlm-roberta-base` | State-of-the-art multilingual XLM-R foundation |
| **Learning Rate** | `2e-5` | Small learning rate for stable fine-tuning |
| **Optimizer** | `AdamW` | Standard Adam optimizer with weight decay |
| **Weight Decay** | `0.01` | Regularization to prevent overfitting |
| **Batch Size** | `32` | 32 samples per device |
| **Training Epochs** | `2` | Iterations over the balanced training dataset |
| **Max Sequence Length** | `128` | Optimized token length for short and medium reviews |
| **Training Set Size** | `20,000` | Perfectly balanced stratified subset (10k positive, 10k negative) |
| **Validation Set Size** | `17,500` | Full original validation dataset |

---

## 🔍 Preprocessing & Tokenization

We employed a robust data preparation pipeline built using Python and PyTorch:
1. **Text Cleaning:** Handled missing values (NaNs), stripped leading/trailing whitespaces, and formatted strings to maintain text integrity.
2. **Multilingual Tokenization:** Used `xlm-roberta-base`'s native SentencePiece-based tokenizer. Tokenization utilizes a massive 250,000 token vocabulary, which virtually eliminates out-of-vocabulary (OOV) issues for non-Latin characters (like Russian Cyrillic, Japanese Kanji/Kana, and Chinese Hanzi).
3. **Sequence Length:** Set to `128` to maintain high training throughput and avoid unnecessary zero-padding memory overhead.

---

## 💻 How to Use

You can easily load and run predictions with this model directly from the Hugging Face Hub using the `pipeline` API:

```python
from transformers import pipeline

# 1. Initialize the sentiment classification pipeline
model_checkpoint = "egencer9/xlm-roberta-base-fine-tuned"
classifier = pipeline("text-classification", model=model_checkpoint, device=0) # Set device=0 for GPU, or device=-1 for CPU

# 2. Test multilingual sentiment predictions
reviews = [
    "Super vendeur ! Produit de très bonne qualité.",  # French - Positive
    "Worst product ever. Stopped working after two days.", # English - Negative
    "Bu ürünü kesinlikle tavsiye etmiyorum, çok kalitesiz.", # Turkish - Negative
    "本当に素晴らしい商品です！大満足です。", # Japanese - Positive
    "Das Gerät funktioniert einwandfrei und der Versand war blitzschnell." # German - Positive
]

predictions = classifier(reviews)

# 3. Print predictions
for text, pred in zip(reviews, predictions):
    # LABEL_0 -> negative, LABEL_1 -> positive
    sentiment = "positive" if pred['label'] == "LABEL_1" else "negative"
    print(f"Review: '{text}'")
    print(f"Prediction: {sentiment} (Score: {pred['score']:.4f})\n")