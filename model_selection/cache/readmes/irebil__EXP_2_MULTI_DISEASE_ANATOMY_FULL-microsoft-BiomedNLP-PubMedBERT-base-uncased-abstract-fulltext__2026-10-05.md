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
- name: EXP_4_MULTI_DISEASE_ANATOMY_FULL-microsoft-BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# EXP_4_MULTI_DISEASE_ANATOMY_FULL-microsoft-BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1025
- Precision: 0.7177
- Recall: 0.7110
- F1: 0.7143
- Accuracy: 0.9718

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
| 0.1365        | 1.0   | 220  | 0.1269          | 0.6794    | 0.6365 | 0.6572 | 0.9678   |
| 0.1028        | 2.0   | 440  | 0.1061          | 0.7142    | 0.6852 | 0.6994 | 0.9709   |
| 0.0937        | 3.0   | 660  | 0.1025          | 0.7177    | 0.7110 | 0.7143 | 0.9718   |


### Framework versions

- Transformers 4.57.2
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
