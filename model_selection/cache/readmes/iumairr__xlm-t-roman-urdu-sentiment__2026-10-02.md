---
language:
- en
- ur
tags:
- sentiment-analysis
- roman-urdu
- xlm-roberta
pipeline_tag: text-classification
license: mit
---

# XLM-T Roman Urdu Sentiment Analyzer

Fine-tuned model for Roman Urdu sentiment analysis.

## Performance
- Accuracy: 71.00%
- F1-Score: 0.706

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained('iumairr/xlm-t-roman-urdu-sentiment')
tokenizer = AutoTokenizer.from_pretrained('iumairr/xlm-t-roman-urdu-sentiment')
```
