---
language:
- ur
license: apache-2.0
base_model:
- Khubaib01/roman-urdu-sentiment-xlm-r
pipeline_tag: text-classification
datasets:
- custom
metrics:
- f1
- accuracy
tags:
- roman-urdu
- emotion-classification
- text-classification
- xlm-roberta
- ekman
- urdu-nlp
model-index:
- name: roman-urdu-emotion-xlmr
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    metrics:
    - type: f1
      value: 0.7149
      name: Macro F1
    - type: accuracy
      value: 0.7148
      name: Accuracy
---

# Roman Urdu Emotion Classifier (XLM-R)

A fine-tuned **XLM-RoBERTa** model for **7-class emotion classification** in Roman Urdu text,
covering Ekman's six basic emotions plus a *none* class.

## Model Details

| Field            | Value                                          |
|------------------|------------------------------------------------|
| Base model       | `Khubaib01/roman-urdu-sentiment-xlm-r`         |
| Task             | Multi-class emotion classification             |
| Language         | Roman Urdu (Romanized Urdu / code-switched)    |
| Classes          | 7 (anger, disgust, fear, joy, sadness, surprise, none) |
| Parameters       | ~278M (XLM-R base + custom head)               |
| Max input length | 128 tokens                                     |

## Emotion Classes

| Label    | Ekman Emotion |
|----------|---------------|
| anger    |  Basic       |
| disgust  |  Basic       |
| fear     |  Basic       |
| joy      |  Basic       |
| sadness  |  Basic       |
| surprise |  Basic       |
| none     | No emotion    |

## Performance

Metrics calculated on test(unseen) dataset.

| Metric     | Score        |
|------------|--------------|
| Macro F1   | 0.7149 |
| Accuracy   | 0.7148 |

### Per-class F1 (Test Set)

| Emotion    | F1 Score |
|------------|----------|
| Anger      | 0.5962 |
| Disgust    | 0.5672 |
| Fear       | 0.8467 |
| Happy      | 0.7276 |
| Sad        | 0.6379 |
| Surprise   | 0.9349 |
| None       | 0.6937 |

## Architecture

```
Input (Roman Urdu text)
    → XLM-R Tokenizer (max_length=128)
    → XLM-R Encoder (12 layers, hidden=768)
    → [CLS] token representation
    → LayerNorm → Dropout(0.3)
    → Linear(768 → 256) → GELU → Dropout(0.15)
    → Linear(256 → 7)
    → CrossEntropyLoss (label_smoothing=0.1)
```

## Training Details

| Hyperparameter       | Value                    |
|----------------------|--------------------------|
| Base LR (encoder)    | 2e-5                     |
| Head LR              | 1e-4                     |
| Layer-wise LR decay  | 0.95 per layer           |
| Scheduler            | Cosine with 10% warm-up  |
| Epochs               | Up to 10 (early stopping)|
| Batch size           | 16                       |
| Label smoothing      | 0.1                      |
| Dropout              | 0.3                      |
| Optimizer            | AdamW                    |
| Mixed precision      | fp16                     |

**Key technique:** Discriminative layer-wise learning rates — the classification
head trains at 5× the base encoder rate, while lower encoder layers decay
further to preserve pre-trained multilingual representations.

## Dataset

- **Total samples:** 21,000
- **Split:** 80% train / 10% val / 10% test
- **Balance:** Perfectly balanced (3,000 samples per class)
- **Language:** Roman Urdu (social media messages)

## Usage

### ⚠️ Important — Custom Architecture

This model uses a **custom PyTorch `nn.Module`**, not a standard HuggingFace
`PreTrainedModel`. You must define the class before loading weights.

```python
from transformers import pipeline

HF_REPO_ID = "Khubaib01/roman-urdu-emotion-xlmr"

pipe = pipeline(
        "text-classification",
        model="f{HF_REPO_ID}",
        trust_remote_code=True,
        top_k=None,
    )
pipe("bhai ab mera kia hoga")
```

## Limitations

- Trained on a specific Roman Urdu dataset; performance may vary on
  highly code-switched (Urdu + English) or dialectal text.
- The *none* class captures emotionally neutral text but may misfire
  on sarcasm or implicit sentiment.
- Not evaluated on formal/literary Urdu.

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{roman-urdu-emotion-xlmr,
  author    = {Muhammad Khubaib Ahmad},
  title     = {Roman Urdu Emotion Classifier (XLM-R)},
  year      = {2026},
  publisher = {HuggingFace},
  url       = {https://huggingface.co/Khubaib01/roman-urdu-emotion-xlmr}
}
```