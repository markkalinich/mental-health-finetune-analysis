---
language:
  - en
  - bn
tags:
  - sentiment-analysis
  - cross-lingual
  - xlm-roberta
  - text-classification
datasets:
  - glue
  - sepidmnorozy/Bengali_sentiment
metrics:
  - accuracy
  - f1
library_name: transformers
pipeline_tag: text-classification
---

# arif481/crosslingual-sentiment-model

A cross-lingual sentiment analysis model fine-tuned on XLM-RoBERTa for binary sentiment classification (positive/negative) across en, bn.

## Model Description

This model performs sentiment classification across multiple languages using transfer learning. It was trained using the **combined** strategy.

### Supported Languages
- English (en)
- Bengali (bn)

### Training Mode: combined
Trained on combined English and Bengali data for multilingual learning.

## Usage

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="arif481/crosslingual-sentiment-model")

# English
result = classifier("This movie is absolutely fantastic!")
print(result)  # [{'label': 'positive', 'score': 0.99}]

# Bengali
result = classifier("এই সিনেমাটি অসাধারণ ছিল!")
print(result)  # [{'label': 'positive', 'score': 0.95}]
```

## Training

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("arif481/crosslingual-sentiment-model")
tokenizer = AutoTokenizer.from_pretrained("arif481/crosslingual-sentiment-model")
```


## Metrics

| Metric | Value |
|--------|-------|
| Accuracy | N/A |
| Macro F1 | N/A |
| Precision | N/A |
| Recall | N/A |


## Limitations

- Binary classification only (positive/negative)
- May not perform well on neutral sentiment
- Bengali performance may be lower than English due to limited training data

## Citation

If you use this model, please cite:

```bibtex
@misc{crosslingual-sentiment,
  author = {Cross-Lingual Sentiment Team},
  title = {Cross-Lingual Sentiment Analysis Model},
  year = {2024},
  publisher = {Hugging Face},
  url = {https://huggingface.co/arif481/crosslingual-sentiment-model}
}
```

## License

This model is released under the MIT License.
