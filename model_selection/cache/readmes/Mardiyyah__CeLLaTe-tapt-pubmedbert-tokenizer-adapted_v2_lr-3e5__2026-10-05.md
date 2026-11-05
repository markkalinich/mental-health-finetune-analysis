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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-3e5

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1493
- Accuracy: 0.7653
- Perplexity: 3.1561

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
| 1.3584        | 1.0   | 14   | 1.2016          | 0.7595   | 3.3253     |
| 1.3699        | 2.0   | 28   | 1.1943          | 0.7615   | 3.3012     |
| 1.3374        | 3.0   | 42   | 1.1951          | 0.7587   | 3.3038     |
| 1.3226        | 4.0   | 56   | 1.2118          | 0.7565   | 3.3596     |
| 1.2976        | 5.0   | 70   | 1.2074          | 0.7574   | 3.3449     |
| 1.283         | 6.0   | 84   | 1.1959          | 0.7552   | 3.3066     |
| 1.2645        | 7.0   | 98   | 1.1472          | 0.7638   | 3.1494     |
| 1.2597        | 8.0   | 112  | 1.2038          | 0.7514   | 3.3326     |
| 1.2291        | 9.0   | 126  | 1.1464          | 0.7597   | 3.1469     |
| 1.2186        | 10.0  | 140  | 1.1744          | 0.7571   | 3.2362     |
| 1.2329        | 11.0  | 154  | 1.1545          | 0.7565   | 3.1724     |
| 1.1898        | 12.0  | 168  | 1.1718          | 0.7589   | 3.2278     |
| 1.1865        | 13.0  | 182  | 1.2333          | 0.7520   | 3.4325     |
| 1.1772        | 14.0  | 196  | 1.1856          | 0.7567   | 3.2727     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
