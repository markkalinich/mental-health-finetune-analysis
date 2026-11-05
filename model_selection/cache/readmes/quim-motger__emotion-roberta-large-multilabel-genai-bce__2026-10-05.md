---
license: mit
language: en
tags:
- text-classification
- multi-label-classification
- emotion-classification
- app-reviews
- roberta
base_model: roberta-large
datasets:
- nlp4se/app-review-emotions
metrics:
- f1
pipeline_tag: text-classification
---

# emotion-roberta-large-multilabel-genai-bce

Fine-tuned `roberta-large` multi-label classifier over Plutchik's eight
emotions plus Neutral, applied to English mobile app review sentences.

This is the best-performing encoder-only configuration found in a broader
comparison of encoder-only and decoder-only LLMs for this task: a shared
multi-label classification head trained with a BCE loss that up-weights
each emotion's positive class in proportion to its rarity, on a training
pool augmented with LLM-generated synthetic reviews (100 per emotion) to
fix the baseline model's complete failure to detect Fear, Surprise and
Anger.

Under 10-fold cross-validation on the human-labelled ground truth, this
configuration reaches **macro-F1 0.591 (+-0.054)**, recovering all three
previously undetected emotions (Anger 0->0.501, Fear 0->0.410,
Surprise 0->0.346 F1) with no regression on the four majority emotions.

This specific checkpoint is refit on the **full** training pool (all
cross-validation folds combined, plus the same synthetic augmentation), so
it has no internal held-out set of its own -- treat the cross-validated
macro-F1 above as the expected-performance estimate for this recipe, not a
number to reproduce exactly from this single checkpoint.

## Labels

`Joy`, `Trust`, `Fear`, `Surprise`, `Sadness`, `Disgust`, `Anger`,
`Anticipation`, `Neutral` -- multi-label (0 or more may apply per sentence).

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained("quim-motger/emotion-roberta-large-multilabel-genai-bce")
model = AutoModelForSequenceClassification.from_pretrained("quim-motger/emotion-roberta-large-multilabel-genai-bce")

emotions = ["Joy", "Trust", "Fear", "Surprise", "Sadness", "Disgust", "Anger", "Anticipation", "Neutral"]

text = "This app used to be great but the last update broke everything."
inputs = tok(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    probs = torch.sigmoid(model(**inputs).logits)[0]

predicted = [e for e, p in zip(emotions, probs) if p >= 0.5]
print(predicted, probs.tolist())
```

Note: the paper's decision rule assigns a label when `p >= 0.5`, falls back
to the single most confident label if none cross that threshold, and caps
predictions at 3 labels (the maximum cardinality observed in the ground
truth). Replicate that rule yourself for scoring compatible with the paper.

## Training data

- Human-labelled ground truth: 1,112 sentences from 257 apps across 10
  Google Play categories, adapted from Plutchik's eight basic emotions plus
  Neutral (Motger et al., 2025).
- Synthetic augmentation: up to 100 additional LLM-generated reviews per
  emotion (`claude-opus-4-6`, few-shot with guideline examples plus dataset
  exemplars), selected via an embedding-based augmentation-utility ranking
  before injection.

## Citation

If you use this model, please cite the ground-truth dataset paper
referenced in the parent replication package.
