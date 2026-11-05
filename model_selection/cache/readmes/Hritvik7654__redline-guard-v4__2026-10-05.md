---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-large
tags:
- generated_from_trainer
model-index:
- name: redline-guard-v4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# redline-guard-v4

This model is a fine-tuned version of [answerdotai/ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0918
- Auprc: 0.9975
- Auroc: 0.9977
- Tpr@1fpr: 0.9581

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
- train_batch_size: 32
- eval_batch_size: 128
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 2

### Training results

| Training Loss | Epoch  | Step  | Auprc  | Auroc  | Validation Loss | Tpr@1fpr |
|:-------------:|:------:|:-----:|:------:|:------:|:---------------:|:--------:|
| 0.101         | 0.0828 | 2000  | 0.9920 | 0.9925 | 0.1112          | 0.8790   |
| 0.0819        | 0.1656 | 4000  | 0.9922 | 0.9923 | 0.1369          | 0.8919   |
| 0.0681        | 0.2484 | 6000  | 0.9940 | 0.9944 | 0.1111          | 0.9066   |
| 0.0592        | 0.3313 | 8000  | 0.9954 | 0.9958 | 0.0954          | 0.9236   |
| 0.0527        | 0.4141 | 10000 | 0.9944 | 0.9944 | 0.1290          | 0.9228   |
| 0.0542        | 0.4969 | 12000 | 0.9964 | 0.9967 | 0.0769          | 0.9298   |
| 0.0581        | 0.5797 | 14000 | 0.9960 | 0.9964 | 0.0782          | 0.9311   |
| 0.0541        | 0.6625 | 16000 | 0.9965 | 0.9968 | 0.0729          | 0.9436   |
| 0.054         | 0.7453 | 18000 | 0.9971 | 0.9974 | 0.0663          | 0.9526   |
| 0.054         | 0.8282 | 20000 | 0.9967 | 0.9970 | 0.0780          | 0.9413   |
| 0.0438        | 0.9110 | 22000 | 0.9973 | 0.9975 | 0.0670          | 0.9472   |
| 0.0419        | 0.9938 | 24000 | 0.9976 | 0.9979 | 0.0635          | 0.9477   |
| 0.0255        | 1.0766 | 26000 | 0.9974 | 0.9977 | 0.0747          | 0.9538   |
| 0.0216        | 1.1594 | 28000 | 0.9973 | 0.9976 | 0.0822          | 0.9534   |
| 0.028         | 1.2422 | 30000 | 0.9972 | 0.9974 | 0.0707          | 0.9555   |
| 0.027         | 1.3251 | 32000 | 0.9974 | 0.9976 | 0.0751          | 0.9575   |
| 0.0254        | 1.4079 | 34000 | 0.9974 | 0.9976 | 0.0754          | 0.9543   |
| 0.0166        | 1.4907 | 36000 | 0.0906 | 0.9974 | 0.9976          | 0.9585   |
| 0.0151        | 1.5735 | 38000 | 0.1104 | 0.9969 | 0.9969          | 0.9541   |
| 0.0181        | 1.6563 | 40000 | 0.0927 | 0.9972 | 0.9973          | 0.9568   |
| 0.016         | 1.7391 | 42000 | 0.0947 | 0.9972 | 0.9973          | 0.9585   |
| 0.013         | 1.8219 | 44000 | 0.0848 | 0.9975 | 0.9976          | 0.9585   |
| 0.0111        | 1.9048 | 46000 | 0.0938 | 0.9975 | 0.9976          | 0.9596   |
| 0.0186        | 1.9876 | 48000 | 0.0918 | 0.9975 | 0.9977          | 0.9581   |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.13.0+cu130
- Datasets 5.0.1
- Tokenizers 0.22.2
