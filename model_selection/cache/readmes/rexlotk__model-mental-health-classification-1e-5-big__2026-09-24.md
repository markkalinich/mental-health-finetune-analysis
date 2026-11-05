---
license: mit
base_model: FacebookAI/xlm-roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: model-mental-health-classification-1e-5-big
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model-mental-health-classification-1e-5-big

This model is a fine-tuned version of [FacebookAI/xlm-roberta-base](https://huggingface.co/FacebookAI/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1832
- Accuracy: 0.5738

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
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.1884        | 1.0   | 5254 | 1.1832          | 0.5738   |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
