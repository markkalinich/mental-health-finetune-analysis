---
license: mit
language:
- en
base_model: ProsusAI/finbert
tags:
- text-classification
- sentiment-analysis
- finance
- finbert
- indian-financial-news
metrics:
- f1
- accuracy
---

# finbert-sentfin

**FinBERT fine-tuned on SEntFiN 1.0** — Indian financial news sentiment classification.

Fine-tuned from [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert) on the [SEntFiN 1.0](https://github.com/pyRis/SEntFiN) dataset of human-annotated Indian financial news headlines sourced from the Economic Times and Moneycontrol, covering NSE500-listed companies.

## Why This Model

`ProsusAI/finbert` was trained primarily on US/EU financial text (SEC filings, financial news wire). On Indian financial headlines it scores approximately **F1 = 0.76**. This model addresses that domain gap by fine-tuning on 9,514 expert-annotated Indian financial headlines, achieving **F1 = 0.873** on a held-out validation set — a **+11% improvement** on Indian financial text.

## Model Details

| Property | Value |
|---|---|
| Base model | `ProsusAI/finbert` |
| Architecture | BERT-base (110M parameters) |
| Task | 3-class sentiment classification |
| Labels | `positive` (0), `negative` (1), `neutral` (2) |
| Training data | SEntFiN 1.0 — 8,086 samples |
| Validation data | SEntFiN 1.0 — 1,428 samples |
| Best epoch | 3 / 4 |
| F1 weighted | 0.873 |
| Accuracy | 0.873 |
| Training hardware | Kaggle T4 GPU (fp16) |

## Training Configuration

```python
TrainingArguments(
    num_train_epochs=4,
    per_device_train_batch_size=32,
    learning_rate=2e-5,
    warmup_steps=100,
    weight_decay=0.01,
    fp16=True,
    load_best_model_at_end=True,
    metric_for_best_model="f1_weighted",
)
```

## Per-Class Results (Validation Set)

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| positive | 0.91 | 0.86 | 0.89 | 504 |
| negative | 0.87 | 0.89 | 0.88 | 407 |
| neutral | 0.84 | 0.87 | 0.86 | 517 |
| **weighted avg** | **0.87** | **0.87** | **0.87** | **1428** |

## Dataset

**SEntFiN 1.0** ([paper](https://arxiv.org/abs/2305.12257), [GitHub](https://github.com/pyRis/SEntFiN)) is a human-annotated dataset of 10,753 financial news headlines with entity-sentiment annotations, covering 920 companies in the NSE500 index (2002–2017). Headlines were sourced from the Economic Times and Moneycontrol.

**Preprocessing applied:**
- Headlines with multiple entities having conflicting sentiments were dropped (1,239 rows)
- Remaining 9,514 rows used for training
- Stratified 85/15 train/validation split

## Usage

```python
from transformers import pipeline

pipe = pipeline(
    "text-classification",
    model="tahp0604/finbert-sentfin",
)

headlines = [
    "Reliance Industries posts record quarterly profit",
    "HDFC Bank shares fall 4% after RBI penalty",
    "TCS Q4 results in line with analyst estimates",
]

for h in headlines:
    result = pipe(h)[0]
    print(f"[{result['label'].upper():8s} {result['score']:.2f}]  {h}")
```

**Output:**
```
[POSITIVE 0.94]  Reliance Industries posts record quarterly profit
[NEGATIVE 0.91]  HDFC Bank shares fall 4% after RBI penalty
[NEUTRAL  0.83]  TCS Q4 results in line with analyst estimates
```

## Direct inference

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("tahp0604/finbert-sentfin")
model     = AutoModelForSequenceClassification.from_pretrained("tahp0604/finbert-sentfin")
model.eval()

def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        probs = torch.softmax(model(**inputs).logits, dim=-1)[0]
    idx   = int(probs.argmax())
    label = model.config.id2label[idx]
    return label, float(probs[idx])

label, confidence = predict("Infosys raises revenue guidance for FY26")
print(f"{label} ({confidence:.2f})")  # positive (0.89)
```

## Label Mapping

```python
id2label = {0: "positive", 1: "negative", 2: "neutral"}
label2id = {"positive": 0, "negative": 1, "neutral": 2}
```

This is identical to `ProsusAI/finbert` — the model is a drop-in replacement.

## Intended Use

- Sentiment scoring of Indian financial news headlines
- NSE/BSE stock news sentiment analysis
- Component in financial signal fusion pipelines

## Limitations

- Trained on headlines from 2002–2017 — may not capture terminology from newer financial instruments or recent regulatory changes
- Optimised for short headlines (≤ 128 tokens) — performance may degrade on full article text
- Covers Indian equities (NSE500) — may underperform on commodities, currencies, or global markets
- Not intended for investment decisions

## Citation

If you use this model, please cite the SEntFiN dataset:

```bibtex
@article{sinha2022sentfin,
  title={SEntFiN 1.0: Entity-Aware Sentiment Analysis for Financial News},
  author={Sinha, Ankur and Kedas, Satishwar and Kumar, Rishu and Malo, Pekka},
  journal={Journal of the Association for Information Science and Technology},
  volume={73},
  number={9},
  pages={1314--1335},
  year={2022}
}

@article{araci2019finbert,
  title={FinBERT: Financial Sentiment Analysis with Pre-Trained Language Models},
  author={Araci, Dogu},
  journal={arXiv preprint arXiv:1908.10063},
  year={2019}
}
```