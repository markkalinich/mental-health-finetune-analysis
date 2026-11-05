---
language: en
license: mit
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
  - pytorch
datasets:
  - custom
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# CopiumMeter 🧪

A text classification model that detects **copium** (denial/coping mechanisms), **sarcasm**, **sincere** statements, and **neutral** text.

## Labels

| Label | Description | Example |
|-------|-------------|---------|
| 0 - Copium 💀 | Denial, coping, dismissive | "Whatever, I didn't want it anyway" |
| 1 - Sarcastic 🙃 | Irony, mocking, exaggeration | "Oh wow, what a surprise" |
| 2 - Sincere 😌 | Genuine, honest, appreciative | "Thank you so much, this really helped" |
| 3 - Neutral 😐 | Factual, informational | "The meeting is at 3pm" |

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="kurtesianplane/copium-meter")

result = classifier("Whatever, I didn't even want that job anyway")
print(result)
# [{'label': 'LABEL_0', 'score': 0.95}]  # Copium detected!
```

### Direct Usage

```python
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

tokenizer = DistilBertTokenizer.from_pretrained("kurtesianplane/copium-meter")
model = DistilBertForSequenceClassification.from_pretrained("kurtesianplane/copium-meter")

text = "Oh sure, that's definitely going to work"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs, dim=1).item()

labels = ["Copium 💀", "Sarcastic 🙃", "Sincere 😌", "Neutral 😐"]
print(f"Prediction: {labels[pred]} ({probs[0][pred]:.1%} confidence)")
```

## Model Details

- **Base Model**: distilbert-base-uncased
- **Task**: Multi-class text classification (4 classes)
- **Training Data**: Curated dataset from Reddit comments
- **Framework**: PyTorch + Transformers

## Training

Trained using the Hugging Face Transformers library with:
- 10,000 samples (2,500 per class)
- 3 epochs
- AdamW optimizer (lr=5e-5)
- Batch size: 16

## Limitations

- Trained primarily on English Reddit-style text
- May not generalize well to formal writing or other languages
- Sarcasm detection is context-dependent and challenging

## License

MIT License
