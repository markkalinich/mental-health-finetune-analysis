---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-large
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: deberta-pii-masking-augmented-test2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-pii-masking-augmented-test2

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0248
- Precision: 0.9565
- Recall: 0.9663
- F1: 0.9613
- Accuracy: 0.9919

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.5574        | 0.16  | 1000 | 0.0750          | 0.8633    | 0.9081 | 0.8851 | 0.9774   |
| 0.0572        | 0.32  | 2000 | 0.0455          | 0.9151    | 0.9290 | 0.9220 | 0.9857   |
| 0.0401        | 0.48  | 3000 | 0.0395          | 0.9294    | 0.9452 | 0.9372 | 0.9873   |
| 0.0319        | 0.64  | 4000 | 0.0301          | 0.9443    | 0.9548 | 0.9496 | 0.9902   |
| 0.0277        | 0.8   | 5000 | 0.0264          | 0.9503    | 0.9618 | 0.9560 | 0.9912   |
| 0.0231        | 0.96  | 6000 | 0.0249          | 0.9538    | 0.9652 | 0.9595 | 0.9920   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Datasets 3.1.0
- Tokenizers 0.19.1
