---
library_name: transformers
license: mit
base_model: prajjwal1/bert-tiny
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: medical_bert_tiny_asymmetric_old_dataset_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_bert_tiny_asymmetric_old_dataset_v2

This model is a fine-tuned version of [prajjwal1/bert-tiny](https://huggingface.co/prajjwal1/bert-tiny) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0096
- Accuracy: 0.9952
- Recall Weighted: 0.9952
- Precision Weighted: 0.9952
- F1 Weighted: 0.9952
- F1 Macro: 0.9931
- F1 Prescription: 0.9889
- F1 Lab Report: 0.9904
- F1 Others: 1.0
- False Alarm Rate: 0.0
- Cross Class Error: 0.0103

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Recall Weighted | Precision Weighted | F1 Weighted | F1 Macro | F1 Prescription | F1 Lab Report | F1 Others | False Alarm Rate | Cross Class Error |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------------:|:------------------:|:-----------:|:--------:|:---------------:|:-------------:|:---------:|:----------------:|:-----------------:|
| 0.0543        | 1.0   | 892  | 0.0200          | 0.9904   | 0.9904          | 0.9906             | 0.9904      | 0.9865   | 0.9784          | 0.9820        | 0.9991    | 0.0              | 0.0186            |
| 0.0011        | 2.0   | 1784 | 0.0095          | 0.9952   | 0.9952          | 0.9952             | 0.9952      | 0.9935   | 0.9910          | 0.9904        | 0.9991    | 0.0009           | 0.0083            |
| 0.0005        | 3.0   | 2676 | 0.0068          | 0.9962   | 0.9962          | 0.9962             | 0.9962      | 0.9949   | 0.9933          | 0.9923        | 0.9991    | 0.0              | 0.0062            |
| 0.0004        | 4.0   | 3568 | 0.0074          | 0.9962   | 0.9962          | 0.9962             | 0.9962      | 0.9949   | 0.9933          | 0.9923        | 0.9991    | 0.0              | 0.0062            |
| 0.0003        | 5.0   | 4460 | 0.0096          | 0.9952   | 0.9952          | 0.9952             | 0.9952      | 0.9931   | 0.9889          | 0.9904        | 1.0       | 0.0              | 0.0103            |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.5
- Tokenizers 0.22.2
