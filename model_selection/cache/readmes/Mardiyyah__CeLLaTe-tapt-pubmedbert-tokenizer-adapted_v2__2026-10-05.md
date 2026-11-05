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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0382
- Accuracy: 0.7691
- Perplexity: 2.8240

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
| 1.2084        | 1.0   | 14   | 1.0521          | 0.7681   | 2.8636     |
| 1.1946        | 2.0   | 28   | 1.0386          | 0.7696   | 2.8253     |
| 1.1586        | 3.0   | 42   | 1.0498          | 0.7687   | 2.8572     |
| 1.1324        | 4.0   | 56   | 1.0643          | 0.7652   | 2.8989     |
| 1.155         | 5.0   | 70   | 1.0055          | 0.7768   | 2.7334     |
| 1.1254        | 6.0   | 84   | 0.9817          | 0.7778   | 2.6691     |
| 1.1211        | 7.0   | 98   | 1.0599          | 0.7684   | 2.8862     |
| 1.0968        | 8.0   | 112  | 1.0617          | 0.7659   | 2.8912     |
| 1.0885        | 9.0   | 126  | 1.0601          | 0.7627   | 2.8868     |
| 1.0577        | 10.0  | 140  | 1.0537          | 0.7705   | 2.8683     |
| 1.0454        | 11.0  | 154  | 1.0260          | 0.7684   | 2.7898     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
