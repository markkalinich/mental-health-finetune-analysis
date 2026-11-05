---
library_name: transformers
base_model: aubmindlab/bert-base-arabertv02
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: pharmacy-complaints-bert-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pharmacy-complaints-bert-v2

This model is a fine-tuned version of [aubmindlab/bert-base-arabertv02](https://huggingface.co/aubmindlab/bert-base-arabertv02) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0001
- Accuracy: 1.0
- F1 Macro: 1.0

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
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Macro |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.0012        | 1.0   | 1270 | 0.0004          | 1.0      | 1.0      |
| 0.0003        | 2.0   | 2540 | 0.0002          | 1.0      | 1.0      |
| 0.0002        | 3.0   | 3810 | 0.0001          | 1.0      | 1.0      |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.11.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
