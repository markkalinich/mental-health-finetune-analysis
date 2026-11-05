---
language:
- tr
license: mit
base_model: dbmdz/bert-base-turkish-cased
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- emotion
- emotion-classification
- turkish
- bert
metrics:
- accuracy
- f1
model-index:
- name: turkish-emotion-classifier
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    metrics:
    - type: f1
      value: 0.9683
      name: F1 (macro)
    - type: accuracy
      value: 0.969
      name: Accuracy
widget:
- text: Bu film gerçekten harikaydı, çok keyif aldım!
- text: Bugün başıma gelenler beni çok üzdü.
- text: Bu duruma gerçekten çok sinirlendim.
- text: Karşımda onu görünce çok şaşırdım!
---

# turkish-emotion-classifier

A fine-tuned version of [`dbmdz/bert-base-turkish-cased`](https://huggingface.co/dbmdz/bert-base-turkish-cased)
for multi-class **emotion classification** of Turkish text.

## Model description

The model takes a short Turkish text and predicts one of six emotion labels. It
is a standard `BertForSequenceClassification` head fine-tuned on top of the cased
Turkish BERT (BERTurk) encoder.

- **Base model:** `dbmdz/bert-base-turkish-cased`
- **Language:** Turkish (`tr`)
- **Task:** Single-label, multi-class text classification (emotion)
- **Number of classes:** 6

### Labels

The label ids follow `model.config.id2label`:

| id | label |
|----|-------|
| 0  | `anger`|
| 1  | `disgust`|
| 2  | `fear`|
| 3  | `joy`|
| 4  | `sadness`|
| 5  | `surprise`|

## Intended uses & limitations

**Intended use:** classifying the dominant emotion of short, informal Turkish
sentences (reviews, social posts, messages).

The model expects **raw text** — no special preprocessing is required. Just pass
your sentence directly; the tokenizer (shipped with the model) handles everything.

**Limitations / out of scope:**
- Long, multi-sentence documents. The model was trained on short single sentences
  and predicts a single dominant emotion. For longer text, split into sentences and
  classify each one separately.
- Formal/legal text, languages other than Turkish, and fine-grained sentiment
  beyond the six trained labels.

## How to use

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="furkankarakuz/turkish-emotion-classifier")
print(pipe("Bu film gerçekten harikaydı!"))
# [{'label': 'joy', 'score': 0.99}]
```

Or load the model and tokenizer directly:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("furkankarakuz/turkish-emotion-classifier")
tokenizer = AutoTokenizer.from_pretrained("furkankarakuz/turkish-emotion-classifier")
```

## Training and evaluation data

<!-- TODO: add the dataset's source and license if you can share them. -->
Trained on a manually labeled Turkish emotion dataset of roughly **23,000** samples
covering six emotions (anger, disgust, fear, joy, sadness, surprise). The data was
split with stratification so the class balance is preserved across splits:

- **Train:** 70%
- **Validation:** 15%
- **Test:** 15%

Labels were integer-encoded with `LabelEncoder`, fit on the training split only.
No lossy text cleaning was applied; the model is trained on raw text.

## Training procedure

Fine-tuned with the 🤗 Transformers `Trainer`, using a class-weighted
cross-entropy loss to handle class imbalance. The best checkpoint was selected on
the validation macro-F1 (best at **epoch 8**) and restored as the final model.

### Training hyperparameters

| Hyperparameter | Value |
|----------------|-------|
| Base model | `dbmdz/bert-base-turkish-cased` |
| Max sequence length | 64 (dynamic padding) |
| Train batch size | 32 |
| Eval batch size | 64 |
| Learning rate | 2e-5 |
| LR scheduler | linear, warmup ratio 0.1 |
| Optimizer | AdamW (torch fused), betas=(0.9, 0.999), eps=1e-8 |
| Epochs | 10 (early stopping, patience 2) |
| Loss | class-weighted cross-entropy |
| Best-model metric | `f1_macro` (validation) |
| Mixed precision | native AMP |
| Seed | 42 |

### Validation results per epoch

The best checkpoint (**epoch 8**, by validation macro-F1) was restored as the final model.

| Epoch | Training Loss | Validation Loss | Accuracy | F1 (macro) | Precision (macro) | Recall (macro) |
|------:|--------------:|----------------:|---------:|-----------:|------------------:|---------------:|
| 1 | 0.1866 | 0.1858 | 0.9460 | 0.9460 | 0.9481 | 0.9442 |
| 2 | 0.1412 | 0.1436 | 0.9591 | 0.9583 | 0.9575 | 0.9592 |
| 3 | 0.0766 | 0.1639 | 0.9619 | 0.9617 | 0.9621 | 0.9619 |
| 4 | 0.0364 | 0.1749 | 0.9622 | 0.9616 | 0.9627 | 0.9608 |
| 5 | 0.0269 | 0.1892 | 0.9631 | 0.9620 | 0.9609 | 0.9635 |
| 6 | 0.0132 | 0.1901 | 0.9656 | 0.9650 | 0.9652 | 0.9649 |
| 7 | 0.0141 | 0.1980 | 0.9642 | 0.9635 | 0.9648 | 0.9625 |
| **8** | **0.0011** | **0.1990** | **0.9676** | **0.9673** | **0.9670** | **0.9676** |
| 9 | 0.0063 | 0.2036 | 0.9665 | 0.9657 | 0.9661 | 0.9656 |
| 10 | 0.0043 | 0.2022 | 0.9670 | 0.9664 | 0.9667 | 0.9662 |

## Evaluation results

Results on the held-out **test** set (3,520 samples), using the final model:

| Metric | Value |
|--------|-------|
| Accuracy | 0.9690 |
| F1 (macro) | 0.9683 |
| Precision (macro) | 0.9676 |
| Recall (macro) | 0.9691 |
| Loss | 0.1880 |

### Per-class results (test set)

| Label | Precision | Recall | F1 | Support |
|-------|----------:|-------:|---:|--------:|
| anger | 0.96 | 0.96 | 0.96 | 616 |
| disgust | 0.96 | 0.98 | 0.97 | 419 |
| fear | 0.98 | 0.97 | 0.97 | 623 |
| joy | 0.98 | 0.98 | 0.98 | 783 |
| sadness | 0.96 | 0.97 | 0.96 | 662 |
| surprise | 0.96 | 0.96 | 0.96 | 417 |

## Limitations and bias

The model reflects the distribution and any biases of its training data and may
underperform on dialects, domains, or emotion expressions not well represented in
it. Predictions are most reliable for short, informal text similar to the training
data.

## Framework versions

- Transformers 5.9.0
- PyTorch 2.11.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2