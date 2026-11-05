---
language:
- en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- distilbert
- transformers
pipeline_tag: text-classification
library_name: transformers
datasets:
- Amazon_Unlocked_Mobile
base_model: distilbert-base-uncased
metrics:
- accuracy
- f1
- recall
- precision
widget:
- text: "Great handset! Works flawlessly."
- text: "Terrible product, waste of money."
---

# DistilBERT for Binary Sentiment Classification

Lightweight sentiment classifier fine-tuned from `distilbert-base-uncased` to predict sentiment (negative vs. positive) for short English product reviews. Trained on a filtered subset of the Amazon Unlocked Mobile dataset.

## Model Details
- Base model: `distilbert-base-uncased`
- Task: binary sentiment classification
- Labels: `0 -> negative` (rating 1), `1 -> positive` (rating 5)
- Max input length: 128 tokens
- Tokenizer: `AutoTokenizer` for the same checkpoint
- Mixed precision: fp16 (when CUDA available)

## Intended Use and Limitations
- Use for short English product-review style texts.
- Binary only (negative/positive). Not suited for nuanced or multi-class sentiment.
- Not for safety-critical decisions or content moderation on its own.

## Dataset and Preprocessing
- Source: Amazon Unlocked Mobile (`Amazon_Unlocked_Mobile.csv`)
- Filtering: keep rows where `Rating ∈ {1, 5}`; drop unrelated columns
- Tokenization: padding to max length, truncation at 128
- Split: train/test with `test_size = 0.3`, `seed = 100`

## Training Configuration
- Optimizer and schedule: handled by `transformers.Trainer`
- Learning rate: `2e-5`
- Batch size: `48` (train/eval per device)
- Epochs: `2`
- Weight decay: `0.01`
- Save/eval strategy: `epoch`
- Push to Hub: enabled

## Evaluation
Computed with `accuracy` and `f1` on the held-out test split. See the repository "Files and versions" / "Training metrics" tabs for run artifacts and exact scores.

## How to Use

Python (Transformers pipeline):
```python
from transformers import pipeline

clf = pipeline(
    "text-classification",
    model="Floressek/sentiment_classification_from_distillbert",
    top_k=None  # returns single label with score
)

print(clf("Great handset!"))
print(clf("Shame. I wish I hadn't bought it."))

---