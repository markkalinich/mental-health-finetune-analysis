---
license: apache-2.0
language:
- en
pipeline_tag: text-classification
tags:
- mental health
- roberta
- multiclass classification
- social media
metrics:
- f1
- recall
- accuracy
- precision
model-index:
  - name: multiMentalRoBERTa 6 class
    results:
      - task:
          type: text-classification
          name: Multiclass mental health detection
        metrics:
          - type: f1
            name: Macro F1
            value: 0.839
          - type: recall
            name: Macro Recall
            value: 0.843
          - type: accuracy
            name: Accuracy
            value: 0.879
---

## Model summary

multiMentalRoBERTa 6 class extends the label space with a stress category: Stress, Anxiety, Depression, PTSD, Suicidal, None. Stress is intentionally broad and overlaps with several conditions. In controlled study this setting reached macro F1 of 0.839 with macro recall of 0.843

## Intended use

- Research on mental health signal detection from public online text
- Safety triage support in peer support platforms with human in the loop
- Educational demos of fair and transparent classification

This model is not a medical device and must not be used for diagnosis or crisis determination without qualified human oversight.


## Labels

Read the mapping from the saved config.

```python
from transformers import AutoConfig
cfg = AutoConfig.from_pretrained("SajjadIslam/multiMentalRoBERTA-6-class")
print(cfg.id2label)
```

## Training data 
Data combines curated Reddit corpora and stress resources, with neutral text for contrast. (More details on the paper)

## Evaluation highlights

- Macro F1: 0.839, Macro Recall: 0.843, Accuracy: 0.879

- Stress achieves strong precision and recall but pulls borderline anxiety and PTSD instances

- Depression and Suicidal remain closely linked and require human confirmation in safety workflows

## Quick start
```python
from transformers import pipeline
clf = pipeline("text-classification", model="SajjadIslam/multiMentalRoBERTA-6-class", top_k=None, truncation=True)
print(clf("I cannot stop panicking and my heart races at night"))
```

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MAX_LENGTH = 512

repo = "SajjadIslam/multiMentalRoBERTA-6-class"
tok = AutoTokenizer.from_pretrained(repo, use_fast=True)
mdl = AutoModelForSequenceClassification.from_pretrained(repo).to(DEVICE).eval()

id2label = {int(k): v for k, v in mdl.config.id2label.items()}


def classify_6(text: str):
    enc = tok(text, truncation=True, padding="max_length", max_length=MAX_LENGTH, return_tensors="pt").to(DEVICE)
    logits = mdl(**enc).logits
    probs = torch.softmax(logits, dim=-1)[0].cpu().numpy()
    pid = int(torch.argmax(logits, dim=-1).item())
    return {
        "predicted_class": id2label[pid],
        "confidence": float(probs[pid]),
        "probabilities": {id2label[i]: float(probs[i]) for i in range(len(probs))}
    }
```

## Limitations and risks
- Labels from social media contain noise and reflect self disclosure conventions
- Close semantic link between depression and suicidal may yield conservative false positives
- Domain and culture transfer has not been clinically validated

## Responsible use
Use with human review and escalation pathways. Document decision policies, monitor drift, and avoid deployment in settings that could result in harm without professional support. Summary findings and safety notes are discussed in the paper.

## Citation
If you use this model, please cite: 

```bibtex
@inproceedings{islam2025multimentalroberta,
  title={multiMentalRoBERTa: A Fine-tuned Multiclass Classifier for Mental Health Disorder},
  author={Islam, KM Sajjadul and Fields, John and Madiraju, Praveen},
  booktitle={2025 IEEE International Conference on Big Data (BigData)},
  pages={3255--3264},
  year={2025},
  organization={IEEE}
}
```