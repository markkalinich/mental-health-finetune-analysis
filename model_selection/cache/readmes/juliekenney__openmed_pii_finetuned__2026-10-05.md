---
library_name: transformers
license: apache-2.0
base_model: OpenMed/OpenMed-PII-Dutch-SuperClinical-Large-434M-v1
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: openmed_pii_finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# openmed_pii_finetuned

This model is a fine-tuned version of [OpenMed/OpenMed-PII-Dutch-SuperClinical-Large-434M-v1](https://huggingface.co/OpenMed/OpenMed-PII-Dutch-SuperClinical-Large-434M-v1) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3078
- Precision: 0.7816
- Recall: 0.8097
- F1: 0.7954
- Accuracy: 0.954

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 1.3820        | 1.0   | 813  | 0.3712          | 0.7548    | 0.7422 | 0.7485 | 0.9422   |
| 0.9324        | 2.0   | 1626 | 0.3253          | 0.7525    | 0.7889 | 0.7703 | 0.948    |
| 0.7569        | 3.0   | 2439 | 0.2990          | 0.7778    | 0.7824 | 0.7801 | 0.9508   |
| 0.6287        | 4.0   | 3252 | 0.3051          | 0.7812    | 0.7982 | 0.7896 | 0.953    |
| 0.6297        | 5.0   | 4065 | 0.3078          | 0.7816    | 0.8097 | 0.7954 | 0.954    |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.3
- Tokenizers 0.22.2
