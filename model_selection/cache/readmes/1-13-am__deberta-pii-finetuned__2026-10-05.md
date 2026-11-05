---
license: mit
base_model: microsoft/deberta-v3-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
model-index:
- name: deberta-pii-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-pii-finetuned

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0065
- F Beta: 0.9611
- Precision: 0.9932
- Recall: 0.9598

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
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F Beta | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:------:|:---------:|:------:|
| 0.0291        | 0.46  | 300  | 0.0104          | 0.9756 | 0.9854    | 0.9752 |
| 0.0062        | 0.93  | 600  | 0.0041          | 0.9830 | 0.9901    | 0.9827 |
| 0.0044        | 1.39  | 900  | 0.0057          | 0.9713 | 0.9895    | 0.9706 |
| 0.0258        | 1.85  | 1200 | 0.0040          | 0.9799 | 0.9920    | 0.9794 |
| 0.0135        | 2.32  | 1500 | 0.0050          | 0.9845 | 0.9943    | 0.9841 |
| 0.0023        | 2.78  | 1800 | 0.0065          | 0.9611 | 0.9932    | 0.9598 |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.0.0
- Datasets 2.1.0
- Tokenizers 0.15.0
