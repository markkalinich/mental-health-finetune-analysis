---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: clasificador-medical-biomedbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clasificador-medical-biomedbert

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9350
- Accuracy: 0.6472

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 405  | 0.8226          | 0.6264   |
| 0.8555        | 2.0   | 810  | 0.7807          | 0.6625   |
| 0.5712        | 3.0   | 1215 | 0.9350          | 0.6472   |


### Framework versions

- Transformers 5.7.0
- Pytorch 2.10.0+cu128
- Datasets 4.8.5
- Tokenizers 0.22.2
