---
library_name: transformers
license: apache-2.0
base_model: google/mt5-base
tags:
- full-finetuning
- amharic
- sentiment-analysis
- single-task
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: STL-FullFineT-mt5-base-sentiment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# STL-FullFineT-mt5-base-sentiment

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0690
- Accuracy: 0.4726
- Macro F1: 0.3523

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 300
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Macro F1 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 13.1579       | 1.0   | 189  | 5.2648          | 0.2544   | 0.1210   |
| 2.6018        | 2.0   | 378  | 2.0854          | 0.3828   | 0.3174   |
| 2.2819        | 3.0   | 567  | 2.0504          | 0.3653   | 0.3028   |
| 2.1426        | 4.0   | 756  | 1.9917          | 0.4601   | 0.4402   |
| 2.1339        | 5.0   | 945  | 1.9797          | 0.4651   | 0.4549   |
| 2.1267        | 6.0   | 1134 | 1.9771          | 0.4501   | 0.3877   |
| 3.2990        | 7.0   | 1323 | 2.1649          | 0.3766   | 0.2263   |
| 2.2734        | 8.0   | 1512 | 2.0690          | 0.4726   | 0.3523   |


### Framework versions

- Transformers 5.16.1
- Pytorch 2.11.0+cu128
- Datasets 4.8.5
- Tokenizers 0.23.1
