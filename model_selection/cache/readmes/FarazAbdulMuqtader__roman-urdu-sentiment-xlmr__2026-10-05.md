---
license: mit
language:
- ur
base_model: xlm-roberta-base
tags:
- sentiment-analysis
- roman-urdu
- text-classification
pipeline_tag: text-classification
---

# Roman Urdu Sentiment Analysis (XLM-RoBERTa)

Fine-tuned XLM-RoBERTa model for sentiment analysis on Roman Urdu (Urdu written in Latin script) — the informal script most commonly used across Pakistani social media, messaging, and reviews.

🚀 **[Try the live demo](https://huggingface.co/spaces/FarazAbdulMuqtader/roman-urdu-sentiment-demo)**

📦 **[GitHub repo](https://github.com/FarazAbdulMuqtader/Roman-Urdu-Sentiment-Analysis)** (full pipeline: preprocessing, training, evaluation scripts)

## Model description

This model classifies Roman Urdu text into one of three sentiment classes: **Positive**, **Negative**, or **Neutral**. It's built on `xlm-roberta-base`, fine-tuned on a large Roman Urdu sentiment corpus to handle the inconsistent spelling and English code-mixing typical of informal Roman Urdu text.

## How to use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "FarazAbdulMuqtader/roman-urdu-sentiment-xlmr"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

label_names = ["Positive", "Negative", "Neutral"]

def predict_sentiment(text):
    encoding = tokenizer(text, padding="max_length", truncation=True, max_length=128, return_tensors="pt")
    with torch.no_grad():
        logits = model(**encoding).logits
    probs = torch.softmax(logits, dim=1).squeeze()
    predicted_id = torch.argmax(probs).item()
    return label_names[predicted_id], probs[predicted_id].item()

label, confidence = predict_sentiment("wah kya baat hai zabardast")
print(f"{label} ({confidence*100:.1f}%)")
```

## Training data

- Source: [`Khubaib01/RomanUrdu-NLP-Sentiment-Corpus`](https://huggingface.co/datasets/Khubaib01/RomanUrdu-NLP-Sentiment-Corpus)
- ~134K raw samples, cleaned down to ~129,377 rows after preprocessing (deduplication, length filtering, normalization)
- Split: 103,501 train / 25,876 held-out test (stratified 80/20)

## Training procedure

- Base model: `xlm-roberta-base`
- 3 epochs, batch size 16, learning rate 2e-5, AdamW optimizer
- Trained on a Kaggle T4 GPU
- Max sequence length: 128 tokens

## Evaluation results

Evaluated on the 25,876-row held-out test set.

**Overall accuracy: 81%**

| Label    | Precision | Recall | F1-score | Support |
|----------|-----------|--------|----------|---------|
| Positive | 0.81      | 0.82   | 0.82     | 7,252   |
| Negative | 0.84      | 0.85   | 0.85     | 10,504  |
| Neutral  | 0.78      | 0.76   | 0.77     | 8,120   |
| **Accuracy** | | | **0.81** | 25,876 |
| Macro avg | 0.81 | 0.81 | 0.81 | 25,876 |
| Weighted avg | 0.81 | 0.81 | 0.81 | 25,876 |

**Confusion matrix** (rows = actual, columns = predicted):

|          | Positive | Negative | Neutral |
|----------|----------|----------|---------|
| Positive | 5,977    | 508      | 767     |
| Negative | 588      | 8,920    | 996     |
| Neutral  | 802      | 1,177    | 6,141   |

## Limitations

- **Neutral is the weakest class** (78% precision, 76% recall) — most confusion happens between Neutral and the other two classes, which is expected since neutral sentiment in short, code-mixed social text is inherently ambiguous (sarcasm, mild opinions, and rhetorical statements often blur the line).
- **Negative is the most reliably distinguished class** (84% precision, 85% recall).
- The model was trained and evaluated specifically on Roman Urdu. Since it's built on multilingual XLM-RoBERTa, it also handles plain English and code-mixed text reasonably, but accuracy on those inputs hasn't been formally evaluated.
- Performance on heavily sarcastic, ironic, or highly context-dependent text may be lower than the aggregate numbers suggest, as these are known hard cases for sentiment classifiers in general.
- The training corpus reflects informal Pakistani social media text; performance may differ on more formal Roman Urdu writing (e.g. news, official communication).

## Intended use

Built to address a low-resource, code-mixed language largely underserved by mainstream NLP tooling. Suitable for sentiment tagging of Roman Urdu social media posts, reviews, and messages. Not intended for high-stakes decision-making without human review.