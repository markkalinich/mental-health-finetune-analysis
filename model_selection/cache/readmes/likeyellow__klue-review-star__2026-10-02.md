---
license: cc-by-nc-sa-4.0
language:
  - ko
base_model: klue/bert-base
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - korean
  - restaurant-review
  - ordinal-regression
datasets:
  - leey4n/KR3
---

# klue-review-star

Successor: [klue-review-star-4class](https://huggingface.co/likeyellow/klue-review-star-4class) — adds a fourth class that rejects non-review input.

Predicts a **1.0–5.0 star rating from Korean restaurant review text alone**,
along with a confidence score.

Fine-tuned from `klue/bert-base` on the KR3 dataset.

## Why

In Korea, "rating terrorism" is a recurring problem: users leave positive
review text ("굿", "친절해요") while assigning one star, dragging a
restaurant's average down. Because the text contains nothing abusive or false,
platforms cannot moderate it.

This model removes the separate star input: the rating is derived from the
review body, so the two cannot diverge.

## How it works

KR3 ships categorical labels (`0` negative, `1` positive, `2` ambiguous)
rather than the original star values, so direct regression is not possible.

Instead:

1. **3-class classification** — negative / positive / neutral
2. **Star rating** = expected value over class anchors `[1.0, 5.0, 3.0]`
3. **Confidence** = `1 − H(p) / ln(3)`, the normalized entropy of the same
   distribution, inverted

Step 3 costs nothing extra and identifies mixed reviews: text combining
praise and complaint produces a spread-out distribution and therefore low
confidence. Downstream, this is used to down-weight ambiguous reviews when
aggregating a restaurant's average.

## Usage

```python
import numpy as np
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL = "likeyellow/klue-review-star"
ANCHOR = np.array([1.0, 5.0, 3.0])  # [negative, positive, neutral]

tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL).eval()

def predict(text):
    enc = tok(text, truncation=True, max_length=256, return_tensors="pt")
    with torch.no_grad():
        p = torch.softmax(model(**enc).logits, dim=-1)[0].numpy()
    star = float((p * ANCHOR).sum())
    ent = float(-(p * np.log(p + 1e-9)).sum())
    return round(star, 2), round(1 - ent / np.log(3), 3)

print(predict("굿"))
# (4.7, 0.607)

print(predict("회는 신선한데 주차가 너무 불편했어요"))
# (3.6, 0.15)   ← mixed review, low confidence

print(predict("재료가 다 상한 것 같고 직원도 불친절했어요 최악"))
# (1.02, 0.958)
```

## Results

Test set: 15,000 reviews, stratified.

| Metric | Value |
|---|---|
| Accuracy | 0.768 |
| Macro F1 | 0.751 |
| **Star MAE** | **0.640** |
| Negative recall | 0.846 |
| Neutral recall | 0.626 |

Star MAE is the primary metric: misclassifying positive as neutral is a full
error under classification, but only a small error in star terms. MAE
reflects what the system is actually for.

### Model comparison

`beomi/KcELECTRA-base`, pretrained on colloquial Korean comment data, was
evaluated on the same split:

| | klue/bert-base | KcELECTRA-base |
|---|---|---|
| Accuracy | **0.768** | 0.755 |
| Star MAE | **0.640** | 0.656 |
| Neutral recall | 0.626 | **0.657** |
| Negative recall | 0.846 | **0.857** |

KcELECTRA is better on minority classes but worse on overall accuracy and
star MAE. Since star accuracy is the objective, `klue/bert-base` was chosen.
KcELECTRA's validation loss was still decreasing at epoch 2, so it may
overtake with longer training.

## Training

- Data: 150,000 reviews stratified from KR3, split 80/10/10
- Class weights `[3.01, 0.55, 1.17]` to correct 11 / 60 / 28 imbalance
- 2 epochs, lr 2e-5, batch 32, max_len 256, fp16, NVIDIA T4
- Best checkpoint selected by validation loss (epoch 1)

## Limitations

- **Out-of-domain input.** Text unrelated to restaurants is still forced into
  one of three classes and tends to drift positive, following the training
  prior. Confidence drops accordingly (~0.2), which is the intended signal,
  but no explicit rejection class exists.
- **Label noise.** KR3's ambiguous class mixes genuinely neutral, purely
  informational, and clearly positive reviews. Neutral recall of 0.626
  reflects this.
- **Understated hedging.** Softly negative phrasing tends to score lower than
  a human would rate it.
- **Confidence is not accuracy.** It measures how concentrated the model's
  distribution is, not how often it is right. No calibration was performed.

## License

CC BY-NC-SA 4.0, inherited from the KR3 dataset. Non-commercial use only.

## Links

- Serving API: https://github.com/likeyellow/review-star-api
- Demo frontend: https://github.com/likeyellow/review-star-ai