---
language: en
license: apache-2.0
base_model: distilbert-base-uncased-finetuned-sst-2-english
datasets:
- McAuley-Lab/Amazon-Reviews-2023
tags:
- text-classification
- sentiment-analysis
- amazon-reviews
- distilbert
pipeline_tag: text-classification
---

# distilbert-amazon-review-sentiment

DistilBERT ([`distilbert-base-uncased-finetuned-sst-2-english`](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english))
fine-tuned for **positive vs negative sentiment of Amazon product reviews** (Appliances + Beauty).
Label 1 = positive (4-5 stars), label 0 = negative (1-2 stars). Part of the
[product-review-intelligence](https://github.com/Waleed-Ilyas/product-review-intelligence) project.

## Training
* 6,400 reviews (3,200 positive / 3,200 negative), **one epoch on a laptop CPU**, max length 96, AdamW lr 2e-5, batch 16.
* Reviews come from products disjoint from the validation/test products.

## Results (8,000 held-out reviews from products never seen in training)
| Model | Macro-F1 | ROC-AUC |
|---|---|---|
| This model, threshold 0.5 | 0.896 | 0.986 |
| **This model, threshold 0.06 (recommended)** | **0.920** | 0.986 |
| DistilBERT SST-2 zero-shot | 0.758 | 0.954 |
| TF-IDF + logistic regression (78k training reviews) | 0.919 | 0.988 |

**Use the threshold 0.06 on P(positive).** Fine-tuning on a balanced sample shifts the model toward
"negative" relative to the natural population (82% of labelled reviews are positive); the threshold was chosen on a
validation subset to maximise macro-F1.

## Limitations
* Trained on only two product categories and 6.4k examples; a longer fine-tune would probably improve it.
* Labels are star ratings, which are noisy; mixed 2-star and 4-star reviews are the main error source.
* English only; not evaluated for other domains. Not for automated decisions about people.

## Usage
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
tok = AutoTokenizer.from_pretrained("WaleedIlyas99/distilbert-amazon-review-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("WaleedIlyas99/distilbert-amazon-review-sentiment").eval()
enc = tok(["Works great but the lid cracked after two weeks."], return_tensors="pt", truncation=True, max_length=128)
p_pos = torch.softmax(model(**enc).logits, dim=-1)[0, 1].item()
print("positive" if p_pos >= 0.06 else "negative", round(p_pos, 3))
```
