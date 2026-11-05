---
library_name: transformers
license: apache-2.0
base_model: bert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mBERT-base-Symptom2Disease
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mBERT-base-Symptom2Disease

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5670
- Accuracy: 0.9567

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.7922792539563206e-05
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 37
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.7613        | 1.0   | 38   | 1.2744          | 0.62     |
| 0.8924        | 2.0   | 76   | 0.6954          | 0.8833   |
| 0.6003        | 3.0   | 114  | 0.6624          | 0.92     |
| 0.5268        | 4.0   | 152  | 0.5494          | 0.9667   |
| 0.4792        | 5.0   | 190  | 0.5403          | 0.97     |
| 0.4655        | 6.0   | 228  | 0.5765          | 0.95     |
| 0.4538        | 7.0   | 266  | 0.5674          | 0.9567   |
| 0.4517        | 8.0   | 304  | 0.5670          | 0.9567   |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
