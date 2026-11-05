---
library_name: transformers
license: mit
base_model: prajjwal1/bert-tiny
tags:
- generated_from_trainer
model-index:
- name: medical_bert_tiny_asymmetric_old_dataset_v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medical_bert_tiny_asymmetric_old_dataset_v3

This model is a fine-tuned version of [prajjwal1/bert-tiny](https://huggingface.co/prajjwal1/bert-tiny) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.0062
- eval_accuracy: 0.9947
- eval_recall_weighted: 0.9947
- eval_precision_weighted: 0.9948
- eval_f1_weighted: 0.9947
- eval_f1_macro: 0.9926
- eval_f1_prescription: 0.9889
- eval_f1_lab_report: 0.9894
- eval_f1_others: 0.9996
- eval_false_alarm_rate: 0.0009
- eval_cross_class_error: 0.0103
- eval_runtime: 2.6043
- eval_samples_per_second: 801.365
- eval_steps_per_second: 12.671
- epoch: 2.0
- step: 1784

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

### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.5
- Tokenizers 0.22.2
