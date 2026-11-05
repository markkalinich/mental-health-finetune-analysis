---
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: NHS-pubmedbert-multi
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NHS-pubmedbert-multi

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8814
- Accuracy: 0.7148
- Precision: 0.7181
- Recall: 0.7148
- F1: 0.7151

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.0855        | 1.0   | 397  | 0.7355          | 0.7192   | 0.7254    | 0.7192 | 0.7212 |
| 0.0541        | 2.0   | 794  | 0.7926          | 0.7180   | 0.7181    | 0.7180 | 0.7036 |
| 0.2545        | 3.0   | 1191 | 0.8814          | 0.7148   | 0.7181    | 0.7148 | 0.7151 |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2
