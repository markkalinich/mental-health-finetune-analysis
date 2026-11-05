---
license: apache-2.0
library_name: transformers
tags:
  - generated_from_trainer
  - text-classification
  - sentiment-analysis
  - distilbert
datasets:
  - stanfordnlp/imdb
metrics:
  - accuracy
  - f1
base_model: distilbert-base-uncased
pipeline_tag: text-classification
model-index:
  - name: finetuning-sentiment-model-3000-samples
    results:
      - task:
          type: text-classification
          name: Text Classification
        dataset:
          name: imdb
          type: stanfordnlp/imdb
        metrics:
          - type: accuracy
            value: 0.87
            name: Accuracy
          - type: f1
            value: 0.8713
            name: F1
---

# finetuning-sentiment-model-3000-samples

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased)
on a 3,000-example subset of the [IMDB dataset](https://huggingface.co/datasets/stanfordnlp/imdb) for binary
sentiment classification (positive / negative movie reviews).

## Model description

DistilBERT is a smaller, faster, and cheaper version of BERT. This model adds a sequence
classification head (2 labels) on top of `distilbert-base-uncased` and fine-tunes it for
sentiment analysis.

- **Task:** Text Classification (Sentiment Analysis)
- **Base model:** distilbert-base-uncased
- **Language:** English
- **Labels:** `LABEL_0` = Negative, `LABEL_1` = Positive

## Training and evaluation data

The model was trained on a shuffled subset of the IMDB dataset (seed=42):
- **Training set:** 3,000 examples
- **Evaluation set:** 300 examples

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: AdamW (betas=(0.9,0.999), epsilon=1e-08)
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

On the 300-example evaluation set, the model achieves:

| Metric   | Value  |
|----------|--------|
| Loss     | 0.3321 |
| Accuracy | 0.8700 |
| F1       | 0.8713 |

### Framework versions

- Transformers 5.16.1
- PyTorch 2.6.0+cpu
- Datasets 5.0.1
- Tokenizers 0.23.2

## How to use

```python
from transformers import pipeline

sentiment_model = pipeline(
    model="ousmane93/finetuning-sentiment-model-3000-samples"
)
sentiment_model(["I love this movie", "This movie sucks!"])
```

## Limitations

- Fine-tuned on a small subset of IMDB (3,000 training / 300 evaluation examples), so
  performance may be lower than a model trained on the full 25,000-example dataset.
- Trained only on English-language movie reviews; performance on other domains,
  topics, or languages is not guaranteed.
- No comparison against other sentiment models has been performed as part of this project.
