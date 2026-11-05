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
- name: tuning-sentiment-abp-pos
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# tuning-sentiment-abp-pos

This model is a fine-tuned version of [5CD-AI/Vietnamese-Sentiment-visobert](https://huggingface.co/5CD-AI/Vietnamese-Sentiment-visobert) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5678
- Accuracy: 0.8153
- F1: 0.8137
- Precision: 0.8548
- Recall: 0.8001

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
| 0.4963        | 1.0   | 799  | 0.4323          | 0.8203   | 0.8122 | 0.8699    | 0.7992 |
| 0.3918        | 2.0   | 1598 | 0.4477          | 0.8223   | 0.8175 | 0.8720    | 0.7997 |
| 0.3535        | 3.0   | 2397 | 0.4750          | 0.8223   | 0.8157 | 0.8747    | 0.8001 |
| 0.3221        | 4.0   | 3196 | 0.5362          | 0.8176   | 0.8150 | 0.8585    | 0.8001 |
| 0.3041        | 5.0   | 3995 | 0.5678          | 0.8153   | 0.8137 | 0.8548    | 0.8001 |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1
