---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITHOUT-DROPOUT-42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITHOUT-DROPOUT-42

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4506
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
- learning_rate: 4.718960201365898e-05
- train_batch_size: 128
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 2
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.4612        | 1.0   | 3    | 1.1750          | 0.6136   |
| 0.9587        | 2.0   | 6    | 0.6861          | 0.9091   |
| 0.5401        | 3.0   | 9    | 0.5511          | 0.9318   |
| 0.4878        | 4.0   | 12   | 0.4981          | 0.9545   |
| 0.44          | 5.0   | 15   | 0.5102          | 0.9091   |
| 0.4054        | 6.0   | 18   | 0.4674          | 0.9545   |
| 0.3942        | 7.0   | 21   | 0.4526          | 0.9773   |
| 0.3903        | 8.0   | 24   | 0.4506          | 0.9773   |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
