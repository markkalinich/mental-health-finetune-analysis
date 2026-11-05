---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITHOUT-DROPOUT-123
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITHOUT-DROPOUT-123

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3844
- Accuracy: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6.840039921359585e-05
- train_batch_size: 64
- eval_batch_size: 16
- seed: 123
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 5
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.2514        | 1.0   | 6    | 0.6219          | 0.9545   |
| 0.5759        | 2.0   | 12   | 0.5212          | 0.9545   |
| 0.4414        | 3.0   | 18   | 0.4739          | 0.9318   |
| 0.3855        | 4.0   | 24   | 0.4289          | 0.9545   |
| 0.3685        | 5.0   | 30   | 0.3981          | 1.0      |
| 0.3583        | 6.0   | 36   | 0.3917          | 1.0      |
| 0.3561        | 7.0   | 42   | 0.3852          | 1.0      |
| 0.3542        | 8.0   | 48   | 0.3844          | 1.0      |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
