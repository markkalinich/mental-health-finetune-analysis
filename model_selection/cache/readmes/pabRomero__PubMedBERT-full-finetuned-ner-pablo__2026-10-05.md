---
library_name: transformers
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
- name: PubMedBERT-full-finetuned-ner-pablo
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# PubMedBERT-full-finetuned-ner-pablo

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the n2c2 2018 dataset for the paper https://arxiv.org/abs/2409.19467.
It achieves the following results on the evaluation set:
- Loss: 0.0712
- Precision: 0.8087
- Recall: 0.7954
- F1: 0.8020
- Accuracy: 0.9781

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
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 231  | 0.0934          | 0.7464    | 0.7652 | 0.7557 | 0.9730   |
| No log        | 2.0   | 462  | 0.0730          | 0.7975    | 0.7915 | 0.7945 | 0.9774   |
| 0.2789        | 3.0   | 693  | 0.0713          | 0.8075    | 0.7924 | 0.7999 | 0.9777   |
| 0.2789        | 4.0   | 924  | 0.0712          | 0.8087    | 0.7954 | 0.8020 | 0.9781   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.1+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
