---
base_model: nlpie/distil-clinicalbert
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: distil-clinicalbert-medical-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distil-clinicalbert-medical-text-classification

This model is a fine-tuned version of [nlpie/distil-clinicalbert](https://huggingface.co/nlpie/distil-clinicalbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8719
- Accuracy: 0.266
- Precision: 0.2357
- Recall: 0.266
- F1: 0.2427

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 2.5512        | 1.0   | 250  | 2.6302          | 0.335    | 0.1402    | 0.335  | 0.1911 |
| 2.0609        | 2.0   | 500  | 2.1857          | 0.357    | 0.2240    | 0.357  | 0.2474 |
| 1.9056        | 3.0   | 750  | 1.8964          | 0.321    | 0.2773    | 0.321  | 0.2812 |
| 1.5646        | 4.0   | 1000 | 1.8117          | 0.323    | 0.3183    | 0.323  | 0.2949 |
| 1.3789        | 5.0   | 1250 | 1.8869          | 0.302    | 0.2643    | 0.302  | 0.2701 |
| 1.3189        | 6.0   | 1500 | 1.8719          | 0.266    | 0.2357    | 0.266  | 0.2427 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
