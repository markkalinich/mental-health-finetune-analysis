---
language: en
library_name: transformers
pipeline_tag: text-classification
license: mit
tags:
- sentiment-analysis
- distilbert
- sequence-classification
- academic-peer-review
- openreview
datasets:
- nhop/OpenReview
base_model:
- distilbert/distilbert-base-uncased
---

# Academic Sentiment Classifier (DistilBERT)

DistilBERT-based sequence classification model that predicts the sentiment polarity of academic peer-review text (binary: negative vs positive). It supports research on evaluating the sentiment of scholarly reviews and AI-generated critique, enabling large-scale, reproducible measurements for academic-style content.

## Model details

- Architecture: DistilBERT for Sequence Classification (2 labels)
- Max input length used during training: 512 tokens
- Labels:
  - LABEL_0 -> negative
  - LABEL_1 -> positive
- Format: `safetensors`

## Intended uses & limitations

Intended uses:

- Analyze sentiment of peer-review snippets, full reviews, or similar scholarly discourse.

Limitations:

- Binary polarity only (no neutral class); confidence scores should be interpreted with care.
- Domain-specific: optimized for academic review-style English text; may underperform on general-domain data.
- Not a replacement for human judgement or editorial decision-making.

Ethical considerations and bias:

- Scholarly reviews can contain technical jargon, hedging, and nuanced tone; polarity is an imperfect proxy for quality or fairness.
- Potential biases may reflect those present in the underlying corpus.

## Training data

The model was fine-tuned on a corpus of academic peer-review text curated from OpenReview review texts. The task is binary sentiment classification over review text spans.

Note: If you plan to use or extend the underlying data, please review the terms of use for OpenReview and any relevant dataset licenses.

## Training procedure (high level)

- Base model: DistilBERT (transformers)
- Objective: single-label binary classification
- Tokenization: standard DistilBERT tokenizer, truncation to 512 tokens
- Optimizer/scheduler: standard Trainer defaults (AdamW with linear schedule)

Exact hyperparameters may vary across runs; typical training uses AdamW with a linear learning rate schedule and truncation to 512 tokens.

## How to use

Basic pipeline usage:

```python
from transformers import pipeline

clf = pipeline(
    task="text-classification",
    model="EvilScript/academic-sentiment-classifier",
    tokenizer="EvilScript/academic-sentiment-classifier",
    return_all_scores=False,
)

text = "The paper is clearly written and provides strong empirical support for the claims."
print(clf(text))
# Example output: [{'label': 'LABEL_1', 'score': 0.97}]  # LABEL_1 -> positive
```

If you prefer friendly labels, you can map them:

```python
from transformers import pipeline

id2name = {"LABEL_0": "negative", "LABEL_1": "positive"}
clf = pipeline("text-classification", model="EvilScript/academic-sentiment-classifier")
res = clf("This section lacks clarity and the experiments are inconclusive.")[0]
res["label"] = id2name.get(res["label"], res["label"])  # map to human-friendly label
print(res)
```

Batch inference:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

device = 0 if torch.cuda.is_available() else -1
tok = AutoTokenizer.from_pretrained("EvilScript/academic-sentiment-classifier")
model = AutoModelForSequenceClassification.from_pretrained("EvilScript/academic-sentiment-classifier")

texts = [
    "I recommend acceptance; the methodology is solid and results are convincing.",
    "Major concerns remain; the evaluation is incomplete and unclear.",
]

inputs = tok(texts, padding=True, truncation=True, max_length=512, return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
probs = torch.softmax(logits, dim=-1)
pred_ids = probs.argmax(dim=-1)

# Map to friendly labels
id2name = {0: "negative", 1: "positive"}
preds = [id2name[i.item()] for i in pred_ids]
print(list(zip(texts, preds)))
```

## Evaluation

If you compute new metrics on public datasets or benchmarks, consider sharing them via a pull request to this model card.

## License

The model weights and card are released under the MIT license. Review and comply with any third-party data licenses if reusing the training data.

## Citation

If you use this model, please cite the project:

```bibtex
@misc{federico_torrielli_2025,
	author       = { Federico Torrielli and Stefano Locci },
	title        = { academic-sentiment-classifier },
	year         = 2025,
	url          = { https://huggingface.co/EvilScript/academic-sentiment-classifier },
	doi          = { 10.57967/hf/6535 },
	publisher    = { Hugging Face }
}
```