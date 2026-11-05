---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
datasets:
- ncbi_disease
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: ner-model-BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: ncbi_disease
      type: ncbi_disease
      config: ncbi_disease
      split: validation
      args: ncbi_disease
    metrics:
    - name: Precision
      type: precision
      value: 0.8267564966313763
    - name: Recall
      type: recall
      value: 0.8947916666666667
    - name: F1
      type: f1
      value: 0.8594297148574287
    - name: Accuracy
      type: accuracy
      value: 0.9847736457525411
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ner-model-BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on the ncbi_disease dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Precision: 0.8268
- Recall: 0.8948
- F1: 0.8594
- Accuracy: 0.9848

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
- eval_batch_size: 20
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0465        | 1.0   | 340  | 0.0537          | 0.7949    | 0.8374 | 0.8156 | 0.9836   |
| 0.0320        | 2.0   | 680  | 0.0466          | 0.8232    | 0.8640 | 0.8431 | 0.9856   |
| 0.0182        | 3.0   | 1020 | 0.0541          | 0.8199    | 0.8679 | 0.8432 | 0.9854   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 2.21.0
- Tokenizers 0.22.2
