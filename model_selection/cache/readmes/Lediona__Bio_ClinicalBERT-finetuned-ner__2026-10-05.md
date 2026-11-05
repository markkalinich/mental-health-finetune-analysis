---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Bio_ClinicalBERT-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bio_ClinicalBERT-finetuned-ner

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1920
- Precision: 0.7879
- Recall: 0.8752
- F1: 0.8292
- Accuracy: 0.9456

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1019        | 1.0   | 201  | 0.2103          | 0.7146    | 0.8483 | 0.7758 | 0.9310   |
| 0.0457        | 2.0   | 402  | 0.1856          | 0.7642    | 0.8627 | 0.8104 | 0.9405   |
| 0.0189        | 3.0   | 603  | 0.1830          | 0.7769    | 0.8708 | 0.8212 | 0.9431   |
| 0.0237        | 4.0   | 804  | 0.1893          | 0.7739    | 0.8722 | 0.8201 | 0.9449   |
| 0.0703        | 5.0   | 1005 | 0.1920          | 0.7879    | 0.8752 | 0.8292 | 0.9456   |


### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cu121
- Tokenizers 0.20.3
