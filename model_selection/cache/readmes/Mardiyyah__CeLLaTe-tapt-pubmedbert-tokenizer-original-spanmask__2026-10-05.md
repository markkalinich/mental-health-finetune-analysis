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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-original-spanmask

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1721
- Accuracy: 0.5857
- Perplexity: 8.7763

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
| 2.7396        | 1.0   | 14   | 2.3642          | 0.5703   | 10.6359    |
| 2.5077        | 2.0   | 28   | 2.2759          | 0.5742   | 9.7369     |
| 2.4329        | 3.0   | 42   | 2.1662          | 0.5936   | 8.7251     |
| 2.3886        | 4.0   | 56   | 2.1748          | 0.5859   | 8.8000     |
| 2.378         | 5.0   | 70   | 2.1150          | 0.5914   | 8.2897     |
| 2.3618        | 6.0   | 84   | 2.1638          | 0.5821   | 8.7040     |
| 2.322         | 7.0   | 98   | 2.1467          | 0.5910   | 8.5563     |
| 2.299         | 8.0   | 112  | 2.1630          | 0.5827   | 8.6973     |
| 2.3081        | 9.0   | 126  | 2.0821          | 0.5989   | 8.0216     |
| 2.2939        | 10.0  | 140  | 2.1986          | 0.5835   | 9.0125     |
| 2.2826        | 11.0  | 154  | 2.1773          | 0.5870   | 8.8226     |
| 2.2581        | 12.0  | 168  | 2.1368          | 0.5880   | 8.4727     |
| 2.2392        | 13.0  | 182  | 2.1805          | 0.5857   | 8.8505     |
| 2.2305        | 14.0  | 196  | 2.1175          | 0.5906   | 8.3106     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
