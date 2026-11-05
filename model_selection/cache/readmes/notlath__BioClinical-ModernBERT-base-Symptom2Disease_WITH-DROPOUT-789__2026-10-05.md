---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-789
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-789

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5520
- Accuracy: 0.9545

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.018827288450037e-05
- train_batch_size: 128
- eval_batch_size: 16
- seed: 789
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 2
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3704        | 1.0   | 3    | 1.1832          | 0.6591   |
| 1.1927        | 2.0   | 6    | 0.8890          | 0.8409   |
| 0.9314        | 3.0   | 9    | 0.6910          | 0.8409   |
| 0.7426        | 4.0   | 12   | 0.5574          | 0.9318   |
| 0.6127        | 5.0   | 15   | 0.5532          | 0.9318   |
| 0.5672        | 6.0   | 18   | 0.5507          | 0.9318   |
| 0.5522        | 7.0   | 21   | 0.5518          | 0.9318   |
| 0.5531        | 8.0   | 24   | 0.5520          | 0.9545   |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
