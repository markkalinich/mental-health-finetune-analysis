---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-456
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-456

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4922
- Accuracy: 0.9773

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.257429996785895e-05
- train_batch_size: 64
- eval_batch_size: 16
- seed: 456
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 5
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3361        | 1.0   | 6    | 0.9282          | 0.8182   |
| 0.8302        | 2.0   | 12   | 0.5890          | 0.8636   |
| 0.5745        | 3.0   | 18   | 0.8040          | 0.8636   |
| 0.5607        | 4.0   | 24   | 0.5510          | 0.9318   |
| 0.5358        | 5.0   | 30   | 0.4874          | 0.9545   |
| 0.4606        | 6.0   | 36   | 0.5069          | 0.9318   |
| 0.44          | 7.0   | 42   | 0.4928          | 0.9545   |
| 0.4406        | 8.0   | 48   | 0.4922          | 0.9773   |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
