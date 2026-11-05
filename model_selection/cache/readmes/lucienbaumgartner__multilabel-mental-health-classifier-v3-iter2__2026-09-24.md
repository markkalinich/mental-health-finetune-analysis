---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: multilabel-mental-health-classifier-v3-iter2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# multilabel-mental-health-classifier-v3-iter2

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0042
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
| 0.204         | 1.0   | 192  | 0.0932          | 0.9773          | 0.9657       | 0.9714   | 0.9849          | 0.9618       | 0.9732   |
| 0.118         | 2.0   | 384  | 0.0546          | 0.9834          | 0.9865       | 0.9849   | 0.9887          | 0.9865       | 0.9876   |
| 0.0709        | 3.0   | 576  | 0.0329          | 0.9901          | 0.9916       | 0.9908   | 0.9918          | 0.9881       | 0.9900   |
| 0.0415        | 4.0   | 768  | 0.0168          | 0.9964          | 0.9979       | 0.9972   | 0.9966          | 0.9959       | 0.9962   |
| 0.0257        | 5.0   | 960  | 0.0124          | 0.9992          | 0.9980       | 0.9986   | 0.9991          | 0.9966       | 0.9978   |
| 0.0179        | 6.0   | 1152 | 0.0078          | 0.9995          | 0.9994       | 0.9994   | 0.9997          | 0.9991       | 0.9994   |
| 0.0119        | 7.0   | 1344 | 0.0057          | 1.0             | 0.9998       | 0.9999   | 1.0             | 0.9997       | 0.9998   |
| 0.0078        | 8.0   | 1536 | 0.0047          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0063        | 9.0   | 1728 | 0.0045          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0059        | 10.0  | 1920 | 0.0042          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.4.1
- Tokenizers 0.22.1
