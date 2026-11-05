
---
library_name: transformers
pipeline_tag: text-classification
tags:
- emotion-classification
- mental-health
- roberta
- pytorch
- text-classification
---

# Mental Health Emotion Classifier

This model is a RoBERTa-based multi-class emotion classifier trained for a mental health chatbot.

## Labels

- sadness
- joy
- love
- anger
- fear
- surprise

## Intended use

The model is used as the **Emotion Classification** module in a RAG-based mental health support chatbot.

Recommended pipeline:

```text
User message
→ language detection
→ translate to English if non-English
→ emotion classifier
→ intent classifier
→ RAG retrieval
→ final response generation
```

## Important note

The model was trained on an English emotion dataset.
For Arabic, French, Spanish, German, or other languages, translate the user input to English first, then run the classifier.

## Metrics

- Test Accuracy: 0.921
- Test Macro-F1: 0.8897

## Example

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo_id = "MariamMohsen112/mental-health-emotion-roberta"

tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)
model.eval()

text = "I feel anxious and I cannot sleep"

inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)

probs = torch.softmax(outputs.logits, dim=-1)[0]
pred_id = int(torch.argmax(probs).item())

print(model.config.id2label[pred_id], float(probs[pred_id]))
```
