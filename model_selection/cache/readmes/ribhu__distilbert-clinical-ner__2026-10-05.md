---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: distilbert-clinical-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-clinical-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3672

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 36   | 0.2829          |
| No log        | 2.0   | 72   | 0.2953          |
| No log        | 3.0   | 108  | 0.3107          |
| No log        | 4.0   | 144  | 0.3310          |
| No log        | 5.0   | 180  | 0.3451          |
| No log        | 6.0   | 216  | 0.3449          |
| No log        | 7.0   | 252  | 0.3620          |
| No log        | 8.0   | 288  | 0.3668          |
| No log        | 9.0   | 324  | 0.3661          |
| No log        | 10.0  | 360  | 0.3672          |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Tokenizers 0.19.1
