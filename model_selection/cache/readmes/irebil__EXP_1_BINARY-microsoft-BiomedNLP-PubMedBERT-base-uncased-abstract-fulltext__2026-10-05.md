---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: EXP_1_BINARY-microsoft-BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# EXP_1_BINARY-microsoft-BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1990
- Precision: 0.8979
- Recall: 0.9153
- F1: 0.9065
- Accuracy: 0.9219

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
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2136        | 1.0   | 220  | 0.2065          | 0.8863    | 0.9244 | 0.9049 | 0.9196   |
| 0.2014        | 2.0   | 440  | 0.2028          | 0.8876    | 0.9279 | 0.9073 | 0.9216   |
| 0.1951        | 3.0   | 660  | 0.1990          | 0.8979    | 0.9153 | 0.9065 | 0.9219   |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.1+cu130
- Datasets 4.4.1
- Tokenizers 0.22.1
