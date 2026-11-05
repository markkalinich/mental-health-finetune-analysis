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
- name: NHS-pubmedbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NHS-pubmedbert

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6667
- Accuracy: 0.8177
- Precision: 0.8190
- Recall: 0.8177
- F1: 0.8143

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
| 0.0827        | 1.0   | 397  | 0.4385          | 0.7994   | 0.8128    | 0.7994 | 0.8011 |
| 0.0149        | 2.0   | 794  | 0.4484          | 0.8227   | 0.8232    | 0.8227 | 0.8229 |
| 0.0027        | 3.0   | 1191 | 0.6667          | 0.8177   | 0.8190    | 0.8177 | 0.8143 |


### Framework versions

- Transformers 4.35.2
- Pytorch 2.1.0+cu121
- Datasets 2.15.0
- Tokenizers 0.15.0
