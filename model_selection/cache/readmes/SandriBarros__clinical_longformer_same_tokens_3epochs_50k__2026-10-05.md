---
base_model: SandriBarros/clinical_longformer_same_tokens_2epochs_250k
tags:
- generated_from_trainer
model-index:
- name: clinical_longformer_same_tokens_3epochs_50k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_longformer_same_tokens_3epochs_50k

This model is a fine-tuned version of [SandriBarros/clinical_longformer_same_tokens_2epochs_250k](https://huggingface.co/SandriBarros/clinical_longformer_same_tokens_2epochs_250k) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3763

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
| 1.493         | 0.18  | 65   | 1.3790          |
| 1.5495        | 0.37  | 130  | 1.3815          |
| 1.5793        | 0.55  | 195  | 1.3888          |
| 1.5757        | 0.74  | 260  | 1.3644          |
| 1.3813        | 0.92  | 325  | 1.3763          |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
