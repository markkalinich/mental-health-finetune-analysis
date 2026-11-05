---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- text-classification
- sentiment-analysis
- customer-support
- transformers
- generated_from_trainer

model-index:
- name: customer-support-sentiment-classifier
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Customer Support Dataset
      type: custom
    metrics:
    - type: loss
      value: 0.0571
      name: Validation Loss
---

# Customer Support Sentiment Classifier

This model is a fine-tuned version of `distilbert-base-uncased` trained on a custom customer support dataset containing customer feedback, complaints, and support-related messages.

The model classifies customer messages into one of two sentiment categories:

- **Negative (0)**
- **Positive (1)**

## Model Description

- **Base Model:** distilbert-base-uncased
- **Task:** Sentiment Analysis
- **Framework:** Hugging Face Transformers
- **Language:** English
- **Training Samples:** 600
- **Fine-Tuning Method:** Supervised Fine-Tuning

## Intended Use

This model can be used for:

- Customer feedback classification
- Customer review analysis
- Support ticket prioritization
- Sentiment analysis of customer messages
- Customer experience monitoring

## Example

### Negative Example

Input:

```text
The app keeps crashing after login.
```

Output:

```text
Negative
```

### Positive Example

Input:

```text
Thank you for the amazing support team.
```

Output:

```text
Positive
```

## Limitations

- Trained on a relatively small dataset (600 examples).
- Performance may decrease on domains outside customer support.
- Only supports English text.
- Predictions depend on the quality and balance of the training data.

## Training and Evaluation Data

The model was trained on a custom JSONL dataset of customer support messages labeled as either Positive or Negative sentiment.

Dataset split:

- Training Set: 80%
- Test Set: 20%

## Training Procedure

### Hyperparameters

- Learning Rate: 2e-5
- Batch Size: 16
- Epochs: 3
- Weight Decay: 0.01
- Optimizer: AdamW
- Scheduler: Linear

### Training Results

| Epoch | Validation Loss |
|---------|---------|
| 1 | 0.2164 |
| 2 | 0.0743 |
| 3 | 0.0571 |

**Final Validation Loss:** 0.0571

## Framework Versions

- Transformers: 5.10.1
- PyTorch: 2.11.0+cu128
- Datasets: 4.0.0
- Tokenizers: 0.22.2