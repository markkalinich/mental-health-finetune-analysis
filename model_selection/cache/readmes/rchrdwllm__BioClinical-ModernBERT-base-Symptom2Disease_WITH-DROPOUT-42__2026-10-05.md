---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITH-DROPOUT-42

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4418
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
- learning_rate: 3.543053320347362e-05
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 5
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.6977        | 1.0   | 6    | 1.2635          | 0.5455   |
| 1.1157        | 2.0   | 12   | 0.8416          | 0.8182   |
| 0.6927        | 3.0   | 18   | 0.5574          | 0.9545   |
| 0.496         | 4.0   | 24   | 0.5281          | 0.9545   |
| 0.4599        | 5.0   | 30   | 0.4679          | 0.9773   |
| 0.4179        | 6.0   | 36   | 0.4463          | 0.9773   |
| 0.4023        | 7.0   | 42   | 0.4415          | 0.9773   |
| 0.3997        | 8.0   | 48   | 0.4418          | 0.9773   |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
