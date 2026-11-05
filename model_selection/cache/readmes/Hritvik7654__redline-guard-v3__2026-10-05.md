---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
model-index:
- name: redline-guard-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# redline-guard-v3

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0965
- Auprc: 0.9914
- Auroc: 0.9953
- Tpr@1fpr: 0.9082

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
| 0.1865        | 0.1941 | 2000  | 0.1469          | 0.9734 | 0.9850 | 0.7717   |
| 0.1211        | 0.3882 | 4000  | 0.1419          | 0.9808 | 0.9892 | 0.8232   |
| 0.1109        | 0.5822 | 6000  | 0.1030          | 0.9867 | 0.9925 | 0.8727   |
| 0.1007        | 0.7763 | 8000  | 0.0974          | 0.9886 | 0.9937 | 0.8874   |
| 0.0997        | 0.9704 | 10000 | 0.0895          | 0.9904 | 0.9948 | 0.9050   |
| 0.0572        | 1.1645 | 12000 | 0.1256          | 0.9899 | 0.9943 | 0.9058   |
| 0.0622        | 1.3586 | 14000 | 0.0962          | 0.9908 | 0.9950 | 0.9098   |
| 0.0562        | 1.5526 | 16000 | 0.1030          | 0.9905 | 0.9949 | 0.9018   |
| 0.065         | 1.7467 | 18000 | 0.0961          | 0.9909 | 0.9951 | 0.9062   |
| 0.0545        | 1.9408 | 20000 | 0.0965          | 0.9914 | 0.9953 | 0.9082   |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.13.0+cu130
- Datasets 5.0.1
- Tokenizers 0.22.2
