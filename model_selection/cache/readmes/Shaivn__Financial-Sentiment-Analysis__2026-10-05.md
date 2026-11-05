---
license: apache-2.0
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- finance
- sentiment-analysis
language:
- en
base_model:
- google-bert/bert-base-uncased
---

# BERT Fine-tuned - Financial Sentiment Analysis Model

<div style="text-align:center;">
    <img src="https://huggingface.co/Shaivn/Financial-Sentiment-Analysis/resolve/main/financial-sentiment-analysis-logo.png" alt="logo" style="width:250px;height:250px;">
</div>



This model is a Fine-Tuned version of BERT (bert-base-uncased)
It is designed to classify text into positive, neutral, and negative sentiments. The fine-tuning was performed using the Financial Phrase Bank dataset.

## Results

It achieves the following results on the evaluation set:

* F1 Score: 0.9468
* Validation loss: 0.1860

## Training Data

The dataset consists of 4840 sentences of the financial phrase bank. The dataset was annotated by 16 people with adequate background knowledge of financial markets.

## Training hyperparameters

The following hyperparameters were used during training:

* learning rate : 2e-5
* train_batch_size : 32
* eval_batch_size: 32
* seed: 42
* Optimizer : AdamW
* num_epochs: 3


## Training Results

  | **Epoch**  | **Validation Loss**   | **Accuracy**  |
  |:----------:|:---------------------:|:-------------:|
  |01          | 0.1860                |    0.9468     |
  |02          | 0.1756                |    0.9424     |
  |03          | 0.1726                |    0.9432     |



This model is a part of my thesis: "A Proposal of a Sentiment Analysis Model for Business Intelligence"