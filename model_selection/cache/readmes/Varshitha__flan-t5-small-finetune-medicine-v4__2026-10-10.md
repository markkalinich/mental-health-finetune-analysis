---
license: apache-2.0
base_model: google/flan-t5-small
tags:
- text2textgeneration
- generated_from_trainer
metrics:
- rouge
model-index:
- name: flan-t5-small-finetune-medicine-v4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-small-finetune-medicine-v4

This model is a fine-tuned version of [google/flan-t5-small](https://huggingface.co/google/flan-t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7404
- Rouge1: 17.0034
- Rouge2: 4.9383
- Rougel: 16.8615
- Rougelsum: 16.6931

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| No log        | 1.0   | 5    | 2.8864          | 15.7685 | 5.117  | 15.7138 | 15.518    |
| No log        | 2.0   | 10   | 2.8754          | 15.7702 | 5.117  | 15.6758 | 15.5641   |
| No log        | 3.0   | 15   | 2.8556          | 15.9322 | 4.0564 | 15.9587 | 15.8195   |
| No log        | 4.0   | 20   | 2.8469          | 16.4117 | 4.9383 | 16.3008 | 16.2258   |
| No log        | 5.0   | 25   | 2.8380          | 17.2745 | 4.9383 | 17.2039 | 17.0175   |
| No log        | 6.0   | 30   | 2.8276          | 16.8416 | 5.6437 | 16.737  | 16.5215   |
| No log        | 7.0   | 35   | 2.8118          | 17.0703 | 4.9383 | 16.9715 | 16.7941   |
| No log        | 8.0   | 40   | 2.8010          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 9.0   | 45   | 2.7898          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 10.0  | 50   | 2.7783          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 11.0  | 55   | 2.7694          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 12.0  | 60   | 2.7617          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 13.0  | 65   | 2.7546          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 14.0  | 70   | 2.7478          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 15.0  | 75   | 2.7437          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 16.0  | 80   | 2.7417          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 17.0  | 85   | 2.7416          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 18.0  | 90   | 2.7409          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 19.0  | 95   | 2.7405          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |
| No log        | 20.0  | 100  | 2.7404          | 17.0034 | 4.9383 | 16.8615 | 16.6931   |


### Framework versions

- Transformers 4.31.0
- Pytorch 2.0.1+cu118
- Datasets 2.14.1
- Tokenizers 0.13.3
