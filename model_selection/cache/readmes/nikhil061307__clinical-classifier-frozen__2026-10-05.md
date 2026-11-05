---
language: en
tags:
- clinical-text
- medical-nlp
- text-classification
- contrastive-learning
library_name: transformers
pipeline_tag: text-classification
---

# Clinical Text Classification Model

## Model Description

Clinical text classification model with frozen contrastive encoder

This model is trained for clinical text classification with the following labels:
Absent, Hypothetical, Present

## Model Architecture

- Base model: Clinical ModernBERT with contrastive learning
- Classification head: 2-layer neural network
- Dropout rate: 0.1

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "your-username/your-model-name"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example usage
text = "Patient presents with [ENTITY]chest pain[/ENTITY] and shortness of breath."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(outputs.logits, dim=-1)

print(f"Predicted class: {predicted_class.item()}")
print(f"Probabilities: {predictions[0].tolist()}")
```

## Label Mapping

```json
{
  "Absent": 0,
  "Hypothetical": 1,
  "Present": 2
}
```

## Training Data

The model was trained on clinical text data with entity mentions marked using [ENTITY] and [/ENTITY] tags.

## Performance

Please refer to the training logs and evaluation metrics provided during model development.

## Citation

If you use this model, please cite appropriately.
