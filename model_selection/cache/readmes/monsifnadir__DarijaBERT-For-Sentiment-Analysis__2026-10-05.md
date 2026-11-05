---
language: "ar"
tags:
- darija
- moroccan-arabic
- sentiment-analysis
- text-classification
- fine-tuned
- tweets
license: apache-2.0
metrics:
- accuracy
- f1
- precision
- recall
- cohen_kappa
---

# DarijaBERT Fine-Tuned for Sentiment Analysis 🇲🇦🧠

This sentiment analysis model is based on **DarijaBERT**, a language model pretrained on Moroccan Arabic (Darija) text.  
The model has been **fine-tuned** to classify Moroccan Arabic tweets and public comments into three sentiment categories:
- **Positive** (2)
- **Neutral** (0)
- **Negative** (1)

---

## 🛠 Model Architecture

The base DarijaBERT architecture was **extended** with:
- Two fully connected layers of **1024 neurons each**
- **Dropout layer (p=0.3)** to enhance generalization
- Final classification layer with **3 output neurons** (one for each sentiment class)

---

## 🧠 Pretraining Details

- **Dataset**: 17,441 Moroccan tweets
  - 9,894 positive tweets (56.73%)
  - 4,039 neutral tweets (23.16%)
  - 3,508 negative tweets (20.11%)
- **Training Framework**: Hugging Face Trainer API
- **Hyperparameters**:
  - Learning rate: `1e-5`
  - Batch size: `16` (with gradient accumulation = 32)
  - Weight decay: `0.01`
  - EarlyStoppingCallback: Training stopped automatically at **92% accuracy**
  - Epochs: Up to 20
- **Evaluation Strategy**: Evaluated after every epoch, best model saved

**Performance**:
- Accuracy: **87%**
- F1 Score: **87%**
- Precision: **88%**
- Cohen's Kappa: **0.80**

---

## 🔥 Fine-Tuning Details (Cash Transfer Public Policy 2023)

- **Dataset**: 1,344 Moroccan comments from YouTube and Hespress
  - 515 neutral
  - 505 negative
  - 324 positive
- **Split**: 80% training / 20% testing
- **Hyperparameters**:
  - Learning rate: `5e-6`
  - Batch size: `32`
  - Maximum sequence length: `256 tokens`
  - Warmup ratio: `0.1`
  - Early stopping enabled
  - Class weights adjusted for imbalance

**Performance**:
- Accuracy: **91.6%**
- Precision: **0.916**
- Recall: **0.916**
- F1 Score: **0.916**
- Cohen’s Kappa: **0.872**

---

## 📥 How to Use the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("monsifnadir/DarijaBERT-For-Sentiment-Analysis")
tokenizer = AutoTokenizer.from_pretrained("monsifnadir/DarijaBERT-For-Sentiment-Analysis")

text = "فرحت بزاف اليوم الحمد لله"
inputs = tokenizer(text, return_tensors="pt", truncation=True)
outputs = model(**inputs)
predicted_class = outputs.logits.argmax(dim=-1).item()

# Map prediction to label
label_map = {0: "Neutral", 1: "Negative", 2: "Positive"}
print("Predicted Sentiment:", label_map[predicted_class])
