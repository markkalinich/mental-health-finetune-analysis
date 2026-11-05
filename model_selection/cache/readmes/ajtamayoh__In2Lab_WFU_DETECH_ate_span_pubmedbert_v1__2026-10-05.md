---
library_name: transformers
license: mit
base_model: microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: In2Lab_WFU_DETECH_ate_span_pubmedbert_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# In2Lab_WFU_DETECH_ate_span_pubmedbert_v1

This model is a fine-tuned version of [microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1159
- Precision: 0.8237
- Recall: 0.8168
- F1: 0.8202

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 7
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 61   | 0.1541          | 0.7421    | 0.6201 | 0.6757 |
| No log        | 2.0   | 122  | 0.1262          | 0.7720    | 0.7468 | 0.7592 |
| No log        | 3.0   | 183  | 0.1156          | 0.7987    | 0.7937 | 0.7962 |
| No log        | 4.0   | 244  | 0.1134          | 0.8160    | 0.7958 | 0.8058 |
| No log        | 5.0   | 305  | 0.1132          | 0.8276    | 0.8050 | 0.8162 |
| No log        | 6.0   | 366  | 0.1119          | 0.8306    | 0.8017 | 0.8159 |
| No log        | 7.0   | 427  | 0.1159          | 0.8237    | 0.8168 | 0.8202 |


### Framework versions

- Transformers 4.57.6
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2
