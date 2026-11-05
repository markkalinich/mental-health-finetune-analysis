
---
language:
  - sl
  - en
  - hr
license: other
license_name: see-attribution
base_model: EMBEDDIA/crosloengual-bert
library_name: transformers
pipeline_tag: text-classification
tags:
  - emotion-recognition
  - multi-label-classification
  - slovene
  - ekman
datasets:
  - go_emotions
widget:
  - text: "Oj kako sem srečen da delam z GaMS!"
  - text: "Kako ogabno pripravljena hrana... kje ti je higiena??"
  - text: "Sem se najprej ustrašil da je to res..."
  - text: "Žalostno. Lahko bi vam dali vsaj ledeni čaj Erik."
---

# CSEBERT for Ekman emotion recognition in Slovene

Multi-label emotion classifier for Slovene text, covering Ekman's six basic emotions
plus a neutral label.

The model is [CroSloEngual BERT](https://huggingface.co/EMBEDDIA/crosloengual-bert)
fine-tuned on the **English** GoEmotions corpus with labels mapped to Ekman's taxonomy,
then applied to Slovene. No Slovene training data was used — the model relies on
CroSloEngual BERT's shared Slovene/Croatian/English representation to transfer the task
across languages.

Produced as part of an undergraduate thesis at the Faculty of Computer and Information
Science, University of Ljubljana.

## Labels

Seven independent binary outputs, not a distribution. A comment may carry several labels
or none.

| id | label | Slovene |
|---|---|---|
| 0 | anger | jeza |
| 1 | disgust | gnus |
| 2 | fear | strah |
| 3 | joy | sreča |
| 4 | sadness | žalost |
| 5 | surprise | presenečenje |
| 6 | neutral | nevtralno |

The GoEmotions 27-label taxonomy was collapsed to Ekman using the official
`ekman_mapping.json` grouping.

## Usage

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_ID = "<uporabnik>/csebert-emotions-sl"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID).eval()

text = "Kako ogabno pripravljena hrana... kje ti je higiena??"
with torch.no_grad():
    enc = tokenizer(text, truncation=True, max_length=128, return_tensors="pt")
    probs = torch.sigmoid(model(**enc).logits)[0]

for i, p in enumerate(probs):
    print(f"{model.config.id2label[i]:12s} {p:.3f}")
```

Reported results use a decision threshold of **0.5**.

## Training

| | |
|---|---|
| Base model | `EMBEDDIA/crosloengual-bert` |
| Training data | GoEmotions, English split, Ekman mapping |
| Objective | multi-label, `BCEWithLogitsLoss` |
| Learning rate | 3e-05 |
| Batch size | 16 |
| Epochs | 10, early stopping with patience 3 on validation macro-F1 |
| Max sequence length | 128 |
| Precision | fp16 |
| Seed | 42 |

Selected from a grid over learning rate {1e-05, 2e-05, 3e-05, 5e-05} and batch size
{16, 32, 64} by **validation** macro-F1.

## Input preprocessing

This matters for getting comparable results. The evaluation data was preprocessed
before inference:

- named entities replaced with `[NAME]`
- digit strings replaced with `[NUMBER]`, currency amounts with `[CURRENCY]`
- URLs, `<3` and leading `>` removed, `&` expanded to *in*
- ASCII art removed, comments kept to 3–30 tokens

Raw user text will not match this distribution. Expect somewhat lower quality on input
that has not been through the same cleanup, particularly text containing names or
numbers.

## Intended use

Research and demonstration: exploratory analysis of emotion in Slovene social media
text, and as a baseline for further work on Slovene emotion recognition.

**Not** intended for decisions about individuals — moderation, hiring, clinical or
psychological assessment, or anything where a wrong label affects someone.

## Attribution

- Base model: [CroSloEngual BERT](https://huggingface.co/EMBEDDIA/crosloengual-bert),
  Ulčar and Robnik-Šikonja
- Training data: [GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions),
  Demszky et al. (2020)
