---
library_name: transformers
license: cc0-1.0
base_model: bionlp/bluebert_pubmed_uncased_L-24_H-1024_A-16
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: medical-ner-bluebert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical-ner-bluebert

This model is a fine-tuned version of [bionlp/bluebert_pubmed_uncased_L-24_H-1024_A-16](https://huggingface.co/bionlp/bluebert_pubmed_uncased_L-24_H-1024_A-16) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0894
- Precision: 0.9365
- Recall: 0.9705
- F1: 0.9532
- Accuracy: 0.9810

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 90   | 0.7138          | 0.5501    | 0.6082 | 0.5777 | 0.7757   |
| No log        | 2.0   | 180  | 0.6697          | 0.5391    | 0.7574 | 0.6298 | 0.7863   |
| No log        | 3.0   | 270  | 0.4996          | 0.6284    | 0.8024 | 0.7048 | 0.8429   |
| No log        | 4.0   | 360  | 0.3957          | 0.6779    | 0.8332 | 0.7476 | 0.8760   |
| No log        | 5.0   | 450  | 0.2886          | 0.7603    | 0.8658 | 0.8096 | 0.9160   |
| 0.4932        | 6.0   | 540  | 0.2345          | 0.8026    | 0.8839 | 0.8413 | 0.9321   |
| 0.4932        | 7.0   | 630  | 0.2061          | 0.8290    | 0.9121 | 0.8686 | 0.9419   |
| 0.4932        | 8.0   | 720  | 0.1715          | 0.8537    | 0.9226 | 0.8868 | 0.9518   |
| 0.4932        | 9.0   | 810  | 0.1454          | 0.8701    | 0.9374 | 0.9025 | 0.9603   |
| 0.4932        | 10.0  | 900  | 0.1422          | 0.8857    | 0.9437 | 0.9137 | 0.9635   |
| 0.4932        | 11.0  | 990  | 0.1134          | 0.9081    | 0.9516 | 0.9293 | 0.9718   |
| 0.0935        | 12.0  | 1080 | 0.1147          | 0.9075    | 0.9582 | 0.9322 | 0.9722   |
| 0.0935        | 13.0  | 1170 | 0.1039          | 0.9165    | 0.9616 | 0.9385 | 0.9757   |
| 0.0935        | 14.0  | 1260 | 0.0978          | 0.9256    | 0.9658 | 0.9453 | 0.9774   |
| 0.0935        | 15.0  | 1350 | 0.0925          | 0.9283    | 0.9671 | 0.9473 | 0.9797   |
| 0.0935        | 16.0  | 1440 | 0.0873          | 0.9378    | 0.9679 | 0.9526 | 0.9813   |
| 0.0301        | 17.0  | 1530 | 0.0927          | 0.9334    | 0.9703 | 0.9515 | 0.9803   |
| 0.0301        | 18.0  | 1620 | 0.0903          | 0.9355    | 0.97   | 0.9525 | 0.9804   |
| 0.0301        | 19.0  | 1710 | 0.0890          | 0.9373    | 0.9711 | 0.9539 | 0.9811   |
| 0.0301        | 20.0  | 1800 | 0.0894          | 0.9365    | 0.9705 | 0.9532 | 0.9810   |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Datasets 3.1.0
- Tokenizers 0.20.3
