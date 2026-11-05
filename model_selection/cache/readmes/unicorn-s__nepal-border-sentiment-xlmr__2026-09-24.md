---
license: mit
language:
- ne
- en
base_model: xlm-roberta-base
pipeline_tag: text-classification
tags:
- sentiment-analysis
- nepali
- low-resource-nlp
- political-sentiment
---

# Nepal Border Sentiment Classifier

XLM-RoBERTa-base fine-tuned for 3-class sentiment classification (positive/neutral/negative) on Nepali and English YouTube comments discussing the Nepal–India border dispute.

## Performance

- **Accuracy:** ~50% on gold-standard evaluation set (manually verified)
- **Random baseline:** 33% (3-class)
- **F1 (weighted):** ~0.50

## Dataset

Trained on the [Nepal Border Sentiment Dataset](https://huggingface.co/datasets/unicorn-s/nepal-border-sentiment-dataset) — ~2100 YouTube comments scraped from 17 Nepali news and commentary channels.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = AutoModelForSequenceClassification.from_pretrained("unicorn-s/nepal-border-sentiment-xlmr")
tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-base")

text = "Your Nepali or English comment here"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
labels = ['negative', 'neutral', 'positive']
print({labels[i]: float(probs[0][i]) for i in range(3)})
```

## Limitations

- Small training set (~1800 silver-labeled samples)
- Single annotator for gold-standard evaluation
- Translation quality varies for Nepali slang and code-switched text
- Class imbalance in training data skewed toward negative sentiment

## Citation / Contribution

This is published as a baseline for low-resource Nepali political sentiment analysis. Contributions of additional labeled data and improved baselines are welcome — see the [GitHub repo](https://github.com/samirasharma/nepal-border-sentiment).