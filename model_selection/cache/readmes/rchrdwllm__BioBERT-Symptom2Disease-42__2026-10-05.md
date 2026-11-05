---
library_name: transformers
license: mit
base_model: thomas-sounack/BioClinical-ModernBERT-base
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioBERT-Symptom2Disease-42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioBERT-Symptom2Disease-42

This model is a fine-tuned version of [thomas-sounack/BioClinical-ModernBERT-base](https://huggingface.co/thomas-sounack/BioClinical-ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5378
- Accuracy: 0.9556

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3.56860980172002e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 131
- num_epochs: 8
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3518        | 1.0   | 132  | 1.5159          | 0.5578   |
| 0.7346        | 2.0   | 264  | 0.6844          | 0.9      |
| 0.5545        | 3.0   | 396  | 0.6610          | 0.9044   |
| 0.4661        | 4.0   | 528  | 0.5774          | 0.9378   |
| 0.4351        | 5.0   | 660  | 0.5931          | 0.9289   |
| 0.4264        | 6.0   | 792  | 0.5469          | 0.9511   |
| 0.4229        | 7.0   | 924  | 0.5383          | 0.9578   |
| 0.422         | 8.0   | 1056 | 0.5378          | 0.9556   |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
