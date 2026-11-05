---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- distilbert
- sentiment-analysis
- hotel-reviews
- text-classification
- fine-tuned
- transformers
metrics:
- accuracy
---

# Hotel Sentiment DistilBERT

This model is a fine-tuned version of DistilBERT created to classify
hotel customer reviews as **POSITIVE** or **NEGATIVE**.

## Model Description

The model was developed as a practical Hugging Face fine-tuning project.

It demonstrates how a pretrained Transformer model can be adapted to
a specific text-classification task using a custom dataset.

## Base Model

The base model is:

`distilbert/distilbert-base-uncased`

DistilBERT is a smaller and faster version of BERT.

## Task

The model performs **binary sentiment classification**.

The two classes are:

- `NEGATIVE`
- `POSITIVE`

## Training Dataset

For this educational project, the model was fine-tuned using a small
custom dataset of hotel customer reviews.

Example positive review:

> The room was clean and comfortable.

Label:

`POSITIVE`

Example negative review:

> The room was dirty and the service was terrible.

Label:

`NEGATIVE`

## Intended Use

The model can be used to demonstrate automatic sentiment analysis of
hotel and hospitality customer reviews.

Example applications include:

- Hotel review analysis
- Customer feedback classification
- Hospitality sentiment monitoring
- AI and NLP training demonstrations

## How to Use

After the model files have been uploaded to this repository, the model
can be loaded with Hugging Face Transformers:

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="arlette80-laure/hotel-sentiment-distilbert"
)

result = classifier(
    "The hotel was excellent and the staff were very friendly."
)

print(result)
```

## Labels

| ID | Label |
|---|---|
| 0 | NEGATIVE |
| 1 | POSITIVE |

## Limitations

This model was created for educational purposes using a very small
training dataset.

Therefore:

- It should not be considered production-ready.
- It may perform poorly on complex or ambiguous reviews.
- It may have difficulty with sarcasm.
- It may have difficulty with mixed positive and negative sentiment.
- It was trained primarily using English examples.
- More training data would be required for reliable real-world deployment.

## Future Improvements

Future versions can be improved by:

- Increasing the number of training examples
- Using real hotel customer reviews
- Creating separate training, validation, and test datasets
- Measuring precision, recall and F1-score
- Supporting French and Spanish reviews
- Performing hyperparameter tuning
- Testing the model on unseen real-world data

## Framework

This model was developed using:

- Hugging Face Transformers
- Hugging Face Datasets
- PyTorch
- Hugging Face Trainer

## License

MIT

## Purpose

This repository forms part of a hands-on Hugging Face learning project
demonstrating the complete workflow:

Pretrained Model → Custom Dataset → Tokenization → Fine-tuning →
Evaluation → Model Publishing → Inference