---
language:
- en
tags:
- sentiment-analysis
- english
- text-classification
- roberta
- roberta-large
- transformers
- pytorch
- nlp
- fine-tuned
- educational-feedback
datasets:
- custom-english-feedback
widget:
- text: "This product is absolutely amazing! Best purchase ever!"
  example_title: Positive Review
- text: "Terrible quality and poor customer service. Very disappointed."
  example_title: Negative Review
- text: "It's okay, nothing special but gets the job done."
  example_title: Neutral Review
- text: "The teacher explains concepts with great patience and clarity."
  example_title: Positive Feedback
- text: "The online platform kept crashing during the session."
  example_title: Negative Feedback
license: mit
library_name: transformers
pipeline_tag: text-classification
model-index:
- name: English Sentiment Analysis (RoBERTa-Large)
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Custom English Feedback Dataset
      type: custom
      split: test
    metrics:
    - type: accuracy
      value: 0.9212
      name: Accuracy
      verified: true
    - type: f1
      value: 0.9191
      name: F1-Score (Weighted)
      verified: true
    - type: precision
      value: 0.9198
      name: Precision (Weighted)
      verified: true
    - type: recall
      value: 0.9212
      name: Recall (Weighted)
      verified: true
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- siebert/sentiment-roberta-large-english
inference:
  parameters:
    max_length: 256
    padding: true
    truncation: true
    return_tensors: pt
co2_eq_emissions:
  emissions: 1.20
  source: Estimated based on training duration and hardware
  training_type: fine-tuning
  hardware_used: NVIDIA Tesla T4 (16GB)
---

# 🇬🇧 English Sentiment Analysis — Fine-tuned RoBERTa-Large

<div align="center">
  <h3>A Fine-tuned RoBERTa-Large Model for 3-Class English Sentiment Classification</h3>
  <p>Trained on educational and consumer feedback data for high-precision sentiment understanding</p>

  [![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow)](https://huggingface.co/tahamueed23/english-sentiment-roberta-large)
  [![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
  [![Transformers](https://img.shields.io/badge/🤗-Transformers-orange)](https://github.com/huggingface/transformers)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
  [![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
</div>

---

## 1. Model Overview

This model is a **fine-tuned RoBERTa-Large** classifier for **English sentiment analysis**, adapted from [`siebert/sentiment-roberta-large-english`](https://huggingface.co/siebert/sentiment-roberta-large-english). It classifies English text into three sentiment categories — **Positive**, **Neutral**, and **Negative** — with high confidence and strong generalization across diverse feedback domains.

The model was trained on a curated dataset of English-language educational and consumer feedback, and achieves **92.12% accuracy** on the held-out test set, making it well-suited for production-grade NLP pipelines.

---

## 2. Model Details

| Attribute | Value |
|:---|:---|
| **Base Model** | `siebert/sentiment-roberta-large-english` |
| **Architecture** | RoBERTa-Large (Transformer Encoder) |
| **Task** | 3-class Sentiment Classification |
| **Classes** | `Negative` (0), `Neutral` (1), `Positive` (2) |
| **Total Parameters** | 355,362,819 (~355M) |
| **Model Size** | ~1.42 GB |
| **Max Sequence Length** | 256 tokens |
| **Training Framework** | Hugging Face Transformers + PyTorch |
| **Compute** | Mixed Precision (FP16) |
| **Repository** | [tahamueed23/english-sentiment-roberta-large](https://huggingface.co/tahamueed23/english-sentiment-roberta-large) |
| **Last Updated** | February 22, 2026 |
| **Author** | Taha Mueed |

---

## 3. Intended Use

This model is designed for any downstream task that requires classifying the sentiment of English text into three categories: Positive, Neutral, or Negative.

| Domain | Application |
|:---|:---|
| 🎓 **Education** | Student feedback analysis, course evaluation, teacher reviews |
| 🛒 **E-commerce** | Product review classification, customer satisfaction scoring |
| 📱 **Social Media** | Comment moderation, brand monitoring, opinion mining |
| 🏢 **Customer Support** | Ticket sentiment tagging, call centre transcript analysis |
| 🏥 **Healthcare** | Patient experience reviews, hospital feedback analysis |
| 📊 **Market Research** | Consumer opinion tracking, NPS survey classification |
| 🛡️ **Content Moderation** | Detecting hostile or negative user-generated content |

### Out-of-Scope Use

This model is designed for **English-only** input. It is not suitable for multilingual text, code-switched content, or non-English languages. It was also not trained for tasks like emotion detection beyond sentiment polarity, toxicity classification, or stance detection.

---

## 4. Dataset Description

The training data was sourced from a **multilingual academic feedback dataset** hosted on Google Sheets, containing 50,056 records across five languages. Only English-language entries were selected for this model's training.

### Full Dataset Composition (N = 50,056)

| Language | Count | Percentage |
|:---|---:|---:|
| Roman Urdu | 16,916 | 33.79% |
| Urdu | 16,782 | 33.52% |
| **English** | **16,355** | **32.67%** |
| Mixed / Other | 3 | 0.01% |

### English Subset — After Filtering and Cleaning (N = 15,650)

| Sentiment Class | Count | Percentage |
|:---|---:|---:|
| **Positive** | 7,160 | 45.75% |
| **Negative** | 5,364 | 34.27% |
| **Neutral** | 3,126 | 19.97% |

The dataset exhibits a moderate class imbalance, with Neutral being the least represented class. This was addressed through **class-weighted loss** during training (see Section 7).

### Train / Validation / Test Split

| Split | Samples | Percentage |
|:---|---:|---:|
| **Training** | 10,955 | 70.0% |
| **Validation** | 2,347 | 15.0% |
| **Test** | 2,348 | 15.0% |
| **Total** | **15,650** | **100%** |

Splits were created using **stratified sampling** to preserve the original class distribution across all three subsets.

---

## 5. Data Preprocessing

The following cleaning and normalization steps were applied to the raw English text before training:

1. **Duplicate removal** — 701 duplicate entries were removed based on exact match of the feedback field.
2. **Null filtering** — Records with missing `feedback` or `senti_manual` values were dropped.
3. **Whitespace normalization** — Consecutive whitespace characters were collapsed using regex substitution.
4. **Short text removal** — Texts shorter than 5 characters were discarded as uninformative.
5. **Empty string removal** — Any remaining blank entries after cleaning were excluded.
6. **Label standardization** — Sentiment labels were title-cased and mapped to integers: `Negative → 0`, `Neutral → 1`, `Positive → 2`.
7. **Label validation** — Rows with labels outside the valid set `{0, 1, 2}` were dropped.

After preprocessing, the final cleaned dataset contained **15,650 samples**, reduced from 16,355 raw English entries.

---

## 6. Training Procedure

The model was initialized from `siebert/sentiment-roberta-large-english` (originally a binary classifier) and adapted to a **3-class classification head** by re-initializing the output projection layer (`classifier.out_proj`) to output 3 logits instead of 2.

Training used a **custom weighted loss Trainer** (`WeightedLossTrainer`) that applies per-class weights during cross-entropy loss computation to compensate for the Neutral class underrepresentation.

### Class Weights Applied During Training

| Class | Weight |
|:---|:---|
| Negative | 0.9725 |
| Neutral | 1.6688 |
| Positive | 0.7286 |

Weights were computed using `sklearn.utils.class_weight.compute_class_weight` with the `balanced` strategy.

Additional training strategies included gradient checkpointing to reduce GPU memory usage, FP16 mixed precision for faster computation, and early stopping with a patience of 3 evaluation cycles to prevent overfitting. Model checkpoints were evaluated every 100 steps on the validation set using weighted F1 as the selection criterion, and the best checkpoint was loaded at the end of training.

**Total training time:** 4,332.72 seconds (~72 minutes) on an NVIDIA Tesla T4 (15.64 GB VRAM).

---

## 7. Hyperparameters

| Parameter | Value |
|:---|:---|
| Epochs | 4 |
| Per-device Train Batch Size | 8 |
| Per-device Eval Batch Size | 16 |
| Gradient Accumulation Steps | 2 (effective batch size = 16) |
| Learning Rate | 2e-5 |
| LR Scheduler | Cosine |
| Warmup Steps | 500 |
| Weight Decay | 0.01 |
| Optimizer | AdamW (`adamw_torch`) |
| Mixed Precision | FP16 |
| Gradient Checkpointing | Yes |
| Max Sequence Length | 256 tokens |
| Early Stopping Patience | 3 evaluation cycles |
| Eval / Save Strategy | Every 100 steps |
| Best Model Selection Metric | Weighted F1 |
| Random Seed | 42 |

---

## 8. Evaluation Metrics

All metrics reported are computed on the **held-out test set** (2,348 samples) unless stated otherwise.

### Overall Performance

| Metric | Score | 
|:---|:---:|
| **Accuracy** | **92.12%** |
| **F1-Score (Weighted)** | **91.91%** |
| **Precision (Weighted)** | **91.98%** |
| **Recall (Weighted)** | **92.12%** |

### Validation Set Performance

| Metric | Score |
|:---|:---:|
| Validation Loss | 0.4273 |
| Accuracy | 92.54% |
| F1-Score (Weighted) | 92.42% |
| Precision (Weighted) | 92.46% |
| Recall (Weighted) | 92.54% |

---

## 9. Results

### Per-Class Performance (Test Set)

| Class | Precision | Recall | F1-Score | Support |
|:---|:---:|:---:|:---:|:---:|
| **Negative** | 91.73% | 96.40% | **94.00%** | 805 |
| **Neutral** | 87.94% | 74.63% | **80.74%** | 469 |
| **Positive** | 93.93% | 96.55% | **95.22%** | 1,074 |
| **Weighted Avg** | **91.98%** | **92.12%** | **91.91%** | 2,348 |

### Confusion Matrix

|  | Predicted: Negative | Predicted: Neutral | Predicted: Positive |
|:---|:---:|:---:|:---:|
| **Actual: Negative** | **776** | 22 | 7 |
| **Actual: Neutral** | 59 | **350** | 60 |
| **Actual: Positive** | 11 | 26 | **1,037** |

The model performs exceptionally well on the **Positive** and **Negative** classes, with F1 scores above 94%. The **Neutral** class, as expected given its lower training representation and linguistic ambiguity, shows a slightly lower recall (74.63%), indicating that some neutral texts are misclassified as positive — a common challenge in 3-class sentiment tasks.

**Error Rate:** 185 misclassifications out of 2,348 samples (7.88%)

### Sample Predictions

| Input Text | Predicted Sentiment | Confidence |
|:---|:---|:---:|
| "This product is absolutely amazing! Best purchase ever!" | Positive 🟢 | 99.88% |
| "Terrible quality and poor customer service." | Negative 🔴 | 99.64% |
| "It's okay, nothing special but does the job." | Neutral 🟡 | 99.49% |
| "The outdoor seating areas are pleasant and encourage socializing." | Positive 🟢 | 99.90% |
| "Very disappointed with this purchase." | Negative 🔴 | 99.63% |
| "Average service, could be better but could be worse." | Neutral 🟡 | 99.68% |
| "Exceptional quality and fantastic customer support!" | Positive 🟢 | 99.90% |

---

## 💻 How to Use

### Method 1: Pipeline API (Quickest)

```python
from transformers import pipeline

# Load the model
classifier = pipeline(
    "sentiment-analysis",
    model="tahamueed23/english-sentiment-roberta-large"
)

# Single prediction
result = classifier("This is an amazing product!")[0]

# Map label to sentiment
sentiment_map = {'LABEL_2': 'Positive', 'LABEL_1': 'Neutral', 'LABEL_0': 'Negative'}
print(f"Sentiment:  {sentiment_map[result['label']]}")
print(f"Confidence: {result['score']:.2%}")
```

### Method 2: Manual Inference

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "tahamueed23/english-sentiment-roberta-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "The lecture was well-structured and easy to follow."
inputs = tokenizer(text, return_tensors="pt", padding=True,
                   truncation=True, max_length=256)

model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = torch.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=1).item()
    confidence = probabilities[0][predicted_class].item()

sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
print(f"Text:       {text}")
print(f"Sentiment:  {sentiment_map[predicted_class]}")
print(f"Confidence: {confidence:.2%}")

# All class probabilities
for i, label in sentiment_map.items():
    print(f"  {label}: {probabilities[0][i]:.2%}")
```

### Method 3: Batch Processing

```python
from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="tahamueed23/english-sentiment-roberta-large"
)

texts = [
    "Best experience I've had with this service!",
    "Very disappointing — would not recommend.",
    "It's acceptable, nothing remarkable.",
    "The support team resolved my issue quickly.",
    "The product broke after two days."
]

results = classifier(texts, batch_size=16)

sentiment_map = {'LABEL_2': 'Positive', 'LABEL_1': 'Neutral', 'LABEL_0': 'Negative'}
for text, result in zip(texts, results):
    sentiment = sentiment_map[result['label']]
    print(f"  {text[:60]:<60} → {sentiment:<8} ({result['score']:.2%})")
```

### Method 4: Hugging Face Inference API

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/tahamueed23/english-sentiment-roberta-large"
headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

def query(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    return response.json()

output = query("The course material was very well organized.")
print(output)
```

---

## 10. Limitations

### Language and Input Constraints

| Limitation | Severity | Notes |
|:---|:---:|:---|
| Non-English text | ❌ High | Model is designed exclusively for English input |
| Very short texts (< 5 chars) | ❌ High | Insufficient context for reliable classification |
| Code-switched or mixed-language text | ⚠️ Medium | May produce unreliable predictions |
| Sarcasm and irony | ⚠️ Medium | Nuanced text may be misclassified |
| Domain-specific jargon | ⚠️ Low | Performance may degrade on highly specialized content |
| Emojis only (no text) | ❌ High | Requires at least some textual content |

### Technical Constraints

| Constraint | Value | Notes |
|:---|:---:|:---|
| Max Sequence Length | 256 tokens | Longer texts will be truncated |
| Model Size | ~1.42 GB | Quantization recommended for low-memory environments |
| CPU Inference Speed | ~450ms/sample | GPU strongly recommended for production use |
| GPU Inference Speed | ~45ms/sample | Real-time capable on modern GPUs |

### Known Weaknesses

The model shows its weakest performance on the **Neutral** class (F1: 80.74%, Recall: 74.63%), which is a known challenge in 3-class sentiment tasks. Texts that contain both positive and negative elements, or those that are factually descriptive without strong polarity, are most likely to be misclassified. Error analysis reveals that the most common mistake is misclassifying neutral educational feedback as positive, particularly when the text contains surface-level positive language without an explicit sentiment intent.

---

## 11. Ethical Considerations

This model was trained on feedback collected from educational and consumer contexts. Users should be aware of the following considerations before deploying it:

**Bias.** The training data reflects the language patterns and sentiments present in specific feedback domains (primarily academic and product reviews). The model may not generalize equitably across all demographic groups, writing styles, or cultural contexts. It could underperform on dialects or informal registers underrepresented in the training corpus.

**Responsible deployment.** Sentiment predictions should not be used as the sole basis for high-stakes decisions affecting individuals (e.g., employee performance review, student grading, or content banning). Human review is strongly recommended for sensitive applications.

**Data privacy.** Ensure that any text submitted for inference does not contain personally identifiable information (PII), as text is processed through the model at inference time.

**Feedback misinterpretation.** The Neutral class has lower recall, meaning some genuinely neutral or ambiguous feedback may be incorrectly flagged as Positive or Negative. Downstream consumers should be designed to tolerate this level of uncertainty.

---

## 12. Future Improvements

| Planned Update | Version | Description |
|:---|:---:|:---|
| Quantized Version | v1.0.1 | INT8 quantization for ~75% model size reduction |
| Improved Neutral Detection | v1.1.0 | Data augmentation and focal loss to address class imbalance |
| Domain Adaptation | v1.2.0 | Specialized fine-tuning for healthcare, legal, or financial text |
| 4-Class Emotion Detection | v2.0.0 | Extending to: Joy, Anger, Sadness, Neutral |
| Multilingual Support | v2.1.0 | Cross-lingual model supporting English + Urdu + Roman Urdu |
| Gradio Demo | — | Interactive web demo on Hugging Face Spaces |

---

## 📚 Citation

If you use this model in your research or project, please cite:

```bibtex
@misc{english_sentiment_roberta_2026,
  author    = {Taha Mueed},
  title     = {English Sentiment Analysis: A Fine-tuned RoBERTa-Large Model for 3-Class Sentiment Classification},
  year      = {2026},
  publisher = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.co/tahamueed23/english-sentiment-roberta-large}},
  note      = {Version 1.0, Test Accuracy: 92.12\%, F1: 91.91\%}
}
```

---

## 📄 License

This model is released under the **MIT License**.

```
MIT License

Copyright (c) 2026 Taha Mueed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 📬 Contact & Support

| Channel | Details | Response Time |
|:---|:---|:---:|
| 🤗 Hugging Face | tahamueed23/english-sentiment-roberta-large | < 24h |
| 📧 Email | tahamueed23@gmail.com | < 72h |

---

## 🙏 Acknowledgments

- **Hugging Face** — Transformers library and model hosting infrastructure
- **siebert / Cardiff NLP** — Base RoBERTa-Large sentiment model and research
- **PyTorch Team** — Deep learning framework
- **scikit-learn** — Evaluation metrics and class weight computation

---

<div align="center">
  <h3>Built for reliable, high-precision English sentiment understanding</h3>
  <br>
  <a href="https://huggingface.co/tahamueed23/english-sentiment-roberta-large">
    <img src="https://img.shields.io/badge/🤗-View%20on%20Hugging%20Face-blue?style=for-the-badge" alt="View on Hugging Face">
  </a>
  <br><br>
  <sub>© 2026 Taha Mueed • MIT License • Version 1.0.0</sub>
</div>