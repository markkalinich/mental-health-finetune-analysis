---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- sentiment-analysis
- finance
- distilbert
- nlp
- pytorch
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: distilbert-financial-sentiment
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-financial-sentiment

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5362
- Accuracy: 0.8811
- F1: 0.8813

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
- eval_batch_size: 32
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.4283        | 1.0   | 597  | 0.4217          | 0.8312   | 0.8362 |
| 0.3001        | 2.0   | 1194 | 0.3502          | 0.8744   | 0.8741 |
| 0.1525        | 3.0   | 1791 | 0.4140          | 0.8781   | 0.8782 |
| 0.0910        | 4.0   | 2388 | 0.4919          | 0.8802   | 0.8804 |
| 0.0699        | 5.0   | 2985 | 0.5362          | 0.8811   | 0.8813 |


### Framework versions

- Transformers 5.9.0
- Pytorch 2.11.0+cu128
- Datasets 2.21.0
- Tokenizers 0.22.2
