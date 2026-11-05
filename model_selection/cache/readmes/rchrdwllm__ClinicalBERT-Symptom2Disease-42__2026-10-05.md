---
library_name: transformers
base_model: medicalai/ClinicalBERT
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: ClinicalBERT-Symptom2Disease-42
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBERT-Symptom2Disease-42

This model is a fine-tuned version of [medicalai/ClinicalBERT](https://huggingface.co/medicalai/ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4637
- Accuracy: 0.9822

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.73070774474794e-05
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
| 1.1887        | 1.0   | 132  | 0.6752          | 0.9067   |
| 0.5111        | 2.0   | 264  | 0.5008          | 0.9622   |
| 0.4641        | 3.0   | 396  | 0.4672          | 0.9711   |
| 0.44          | 4.0   | 528  | 0.4614          | 0.9778   |
| 0.4299        | 5.0   | 660  | 0.4686          | 0.9756   |
| 0.4246        | 6.0   | 792  | 0.4636          | 0.9822   |
| 0.4232        | 7.0   | 924  | 0.4638          | 0.9822   |
| 0.423         | 8.0   | 1056 | 0.4637          | 0.9822   |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.8.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.1
