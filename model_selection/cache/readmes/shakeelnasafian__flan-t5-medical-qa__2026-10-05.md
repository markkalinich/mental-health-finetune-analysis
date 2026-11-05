---
library_name: transformers
license: apache-2.0
base_model: google/flan-t5-small
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: flan-t5-medical-qa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-medical-qa

This model is a fine-tuned version of [google/flan-t5-small](https://huggingface.co/google/flan-t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Rouge1: 0.0419
- Rouge2: 0.0158
- Rougel: 0.036
- Rougelsum: 0.0361
- Gen Len: 2.795

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 0.0           | 1.0   | 100  | nan             | 0.0419 | 0.0158 | 0.036  | 0.0361    | 2.795   |
| 0.0           | 2.0   | 200  | nan             | 0.0419 | 0.0158 | 0.036  | 0.0361    | 2.795   |
| 0.0           | 3.0   | 300  | nan             | 0.0419 | 0.0158 | 0.036  | 0.0361    | 2.795   |
| 0.0           | 4.0   | 400  | nan             | 0.0419 | 0.0158 | 0.036  | 0.0361    | 2.795   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
