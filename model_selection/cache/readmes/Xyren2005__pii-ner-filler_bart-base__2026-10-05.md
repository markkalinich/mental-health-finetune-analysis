---
library_name: transformers
license: apache-2.0
base_model: facebook/bart-base
tags:
- generated_from_trainer
model-index:
- name: filler_bart-base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# filler_bart-base

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8371

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 4640
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 4.6092        | 1.0   | 2901  | 2.1525          |
| 4.2982        | 2.0   | 5802  | 2.0552          |
| 4.1210        | 3.0   | 8703  | 1.9938          |
| 3.9219        | 4.0   | 11604 | 1.9542          |
| 3.8350        | 5.0   | 14505 | 1.9148          |
| 3.8411        | 6.0   | 17406 | 1.8929          |
| 3.7769        | 7.0   | 20307 | 1.8730          |
| 3.7537        | 8.0   | 23208 | 1.8590          |
| 3.5861        | 9.0   | 26109 | 1.8513          |
| 3.5525        | 10.0  | 29010 | 1.8407          |
| 3.4343        | 11.0  | 31911 | 1.8371          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.3
- Tokenizers 0.22.2
