---
license: cc-by-nc-sa-4.0
language: en
base_model: ProsusAI/finbert
tags:
- text-classification
- sentiment-analysis
- financial-sentiment-analysis
- finance
- bert
pipeline_tag: text-classification
widget:
- text: "The company reported record profits and raised its annual dividend by 25%."
  example_title: Positive
- text: "The firm faces serious liquidity concerns and may default on its debt."
  example_title: Negative
- text: "The company will release its quarterly earnings report next Monday."
  example_title: Neutral
---

# FinBERT fine-tuned on Financial PhraseBank

A [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) checkpoint fine-tuned for
3-class sentiment classification (negative / neutral / positive) on the
[Financial PhraseBank](https://www.researchgate.net/publication/251231107_Good_Debt_or_Bad_Debt_Detecting_Semantic_Orientations_in_Economic_Texts)
dataset (Malo et al., 2014).

**This model classifies the sentiment of text. It does not predict prices, returns, or any
tradeable signal.** Sentiment on financial news headlines is not, by itself, a trading
strategy.

Full source code, training notebook, benchmark harness, and deployment instructions:
[karthik-1604/financial-sentiment-finbert-api](https://github.com/karthik-1604/financial-sentiment-finbert-api).

## How to use

```python
from transformers import BertTokenizer, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("Karthik1610/finbert-financial-sentiment")
model = BertForSequenceClassification.from_pretrained("Karthik1610/finbert-financial-sentiment")

text = "The company reported record profits and raised its annual dividend by 25%."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=64, padding="max_length")
with torch.no_grad():
    logits = model(**inputs).logits
probs = torch.softmax(logits, dim=1).squeeze()

id2label = model.config.id2label
pred_id = int(probs.argmax())
print(id2label[pred_id], float(probs[pred_id]))
# positive 0.99...
```

Label order: `{0: "negative", 1: "neutral", 2: "positive"}` (`model.config.id2label`) - note
this is **not** the same order as the base `ProsusAI/finbert` checkpoint's native config
(`{0: positive, 1: negative, 2: neutral}`). Always read the id-to-label mapping from
`model.config` rather than hardcoding it; the repo's `eval/label_mapping.py` does this
defensively for exactly that reason.

## Training data

[Financial PhraseBank](https://www.kaggle.com/datasets/ankurzing/sentiment-analysis-for-financial-news)
(`ankurzing/sentiment-analysis-for-financial-news` on Kaggle) - 4,838 English-language
financial news sentences, annotated by finance professionals with negative / neutral /
positive sentiment. Class distribution: 59.4% neutral, 28.2% positive, 12.5% negative.

## Training procedure

- Base model: `ProsusAI/finbert`
- Max sequence length: 64
- Batch size: 32
- Epochs: 4
- Learning rate: 2e-5, linear warmup (10% of steps) + linear decay
- Loss: weighted cross-entropy (inverse-frequency class weights: negative=1.814,
  neutral=0.382, positive=0.804) to counter class imbalance
- Train/test split: stratified 85/15, seed 42
- Also validated via stratified 5-fold cross-validation (mean accuracy 88.30% +/- 0.85%,
  mean weighted-F1 88.39% +/- 0.79%)

Full training code: `notebooks/finbert_training.ipynb` in the GitHub repo.

## Evaluation results

Scored through a shared, model-agnostic harness (`eval/harness.py` in the repo) against
four baselines - majority-class, TF-IDF+LogisticRegression, `ProsusAI/finbert` zero-shot,
and `bert-base-uncased` fine-tuned the same way - on both the in-domain PhraseBank test
split and an out-of-distribution set ([FiQA](https://huggingface.co/datasets/TheFinAI/fiqa-sentiment-classification)
Task-1 sentiment, thresholded from its native [-1, 1] score).

### PhraseBank test (in-domain)

| Model | Macro-F1 | Accuracy |
|---|---|---|
| **This model (fine-tuned FinBERT)** | **0.883** | **0.886** |
| FinBERT, zero-shot | 0.865 | 0.872 |
| bert-base-uncased, fine-tuned | 0.845 | 0.850 |
| TF-IDF + Logistic Regression | 0.716 | 0.752 |
| Majority-class (floor) | 0.248 | 0.594 |

### FiQA OOD (out-of-distribution)

| Model | Macro-F1 | Accuracy |
|---|---|---|
| FinBERT, zero-shot | **0.482** | 0.498 |
| **This model (fine-tuned FinBERT)** | 0.414 | 0.403 |
| bert-base-uncased, fine-tuned | 0.428 | 0.417 |
| TF-IDF + Logistic Regression | 0.289 | 0.299 |
| Majority-class (floor) | 0.049 | 0.079 |

**Notable finding:** zero-shot FinBERT (no fine-tuning at all) generalizes *better* to the
out-of-distribution FiQA set than this fine-tuned model does, despite scoring lower
in-domain. Fine-tuning on PhraseBank's narrow style (short, 2014-era financial headlines)
buys in-domain accuracy at some cost to robustness on different financial text. See the
[GitHub repo's benchmark section](https://github.com/karthik-1604/financial-sentiment-finbert-api#benchmark)
for the full table, confusion matrices, and cost comparison.

Calibration note: the original FinBERT paper (Araci, 2019) reports ~0.84 F1 across all
PhraseBank agreement levels and ~0.95 F1 on the 100%-agreement subset. Our splits differ
(own seeded 85/15 split, no agreement filtering), so these numbers are not directly
comparable - listed for context only.

## Limitations

- Small dataset (4,838 sentences; ~726 in the test split) - metrics have real variance.
- English-language, 2014-era financial news headlines only. Performance on other
  languages, document types, or more recent terminology is untested (the FiQA OOD result
  above is the closest measurement of that kind of gap).
- Sentiment classification, not a trading signal - see the notice at the top.
- Fine-tuned on data licensed CC-BY-NC-SA-4.0 (Financial PhraseBank via Kaggle); this
  checkpoint is released under the same license and terms (non-commercial, share-alike).

## Citation

If referencing the base model or dataset:

```
@article{araci2019finbert,
  title={FinBERT: Financial Sentiment Analysis with Pre-trained Language Models},
  author={Araci, Dogu},
  journal={arXiv preprint arXiv:1908.10063},
  year={2019}
}

@article{malo2014good,
  title={Good debt or bad debt: Detecting semantic orientations in economic texts},
  author={Malo, Pekka and Sinha, Ankur and Korhonen, Pekka and Wallenius, Jyrki and Takala, Pyry},
  journal={Journal of the Association for Information Science and Technology},
  year={2014}
}
```
