---
library_name: transformers
language:
- en
license: apache-2.0
base_model: Mardiyyah/variant-tapt_freeze_llrd-LR_5e-05
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: variant_tapt_freeze_llrd_LR_5e
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# variant_tapt_freeze_llrd_LR_5e

This model is a fine-tuned version of [Mardiyyah/variant-tapt_freeze_llrd-LR_5e-05](https://huggingface.co/Mardiyyah/variant-tapt_freeze_llrd-LR_5e-05) on the OTAR3088/Variants_IOB-V2 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0651
- Precision: 0.8584
- Recall: 0.8664
- F1: 0.8624
- Accuracy: 0.9858

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
- seed: 3407
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.5514        | 1.0   | 34   | 0.2347          | 0.2767    | 0.2028 | 0.2340 | 0.9168   |
| 0.1451        | 2.0   | 68   | 0.0934          | 0.6139    | 0.7327 | 0.6681 | 0.9716   |
| 0.0725        | 3.0   | 102  | 0.0718          | 0.8148    | 0.8111 | 0.8129 | 0.9812   |
| 0.0485        | 4.0   | 136  | 0.0651          | 0.8136    | 0.8249 | 0.8192 | 0.9831   |
| 0.0321        | 5.0   | 170  | 0.0605          | 0.8378    | 0.8571 | 0.8474 | 0.9850   |
| 0.0243        | 6.0   | 204  | 0.0646          | 0.8493    | 0.8571 | 0.8532 | 0.9852   |
| 0.0181        | 7.0   | 238  | 0.0641          | 0.8468    | 0.8664 | 0.8565 | 0.9864   |
| 0.0161        | 8.0   | 272  | 0.0603          | 0.8584    | 0.8664 | 0.8624 | 0.9858   |
| 0.0125        | 9.0   | 306  | 0.0584          | 0.8386    | 0.8618 | 0.85   | 0.9858   |
| 0.0118        | 10.0  | 340  | 0.0616          | 0.8462    | 0.8618 | 0.8539 | 0.9862   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
