---
license: apache-2.0
language:
- en
metrics:
- f1
- recall
base_model:
- sentence-transformers/all-roberta-large-v1
tags:
- mental health
- roberta
- classification
- social media
- peer support system
datasets:
- custom
model-index:
- name: multiMentalRoBERTa 5 class
  results:
  - task:
      type: text-classification
      name: Multiclass mental health detection
    metrics:
    - type: f1
      name: Macro F1
      value: 0.87
    - type: recall
      name: Macro Recall
      value: 0.869
    - type: accuracy
      name: Accuracy
      value: 0.881
pipeline_tag: text-classification
---

## Model summary

multiMentalRoBERTa 5 class is a fine tuned RoBERTa large model for multiclass detection of common mental health conditions from short social media texts. It classifies into five categories that exclude stress to reduce overlap and improve separability. In controlled experiments it achieved macro F1 of 0.870 and macro recall of 0.869, outperforming strong baselines and domain adapted transformers.

## Intended use

- Research on mental health signal detection from public online text
- Safety triage support in peer support platforms with human in the loop
- Educational demos of fair and transparent classification

This model is not a medical device and must not be used for diagnosis or crisis determination without qualified human oversight.

## Labels

The exact mapping is stored in the config and should be read programmatically. The five classes correspond to: Anxiety, Depression, PTSD, Suicidal, and None. The learned numeric ids come from the saved config.

```python
from transformers import AutoConfig
cfg = AutoConfig.from_pretrained("SajjadIslam/multiMentalRoBERTA-5-class")
print(cfg.id2label)  # authoritative mapping
```

## Training data and setup

Data combines curated Reddit corpora and stress resources, with neutral text for contrast. The five class setting removes stress to reduce linguistic overlap that otherwise confounds anxiety and PTSD and also the depression and suicidal boundary. (More details on the paper)

## Evaluation highlights

- Five class setup improves consistency compared to six class due to removal of diffuse stress category
- Macro F1: 0.870, Macro Recall: 0.869, Accuracy: 0.881 on held out test data
- Depression and Suicidal remain closely related and should be reviewed by humans in sensitive workflows

## Quick start

#### Transformers pipeline
```python
from transformers import pipeline
clf = pipeline("text-classification", model="SajjadIslam/multiMentalRoBERTA-5-class", top_k=None, truncation=True)
text = "I feel stuck and cannot sleep from worry."
print(clf(text))
```

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MAX_LENGTH = 512

repo = "SajjadIslam/multiMentalRoBERTA-5-class"
tok = AutoTokenizer.from_pretrained(repo, use_fast=True)
mdl = AutoModelForSequenceClassification.from_pretrained(repo).to(DEVICE).eval()

id2label = {int(k): v for k, v in mdl.config.id2label.items()}

@torch.no_grad()
def classify_5(text: str):
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