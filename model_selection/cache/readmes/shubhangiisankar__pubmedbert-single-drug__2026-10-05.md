---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract
tags:
- generated_from_trainer
model-index:
- name: pubmedbert-single-drug
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pubmedbert-single-drug

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0000

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.0027        | 1.0   | 1057 | 0.0000          |
| 0.0010        | 2.0   | 2114 | 0.0003          |
| 0.0005        | 3.0   | 3171 | 0.0000          |


### Framework versions

- Transformers 5.1.0
- Pytorch 2.9.0+cu126
- Datasets 4.5.0
- Tokenizers 0.22.2
