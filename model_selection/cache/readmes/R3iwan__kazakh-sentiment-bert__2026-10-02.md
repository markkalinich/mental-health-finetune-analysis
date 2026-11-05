---
language:
- kk
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- kazakh
- bert
- multilingual
pipeline_tag: text-classification
datasets:
- R3iwan/entertainment-reviews-kazakh
base_model: google-bert/bert-base-multilingual-cased
model-index:
- name: kazakh-sentiment-bert
  results: []
---

# Kazakh Sentiment Analysis Model

A sentiment analysis model for Kazakh text, fine-tuned on a dataset of entertainment reviews.

## Model Description

This model is based on `bert-base-multilingual-cased` and fine-tuned for sentiment classification of Kazakh text into three classes:
- **positive** (positive sentiment)
- **neutral** (neutral sentiment)
- **negative** (negative sentiment)

## Usage

### Using transformers pipeline

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="R3iwan/kazakh-sentiment-bert")

text = "Бұл фильм маған ұнамады"
result = classifier(text)
print(result)
```

### Direct model usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "R3iwan/kazakh-sentiment-bert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Бұл фильм маған ұнамады"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

predicted_class = torch.argmax(predictions, dim=-1).item()
labels = ["negative", "neutral", "positive"]
print(f"Predicted: {labels[predicted_class]}")
print(f"Confidence: {predictions[0][predicted_class].item():.2%}")
```

## Training

The model was trained on the [R3iwan/entertainment-reviews-kazakh](https://huggingface.co/datasets/R3iwan/entertainment-reviews-kazakh) dataset with the following parameters:

- **Base Model**: `bert-base-multilingual-cased`
- **Epochs**: 2
- **Batch Size**: 8
- **Learning Rate**: 2.5e-5 (with linear decay)
- **Train/Validation/Test Split**: ~80/10/10

## Metrics

- **Accuracy**: 100% on test set
- **Task**: Text Classification (Sentiment Analysis)

## Limitations

The model is trained on a limited dataset of entertainment reviews and may perform better on similar texts. For other domains, additional fine-tuning may be required.

## Author

R3iwan

## License

Apache 2.0
