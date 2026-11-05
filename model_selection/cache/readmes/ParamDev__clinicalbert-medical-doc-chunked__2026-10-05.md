---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: clinicalbert-medical-doc-chunked
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinicalbert-medical-doc-chunked

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0374
- Accuracy: 0.9925
- F1: 0.9919

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 0.0491        | 1.0   | 6796  | 0.0410          | 0.9911   | 0.9900 |
| 0.0328        | 2.0   | 13592 | 0.0354          | 0.9927   | 0.9917 |
| 0.0249        | 3.0   | 20388 | 0.0374          | 0.9925   | 0.9919 |


### Framework versions

- Transformers 5.4.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2
