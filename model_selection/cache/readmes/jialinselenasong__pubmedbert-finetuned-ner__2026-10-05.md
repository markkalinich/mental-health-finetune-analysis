---
license: apache-2.0
base_model: neuml/pubmedbert-base-embeddings
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pubmedbert-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmedbert-finetuned-ner

This model is a fine-tuned version of [neuml/pubmedbert-base-embeddings](https://huggingface.co/neuml/pubmedbert-base-embeddings) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4100
- Precision: 0.6458
- Recall: 0.6891
- F1: 0.6668
- Accuracy: 0.8570

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 305  | 0.4216          | 0.6399    | 0.6691 | 0.6542 | 0.8532   |
| 0.4885        | 2.0   | 610  | 0.4065          | 0.6374    | 0.6901 | 0.6627 | 0.8546   |
| 0.4885        | 3.0   | 915  | 0.4100          | 0.6458    | 0.6891 | 0.6668 | 0.8570   |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
