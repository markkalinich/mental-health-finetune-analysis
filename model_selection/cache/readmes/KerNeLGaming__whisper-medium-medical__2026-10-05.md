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
- Loss: 0.2889
- Wer: 0.1281

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_BNB with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.4747        | 1.0   | 102  | 0.3153          | 0.1621 |
| 1.4045        | 2.0   | 204  | 0.2641          | 0.1341 |
| 0.6465        | 3.0   | 306  | 0.2671          | 0.1321 |
| 0.2759        | 4.0   | 408  | 0.2727          | 0.1278 |
| 0.1574        | 5.0   | 510  | 0.2889          | 0.1281 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 2.19.0
- Tokenizers 0.22.2
