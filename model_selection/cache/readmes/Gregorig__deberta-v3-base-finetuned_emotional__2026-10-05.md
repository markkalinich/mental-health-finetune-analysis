---
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: deberta-v3-base-finetuned_emotional
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-base-finetuned_emotional

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9584
- Accuracy: 0.605
- F1: 0.5937

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 1.2964        | 1.0   | 26   | 1.1782          | 0.45     | 0.3535 |
| 1.1059        | 2.0   | 52   | 1.0207          | 0.505    | 0.4339 |
| 0.9256        | 3.0   | 78   | 0.9845          | 0.57     | 0.5379 |
| 0.8308        | 4.0   | 104  | 0.9633          | 0.595    | 0.5645 |
| 0.7769        | 5.0   | 130  | 0.9584          | 0.605    | 0.5937 |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Tokenizers 0.19.1
