---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: encoder_deberta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# encoder_deberta

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0614
- F1: 0.9372

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 4640
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step  | F1     | Validation Loss |
|:-------------:|:-----:|:-----:|:------:|:---------------:|
| 0.6702        | 1.0   | 2901  | 0.8350 | 0.1344          |
| 0.3783        | 2.0   | 5802  | 0.9054 | 0.0811          |
| 0.2713        | 3.0   | 8703  | 0.9190 | 0.0649          |
| 0.2137        | 4.0   | 11604 | 0.9264 | 0.0611          |
| 0.1863        | 5.0   | 14505 | 0.9312 | 0.0572          |
| 0.1400        | 6.0   | 17406 | 0.9343 | 0.0610          |
| 0.1279        | 7.0   | 20307 | 0.9369 | 0.0594          |
| 0.1059        | 8.0   | 23208 | 0.0614 | 0.9372          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.3
- Tokenizers 0.22.2
