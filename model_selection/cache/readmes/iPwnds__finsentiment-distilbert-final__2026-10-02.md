---
library_name: transformers
tags:
- finance
- sentiment-analysis
- financial-sentiment
- finbert
- bert
- text-classification
- financial-phrasebank
- twitter-financial-news
language:
- en
base_model: ProsusAI/finbert
license: apache-2.0
datasets:
- takala/financial_phrasebank
- zeroshot/twitter-financial-news-sentiment
metrics:
- f1
---

# finsentiment-distilbert-final

A financial sentiment classifier fine-tuned from **FinBERT** (`ProsusAI/finbert`) on a combined **Financial PhraseBank + Twitter Financial News Sentiment** dataset with class-weighted loss and post-hoc temperature calibration. Classifies financial text into **positive**, **negative**, or **neutral** sentiment with a weighted F1 of **0.8949** on a held-out test set that — unlike v1's — includes informal, social-media-style financial text.

This is the second-generation successor to [`iPwnds/finsentiment-distilbert`](https://huggingface.co/iPwnds/finsentiment-distilbert). The repo name is kept for continuity with the FinSight CLI's model pipeline, but the underlying architecture changed from DistilBERT to FinBERT and the training data roughly sextupled to cover informal/social text, which v1 never saw.

It runs **fully locally** — no API keys required.

---

## Model Details

### Model Description

`finsentiment-distilbert-final` is a sequence classification fine-tune of `ProsusAI/finbert` (itself a BERT-base model pre-trained on financial corpora) trained on the union of the Financial PhraseBank AllAgree subset and the Twitter Financial News Sentiment dataset, with **class-weighted cross-entropy loss** to counteract the underrepresentation of the `negative` class, and **temperature scaling** applied post-training to calibrate confidence scores.

Where v1 was trained purely on clean, formally-worded analyst sentences, this model was explicitly built to also handle **informal financial text** — tickers, emoji, abbreviations, social-media phrasing — which v1's FPB-only training never exposed it to.

The model is the sentiment backbone of the [FinSight Bloomberg Terminal CLI](https://github.com/iPwnds/bloomberg-terminal) — a Bloomberg-style terminal that scores every news headline in real time to feed an aggregate sentiment signal into the AI analyst's stock reports.

- **Developed by:** Florian Braun ([@iPwnds](https://huggingface.co/iPwnds))
- **Model type:** Encoder-only transformer — sequence classification
- **Language:** English
- **License:** Apache 2.0
- **Fine-tuned from:** [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert)

### Model Sources

- **Repository:** [github.com/iPwnds/bloomberg-terminal](https://github.com/iPwnds/bloomberg-terminal)
- **Training notebook:** [`notebooks/FinSentiment_Classifier_Full.ipynb`](https://github.com/iPwnds/bloomberg-terminal/blob/main/notebooks/FinSentiment_Classifier_Full.ipynb)
- **Previous version:** [`iPwnds/finsentiment-distilbert`](https://huggingface.co/iPwnds/finsentiment-distilbert) (v1 — DistilBERT, FPB-only)
- **Companion generative model:** [`iPwnds/finanalyst-qwen1.5b-final`](https://huggingface.co/iPwnds/finanalyst-qwen1.5b-final)

---

## Uses

### Direct Use

The model classifies individual financial sentences — news headlines, tweets, earnings call snippets, analyst commentary — into one of three sentiment classes:

| Label | ID | Meaning |
|---|---|---|
| `positive` | 0 | Bullish / favourable news |
| `negative` | 1 | Bearish / adverse news |
| `neutral` | 2 | Factual / no clear directional signal |

Note the label-ID mapping is **inherited from FinBERT** and differs from v1 (`positive=0, negative=1, neutral=2` here vs. `negative=0, neutral=1, positive=2` in v1) — always read labels by name via `model.config.id2label`, never assume the ID ordering.

It handles both formal financial writing (press releases, analyst reports) and informal text (tickers, emoji, social-media phrasing) noticeably better than v1.

### Downstream Use

In the FinSight CLI the model is loaded as a `transformers` pipeline in `analysis/sentiment.py` and called on every headline returned for a given ticker. Individual scores are then aggregated into a per-ticker sentiment summary (overall label + confidence-weighted score) that is passed as context to the generative analyst LLM.

It can also be used standalone as a drop-in financial sentiment scorer for any NLP pipeline:

```python
from transformers import pipeline

clf = pipeline("text-classification", model="iPwnds/finsentiment-distilbert-final")

headlines = [
    "Apple reports record quarterly earnings, beats Wall Street estimates",
    "$TSLA mooning rn, shorts getting absolutely destroyed 🚀🚀",
    "Tesla misses delivery targets as EV demand slows globally",
]

for h in headlines:
    result = clf(h)[0]
    print(f"{result['label']:8s}  ({result['score']:.2%})  {h}")
```

### Out-of-Scope Use

- **Long documents** — the model was trained on short sentences/tweets (max 128 tokens). Passing full articles or paragraphs without sentence splitting will degrade performance.
- **Non-English text** — `ProsusAI/finbert` and the training data are English-only.
- **Non-financial domains** — sentiment language in finance is domain-specific (e.g. "profit warning" is clearly negative; "restructuring" is ambiguous). The model is not calibrated for general-purpose sentiment.
- **Fine-grained or aspect-based sentiment** — the model produces document-level labels only, not aspect- or entity-level sentiment.

---

## Bias, Risks, and Limitations

- **Class imbalance:** even after combining FPB and Twitter data, `neutral` dominates the training set (7,276 / 11,356 = 64%) while `negative` remains the smallest class. Class-weighted loss (see below) mitigates but does not eliminate this — `positive` and `negative` still show lower per-class F1 (0.8517 and 0.8122) than `neutral` (0.9270) on the test set.
- **Lower headline F1 than v1** (0.8949 vs. v1's 0.9737) — but the two numbers are **not directly comparable**: v1 was evaluated only on clean, single-agreement Financial PhraseBank sentences, while this model is evaluated on a much larger, harder, mixed test set that includes noisy social-media text. Direct like-for-like comparison would require re-evaluating v1 on the same combined test split.
- **Twitter label remapping:** the Twitter Financial News dataset's own label scheme (`0=Bearish, 1=Bullish, 2=Neutral`) was manually remapped to FinBERT's scheme; any systematic annotation bias in the source dataset (financial Twitter/StockTwits-style discourse, ~2022 era) carries through.
- **Domain shift:** financial language evolves with market conditions and terminology; sentences from novel domains (crypto, ESG, AI hardware narratives) may be under-represented in both source datasets.
- **Base model:** `ProsusAI/finbert` is itself a fine-tune of BERT-base on a financial corpus (Malo et al.'s Financial PhraseBank, among other sources), so some pre-training/fine-tuning overlap with FPB exists at the base-model level.

### Recommendations

Use confidence scores (which are temperature-calibrated — see below) alongside labels: predictions with low confidence on the top class are more likely to be genuinely ambiguous. For high-stakes applications, treat predictions as one signal among several rather than a definitive classification.

---

## How to Get Started with the Model

```python
from transformers import pipeline

# Load — model weights are ~438 MB; cached locally after first download
clf = pipeline(
    "text-classification",
    model="iPwnds/finsentiment-distilbert-final",
    device=0,   # GPU if available; remove or set to -1 for CPU
)

result = clf("Earnings per share exceeded analyst expectations by a wide margin")
# → [{'label': 'positive', 'score': ...}]

# Batch inference (much faster than calling one-by-one)
headlines = [
    "Company announces $2B share buyback programme",
    "$INTC complete dumpster fire this year",
    "CEO resigns amid accounting investigation",
]
results = clf(headlines)
for h, r in zip(headlines, results):
    print(f"{r['label']:8s}  ({r['score']:.2%})  {h}")
```

The pipeline's `score` already reflects **calibrated** confidence — the model was trained with logits at their native scale, then a temperature factor (`T = 1.4754`, stored in `model.config.calibration_temperature`) was fit post-hoc to soften over-confident predictions. If accessing raw logits directly (bypassing the `pipeline`), divide by this temperature before applying softmax:

```python
calibrated_logits = raw_logits / model.config.calibration_temperature
```

Label mapping (FinBERT scheme): `positive` → 0, `negative` → 1, `neutral` → 2.

---

## Training Details

### Training Data

Two datasets were combined:

**1. Financial PhraseBank v1.0 (AllAgree subset)** — [`takala/financial_phrasebank`](https://huggingface.co/datasets/takala/financial_phrasebank), 2,264 expert-labeled English financial-news sentences where all annotators agreed on the label:

| Label | Count |
|---|---|
| Positive | 570 |
| Negative | 303 |
| Neutral | 1,391 |

> Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). *Good debt or bad debt: Detecting semantic orientations in economic texts.* Journal of the American Society for Information Science and Technology, 65(4), 782–796.

**2. Twitter Financial News Sentiment** — [`zeroshot/twitter-financial-news-sentiment`](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment), ~12,144 real financial tweets (train + validation splits combined, 11,931 examples used), covering informal text, tickers, abbreviations, and social-media phrasing that Financial PhraseBank never captures. The dataset's native labels (`0=Bearish, 1=Bullish, 2=Neutral`) were remapped to FinBERT's scheme (`Bearish→negative=1, Bullish→positive=0, Neutral→neutral=2`):

| Label | Count |
|---|---|
| Positive | 2,398 |
| Negative | 1,789 |
| Neutral | 7,744 |

**Combined dataset:** 14,195 examples, shuffled (`seed=42`) and split **80/10/10**:

| Split | Examples |
|---|---|
| Train | 11,356 |
| Validation | 1,419 |
| Test | 1,420 |

Train-split class distribution: positive 2,390 / negative 1,690 / neutral 7,276.

### Training Procedure

#### Class weighting

`negative` remains the rarest class even after adding Twitter data, and it's the class that matters most for a risk-aware financial analyst. Balanced class weights were computed (`sklearn.utils.class_weight`, `"balanced"`) and applied via a `Trainer` subclass (`WeightedTrainer`) that injects them into the cross-entropy loss:

| Class | Weight |
|---|---|
| positive | 1.5838 |
| negative | 2.2398 |
| neutral | 0.5202 |

#### Preprocessing

Sentences/tweets were tokenized with the `ProsusAI/finbert` tokenizer, `padding="max_length"`, `max_length=128`.

#### Training Hyperparameters

| Hyperparameter | Value |
|---|---|
| Base model | `ProsusAI/finbert` |
| Number of labels | 3 |
| Epochs | 3 |
| Per-device train batch size | 32 |
| Per-device eval batch size | 64 |
| Learning rate | 2e-5 (lower than default — FinBERT is already domain-adapted; a gentle LR avoids catastrophic forgetting) |
| Warmup steps | 200 |
| Weight decay | 0.01 |
| Mixed precision | fp16 |
| Loss | Class-weighted cross-entropy |
| Best checkpoint metric | Validation F1 (weighted) |
| Max sequence length | 128 tokens |

**Training regime:** fp16 mixed precision.

#### Speeds, Sizes, Times

| | |
|---|---|
| Training time | ~4.4 minutes (261s, T4 GPU, Google Colab) |
| Total steps | 1,065 |
| Train samples/sec | 130.4 |
| Final training loss | 0.3114 |
| Model size | ~438 MB |
| Inference speed | ~1–2 ms / headline (Apple MPS / T4 GPU) |

---

## Evaluation

### Testing Data

The held-out test split: **1,420 examples** drawn from the combined Financial PhraseBank + Twitter dataset, stratified by the same 80/10/10 shuffle with `seed=42`. No examples from the test split were seen during training or used for checkpoint selection.

### Factors

Evaluation is disaggregated by class (positive / negative / neutral) via a full classification report, given the class imbalance in the underlying data.

### Metrics

**Weighted F1** (`evaluate.load("f1")`, `average="weighted"`) — the primary metric used for checkpoint selection and reporting, appropriate given the class imbalance.

**Expected Calibration Error (ECE)** was additionally measured before/after temperature scaling to validate the calibration step.

### Results

| Metric | Value |
|---|---|
| Test F1 (weighted) | **0.8949** |
| Test accuracy | 0.8930 |
| Test samples | 1,420 |

Per-class breakdown:

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| positive | 0.8257 | 0.8795 | 0.8517 | 307 |
| negative | 0.7522 | 0.8827 | 0.8122 | 196 |
| neutral | 0.9560 | 0.8997 | 0.9270 | 917 |
| **macro avg** | 0.8446 | 0.8873 | 0.8636 | 1,420 |
| **weighted avg** | 0.8997 | 0.8930 | 0.8949 | 1,420 |

**Calibration:**

| Metric | Value |
|---|---|
| Optimal temperature (T) | 1.4754 |
| ECE before calibration | 0.0605 |
| ECE after calibration | 0.0207 |

Temperature scaling only rescales confidence — it does not change the predicted class (verified: predictions are identical before/after dividing logits by T).

#### Summary

Fine-tuning FinBERT on the combined, class-weighted dataset produces a classifier that handles both formal and informal financial text, with `negative` recall (0.8827) notably improved relative to a naive baseline thanks to class weighting — important for a risk-aware use case where missing bearish signals is costlier than a false positive. The weighted F1 (0.8949) is lower than v1's FPB-only score (0.9737), but the evaluation set here is substantially larger and includes noisy social-media text that v1 was never tested against; the two scores measure different things. Confidence calibration meaningfully reduced ECE (0.0605 → 0.0207) without affecting accuracy.

---

## Environmental Impact

Training was performed on a Google Colab T4 GPU for approximately 4.4 minutes. Estimated carbon emissions are negligible.

- **Hardware type:** NVIDIA T4 (Google Colab)
- **Hours used:** ~0.073 hours
- **Cloud provider:** Google (Colab)
- **Compute region:** US (Colab default)
- **Carbon emitted:** < 2 g CO₂eq (estimated)

---

## Technical Specifications

### Model Architecture and Objective

- **Base architecture:** FinBERT (`ProsusAI/finbert`) — BERT-base encoder pre/fine-tuned on financial text, 109.5M parameters
- **Classification head:** Linear layer on top of the `[CLS]` token → 3 logits
- **Objective:** Class-weighted cross-entropy loss for 3-class sequence classification (positive / negative / neutral)
- **Post-processing:** Temperature scaling (T=1.4754) applied to logits at inference for calibrated confidence scores

### Compute Infrastructure

#### Hardware

- NVIDIA T4 GPU (15 GB VRAM) for training — Google Colab
- Apple Silicon (MPS), CUDA GPU, or CPU for inference

#### Software

| Package | Role |
|---|---|
| `transformers` | Model, tokenizer, `Trainer`, `TrainingArguments` |
| `datasets` | Dataset loading, concatenation, splitting, tokenization mapping |
| `evaluate` | Weighted F1 metric computation |
| `scikit-learn` | Class weight computation, confusion matrix, per-class metrics |
| `accelerate` | Mixed-precision training (fp16) |
| `huggingface_hub` | Dataset download, `push_to_hub` |

---

## Citation

If you use this model, please cite both source datasets:

**BibTeX:**

```bibtex
@article{malo2014good,
  title   = {Good debt or bad debt: Detecting semantic orientations in economic texts},
  author  = {Malo, Pekka and Sinha, Ankur and Korhonen, Pekka and Wallenius, Jyrki and Takala, Pyry},
  journal = {Journal of the American Society for Information Science and Technology},
  volume  = {65},
  number  = {4},
  pages   = {782--796},
  year    = {2014}
}
```

**APA:**

Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). Good debt or bad debt: Detecting semantic orientations in economic texts. *Journal of the American Society for Information Science and Technology, 65*(4), 782–796.

Twitter Financial News Sentiment dataset: [`zeroshot/twitter-financial-news-sentiment`](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment).

---

## Model Card Authors

Florian Braun ([@iPwnds](https://huggingface.co/iPwnds))

## Model Card Contact

[huggingface.co/iPwnds](https://huggingface.co/iPwnds)
