---
license: apache-2.0
base_model: google/flan-t5-small
tags:
- text2textgeneration
- generated_from_trainer
metrics:
- rouge
model-index:
- name: flan-t5-small-finetune-medicine-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-small-finetune-medicine-v3

This model is a fine-tuned version of [google/flan-t5-small](https://huggingface.co/google/flan-t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8757
- Rouge1: 15.991
- Rouge2: 5.2469
- Rougel: 14.6278
- Rougelsum: 14.7076

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| No log        | 1.0   | 5    | 2.9996          | 12.4808 | 4.9536 | 12.3712 | 12.2123   |
| No log        | 2.0   | 10   | 2.9550          | 13.6471 | 4.9536 | 13.5051 | 13.5488   |
| No log        | 3.0   | 15   | 2.9224          | 13.8077 | 5.117  | 13.7274 | 13.753    |
| No log        | 4.0   | 20   | 2.9050          | 13.7861 | 5.117  | 13.6982 | 13.7001   |
| No log        | 5.0   | 25   | 2.8920          | 14.668  | 5.117  | 14.4497 | 14.4115   |
| No log        | 6.0   | 30   | 2.8820          | 14.9451 | 5.2469 | 14.5797 | 14.6308   |
| No log        | 7.0   | 35   | 2.8770          | 15.991  | 5.2469 | 14.6278 | 14.7076   |
| No log        | 8.0   | 40   | 2.8757          | 15.991  | 5.2469 | 14.6278 | 14.7076   |


### Framework versions

- Transformers 4.31.0
- Pytorch 2.0.1+cu118
- Datasets 2.14.1
- Tokenizers 0.13.3
