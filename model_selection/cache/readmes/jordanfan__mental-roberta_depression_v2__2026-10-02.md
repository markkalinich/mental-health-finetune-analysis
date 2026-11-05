---
library_name: transformers
license: cc-by-nc-4.0
base_model: mental/mental-roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: mental-roberta_depression_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental-roberta_depression_v2

This model is a fine-tuned version of [mental/mental-roberta-base](https://huggingface.co/mental/mental-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5003
- Accuracy: 0.7974
- Precision: 0.7981
- Recall: 0.7974
- F1: 0.7972

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_8BIT with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.5859        | 1.0   | 969  | 0.5015          | 0.7693   | 0.7913    | 0.7693 | 0.7608 |
| 0.416         | 2.0   | 1938 | 0.4553          | 0.7984   | 0.8032    | 0.7984 | 0.7980 |
| 0.3386        | 3.0   | 2907 | 0.5003          | 0.7974   | 0.7981    | 0.7974 | 0.7972 |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 3.3.2
- Tokenizers 0.21.0
