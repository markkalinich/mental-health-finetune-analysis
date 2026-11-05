---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-small
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-small-medical
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-medical

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5183
- Wer: 0.1197

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 50
- training_steps: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer    |
|:-------------:|:-------:|:----:|:---------------:|:------:|
| 0.0144        | 4.5581  | 100  | 0.4991          | 0.1408 |
| 0.0009        | 9.0930  | 200  | 0.4764          | 0.1244 |
| 0.0003        | 13.6512 | 300  | 0.5091          | 0.1197 |
| 0.0002        | 18.1860 | 400  | 0.5164          | 0.1197 |
| 0.0002        | 22.7442 | 500  | 0.5183          | 0.1197 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
