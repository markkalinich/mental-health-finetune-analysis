---
language: en
license: mit
library_name: transformers
tags:
  - sentiment-analysis
  - text-classification
  - distilbert
  - beginner
datasets:
  - imdb
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# My First Sentiment Analysis Model 🎬

A fine-tuned **DistilBERT** model for classifying movie reviews as
**POSITIVE** or **NEGATIVE**.

## How to Use

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="Kapilydv6/my-first-sentiment-model")

result = classifier("This movie was amazing!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.99}]
```

## Training Details

- **Base model:** distilbert-base-uncased
- **Dataset:** IMDB (2000 training samples)
- **Epochs:** 3
- **Framework:** PyTorch + Hugging Face Transformers

## Limitations

This is a beginner project trained on a small subset of IMDB reviews.
For production use, train on the full dataset with more epochs.


# Training Results Explained

## 📌 What Happened Step by Step

### 1. Dataset Loaded
- Downloaded the full IMDB dataset (**25,000 train + 25,000 test reviews**)
- Used only:
  - **2,000 samples for training**
  - **500 samples for testing**
- This was done as per configuration

---

### 2. Model Loaded — "MISSING / UNEXPECTED" Warnings

These warnings are **normal and expected**:

- **UNEXPECTED keys (vocab layers)**  
  - DistilBERT was originally trained for **masked language modeling**
  - These layers are **not needed for classification**

- **MISSING keys (classifier, pre_classifier)**  
  - These are **new layers added for the sentiment task**
  - They are **randomly initialized** and learned during training

---

### 3. Training (3 Epochs — ~1h 46min on CPU)

| Epoch | Train Loss | Eval Accuracy | Eval F1 |
|------|------------|--------------|--------|
| 1    | ~0.51      | 85.0%        | 84.96% |
| 2    | ~0.26      | 86.6%        | 86.55% |
| 3    | ~0.16      | 87.4%        | 87.39% |

✅ **Loss decreased** (0.60 → 0.15) → Model is learning  
✅ **Accuracy increased each epoch** → Model is improving  
✅ **Best model (Epoch 3)** was automatically selected and saved  

---

### 4. Final Accuracy

- **87.4% accuracy**
- Strong performance considering only **2,000 training samples**
- Using the full dataset could reach **~93%+ accuracy**

---

### 5. Test Predictions

| Review                              | Prediction | Confidence |
|------------------------------------|-----------|-----------|
| "Absolutely fantastic!"            | POSITIVE  | 97.9%     |
| "Terrible waste of time"           | NEGATIVE  | 96.7%     |
| "It was okay, nothing special"     | NEGATIVE  | 75.3%     |

💡 **Insight:**
- The third review is **ambiguous**
- A human might label it **neutral**
- The model predicts **NEGATIVE with lower confidence**, which is reasonable

---

## ⚠️ Warnings to Ignore

- **Symlinks warning**
  - Harmless Windows limitation
  - Only affects disk usage

- **LayerNorm gamma/beta → weight/bias**
  - Due to PyTorch naming changes
  - **No impact on results**

---

## ✅ Summary

- Model trained successfully  
- Performance improved across epochs  
- Achieved strong accuracy with limited data  
- Predictions are confident and reasonable  
- Warnings are expected and safe to ignore  

---
