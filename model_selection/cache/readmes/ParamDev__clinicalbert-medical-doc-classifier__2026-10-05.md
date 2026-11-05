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
- name: clinicalbert-medical-doc-classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinicalbert-medical-doc-classifier

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0252
- Accuracy: 0.9953
- F1: 0.9948

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:------:|:----:|:---------------:|:--------:|:------:|
| 0.1238        | 0.1582 | 100  | 0.1158          | 0.9757   | 0.9679 |
| 0.0966        | 0.3165 | 200  | 0.0470          | 0.9924   | 0.9912 |
| 0.0269        | 0.4747 | 300  | 0.0364          | 0.9942   | 0.9931 |
| 0.0178        | 0.6329 | 400  | 0.0336          | 0.9947   | 0.9935 |
| 0.0428        | 0.7911 | 500  | 0.0327          | 0.9940   | 0.9933 |
| 0.0062        | 0.9494 | 600  | 0.0296          | 0.9949   | 0.9937 |
| 0.0370        | 1.1076 | 700  | 0.0262          | 0.9947   | 0.9935 |
| 0.0201        | 1.2658 | 800  | 0.0279          | 0.9947   | 0.9935 |
| 0.0231        | 1.4241 | 900  | 0.0252          | 0.9953   | 0.9948 |
| 0.0193        | 1.5823 | 1000 | 0.0249          | 0.9953   | 0.9942 |
| 0.0189        | 1.7405 | 1100 | 0.0263          | 0.9951   | 0.9941 |
| 0.0201        | 1.8987 | 1200 | 0.0256          | 0.9953   | 0.9947 |


### Framework versions

- Transformers 5.4.0
- Pytorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2
