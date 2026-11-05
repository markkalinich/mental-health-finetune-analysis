---
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Fine_tune_PubMedBert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Fine_tune_PubMedBert

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4669
- Precision: 0.6359
- Recall: 0.7044
- F1: 0.6684
- Accuracy: 0.8802

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 11   | 0.8690          | 0.3548    | 0.0401 | 0.0721 | 0.7691   |
| No log        | 2.0   | 22   | 0.6036          | 0.6005    | 0.4635 | 0.5232 | 0.8468   |
| No log        | 3.0   | 33   | 0.4788          | 0.6160    | 0.5912 | 0.6034 | 0.8678   |
| No log        | 4.0   | 44   | 0.4621          | 0.5331    | 0.6898 | 0.6014 | 0.8611   |
| No log        | 5.0   | 55   | 0.4319          | 0.5795    | 0.6916 | 0.6306 | 0.8681   |
| No log        | 6.0   | 66   | 0.4444          | 0.5754    | 0.7099 | 0.6356 | 0.8694   |
| No log        | 7.0   | 77   | 0.4472          | 0.6069    | 0.7099 | 0.6543 | 0.8756   |
| No log        | 8.0   | 88   | 0.4556          | 0.6227    | 0.6898 | 0.6545 | 0.8786   |
| No log        | 9.0   | 99   | 0.4613          | 0.6118    | 0.7190 | 0.6611 | 0.8767   |
| No log        | 10.0  | 110  | 0.4669          | 0.6359    | 0.7044 | 0.6684 | 0.8802   |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu118
- Datasets 2.15.0
- Tokenizers 0.15.0
