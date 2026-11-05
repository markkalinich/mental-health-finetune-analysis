---
license: apache-2.0
base_model: google/flan-t5-base
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: finetuned-t5-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned-t5-medical

This model is a fine-tuned version of [google/flan-t5-base](https://huggingface.co/google/flan-t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8686
- Rouge1: 0.1114
- Rouge2: 0.0304
- Rougel: 0.0872
- Rougelsum: 0.1020

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| No log        | 1.0   | 85   | 2.0499          | 0.1186 | 0.0307 | 0.0940 | 0.1071    |
| No log        | 2.0   | 170  | 1.9463          | 0.1021 | 0.0251 | 0.0838 | 0.0926    |
| No log        | 3.0   | 255  | 1.8942          | 0.1158 | 0.0324 | 0.0934 | 0.1083    |
| No log        | 4.0   | 340  | 1.8706          | 0.1101 | 0.0279 | 0.0860 | 0.1017    |
| No log        | 5.0   | 425  | 1.8686          | 0.1114 | 0.0304 | 0.0872 | 0.1020    |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
