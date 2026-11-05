---
base_model: camilon/clinical_longformer_same_tokens_1epochs_200k
tags:
- generated_from_trainer
model-index:
- name: clinical_longformer_same_tokens_1epochs_250k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_longformer_same_tokens_1epochs_250k

This model is a fine-tuned version of [camilon/clinical_longformer_same_tokens_1epochs_200k](https://huggingface.co/camilon/clinical_longformer_same_tokens_1epochs_200k) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5640

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
- train_batch_size: 2
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1500
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.7984        | 0.16  | 65   | 1.6415          |
| 1.8332        | 0.31  | 130  | 1.6324          |
| 1.7428        | 0.47  | 195  | 1.6149          |
| 1.8757        | 0.63  | 260  | 1.5976          |
| 1.7874        | 0.78  | 325  | 1.5924          |
| 1.8166        | 0.94  | 390  | 1.5640          |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
