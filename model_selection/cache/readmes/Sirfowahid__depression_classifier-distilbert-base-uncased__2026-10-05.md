---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: depression_classifier-distilbert-base-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# depression_classifier-distilbert-base-uncased

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000
- Accuracy: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.0625        | 1.0   | 130  | 0.0002          | 1.0      |
| 0.0002        | 2.0   | 260  | 0.0001          | 1.0      |
| 0.0001        | 3.0   | 390  | 0.0000          | 1.0      |
| 0.0           | 4.0   | 520  | 0.0000          | 1.0      |
| 0.0           | 5.0   | 650  | 0.0000          | 1.0      |
| 0.0           | 6.0   | 780  | 0.0000          | 1.0      |
| 0.0           | 7.0   | 910  | 0.0000          | 1.0      |
| 0.0           | 8.0   | 1040 | 0.0000          | 1.0      |
| 0.0           | 9.0   | 1170 | 0.0000          | 1.0      |
| 0.0           | 10.0  | 1300 | 0.0000          | 1.0      |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
