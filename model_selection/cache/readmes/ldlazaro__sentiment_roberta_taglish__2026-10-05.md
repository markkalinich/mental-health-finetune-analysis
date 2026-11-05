---
library_name: transformers
tags: ["text-classification", "sentiment-analysis", "taglish"]
---

# Sentiment RoBERTa Taglish

A fine-tuned RoBERTa model for sentiment analysis on Taglish (Tagalog + English) Shopee comments. Developed as part of a project for DOST-STII-IRAD by an APC College group.

---

## Model Details

- **Base model:** `dost-asti/RoBERTa-tl-sentiment-analysis`  
- **Tokenizer:** `AutoTokenizer.from_pretrained("dost-asti/RoBERTa-tl-sentiment-analysis")`  
- **Task:** Sequence classification (Sentiment analysis)  
- **Labels:**  
  - `0` = Negative  
  - `1` = Neutral  
  - `2` = Positive  
- **Dataset used:** `letijo03/sentiment-analysis-taglish-shopee-comment` (train split)  
- **Framework:** PyTorch  

---

### Training & Evaluation

#### Evaluation Metrics

**Test Set Performance:**
- Accuracy: 0.8630
- Macro F1 Score: 0.6939
- Weighted Average F1 Score: 0.8686

---

### Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load tokenizer and model from Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained("ldlazaro/sentiment_roberta_taglish")
model = AutoModelForSequenceClassification.from_pretrained("ldlazaro/sentiment_roberta_taglish")

# Example inference
text = "Ang ganda ng araw na ito!"
inputs = tokenizer(text, return_tensors="pt")
pred = model(**inputs).logits.argmax(-1)
print(pred.item())




