---
license: apache-2.0
base_model: NeuML/pubmedbert-base-embeddings
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pubmed-bert-all-deep
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmed-bert-all-deep

This model is a fine-tuned version of [NeuML/pubmedbert-base-embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9764
- Precision: 0.4738
- Recall: 0.4800
- F1: 0.4769
- Accuracy: 0.7380

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 363  | 1.1611          | 0.1988    | 0.1654 | 0.1806 | 0.6258   |
| 1.3011        | 2.0   | 726  | 1.0030          | 0.3355    | 0.3221 | 0.3287 | 0.6877   |
| 0.9032        | 3.0   | 1089 | 0.9300          | 0.4125    | 0.3563 | 0.3823 | 0.7095   |
| 0.9032        | 4.0   | 1452 | 0.8892          | 0.4466    | 0.4189 | 0.4323 | 0.7220   |
| 0.7036        | 5.0   | 1815 | 0.9079          | 0.4476    | 0.4530 | 0.4503 | 0.7257   |
| 0.5735        | 6.0   | 2178 | 0.9415          | 0.4651    | 0.4684 | 0.4667 | 0.7299   |
| 0.4796        | 7.0   | 2541 | 0.9484          | 0.4791    | 0.4558 | 0.4672 | 0.7324   |
| 0.4796        | 8.0   | 2904 | 0.9677          | 0.4673    | 0.4757 | 0.4715 | 0.7335   |
| 0.4197        | 9.0   | 3267 | 0.9810          | 0.4760    | 0.4791 | 0.4775 | 0.7361   |
| 0.3812        | 10.0  | 3630 | 0.9764          | 0.4738    | 0.4800 | 0.4769 | 0.7380   |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
