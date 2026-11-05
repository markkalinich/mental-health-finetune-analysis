---
language:
- en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
datasets:
  - stanfordnlp/imdb

tags:
- distilbert
- sentiment-analysis
- text-classification
- imdb
- fine-tuned
base_model:
- distilbert/distilbert-base-uncased
---

# DistilBERT IMDb Sentiment Analysis

This model is a fine-tuned version of [`distilbert/distilbert-base-uncased`](https://huggingface.co/distilbert/distilbert-base-uncased) for **binary sentiment classification** of English movie reviews.

It predicts whether a movie review expresses a positive or negative sentiment.

## Model Details

- **Model:** DistilBERT Base Uncased
- **Task:** Sentiment Analysis
- **Language:** English
- **Dataset:** [IMDb Movie Reviews](https://huggingface.co/datasets/stanfordnlp/imdb)
- **Number of classes:** 2
- **Labels:**
  - `0`: NEGATIVE
  - `1`: POSITIVE
- **Maximum sequence length:** 256 tokens
- **Fine-tuning framework:** Hugging Face Transformers
- **Training approach:** Supervised fine-tuning

## Intended Use

This model is intended for:
- Classifying movie reviews as positive or negative.
- Experimenting with transformer-based text classification.
- Learning and demonstrating the Hugging Face fine-tuning workflow.

It is not specifically designed for sarcasm detection, emotion classification, or sentiment analysis in domains other than movie reviews.

## Training Data

The model was fine-tuned using the IMDb dataset, which contains movie reviews labeled as positive or negative.

The original training split was divided into:
- **Training set:** 90% of the original training data.
- **Validation set:** 10% of the original training data.
- **Test set:** The original IMDb test split.

The validation set was used for model evaluation and model selection during training.

## Training Procedure

The model was fine-tuned using the Hugging Face `Trainer` API.

| Hyperparameter | Value |
|---|---|
| Base model | `distilbert/distilbert-base-uncased` |
| Learning rate | 2e-5 |
| Training epochs | 3 |
| Training batch size | 16 |
| Weight decay | 0.01 |
| Maximum sequence length | 256 |
| Evaluation strategy | Per epoch |
| Model selection metric | F1-score |
| Optimizer | Trainer default |

## Evaluation

The model was evaluated on the IMDb test split using the following metrics:

- Accuracy
- Precision
- Recall
- F1-score


| Metric | Score |
|---|---|
| Accuracy | `0.91176` |
| Precision | `0.9099235425294679` |
| Recall | `0.914` |
| F1-score | `0.9119572158365262` |

## Usage

You can load the model directly using the Transformers pipeline.

```python
from transformers import pipeline

model_id = "YOUR_USERNAME/distilbert-imdb-sentiment"

classifier = pipeline(
    "text-classification",
    model=model_id
)

text = "The movie was fantastic. The acting and story were amazing!"

result = classifier(text)

print(result)
```

Example output:

```python
[{'label': 'POSITIVE', 'score': 0.99}]
```

The score is the model's confidence for its predicted label. This example is illustrative, not a measured result.

## Limitations and Bias

- The model is trained on IMDb movie reviews and may not generalize well to other types of text.
- It may struggle with sarcasm, ambiguous opinions, mixed sentiment, or complex language.
- Its predictions may reflect biases present in the training data.
- The confidence score should not be interpreted as a perfectly calibrated probability.

## Frameworks

- [Transformers](https://huggingface.co/docs/transformers)
- [Datasets](https://huggingface.co/docs/datasets)
- [PyTorch](https://pytorch.org/)

## Author

**Arjo Ghosh**

This project was created as a practical exercise in fine-tuning and deploying transformer-based models using Hugging Face.