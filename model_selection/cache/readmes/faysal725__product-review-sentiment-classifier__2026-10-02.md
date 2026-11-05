---
language: en
license: mit
tags:
  - setfit
  - sentiment-analysis
  - product-reviews
  - text-classification
  - binary-classification
metrics:
  - accuracy
  - f1
datasets:
  - yassiracharki/Amazon_Reviews_Binary_for_Sentiment_Analysis
pipeline_tag: text-classification
---

# Product Review Sentiment Classifier

Binary sentiment classifier for product reviews — **positive** or **negative** with calibrated confidence scores.

## Performance

| Metric   | Score  |
|----------|--------|
| Accuracy | 91.2%  |
| F1       | 0.913  |
| Brier    | 0.079  |

## Usage

```python
from setfit import SetFitModel
import pickle, numpy as np

model = SetFitModel.from_pretrained("faysal725/product-review-sentiment-classifier")

# For calibrated confidence, download platt_calibrator.pkl from this repo
with open("platt_calibrator.pkl", "rb") as f:
    platt = pickle.load(f)

text = "This product is amazing, best purchase ever!"
raw_probs = np.array(model.predict_proba([text]))
calibrated = platt.predict_proba(raw_probs[:, 1].reshape(-1, 1))[0]
label = "positive" if calibrated[1] >= 0.5 else "negative"
confidence = max(calibrated)

print(f"{label} ({confidence:.1%})")
```

## Training

- **Method:** SetFit (few-shot contrastive learning, 256 examples)
- **Backbone:** paraphrase-mpnet-base-v2
- **Calibration:** Platt scaling (LogisticRegression on raw scores)
- **Data:** Amazon Reviews Binary (Apache-2.0), 10k balanced subset

## Full Package

For the complete package with FastAPI server, batch endpoint, Docker deployment, and full documentation, visit [Gumroad](https://faysaldev.gumroad.com/l/product-review-sentiment-classifier).

## License

MIT
