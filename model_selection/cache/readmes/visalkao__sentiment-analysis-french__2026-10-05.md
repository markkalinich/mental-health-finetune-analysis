---
language: fr
tags:
- camembert
- sentiment-analysis
- french
license: mit
pipeline_tag: text-classification
datasets:
- tblard/allocine
demo: https://huggingface.co/spaces/visalkao/sentiment-analysis-french
---

# French Sentiment Analysis with CamemBERT

This model predicts sentiment (0: NEGATIVE, 1: POSITIVE) for French product reviews.

## How to Test the model
You can go to the space attach to this model - https://huggingface.co/spaces/visalkao/sentiment-analysis-french

## Note:
This model is finetuned on a subset of tblard/allocine dataset (7000 random samples 50-50).

## Example Output
```json
{
  "label": "POSITIVE",
  "score": 0.98
}
```

## Training procedure
The following hyperparameters were used during training:

* learning_rate: 2e-05
* train_batch_size: 8
* eval_batch_size: 8
* weight_decay=0.01
* num_epochs: 10
## Training results
Here is the result of training:

| Epoch | Training Loss | Validation Loss | Accuracy on Validation| Precision on Validation|
|-------|---------------|-----------------|---------------------|----------------------|
| 1     | 0.224300      | 0.166868        |      0.954000       |      0.955621        |
| 2     | 0.224000      | 0.174095        |      0.959500       |      0.959500        |
| 3     | 0.145400      | 0.194145        |      0.961500       |      0.961873        |
