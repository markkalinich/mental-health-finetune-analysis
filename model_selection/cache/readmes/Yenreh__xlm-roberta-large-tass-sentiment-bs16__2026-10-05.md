
---
language: es
tags:
- sentiment-analysis
- spanish
- xlm-roberta
- tass
- twitter
datasets:
- TASS
metrics:
- f1
- accuracy
- precision
- recall
model-index:
- name: xlm-roberta-large-tass-sentiment-bs16
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: TASS (Spanish Twitter)
      type: tass
    metrics:
    - type: f1
      value: 0.6899
      name: F1 Score
    - type: accuracy
      value: 0.6901
      name: Accuracy
    - type: precision
      value: 0.6904
      name: Precision
    - type: recall
      value: 0.6901
      name: Recall
---

# XLM-RoBERTa Large Fine-tuned for Spanish Sentiment Analysis (TASS)

## Model Description

This model is a fine-tuned version of [FacebookAI/xlm-roberta-large](https://huggingface.co/FacebookAI/xlm-roberta-large) 
for sentiment analysis on Spanish Twitter data (TASS dataset).

## Training Details

- **Base Model:** xlm-roberta-large
- **Task:** Multi-class Sentiment Classification (Negative/Neutral/Positive)
- **Dataset:** TASS (Twitter Analysis Sentiment Seminar)
- **Training Samples:** 4,636
- **Validation Samples:** 1,159
- **Test Samples:** 1,449
- **Batch Size:** 16
- **Epochs:** 10
- **Learning Rate:** 2e-05
- **Weight Decay:** 0.01
- **Max Sequence Length:** 256
- **Class Balancing:** Weighted Cross-Entropy Loss
- **Early Stopping:** Enabled (patience=3)

## Performance (Test Set)

| Metric | Score |
|--------|-------|
| F1 Score | 0.6899 |
| Accuracy | 0.6901 |
| Precision | 0.6904 |
| Recall | 0.6901 |

## Training History (Validation Set)

Metrics per epoch during training:

| Epoch | Loss | Accuracy | F1 Score | Precision | Recall |
|-------|------|----------|----------|-----------|--------|
| 1 | 0.8022 | 0.6908 | 0.6796 | 0.6845 | 0.6908 |
| 2 | 0.7347 | 0.6853 | 0.6846 | 0.6850 | 0.6853 |
| 3 | 0.7679 | 0.6736 | 0.6671 | 0.6677 | 0.6736 |
| 4 | 0.8447 | 0.6901 | 0.6899 | 0.6904 | 0.6901 |
| 5 | 0.9078 | 0.6950 | 0.6863 | 0.6879 | 0.6950 |
| 6 | 1.2134 | 0.6846 | 0.6829 | 0.6826 | 0.6846 |
| 7 | 1.4088 | 0.6846 | 0.6833 | 0.6831 | 0.6846 |


## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Cargar modelo y tokenizer
tokenizer = AutoTokenizer.from_pretrained("tu-usuario/xlm-roberta-large-tass-sentiment-bs16")
model = AutoModelForSequenceClassification.from_pretrained("tu-usuario/xlm-roberta-large-tass-sentiment-bs16")

# Ejemplo de uso
text = "Me encanta este producto, es excelente"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=256)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1).item()

labels = {0: "Negativo", 1: "Neutral", 2: "Positivo"}
print(f"Sentimiento: {labels[predicted_class]}")
print(f"Confianza: {predictions[0][predicted_class].item():.4f}")
```

### Como Pipeline

```python
from transformers import pipeline

# Usar como pipeline
classifier = pipeline('sentiment-analysis', model='tu-usuario/xlm-roberta-large-tass-sentiment-bs16')

result = classifier("Me encanta este producto, es excelente")
print(result)
# Output: [{'label': 'LABEL_2', 'score': 0.95}]
# LABEL_0 = Negativo, LABEL_1 = Neutral, LABEL_2 = Positivo
```

## Labels

- `0` (LABEL_0): Negative sentiment
- `1` (LABEL_1): Neutral sentiment
- `2` (LABEL_2): Positive sentiment

## Training Configuration

The model was trained with weighted loss to handle class imbalance.

Distribution in training set (estimated):
- Negative samples: ~1854 (~40%)
- Neutral samples: ~1391 (~30%)
- Positive samples: ~1391 (~30%)

## Limitations and Bias

- This model is specifically trained on Spanish Twitter data
- Performance may vary on other Spanish text domains
- The model classifies sentiment into three categories (negative, neutral, positive)
- May reflect biases present in the TASS Twitter dataset

