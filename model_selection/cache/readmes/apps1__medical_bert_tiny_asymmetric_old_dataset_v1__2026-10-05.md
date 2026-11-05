---
library_name: peft
license: mit
base_model: prajjwal1/bert-tiny
tags:
- base_model:adapter:prajjwal1/bert-tiny
- lora
- transformers
metrics:
- accuracy
model-index:
- name: medical_bert_tiny_asymmetric_old_dataset_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_bert_tiny_asymmetric_old_dataset_v1

This model is a fine-tuned version of [prajjwal1/bert-tiny](https://huggingface.co/prajjwal1/bert-tiny) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0130
- Accuracy: 0.9885
- Recall Weighted: 0.9885
- Precision Weighted: 0.9885
- F1 Weighted: 0.9885
- F1 Macro: 0.9834
- F1 Prescription: 0.9730
- F1 Lab Report: 0.9771
- F1 Others: 1.0
- False Alarm Rate: 0.0
- Cross Class Error: 0.0248

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
| 0.0885        | 1.0   | 892  | 0.0208          | 0.9837   | 0.9837          | 0.9840             | 0.9837      | 0.9764   | 0.9611          | 0.9680        | 1.0       | 0.0              | 0.0351            |
| 0.1100        | 2.0   | 1784 | 0.0176          | 0.9847   | 0.9847          | 0.9849             | 0.9846      | 0.9778   | 0.9635          | 0.9698        | 1.0       | 0.0              | 0.0331            |
| 0.0162        | 3.0   | 2676 | 0.0169          | 0.9851   | 0.9851          | 0.9857             | 0.9851      | 0.9784   | 0.9643          | 0.9709        | 1.0       | 0.0              | 0.0320            |
| 0.0538        | 4.0   | 3568 | 0.0131          | 0.9880   | 0.9880          | 0.9881             | 0.9880      | 0.9827   | 0.9718          | 0.9762        | 1.0       | 0.0              | 0.0258            |
| 0.0004        | 5.0   | 4460 | 0.0130          | 0.9885   | 0.9885          | 0.9885             | 0.9885      | 0.9834   | 0.9730          | 0.9771        | 1.0       | 0.0              | 0.0248            |


### Framework versions

- PEFT 0.18.1
- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.5
- Tokenizers 0.22.2