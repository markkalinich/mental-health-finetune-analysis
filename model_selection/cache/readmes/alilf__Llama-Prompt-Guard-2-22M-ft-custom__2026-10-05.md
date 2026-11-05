---
library_name: transformers
base_model: HooshvareLab/bert-base-parsbert-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: Llama-Prompt-Guard-2-22M-ft-custom
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Llama-Prompt-Guard-2-22M-ft-custom

This model is a fine-tuned version of [HooshvareLab/bert-base-parsbert-uncased](https://huggingface.co/HooshvareLab/bert-base-parsbert-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1352
- Accuracy: 1.0
- Precision: 1.0000
- Recall: 1.0000
- F1: 1.0000

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
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 8    | 0.3232          | 0.9667   | 0.9500    | 1.0000 | 0.9744 |
| No log        | 2.0   | 16   | 0.1534          | 1.0      | 1.0000    | 1.0000 | 1.0000 |
| No log        | 3.0   | 24   | 0.1194          | 1.0      | 1.0000    | 1.0000 | 1.0000 |


### Framework versions

- Transformers 4.53.3
- Pytorch 2.6.0+cu124
- Datasets 4.4.1
- Tokenizers 0.21.2
