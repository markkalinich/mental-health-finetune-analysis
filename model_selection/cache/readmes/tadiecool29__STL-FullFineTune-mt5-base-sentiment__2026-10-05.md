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
- name: STL-FullFineTune-mt5-base-sentiment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# STL-FullFineTune-mt5-base-sentiment

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1416
- Accuracy: 0.6646
- Macro F1: 0.6506

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
- label_smoothing_factor: 0.05

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Macro F1 |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 15.2673       | 1.0   | 189  | 9.2069          | 0.0      | 0.0      |
| 1.7349        | 2.0   | 378  | 1.2640          | 0.3953   | 0.2513   |
| 1.3796        | 3.0   | 567  | 1.2343          | 0.5162   | 0.4961   |
| 1.2741        | 4.0   | 756  | 1.1625          | 0.6434   | 0.6279   |
| 1.2372        | 5.0   | 945  | 1.1462          | 0.6172   | 0.5825   |
| 1.1962        | 6.0   | 1134 | 1.1414          | 0.6633   | 0.6448   |
| 1.1813        | 7.0   | 1323 | 1.1426          | 0.6534   | 0.6349   |
| 1.1872        | 8.0   | 1512 | 1.1412          | 0.6633   | 0.6486   |
| 1.1780        | 9.0   | 1701 | 1.1417          | 0.6646   | 0.6506   |
| 1.1775        | 10.0  | 1890 | 1.1416          | 0.6646   | 0.6506   |


### Framework versions

- Transformers 5.16.1
- Pytorch 2.11.0+cu128
- Datasets 4.8.5
- Tokenizers 0.23.1
