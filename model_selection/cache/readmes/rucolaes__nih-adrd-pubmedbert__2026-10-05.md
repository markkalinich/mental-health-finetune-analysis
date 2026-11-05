---
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
language: en
pipeline_tag: text-classification
tags:
- biomedical
- alzheimer
- dementia
- grant-classification
- pubmedbert
- text-classification
metrics:
- pr_auc
- f1
---

# NIH AD/ADRD Classifier (PubMedBERT)

A binary text classifier that predicts whether a research project's **title + abstract**
belongs to NIH's Alzheimer's Disease / Alzheimer's Disease-Related Dementias (AD/ADRD)
research portfolio. Fine-tuned from
[PubMedBERT / BiomedBERT](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext)
on NIH's own portfolio labels — not a general "neurodegenerative disease" classifier.

## Model description

- **Base model**: `microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext` (BERT-base,
  domain vocabulary pretrained from scratch on PubMed abstracts + PMC full text)
- **Task**: binary sequence classification, input = `(title, abstract)` as a tokenizer pair
  (proper `token_type_ids` segmentation, not a manually concatenated string)
- **Max sequence length**: 512 tokens
- **Output**: softmax probability of the positive (AD/ADRD) class

## Training data

Source: [NIH ExPORTER](https://reporter.nih.gov/exporter) bulk data (Projects + Abstracts,
joined on `APPLICATION_ID`), fiscal years **2018–2024**.

**Label**: positive iff the award's `NIH_SPENDING_CATS` field contains one of these three
exact RCDC category strings (an explicit allowlist, not a substring heuristic):
- `Alzheimer's Disease` (RCDC code 40)
- `Alzheimer's Disease Related Dementias (ADRD)` (code 3254)
- `Alzheimer's Disease including Alzheimer's Disease Related Dementias (AD/ADRD)` (code 3246)

This is NIH's own strict scope — it does **not** include Parkinson's disease, ALS, or
Huntington's disease, which NIH tracks under their own separate RCDC categories.

**Preprocessing**:
- Exact-duplicate `(title, abstract)` pairs removed (renewal/resubmission text reused
  verbatim across fiscal years — ~50% of the raw corpus)
- Split **grouped by `CORE_PROJECT_NUM`** (stratified, 70/15/15) so that no NIH project's
  multi-year renewals cross the train/val/test boundary
- Train-set negatives: guaranteed inclusion of two targeted hard-negative cohorts (NIH
  awards coded Parkinson's/ALS/Huntington's/VCID but not AD/ADRD; awards mentioning
  amyloid-family vocabulary but not AD/ADRD-labeled), plus random fill to a 10:1
  negative:positive ratio. Validation and test sets keep the natural class distribution.

| Split | Rows | Positive | Rate |
|---|---|---|---|
| train | 125,961 | 11,451 | 9.1% |
| val | 42,431 | 2,411 | 5.7% |
| test | 42,034 | 2,513 | 6.0% |

## Training procedure

- Loss: class-weighted cross-entropy (weight = train-set negative:positive ratio)
- Optimizer: AdamW, lr 2e-5, weight decay 0.01, warmup ratio 0.1
- 3 epochs, batch size 16 (train) / 32 (eval), fp16
- Model selection: best checkpoint by validation PR-AUC (positive rate ≈ 6-9%, so PR-AUC
  rather than accuracy)
- Hardware: single A10G GPU (~70 minutes)

## Evaluation

Held-out test set (natural class distribution, never used for training or model selection):

| Metric | Value |
|---|---|
| PR-AUC | 0.960 |
| F1 (threshold 0.5) | 0.929 |

A near-duplicate leakage audit (TF-IDF cosine similarity between every test row and its
nearest training neighbor) found PR-AUC stable (0.960 → 0.959) after excluding the most
similar 1-2% of test rows, so this is not inflated by train/test text overlap.

**On threshold choice**: the raw softmax output is not a calibrated posterior probability —
training uses negative downsampling plus inverse-frequency class weighting, which shifts
the effective training prevalence well above NIH's true ~6% base rate. Use PR-AUC/ROC-AUC
for ranking, and pick an operating threshold from a validation set matching your deployment
distribution rather than assuming 0.5. Platt scaling (fit on the logit, not the raw
probability) is a reasonable post-hoc calibration if you need an actual probability estimate.

## Intended use and limitations

- Trained and evaluated on **NIH-style grant abstracts**. Applied informally to EU/Horizon
  (CORDIS) project text as a cross-domain check; agreement with an independent LLM-based
  classification (Claude + GPT, matching disease scope) was substantial-to-almost-perfect
  (Cohen's κ ≈ 0.82), but this is not a validated cross-domain benchmark — treat
  out-of-domain predictions as a signal to review, not a final decision.
- Known residual failure mode: occasional false positives on text containing surface-level
  token overlap with AD-associated vocabulary in an unrelated context (e.g., generic
  AI/technology-infrastructure projects with broad "health" framing). A prior version of
  this model also collided on abbreviation overlap (e.g. "AD" as *Anno Domini* in historical
  text); this is substantially reduced but not eliminated by the hard-negative training here.
- Designed as a **high-recall prefilter / triage signal**, not a sole final-decision system —
  best used alongside expert or LLM review of flagged candidates, particularly for anything
  outside the strict NIH AD/ADRD definition it was trained on.

## How to use

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("rucolaes/nih-adrd-pubmedbert")
model = AutoModelForSequenceClassification.from_pretrained("rucolaes/nih-adrd-pubmedbert").eval()

title = "..."
abstract = "..."
inputs = tokenizer(title, abstract, truncation=True, max_length=512, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
prob_adrd = torch.softmax(logits, dim=1)[0, 1].item()
```
