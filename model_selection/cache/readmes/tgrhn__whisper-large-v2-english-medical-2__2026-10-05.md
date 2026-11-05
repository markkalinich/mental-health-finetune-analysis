---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-large-v2
tags:
- generated_from_trainer
model-index:
- name: whisper-large-v2-english-medical-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-large-v2-english-medical-2

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1072

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 249  | 0.1321          |
| No log        | 2.0   | 498  | 0.1072          |


### Framework versions

- Transformers 4.45.2
- Pytorch 2.4.0+cu121
- Datasets 2.18.0
- Tokenizers 0.20.1
