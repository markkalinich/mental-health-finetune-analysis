---
language:
- ru
- uk
- en
- zh
- ja
- ar
- es
- de
- fr
license: cc-by-nc-4.0
base_model: cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual
tags:
- sentiment-analysis
- multilingual
- news
pipeline_tag: text-classification
library_name: transformers
---

# Regional multilingual news sentiment

Fine-tuned **XLM-RoBERTa-base** for 3-class news headline sentiment in
Russian, Ukrainian, Kazakh, Chinese, Japanese, Arabic, and Western
European languages.

## Why this model exists

The downstream OSINT dashboard scores ~200 news headlines every five
minutes for its overall threat indicator.  VADER (the upstream choice)
returns 0.0 for every Cyrillic or CJK headline, which zeroed out 25 %
of the threat formula for any non-English-dominant region.  This
fine-tune restores that signal for Cyrillic without regressing Latin
text — English keeps VADER under the script-aware router in
`oracle_service.compute_sentiment`.

## Labels

| id | name     | what it covers |
|----|----------|----------------|
| 0  | negative | casualty / conflict / disaster / strong-negative coverage |
| 1  | neutral  | routine / procedural / non-evaluative coverage |
| 2  | positive | resolution / cooperation / strong-positive coverage |

## Training data

Mix of three public sources (~30.9 K train / 10.7 K val / 16.2 K test):

* `MonoHime/ru_sentiment_dataset` — 190 K RU reviews+news, label
  convention remapped 0/1/2 ↔ neg/neu/pos.
* `tyqiangz/multilingual-sentiments` — ZH (2.5 K), JA (2.5 K), AR/EN/
  ES/DE/FR (~3.7 K each).
* `cardiffnlp/tweet_sentiment_multilingual` — Twitter sentiment in
  EN/FR/DE/ES/AR/HI/IT/PT.

Recipe: `scripts/prepare_sentiment_dataset.py` in the GitHub repo.

## Training

* Apple-Silicon MPS, batch 8 + grad_accum 2 (effective 16), max_length
  96, lr 1e-5, warmup 6 %, weight decay 0.01.
* HF Trainer, `save_strategy="steps"`, `save_steps = steps_per_epoch
  // 10` → checkpoint every 0.1 epoch.
* Early-stopped at 1.1 epoch (patience 4 from best @0.6 epoch).
* Recipe: `scripts/train_sentiment.py` in the GitHub repo.

## Evaluation

* `val_f1_macro` (best checkpoint): **0.655**
* `test_f1_macro` (final): **0.597**
* `test_accuracy` (final): **0.600**

Test is lower than val because the test split has a heavier
Twitter/cardiff share where the Twitter-tuned baseline pre-train leaks
through.

## Smoke results vs VADER baseline

On a held-out hand-picked set of Russian news headlines spanning the
three classes:

| Class | VADER (baseline) | this model |
|---|---|---|
| Negative coverage | 0.000 (VADER returns 0 for any Cyrillic input) | −0.45 to −0.75 |
| Positive coverage | 0.000 | +0.40 to +0.55 |
| Neutral / procedural coverage | 0.000 | ≈ 0.00 (correctly close to zero) |

Cyrillic gains are dramatic — the model recovers a signal that VADER
silently dropped to zero.  English and CJK have small regressions vs
strong VADER and dictionary baselines on news-specific phrasings, so
the regional-fork runtime routes only Cyrillic input through this
model and keeps VADER + a hand-curated CJK character dict for the
other scripts.

## Usage in the regional fork

```bash
huggingface-cli login
uv run --group ml python scripts/download_model.py
# adapter auto-discovers backend/data/models/sentiment-finetuned/final/
SENTIMENT_ML_BACKEND=auto uv run uvicorn main:app --reload
```

## Direct usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
tok = AutoTokenizer.from_pretrained("ssb000ss/regional-sentiment-ru")
mdl = AutoModelForSequenceClassification.from_pretrained("ssb000ss/regional-sentiment-ru")
clf = pipeline("text-classification", model=mdl, tokenizer=tok)

# Pass a Russian / Ukrainian / Kazakh / Chinese / Japanese / Arabic /
# Spanish / German / French headline.  Output: 3-class sentiment with
# confidence in [0..1].
print(clf("<your headline here>"))
# [{'label': 'negative' | 'neutral' | 'positive', 'score': 0.5x}]
```

## License

CC-BY-NC-4.0 (non-commercial), inherited from the regional fork it
ships with.

## Citation

If you use this model, please cite the upstream base model
(`cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual`) and the
public sentiment datasets listed under **Training data** above.
