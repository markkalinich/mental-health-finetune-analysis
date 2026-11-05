---
language:
- en
license: cc-by-nc-4.0
library_name: transformers
pipeline_tag: text-classification
base_model: microsoft/deberta-v3-large
tags:
- emotion-classification
- multi-label-classification
- deberta-v2
- safetensors
datasets:
- go_emotions
- empathetic_dialogues
---

# Text Emotion Detector

This is a multi-label emotion classifier for conversational English text. It is based on `microsoft/deberta-v3-large`, adapted on Empathetic Dialogues, fine-tuned on GoEmotions, and then optionally tuned on hard examples for subtle distress/self-dismissal style inputs.

The model predicts 28 GoEmotions labels and is intended to return the top emotions for a piece of text rather than a single exclusive class.

## Install

```bash
pip install torch transformers huggingface_hub
```

## Basic Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo = "JamieYCR/text-emotion-detector-final"

tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo)
model.eval()

text = "I can't believe she actually said yes!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    logits = model(**inputs).logits[0]
    probs = torch.sigmoid(logits)

top_k = 3
top = probs.argsort(descending=True)[:top_k]

for idx in top:
    label = model.config.id2label[int(idx)]
    score = float(probs[idx])
    print(f"{label}: {score:.4f}")
```

## Calibrated Probabilities

This repo includes `temperature.json`, which was fitted during calibration. Plain `transformers` loading does not apply it automatically. To use calibrated probabilities, divide logits by the temperature before applying sigmoid:

```python
import json
import torch
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo = "JamieYCR/text-emotion-detector-final"

tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo)
model.eval()

temperature_path = hf_hub_download(repo_id=repo, filename="temperature.json")
with open(temperature_path, "r", encoding="utf-8") as f:
    temperature = float(json.load(f)["temperature"])

text = "I'm so tired of pretending everything is fine."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    logits = model(**inputs).logits[0]
    probs = torch.sigmoid(logits / temperature)

top = probs.argsort(descending=True)[:3]
results = [
    (model.config.id2label[int(i)], float(probs[i]))
    for i in top
]

print(results)
```

## Batch Inference

```python
texts = [
    "Good morning, I hope you have a wonderful day.",
    "Ugh, fine. Whatever.",
]

inputs = tokenizer(
    texts,
    return_tensors="pt",
    padding=True,
    truncation=True,
    max_length=128,
)

with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.sigmoid(logits)

for text, row in zip(texts, probs):
    top = row.argsort(descending=True)[:3]
    print(text)
    for idx in top:
        print(f"  {model.config.id2label[int(idx)]}: {float(row[idx]):.4f}")
```

## Labels

The model uses the GoEmotions label set:

`admiration`, `amusement`, `anger`, `annoyance`, `approval`, `caring`, `confusion`, `curiosity`, `desire`, `disappointment`, `disapproval`, `disgust`, `embarrassment`, `excitement`, `fear`, `gratitude`, `grief`, `joy`, `love`, `nervousness`, `optimism`, `pride`, `realization`, `relief`, `remorse`, `sadness`, `surprise`, `neutral`.

## Notes

- This is a multi-label classifier, so use `torch.sigmoid`, not `softmax`.
- The model was trained for top-k emotion ranking. For most applications, inspect the top 3-5 labels.
- The uploaded `temperature.json` can be used for calibrated probabilities.
- Empathetic Dialogues is licensed for non-commercial use, so treat this model as non-commercial unless retrained without that data.

## Example Repository ID

```python
repo = "JamieYCR/text-emotion-detector-final"
```
