---
library_name: transformers
language:
- en
license: apache-2.0
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-original-baseline

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9726
- Accuracy: 0.7783
- Perplexity: 2.6448

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-06 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Perplexity |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:----------:|
| 1.1444        | 1.0   | 14   | 1.0112          | 0.7749   | 2.7489     |
| 1.1264        | 2.0   | 28   | 0.9842          | 0.7806   | 2.6757     |
| 1.118         | 3.0   | 42   | 0.9774          | 0.7810   | 2.6574     |
| 1.0848        | 4.0   | 56   | 0.9892          | 0.7781   | 2.6891     |
| 1.0813        | 5.0   | 70   | 0.9697          | 0.7861   | 2.6372     |
| 1.0682        | 6.0   | 84   | 0.9910          | 0.7782   | 2.6938     |
| 1.0576        | 7.0   | 98   | 0.9641          | 0.7807   | 2.6225     |
| 1.0377        | 8.0   | 112  | 0.9392          | 0.7880   | 2.5580     |
| 1.0206        | 9.0   | 126  | 0.9936          | 0.7765   | 2.7009     |
| 1.0254        | 10.0  | 140  | 0.9782          | 0.7797   | 2.6595     |
| 0.9976        | 11.0  | 154  | 0.9627          | 0.7833   | 2.6188     |
| 0.9818        | 12.0  | 168  | 0.9549          | 0.7833   | 2.5985     |
| 0.9706        | 13.0  | 182  | 0.9498          | 0.7855   | 2.5851     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
