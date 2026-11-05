---
license: apache-2.0
base_model: facebook/wav2vec2-base
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: fineturning-medical_data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fineturning-medical_data

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3803
- Wer: 0.2026

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 35
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.5432        | 5.08  | 500  | 0.5657          | 0.3742 |
| 0.3691        | 10.15 | 1000 | 0.4064          | 0.2665 |
| 0.2045        | 15.23 | 1500 | 0.4500          | 0.2437 |
| 0.1385        | 20.3  | 2000 | 0.4261          | 0.2285 |
| 0.1028        | 25.38 | 2500 | 0.3828          | 0.2093 |
| 0.0696        | 30.46 | 3000 | 0.3803          | 0.2026 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
