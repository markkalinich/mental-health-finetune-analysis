---
library_name: transformers
license: mit
base_model: roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: scenescope-mood
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# scenescope-mood

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8130
- Accuracy: 0.6667
- F1: 0.6675

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
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.7078        | 1.0   | 70   | 0.6921          | 0.5167   | 0.3520 |
| 0.7055        | 2.0   | 140  | 0.6720          | 0.5333   | 0.3881 |
| 0.6339        | 3.0   | 210  | 0.5943          | 0.7333   | 0.7182 |
| 0.4387        | 4.0   | 280  | 0.5529          | 0.725    | 0.7241 |
| 0.3427        | 5.0   | 350  | 0.5633          | 0.7667   | 0.7667 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cpu
- Datasets 4.0.0
- Tokenizers 0.22.2
