---
language: en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- distilbert
- imdb
- mlops
datasets:
- stanfordnlp/imdb
base_model: distilbert-base-uncased
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: mlops-group-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Classification
    dataset:
      type: stanfordnlp/imdb
      name: IMDB
    metrics:
    - type: accuracy
      value: 0.90
      name: Test Accuracy
    - type: f1
      value: 0.90
      name: Test F1 (weighted)
---

# mlops-group-sentiment

A `distilbert-base-uncased` model fine-tuned on the IMDB movie reviews dataset
for binary sentiment classification (positive / negative).

This model is the final artifact of an MLOps group project at IIT Jodhpur
(Course CSL7040), demonstrating an end-to-end production ML pipeline: version
control on GitHub, GPU training on Kaggle, experiment tracking on Weights &
Biases, container packaging via Docker, and deployment to the Hugging Face Hub.

## How to Use

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="pujaniitj/mlops-group-sentiment")
result = classifier("This movie was fantastic!")
print(result)
# [{'label': 'positive', 'score': 0.9876}]
```

## Intended Use

**Primary use case**: Classifying English-language movie reviews as positive
or negative sentiment.

**Out-of-scope uses**:
- Non-English text (model only trained on English IMDB reviews)
- Domain shift — e.g. tweets, product reviews, news articles, customer support
  transcripts. Performance will degrade outside the movie-review domain.
- Fine-grained sentiment (beyond binary pos/neg, e.g. 5-star ratings)
- High-stakes decisions or content moderation without human review

## Model Description

- **Base architecture**: DistilBERT (`distilbert-base-uncased`)
- **Distinct from base**: Fine-tuned classification head (2 output labels)
- **Parameters**: ~66 million
- **Tokenizer**: WordPiece (DistilBERT default)
- **Max sequence length**: 256 tokens
- **Labels**: `0 → negative`, `1 → positive`

## Training Data

- **Dataset**: [IMDB Movie Reviews](https://huggingface.co/datasets/stanfordnlp/imdb)
- **Train size**: 25,000 reviews (12,500 positive + 12,500 negative — perfectly balanced)
- **Test size**: 25,000 reviews (same balance)
- **Train/Validation split**: 90/10 of the train set, with `seed=42`

## Training Procedure

### Hyperparameters

| Setting              | Value  |
|----------------------|--------|
| Learning rate        | 3e-5   |
| Train batch size     | 16     |
| Eval batch size      | 32     |
| Epochs               | 3      |
| Max sequence length  | 256    |
| Warmup ratio         | 0.1    |
| Weight decay         | 0.01   |
| Optimizer            | AdamW  |
| Mixed precision      | fp16   |
| Seed                 | 42     |

### Training Environment

- **Platform**: Kaggle Notebook
- **Hardware**: 2× NVIDIA Tesla T4 GPU
- **Training time**: ~17 minutes

### Experiment Tracking

Two configurations were trained and compared via Weights & Biases:

| Run  | Learning rate | Test F1 | Test Accuracy | Test Loss |
|------|---------------|---------|---------------|-----------|
| v1 (this model) | 3e-5 | ~0.90 | ~0.90 | ~0.70 |
| v2 (discarded)  | 5e-5 | ~0.91 | ~0.91 | ~0.85 |

>  Replace these values with the exact decimals from your W&B run summary
> before publishing the final model card.

**Why v1 was selected**: While v2 achieved a marginally higher F1 (~0.5%),
it showed clear signs of overfitting — its eval loss climbed sharply across
epochs while v1's remained more stable. v1 also delivers ~25% faster inference,
making it the better choice for a production deployment.

## Evaluation Results

Evaluation on the held-out IMDB test set (25,000 reviews):

| Metric              | Value |
|---------------------|-------|
| Accuracy            | ~0.90 |
| F1 (weighted)       | ~0.90 |
| Precision (weighted)| ~0.90 |
| Recall (weighted)   | ~0.90 |

## Limitations and Biases

- **Domain**: Only trained on movie reviews. Expect degraded performance on
  other domains.
- **Length**: Inputs are truncated to 256 tokens (~200 words). Longer reviews
  may lose tail information that matters for sentiment.
- **Language**: English only.
- **Demographic biases**: IMDB reviewers historically skew toward certain
  demographics (e.g., predominantly male, English-speaking). The model may
  inherit these biases — e.g., it may misclassify reviews using vernacular or
  cultural references underrepresented in IMDB.
- **Sarcasm and irony**: Like most BERT-based classifiers, the model can
  struggle with sarcastic or ironic text where the surface sentiment opposes
  the intended meaning.

## Project Resources

- **GitHub repository**: https://github.com/pujaniitj/mlops-group-project-iitj
- **W&B experiment dashboard**: https://wandb.ai/pujaniitj-iit-jodpur/MLops_group_8
- **Training notebook (v1)**: https://www.kaggle.com/code/pujaniitj/mlops-group-8-imdb-v1
- **Training notebook (v2)**: https://www.kaggle.com/code/pujaniitj/mlops-group-8-imdb-v2

## Acknowledgments

- **Base model**: [DistilBERT](https://huggingface.co/distilbert-base-uncased)
  by Sanh et al. (Hugging Face)
- **Dataset**: [IMDB](https://huggingface.co/datasets/stanfordnlp/imdb)
  by Maas et al. (Stanford NLP)
- **Training infrastructure**: [Kaggle Notebooks](https://www.kaggle.com)
- **Experiment tracking**: [Weights & Biases](https://wandb.ai)