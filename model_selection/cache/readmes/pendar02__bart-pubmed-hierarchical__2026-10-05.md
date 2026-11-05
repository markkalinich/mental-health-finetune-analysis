---
library_name: transformers
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-pubmed-hierarchical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-pubmed-hierarchical

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.4014
- Rouge1: 20.2
- Rouge2: 1.95
- Rougel: 13.15
- Rougelsum: 18.47

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 5.7363        | 0.5   | 5    | 4.6641          | 15.62  | 0.49   | 10.37  | 14.03     |
| 5.4938        | 1.0   | 10   | 4.5342          | 20.66  | 0.95   | 13.1   | 19.59     |
| 4.6575        | 1.5   | 15   | 4.4149          | 20.37  | 1.3    | 12.87  | 18.29     |
| 4.0167        | 2.0   | 20   | 4.4014          | 20.2   | 1.95   | 13.15  | 18.47     |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 3.2.0
- Tokenizers 0.19.1
