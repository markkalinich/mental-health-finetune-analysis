---
library_name: transformers
tags:
- sentiment-analysis
- distilbert
- classification
- imdb
license: apache-2.0
language:
- en
---

# Custom Sentiment Analysis Model

This model is a fine-tuned version of `distilbert-base-uncased` on an IMDB dataset subset for sentiment analysis.

## Model Details

### Model Description

This model classifies text into two categories: POSITIVE or NEGATIVE. It was developed as part of a custom sentiment analysis project using the Hugging Face `transformers` and `datasets` libraries.

- **Developed by:** Christian DJOMATIN AHO (DJO5555)
- **Model type:** Transformer-based Sequence Classification
- **Language(s) (NLP):** English
- **License:** Apache-2.0
- **Finetuned from model:** distilbert-base-uncased

### Model Sources

- **Repository:** https://huggingface.co/DJO5555/custom-sentiment-analysis

## Uses

### Direct Use

The model can be used directly for sentiment analysis on English text, particularly movie reviews or similar content.

### Out-of-Scope Use

The model is not intended for use in production environments requiring high precision, as it was trained on a very small subset of data for demonstration purposes.

## Bias, Risks, and Limitations

This model was trained on a small subset (100 samples) of the IMDB dataset, which means its generalization capabilities are limited. It may exhibit biases present in the original IMDB dataset.

### Recommendations

Users should be aware that this is a demonstration model. For robust sentiment analysis, a model trained on a larger and more diverse dataset is recommended.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="DJO5555/custom-sentiment-analysis")

results = classifier(["I love this AI assistant, it's so helpful!", "This is the worst experience ever."])
for result in results:
    print(f"Label: {result['label']}, Score: {result['score']:.4f}")
```

## Training Details

### Training Data

The model was trained on a subset of the [IMDB dataset](https://huggingface.co/datasets/imdb).
- **Training samples:** 100
- **Evaluation samples:** 50

### Training Procedure

#### Training Hyperparameters

- **Training regime:** fp32
- **Epochs:** 1
- **Batch size:** 8
- **Warmup steps:** 10
- **Weight decay:** 0.01

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The evaluation was performed on 50 samples from the IMDB test set.

#### Metrics

The primary metric used for evaluation during training was the training/validation loss.

### Results

The model displays basic sentiment recognition capabilities on standard movie review sentences.

## Technical Specifications

### Model Architecture and Objective

- **Architecture:** DistilBertForSequenceClassification
- **Objective:** Single-label Classification (Positive/Negative)

### Compute Infrastructure

#### Software
- **Transformers version:** 4.57.3
- **PyTorch / Hugging Face Trainer API**

## Model Card Authors

Christian DJOMATIN AHO

## Model Card Contact

DJO5555 (Hugging Face Hub)