---
license: apache-2.0
base_model: google/vit-base-patch16-224-in21k
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: dental_classification_model_010424_1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dental_classification_model_010424_1

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5468
- Accuracy: 0.8293

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.9173        | 0.99  | 41   | 1.9026          | 0.2825   |
| 1.7055        | 2.0   | 83   | 1.6619          | 0.3882   |
| 1.5398        | 2.99  | 124  | 1.5061          | 0.4849   |
| 1.3415        | 4.0   | 166  | 1.3317          | 0.5801   |
| 1.1753        | 4.99  | 207  | 1.2437          | 0.5876   |
| 1.017         | 6.0   | 249  | 1.1052          | 0.6390   |
| 0.8724        | 6.99  | 290  | 0.9521          | 0.6873   |
| 0.8207        | 8.0   | 332  | 0.9114          | 0.7115   |
| 0.7706        | 8.99  | 373  | 0.8574          | 0.7130   |
| 0.6788        | 10.0  | 415  | 0.7974          | 0.7523   |
| 0.63          | 10.99 | 456  | 0.7611          | 0.7659   |
| 0.5633        | 12.0  | 498  | 0.7764          | 0.7553   |
| 0.5581        | 12.99 | 539  | 0.7370          | 0.7779   |
| 0.5117        | 14.0  | 581  | 0.6945          | 0.7689   |
| 0.4933        | 14.99 | 622  | 0.7066          | 0.7719   |
| 0.4787        | 16.0  | 664  | 0.6405          | 0.8006   |
| 0.4169        | 16.99 | 705  | 0.6443          | 0.8036   |
| 0.3756        | 18.0  | 747  | 0.5991          | 0.8187   |
| 0.3629        | 18.99 | 788  | 0.5774          | 0.8202   |
| 0.3719        | 20.0  | 830  | 0.5451          | 0.8369   |
| 0.4216        | 20.99 | 871  | 0.5623          | 0.8338   |
| 0.3739        | 22.0  | 913  | 0.5995          | 0.8066   |
| 0.3096        | 22.99 | 954  | 0.5330          | 0.8353   |
| 0.3002        | 24.0  | 996  | 0.5109          | 0.8323   |
| 0.3372        | 24.99 | 1037 | 0.5468          | 0.8293   |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
