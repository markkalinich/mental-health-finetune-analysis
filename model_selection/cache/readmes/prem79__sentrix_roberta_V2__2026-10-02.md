---
language:
- en
- fr
- es
- de
- pt
license: mit
tags:
- sentiment-analysis
- text-classification
- roberta
- twitter
- nlp
- fine-tuned
datasets:
- tweet_eval
metrics:
- accuracy
- f1
model-index:
- name: sentrix_roberta_V2
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    metrics:
    - type: accuracy
      value: 0.8821
    - type: f1
      value: 0.8821
---

# sentrix_roberta_V2

Fine-tuned RoBERTa for binary sentiment classification on social media text. 88.21% accuracy on a held-out test set of 40,000 balanced samples, trained on Kaggle with GPU acceleration.

Runs locally via the HuggingFace Transformers library. Downloads once on first use, cached for all subsequent runs. No cloud subscription required.

---

## What this model does

It reads text, returns a POSITIVE or NEGATIVE label, and provides per-class confidence scores. Straightforward by design.

Labels: `NEGATIVE` (0) and `POSITIVE` (1). Binary output only. See the Limitations section if you need neutral classification.

Test accuracy: **88.21%**. Symmetric across both classes, meaning it is not secretly biased toward one label because the training set was balanced from the start.

---

## Model details

| Property | Value |
|---|---|
| Base model | `cardiffnlp/twitter-roberta-base-sentiment-latest` |
| Architecture | RoBERTa-base (125M parameters) |
| Task | Binary Sentiment Classification |
| Labels | NEGATIVE (0), POSITIVE (1) |
| Test Accuracy | 88.21% |
| Test F1 | 88.21% |
| Training samples | ~80,000 |
| Test samples | 40,000 (perfectly balanced) |
| Max sequence length | 128 tokens |
| Training platform | Kaggle (GPU) |
| Framework | PyTorch + HuggingFace Transformers |

---

## Why this base model

Cardiff NLP's `twitter-roberta-base-sentiment-latest` was pretrained on 58 million tweets before it ever saw the fine-tuning data. That means it already understands how people actually write online - abbreviations, slang, run-on sentences, missing punctuation, words that autocorrect clearly did not help with. Starting from that checkpoint instead of vanilla RoBERTa meant the model came in with real-world social media knowledge rather than learning it from scratch during fine-tuning.

---

## Training

### Data

Balanced Twitter sentiment dataset from Kaggle. Equal number of positive and negative samples so the model cannot cheat by defaulting to the majority class.

| Split | Samples | Negative | Positive |
|---|---|---|---|
| Train | ~80,000 | 50% | 50% |
| Validation | 20,000 | 50% | 50% |
| Test | 40,000 | 20,000 | 20,000 |

### Preprocessing

Two substitutions applied before tokenization, matching the convention the base model was pretrained with:

- URLs replaced with `http`
- User mentions replaced with `@user`

Skip these and you will see a small but consistent accuracy drop on anything with links or @mentions. The model expects those specific tokens.

### Training run

Trained with the HuggingFace `Trainer` API, evaluated every 500 steps. Best checkpoint saved on highest validation accuracy. Training was stopped at step 8500 (epoch 3.4 of 10 max) because the validation metrics had plateaued and the best checkpoint had already been captured.

| Step | Train Loss | Val Loss | Accuracy | F1 |
|---|---|---|---|---|
| 500 | 0.8806 | 0.8685 | 85.00% | 85.00% |
| 1000 | 0.8451 | 0.8348 | 86.25% | 86.25% |
| 1500 | 0.8336 | 0.8187 | 86.48% | 86.48% |
| 2000 | 0.8291 | 0.8075 | 86.84% | 86.83% |
| 2500 | 0.8155 | 0.8062 | 87.26% | 87.26% |
| 3000 | 0.7788 | 0.7987 | 87.32% | 87.31% |
| 3500 | 0.7690 | 0.7931 | 87.35% | 87.34% |
| 4000 | 0.7754 | 0.8005 | 87.53% | 87.53% |
| 4500 | 0.7661 | 0.7966 | 87.61% | 87.61% |
| 5000 | 0.7676 | 0.8098 | 87.59% | 87.58% |
| 5500 | 0.7407 | 0.8080 | 87.56% | 87.56% |
| 6000 | 0.7356 | 0.7944 | 87.72% | 87.72% |
| 6500 | 0.7205 | 0.7986 | 87.72% | 87.72% |
| 7000 | 0.7310 | 0.7979 | 87.68% | 87.68% |
| 7500 | 0.7232 | 0.7959 | 87.69% | 87.68% |
| 8000 | 0.6885 | 0.8235 | 87.74% | 87.74% |
| 8500 | 0.6905 | 0.8104 | 87.72% | 87.72% |

Training loss went from 0.88 to 0.69. Validation loss bottomed around step 6000-6500 and started creeping back up after that - classic sign the best checkpoint was already in the bag.

---

## Results

Evaluated on the held-out test set. 40,000 samples. Never seen during training or validation.

```
              precision    recall  f1-score   support

    Negative       0.88      0.88      0.88     20,000
    Positive       0.88      0.88      0.88     20,000

    accuracy                           0.88     40,000
   macro avg       0.88      0.88      0.88     40,000
weighted avg       0.88      0.88      0.88     40,000
```

Precision and recall are identical for both classes. The model is not sacrificing recall for precision or the other way around - it is genuinely balanced. That is what a properly balanced training set gets you.

| Metric | Value |
|---|---|
| Accuracy | 0.8821 |
| F1 (macro) | 0.8821 |
| Eval loss | 0.8102 |
| Throughput | 287.6 samples/second |

---

## How to use it

### Quickest way - pipeline

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="prem79/sentrix_roberta_V2"
)

print(classifier("The camera quality on this phone is absolutely stunning"))
# [{'label': 'POSITIVE', 'score': 0.9505}]

print(classifier("Battery is terrible, drains in 2 hours, not worth the price"))
# [{'label': 'NEGATIVE', 'score': 0.9472}]
```

### Full manual inference

```python
import torch
import torch.nn.functional as F
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("prem79/sentrix_roberta_V2")
model = AutoModelForSequenceClassification.from_pretrained("prem79/sentrix_roberta_V2")
model.eval()

def predict(text):
    # preprocess - do not skip this, the model expects these tokens
    text = re.sub(r'http\S+', 'http', text)
    text = re.sub(r'@\w+', '@user', text)

    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        probs = F.softmax(model(**inputs).logits, dim=-1)[0]

    return {
        "sentiment": "POSITIVE" if probs[1] > probs[0] else "NEGATIVE",
        "negative":  round(probs[0].item() * 100, 2),
        "positive":  round(probs[1].item() * 100, 2),
    }

predict("The new phone camera is absolutely stunning at night")
# {'sentiment': 'POSITIVE', 'negative': 4.95, 'positive': 95.05}

predict("Battery is terrible, drains in 2 hours, not worth the price")
# {'sentiment': 'NEGATIVE', 'negative': 94.72, 'positive': 5.28}

predict("Ce produit est incroyable! Tres satisfait de la qualite.")
# {'sentiment': 'POSITIVE', 'negative': 7.18, 'positive': 92.82}
# cross-lingual capability from base model pretraining
```

### Batch inference

```python
texts = [
    "Absolutely love this, best purchase this year",
    "Returned it on day two, complete waste of money",
    "It is okay I guess, nothing to write home about",
]

inputs = tokenizer(
    texts, padding=True, truncation=True,
    max_length=128, return_tensors="pt"
)
with torch.no_grad():
    probs = F.softmax(model(**inputs).logits, dim=-1)

for text, p in zip(texts, probs):
    label = "POSITIVE" if p[1] > p[0] else "NEGATIVE"
    print(f"{label} ({p[1].item():.1%} pos)  |  {text}")
```

---

## What it cannot do

Known constraints and failure modes:

- **Neutral sentiment** - binary output only. Text that is neither positive nor negative gets pushed into whichever class the token distribution leans toward. If you need three-way classification, this is not your model.
- **Sarcasm** - "oh great, another product that broke on day one, absolutely love it" will likely be classified as POSITIVE. The model sees "great," "love," and decides accordingly. Sarcasm detection is a different and significantly harder problem.
- **Long documents** - hard truncation at 128 tokens. Anything longer gets cut off. The first 128 tokens determine the output. If the important negative content is at the end of a long review, the model might miss it.
- **Domain shift** - trained on tweets and product reviews. Performance on news articles, legal documents, medical text, or academic writing has not been tested and will probably be worse.
- **Non-English accuracy** - the base model has cross-lingual capability from Twitter pretraining but the fine-tuning data was primarily English. French, Spanish, German, and Portuguese work but at lower confidence than English.

---

## Live demo

This model powers the SENTRIX web application:

- Frontend: https://prem-479.github.io/sentrix_ML_IA/
- Source code: https://github.com/prem-479/sentrix_ML_IA

The app runs the model locally on your machine. The frontend just sends text to your Flask server and displays the results. No cloud inference. No data leaving your device.

---

## Files in this repository

| File | Size | What it is |
|---|---|---|
| `config.json` | 886 B | Model architecture config and label mapping |
| `model.safetensors` | 499 MB | The actual weights. This is the big one. |
| `tokenizer.json` | 3.56 MB | Tokenizer vocabulary |
| `tokenizer_config.json` | 387 B | Tokenizer settings |

---

## Citation

This model fine-tunes Cardiff NLP's RoBERTa checkpoint. If you use this in something academic:

```bibtex
@inproceedings{barbieri-etal-2020-tweeteval,
    title = "{T}weet{E}val: Unified Benchmark and Comparative Evaluation for Tweet Classification",
    author = "Barbieri, Francesco and Camacho-Collados, Jose and Espinosa Anke, Luis and Neves, Leonardo",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2020",
    year = "2020",
    publisher = "Association for Computational Linguistics",
}
```

---

*Trained on Kaggle with GPU acceleration. Fine-tuned from cardiffnlp/twitter-roberta-base-sentiment-latest.*