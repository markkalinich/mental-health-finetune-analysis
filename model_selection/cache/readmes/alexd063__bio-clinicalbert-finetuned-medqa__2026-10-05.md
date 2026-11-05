---
library_name: transformers
license: mit
base_model: emilyalsentzer/Bio_ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bio-clinicalbert-finetuned-medqa
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bio-clinicalbert-finetuned-medqa

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on the GBaker/MedQA-USMLE-4-options dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3851
- Accuracy: 0.2616
- F1 Macro: 0.2603
- Ece: 0.0085

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Macro | Ece    |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|:------:|
| 1.4200        | 1.0   | 2290 | 1.3856          | 0.2574   | 0.2575   | 0.0040 |
| 1.3998        | 2.0   | 4580 | 1.3866          | 0.2446   | 0.1338   | 0.0054 |
| 1.3936        | 3.0   | 6870 | 1.3866          | 0.2544   | 0.1278   | 0.0044 |


### Framework versions

- Transformers 5.8.1
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
