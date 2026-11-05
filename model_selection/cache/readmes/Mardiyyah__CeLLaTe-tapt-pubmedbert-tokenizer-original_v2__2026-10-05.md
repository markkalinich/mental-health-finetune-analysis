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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-original_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-original_v2

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/TAPT_CeLLaTe2.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0433
- Accuracy: 0.7695
- Perplexity: 2.8385

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
| 1.209         | 1.0   | 14   | 1.0540          | 0.7678   | 2.8692     |
| 1.1983        | 2.0   | 28   | 1.0407          | 0.7700   | 2.8313     |
| 1.1651        | 3.0   | 42   | 1.0530          | 0.7689   | 2.8662     |
| 1.1403        | 4.0   | 56   | 1.0620          | 0.7659   | 2.8920     |
| 1.1665        | 5.0   | 70   | 1.0056          | 0.7774   | 2.7337     |
| 1.1431        | 6.0   | 84   | 0.9861          | 0.7798   | 2.6806     |
| 1.1417        | 7.0   | 98   | 1.0499          | 0.7707   | 2.8572     |
| 1.1194        | 8.0   | 112  | 1.0551          | 0.7675   | 2.8722     |
| 1.1158        | 9.0   | 126  | 1.0471          | 0.7644   | 2.8494     |
| 1.0882        | 10.0  | 140  | 1.0437          | 0.7717   | 2.8396     |
| 1.0809        | 11.0  | 154  | 1.0141          | 0.7710   | 2.7570     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
