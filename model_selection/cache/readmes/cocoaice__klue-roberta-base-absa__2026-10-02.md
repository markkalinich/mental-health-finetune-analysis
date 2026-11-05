---
library_name: transformers
license: mit
base_model: klue/roberta-base
tags:
- absa
- aspect-based-sentiment-analysis
- sentiment-analysis
- korean
- roberta
- transformers
- pytorch
- generated_from_trainer
model-index:
- name: klue-roberta-base-absa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# klue-roberta-base-absa

This model is a fine-tuned version of [klue/roberta-base](https://huggingface.co/klue/roberta-base) on an unknown dataset.

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
