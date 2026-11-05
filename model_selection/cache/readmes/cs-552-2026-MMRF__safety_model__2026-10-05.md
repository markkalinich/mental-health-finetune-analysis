---
library_name: transformers
base_model: cs-552-2026-MMRF/15kDPO
tags:
- generated_from_trainer
model-index:
- name: 2xwildguard
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 2xwildguard

This model is a fine-tuned version of [cs-552-2026-MMRF/15kDPO](https://huggingface.co/cs-552-2026-MMRF/15kDPO) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0466

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
| 0.0856        | 0.0714 | 50   | 0.0800          |
| 0.0673        | 0.1428 | 100  | 0.0686          |
| 0.0722        | 0.2142 | 150  | 0.0625          |
| 0.0506        | 0.2856 | 200  | 0.0613          |
| 0.0480        | 0.3570 | 250  | 0.0549          |
| 0.0426        | 0.4283 | 300  | 0.0536          |
| 0.0520        | 0.4997 | 350  | 0.0523          |
| 0.0446        | 0.5711 | 400  | 0.0502          |
| 0.0586        | 0.6425 | 450  | 0.0477          |
| 0.0502        | 0.7139 | 500  | 0.0477          |
| 0.0474        | 0.7853 | 550  | 0.0475          |
| 0.0456        | 0.8567 | 600  | 0.0471          |
| 0.0491        | 0.9281 | 650  | 0.0466          |
| 0.0563        | 0.9995 | 700  | 0.0466          |
| 0.0563        | 1.0    | 701  | 0.0466          |


### Framework versions

- Transformers 5.7.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.5
- Tokenizers 0.22.2
