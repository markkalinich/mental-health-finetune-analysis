---
library_name: transformers
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: muril_suicide_detection_final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# muril_suicide_detection_final

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1370
- Accuracy: 0.9262
- F1: 0.9275
- Precision: 0.9032
- Recall: 0.9532

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.0652        | 1.0   | 119  | 0.0203          | 0.9684   | 0.9676 | 0.9912    | 0.9451 |
| 0.0127        | 2.0   | 238  | 0.0250          | 0.9642   | 0.9631 | 0.9911    | 0.9367 |
| 0.0073        | 3.0   | 357  | 0.0250          | 0.9747   | 0.9742 | 0.9913    | 0.9578 |
| 0.0050        | 4.0   | 476  | 0.0248          | 0.9726   | 0.9720 | 0.9912    | 0.9536 |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.3
- Tokenizers 0.22.2
