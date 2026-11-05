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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0329
- Accuracy: 0.7709
- Perplexity: 2.8091

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
| 1.2066        | 1.0   | 14   | 1.0552          | 0.7680   | 2.8725     |
| 1.2022        | 2.0   | 28   | 1.0389          | 0.7703   | 2.8262     |
| 1.1634        | 3.0   | 42   | 1.0517          | 0.7694   | 2.8624     |
| 1.1435        | 4.0   | 56   | 1.0598          | 0.7664   | 2.8858     |
| 1.1674        | 5.0   | 70   | 0.9973          | 0.7784   | 2.7109     |
| 1.1354        | 6.0   | 84   | 0.9737          | 0.7797   | 2.6478     |
| 1.1377        | 7.0   | 98   | 1.0435          | 0.7709   | 2.8391     |
| 1.1163        | 8.0   | 112  | 1.0534          | 0.7680   | 2.8675     |
| 1.1126        | 9.0   | 126  | 1.0454          | 0.7648   | 2.8445     |
| 1.0904        | 10.0  | 140  | 1.0425          | 0.7715   | 2.8363     |
| 1.0807        | 11.0  | 154  | 1.0148          | 0.7702   | 2.7587     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
