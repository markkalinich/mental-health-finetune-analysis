---
language: en
tags:
- emotion-detection
- text-classification
- transformers
- distilbert
datasets:
- nelgiriyewithana/emotions
model-index:
- name: DistilBERT Emotion Classifier
  results:
  - task:
      type: text-classification
      name: Emotion Detection
    dataset:
      name: Kaggle Emotions Dataset
      type: text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.94
    - name: F1
      type: f1
      value: 0.94
    - name: Precision
      type: precision
      value: 0.94
    - name: Recall
      type: recall
      value: 0.94
license: apache-2.0
metrics:
- accuracy
- recall
- precision
---

# DistilBERT Emotion Classifier 🎭

This model classifies English text into one of six emotions: **sadness, joy, love, anger, fear, surprise**.

- **Base model**: `distilbert-base-uncased`
- **Framework**: Hugging Face Transformers
- **Dataset**: [Kaggle Emotions Dataset](https://www.kaggle.com/datasets/nelgiriyewithana/emotions)
- **Task**: Multi-class emotion detection

---

## 📊 Evaluation

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0 (sadness)  | 0.99 | 0.96 | 0.98 | 24,121 |
| 1 (joy)      | 0.93 | 0.99 | 0.96 | 28,220 |
| 2 (love)     | 1.00 | 0.71 | 0.83 | 6,824  |
| 3 (anger)    | 0.95 | 0.94 | 0.95 | 11,448 |
| 4 (fear)     | 0.90 | 0.91 | 0.91 | 9,574  |
| 5 (surprise) | 0.74 | 0.99 | 0.85 | 3,038  |

**Overall Performance**:  
- Accuracy: **94%**  
- Macro F1: **0.91**  
- Weighted F1: **0.94**  

---

## 🧑‍💻 Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

model_name = "YamenRM/distilbert-emotion-classifier"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

nlp = pipeline("text-classification", model=model, tokenizer=tokenizer)

print(nlp("I feel so happy and excited today!"))
# [{'label': 'joy', 'score': 0.98}]