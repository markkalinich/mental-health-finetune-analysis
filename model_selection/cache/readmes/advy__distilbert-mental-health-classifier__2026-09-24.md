---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: distilbert-mental-health-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-mental-health-classifier

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0007

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
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.6958        | 0.5   | 10   | 0.4475          |
| 0.4296        | 1.0   | 20   | 0.2968          |
| 0.2364        | 1.5   | 30   | 0.1774          |
| 0.1452        | 2.0   | 40   | 0.0756          |
| 0.0155        | 2.5   | 50   | 0.0066          |
| 0.0058        | 3.0   | 60   | 0.0030          |
| 0.0032        | 3.5   | 70   | 0.0021          |
| 0.0025        | 4.0   | 80   | 0.0016          |
| 0.0021        | 4.5   | 90   | 0.0013          |
| 0.0016        | 5.0   | 100  | 0.0012          |
| 0.0015        | 5.5   | 110  | 0.0010          |
| 0.0013        | 6.0   | 120  | 0.0010          |
| 0.0012        | 6.5   | 130  | 0.0009          |
| 0.0011        | 7.0   | 140  | 0.0008          |
| 0.001         | 7.5   | 150  | 0.0008          |
| 0.001         | 8.0   | 160  | 0.0007          |
| 0.0011        | 8.5   | 170  | 0.0007          |
| 0.0009        | 9.0   | 180  | 0.0007          |
| 0.001         | 9.5   | 190  | 0.0007          |
| 0.0009        | 10.0  | 200  | 0.0007          |


### Framework versions

- Transformers 4.52.4
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
