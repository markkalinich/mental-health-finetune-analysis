---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: pii_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0326
- Accuracy: 0.9950
- F1: 0.9873

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 0.0207        | 1.0   | 1846  | 0.0205          | 0.9938   | 0.9813 |
| 0.01          | 2.0   | 3692  | 0.0222          | 0.9938   | 0.9825 |
| 0.0053        | 3.0   | 5538  | 0.0231          | 0.9946   | 0.9851 |
| 0.0041        | 4.0   | 7384  | 0.0258          | 0.9945   | 0.9852 |
| 0.0026        | 5.0   | 9230  | 0.0262          | 0.9946   | 0.9857 |
| 0.0016        | 6.0   | 11076 | 0.0305          | 0.9946   | 0.9857 |
| 0.0011        | 7.0   | 12922 | 0.0268          | 0.9949   | 0.9866 |
| 0.0009        | 8.0   | 14768 | 0.0299          | 0.9948   | 0.9867 |
| 0.0004        | 9.0   | 16614 | 0.0307          | 0.9949   | 0.9872 |
| 0.0001        | 10.0  | 18460 | 0.0326          | 0.9950   | 0.9873 |


### Framework versions

- Transformers 4.55.2
- Pytorch 2.8.0+cu126
- Datasets 3.6.0
- Tokenizers 0.21.4
