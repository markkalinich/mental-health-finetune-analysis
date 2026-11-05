---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-1024
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-1024

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5515
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
- learning_rate: 7.359552467551551e-05
- train_batch_size: 128
- eval_batch_size: 16
- seed: 1024
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 2
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.5945        | 1.0   | 3    | 1.2203          | 0.4091   |
| 1.2782        | 2.0   | 6    | 0.8503          | 0.8409   |
| 0.9045        | 3.0   | 9    | 0.6354          | 0.9091   |
| 0.6434        | 4.0   | 12   | 0.5134          | 0.8864   |
| 0.5588        | 5.0   | 15   | 0.5156          | 0.9773   |
| 0.5302        | 6.0   | 18   | 0.5504          | 0.9545   |
| 0.5345        | 7.0   | 21   | 0.5581          | 0.9318   |
| 0.5304        | 8.0   | 24   | 0.5515          | 0.9545   |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
