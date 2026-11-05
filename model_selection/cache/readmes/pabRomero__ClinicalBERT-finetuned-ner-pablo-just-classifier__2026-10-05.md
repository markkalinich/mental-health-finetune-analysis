---
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: ClinicalBERT-finetuned-ner-pablo-just-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT-finetuned-ner-pablo-just-classifier

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1567
- Precision: 0.7118
- Recall: 0.7328
- F1: 0.7221
- Accuracy: 0.9650

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.1
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.05
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.495         | 0.9996 | 652  | 0.3446          | 0.6425    | 0.6934 | 0.6670 | 0.9575   |
| 0.3703        | 1.9992 | 1304 | 0.1567          | 0.7118    | 0.7328 | 0.7221 | 0.9650   |


### Framework versions

- Transformers 4.44.0
- Pytorch 2.4.0+cu124
- Datasets 2.21.0
- Tokenizers 0.19.1
