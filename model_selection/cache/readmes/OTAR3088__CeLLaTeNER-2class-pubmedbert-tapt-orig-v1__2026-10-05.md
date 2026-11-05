---
library_name: transformers
license: mit
base_model: Mardiyyah/CeLLaTe-pubmedbert-tapt-base
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: CeLLaTe-PubMedBERT-tapt-adapted-base
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-PubMedBERT-tapt-adapted-base

This model is a fine-tuned version of [Mardiyyah/CeLLaTe-pubmedbert-tapt-base](https://huggingface.co/Mardiyyah/CeLLaTe-pubmedbert-tapt-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0619
- Precision: 0.7896
- Recall: 0.7029
- F1: 0.7437
- Accuracy: 0.9830

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
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.01
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.5126        | 0.3802 | 100  | 0.1116          | 0.2188    | 0.1788 | 0.1968 | 0.9578   |
| 0.0895        | 0.7605 | 200  | 0.0686          | 0.6673    | 0.6217 | 0.6437 | 0.9805   |
| 0.0553        | 1.1407 | 300  | 0.0620          | 0.7445    | 0.6968 | 0.7198 | 0.9829   |
| 0.0414        | 1.5209 | 400  | 0.0548          | 0.7329    | 0.7267 | 0.7298 | 0.9827   |
| 0.0358        | 1.9011 | 500  | 0.0590          | 0.69      | 0.7578 | 0.7223 | 0.9823   |
| 0.0302        | 2.2814 | 600  | 0.0616          | 0.7896    | 0.7029 | 0.7437 | 0.9830   |
| 0.0271        | 2.6616 | 700  | 0.0553          | 0.7224    | 0.7193 | 0.7209 | 0.9813   |
| 0.0264        | 3.0418 | 800  | 0.0609          | 0.7711    | 0.7090 | 0.7387 | 0.9833   |
| 0.0187        | 3.4221 | 900  | 0.0712          | 0.7979    | 0.6937 | 0.7422 | 0.9831   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
