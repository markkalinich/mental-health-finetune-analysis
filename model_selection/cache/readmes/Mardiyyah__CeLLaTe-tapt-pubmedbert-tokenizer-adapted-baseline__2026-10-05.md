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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1076
- Accuracy: 0.7643
- Perplexity: 3.0272

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
| 1.3684        | 1.0   | 14   | 1.2141          | 0.7641   | 3.3674     |
| 1.3406        | 2.0   | 28   | 1.1774          | 0.7648   | 3.2459     |
| 1.3246        | 3.0   | 42   | 1.1310          | 0.7689   | 3.0988     |
| 1.2929        | 4.0   | 56   | 1.1271          | 0.7675   | 3.0866     |
| 1.2489        | 5.0   | 70   | 1.1542          | 0.7641   | 3.1716     |
| 1.2216        | 6.0   | 84   | 1.0947          | 0.7733   | 2.9882     |
| 1.1987        | 7.0   | 98   | 1.0540          | 0.7750   | 2.8691     |
| 1.2006        | 8.0   | 112  | 1.0942          | 0.7706   | 2.9868     |
| 1.1659        | 9.0   | 126  | 1.0899          | 0.7701   | 2.9741     |
| 1.1546        | 10.0  | 140  | 1.0596          | 0.7757   | 2.8851     |
| 1.1216        | 11.0  | 154  | 1.0536          | 0.7735   | 2.8680     |
| 1.1113        | 12.0  | 168  | 1.0336          | 0.7779   | 2.8111     |
| 1.0872        | 13.0  | 182  | 1.0709          | 0.7716   | 2.9179     |
| 1.1014        | 14.0  | 196  | 1.0786          | 0.7746   | 2.9406     |
| 1.0882        | 15.0  | 210  | 1.0788          | 0.7727   | 2.9413     |
| 1.0683        | 16.0  | 224  | 1.0398          | 0.7796   | 2.8287     |
| 1.0612        | 17.0  | 238  | 1.0620          | 0.7712   | 2.8920     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
