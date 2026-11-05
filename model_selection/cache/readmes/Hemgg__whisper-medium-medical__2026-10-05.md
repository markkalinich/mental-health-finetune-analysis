---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-medium
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-medium-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-medium-medical

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0562
- Wer: 10.7169

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- training_steps: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer     |
|:-------------:|:------:|:----:|:---------------:|:-------:|
| 0.5008        | 0.5405 | 100  | 0.1965          | 12.0203 |
| 0.1034        | 1.0811 | 200  | 0.0870          | 12.2616 |
| 0.0563        | 1.6216 | 300  | 0.0642          | 8.3514  |
| 0.0238        | 2.1622 | 400  | 0.0610          | 11.6341 |
| 0.0129        | 2.7027 | 500  | 0.0562          | 10.7169 |


### Framework versions

- Transformers 4.49.0
- Pytorch 2.6.0+cu118
- Datasets 3.3.1
- Tokenizers 0.21.0
