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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask-combinedData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask-combinedData

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/Combined_TAPT_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1023
- Accuracy: 0.5977
- Perplexity: 8.1850

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
| 2.6735        | 1.0   | 28   | 2.2438          | 0.5810   | 9.4294     |
| 2.4083        | 2.0   | 56   | 2.1526          | 0.5907   | 8.6071     |
| 2.375         | 3.0   | 84   | 2.1275          | 0.5909   | 8.3943     |
| 2.3415        | 4.0   | 112  | 2.1319          | 0.5954   | 8.4312     |
| 2.3423        | 5.0   | 140  | 2.1031          | 0.5948   | 8.1917     |
| 2.3198        | 6.0   | 168  | 2.0806          | 0.5985   | 8.0092     |
| 2.31          | 7.0   | 196  | 2.0744          | 0.6028   | 7.9594     |
| 2.3199        | 8.0   | 224  | 2.1230          | 0.5918   | 8.3558     |
| 2.2729        | 9.0   | 252  | 2.0403          | 0.6020   | 7.6928     |
| 2.2842        | 10.0  | 280  | 2.1096          | 0.5930   | 8.2446     |
| 2.2639        | 11.0  | 308  | 2.0864          | 0.5989   | 8.0560     |
| 2.2578        | 12.0  | 336  | 2.0610          | 0.6004   | 7.8541     |
| 2.2211        | 13.0  | 364  | 2.1497          | 0.5861   | 8.5819     |
| 2.2328        | 14.0  | 392  | 2.0952          | 0.5916   | 8.1274     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
