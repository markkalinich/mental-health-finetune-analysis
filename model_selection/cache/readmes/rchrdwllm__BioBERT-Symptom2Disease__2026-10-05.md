---
library_name: transformers
base_model: dmis-lab/biobert-v1.1
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BioBERT-Symptom2Disease
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BioBERT-Symptom2Disease

This model is a fine-tuned version of [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9704
- Accuracy: 0.6364

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.4346431315956026e-05
- train_batch_size: 128
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.3808        | 1.0   | 3    | 1.3027          | 0.4091   |
| 1.2227        | 2.0   | 6    | 1.1699          | 0.6364   |
| 1.0889        | 3.0   | 9    | 1.0762          | 0.6591   |
| 1.0029        | 4.0   | 12   | 1.0024          | 0.6591   |
| 0.9398        | 5.0   | 15   | 0.9704          | 0.6364   |


### Framework versions

- Transformers 4.56.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.0
