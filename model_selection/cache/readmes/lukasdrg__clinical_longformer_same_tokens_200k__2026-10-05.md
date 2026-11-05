---
base_model: lukasdrg/clinical_longformer_same_tokens_180k
tags:
- generated_from_trainer
model-index:
- name: clinical_longformer_same_tokens_200k
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical_longformer_same_tokens_200k

This model is a fine-tuned version of [lukasdrg/clinical_longformer_same_tokens_180k](https://huggingface.co/lukasdrg/clinical_longformer_same_tokens_180k) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9880

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
| 2.1167        | 0.46  | 65   | 1.9521          |
| 2.2993        | 0.92  | 130  | 1.9880          |


### Framework versions

- Transformers 4.35.0
- Pytorch 2.1.0+cu118
- Datasets 2.14.6
- Tokenizers 0.14.1
