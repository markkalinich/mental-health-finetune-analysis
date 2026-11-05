---
license: apache-2.0
base_model: jonatasgrosman/wav2vec2-xls-r-1b-portuguese
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: wav2vec2-xls-r-1b-medical-domain
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-1b-medical-domain

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-xls-r-1b-portuguese](https://huggingface.co/jonatasgrosman/wav2vec2-xls-r-1b-portuguese) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5363
- Wer: 0.7022

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
- train_batch_size: 2
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Wer    |
|:-------------:|:-------:|:----:|:---------------:|:------:|
| No log        | 9.9379  | 200  | 0.2631          | 0.3790 |
| 1.2151        | 19.8758 | 400  | 0.5363          | 0.7022 |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.1.2+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
