---
library_name: transformers
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-pubmedd
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-pubmedd

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5626
- Rouge1: 37.72
- Rouge2: 14.01
- Rougel: 22.84
- Rougelsum: 33.26

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 1000

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:------:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.1141        | 0.2668 | 200  | 2.7332          | 36.95  | 13.98  | 22.78  | 32.78     |
| 2.9621        | 0.5337 | 400  | 2.6831          | 38.12  | 14.37  | 22.8   | 33.44     |
| 2.9085        | 0.8005 | 600  | 2.6033          | 37.28  | 13.84  | 22.44  | 32.9      |
| 2.7868        | 1.0674 | 800  | 2.5722          | 37.18  | 13.95  | 22.58  | 32.94     |
| 2.8079        | 1.3342 | 1000 | 2.5626          | 37.72  | 14.01  | 22.84  | 33.26     |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 3.2.0
- Tokenizers 0.19.1
