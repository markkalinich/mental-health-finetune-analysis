---
language: en
license: mit
library_name: transformers
datasets:
- imdb
tags:
- text-classification
- sentiment-analysis
- distilbert
pipeline_tag: text-classification
---

# Model Card: distilbert-imdb-sentiment-analysis 🎬

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) for sentiment analysis on the IMDB movie review dataset. It classifies text as either **positive** or **negative**.

## Model Description

This model was developed as an end-to-end project to demonstrate the process of fine-tuning a Transformer for a binary text classification task. The base model, DistilBERT, was chosen for its excellent balance of performance and computational efficiency. The model was trained on a comprehensive dataset of movie reviews, enabling it to understand and classify the sentiment of similar texts effectively.

The project utilized the Hugging Face ecosystem, including the `transformers`, `datasets`, and `evaluate` libraries, with PyTorch as the backend framework.

## Intended Uses & Limitations

### Intended Uses

This model is primarily intended for sentiment analysis on English-language text, particularly in the domain of user reviews (e.g., movies, products, services). It can be used to:

* Automatically categorize customer feedback.
* Gauge public opinion from social media posts.
* Power content recommendation systems based on user sentiment.

### Limitations

* **Domain Sensitivity:** The model was trained specifically on movie reviews. Its performance may be lower on texts from significantly different domains (e.g., legal documents, medical reports, or highly technical content).
* **Nuance and Sarcasm:** Like most sentiment analysis models, it may struggle to correctly classify sarcasm, irony, or complex sentences with mixed sentiments.
* **Bias:** The model is trained on the IMDB dataset, which reflects the language and biases of its contributors. It may therefore reproduce societal biases present in the training data.
* **Language:** This model is intended for English text only.

## How to Use

The easiest way to use this model is with a `pipeline` from the `transformers` library.

```python
from transformers import pipeline

# Load the sentiment analysis pipeline with our fine-tuned model
sentiment_analyzer = pipeline("sentiment-analysis", model="timothykimutai/distilbert-imdb-sentiment-analysis")

# Example 1: Positive review
result_pos = sentiment_analyzer("This movie was an absolute masterpiece! The acting was superb and the plot was gripping.")
print(result_pos)
# >>> [{'label': 'POSITIVE', 'score': 0.99...}]

# Example 2: Negative review
result_neg = sentiment_analyzer("I was really disappointed. The story was predictable and the characters were boring.")
print(result_neg)
# >>> [{'label': 'NEGATIVE', 'score': 0.99...}]
```

## Training and evaluation data

The model was fine-tuned on the IMDB (Internet Movie Database) dataset. This is a well-known benchmark dataset for binary sentiment classification, containing 50,000 highly polarized movie reviews.

* **Training set:** 25,000 reviews

* **Testing set:** 25,000 reviews

The data was preprocessed by tokenizing the text using the standard distilbert-base-uncased tokenizer, truncating sequences to a maximum length of 512 tokens.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.4312        | 1.0   | 125  | 0.4289          | 0.802    | 0.7981 | 0.8196    | 0.802  |
| 0.2557        | 2.0   | 250  | 0.3835          | 0.864    | 0.8634 | 0.8764    | 0.864  |
| 0.2714        | 3.0   | 375  | 0.3793          | 0.876    | 0.8759 | 0.8764    | 0.876  |


### Framework versions

- Transformers 4.55.0
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.4
