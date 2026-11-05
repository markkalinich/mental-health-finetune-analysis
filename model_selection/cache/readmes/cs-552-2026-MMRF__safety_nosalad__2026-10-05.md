---
library_name: transformers
base_model: cs-552-2026-MMRF/15kDPO
tags:
- generated_from_trainer
model-index:
- name: safety_nosalad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# safety_nosalad

This model is a fine-tuned version of [cs-552-2026-MMRF/15kDPO](https://huggingface.co/cs-552-2026-MMRF/15kDPO) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0528

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.0782        | 0.1170 | 50   | 0.0776          |
| 0.0823        | 0.2339 | 100  | 0.0696          |
| 0.0569        | 0.3509 | 150  | 0.0629          |
| 0.0547        | 0.4678 | 200  | 0.0583          |
| 0.0625        | 0.5848 | 250  | 0.0561          |
| 0.0527        | 0.7018 | 300  | 0.0534          |
| 0.0597        | 0.8187 | 350  | 0.0531          |
| 0.0610        | 0.9357 | 400  | 0.0529          |
| 0.0539        | 1.0    | 428  | 0.0528          |


### Framework versions

- Transformers 5.7.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.5
- Tokenizers 0.22.2
