---
license: apache-2.0
base_model: google/flan-t5-base
tags:
- generated_from_trainer
datasets:
- pubmed-summarization
model-index:
- name: flan-t5-base-pubmed-summarization
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-base-pubmed-summarization

This model is a fine-tuned version of [google/flan-t5-base](https://huggingface.co/google/flan-t5-base) on the pubmed-summarization dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6534

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 1.8896        | 1.0   | 14991  | 1.7152          |
| 1.8445        | 2.0   | 29982  | 1.6872          |
| 1.8061        | 3.0   | 44973  | 1.6689          |
| 1.7714        | 4.0   | 59964  | 1.6626          |
| 1.7764        | 5.0   | 74955  | 1.6597          |
| 1.7523        | 6.0   | 89946  | 1.6566          |
| 1.752         | 7.0   | 104937 | 1.6545          |
| 1.7281        | 8.0   | 119928 | 1.6538          |
| 1.7523        | 9.0   | 134919 | 1.6534          |
| 1.7439        | 10.0  | 149910 | 1.6534          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.0+cu121
- Datasets 2.17.1
- Tokenizers 0.15.2
