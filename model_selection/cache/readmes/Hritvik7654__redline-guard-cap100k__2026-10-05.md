---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
model-index:
- name: redline-guard-cap100k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# redline-guard-cap100k

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1093
- Auprc: 0.9916
- Auroc: 0.9954
- Tpr@1fpr: 0.9322

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
- train_batch_size: 32
- eval_batch_size: 128
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 2

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Auprc  | Auroc  | Tpr@1fpr |
|:-------------:|:------:|:-----:|:---------------:|:------:|:------:|:--------:|
| 0.1527        | 0.1561 | 2000  | 0.1273          | 0.9793 | 0.9884 | 0.8557   |
| 0.1179        | 0.3121 | 4000  | 0.1310          | 0.9786 | 0.9861 | 0.9034   |
| 0.0973        | 0.4682 | 6000  | 0.1091          | 0.9886 | 0.9941 | 0.9019   |
| 0.0878        | 0.6243 | 8000  | 0.0927          | 0.9889 | 0.9931 | 0.9356   |
| 0.0809        | 0.7803 | 10000 | 0.0785          | 0.9907 | 0.9944 | 0.9398   |
| 0.0883        | 0.9364 | 12000 | 0.0803          | 0.9905 | 0.9945 | 0.9319   |
| 0.0451        | 1.0925 | 14000 | 0.1237          | 0.9900 | 0.9951 | 0.8921   |
| 0.0505        | 1.2485 | 16000 | 0.1267          | 0.9895 | 0.9942 | 0.9132   |
| 0.0404        | 1.4046 | 18000 | 0.1216          | 0.9906 | 0.9946 | 0.9270   |
| 0.0488        | 1.5607 | 20000 | 0.1056          | 0.9919 | 0.9959 | 0.9243   |
| 0.0411        | 1.7167 | 22000 | 0.1096          | 0.9919 | 0.9957 | 0.9240   |
| 0.0368        | 1.8728 | 24000 | 0.1093          | 0.9916 | 0.9954 | 0.9322   |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.13.0+cu130
- Datasets 5.0.1
- Tokenizers 0.22.2
