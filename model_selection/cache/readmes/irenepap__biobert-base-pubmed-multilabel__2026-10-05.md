---
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: biobert-base-pubmed-multilabel
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biobert-base-pubmed-multilabel

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2677
- Precision: 0.9044
- Recall: 0.8528
- F1: 0.8778

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|
| 0.3373        | 0.2   | 500  | 0.2859          | 0.9093    | 0.8006 | 0.8515 |
| 0.2781        | 0.4   | 1000 | 0.2748          | 0.8972    | 0.8388 | 0.8670 |
| 0.269         | 0.6   | 1500 | 0.2639          | 0.9026    | 0.8405 | 0.8705 |
| 0.2598        | 0.81  | 2000 | 0.2610          | 0.9037    | 0.8435 | 0.8726 |
| 0.2543        | 1.01  | 2500 | 0.2559          | 0.9052    | 0.8494 | 0.8764 |
| 0.2191        | 1.21  | 3000 | 0.2554          | 0.9091    | 0.8437 | 0.8752 |
| 0.2217        | 1.41  | 3500 | 0.2620          | 0.8917    | 0.8676 | 0.8795 |
| 0.2232        | 1.61  | 4000 | 0.2529          | 0.9070    | 0.8470 | 0.8759 |
| 0.2256        | 1.81  | 4500 | 0.2567          | 0.9231    | 0.8176 | 0.8671 |
| 0.2191        | 2.02  | 5000 | 0.2591          | 0.8936    | 0.8731 | 0.8832 |
| 0.1744        | 2.22  | 5500 | 0.2674          | 0.8978    | 0.8631 | 0.8801 |
| 0.1745        | 2.42  | 6000 | 0.2736          | 0.8974    | 0.8566 | 0.8766 |
| 0.1749        | 2.62  | 6500 | 0.2677          | 0.9044    | 0.8528 | 0.8778 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
