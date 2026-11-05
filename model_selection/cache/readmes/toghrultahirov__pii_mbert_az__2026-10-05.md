---
license: apache-2.0
base_model: google-bert/bert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii_mbert_az
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii_mbert_az

This model is a fine-tuned version of [google-bert/bert-base-multilingual-cased](https://huggingface.co/google-bert/bert-base-multilingual-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1319
- Precision: 0.8726
- Recall: 0.9026
- F1: 0.8874
- Accuracy: 0.9619

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: reduce_lr_on_plateau
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 313  | 0.1464          | 0.8797    | 0.8615 | 0.8705 | 0.9587   |
| 0.2128        | 2.0   | 626  | 0.1319          | 0.8726    | 0.9026 | 0.8874 | 0.9619   |
| 0.2128        | 3.0   | 939  | 0.1461          | 0.8689    | 0.8924 | 0.8805 | 0.9596   |
| 0.0783        | 4.0   | 1252 | 0.1529          | 0.8837    | 0.9049 | 0.8942 | 0.9620   |
| 0.0443        | 5.0   | 1565 | 0.1921          | 0.8657    | 0.9157 | 0.8900 | 0.9615   |
| 0.0443        | 6.0   | 1878 | 0.1647          | 0.8975    | 0.9224 | 0.9098 | 0.9685   |
| 0.0201        | 7.0   | 2191 | 0.1725          | 0.8904    | 0.9183 | 0.9041 | 0.9674   |
| 0.0098        | 8.0   | 2504 | 0.1766          | 0.8917    | 0.9199 | 0.9056 | 0.9682   |
| 0.0098        | 9.0   | 2817 | 0.1756          | 0.8926    | 0.9202 | 0.9062 | 0.9686   |
| 0.007         | 10.0  | 3130 | 0.1763          | 0.8916    | 0.9189 | 0.9051 | 0.9684   |
| 0.007         | 11.0  | 3443 | 0.1772          | 0.8907    | 0.9183 | 0.9043 | 0.9682   |
| 0.007         | 12.0  | 3756 | 0.1773          | 0.8895    | 0.9173 | 0.9032 | 0.9680   |
| 0.0067        | 13.0  | 4069 | 0.1775          | 0.8892    | 0.9170 | 0.9029 | 0.9680   |
| 0.0067        | 14.0  | 4382 | 0.1775          | 0.8897    | 0.9170 | 0.9032 | 0.9679   |
| 0.0062        | 15.0  | 4695 | 0.1775          | 0.8897    | 0.9170 | 0.9032 | 0.9679   |


### Framework versions

- Transformers 4.41.0
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
