---
language:
- fil
- eng
license: cc-by-4.0
library_name: transformers
tags:
- sentiment-analysis
- code-switching
- taglish
- filipino-nlp
- xlm-roberta
- lexiliksik
- thesis-model
---

# LexCAT: Lexicon-Enhanced Code-Switched Attention Transformer for Tagalog–English Sentiment Analysis

**Author**: Glenn Marcus D. Cinco  
**Institution**: Mapúa University  
**Thesis Title**: LexCAT: A Lexicon-Based Approach for Code-Switching Analysis with Transformers Using XLM-RoBERTa and LexiLiksik  
**Degree**: BS & MS in Computer Science  
**Date**: July 2025  

---

## 🎓 Abstract

LexCAT is a fine-tuned XLM-RoBERTa model enhanced with **LexiLiksik**, a cross-lingual, context-aware Tagalog–English sentiment lexicon developed to handle **intra-sentential sentiment shifts** in code-switched Taglish text. LexCAT achieves **84.31% validation accuracy** on the FiReCS dataset, significantly outperforming monolingual baselines (FilCon: 73.12%, SentiWordNet: 69.52%).

This model is the final output of a thesis that systematically addresses gaps in code-switched sentiment analysis through lexicon development, attention biasing, and real-world fine-tuning.

---

## 🔧 Model Architecture

- **Base Model**: `xlm-roberta-base`
- **Enhancement**: Integrated **LexiLiksik** via:
  - Soft constraints during fine-tuning
  - Attention weight adjustment for sentiment-relevant tokens
  - Metadata-aware pooling (POS, code-switching type)
- **Fine-tuning Dataset**: FiReCS (10,487 Filipino–English code-switched reviews)
- **Evaluation Dataset**: SentiTaglish Products and Services + FiReCS Test Set

---

## 📊 Performance

| Metric       | Value   |
|--------------|---------|
| Accuracy     | 84.31%  |
| F1-Score     | 0.8566  |
| Precision    | 0.8353  |
| Recall       | 0.8574  |
| Cohen’s κ    | 0.83 (from FiReCS annotators) |

> ✅ **Key Strength**: Correctly classifies contrastive phrases like *“Maganda pero expensive”* as **negative**.

---

## 📥 How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "your-hf-username/LexCAT-LexiLiksik-Final"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "sobrang lambot ng burger pero expensive tlga"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
predicted_class = torch.argmax(predictions, dim=1).item()

# Class: 0 = Negative, 1 = Neutral, 2 = Positive
sentiment = ["Negative", "Neutral", "Positive"][predicted_class]
print(f"Predicted Sentiment: {sentiment}")
```
---

## 📚 Citation
```
@mastersthesis{cinco2025lexcat,
  author = {Cinco, Glenn Marcus D.},
  title = {LexCAT: A Lexicon-Based Approach for Code-Switching Analysis with Transformers Using XLM-RoBERTa and LexiLiksik},
  school = {Mapúa University},
  year = {2025},
  month = {July}
}
```