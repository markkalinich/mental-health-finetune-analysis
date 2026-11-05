---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: distilbert-llm-aug-pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-llm-aug-pubmed

This model is a fine-tuned version of [distilbert/distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) on the marcgrec/pubmed_20k-llm-aug dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6845
- F1: 0.6227

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 1.0   | 157  | 0.7439          | 0.6239 |
| No log        | 2.0   | 314  | 0.7487          | 0.6577 |
| No log        | 3.0   | 471  | 0.9575          | 0.6186 |
| 0.5811        | 4.0   | 628  | 1.2496          | 0.6181 |
| 0.5811        | 5.0   | 785  | 1.4972          | 0.6104 |
| 0.5811        | 6.0   | 942  | 1.5878          | 0.6106 |
| 0.0245        | 7.0   | 1099 | 1.6166          | 0.6234 |
| 0.0245        | 8.0   | 1256 | 1.6534          | 0.6216 |
| 0.0245        | 9.0   | 1413 | 1.6430          | 0.6275 |
| 0.0018        | 10.0  | 1570 | 1.6845          | 0.6227 |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.0+cu128
- Datasets 4.3.0
- Tokenizers 0.22.1
