---
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- token-classification
- ner
- clinical-trials
- biomedical
---

# PubMedBERT/BiomedBERT fine-tuned for CHIA clinical trial eligibility NER

Fine-tuned `microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext` for
named entity recognition on clinical trial eligibility criteria (CHIA corpus),
as part of a course NLP project comparing fine-tuned biomedical transformers
vs. GPT-4 prompting.

- **Code / full writeup**: https://github.com/jatinpsingh/NER_Clinical_Trial_Eligibility/tree/main/pmb
- **Base model**: PubMedBERT-base (renamed BiomedBERT), Gu et al. 2021
- **Task**: token classification, 31 labels (`O` + 15 entity types x B/I)
- **Data**: CHIA eligibility criteria, team's shared fixed split (10,006 train / 1,240 val / 1,163 test sentences -- fold 0 of a 10-fold CV scheme, see below)

## Hyperparameters (matching Li et al. 2022, Table 3)

| | |
|---|---|
| Learning rate | 5e-5 |
| Batch size | 8 |
| Epochs | 10 |
| Max sequence length | 256 |
| Adam epsilon | 1e-8 |

## Results

**This checkpoint's own fold** (entity-level, test set):

| | Precision | Recall | F1 |
|---|---|---|---|
| Strict (exact span match) | 0.639 | 0.674 | 0.656 |
| Relaxed (type + overlap match) | 0.750 | 0.791 | 0.770 |

**Full 10-fold cross-validation** (mean +/- std across all 10 folds -- the
number directly comparable to Li et al. 2022's own 10-fold-averaged
reporting; the weights hosted in this repo are from one of these 10 folds,
not a checkpoint averaged across them):

| | Precision | Recall | F1 |
|---|---|---|---|
| Strict | 0.657 +/- 0.013 | 0.682 +/- 0.021 | 0.669 +/- 0.013 |
| Relaxed | 0.758 +/- 0.014 | 0.787 +/- 0.024 | 0.772 +/- 0.015 |

Both this checkpoint's own score and the 10-fold mean exceed Li et al. 2022's
published PubMedBERT numbers on Chia (0.622 strict / 0.744 relaxed).

## Usage

```python
from transformers import AutoModelForTokenClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ptanwar/pubmedbert-chia-ner")
model = AutoModelForTokenClassification.from_pretrained("ptanwar/pubmedbert-chia-ner")
```

## Known limitations

- The hosted weights are one fold's model, not a checkpoint averaged/ensembled
  across the 10-fold CV run -- treat the single-fold numbers above as this
  specific checkpoint's performance, and the 10-fold mean +/- std as the more
  rigorous estimate of the approach's true performance.
- Weakest on rare/ambiguous types (`Mood`, `Observation`, `Reference_point`) -- see the full writeup for error analysis.
