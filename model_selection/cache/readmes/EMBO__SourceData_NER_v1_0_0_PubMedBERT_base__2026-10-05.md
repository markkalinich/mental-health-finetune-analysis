---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract
tags:
- generated_from_trainer
datasets:
- source_data
metrics:
- precision
- recall
- f1
model-index:
- name: SourceData_NER_v1_0_0_PubMedBERT_base
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: source_data
      type: source_data
      config: NER
      split: validation
      args: NER
    metrics:
    - name: Precision
      type: precision
      value: 0.8140302498537645
    - name: Recall
      type: recall
      value: 0.8535940649005462
    - name: F1
      type: f1
      value: 0.8333428384042887
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SourceData_NER_v1_0_0_PubMedBERT_base

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) on the source_data dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1432
- Accuracy Score: 0.9557
- Precision: 0.8140
- Recall: 0.8536
- F1: 0.8333

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 64
- eval_batch_size: 128
- seed: 42
- optimizer: Use adafactor and the args are:
No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy Score | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:---------:|:------:|:------:|
| 0.1092        | 1.0   | 864  | 0.1403          | 0.9520         | 0.8061    | 0.8293 | 0.8175 |
| 0.075         | 2.0   | 1728 | 0.1432          | 0.9557         | 0.8140    | 0.8536 | 0.8333 |


### Framework versions

- Transformers 4.46.3
- Pytorch 1.13.1+cu117
- Datasets 3.1.0
- Tokenizers 0.20.3
