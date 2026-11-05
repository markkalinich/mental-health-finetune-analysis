---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: Depression_Detection_Model_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Depression_Detection_Model_v2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0711
- Accuracy: 0.9825

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

https://github.com/DoryDing/Depression_Detection_Dataset.git

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 376  | 0.0954          | 0.9683   |
| 0.1028        | 2.0   | 752  | 0.1432          | 0.9683   |
| 0.0364        | 3.0   | 1128 | 0.0711          | 0.9825   |
| 0.0139        | 4.0   | 1504 | 0.1701          | 0.97     |
| 0.0139        | 5.0   | 1880 | 0.1093          | 0.9808   |
| 0.0059        | 6.0   | 2256 | 0.1272          | 0.9775   |


### Framework versions

- Transformers 4.31.0
- Pytorch 1.13.1
- Datasets 2.14.0
- Tokenizers 0.13.3
