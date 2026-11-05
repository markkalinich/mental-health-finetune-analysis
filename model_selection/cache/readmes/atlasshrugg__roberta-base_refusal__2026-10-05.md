---
license: mit
base_model: roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: roberta-base_refusal
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/tingan-2017chen-florida-state-university/huggingface/runs/nznyn228)
# roberta-base_refusal

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0104
- Accuracy: 0.9981

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:--------:|
| 0.0002        | 0.2776 | 500  | 0.0159          | 0.9975   |
| 0.0011        | 0.5552 | 1000 | 0.0372          | 0.9931   |
| 0.0376        | 0.8329 | 1500 | 0.0214          | 0.9963   |
| 0.038         | 1.1105 | 2000 | 0.0147          | 0.9981   |
| 0.0465        | 1.3881 | 2500 | 0.0157          | 0.9975   |
| 0.0495        | 1.6657 | 3000 | 0.0096          | 0.9988   |
| 0.0011        | 1.9434 | 3500 | 0.0136          | 0.9981   |
| 0.0004        | 2.2210 | 4000 | 0.0153          | 0.9981   |
| 0.0007        | 2.4986 | 4500 | 0.0123          | 0.9981   |
| 0.0004        | 2.7762 | 5000 | 0.0362          | 0.9956   |
| 0.044         | 3.0539 | 5500 | 0.0176          | 0.9975   |
| 0.0015        | 3.3315 | 6000 | 0.0142          | 0.9975   |
| 0.0004        | 3.6091 | 6500 | 0.0113          | 0.9981   |
| 0.0004        | 3.8867 | 7000 | 0.0227          | 0.9956   |
| 0.0436        | 4.1644 | 7500 | 0.0129          | 0.9969   |
| 0.0085        | 4.4420 | 8000 | 0.0102          | 0.9988   |
| 0.0003        | 4.7196 | 8500 | 0.0102          | 0.9988   |
| 0.0002        | 4.9972 | 9000 | 0.0104          | 0.9981   |


### Framework versions

- Transformers 4.42.3
- Pytorch 2.1.2
- Datasets 2.20.0
- Tokenizers 0.19.1
