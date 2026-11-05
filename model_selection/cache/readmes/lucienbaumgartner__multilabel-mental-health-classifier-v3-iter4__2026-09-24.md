---
library_name: transformers
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: multilabel-mental-health-classifier-v3-iter4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# multilabel-mental-health-classifier-v3-iter4

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0007
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
| 0.1657        | 1.0   | 211  | 0.0582          | 0.9920          | 0.9877       | 0.9898   | 0.9932          | 0.9881       | 0.9906   |
| 0.0569        | 2.0   | 422  | 0.0239          | 0.9825          | 0.9940       | 0.9880   | 0.9904          | 0.9960       | 0.9932   |
| 0.0257        | 3.0   | 633  | 0.0040          | 0.9954          | 0.9995       | 0.9974   | 0.9977          | 0.9991       | 0.9984   |
| 0.0075        | 4.0   | 844  | 0.0031          | 0.9969          | 0.9995       | 0.9982   | 0.9986          | 0.9991       | 0.9989   |
| 0.0059        | 5.0   | 1055 | 0.0021          | 0.9998          | 0.9995       | 0.9996   | 0.9997          | 0.9991       | 0.9994   |
| 0.003         | 6.0   | 1266 | 0.0009          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0013        | 7.0   | 1477 | 0.0008          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.0011        | 8.0   | 1688 | 0.0007          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.001         | 9.0   | 1899 | 0.0007          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |
| 0.001         | 10.0  | 2110 | 0.0007          | 1.0             | 1.0          | 1.0      | 1.0             | 1.0          | 1.0      |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.4.1
- Tokenizers 0.22.1
