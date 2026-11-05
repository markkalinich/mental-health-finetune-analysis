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
- name: EXP_5_MULTI_DISEASE_BIO_FULL-microsoft-BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# EXP_5_MULTI_DISEASE_BIO_FULL-microsoft-BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract-fulltext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1295
- Precision: 0.6948
- Recall: 0.6350
- F1: 0.6636
- Accuracy: 0.9657

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
| 0.1814        | 1.0   | 220  | 0.1587          | 0.6848    | 0.5259 | 0.5950 | 0.9612   |
| 0.1354        | 2.0   | 440  | 0.1330          | 0.7093    | 0.6002 | 0.6502 | 0.9652   |
| 0.122         | 3.0   | 660  | 0.1295          | 0.6948    | 0.6350 | 0.6636 | 0.9657   |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.1+cu130
- Datasets 4.4.1
- Tokenizers 0.22.1
