---
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
model-index:
- name: CRAFT_ClinicalBERT_NER
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CRAFT_ClinicalBERT_NER

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1733
- Seqeval classification report:               precision    recall  f1-score   support

       CHEBI       0.68      0.66      0.67      1365
          CL       0.55      0.50      0.52       284
         GGP       0.87      0.81      0.84      4632
          GO       0.66      0.65      0.65      8852
          SO       0.68      0.50      0.58       616
       Taxon       0.81      0.73      0.77       986

   micro avg       0.72      0.69      0.71     16735
   macro avg       0.71      0.64      0.67     16735
weighted avg       0.73      0.69      0.71     16735


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

| Training Loss | Epoch | Step | Validation Loss | Seqeval classification report                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| No log        | 1.0   | 347  | 0.1894          |               precision    recall  f1-score   support

       CHEBI       0.64      0.56      0.60      1365
          CL       0.53      0.35      0.42       284
         GGP       0.84      0.77      0.81      4632
          GO       0.60      0.61      0.60      8852
          SO       0.53      0.46      0.49       616
       Taxon       0.78      0.66      0.71       986

   micro avg       0.68      0.64      0.66     16735
   macro avg       0.65      0.57      0.61     16735
weighted avg       0.68      0.64      0.66     16735
 |
| 0.2231        | 2.0   | 695  | 0.1740          |               precision    recall  f1-score   support

       CHEBI       0.69      0.63      0.66      1365
          CL       0.56      0.44      0.49       284
         GGP       0.83      0.79      0.81      4632
          GO       0.65      0.65      0.65      8852
          SO       0.68      0.47      0.55       616
       Taxon       0.81      0.72      0.76       986

   micro avg       0.71      0.68      0.69     16735
   macro avg       0.70      0.62      0.65     16735
weighted avg       0.71      0.68      0.69     16735
 |
| 0.0813        | 3.0   | 1041 | 0.1733          |               precision    recall  f1-score   support

       CHEBI       0.68      0.66      0.67      1365
          CL       0.55      0.50      0.52       284
         GGP       0.87      0.81      0.84      4632
          GO       0.66      0.65      0.65      8852
          SO       0.68      0.50      0.58       616
       Taxon       0.81      0.73      0.77       986

   micro avg       0.72      0.69      0.71     16735
   macro avg       0.71      0.64      0.67     16735
weighted avg       0.73      0.69      0.71     16735
 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
