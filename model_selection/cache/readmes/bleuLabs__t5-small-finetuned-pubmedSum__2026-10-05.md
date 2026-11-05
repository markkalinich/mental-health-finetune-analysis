---
library_name: transformers
license: apache-2.0
base_model: google-t5/t5-small
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-finetuned-pubmedSum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-pubmedSum

This model is a fine-tuned version of [google-t5/t5-small](https://huggingface.co/google-t5/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0141
- Rouge1: 14.3086
- Rouge2: 6.1646
- Rougel: 12.2632
- Rougelsum: 13.2105
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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.2119        | 1.0   | 29981 | 2.0141          | 14.3086 | 6.1646 | 12.2632 | 13.2105   | 19.0    |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu124
- Datasets 2.21.0
- Tokenizers 0.19.1
