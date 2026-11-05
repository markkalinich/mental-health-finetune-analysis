
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
      value: 0.4098
      name: F1 Score
    - type: accuracy
      value: 0.5079
      name: Accuracy
    - type: precision
      value: 0.5283
      name: Precision
    - type: recall
      value: 0.5079
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
- **Max Sequence Length:** 128
- **Class Balancing:** Weighted Cross-Entropy Loss
- **Early Stopping:** Enabled (patience=3)

## Performance (Test Set)

| Metric | Score |
|--------|-------|
| F1 Score | 0.4098 |
| Accuracy | 0.5079 |
| Precision | 0.5283 |
| Recall | 0.5079 |

## Training History (Validation Set)

Metrics per epoch during training:

| Epoch | Loss | Accuracy | F1 Score | Precision | Recall |
|-------|------|----------|----------|-----------|--------|
| 1 | 1.1272 | 0.3819 | 0.3235 | 0.4629 | 0.3819 |
| 2 | 1.0278 | 0.4931 | 0.3947 | 0.3591 | 0.4931 |
| 3 | 1.0981 | 0.3991 | 0.2382 | 0.3610 | 0.3991 |
| 4 | 1.0494 | 0.4440 | 0.3561 | 0.3265 | 0.4440 |
| 5 | 1.0650 | 0.4405 | 0.3174 | 0.3696 | 0.4405 |


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

## Citation

If you use this model, please cite:

```
@misc{xlm-roberta-tass-sentiment,
  author = {Your Name},
  title = {XLM-RoBERTa Large Fine-tuned for Spanish Sentiment Analysis},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/tu-usuario/xlm-roberta-large-tass-sentiment-bs16}}
}
```
