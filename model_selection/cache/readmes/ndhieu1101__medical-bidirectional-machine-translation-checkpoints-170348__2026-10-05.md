---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: medical-bidirectional-machine-translation-checkpoints-170348
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-bidirectional-machine-translation-checkpoints-170348

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4300
- Bleu: 46.9673
- Meteor: 0.7008
- Ter: 44.9558

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
| 2.7667        | 0.9392 | 5000  | 43.6287 | 2.5316          | 0.6726 | 48.6120 |
| 2.5786        | 1.8784 | 10000 | 46.4032 | 2.4425          | 0.6968 | 45.4942 |
| 2.4532        | 2.8175 | 15000 | 2.4300  | 46.9673         | 0.7008 | 44.9558 |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.10.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2
