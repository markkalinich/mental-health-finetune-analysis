---
license: apache-2.0
base_model: google/flan-t5-small
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: flan-t5-small-medical_model_2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-small-medical_model_2

This model is a fine-tuned version of [google/flan-t5-small](https://huggingface.co/google/flan-t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9215
- Rouge1: 0.1439
- Rouge2: 0.0872
- Rougel: 0.1311
- Rougelsum: 0.1383

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 2.4473        | 1.0   | 1436 | 2.0780          | 0.1387 | 0.0818 | 0.1261 | 0.1332    |
| 2.2213        | 2.0   | 2872 | 1.9935          | 0.1431 | 0.0865 | 0.1304 | 0.1374    |
| 2.1841        | 3.0   | 4308 | 1.9510          | 0.1438 | 0.0871 | 0.1310 | 0.1381    |
| 2.1274        | 4.0   | 5744 | 1.9282          | 0.1443 | 0.0874 | 0.1315 | 0.1388    |
| 2.092         | 5.0   | 7180 | 1.9215          | 0.1439 | 0.0872 | 0.1311 | 0.1383    |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.0+cu121
- Datasets 2.16.1
- Tokenizers 0.15.1
