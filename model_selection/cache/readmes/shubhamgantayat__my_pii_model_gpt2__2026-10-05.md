---
license: mit
base_model: openai-community/gpt2
tags:
- generated_from_trainer
model-index:
- name: my_pii_model_gpt2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my_pii_model_gpt2

This model is a fine-tuned version of [openai-community/gpt2](https://huggingface.co/openai-community/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0007

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0019        | 1.0   | 1532 | 0.0010          |
| 0.0012        | 2.0   | 3064 | 0.0008          |
| 0.001         | 3.0   | 4596 | 0.0007          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
