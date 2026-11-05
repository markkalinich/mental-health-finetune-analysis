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
- name: AnnoMI-full_speaker_role_id-bert-base-uncased-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AnnoMI-full_speaker_role_id-bert-base-uncased-v1

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3878
- Accuracy: 0.8819
- Precision Macro: 0.8819
- Recall Macro: 0.8819
- F1 Macro: 0.8819
- Precision Weighted: 0.8820
- Recall Weighted: 0.8819
- F1 Weighted: 0.8819
- Report:               precision    recall  f1-score   support

           0       0.89      0.88      0.88       683
           1       0.88      0.89      0.88       672

    accuracy                           0.88      1355
   macro avg       0.88      0.88      0.88      1355
weighted avg       0.88      0.88      0.88      1355


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

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | Precision Macro | Recall Macro | F1 Macro | Precision Weighted | Recall Weighted | F1 Weighted | Report                                                                                                                                                                                                                                                                                                                                 |
|:-------------:|:------:|:----:|:---------------:|:--------:|:---------------:|:------------:|:--------:|:------------------:|:---------------:|:-----------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| 0.2898        | 1.4753 | 500  | 0.2720          | 0.8871   | 0.8874          | 0.8872       | 0.8871   | 0.8876             | 0.8871          | 0.8871      |               precision    recall  f1-score   support

           0       0.90      0.87      0.89       683
           1       0.87      0.90      0.89       672

    accuracy                           0.89      1355
   macro avg       0.89      0.89      0.89      1355
weighted avg       0.89      0.89      0.89      1355
 |
| 0.217         | 2.9506 | 1000 | 0.2941          | 0.8819   | 0.8824          | 0.8821       | 0.8819   | 0.8825             | 0.8819          | 0.8819      |               precision    recall  f1-score   support

           0       0.90      0.86      0.88       683
           1       0.87      0.90      0.88       672

    accuracy                           0.88      1355
   macro avg       0.88      0.88      0.88      1355
weighted avg       0.88      0.88      0.88      1355
 |
| 0.189         | 4.4251 | 1500 | 0.3902          | 0.8797   | 0.8797          | 0.8798       | 0.8797   | 0.8798             | 0.8797          | 0.8797      |               precision    recall  f1-score   support

           0       0.89      0.87      0.88       683
           1       0.87      0.89      0.88       672

    accuracy                           0.88      1355
   macro avg       0.88      0.88      0.88      1355
weighted avg       0.88      0.88      0.88      1355
 |
| 0.167         | 5.9004 | 2000 | 0.3878          | 0.8819   | 0.8819          | 0.8819       | 0.8819   | 0.8820             | 0.8819          | 0.8819      |               precision    recall  f1-score   support

           0       0.89      0.88      0.88       683
           1       0.88      0.89      0.88       672

    accuracy                           0.88      1355
   macro avg       0.88      0.88      0.88      1355
weighted avg       0.88      0.88      0.88      1355
 |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2
