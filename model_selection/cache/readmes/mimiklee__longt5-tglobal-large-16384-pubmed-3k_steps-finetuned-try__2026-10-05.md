---
license: apache-2.0
base_model: Stancld/longt5-tglobal-large-16384-pubmed-3k_steps
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: longt5-tglobal-large-16384-pubmed-3k_steps-finetuned-try
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# longt5-tglobal-large-16384-pubmed-3k_steps-finetuned-try

This model is a fine-tuned version of [Stancld/longt5-tglobal-large-16384-pubmed-3k_steps](https://huggingface.co/Stancld/longt5-tglobal-large-16384-pubmed-3k_steps) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.4908
- Rouge1: 9.8332
- Rouge2: 4.5131
- Rougel: 7.9018
- Rougelsum: 9.1249
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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:------:|:---------:|:-------:|
| No log        | 1.0   | 25   | 3.6842          | 9.7994  | 4.6182 | 8.4691 | 9.1692    | 19.0    |
| No log        | 2.0   | 50   | 3.5808          | 10.1729 | 4.5409 | 8.4082 | 9.3547    | 19.0    |
| No log        | 3.0   | 75   | 3.5255          | 10.2028 | 4.6251 | 8.3879 | 9.4187    | 19.0    |
| No log        | 4.0   | 100  | 3.4989          | 9.8481  | 4.4739 | 7.8605 | 9.1653    | 19.0    |
| No log        | 5.0   | 125  | 3.4908          | 9.8332  | 4.5131 | 7.9018 | 9.1249    | 19.0    |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1
