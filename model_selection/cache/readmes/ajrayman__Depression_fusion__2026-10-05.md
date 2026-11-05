---
library_name: transformers
tags:
- generated_from_trainer
model-index:
- name: Depression_fusion
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Depression_fusion

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0746
- Rmse: 0.2731
- Mae: 0.2175
- Corr: 0.4556

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 1234
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rmse   | Mae    | Corr   |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|
| No log        | 1.0   | 235  | 0.0666          | 0.2581 | 0.2106 | 0.5060 |
| No log        | 2.0   | 470  | 0.0663          | 0.2575 | 0.2094 | 0.5207 |
| 0.0767        | 3.0   | 705  | 0.0657          | 0.2562 | 0.2060 | 0.4956 |
| 0.0767        | 4.0   | 940  | 0.0693          | 0.2633 | 0.2086 | 0.4893 |
| 0.0478        | 5.0   | 1175 | 0.0746          | 0.2731 | 0.2175 | 0.4556 |


### Framework versions

- Transformers 4.44.1
- Pytorch 1.11.0
- Datasets 2.12.0
- Tokenizers 0.19.1
