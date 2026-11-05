---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: brand-safety-model-updated
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# brand-safety-model-updated

This model is a fine-tuned version of [distilbert/distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4738
- Accuracy: 0.8669

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
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.5713        | 1.0   | 112  | 1.4436          | 0.7101   |
| 0.8978        | 2.0   | 224  | 0.8602          | 0.7854   |
| 0.6488        | 3.0   | 336  | 0.6759          | 0.8337   |
| 0.5417        | 4.0   | 448  | 0.5690          | 0.8539   |
| 0.4874        | 5.0   | 560  | 0.5204          | 0.8624   |
| 0.3607        | 6.0   | 672  | 0.4899          | 0.8657   |
| 0.3392        | 7.0   | 784  | 0.4799          | 0.8657   |
| 0.2559        | 8.0   | 896  | 0.4738          | 0.8669   |
| 0.2255        | 9.0   | 1008 | 0.4983          | 0.8584   |
| 0.1489        | 10.0  | 1120 | 0.5045          | 0.8590   |
| 0.1617        | 11.0  | 1232 | 0.4948          | 0.8584   |
| 0.1446        | 12.0  | 1344 | 0.4925          | 0.8629   |
| 0.1381        | 13.0  | 1456 | 0.5027          | 0.8624   |
| 0.1385        | 14.0  | 1568 | 0.4958          | 0.8612   |
| 0.1283        | 15.0  | 1680 | 0.4996          | 0.8590   |


### Framework versions

- Transformers 4.46.3
- Pytorch 2.4.0
- Datasets 2.20.0
- Tokenizers 0.20.3
