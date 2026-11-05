---
language: en
license: apache-2.0
tags:
  - sentiment-analysis
  - text-classification
  - bert
  - hospitality
  - hotel-reviews
  - nlp
datasets:
  - kaenova/hotel-sentiment
metrics:
  - accuracy
  - precision
  - recall
  - f1
  - roc_auc
model_name: BERT Hospitality Review Classifier
pipeline_tag: text-classification
base_model: bert-base-uncased
library_name: transformers
---

# BERT Hospitality Review Classifier

## Model Description

**BERT Hospitality Review Classifier** is a fine-tuned `bert-base-uncased` model designed to classify hotel reviews into **positive** or **negative** sentiment.  
The model is trained on a large-scale hospitality-specific dataset to capture nuanced language patterns commonly found in hotel guest feedback.

- **Base model:** bert-base-uncased  
- **Task:** Binary Sentiment Classification  
- **Domain:** Hospitality / Hotel Reviews  
- **Language:** English  
- **Labels:** `negative`, `positive`

---

## Dataset

The model is trained and evaluated using the **kaenova/hotel-sentiment** dataset from Hugging Face.

- **Total samples:** 742,612 reviews  
- **Training set:** 668,350  
- **Validation set:** 37,131  
- **Test set:** 37,131  
- **Classes:** Binary (Negative, Positive)  
- **Label distribution:** Approximately balanced  

Dataset link: https://huggingface.co/datasets/kaenova/hotel-sentiment

---

## Training Details

- **Architecture:** BERT with sequence classification head  
- **Max sequence length:** 256 tokens  
- **Optimizer:** AdamW  
- **Loss function:** Cross-entropy  
- **Hardware:** NVIDIA T4 GPU (Google Colab)  
- **Framework:** Hugging Face Transformers  

The classification head was newly initialized and trained during fine-tuning, which is expected behavior when adapting BERT to a downstream task.

---

## Evaluation Results

The model was evaluated on a held-out test set of **37,131 reviews**.

### Overall Metrics

| Metric       | Score |
|-------------|-------|
| Accuracy    | **0.9690** |
| Precision   | **0.9772** |
| Recall      | **0.9668** |
| F1-score    | **0.9720** |
| ROC-AUC     | **0.9923** |

---

## Confusion Matrix

<p align="center">
  <img src="assets/confusion_matrix.png" width="420"/>
</p>

- **True Positives:** 19,946  
- **True Negatives:** 16,034  
- **False Positives:** 466  
- **False Negatives:** 685  

---

## ROC Curve

<p align="center">
  <img src="assets/roc_curve.png" width="480"/>
</p>

The ROC curve shows strong class separability, with an AUC of **0.9923**, indicating excellent discriminative performance.

---

## Error Analysis (Qualitative)

### Common False Positives
- Reviews with **strong positive wording** but subtle complaints
- Location-focused praise masking dissatisfaction in services

### Common False Negatives
- Reviews with **mild criticism** framed in neutral language
- Operational complaints without strong emotional markers

This behavior aligns with real-world hospitality feedback patterns.

---

## Intended Use

This model is suitable for:

- Hotel review sentiment analysis
- Guest feedback monitoring systems
- Hospitality analytics dashboards
- Customer experience automation
- AI-powered hotel assistants

---

## Limitations

- Binary sentiment only (no neutral or aspect-based sentiment)
- Trained on English-language reviews
- Performance may degrade on highly sarcastic or ambiguous text

---

## Ethical Considerations

- The model reflects sentiment trends in publicly available hotel reviews
- Predictions should support, not replace, human decision-making
- Not intended for high-stakes automated judgments

---

## Author

Amey Tillu
Hospitality Data Analyst & AI/ML Hobbyist

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Amey9766/BERT-hospitality-review-classifier")
model = AutoModelForSequenceClassification.from_pretrained("Amey9766/BERT-hospitality-review-classifier")

text = "The hotel was clean and staff were very helpful."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=1).item()

label_map = {0: "negative", 1: "positive"}
print(label_map[prediction])
