---
license: apache-2.0
base_model: google/flan-t5-large
tags:
- text2textgeneration
- generated_from_trainer
metrics:
- rouge
model-index:
- name: flan-t5-large-finetune-medicine-v5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-large-finetune-medicine-v5

This model is a fine-tuned version of [google/flan-t5-large](https://huggingface.co/google/flan-t5-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3517
- Rouge1: 27.7218
- Rouge2: 10.9162
- Rougel: 23.6057
- Rougelsum: 23.2999

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 1.0   | 5    | 2.2465          | 14.6773 | 3.5979  | 13.871  | 14.2474   |
| No log        | 2.0   | 10   | 2.1106          | 10.2078 | 2.1164  | 10.2919 | 10.276    |
| No log        | 3.0   | 15   | 2.0535          | 16.7761 | 1.5873  | 16.7952 | 17.1838   |
| No log        | 4.0   | 20   | 2.0323          | 16.6844 | 1.5873  | 16.8444 | 16.9094   |
| No log        | 5.0   | 25   | 2.0063          | 17.2911 | 2.3045  | 14.8127 | 15.3235   |
| No log        | 6.0   | 30   | 2.0079          | 15.3197 | 4.6561  | 14.278  | 14.8369   |
| No log        | 7.0   | 35   | 2.0319          | 15.9877 | 5.8947  | 13.9837 | 14.1814   |
| No log        | 8.0   | 40   | 2.0748          | 23.1763 | 10.5    | 20.2887 | 20.2578   |
| No log        | 9.0   | 45   | 2.1303          | 21.1874 | 6.9444  | 19.0088 | 18.991    |
| No log        | 10.0  | 50   | 2.1746          | 20.2807 | 6.2865  | 18.2145 | 18.1012   |
| No log        | 11.0  | 55   | 2.1729          | 21.8364 | 9.8421  | 18.7897 | 18.8242   |
| No log        | 12.0  | 60   | 2.2083          | 22.777  | 10.9162 | 21.3444 | 21.1464   |
| No log        | 13.0  | 65   | 2.2658          | 21.7641 | 10.9162 | 20.3906 | 19.8167   |
| No log        | 14.0  | 70   | 2.2889          | 21.7641 | 10.9162 | 20.3906 | 19.8167   |
| No log        | 15.0  | 75   | 2.2998          | 25.3171 | 10.9162 | 21.3683 | 20.9228   |
| No log        | 16.0  | 80   | 2.3082          | 26.0279 | 10.9162 | 21.9565 | 21.7519   |
| No log        | 17.0  | 85   | 2.3166          | 26.0279 | 10.9162 | 21.9565 | 21.7519   |
| No log        | 18.0  | 90   | 2.3325          | 27.7218 | 10.9162 | 23.6057 | 23.2999   |
| No log        | 19.0  | 95   | 2.3462          | 27.7218 | 10.9162 | 23.6057 | 23.2999   |
| No log        | 20.0  | 100  | 2.3517          | 27.7218 | 10.9162 | 23.6057 | 23.2999   |


### Framework versions

- Transformers 4.31.0
- Pytorch 2.0.1+cu118
- Datasets 2.14.1
- Tokenizers 0.13.3
