---
language: en
tags:
- token-classification
- pii-detection
license: apache-2.0
datasets:
- custom_dataset
---

# Model Name

PII Detection Model Based on DistilBERT

## Model description

This model is a token classification model trained for detecting personally identifiable information (PII) entities such as names, addresses, dates of birth, credit card numbers, etc. The model is based on the DistilBERT architecture and has been fine-tuned on a custom dataset for PII detection.

## Intended use

The model is intended to be used for automatically identifying and extracting PII entities from text data. It can be incorporated into data processing pipelines for tasks such as data anonymization, redaction, compliance with privacy regulations, etc.

## Evaluation results

The model's performance was evaluated on a held-out validation set using the following metrics:

- Precision: 94%
- Recall: 96%
- F1 Score: 95%
- Accuracy: 99%

## Limitations and bias

- The model's performance may vary depending on the quality and diversity of the input data.
- It may exhibit biases present in the training data, such as overrepresentation or underrepresentation of certain demographic groups or types of PII.
- The model may struggle with detecting PII entities in noisy or poorly formatted text.

## Ethical considerations

- Care should be taken when deploying the model in production to ensure that it does not inadvertently expose sensitive information or violate individuals' privacy rights.
- Data used to train and evaluate the model should be handled with caution to avoid the risk of exposing PII.
- Regular monitoring and auditing of the model's predictions may be necessary to identify and mitigate any potential biases or errors.

## Model Training and Evaluation Results

| Epoch | Training Loss | Validation Loss | Precision | Recall | F1 Score | Accuracy |
|-------|---------------|-----------------|-----------|--------|----------|----------|
| 1     | 0.047         | 0.051537        | 91.35%    | 95.23% | 93.25%   | 98.56%   |
| 2     | 0.0307        | 0.043873        | 93.27%    | 96.10% | 94.66%   | 98.75%   |
| 3     | 0.0208        | 0.04702         | 91.83%    | 95.49% | 93.62%   | 98.54%   |
| 4     | 0.0147        | 0.046979        | 93.27%    | 94.97% | 94.11%   | 98.77%   |
| 5     | 0.0094        | 0.057863        | 93.41%    | 95.92% | 94.65%   | 98.70%   |


## Authors

- abhijeet__@outlook.com

