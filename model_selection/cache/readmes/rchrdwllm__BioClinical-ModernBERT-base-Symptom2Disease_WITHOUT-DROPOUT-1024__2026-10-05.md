---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioClinical-ModernBERT-base-Symptom2Disease_WITHOUT-DROPOUT-1024
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioClinical-ModernBERT-base-Symptom2Disease_WITHOUT-DROPOUT-1024

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3624
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
- learning_rate: 6.379032964641383e-05
- train_batch_size: 64
- eval_batch_size: 16
- seed: 1024
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 5
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.5113        | 1.0   | 6    | 1.0219          | 0.6364   |
| 0.6904        | 2.0   | 12   | 0.5551          | 0.8864   |
| 0.4791        | 3.0   | 18   | 0.4180          | 1.0      |
| 0.3863        | 4.0   | 24   | 0.3780          | 1.0      |
| 0.3678        | 5.0   | 30   | 0.3647          | 1.0      |
| 0.3597        | 6.0   | 36   | 0.3661          | 1.0      |
| 0.3555        | 7.0   | 42   | 0.3632          | 1.0      |
| 0.3546        | 8.0   | 48   | 0.3624          | 1.0      |


### Framework versions

- Transformers 4.56.2
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
