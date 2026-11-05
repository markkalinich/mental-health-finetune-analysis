---
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
model-index:
- name: BC5CDR_PubMedBERT_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BC5CDR_PubMedBERT_NER

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0783
- Seqeval classification report:               precision    recall  f1-score   support

    Chemical       0.99      0.98      0.98    103336
     Disease       0.76      0.86      0.81      3447

   micro avg       0.98      0.98      0.98    106783
   macro avg       0.87      0.92      0.89    106783
weighted avg       0.98      0.98      0.98    106783


## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Seqeval classification report                                                                                                                                                                                                                                                                                                          |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| No log        | 1.0   | 143  | 0.0952          |               precision    recall  f1-score   support

    Chemical       0.99      0.97      0.98    103336
     Disease       0.68      0.88      0.76      3447

   micro avg       0.97      0.97      0.97    106783
   macro avg       0.83      0.92      0.87    106783
weighted avg       0.98      0.97      0.97    106783
 |
| No log        | 2.0   | 286  | 0.0804          |               precision    recall  f1-score   support

    Chemical       0.99      0.98      0.98    103336
     Disease       0.75      0.86      0.80      3447

   micro avg       0.98      0.97      0.97    106783
   macro avg       0.87      0.92      0.89    106783
weighted avg       0.98      0.97      0.98    106783
 |
| No log        | 3.0   | 429  | 0.0783          |               precision    recall  f1-score   support

    Chemical       0.99      0.98      0.98    103336
     Disease       0.76      0.86      0.81      3447

   micro avg       0.98      0.98      0.98    106783
   macro avg       0.87      0.92      0.89    106783
weighted avg       0.98      0.98      0.98    106783
 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
