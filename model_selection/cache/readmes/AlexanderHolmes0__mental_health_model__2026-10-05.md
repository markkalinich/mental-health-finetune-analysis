---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mental_health_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental_health_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6755
- Accuracy: 0.7277

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |  Accuracy |
|:-------------:|:-----:|:----:|:--------:|:---------------:|
| No log        | 1.0   | 270  | 0.6665   | 0.7627          |
| 0.6949        | 2.0   | 540  | 0.6968   | 0.6960          |
| 0.6949        | 3.0   | 810  | 0.7038   | 0.6750          |
| 0.5696        | 4.0   | 1080 | 0.7185   | 0.6674          |
| 0.5696        | 5.0   | 1350 | 0.7136   | 0.6607          |
| 0.49          | 6.0   | 1620 | 0.7206   | 0.6531          |
| 0.49          | 7.0   | 1890 | 0.7228   | 0.6543          |
| 0.4287        | 8.0   | 2160 | 0.7250   | 0.6560          |
| 0.4287        | 9.0   | 2430 | 0.6747   | 0.7239          |
| 0.3996        | 10.0  | 2700 | 0.6755   | 0.7277          |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.17.0
- Tokenizers 0.15.2
