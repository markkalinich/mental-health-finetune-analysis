---
library_name: transformers
license: apache-2.0
base_model: distilbert/distilbert-base-multilingual-cased
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: distilbert-no-aug-pubmed
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-no-aug-pubmed

This model is a fine-tuned version of [distilbert/distilbert-base-multilingual-cased](https://huggingface.co/distilbert/distilbert-base-multilingual-cased) on the pietrolesci/pubmed-20k-rct dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7624
- F1: 0.6499

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
| No log        | 1.0   | 32   | 1.3359          | 0.4524 |
| No log        | 2.0   | 64   | 0.9877          | 0.5552 |
| No log        | 3.0   | 96   | 0.7930          | 0.6458 |
| No log        | 4.0   | 128  | 0.7555          | 0.6404 |
| No log        | 5.0   | 160  | 0.7209          | 0.6516 |
| No log        | 6.0   | 192  | 0.7981          | 0.6238 |
| No log        | 7.0   | 224  | 0.7684          | 0.6489 |
| No log        | 8.0   | 256  | 0.7444          | 0.6535 |
| No log        | 9.0   | 288  | 0.7954          | 0.6307 |
| No log        | 10.0  | 320  | 0.7624          | 0.6499 |


### Framework versions

- Transformers 4.57.1
- Pytorch 2.9.0+cu128
- Datasets 4.3.0
- Tokenizers 0.22.1
