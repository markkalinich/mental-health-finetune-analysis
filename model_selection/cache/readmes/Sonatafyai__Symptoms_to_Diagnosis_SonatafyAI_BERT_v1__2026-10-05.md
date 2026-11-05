---
license: apache-2.0
base_model: bert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: Symptoms_to_Diagnosis_SonatafyAI_BERT_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Symptoms_to_Diagnosis_SonatafyAI_BERT_v1

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6203
- Accuracy: 0.9198

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 54   | 2.7261          | 0.2123   |
| No log        | 2.0   | 108  | 2.2144          | 0.5283   |
| No log        | 3.0   | 162  | 1.7385          | 0.6698   |
| No log        | 4.0   | 216  | 1.3686          | 0.7925   |
| No log        | 5.0   | 270  | 1.1194          | 0.8302   |
| No log        | 6.0   | 324  | 0.9123          | 0.8632   |
| No log        | 7.0   | 378  | 0.7822          | 0.9009   |
| No log        | 8.0   | 432  | 0.6871          | 0.9009   |
| No log        | 9.0   | 486  | 0.6415          | 0.9104   |
| 1.4504        | 10.0  | 540  | 0.6203          | 0.9198   |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
