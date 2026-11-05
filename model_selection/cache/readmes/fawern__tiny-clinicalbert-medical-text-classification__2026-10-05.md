---
license: mit
base_model: nlpie/tiny-clinicalbert
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: tiny-clinicalbert-medical-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tiny-clinicalbert-medical-text-classification

This model is a fine-tuned version of [nlpie/tiny-clinicalbert](https://huggingface.co/nlpie/tiny-clinicalbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1588
- Accuracy: 0.236
- Precision: 0.2048
- Recall: 0.236
- F1: 0.2109

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
| 2.9902        | 1.0   | 250  | 3.0201          | 0.274    | 0.0880    | 0.274  | 0.1318 |
| 2.4558        | 2.0   | 500  | 2.6033          | 0.341    | 0.1392    | 0.341  | 0.1922 |
| 2.4627        | 3.0   | 750  | 2.4332          | 0.368    | 0.2003    | 0.368  | 0.2252 |
| 2.2983        | 4.0   | 1000 | 2.3126          | 0.365    | 0.2212    | 0.365  | 0.2495 |
| 2.1395        | 5.0   | 1250 | 2.2385          | 0.349    | 0.2100    | 0.349  | 0.2518 |
| 1.8919        | 6.0   | 1500 | 2.1892          | 0.339    | 0.2176    | 0.339  | 0.2490 |
| 1.9892        | 7.0   | 1750 | 2.1364          | 0.336    | 0.2310    | 0.336  | 0.2643 |
| 1.8569        | 8.0   | 2000 | 2.1441          | 0.321    | 0.2316    | 0.321  | 0.2532 |
| 1.9182        | 9.0   | 2250 | 2.1263          | 0.309    | 0.2185    | 0.309  | 0.2417 |
| 1.6594        | 10.0  | 2500 | 2.1234          | 0.262    | 0.2180    | 0.262  | 0.2245 |
| 1.5966        | 11.0  | 2750 | 2.1176          | 0.256    | 0.2149    | 0.256  | 0.2197 |
| 1.6185        | 12.0  | 3000 | 2.1578          | 0.243    | 0.2126    | 0.243  | 0.2140 |
| 1.3881        | 13.0  | 3250 | 2.1588          | 0.236    | 0.2048    | 0.236  | 0.2109 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
