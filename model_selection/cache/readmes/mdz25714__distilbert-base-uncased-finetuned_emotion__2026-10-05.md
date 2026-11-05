---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
- transformers
- distilbert
- text-classification
- emotion-classification
- fine-tuning
- pytorch
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncased-finetuned_emotion
  results: []
datasets:
- AiLab-IMCS-UL/twitter_emotions-en
---

# distilbert-base-uncased-finetuned_emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the Twitter Emotion Dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1325
- Accuracy: 0.9395
- F1: 0.9393

## Model description

This model is a fine-tuned version of DistilBERT for six-class emotion
classification.

Given an English text input, the model predicts one of the following emotions:
sadness, joy, love, anger, fear, or surprise.

The model was fine-tuned using Hugging Face Transformers and the Trainer API.

## Intended uses & limitations

### Intended uses

This model can be used for:
- Emotion classification in English text
- Sentiment and emotion analysis
- NLP experimentation and educational projects
- Building emotion-aware NLP applications

### Limitations

The model was trained on a specific emotion dataset and may not generalize
perfectly to all domains, writing styles, or languages.

Some emotions such as love and joy, or fear and sadness, can be semantically
overlapping, which may result in ambiguous predictions.

### Labels

| ID | Emotion |
|---:|---------|
| 0 | sadness |
| 1 | joy |
| 2 | love |
| 3 | anger |
| 4 | fear |
| 5 | surprise |

## Training and evaluation data

The model was fine-tuned on the **Twitter Emotion Dataset**, downloaded from Kaggle.

The dataset contains 416,809 English text samples annotated with six emotion classes:

* sadness
* joy
* love
* anger
* fear
* surprise

The dataset was split into training, validation, and test sets for model training and evaluation.

The dataset is also available on Hugging Face as **AiLab-IMCS-UL/twitter_emotions-en**.


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2

## Results

The fine-tuned model achieved:

- Accuracy: 93.95%
- Weighted F1: 93.93%
- Validation Loss: 0.1325

The model was trained for 2 epochs with a learning rate of 1e-5 and
a batch size of 64.

## Error analysis

Analysis of high-loss examples showed that the most challenging cases were
semantically similar emotions, particularly:

- Love vs. Joy
- Fear vs. Sadness

Some errors also appeared to be caused by ambiguous wording and strong
emotion-related keywords that can occur across multiple emotion classes.

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.1274        | 1.0   | 313  | 0.1330          | 0.9385   | 0.9385 |
| 0.1102        | 2.0   | 626  | 0.1325          | 0.9395   | 0.9393 |


### Framework versions

- Transformers 5.16.1
- Pytorch 2.11.0+cu128
- Datasets 4.8.5
- Tokenizers 0.23.1