---
language: en
license: mit
base_model: Simonlee711/Clinical_ModernBERT
pipeline_tag: text-classification
tags:
- clinical-nlp
- medical
- cytomegalovirus
- radiology-reports
- sentence-classification
---

# Clinical_ModernBERT — CMV sentence classifier

Fine-tuned [Simonlee711/Clinical_ModernBERT](https://huggingface.co/Simonlee711/Clinical_ModernBERT)
for detecting cytomegalovirus (CMV) positivity in histopathology reports. This is a **sentence-level** binary classifier (`CMV_POSITIVE` vs `CMV_NEGATIVE`).


## Intended use

- Input: one sentence from a clinical report.
- Output: probability that the sentence indicates CMV positivity.
- Report-level classification: a report is classified as positive if any sentence within the report is predicted as positive; otherwise, it is classified as negative.

Not a medical device; outputs must not be used for clinical decision-making
without expert review.

## Usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

repo = "Amber-666/clinical-modernbert-cmv"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo).eval()

def sentence_probs(sentences, batch_size=8):
    probs = []
    for i in range(0, len(sentences), batch_size):
        enc = tok(sentences[i:i + batch_size], truncation=True, padding=True,
                  max_length=512, return_tensors="pt")
        with torch.no_grad():
            logits = model(**enc).logits
        probs.extend(torch.softmax(logits, dim=-1)[:, 1].tolist())
    return probs

# report-level decision 
report_sentences = ["...", "..."]          # the report split into sentences
p_report = max(sentence_probs(report_sentences))
is_cmv_positive = p_report >= 0.5
```

## Training

- Base model: `Simonlee711/Clinical_ModernBERT`
- Data: 10,073 manually annotated sentences from 279 CMV histopathology reports.
- Hyperparameters: lr 3e-5, weight decay 0, no warmup, linear LR decay,
  batch size 8, max length 512, 3 epochs, seed 168


## Citation

TODO: add paper citation when available.
