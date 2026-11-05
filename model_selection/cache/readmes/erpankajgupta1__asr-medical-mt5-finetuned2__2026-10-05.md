---
library_name: transformers
license: apache-2.0
base_model: HiTZ/Medical-mT5-large
tags:
- generated_from_trainer
model-index:
- name: asr-medical-mt5-finetuned2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# asr-medical-mt5-finetuned2

This model is a fine-tuned version of [HiTZ/Medical-mT5-large](https://huggingface.co/HiTZ/Medical-mT5-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 9.8316

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2417153.8     | 1.0   | 138  | 9.8316          |
| 359610.675    | 2.0   | 276  | 9.8316          |
| 9973.0102     | 3.0   | 414  | 9.8316          |


### Framework versions

- Transformers 4.52.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
