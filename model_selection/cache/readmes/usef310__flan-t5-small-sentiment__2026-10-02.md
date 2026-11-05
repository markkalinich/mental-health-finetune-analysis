---
language: en
tags:
- sentiment-analysis
- flan-t5
- text-classification
license: apache-2.0
datasets:
- imdb
---

# FLAN-T5 Small - Sentiment Analysis

Fine-tuned version of `google/flan-t5-small` for sentiment analysis on IMDB reviews.

## Model Details
- **Base Model:** google/flan-t5-small
- **Task:** Binary sentiment classification (positive/negative)
- **Dataset:** IMDB movie reviews (300 training samples)
- **Accuracy:** 85.00%

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("usef310/flan-t5-small-sentiment")
model = AutoModelForSeq2SeqLM.from_pretrained("usef310/flan-t5-small-sentiment")

text = "This movie was amazing!"
inputs = tokenizer("sentiment: " + text, return_tensors="pt")
outputs = model.generate(**inputs)
prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(prediction)  # Output: positive or negative
```

## Training Details
- Epochs: 3
- Batch size: 4 (with gradient accumulation)
- Learning rate: 5e-5
- Optimizer: AdamW
