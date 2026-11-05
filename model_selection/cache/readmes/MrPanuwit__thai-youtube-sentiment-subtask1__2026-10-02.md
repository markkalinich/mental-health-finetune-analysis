---
language: th
license: apache-2.0
tags:
- sentiment-analysis
- thai
- youtube-comments
- bert
library_name: transformers
pipeline_tag: text-classification
---

# MrPanuwit/thai-youtube-sentiment-subtask1

## Model Description

Thai sentiment analysis model trained on YouTube comments for sentiment classification.

## Model Details

- **Model Type:** BERT-based text classification
- **Language:** Thai (th)
- **Task:** sentiment classification
- **Base Model:** bert-base-multilingual-cased
- **Training Data:** YouTube comments dataset

## Labels

- Neutral
- Optimistic
- Pessimistic

## Usage

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load model and tokenizer
tokenizer = BertTokenizer.from_pretrained("MrPanuwit/thai-youtube-sentiment-subtask1")
model = BertForSequenceClassification.from_pretrained("MrPanuwit/thai-youtube-sentiment-subtask1")

# Example usage
text = "วิดีโอนี้สนุกมาก"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=-1)
    
print(f"Prediction: {predictions.item()}")
```

## Training Details

- **Framework:** PyTorch + Transformers
- **Optimizer:** AdamW
- **Max Sequence Length:** 128

## Limitations

- Trained specifically on Thai YouTube comments
- May not perform well on other text domains
- Limited to the specific sentiment categories in training data

## Citation

```
@misc{thai-youtube-sentiment,
  author = {Your Name},
  title = {Thai YouTube Comment Sentiment Analysis},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/MrPanuwit/thai-youtube-sentiment-subtask1}
}
```
