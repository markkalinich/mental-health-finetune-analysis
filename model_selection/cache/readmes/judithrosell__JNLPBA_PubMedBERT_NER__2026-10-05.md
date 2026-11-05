---
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
model-index:
- name: JNLPBA_PubMedBERT_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# JNLPBA_PubMedBERT_NER

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1450
- Seqeval classification report:               precision    recall  f1-score   support

         DNA       0.75      0.83      0.79       955
         RNA       0.80      0.83      0.82      1144
   cell_line       0.76      0.79      0.78      5330
   cell_type       0.86      0.91      0.88      2518
     protein       0.87      0.85      0.86       926

   micro avg       0.80      0.83      0.81     10873
   macro avg       0.81      0.84      0.82     10873
weighted avg       0.80      0.83      0.81     10873


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

| Training Loss | Epoch | Step | Validation Loss | Seqeval classification report                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 0.2726        | 1.0   | 582  | 0.1526          |               precision    recall  f1-score   support

         DNA       0.73      0.82      0.77       955
         RNA       0.79      0.82      0.81      1144
   cell_line       0.75      0.78      0.76      5330
   cell_type       0.86      0.86      0.86      2518
     protein       0.86      0.84      0.85       926

   micro avg       0.79      0.81      0.80     10873
   macro avg       0.80      0.82      0.81     10873
weighted avg       0.79      0.81      0.80     10873
 |
| 0.145         | 2.0   | 1164 | 0.1473          |               precision    recall  f1-score   support

         DNA       0.73      0.82      0.77       955
         RNA       0.85      0.78      0.81      1144
   cell_line       0.77      0.78      0.78      5330
   cell_type       0.85      0.92      0.88      2518
     protein       0.88      0.83      0.85       926

   micro avg       0.80      0.82      0.81     10873
   macro avg       0.81      0.83      0.82     10873
weighted avg       0.80      0.82      0.81     10873
 |
| 0.1276        | 3.0   | 1746 | 0.1450          |               precision    recall  f1-score   support

         DNA       0.75      0.83      0.79       955
         RNA       0.80      0.83      0.82      1144
   cell_line       0.76      0.79      0.78      5330
   cell_type       0.86      0.91      0.88      2518
     protein       0.87      0.85      0.86       926

   micro avg       0.80      0.83      0.81     10873
   macro avg       0.81      0.84      0.82     10873
weighted avg       0.80      0.83      0.81     10873
 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
