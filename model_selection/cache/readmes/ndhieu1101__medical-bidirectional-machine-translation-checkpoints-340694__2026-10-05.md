---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: medical-bidirectional-machine-translation-checkpoints-340694
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-bidirectional-machine-translation-checkpoints-340694

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Bleu: 49.0909
- Loss: 2.3428
- Meteor: 0.7167
- Ter: 43.1201

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 3
- mixed_precision_training: Native AMP
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch  | Step  | Bleu    | Validation Loss | Meteor | Ter     |
|:-------------:|:------:|:-----:|:-------:|:---------------:|:------:|:-------:|
| 2.7981        | 0.4696 | 5000  | 42.9710 | 2.5439          | 0.6672 | 50.5847 |
| 2.6759        | 0.9393 | 10000 | 46.1727 | 2.4387          | 0.6955 | 45.4049 |
| 2.5064        | 1.4089 | 15000 | 47.7724 | 2.3950          | 0.7069 | 44.3175 |
| 2.4793        | 1.8785 | 20000 | 48.6344 | 2.3593          | 0.7132 | 43.5354 |
| 2.3757        | 2.3481 | 25000 | 49.0054 | 2.3496          | 0.7161 | 43.2306 |
| 2.3819        | 2.8177 | 30000 | 49.0909 | 2.3428          | 0.7167 | 43.1201 |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.10.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2
