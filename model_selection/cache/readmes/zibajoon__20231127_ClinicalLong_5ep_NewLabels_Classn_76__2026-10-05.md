---
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: 20231127_ClinicalLong_5ep_NewLabels
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 20231127_ClinicalLong_5ep_NewLabels

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1204
- Accuracy: 0.76

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
- train_batch_size: 12
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 101  | 2.3747          | 0.35     |
| No log        | 2.0   | 202  | 1.6577          | 0.53     |
| No log        | 3.0   | 303  | 1.2947          | 0.67     |
| No log        | 4.0   | 404  | 1.1553          | 0.69     |
| 1.344         | 5.0   | 505  | 1.1204          | 0.76     |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.0.1+cu118
- Datasets 2.10.1
- Tokenizers 0.14.1
