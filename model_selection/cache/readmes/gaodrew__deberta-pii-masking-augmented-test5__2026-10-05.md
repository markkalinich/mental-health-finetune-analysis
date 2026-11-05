---
library_name: transformers
license: mit
base_model: microsoft/deberta-v3-large
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: deberta-pii-masking-augmented-test5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-pii-masking-augmented-test5

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0360
- Precision: 0.9402
- Recall: 0.9557
- F1: 0.9479
- Accuracy: 0.9891

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.6188        | 0.0305 | 500  | 0.3788          | 0.5431    | 0.6547 | 0.5937 | 0.9030   |
| 0.1746        | 0.0609 | 1000 | 0.1576          | 0.7686    | 0.8381 | 0.8019 | 0.9565   |
| 0.0857        | 0.0914 | 1500 | 0.1094          | 0.8148    | 0.8787 | 0.8455 | 0.9669   |
| 0.0624        | 0.1219 | 2000 | 0.0882          | 0.8475    | 0.8979 | 0.8720 | 0.9728   |
| 0.0512        | 0.1524 | 2500 | 0.0610          | 0.8834    | 0.9161 | 0.8994 | 0.9811   |
| 0.0445        | 0.1828 | 3000 | 0.0584          | 0.8968    | 0.9216 | 0.9090 | 0.9814   |
| 0.0398        | 0.2133 | 3500 | 0.0545          | 0.9097    | 0.9324 | 0.9209 | 0.9836   |
| 0.0355        | 0.2438 | 4000 | 0.0500          | 0.9125    | 0.9342 | 0.9232 | 0.9845   |
| 0.0337        | 0.2743 | 4500 | 0.0477          | 0.9068    | 0.9355 | 0.9209 | 0.9843   |
| 0.0309        | 0.3047 | 5000 | 0.0489          | 0.9214    | 0.9408 | 0.9310 | 0.9854   |
| 0.0284        | 0.3352 | 5500 | 0.0444          | 0.9173    | 0.9433 | 0.9301 | 0.9861   |
| 0.0278        | 0.3657 | 6000 | 0.0423          | 0.9247    | 0.9416 | 0.9331 | 0.9865   |
| 0.0258        | 0.3962 | 6500 | 0.0410          | 0.9291    | 0.9471 | 0.9380 | 0.9873   |
| 0.0242        | 0.4266 | 7000 | 0.0375          | 0.9301    | 0.9499 | 0.9399 | 0.9881   |
| 0.0241        | 0.4571 | 7500 | 0.0380          | 0.9321    | 0.9500 | 0.9410 | 0.9882   |
| 0.0217        | 0.4876 | 8000 | 0.0347          | 0.9404    | 0.9545 | 0.9474 | 0.9890   |
| 0.0207        | 0.5181 | 8500 | 0.0335          | 0.9360    | 0.9526 | 0.9442 | 0.9892   |
| 0.0204        | 0.5485 | 9000 | 0.0366          | 0.9364    | 0.9542 | 0.9452 | 0.9888   |
| 0.019         | 0.5790 | 9500 | 0.0362          | 0.9355    | 0.9534 | 0.9444 | 0.9887   |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu124
- Datasets 3.1.0
- Tokenizers 0.20.3
