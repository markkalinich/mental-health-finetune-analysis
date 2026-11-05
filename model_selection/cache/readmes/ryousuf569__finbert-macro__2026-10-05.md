---
language: en
license: cc-by-nc-sa-4.0
base_model: ProsusAI/finbert
pipeline_tag: text-classification
tags:
  - finance
  - financial-nlp
  - sentiment-analysis
  - macroeconomics
  - bert
metrics:
  - f1
  - accuracy
---

# finbert-macro

FinBERT fine-tuned to read macroeconomic headlines by their effect on equities, without losing the
base model's grip on company news.

ProsusAI/finbert scores 39.0 macro-F1 on the macro test set, which is near chance for three classes.
This checkpoint scores 68.8, and corporate news improves at the same time, 70.2 to 84.0.

## Labels

`0 = positive`, `1 = negative`, `2 = neutral`, the same ids as the base model.

On macro text the label is market impact, not tone. Dovish maps to positive, hawkish maps to
negative. A hot CPI print or a strong payrolls number comes back `negative` here because it implies
tighter policy. If you want literal sentiment, use ProsusAI/finbert instead.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

name = "ryousuf569/finbert-macro"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name).eval()

texts = ["Powell signals rate cuts are coming as price pressures ease",
         "Payrolls blow past forecasts, wage growth accelerates",
         "GDP growth unchanged from prior quarter"]
with torch.no_grad():
    logits = model(**tok(texts, padding=True, truncation=True,
                         max_length=64, return_tensors="pt")).logits
for t, p in zip(texts, logits.argmax(-1).tolist()):
    print(model.config.id2label[p], "|", t)

# positive | Powell signals rate cuts are coming as price pressures ease
# negative | Payrolls blow past forecasts, wage growth accelerates
# neutral  | GDP growth unchanged from prior quarter
```

"Jobless claims rise, cooling a tight labor market" also comes back positive, which is the mapping
working as intended rather than a bug.

## Results

Macro and corporate are always reported separately. Averaging them would hide a macro gain paid for
by forgetting corporate news.

| model | macro acc | macro F1 | corporate acc | corporate F1 |
|---|---|---|---|---|
| ProsusAI/finbert | 38.06 | 39.03 | 71.60 | 70.24 |
| finbert-macro | 68.89 | 68.82 | 85.03 | 83.97 |
| change | +30.83 | +29.79 | +13.43 | +13.73 |

Macro test set is 6,101 real held-out rows, corporate is 4,169. No class collapsed on either set.
Lowest per-class F1 is 65.9 on macro, 81.3 on corporate.

## Seed replication

One seed cannot separate a real gap from run-to-run noise, so the winning configuration (u6@32k: 6
unfrozen encoder blocks, 32,000 training rows) and the runner-up (u4@20k: 4 blocks, 20,000 rows)
were each retrained from scratch at seeds 42, 1 and 2.

**u6@32k beats u4@20k by 1.87 points of macro-F1 and 1.67 points of corporate F1. Both gaps survive
the change of seed, and both domains improve at once, so this is not a macro-for-corporate trade.**

| config | seed 42 | seed 1 | seed 2 | mean | std | min to max |
|---|---|---|---|---|---|---|
| macro-F1, u4@20k | 67.59 | 67.29 | 67.41 | 67.43 | 0.15 | 67.29 to 67.59 |
| macro-F1, u6@32k | 68.82 | 69.34 | 69.73 | 69.30 | 0.46 | 68.82 to 69.73 |
| corporate F1, u4@20k | 81.39 | 82.06 | 82.32 | 81.92 | 0.48 | 81.39 to 82.32 |
| corporate F1, u6@32k | 83.97 | 82.66 | 84.16 | 83.60 | 0.82 | 82.66 to 84.16 |

The macro gap of 1.87 points is wider than the widest seed range of 0.91, and the corporate gap of
1.67 is wider than its widest range of 1.50. Every u6@32k seed beats every u4@20k seed on both
metrics. Three seeds gives a range, not a significance test, so there is no p-value here and none
should be inferred.

The published weights are the seed 42 run, the seed fixed before the replication study. Seed 2
scored higher at 69.73, but picking it would be selecting a checkpoint on the test set.

## What did not replicate

Four other metrics moved more between seeds than between configurations, so they were dropped from
the decision and are listed here only as description.

| metric | gap between configs | widest seed range |
|---|---|---|
| probe accuracy (48 probes) | 8.33 | 14.58 |
| minimal pairs solved (of 18) | 1.67 | 7.00 |
| polarity-agreeing probe accuracy (14 probes) | 7.14 | 7.14 |
| Financial PhraseBank F1 | 12.31 | 13.29 |

The probe suite is small enough that this is structural. With 14 polarity-agreeing probes, one probe
changing its answer is worth 7.14 points, which is the entire gap. More probes would fix this. More
seeds would not.

## Limitations

The PhraseBank comparison is not clean. This model gets 73.1 PhraseBank macro-F1 against the base
model's 96.3, but ProsusAI/finbert was itself fine-tuned on Financial PhraseBank, so 96.3 is close
to its training score. PhraseBank was never trained on here and every pool was filtered against it
for leakage. Read 73.1 as retained company-level ability rather than a 23-point regression.

Two things changed at once between u6@32k and u4@20k, unfreeze depth and training rows. The gain is
real and repeatable, but this experiment cannot say which of the two produced it.

1,817 of the 20,800 macro training rows are synthetic templates. They are scored as a separate
evaluation set and never folded into the reported macro number, but they are in the training mix.

Scope is short English headlines and policy sentences, 64 tokens. Central-bank language from 1996 to
2024 dominates the macro side. Not built for filings, transcripts, long documents or other
languages. The output is a text label, not a market forecast.

## Training

32,000 rows, 20,800 macro and 11,200 corporate, sampled without replacement. The corporate share is
an anchor against forgetting. Everything is frozen except the top 6 encoder blocks, the pooler and
the head, since full fine-tuning is the fastest way to lose corporate competence. Cross-entropy with
inverse-frequency class weights, lr 2e-5, weight decay 0.01, warmup 0.1, batch 32, fp16.

Both a macro and a corporate validation set are scored each epoch. The selected epoch maximizes
macro-F1 while corporate validation F1 stays within 0.01 of the base checkpoint. Epoch 5 of 7 won
and its weights were restored, against a ceiling of 16 epochs with early stopping. Training took 145
minutes on one GTX 1660 Ti (6 GB, Turing).

On that card `torch.cuda.is_bf16_supported()` returns True but counts emulated bf16, which is
unusably slow, so this was trained in fp16.

## Data and license

Macro pool: World Central Banks, 16,870 rows, CC BY-NC-SA 4.0. FOMC / Trillion Dollar Words, 1,660
rows, CC BY-NC 4.0. FinMarBa headlines, 749 rows, MIT. Synthetic templates, 1,848 rows.

Corporate pool: SEntFiN, Twitter financial news and FiQA, 14,591 rows, all MIT.

Splits are date-blocked per source where dates exist and grouped-random otherwise.

The largest macro source is CC BY-NC-SA 4.0, so this model is released under CC BY-NC-SA 4.0,
non-commercial and share-alike. That is stricter than the base model's Apache-2.0 licence, and the
restriction comes from the training data.

## Reproducing the seed study

```bash
python seed_rep.py --criterion macro_floored --seeds 42 1 2 \
  --config "u4@20k:unfreeze=4,total=20000" \
  --config "u6@32k:unfreeze=6,total=32000" --yes
```
