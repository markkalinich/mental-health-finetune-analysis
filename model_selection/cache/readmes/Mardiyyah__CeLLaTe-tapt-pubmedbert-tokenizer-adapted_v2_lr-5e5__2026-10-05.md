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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-5e5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted_v2_lr-5e5

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1756
- Accuracy: 0.7630
- Perplexity: 3.2401

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
| 1.3568        | 1.0   | 14   | 1.1951          | 0.7597   | 3.3038     |
| 1.3615        | 2.0   | 28   | 1.1865          | 0.7620   | 3.2756     |
| 1.3234        | 3.0   | 42   | 1.1876          | 0.7577   | 3.2792     |
| 1.3074        | 4.0   | 56   | 1.2069          | 0.7564   | 3.3432     |
| 1.2786        | 5.0   | 70   | 1.2031          | 0.7565   | 3.3303     |
| 1.261         | 6.0   | 84   | 1.1954          | 0.7546   | 3.3048     |
| 1.2397        | 7.0   | 98   | 1.1487          | 0.7636   | 3.1540     |
| 1.2315        | 8.0   | 112  | 1.2123          | 0.7520   | 3.3613     |
| 1.1975        | 9.0   | 126  | 1.1515          | 0.7574   | 3.1630     |
| 1.1853        | 10.0  | 140  | 1.1865          | 0.7563   | 3.2756     |
| 1.1912        | 11.0  | 154  | 1.1648          | 0.7541   | 3.2052     |
| 1.1469        | 12.0  | 168  | 1.1832          | 0.7563   | 3.2648     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
