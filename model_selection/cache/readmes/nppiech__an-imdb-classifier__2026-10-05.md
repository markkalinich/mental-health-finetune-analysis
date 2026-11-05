---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- sentiment analysis
- text-classification
- distilbert
- imdb
- transformers
metrics:
- accuracy
model-index:
- name: an-imdb-classifier
  results: []
datasets:
- stanfordnlp/imdb
---

# an-imdb-classifier

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the stanfordnlp.imdb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3635
- Accuracy: 0.898

## Model description

This model is a fine-tuned version of the distilbert-base-uncased model, trained for sentiment analysis on a subset of the IMDb dataset.
It is designed to classify movie reviews as either positive or negative.

## Intended uses & limitations

This model is intended for use in classifying the sentiment of movie reviews. 

It can be used for tasks such as:
Automatically categorizing movie reviews on websites or platforms.
Analyzing the overall sentiment towards a particular movie.
Providing feedback to users based on their review sentiment.

## Training and evaluation data

The model was fine-tuned on a small subset of the IMDb dataset.

Training set size: 5000 examples
Evaluation set size: 500 examples

The dataset contains movie reviews labeled as either positive (label 1) or negative (label 0).
The distribution of labels in the training set is approximately equal (2494 negative, 2506 positive).

## Training procedure

The model was trained using the Hugging Face Trainer on the tokenized IMDb dataset subset, using the preprocess_function to tokenize the text and truncate it.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 313  | 0.3199          | 0.866    |
| 0.2966        | 2.0   | 626  | 0.3023          | 0.89     |
| 0.2966        | 3.0   | 939  | 0.3635          | 0.898    |


### Framework versions

- Transformers 4.55.0
- Pytorch 2.6.0+cu124
- Datasets 4.0.0
- Tokenizers 0.21.4