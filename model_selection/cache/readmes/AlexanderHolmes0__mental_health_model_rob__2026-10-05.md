---
license: mit
base_model: FacebookAI/roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mental_health_model_rob
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental_health_model_rob

This model is a fine-tuned version of [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5858
- Accuracy: 0.7585

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Accuracy | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:---------------:|
| No log        | 1.0   | 270  | 0.7201   | 0.6445          |
| 0.7167        | 2.0   | 540  | 0.7585   | 0.5858          |
| 0.7167        | 3.0   | 810  | 0.7726   | 0.6201          |
| 0.3475        | 4.0   | 1080 | 0.7829   | 0.6671          |
| 0.3475        | 5.0   | 1350 | 0.7226   | 0.7786          |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
