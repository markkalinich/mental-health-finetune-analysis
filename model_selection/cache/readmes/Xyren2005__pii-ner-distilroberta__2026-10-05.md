---
library_name: transformers
license: apache-2.0
base_model: distilroberta-base
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: encoder_distilroberta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# encoder_distilroberta

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0709
- F1: 0.9117

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 64
- eval_batch_size: 128
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 4640
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | F1     | Validation Loss |
|:-------------:|:-----:|:-----:|:------:|:---------------:|
| 0.1511        | 1.0   | 2901  | 0.8117 | 0.1268          |
| 0.0962        | 2.0   | 5802  | 0.8733 | 0.0841          |
| 0.0680        | 3.0   | 8703  | 0.0744 | 0.8899          |
| 0.0515        | 4.0   | 11604 | 0.0669 | 0.8972          |
| 0.0436        | 5.0   | 14505 | 0.0675 | 0.9058          |
| 0.0370        | 6.0   | 17406 | 0.0673 | 0.9099          |
| 0.0307        | 7.0   | 20307 | 0.0689 | 0.9110          |
| 0.0261        | 8.0   | 23208 | 0.0709 | 0.9117          |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.3
- Tokenizers 0.22.2
