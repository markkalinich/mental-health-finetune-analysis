---
license: apache-2.0
base_model: google/flan-t5-small
tags:
- text2textgeneration
- generated_from_trainer
metrics:
- rouge
model-index:
- name: flan-t5-small-finetuned-medicine
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-small-finetuned-medicine

This model is a fine-tuned version of [google/flan-t5-small](https://huggingface.co/google/flan-t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9066
- Rouge1: 9.3596
- Rouge2: 2.6144
- Rougel: 8.94
- Rougelsum: 8.94

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.1417        | 1.0   | 5    | 2.9168          | 9.5238 | 2.6144 | 8.9947 | 8.9947    |
| 3.1069        | 2.0   | 10   | 2.9066          | 9.3596 | 2.6144 | 8.94   | 8.94      |


### Framework versions

- Transformers 4.31.0
- Pytorch 2.0.1+cu118
- Datasets 2.14.0
- Tokenizers 0.13.3
