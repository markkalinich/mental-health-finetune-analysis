---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-large-uncased-abstract
tags:
- generated_from_trainer
datasets:
- source_data
metrics:
- precision
- recall
- f1
model-index:
- name: SourceData_NER_v1_0_0_PubMedBERT_large
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
      value: 0.8202296075899624
    - name: Recall
      type: recall
      value: 0.8535064404007361
    - name: F1
      type: f1
      value: 0.8365372228504359
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SourceData_NER_v1_0_0_PubMedBERT_large

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-large-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-large-uncased-abstract) on the source_data dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1352
- Accuracy Score: 0.9575
- Precision: 0.8202
- Recall: 0.8535
- F1: 0.8365

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
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Use adafactor and the args are:
No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 2.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy Score | Precision | Recall | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:---------:|:------:|:------:|
| 0.108         | 0.9994 | 863  | 0.1354          | 0.9557         | 0.8133    | 0.8463 | 0.8294 |
| 0.0778        | 1.9988 | 1726 | 0.1352          | 0.9575         | 0.8202    | 0.8535 | 0.8365 |


### Framework versions

- Transformers 4.46.3
- Pytorch 1.13.1+cu117
- Datasets 3.1.0
- Tokenizers 0.20.3
