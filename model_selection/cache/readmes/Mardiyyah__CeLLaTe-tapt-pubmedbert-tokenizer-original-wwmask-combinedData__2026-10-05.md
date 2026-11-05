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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask-combinedData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-original-wwmask-combinedData

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/Combined_TAPT_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0617
- Accuracy: 0.7651
- Perplexity: 2.8914

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
| 1.1819        | 1.0   | 28   | 1.0755          | 0.7637   | 2.9314     |
| 1.177         | 2.0   | 56   | 1.0435          | 0.7700   | 2.8391     |
| 1.1729        | 3.0   | 84   | 1.0621          | 0.7669   | 2.8925     |
| 1.153         | 4.0   | 112  | 1.0608          | 0.7672   | 2.8887     |
| 1.1487        | 5.0   | 140  | 1.0797          | 0.7591   | 2.9437     |
| 1.1204        | 6.0   | 168  | 1.0668          | 0.7645   | 2.9060     |
| 1.1177        | 7.0   | 196  | 1.0658          | 0.7605   | 2.9033     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
