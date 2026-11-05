---
language:
- en
license: mit
tags:
- text-classification
- hate-speech-detection
- sentiment-analysis
- twitter
- roberta
- transformers
- fine-tuned
datasets:
- cardiffnlp/tweet_eval
metrics:
- f1
- accuracy
pipeline_tag: text-classification
model-index:
- name: tweet-eval-3class-classifier
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: TweetEval (sentiment + hate + offensive)
      type: cardiffnlp/tweet_eval
    metrics:
    - name: Weighted F1
      type: f1
      value: see evaluation cell
---

# Tweet Eval 3-Class Classifier

**Author:** [ChristianAgyapong](https://huggingface.co/ChristianAgyapong)

A fine-tuned version of [`cardiffnlp/twitter-roberta-base-sentiment-latest`](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) trained on a combined TweetEval corpus (sentiment + hate + offensive tasks) for **3-class tweet classification**.

---

## Label Scheme

| Label | Class | Description |
|-------|-------|-------------|
| 0 | **Safe / Positive** | Positive or safe content |
| 1 | **Neutral** | Neutral / non-problematic content |
| 2 | **Hate / Offensive** | Hateful or offensive content |

---

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | `cardiffnlp/twitter-roberta-base-sentiment-latest` |
| Datasets | TweetEval sentiment + hate + offensive |
| Max sequence length | 128 tokens |
| Learning rate | 2e-5 |
| Batch size | 32 (train) / 64 (eval) |
| Epochs | Up to 5 (early stopping, patience=2) |
| Weight decay | 0.01 |
| FP16 | ✅ |
| Optimizer | AdamW |
| Best model metric | Weighted F1 |

---

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "ChristianAgyapong/tweet-eval-3class-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model     = AutoModelForSequenceClassification.from_pretrained(model_id)

LABEL_MAP = {0: "Safe/Positive", 1: "Neutral", 2: "Hate/Offensive"}

def classify(text: str) -> dict:
    inputs = tokenizer(text, truncation=True, max_length=128, return_tensors="pt")
    model.eval()
    with torch.no_grad():
        probs = torch.softmax(model(**inputs).logits, dim=-1)[0].tolist()
    pred = int(torch.argmax(torch.tensor(probs)))
    return {"label": LABEL_MAP[pred], "score": probs[pred], "all_probs": probs}

print(classify("I love this so much!"))
# → {'label': 'Safe/Positive', 'score': 0.92, 'all_probs': [...]}
```

---

## Limitations

- Trained on English Twitter text only; may degrade on formal writing or other languages.
- Edge cases between neutral and hate may be misclassified — use as a signal, not a sole decision-maker.
- Does not capture sarcasm well.

---

## Citation

```bibtex
@misc{tweet-eval-3class-2026,
  author       = {Christian Agyapong},
  title        = {Tweet Eval 3-Class Classifier},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ChristianAgyapong/tweet-eval-3class-classifier}}
}
```
