---
library_name: transformers
license: apache-2.0
language:
- en
pipeline_tag: text-classification
datasets:
- dair-ai/emotion
metrics:
- accuracy
- f1
tags:
- text-classification
- emotion-classification
- distilbert
- trained-from-scratch
---

# my-own-emotion-classifier

A small transformer model that reads an English sentence and predicts which emotion it expresses: **sadness, joy, love, anger, fear, or surprise**.

This model was **trained from scratch**: it starts with random weights and learns only from the training data. It is not fine-tuned from a pre-trained model.

## Model Details

### Model Description

- **Developed by:** Mohak512
- **Model type:** DistilBERT-style transformer encoder for sequence classification (4 layers, hidden size 256, 4 attention heads, about 11 million parameters)
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model:** None. Weights were randomly initialised and trained from scratch. Only the tokenizer (vocabulary) is reused from `distilbert-base-uncased`.

### Model Sources

- **Repository:** https://huggingface.co/Mohak512/my-own-emotion-classifier
- **Paper:** None
- **Demo:** None

## Uses

### Direct Use

Classify short English texts (such as tweets or messages) into one of six emotions.

### Downstream Use

Can be used as a starting point for learning projects, demos, or simple emotion tagging in a larger text pipeline.

### Out-of-Scope Use

- Medical, psychological, or mental-health assessment of a person.
- Decisions that affect people (hiring, moderation, credit, etc.) without human review.
- Languages other than English, or long documents (inputs are cut at 128 tokens).

## Bias, Risks, and Limitations

- Trained on Twitter-style English text, so it may work poorly on formal writing, other languages, slang from other regions, or sarcasm.
- The dataset labels were assigned automatically from hashtags, so some labels are noisy, and the model can inherit those errors.
- The model is small and was trained from scratch, so it is less accurate than large pre-trained models.
- It predicts only one emotion per text, and some texts express several emotions or none of these six.

### Recommendations

Use the predictions as a rough signal, not as ground truth, and test the model on your own data before relying on it.

## How to Get Started with the Model

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Mohak512/my-own-emotion-classifier")

print(clf("I can't believe I finally got the job, I'm over the moon!"))
print(clf("You lied to me again and I am furious."))
```

## Training Details

### Training Data

[dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion): English Twitter messages labelled with six emotions (sadness, joy, love, anger, fear, surprise). The full training split was used, with a validation split for model selection and a held-out test split for the final evaluation.

### Training Procedure

#### Preprocessing

Text was tokenized with the `distilbert-base-uncased` tokenizer (lower-cased, WordPiece), truncated to 128 tokens, and padded dynamically per batch.

#### Training Hyperparameters

- **Training regime:** fp16 mixed precision
- **Epochs:** 15
- **Batch size:** 32
- **Learning rate:** 1e-4
- **Weight decay:** 0.01
- **Warmup ratio:** 0.1
- **Optimizer:** AdamW (Hugging Face Trainer default)
- **Model selection:** best checkpoint by macro F1 on the validation set
- **Seed:** 42

#### Speeds, Sizes, Times

- Training time: [fill in, e.g. about X minutes]
- Model size: about 11 million parameters

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

Test split of [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion).

#### Factors

Results are reported overall and per emotion class.

#### Metrics

- **Accuracy:** share of test texts classified correctly.
- **Macro F1:** the average F1 score across the six classes, which treats small classes (like surprise) fairly.

### Results

| Metric | Score |
|---|---|
| Test accuracy | [fill in from section 9 of the notebook] |
| Test macro F1 | [fill in from section 9 of the notebook] |

#### Summary

[Write one sentence, e.g. "The model performs best on joy and sadness and is weakest on surprise and love."]

## Environmental Impact

- **Hardware Type:** NVIDIA T4 GPU (free Google Colab)
- **Hours used:** [fill in, likely under 1 hour]
- **Cloud Provider:** Google Colab
- **Compute Region:** [fill in if known]
- **Carbon Emitted:** Not measured (small model, short training run)

## Technical Specifications

### Model Architecture and Objective

DistilBERT-style encoder (`DistilBertForSequenceClassification`) with 4 layers, 256 hidden dimensions, 1024 feed-forward dimensions and 4 attention heads, plus a classification head with 6 outputs. Trained with cross-entropy loss.

### Compute Infrastructure

#### Hardware

Google Colab, single NVIDIA T4 GPU.

#### Software

Python, PyTorch, Hugging Face Transformers, Datasets, scikit-learn.

## Model Card Authors

Mohak512

## Model Card Contact

[Add your email or Hugging Face profile link, or delete this line]