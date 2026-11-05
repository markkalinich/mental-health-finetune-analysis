---
language: en
license: apache-2.0
library_name: transformers
tags:
  - text-classification
  - emotion
  - distilbert
  - fine-tuned
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
base_model: distilbert-base-uncased
pipeline_tag: text-classification
widget:
  - text: "I'm so excited about my new job!"
    example_title: Joy
  - text: "I miss my grandmother so much."
    example_title: Sadness
  - text: "I love spending time with my family."
    example_title: Love
  - text: "There's something behind that door..."
    example_title: Fear
  - text: "I can't believe they would do this to me."
    example_title: Anger (tricky)
  - text: "Wait, you got engaged?!"
    example_title: Surprise
model-index:
  - name: distilbert-emotion-finetuned
    results:
      - task:
          type: text-classification
          name: Text Classification
        dataset:
          name: dair-ai/emotion
          type: emotion
          split: validation
        metrics:
          - type: accuracy
            value: 0.933
            name: Accuracy
---

# DistilBERT — Emotion Classifier

Fine-tuned [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) on the [`emotion`](https://huggingface.co/datasets/dair-ai/emotion) dataset for 6-class emotion classification.

**Validation accuracy: 93.3%** (1,000-sample validation subset, 3 epochs, Colab CPU).

## Labels

The model predicts one of six emotions:

| ID | Label    |
|----|----------|
| 0  | sadness  |
| 1  | joy      |
| 2  | love     |
| 3  | anger    |
| 4  | fear     |
| 5  | surprise |

`id2label` and `label2id` are baked into `config.json`, so `pipeline(...)` returns string labels directly.

## How to use

Quick start with `pipeline`:

~~~python
from transformers import pipeline

clf = pipeline("text-classification", model="harshaojha/distilbert-emotion-finetuned")
clf("I'm so excited about my new job!")
# [{'label': 'joy', 'score': 0.998...}]
~~~

For full probability distributions across all 6 classes:

~~~python
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForSequenceClassification

REPO = "harshaojha/distilbert-emotion-finetuned"
tok = AutoTokenizer.from_pretrained(REPO)
mdl = AutoModelForSequenceClassification.from_pretrained(REPO)
mdl.eval()

inputs = tok("I miss my grandmother so much.", return_tensors="pt", truncation=True, max_length=64)
with torch.no_grad():
    probs = F.softmax(mdl(**inputs).logits, dim=-1)[0]

for i, p in enumerate(probs):
    print(f"{mdl.config.id2label[i]}: {p.item():.3f}")
~~~

## Training data

- Dataset: [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion)
- Training subset: 6,000 examples (shuffled, seed=42, from the full 16,000-example train split)
- Validation subset: 1,000 examples (shuffled, seed=42, from the full 2,000-example validation split)
- Tokenizer truncation: `max_length=64`

## Training procedure

| Hyperparameter           | Value                          |
|--------------------------|--------------------------------|
| Base model               | distilbert-base-uncased        |
| Optimizer                | AdamW (Trainer default)        |
| Learning rate            | 3e-5                           |
| Batch size (train)       | 32                             |
| Batch size (eval)        | 64                             |
| Epochs                   | 3                              |
| Weight decay             | 0.01                           |
| Max sequence length      | 64                             |
| Mixed precision          | None (CPU)                     |
| Best checkpoint strategy | `load_best_model_at_end=True`  |

Trained on a Google Colab CPU runtime in ~90 minutes.

## Training results

| Epoch | Training Loss | Validation Loss | Accuracy   |
|-------|---------------|-----------------|------------|
| 1     | 0.7161        | 0.4197          | 0.8830     |
| 2     | 0.2607        | 0.2323          | 0.9220     |
| 3     | 0.1385        | 0.2097          | **0.9330** |

Both training and validation loss were still decreasing at epoch 3, suggesting more epochs (or full data) would push accuracy higher.

## Limitations

- **Class imbalance / joy bias.** The `emotion` dataset is dominated by `joy` and `sadness`. The model can over-predict `joy` on indirect or sarcastic phrasings — e.g. *"I can't believe they would do this to me"* may be classified as `joy` rather than `anger` due to surface-pattern overlap with positively-toned "I can't believe …" sentences in the training data.
- **Domain.** Trained on short, single-sentence English text. Performance on long passages, formal writing, or non-English text is not evaluated.
- **Coarse label set.** Only 6 broad classes — there is no `disappointment`, `annoyance`, or `disapproval`. For finer-grained emotion classification, see [`go_emotions`](https://huggingface.co/datasets/google-research-datasets/go_emotions) (27 labels) as a base.
- **Subsampled training data.** Trained on 6,000 / 16,000 examples to fit a CPU runtime budget. Full-data training on a GPU typically reaches ~94% accuracy.

## Possible improvements

- **Class-weighted loss** to counter the joy bias (weight inversely proportional to class frequency).
- **Full training set** (16k examples) with 6 epochs on a GPU — expected ~94% accuracy.
- **Switch to `go_emotions`** for fine-grained labels (multi-label, sigmoid + threshold).

## Framework versions

- transformers 4.46.3
- huggingface_hub 0.26.5
- datasets, evaluate, accelerate, scikit-learn

## License

Apache-2.0 (inherits from the base model and dataset).