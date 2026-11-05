
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
- name: xlm-roberta-large-tass-sentiment-bs8
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: TASS (Spanish Twitter)
      type: tass
    metrics:
    - type: f1
      value: 0.6876
      name: F1 Score
    - type: accuracy
      value: 0.6888
      name: Accuracy
    - type: precision
      value: 0.6874
      name: Precision
    - type: recall
      value: 0.6888
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
- **Batch Size:** 8
- **Epochs:** 10
- **Learning Rate:** 2e-05
- **Weight Decay:** 0.01
- **Max Sequence Length:** 256
- **Class Balancing:** Weighted Cross-Entropy Loss
- **Early Stopping:** Enabled (patience=3)

## Performance (Test Set)

| Metric | Score |
|--------|-------|
| F1 Score | 0.6876 |
| Accuracy | 0.6888 |
| Precision | 0.6874 |
| Recall | 0.6888 |

## Training History (Validation Set)

Metrics per epoch during training:

| Epoch | Loss | Accuracy | F1 Score | Precision | Recall |
|-------|------|----------|----------|-----------|--------|
| 1 | 1.0415 | 0.3796 | 0.2859 | 0.2294 | 0.3796 |
| 2 | 0.8871 | 0.5949 | 0.5811 | 0.6149 | 0.5949 |
| 3 | 0.9549 | 0.5528 | 0.4932 | 0.6216 | 0.5528 |
| 4 | 0.9607 | 0.6059 | 0.5713 | 0.6096 | 0.6059 |
| 5 | 0.9084 | 0.6335 | 0.6301 | 0.6315 | 0.6335 |
| 6 | 0.8614 | 0.6722 | 0.6702 | 0.6696 | 0.6722 |
| 7 | 0.8683 | 0.6798 | 0.6774 | 0.6762 | 0.6798 |
| 8 | 1.1485 | 0.6798 | 0.6786 | 0.6815 | 0.6798 |
| 9 | 1.3851 | 0.6888 | 0.6876 | 0.6874 | 0.6888 |
| 10 | 1.5043 | 0.6770 | 0.6762 | 0.6759 | 0.6770 |


## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Cargar modelo y tokenizer
tokenizer = AutoTokenizer.from_pretrained("tu-usuario/xlm-roberta-large-tass-sentiment-bs8")
model = AutoModelForSequenceClassification.from_pretrained("tu-usuario/xlm-roberta-large-tass-sentiment-bs8")

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
classifier = pipeline('sentiment-analysis', model='tu-usuario/xlm-roberta-large-tass-sentiment-bs8')

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

