---
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
  - text-classification
  - multi-label-classification
  - clinical
  - forensic
  - overdose-surveillance
pipeline_tag: text-classification
---

# Bio_ClinicalBERT-DrugDetector

A multi-label classifier fine-tuned from [`emilyalsentzer/Bio_ClinicalBERT`](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) to detect substance involvement in death-certificate cause-of-death text, for overdose surveillance research (ROSLA pipeline).

Given free-text cause-of-death fields, it predicts 10 binary labels:

`Methamphetamine`, `Heroin`, `Cocaine`, `Fentanyl`, `Alcohol`, `Prescription.opioids`, `Any Opioids`, `Benzodiazepines`, `Others`, `Any Drugs`

`Any Opioids` and `Any Drugs` are aggregate flags (true if any opioid / any substance is implicated, even when the specific drug isn't independently confirmed elsewhere).

## Performance

Macro F1 = **0.9811** on a held-out external test set (3,335 records, disjoint from training data), evaluated with per-label decision thresholds (not the default 0.5 — see `best_thresholds.json`).

| Label | F1 | Precision | Recall | Support |
|---|---|---|---|---|
| Methamphetamine | 0.964 | 0.930 | 1.000 | 93 |
| Heroin | 0.987 | 0.975 | 1.000 | 78 |
| Cocaine | 0.995 | 0.990 | 1.000 | 381 |
| Fentanyl | 0.999 | 0.998 | 1.000 | 615 |
| Alcohol | 0.992 | 1.000 | 0.983 | 357 |
| Prescription.opioids | 0.992 | 0.992 | 0.992 | 129 |
| Any Opioids | 0.998 | 0.997 | 1.000 | 665 |
| Benzodiazepines | 0.995 | 0.991 | 1.000 | 105 |
| Others | 0.900 | 0.960 | 0.848 | 309 |
| Any Drugs | 0.988 | 0.997 | 0.979 | 967 |

## ⚠️ Required text preprocessing

**This model was trained on normalized text, and needs the same normalization at inference time or performance will silently degrade.** An earlier version of this model, evaluated without matching preprocessing, dropped from ~0.98 to ~0.78 macro F1 on the exact same test set — same model, same weights, just un-normalized input text.

Apply this function to your text before tokenizing:

```python
import re

def clean_bert_text(value) -> str:
    if value is None or (isinstance(value, float) and value != value):  # NaN
        return ""
    s = str(value)
    s = s.replace("\t", " ").replace("\n", " ").replace("\r", " ")
    s = re.sub(r"\bNULL\b", " ", s, flags=re.IGNORECASE)
    s = s.replace(", ", " ")
    s = s.upper()
    return re.sub(r"\s+", " ", s).strip()
```

This strips literal `"NULL"` placeholder tokens, tabs/newlines, a "comma after every word" tokenization artifact present in some upstream data sources, and forces uppercase (the training data has no lowercase examples, so casing is not a signal the model can use — normalizing avoids an artificial train/inference mismatch).

## Usage

```python
import json
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL_ID = "fabriceyhc/Bio_ClinicalBERT-DrugDetector"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_ID)
model.eval()

# Per-label decision thresholds -- do NOT use the default 0.5, thresholds
# were individually tuned per label on a held-out validation split.
import huggingface_hub
thresholds_path = huggingface_hub.hf_hub_download(MODEL_ID, "best_thresholds.json")
thresholds = json.load(open(thresholds_path))

text = clean_bert_text("Acute intoxication due to the combined effects of fentanyl and cocaine")
inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True)
with torch.no_grad():
    probs = torch.sigmoid(model(**inputs).logits)[0]

for i, label in model.config.id2label.items():
    prob = probs[int(i)].item()
    pred = prob >= thresholds[label]
    print(f"{label:<25} prob={prob:.3f}  pred={pred}")
```

## Training data

Fine-tuned on de-identified coroner/medical-examiner cause-of-death text (short phrases, e.g. `"COMPLICATIONS OF FENTANYL AND COCAINE TOXICITY"`), label-corrected via a consistency audit that checked for term/label agreement, logical-invariant violations between specific and aggregate columns, duplicate-text label conflicts, and negation. No names, addresses, or other directly identifying fields are present in the training text.

- Base model: `emilyalsentzer/Bio_ClinicalBERT` (BERT-base architecture, 12 layers, 768 hidden, 12 heads)
- Fine-tuning: 6 epochs, batch size 32, lr 2e-5, weight decay 0.01, early stopping (patience 2) on validation macro F1
- Multi-label classification head (`problem_type="multi_label_classification"`), sigmoid + independent per-label thresholds rather than softmax

## Limitations

- Trained on a specific jurisdiction's death-certificate phrasing conventions; may not generalize to differently structured or differently worded cause-of-death text without re-validation.
- `Others` (F1 0.900) is the weakest label — it's a catch-all category covering a long tail of less-common substances and has the least consistent training signal.
- This is a research/surveillance tool for aggregate public-health monitoring, not a diagnostic or forensic determination instrument, and should not be used as the sole basis for any individual case decision.
- Generic substance-class mentions (e.g. "opioid" without naming a specific drug) are intentionally routed only to the aggregate `Any Opioids`/`Any Drugs` flags, not to a specific-drug column, matching how the underlying data was labeled.
