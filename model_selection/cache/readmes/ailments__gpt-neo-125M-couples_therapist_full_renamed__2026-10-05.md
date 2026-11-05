---
license: mit
base_model: EleutherAI/gpt-neo-125M
tags:
- generated_from_trainer
model-index:
- name: gpt-neo-125M-couples_therapist_full_renamed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt-neo-125M-couples_therapist_full_renamed

This model is a fine-tuned version of [EleutherAI/gpt-neo-125M](https://huggingface.co/EleutherAI/gpt-neo-125M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0778

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 73   | 3.2091          |
| No log        | 2.0   | 146  | 3.1027          |
| No log        | 3.0   | 219  | 3.0778          |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
