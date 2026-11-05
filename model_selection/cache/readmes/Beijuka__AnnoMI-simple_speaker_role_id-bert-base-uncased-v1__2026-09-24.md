---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- speaker-role-identification
- dialogue-analysis
- psychotherapy
- conversation-analysis
- bert
- AnnoMI
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: AnnoMI-simple_speaker_role_id-bert-base-uncased-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AnnoMI-simple_speaker_role_id-bert-base-uncased-v1

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7799
- Accuracy: 0.8443
- Precision Macro: 0.8448
- Recall Macro: 0.8442
- F1 Macro: 0.8442
- Precision Weighted: 0.8447
- Recall Weighted: 0.8443
- F1 Weighted: 0.8443
- Report:               precision    recall  f1-score   support

           0       0.83      0.86      0.85       488
           1       0.86      0.83      0.84       482

    accuracy                           0.84       970
   macro avg       0.84      0.84      0.84       970
weighted avg       0.84      0.84      0.84       970


## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Accuracy | Precision Macro | Recall Macro | F1 Macro | Precision Weighted | Recall Weighted | F1 Weighted | Report                                                                                                                                                                                                                                                                                                                                 |
|:-------------:|:-------:|:----:|:---------------:|:--------:|:---------------:|:------------:|:--------:|:------------------:|:---------------:|:-----------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 0.3142        | 2.0577  | 500  | 0.4281          | 0.8423   | 0.8438          | 0.8425       | 0.8421   | 0.8439             | 0.8423          | 0.8421      |               precision    recall  f1-score   support

           0       0.87      0.81      0.84       488
           1       0.82      0.88      0.85       482

    accuracy                           0.84       970
   macro avg       0.84      0.84      0.84       970
weighted avg       0.84      0.84      0.84       970
 |
| 0.1986        | 4.1155  | 1000 | 0.5841          | 0.8144   | 0.8250          | 0.8150       | 0.8131   | 0.8253             | 0.8144          | 0.8130      |               precision    recall  f1-score   support

           0       0.89      0.73      0.80       488
           1       0.76      0.90      0.83       482

    accuracy                           0.81       970
   macro avg       0.82      0.81      0.81       970
weighted avg       0.83      0.81      0.81       970
 |
| 0.177         | 6.1732  | 1500 | 0.6025          | 0.8392   | 0.8392          | 0.8392       | 0.8392   | 0.8392             | 0.8392          | 0.8392      |               precision    recall  f1-score   support

           0       0.84      0.84      0.84       488
           1       0.84      0.84      0.84       482

    accuracy                           0.84       970
   macro avg       0.84      0.84      0.84       970
weighted avg       0.84      0.84      0.84       970
 |
| 0.1595        | 8.2309  | 2000 | 0.5967          | 0.8495   | 0.8495          | 0.8495       | 0.8495   | 0.8495             | 0.8495          | 0.8495      |               precision    recall  f1-score   support

           0       0.85      0.85      0.85       488
           1       0.85      0.84      0.85       482

    accuracy                           0.85       970
   macro avg       0.85      0.85      0.85       970
weighted avg       0.85      0.85      0.85       970
 |
| 0.1593        | 10.2887 | 2500 | 0.6821          | 0.8433   | 0.8433          | 0.8433       | 0.8433   | 0.8433             | 0.8433          | 0.8433      |               precision    recall  f1-score   support

           0       0.84      0.85      0.84       488
           1       0.85      0.84      0.84       482

    accuracy                           0.84       970
   macro avg       0.84      0.84      0.84       970
weighted avg       0.84      0.84      0.84       970
 |
| 0.148         | 12.3464 | 3000 | 0.6469          | 0.8423   | 0.8456          | 0.8420       | 0.8418   | 0.8454             | 0.8423          | 0.8418      |               precision    recall  f1-score   support

           0       0.81      0.89      0.85       488
           1       0.88      0.79      0.83       482

    accuracy                           0.84       970
   macro avg       0.85      0.84      0.84       970
weighted avg       0.85      0.84      0.84       970
 |
| 0.1446        | 14.4041 | 3500 | 0.7799          | 0.8443   | 0.8448          | 0.8442       | 0.8442   | 0.8447             | 0.8443          | 0.8443      |               precision    recall  f1-score   support

           0       0.83      0.86      0.85       488
           1       0.86      0.83      0.84       482

    accuracy                           0.84       970
   macro avg       0.84      0.84      0.84       970
weighted avg       0.84      0.84      0.84       970
 |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2
