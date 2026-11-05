---
library_name: transformers
license: mit
base_model: FacebookAI/roberta-large
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: roberta-Empathy-goodareas-eval_FeedbackESConv5pp_CARE10pp-sweeps-current
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-Empathy-goodareas-eval_FeedbackESConv5pp_CARE10pp-sweeps-current

This model is a fine-tuned version of [FacebookAI/roberta-large](https://huggingface.co/FacebookAI/roberta-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4517
- Accuracy: 0.8126
- Precision: 0.6552
- Recall: 0.8531
- F1: 0.7411

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.4215053849812563e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.6796        | 1.0   | 123  | 0.5135          | 0.7330   | 0.5527    | 0.7918 | 0.6510 |
| 0.5601        | 2.0   | 246  | 0.3676          | 0.7869   | 0.6287    | 0.7878 | 0.6993 |
| 0.4963        | 3.0   | 369  | 0.3964          | 0.8216   | 0.6893    | 0.7878 | 0.7352 |
| 0.4666        | 4.0   | 492  | 0.5450          | 0.7433   | 0.5547    | 0.9306 | 0.6951 |
| 0.44          | 5.0   | 615  | 0.2741          | 0.8216   | 0.7154    | 0.7184 | 0.7169 |
| 0.3848        | 6.0   | 738  | 0.3214          | 0.8177   | 0.6846    | 0.7796 | 0.7290 |
| 0.3553        | 7.0   | 861  | 0.3163          | 0.8139   | 0.6825    | 0.7633 | 0.7206 |
| 0.3197        | 8.0   | 984  | 0.4856          | 0.7882   | 0.6136    | 0.8816 | 0.7236 |
| 0.2825        | 9.0   | 1107 | 0.4515          | 0.7959   | 0.6303    | 0.8490 | 0.7235 |
| 0.2423        | 10.0  | 1230 | 0.4517          | 0.8126   | 0.6552    | 0.8531 | 0.7411 |


### Framework versions

- Transformers 4.48.3
- Pytorch 2.5.1+cu124
- Datasets 2.21.0
- Tokenizers 0.21.0
