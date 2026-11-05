---
language: 
  - en
license: mit
tags:
  - sentiment-analysis
  - english
  - text-classification
  - roberta
base_model: siebert/sentiment-roberta-large-english
datasets:
  - custom
pipeline_tag: text-classification
metrics:
  - accuracy
  - precision
  - recall
  - f1
---

## 🚀 Model Overview

- **Base Model:** siebert/sentiment-roberta-large-english  
- **Task:** Sentiment Classification  
- **Languages:** English  
- **Dataset Source:** Google Sheets CSV (custom dataset)  
- **Columns Used:** `Sentence`, `Language`, `Sentiment`, `Topic`, `Characters`
- **Filtered:** Only English rows were kept  

---

## 📊 Training Results (by Epoch)

| Epoch | Training Loss | Validation Loss | Accuracy | Precision | Recall | F1 |
|-------|---------------|-----------------|----------|-----------|--------|------|
| **1** | 0.627600 | 0.484212 | 0.875636 | 0.874333 | 0.875636 | 0.872211 |
| **2** | 0.250100 | 0.419673 | 0.905031 | 0.901430 | 0.905031 | 0.902535 |
| **3** | 0.229800 | 0.467646 | **0.906727** | **0.903297** | **0.906727** | **0.904490** |

---

## 🧪 Final Evaluation Metrics


The model shows **strong performance** with ~90%+ across all core metrics (accuracy, precision, recall, F1).

> ⚠️ A warning from scikit-learn indicated some classes had no predicted samples. This usually happens when the dataset is imbalanced. Class-balancing or weighted loss can improve minority class scores.

---

## 🧠 Intended Use

This model is suitable for:

- Product review sentiment
- Student Feedback
- Customer feedback analysis
- Social media sentiment
- General English text polarity detection

---

## 🚫 Limitations

- Trained only on English sentences — performance on Urdu / Roman Urdu is not guaranteed.
- Dataset may be imbalanced.
- Not designed for multi-label sentiment or non-general texts (e.g., sarcasm).

---

## 🧩 How to Use

### **Pipeline Usage**
```python
from transformers import pipeline

model_name = "tahamueed23/sentiment_roberta_english_finetuned"

classifier = pipeline("text-classification", model=model_name, tokenizer=model_name)

classifier("I really love this product!")
