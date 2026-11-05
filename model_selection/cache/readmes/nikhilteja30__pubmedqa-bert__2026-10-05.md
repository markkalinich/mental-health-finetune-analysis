---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: pubmedqa-bert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmedqa-bert

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1777
- Accuracy: 0.57
- F1 Macro: 0.5147

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 34
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Macro |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.7552        | 1.0   | 57   | 1.0784          | 0.58     | 0.4976   |
| 0.4710        | 2.0   | 114  | 1.2157          | 0.51     | 0.4021   |
| 0.4729        | 3.0   | 171  | 1.1777          | 0.57     | 0.5147   |


### Framework versions

- Transformers 5.0.0
- Pytorch 2.10.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
