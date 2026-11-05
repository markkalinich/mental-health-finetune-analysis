---
language:
- multilingual
license: apache-2.0
base_model: xlm-roberta-base
tags:
- sentiment-analysis
- text-classification
- multilingual
- xlm-roberta
metrics:
- f1
---

# cmpe346-assignment02-sentiment

This model was fine-tuned for CMPE 346 Assignment 02. The task is multilingual binary sentiment classification, where each input text is classified as either negative or positive.

## Model description

I used `xlm-roberta-base` as the base model because it is trained on many languages and fits the multilingual structure of the dataset. I fine-tuned it with a sequence classification head for two labels:

- `LABEL_0`: negative
- `LABEL_1`: positive

## Intended uses & limitations

This model is intended for classifying short or medium length multilingual texts as positive or negative. It can be used for sentiment analysis experiments and assignment evaluation.

Since it was trained only on the provided assignment dataset, it may not perform equally well on every domain or language. Very long texts are truncated during preprocessing, so some information may be lost for longer inputs.

## Training and evaluation data

The model was trained on the training set provided for the assignment and evaluated on the provided validation set. The dataset contains multilingual text samples with binary sentiment labels.

## Training procedure

The model was fine-tuned using Hugging Face Transformers on an A100 GPU in Google Colab.

Main training settings:

- Base model: `xlm-roberta-base`
- Maximum sequence length: 256
- Number of epochs: 2
- Learning rate: 2e-5
- Training batch size: 32
- Evaluation batch size: 64
- Seed: 42

## Results

The validation result from the assignment evaluation script was:

- F1 score: 0.9176

The Trainer evaluation result was approximately:

- Validation loss: 0.2395
- F1 score: 0.9161
