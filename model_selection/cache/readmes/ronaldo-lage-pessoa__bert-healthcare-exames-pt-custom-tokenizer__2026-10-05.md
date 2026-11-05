---
license: mit
base_model: neuralmind/bert-base-portuguese-cased
tags:
- generated_from_trainer
model-index:
- name: bert-healthcare-exames-pt-custom-tokenizer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-healthcare-exames-pt-custom-tokenizer

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5458

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
- train_batch_size: 40
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.989         | 0.44  | 500  | 1.1229          |
| 0.971         | 0.89  | 1000 | 0.8171          |
| 0.7603        | 1.33  | 1500 | 0.6829          |
| 0.6537        | 1.78  | 2000 | 0.6054          |
| 0.5908        | 2.22  | 2500 | 0.5811          |
| 0.5555        | 2.67  | 3000 | 0.5458          |


### Framework versions

- Transformers 4.36.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.15.2
