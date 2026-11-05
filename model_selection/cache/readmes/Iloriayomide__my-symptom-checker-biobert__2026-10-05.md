---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
model-index:
- name: my-symptom-checker-biobert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# my-symptom-checker-biobert

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1376

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
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 30   | 2.9013          |
| No log        | 2.0   | 60   | 2.4887          |
| No log        | 3.0   | 90   | 2.0553          |
| No log        | 4.0   | 120  | 1.6494          |
| No log        | 5.0   | 150  | 1.3190          |
| No log        | 6.0   | 180  | 1.0499          |
| No log        | 7.0   | 210  | 0.8211          |
| No log        | 8.0   | 240  | 0.6230          |
| No log        | 9.0   | 270  | 0.4702          |
| No log        | 10.0  | 300  | 0.3656          |
| No log        | 11.0  | 330  | 0.2884          |
| No log        | 12.0  | 360  | 0.2331          |
| No log        | 13.0  | 390  | 0.1986          |
| No log        | 14.0  | 420  | 0.1808          |
| No log        | 15.0  | 450  | 0.1630          |
| No log        | 16.0  | 480  | 0.1546          |
| 0.9873        | 17.0  | 510  | 0.1469          |
| 0.9873        | 18.0  | 540  | 0.1409          |
| 0.9873        | 19.0  | 570  | 0.1378          |
| 0.9873        | 20.0  | 600  | 0.1376          |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.1+cu128
- Datasets 4.4.1
- Tokenizers 0.22.1
