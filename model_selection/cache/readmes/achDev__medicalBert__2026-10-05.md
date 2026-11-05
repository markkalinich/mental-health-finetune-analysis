---
base_model: aubmindlab/bert-base-arabertv2
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: medicalBert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medicalBert

This model is a fine-tuned version of [aubmindlab/bert-base-arabertv2](https://huggingface.co/aubmindlab/bert-base-arabertv2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0432
- Accuracy: 1.0

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 19   | 1.3351          | 0.6579   |
| No log        | 2.0   | 38   | 0.7920          | 0.8289   |
| No log        | 3.0   | 57   | 0.4334          | 0.8684   |
| No log        | 4.0   | 76   | 0.2400          | 0.9605   |
| No log        | 5.0   | 95   | 0.1408          | 0.9868   |
| No log        | 6.0   | 114  | 0.1014          | 1.0      |
| No log        | 7.0   | 133  | 0.0681          | 1.0      |
| No log        | 8.0   | 152  | 0.0478          | 1.0      |
| No log        | 9.0   | 171  | 0.0442          | 1.0      |
| No log        | 10.0  | 190  | 0.0432          | 1.0      |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
