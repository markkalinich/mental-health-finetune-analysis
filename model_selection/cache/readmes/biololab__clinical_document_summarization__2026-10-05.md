---
license: mit
base_model: flax-community/spanish-t5-small
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: clinical_document_summarization
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_document_summarization

This model is a fine-tuned version of [flax-community/spanish-t5-small](https://huggingface.co/flax-community/spanish-t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4429
- Rouge1: 0.3814
- Rouge2: 0.3162
- Rougel: 0.3727
- Rougelsum: 0.3727
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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 0.9449        | 1.0   | 592  | 0.6076          | 0.3739 | 0.303  | 0.3633 | 0.3632    | 18.9996 |
| 0.6902        | 2.0   | 1184 | 0.5278          | 0.3771 | 0.3101 | 0.3686 | 0.3685    | 19.0    |
| 0.601         | 3.0   | 1776 | 0.4962          | 0.3797 | 0.3143 | 0.3721 | 0.3721    | 19.0    |
| 0.568         | 4.0   | 2368 | 0.4721          | 0.3792 | 0.3134 | 0.3701 | 0.3701    | 19.0    |
| 0.5334        | 5.0   | 2960 | 0.4597          | 0.3795 | 0.3143 | 0.3713 | 0.3713    | 19.0    |
| 0.4968        | 6.0   | 3552 | 0.4496          | 0.3816 | 0.3165 | 0.3729 | 0.3729    | 19.0    |
| 0.4873        | 7.0   | 4144 | 0.4449          | 0.3812 | 0.316  | 0.3726 | 0.3726    | 19.0    |
| 0.4794        | 8.0   | 4736 | 0.4429          | 0.3814 | 0.3162 | 0.3727 | 0.3727    | 19.0    |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.1.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
