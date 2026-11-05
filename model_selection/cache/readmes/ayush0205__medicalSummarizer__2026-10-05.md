---
library_name: transformers
license: apache-2.0
base_model: t5-small
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: medicalSummarizer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medicalSummarizer

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9779
- Rouge1: 21.6093
- Rouge2: 12.601
- Rougel: 19.1461
- Rougelsum: 20.6328
- Gen Len: 19.0

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
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 1.2835        | 1.0   | 865  | 0.9779          | 21.6093 | 12.601 | 19.1461 | 20.6328   | 19.0    |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu124
- Datasets 3.1.0
- Tokenizers 0.20.3
