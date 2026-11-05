---
library_name: transformers
license: apache-2.0
base_model: GanjinZero/biobart-v2-base
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: biobart-pubmed-summarization
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobart-pubmed-summarization

This model is a fine-tuned version of [GanjinZero/biobart-v2-base](https://huggingface.co/GanjinZero/biobart-v2-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8444
- Rouge1: 41.78
- Rouge2: 16.03
- Rougel: 24.42
- Rougelsum: 37.28

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.05
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 3.9002        | 1.0   | 1000 | 1.8796          | 41.31  | 16.05  | 24.3   | 37.08     |
| 3.6223        | 2.0   | 2000 | 1.8444          | 41.78  | 16.03  | 24.42  | 37.28     |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.11.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2
