---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: medical-bidirectional-machine-translation-checkpoints-68138
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-bidirectional-machine-translation-checkpoints-68138

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5705
- Bleu: 43.0721
- Meteor: 0.6675
- Ter: 48.8645

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

| Training Loss | Epoch  | Step | Validation Loss | Bleu    | Meteor | Ter     |
|:-------------:|:------:|:----:|:---------------:|:-------:|:------:|:-------:|
| 2.5866        | 2.3475 | 5000 | 2.5705          | 43.0721 | 0.6675 | 48.8645 |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.10.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2
