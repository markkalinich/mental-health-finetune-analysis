---
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: Bio_ClinicalBERT-medical-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bio_ClinicalBERT-medical-text-classification

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8941
- Accuracy: 0.273
- Precision: 0.2486
- Recall: 0.273
- F1: 0.2532

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
| 2.4866        | 1.0   | 250  | 2.5436          | 0.355    | 0.1460    | 0.355  | 0.2036 |
| 1.9145        | 2.0   | 500  | 2.0555          | 0.369    | 0.2437    | 0.369  | 0.2406 |
| 1.849         | 3.0   | 750  | 1.8421          | 0.321    | 0.2862    | 0.321  | 0.2949 |
| 1.4025        | 4.0   | 1000 | 1.7678          | 0.325    | 0.2950    | 0.325  | 0.2957 |
| 1.311         | 5.0   | 1250 | 1.8007          | 0.312    | 0.2654    | 0.312  | 0.2743 |
| 1.2112        | 6.0   | 1500 | 1.8941          | 0.273    | 0.2486    | 0.273  | 0.2532 |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.1.2
- Datasets 2.18.0
- Tokenizers 0.15.2
