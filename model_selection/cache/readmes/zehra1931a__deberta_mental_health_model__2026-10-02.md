---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta_mental_health_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta_mental_health_model

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3262
- F1 Micro: 0.8207
- F1 Macro: 0.8013
- Accuracy: 0.7401

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | F1 Micro | F1 Macro | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:--------:|:--------:|
| 0.3001        | 1.0   | 9825  | 0.3093          | 0.8074   | 0.7871   | 0.7231   |
| 0.2517        | 2.0   | 19650 | 0.3001          | 0.8231   | 0.8042   | 0.7382   |
| 0.204         | 3.0   | 29475 | 0.3215          | 0.8233   | 0.8057   | 0.7430   |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
