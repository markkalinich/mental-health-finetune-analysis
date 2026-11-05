---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- generated_from_trainer
model-index:
- name: redline-guard
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# redline-guard

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0493
- Auprc: 0.9979
- Auroc: 0.9985
- Tpr@1fpr: 0.9743

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
| 0.149         | 0.0770 | 2000  | 0.1499          | 0.9800 | 0.9861 | 0.8161   |
| 0.0901        | 0.1541 | 4000  | 0.0956          | 0.9914 | 0.9941 | 0.9168   |
| 0.0743        | 0.2311 | 6000  | 0.0808          | 0.9940 | 0.9959 | 0.9348   |
| 0.0703        | 0.3082 | 8000  | 0.1379          | 0.9910 | 0.9943 | 0.8894   |
| 0.069         | 0.3852 | 10000 | 0.0690          | 0.9953 | 0.9969 | 0.9440   |
| 0.0589        | 0.4623 | 12000 | 0.0752          | 0.9954 | 0.9971 | 0.9407   |
| 0.0658        | 0.5393 | 14000 | 0.0744          | 0.9959 | 0.9972 | 0.9504   |
| 0.0615        | 0.6164 | 16000 | 0.0592          | 0.9963 | 0.9975 | 0.9598   |
| 0.0573        | 0.6934 | 18000 | 0.0642          | 0.9961 | 0.9974 | 0.9521   |
| 0.0512        | 0.7704 | 20000 | 0.0529          | 0.9970 | 0.9980 | 0.9666   |
| 0.0501        | 0.8475 | 22000 | 0.0494          | 0.9972 | 0.9981 | 0.9645   |
| 0.0573        | 0.9245 | 24000 | 0.0496          | 0.9972 | 0.9982 | 0.9656   |
| 0.0473        | 1.0016 | 26000 | 0.0494          | 0.9975 | 0.9983 | 0.9710   |
| 0.031         | 1.0786 | 28000 | 0.0561          | 0.9972 | 0.9981 | 0.9691   |
| 0.0314        | 1.1557 | 30000 | 0.0537          | 0.9974 | 0.9982 | 0.9704   |
| 0.0266        | 1.2327 | 32000 | 0.0574          | 0.9973 | 0.9982 | 0.9693   |
| 0.0286        | 1.3098 | 34000 | 0.0538          | 0.9974 | 0.9981 | 0.9713   |
| 0.0317        | 1.3868 | 36000 | 0.0554          | 0.9976 | 0.9983 | 0.9724   |
| 0.0281        | 1.4638 | 38000 | 0.0514          | 0.9976 | 0.9983 | 0.9737   |
| 0.0254        | 1.5409 | 40000 | 0.0578          | 0.9974 | 0.9982 | 0.9703   |
| 0.0287        | 1.6179 | 42000 | 0.0536          | 0.9976 | 0.9983 | 0.9726   |
| 0.0233        | 1.6950 | 44000 | 0.0514          | 0.9978 | 0.9985 | 0.9752   |
| 0.0215        | 1.7720 | 46000 | 0.0533          | 0.9976 | 0.9983 | 0.9751   |
| 0.031         | 1.8491 | 48000 | 0.0512          | 0.9978 | 0.9985 | 0.9740   |
| 0.0265        | 1.9261 | 50000 | 0.0493          | 0.9979 | 0.9985 | 0.9743   |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.13.0+cu130
- Datasets 5.0.1
- Tokenizers 0.22.2
