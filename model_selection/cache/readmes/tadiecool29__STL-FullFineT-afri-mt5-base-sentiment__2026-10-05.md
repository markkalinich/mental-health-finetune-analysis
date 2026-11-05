---
library_name: transformers
license: afl-3.0
base_model: masakhane/afri-mt5-base
tags:
- full-finetuning
- amharic
- sentiment-analysis
- single-task
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: STL-FullFineT-afri-mt5-base-sentiment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# STL-FullFineT-afri-mt5-base-sentiment

This model is a fine-tuned version of [masakhane/afri-mt5-base](https://huggingface.co/masakhane/afri-mt5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8686
- Accuracy: 0.6883
- Macro F1: 0.6773

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
| 6.4464        | 1.0   | 189  | 2.8518          | 0.3167   | 0.1388   |
| 2.0518        | 2.0   | 378  | 1.9034          | 0.6160   | 0.5980   |
| 1.9116        | 3.0   | 567  | 1.8464          | 0.6995   | 0.6891   |
| 1.8473        | 4.0   | 756  | 1.8529          | 0.6883   | 0.6851   |
| 1.8355        | 5.0   | 945  | 1.8394          | 0.6908   | 0.6823   |
| 1.7861        | 6.0   | 1134 | 1.8686          | 0.6883   | 0.6773   |


### Framework versions

- Transformers 5.16.1
- Pytorch 2.11.0+cu128
- Datasets 4.8.5
- Tokenizers 0.23.1
