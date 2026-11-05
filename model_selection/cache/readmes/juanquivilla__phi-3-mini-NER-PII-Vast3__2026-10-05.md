---
license: mit
base_model: microsoft/Phi-3-mini-4k-instruct
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: phi-3-mini-NER-PII-Vast3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# phi-3-mini-NER-PII-Vast3

This model is a fine-tuned version of [microsoft/Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1122
- Precision: 0.6826
- Recall: 0.8382
- F1: 0.7524
- Accuracy: 0.9697

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Accuracy | F1     | Validation Loss | Precision | Recall |
|:-------------:|:-----:|:-----:|:--------:|:------:|:---------------:|:---------:|:------:|
| 0.1017        | 1.0   | 11105 | 0.9693   | 0.7506 | 0.1123          | 0.6807    | 0.8364 |
| 0.0782        | 2.0   | 22210 | 0.1119   | 0.6819 | 0.8382          | 0.7520    | 0.9697 |
| 0.0944        | 3.0   | 33315 | 0.1122   | 0.6826 | 0.8382          | 0.7524    | 0.9697 |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0
- Datasets 2.19.1
- Tokenizers 0.19.1
