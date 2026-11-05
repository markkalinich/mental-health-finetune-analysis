---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: multilabel-mental-health-classifier-v3-iter3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# multilabel-mental-health-classifier-v3-iter3

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0013
- Precision Macro: 1.0
- Recall Macro: 0.9998
- F1 Macro: 0.9999
- Precision Micro: 1.0
- Recall Micro: 0.9997
- F1 Micro: 0.9999

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
| 0.1681        | 1.0   | 201  | 0.0308          | 0.9702          | 0.9923       | 0.9809   | 0.9849          | 0.9911       | 0.9880   |
| 0.0523        | 2.0   | 402  | 0.0158          | 0.9916          | 0.9956       | 0.9935   | 0.9970          | 0.9946       | 0.9958   |
| 0.0285        | 3.0   | 603  | 0.0121          | 0.9892          | 0.9969       | 0.9929   | 0.9929          | 0.9976       | 0.9953   |
| 0.01          | 4.0   | 804  | 0.0034          | 0.9992          | 0.9998       | 0.9995   | 0.9994          | 0.9997       | 0.9996   |
| 0.0074        | 5.0   | 1005 | 0.0026          | 1.0             | 0.9999       | 0.9999   | 1.0             | 0.9997       | 0.9999   |
| 0.0045        | 6.0   | 1206 | 0.0021          | 1.0             | 0.9996       | 0.9998   | 1.0             | 0.9994       | 0.9997   |
| 0.0031        | 7.0   | 1407 | 0.0015          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0022        | 8.0   | 1608 | 0.0013          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0018        | 9.0   | 1809 | 0.0014          | 1.0             | 0.9998       | 0.9999   | 1.0             | 0.9997       | 0.9999   |
| 0.0017        | 10.0  | 2010 | 0.0013          | 1.0             | 0.9998       | 0.9999   | 1.0             | 0.9997       | 0.9999   |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.4.1
- Tokenizers 0.22.1
