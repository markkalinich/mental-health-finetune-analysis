---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: medical-bidirectional-machine-translation-checkpoints-511042
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-bidirectional-machine-translation-checkpoints-511042

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3042
- Bleu: 50.0202
- Meteor: 0.7238
- Ter: 42.2003

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
| 2.8369        | 0.3131 | 5000  | 42.1073 | 2.5620          | 0.6619 | 50.4746 |
| 2.6585        | 0.6262 | 10000 | 45.5762 | 2.4499          | 0.6918 | 46.0188 |
| 2.5862        | 0.9392 | 15000 | 47.2641 | 2.3876          | 0.7029 | 44.6590 |
| 2.4641        | 1.2523 | 20000 | 48.2187 | 2.3542          | 0.7096 | 43.6970 |
| 2.4571        | 1.5654 | 25000 | 49.0444 | 2.3360          | 0.7175 | 43.0409 |
| 2.4155        | 1.8784 | 30000 | 49.4393 | 2.3161          | 0.7198 | 42.8651 |
| 2.3504        | 2.1915 | 35000 | 49.8071 | 2.3103          | 0.7225 | 42.4001 |
| 2.3259        | 2.5046 | 40000 | 2.3048  | 49.9102         | 0.7230 | 42.3674 |
| 2.316         | 2.8176 | 45000 | 2.3042  | 50.0202         | 0.7238 | 42.2003 |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.10.0+cu128
- Datasets 5.0.0
- Tokenizers 0.22.2
