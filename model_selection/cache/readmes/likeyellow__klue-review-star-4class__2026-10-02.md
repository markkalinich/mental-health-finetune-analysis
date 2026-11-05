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
  - out-of-domain-detection
datasets:
  - leey4n/KR3
  - klue
---

# klue-review-star-4class

Predicts a **1.0–5.0 star rating from Korean restaurant review text**, and
rejects input that is not a restaurant review.

Successor to [likeyellow/klue-review-star](https://huggingface.co/likeyellow/klue-review-star),
which had no way to decline.

## Why a fourth class

The 3-class predecessor was forced to pick one of negative / positive /
neutral for any input. Unrelated text still produced a rating:

| Input | 3-class output |
|---|---|
| 엄마 보고 싶어요 ("I miss my mom") | 4.04 stars, confidence 0.21 |
| ㅇㄴㅇㅎㄴㄷㅎ (keyboard mash) | 3.57 stars, confidence 0.08 |

Low confidence flagged these, but a threshold could not separate them from
genuinely mixed reviews — both sat in the same 0.15–0.35 band. Measured over
25 hand-labelled sentences:

| Category | Mean confidence |
|---|---|
| Clear negative | 0.904 |
| Clear positive | 0.615 |
| Informational | 0.400 |
| **Unrelated** | **0.269** |
| **Mixed review** | **0.256** |

A fourth class was added instead.

## Labels

| id | Meaning | Star anchor |
|---|---|---|
| 0 | negative | 1.0 |
| 1 | positive | 5.0 |
| 2 | neutral | 3.0 |
| 3 | **not a review** | — (no rating produced) |

For classes 0–2, the rating is the expected value over anchors after
renormalising the first three probabilities. Confidence is the normalised,
inverted entropy of that renormalised distribution, so it stays comparable to
the 3-class model.

## Usage

```python
import numpy as np, torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

MODEL  = "likeyellow/klue-review-star-4class"
ANCHOR = np.array([1.0, 5.0, 3.0])
LABEL  = ["negative", "positive", "neutral", "not_a_review"]

tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL).eval()

def predict(text):
    enc = tok(text, truncation=True, max_length=256, return_tensors="pt")
    with torch.no_grad():
        p = torch.softmax(model(**enc).logits, dim=-1)[0].numpy()
    if int(p.argmax()) == 3:
        return {"label": "not_a_review", "star": None, "confidence": None}
    q = p[:3] / p[:3].sum()
    ent = float(-(q * np.log(q + 1e-9)).sum())
    return {"label": LABEL[int(p.argmax())],
            "star": round(float((q * ANCHOR).sum()), 2),
            "confidence": round(1 - ent / np.log(3), 3)}

predict("존맛탱")            # {'label': 'positive', 'star': 4.94, ...}
predict("엄마 보고 싶어요")   # {'label': 'not_a_review', 'star': None, ...}
```

## Results

Test set: 17,494 held-out examples.

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| negative | 0.712 | 0.883 | 0.789 | 1,719 |
| positive | 0.868 | 0.777 | 0.820 | 9,106 |
| neutral | 0.582 | 0.655 | 0.616 | 4,215 |
| **not a review** | **0.994** | **0.998** | **0.996** | 2,454 |
| accuracy | | | **0.789** | |

**Star MAE on review classes only: 0.668** (3-class predecessor: 0.640).

Rejection costs almost nothing in rating accuracy: only 16 of 15,040 genuine
reviews were misrouted to class 3, and recall on negative and neutral
actually improved (0.846 → 0.883, 0.626 → 0.655).

Note that the 0.996 F1 on class 3 reflects an easy test distribution — news
headlines differ sharply in register from reviews. Real borderline input is
harder; see below.

## Training

- 150,000 KR3 reviews (classes 0–2), stratified
- 20,000 `klue/ynat` news headlines (class 3)
- ~480 hand-built out-of-domain sentences, repeated ×10 (class 3)
- Class weights to correct imbalance; 1 epoch, lr 2e-5, batch 32, max_len 256, T4
- Validation loss rose at epoch 2 (0.4035 → 0.4155), so epoch 1 was kept

### Why the hand-built set mattered

A first attempt used news headlines alone. It caught keyboard mash and
everyday chat, but food-related non-reviews still passed:

| Input | v1 (news only) | v2 (+ hand-built) |
|---|---|---|
| 떡볶이 먹고 싶다 ("I want tteokbokki") | neutral 0.977 | not a review 0.999 |
| 이 책 정말 재밌어요 ("this book is fun") | neutral 0.841 | not a review 1.000 |
| 오늘 점심 뭐 먹지 ("what's for lunch") | neutral 0.894 | not a review 0.709 |

The model had learned a shallow rule — *food word present ⇒ review* — because
no food vocabulary appeared in the negative examples. Adding food-related
non-review sentences fixed it, and the fix generalised: 만두 ("dumpling") and
소설 ("novel") were held out of training entirely, yet both are rejected at
0.999+.

## Limitations

- **Borderline input is weaker than the metrics suggest.** 오늘 점심 뭐 먹지
  scores 0.709 for class 3 while other rejections score 0.999+.
- **Neutral remains noisy.** Precision 0.582, with 1,826 positive→neutral and
  1,035 neutral→positive errors. This is inherited from KR3's ambiguous label
  and is unchanged from the 3-class model.
- **Korean only.** Korean tokenizer, Korean training data.
- **Confidence is not accuracy.** It measures how concentrated the
  distribution is, not how often the model is right. No calibration performed.
- **Understated complaints skew neutral.** 아쉬웠어요 phrasing lands around 3
  stars rather than lower.

## Observed behaviour

Probing with crafted sentence pairs revealed that the model weights
**revisit-intent phrasing above sentiment adjectives**:

| Input | Star |
|---|---|
| 가격이 너무 비싸서 아쉬웠어요 하지만 또 갈 것 같아요 | 4.16 |
| 가격이 너무 비싸서 아쉬웠어요 다시는 안 갈 것 같아요 | 1.05 |
| 맛있었어요 근데 다시는 안 갈 것 같아요 | 1.92 (negative) |

The last row carries an explicit positive adjective yet is classified
negative. This matches how people assign stars in practice.

It is also more confident on colloquial phrasing than formal phrasing:
존맛탱 (slang for "delicious") scores 4.94 at confidence 0.87, while
매우 훌륭한 맛이었습니다 (formal, same meaning) scores 4.59 at 0.51.

## License

CC BY-NC-SA 4.0, inherited from KR3. Non-commercial use only.

## Links

- Predecessor: https://huggingface.co/likeyellow/klue-review-star
- Serving API: https://github.com/likeyellow/review-star-api
- Demo frontend: https://github.com/likeyellow/review-star-ai