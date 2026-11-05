---
language: en
license: mit
tags:
- bert
- text-classification
- sentiment-analysis
- english
- imdb
datasets:
- imdb
metrics:
- accuracy
model-index:
- name: finetuned-bert-imdb
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      type: imdb
      name: IMDB
    metrics:
    - type: accuracy
      value: 0.802
      name: Test Accuracy
pipeline_tag: text-classification
---

# BERT Fine-tuned for IMDB Sentiment Analysis

This model is a fine-tuned version of `bert-base-uncased` on the IMDB movie reviews dataset for sentiment analysis (binary classification). It can predict whether a movie review is positive or negative.

## Model description

- **Model type:** BERT (bert-base-uncased)
- **Language:** English
- **Task:** Sentiment Analysis
- **Training Dataset:** IMDB Movie Reviews
- **License:** MIT

### Training Hyperparameters

The model was trained with the following parameters:
- Learning rate: 2e-5
- Batch size: 16
- Number of epochs: 3
- Weight decay: 0.01
- Maximum sequence length: 64
- Training samples: 2000 (balanced: 1000 positive, 1000 negative)
- Optimizer: AdamW

### Training Results

- **Accuracy on test set:** 80.2%
- **Training loss:** 0.381

## Intended uses & limitations

### Intended uses

This model is designed for:
- Sentiment analysis of movie reviews and similar text content
- Binary classification (positive/negative) of English text
- Research and educational purposes

### Limitations

- The model is trained on movie reviews and might not perform as well on other domains
- Limited to English language text
- Maximum input length is 512 tokens
- May exhibit biases present in the training data

## How to use

Here's how to use the model with PyTorch:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("xanderIV/finetuned-bert-imdb")
tokenizer = AutoTokenizer.from_pretrained("xanderIV/finetuned-bert-imdb")

# Prepare your text
texts = [
    "This movie was fantastic! Great acting and amazing plot.",
    "Terrible waste of time. Poor acting and confusing story."
]

# Tokenize the input
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)

# Get predictions
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=1)
    labels = torch.argmax(predictions, dim=1)

# Process results
for text, pred, probs in zip(texts, labels, predictions):
    sentiment = "positive" if pred.item() == 1 else "negative"
    confidence = probs[pred].item() * 100
    print(f"\nText: {text}")
    print(f"Sentiment: {sentiment} (confidence: {confidence:.1f}%)")
```

### Example Outputs

```
Text: This movie was fantastic! Great acting and amazing plot.
Sentiment: positive (confidence: 97.7%)

Text: Terrible waste of time. Poor acting and confusing story.
Sentiment: negative (confidence: 98.4%)
```

## Training Data

The model was fine-tuned on a subset of the IMDB dataset:
- 2000 training examples (1000 positive, 1000 negative reviews)
- 500 test examples
- Reviews were truncated to 64 tokens to optimize training speed

## Evaluation Results

The model achieved the following results on the test set:
- Accuracy: 80.2%
- Loss: 0.482

## Bias & Limitations

This model may exhibit biases inherent to the IMDB dataset:
- Movie-specific vocabulary and expressions
- Cultural biases in movie reviews
- English-language bias
- Internet and entertainment domain bias

## Citation

If you use this model, please cite:
```bibtex
@misc{finetuned-bert-imdb,
  author = {xanderIV},
  title = {BERT Fine-tuned for IMDB Sentiment Analysis},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Model Hub},
  howpublished = {\url{https://huggingface.co/xanderIV/finetuned-bert-imdb}}
}
```