---
library_name: transformers
base_model: 5CD-AI/Vietnamese-Sentiment-visobert
tags:
- text-classification
- vietnamese
- sentiment-analysis
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: tuning-sentiment-abp-neu
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tuning-sentiment-abp-neu

This model is a fine-tuned version of [5CD-AI/Vietnamese-Sentiment-visobert](https://huggingface.co/5CD-AI/Vietnamese-Sentiment-visobert) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5203
- Accuracy: 0.7812
- F1: 0.6565
- Precision: 0.6573
- Recall: 0.6570

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 261  | 0.3318          | 0.8144   | 0.5907 | 0.6726    | 0.6565 |
| 0.3498        | 2.0   | 522  | 0.3483          | 0.8152   | 0.6042 | 0.6727    | 0.6586 |
| 0.3498        | 3.0   | 783  | 0.3772          | 0.8169   | 0.5855 | 0.6107    | 0.6562 |
| 0.2683        | 4.0   | 1044 | 0.4225          | 0.7887   | 0.6528 | 0.6581    | 0.6576 |
| 0.2683        | 5.0   | 1305 | 0.5203          | 0.7812   | 0.6565 | 0.6573    | 0.6570 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
