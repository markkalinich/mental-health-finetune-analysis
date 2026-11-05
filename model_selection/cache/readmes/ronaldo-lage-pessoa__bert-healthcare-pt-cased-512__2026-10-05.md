---
license: mit
base_model: neuralmind/bert-base-portuguese-cased
tags:
- generated_from_trainer
model-index:
- name: bert-healthcare-pt-cased-512
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-healthcare-pt-cased-512

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3841

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.2563        | 2.84  | 500  | 0.5272          |
| 0.4757        | 5.69  | 1000 | 0.3841          |


### Framework versions

- Transformers 4.36.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.15.2
