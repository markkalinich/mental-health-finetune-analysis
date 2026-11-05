---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
model-index:
- name: distillbert-clinical-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distillbert-clinical-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4598

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 144  | 0.2837          |
| No log        | 2.0   | 288  | 0.3082          |
| No log        | 3.0   | 432  | 0.3243          |
| 0.1109        | 4.0   | 576  | 0.3519          |
| 0.1109        | 5.0   | 720  | 0.3840          |
| 0.1109        | 6.0   | 864  | 0.4083          |
| 0.045         | 7.0   | 1008 | 0.4329          |
| 0.045         | 8.0   | 1152 | 0.4411          |
| 0.045         | 9.0   | 1296 | 0.4589          |
| 0.045         | 10.0  | 1440 | 0.4598          |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.5.0+cu121
- Tokenizers 0.19.1
