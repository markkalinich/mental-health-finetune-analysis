---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - text-classification
  - multi-label-classification
  - emotion-detection
  - distilbert
  - pytorch
datasets:
  - go_emotions
language:
  - en
metrics:
  - f1
pipeline_tag: text-classification
---

# EmotiCare — Multi-Label Emotion Classifier

EmotiCare is a fine-tuned [DistilBERT](https://huggingface.co/distilbert-base-uncased) model for **multi-label emotion detection** in English text. Given a sentence, it predicts one or more emotions from 28 categories drawn from the [GoEmotions](https://huggingface.co/datasets/go_emotions) dataset.

It is designed for use in applications that need nuanced, fine-grained emotion understanding — such as mental health tools, sentiment dashboards, chatbots, and content moderation systems.

## Emotions

The model classifies text into 28 emotions:

`admiration` · `amusement` · `anger` · `annoyance` · `approval` · `caring` · `confusion` · `curiosity` · `desire` · `disappointment` · `disapproval` · `disgust` · `embarrassment` · `excitement` · `fear` · `gratitude` · `grief` · `joy` · `love` · `nervousness` · `optimism` · `pride` · `realization` · `relief` · `remorse` · `sadness` · `surprise` · `neutral`

## Model Details

| Property | Value |
|---|---|
| Base model | `distilbert-base-uncased` |
| Architecture | DistilBertForSequenceClassification |
| Task | Multi-label text classification |
| Dataset | GoEmotions (simplified, 43,410 train samples) |
| Training epochs | 3 |
| Max sequence length | 512 tokens |
| Framework | PyTorch + 🤗 Transformers |

## Evaluation Results

Evaluated on the GoEmotions test set (5,427 examples):

| Metric | Score |
|---|---|
| F1 Macro | **0.4019** |
| F1 Micro | **0.5702** |
| Eval Loss | 0.0843 |

> Note: Multi-label emotion classification on GoEmotions is a challenging task due to class imbalance and overlapping emotions. F1 Micro of ~0.57 is competitive with similar fine-tuned DistilBERT baselines.

## Inference

### Using the 🤗 `pipeline` (recommended)

```python
from transformers import pipeline
import torch

classifier = pipeline(
    "text-classification",
    model="BruceIC/emoticare",  # replace with your HF repo path
    tokenizer="BruceIC/emoticare",
    top_k=None,                        # return scores for all labels
    device=0 if torch.cuda.is_available() else -1,
)

text = "I can't believe how thoughtful that was, I'm so touched."
results = classifier(text)

# Filter to emotions above a confidence threshold
threshold = 0.3
detected = [r for r in results[0] if r["score"] > threshold]
for emotion in sorted(detected, key=lambda x: -x["score"]):
    print(f"{emotion['label']:<20} {emotion['score']:.3f}")
```

**Example output:**
```
gratitude            0.847
admiration           0.612
love                 0.431
```

---

### Manual inference (more control)

```python
import torch
import torch.nn.functional as F
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

model_name = "BruceIC/emoticare"  # replace with your HF repo path

tokenizer = DistilBertTokenizer.from_pretrained(model_name)
model = DistilBertForSequenceClassification.from_pretrained(model_name)
model.eval()

def predict_emotions(text: str, threshold: float = 0.3):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512,
        padding=True,
    )
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.sigmoid(logits).squeeze()  # sigmoid for multi-label

    emotions = model.config.id2label
    results = [
        {"label": emotions[i], "score": float(probs[i])}
        for i in range(len(emotions))
        if float(probs[i]) > threshold
    ]
    return sorted(results, key=lambda x: -x["score"])

# Example
print(predict_emotions("I'm so proud of everything we've built together!"))
```

---

### Batch inference

```python
texts = [
    "I'm terrified of what might happen next.",
    "This is the best day of my life!",
    "I don't really feel anything about it.",
]

inputs = tokenizer(
    texts,
    return_tensors="pt",
    truncation=True,
    max_length=512,
    padding=True,
)

with torch.no_grad():
    logits = model(**inputs).logits

probs = torch.sigmoid(logits)  # shape: (batch_size, 28)
threshold = 0.3

for i, text in enumerate(texts):
    detected = [
        model.config.id2label[j]
        for j in range(28)
        if probs[i][j] > threshold
    ]
    print(f"Text: {text}")
    print(f"Emotions: {', '.join(detected) or 'none above threshold'}\n")
```

## Training Details

- **Base model:** `distilbert-base-uncased`
- **Dataset:** [go_emotions](https://huggingface.co/datasets/go_emotions) (simplified config)
- **Loss function:** Binary Cross-Entropy (multi-label)
- **Optimizer:** AdamW with linear warmup + decay
- **Learning rate:** 2e-5 (peak)
- **Batch size:** 16
- **Epochs:** 3
- **Best checkpoint:** step 8142 (epoch 3)

## Limitations

- Trained on Reddit comments — performance may degrade on formal text, non-native English, or very short inputs.
- Some rare emotions (grief, pride, relief) have limited training examples and lower per-class F1.
- Outputs are probabilities; the optimal threshold (default 0.3) may need tuning for your use case.

## Citation

If you use this model, please cite the GoEmotions dataset:

```bibtex
@inproceedings{demszky-etal-2020-goemotions,
  title     = {{GoEmotions}: A Dataset of Fine-Grained Emotions},
  author    = {Demszky, Dorottya and Movshovitz-Attias, Dana and Ko, Jeongwook
               and Cowen, Alan and Nemade, Gaurav and Ravi, Sujith},
  booktitle = {Proceedings of the 58th Annual Meeting of the Association for
               Computational Linguistics},
  year      = {2020},
}
```
