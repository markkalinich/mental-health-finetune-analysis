---
language: ne
license: apache-2.0
base_model: xlm-roberta-base
tags:
- sentiment-analysis
- nepali
- text-classification
- xlm-roberta
- fine-tuned
datasets:
- IRIIS-RESEARCH/Sentiment-Analysis-Nepali
metrics:
- accuracy
- f1
---

# Nepali Sentiment Analysis — Fine-Tuned XLM-RoBERTa

Fine-tuned XLM-RoBERTa-base for binary sentiment classification on Nepali text (Devanagari script), achieving 88.5% accuracy and 0.88 F1 score — a +38 percentage point improvement over the zero-shot baseline.

## Model Details

- **Base model:** xlm-roberta-base
- **Task:** Binary sentiment classification (positive/negative)
- **Language:** Nepali (ne) — Devanagari script
- **Fine-tuned by:** Ujwal Dahal (ujwaldahal.com.np)
- **License:** Apache 2.0

## Performance

| Metric | Baseline (Zero-Shot) | Fine-Tuned | Improvement |
|--------|---------------------|------------|-------------|
| Accuracy | 50.50% | 88.50% | +38.0pp |
| F1 Score | 0.00 | 0.88 | +0.88 |
| Error Rate | 49.50% | 11.50% | -38.0pp |

Evaluated on 200 random samples from the IRIIS-RESEARCH test set.

Confusion matrix: [[90, 11], [12, 87]] — balanced errors across classes.

## Training Details

- **Dataset:** IRIIS-RESEARCH/Sentiment-Analysis-Nepali (65,106 train / 16,279 test)
- **Epochs:** 2
- **Batch size:** 16 (effective 64 with gradient accumulation)
- **Learning rate:** 2e-5 (AdamW with linear warmup)
- **Warmup:** 10% of total steps (~407 steps)
- **Gradient clipping:** max norm 1.0
- **Training time:** ~50 minutes on Google Colab T4 GPU
- **Implementation:** Manual PyTorch training loop (not HuggingFace Trainer API)

## How to Use

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_name = "Ujju33/nepali-sentiment-xlm-roberta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        confidence, predicted_class = torch.max(probs, dim=1)
    
    labels = {0: "negative", 1: "positive"}
    return {
        "sentiment": labels[predicted_class.item()],
        "confidence": round(confidence.item(), 4)
    }

# Example
result = predict_sentiment("यो फिल्म एकदमै राम्रो छ!")
print(result)  # {'sentiment': 'positive', 'confidence': 0.9964}
```

## Known Limitations

- **Domain:** Trained on COVID-19 news headlines (2020-2021). May not generalize well to social media, product reviews, or literature.
- **Short texts:** Ambiguous texts under 10 words have higher error rates.
- **Long texts:** Texts over 512 tokens are truncated.
- **Script:** Optimized for Devanagari; romanized Nepali not tested.

## Training Code

Full training notebook available at:
https://github.com/ujju1124/nepali-sentiment-finetuning

## Live Demo

This model powers the Nepali News Intelligence Agent:
https://huggingface.co/spaces/Ujju33/nepali-news-agent
