---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: multilabel-mental-health-classifier-v3-iter5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# multilabel-mental-health-classifier-v3-iter5

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0005
- Precision Macro: 1.0
- Recall Macro: 1.0
- F1 Macro: 1.0
- Precision Micro: 1.0
- Recall Micro: 1.0
- F1 Micro: 1.0

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
- seed: 764
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision Macro | Recall Macro | F1 Macro | Precision Micro | Recall Micro | F1 Micro |
|:-------------:|:-----:|:----:|:---------------:|:---------------:|:------------:|:--------:|:---------------:|:------------:|:--------:|
| 0.2023        | 1.0   | 220  | 0.0706          | 0.9857          | 0.9874       | 0.9865   | 0.9881          | 0.9911       | 0.9896   |
| 0.0772        | 2.0   | 440  | 0.0181          | 0.9922          | 0.9963       | 0.9942   | 0.9938          | 0.9973       | 0.9955   |
| 0.0214        | 3.0   | 660  | 0.0099          | 0.9979          | 0.9983       | 0.9981   | 0.9981          | 0.9995       | 0.9988   |
| 0.0161        | 4.0   | 880  | 0.0025          | 0.9981          | 0.9993       | 0.9987   | 0.9992          | 0.9995       | 0.9993   |
| 0.0034        | 5.0   | 1100 | 0.0013          | 1.0             | 0.9999       | 0.9999   | 1.0             | 0.9997       | 0.9999   |
| 0.0024        | 6.0   | 1320 | 0.0006          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0012        | 7.0   | 1540 | 0.0006          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0009        | 8.0   | 1760 | 0.0005          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0007        | 9.0   | 1980 | 0.0005          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0006        | 10.0  | 2200 | 0.0005          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.4.1
- Tokenizers 0.22.1
