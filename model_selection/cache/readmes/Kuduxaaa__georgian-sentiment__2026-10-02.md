---
language:
- ka
license: mit
base_model: FacebookAI/xlm-roberta-base
tags:
- text-classification
- sentiment-analysis
- georgian
- xlm-roberta
pipeline_tag: text-classification
widget:
- text: "[POST] მთავრობამ ახალი კანონი მიიღო [SEP] [COMMENT] საბოლოოდ სწორი გადაწყვეტილება!"
  example_title: "Positive"
- text: "[POST] მთავრობამ ახალი კანონი მიიღო [SEP] [COMMENT] კატასტროფაა, ეს ქვეყანა დაიღუპა"
  example_title: "Negative"
- text: "[POST] მთავრობამ ახალი კანონი მიიღო [SEP] [COMMENT] კანონი ხვალ ძალაში შედის"
  example_title: "Neutral"
---

# Georgian Sentiment Analysis (XLM-RoBERTa)

Fine-tuned [`xlm-roberta-base`](https://huggingface.co/FacebookAI/xlm-roberta-base) for sentiment classification of Georgian Facebook comments in political context.

The model classifies a comment's sentiment **toward the post's subject** as:
- `negative` (0)
- `neutral` (1)
- `positive` (2)

## Performance

Evaluated on a held-out test set of **1,106 samples**:

| Metric | Score |
|---|---|
| Accuracy | 0.801 |
| Macro F1 | 0.705 |
| Weighted F1 | 0.810 |

### Per-class

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| negative | 0.74 | 0.73 | **0.736** | 321 |
| neutral | 0.41 | 0.51 | **0.454** | 142 |
| positive | 0.94 | 0.91 | **0.924** | 643 |

## Usage

The model expects input in this format:

```
[POST] <post text> [SEP] [COMMENT] <comment text>
```

This separation lets the model judge the comment's sentiment in the context of the post it responds to.

### Quick start

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Kuduxaaa/georgian-sentiment",
)

text = "[POST] მთავრობამ ახალი კანონი მიიღო [SEP] [COMMENT] საბოლოოდ სწორი გადაწყვეტილება!"
result = classifier(text)
print(result)
# [{'label': 'positive', 'score': 0.92}]
```

### Manual inference

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "Kuduxaaa/georgian-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

def predict(post: str, comment: str):
    text = f"[POST] {post} [SEP] [COMMENT] {comment}"
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
    
    with torch.no_grad():
        logits = model(**inputs).logits
    
    probs = torch.softmax(logits, dim=-1)[0]
    pred = torch.argmax(probs).item()
    
    return {
        "label": model.config.id2label[pred],
        "score": round(probs[pred].item(), 3),
        "probs": {
            "negative": round(probs[0].item(), 3),
            "neutral":  round(probs[1].item(), 3),
            "positive": round(probs[2].item(), 3),
        }
    }

print(predict(
    "მთავრობამ ახალი კანონი მიიღო",
    "კატასტროფაა, ეს ქვეყანა დაიღუპა"
))
```

### Batched inference

For higher throughput, batch many comments at once:

```python
def predict_batch(pairs, batch_size=32):
    """pairs: list of (post, comment) tuples"""
    texts = [f"[POST] {p} [SEP] [COMMENT] {c}" for p, c in pairs]
    results = classifier(texts, truncation=True, max_length=256, batch_size=batch_size)
    return results
```

## Training Details

### Data

- **Size**: ~5,500 labeled Georgian Facebook comments
- **Domain**: Political content (news posts, party pages, public figures)
- **Labeling**: LLM-assisted (Claude) with confidence scores per sample
- **Split**: 70% train / 10% validation / 20% test (stratified by label)

### Class distribution

| Label | Count | Share |
|---|---|---|
| positive | 3,212 | 58.1% |
| negative | 1,603 | 29.0% |
| neutral | 712 | 12.9% |

### Hyperparameters

| Parameter | Value |
|---|---|
| Base model | `FacebookAI/xlm-roberta-base` |
| Max sequence length | 256 |
| Effective batch size | 32 |
| Learning rate | 2e-5 |
| Optimizer | AdamW |
| Weight decay | 0.01 |
| Warmup ratio | 0.1 |
| Epochs (with early stopping) | up to 10 |
| Loss | Class-weighted CrossEntropy with label smoothing |
| Mixed precision | fp16 |

### Hardware

Trained on Kaggle 2× Tesla T4 (free tier). Total training time: ~25 minutes.

## Limitations

- **Sarcasm detection is weak.** Comments like "გენიოსები არიან" (sarcastic) are often labeled `positive` because the labeled data treats sarcasm as positive in many cases. For production use, combine model predictions with rule-based post-processing (e.g., flagging sarcasm emoji + low confidence).
- **Neutral class underperforms** (F1 = 0.45). Neutral examples are the smallest class in the training data (~13%) and are inherently harder — the boundary between mild praise / mild criticism / factual statements is fuzzy.
- **Context-dependent comments** (e.g., short replies like "სწორად იქცევიან", "ბავშვობა გამოსდით") rely heavily on the post for correct interpretation. Always pass the post text using the `[POST] ... [SEP] [COMMENT] ...` format.
- **Domain-specific.** The model is trained on political Facebook content. Performance on product reviews, customer support, or other domains will be lower without further fine-tuning.

## Recommended Production Setup

For higher reliability, apply a confidence threshold and route low-confidence predictions for human review:

```python
def predict_safe(post, comment, threshold=0.65):
    r = predict(post, comment)
    if r["score"] < threshold:
        return {"label": "uncertain", "score": r["score"]}
    return r
```

## License

MIT — feel free to use, modify, and distribute.

## Acknowledgements

Built on top of [XLM-RoBERTa](https://huggingface.co/FacebookAI/xlm-roberta-base) by FacebookAI.