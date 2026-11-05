---
license: apache-2.0
base_model: gayanin/bart-with-pubmed-noise-data-0.1-v2
tags:
- generated_from_trainer
model-index:
- name: bart-with-pubmed-asr-noise-data-0.1-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-with-pubmed-asr-noise-data-0.1-v2

This model is a fine-tuned version of [gayanin/bart-with-pubmed-noise-data-0.1-v2](https://huggingface.co/gayanin/bart-with-pubmed-noise-data-0.1-v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3346

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 10
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.4242        | 0.87  | 500  | 0.3986          |
| 0.2914        | 1.73  | 1000 | 0.3416          |
| 0.2518        | 2.6   | 1500 | 0.3346          |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.2+cu121
- Datasets 2.17.0
- Tokenizers 0.15.1
