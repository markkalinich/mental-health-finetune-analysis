---
library_name: transformers
license: apache-2.0
base_model: d4data/biomedical-ner-all
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biomedical-ner-all-finetuned-ner-combined-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biomedical-ner-all-finetuned-ner-combined-v1

This model is a fine-tuned version of [d4data/biomedical-ner-all](https://huggingface.co/d4data/biomedical-ner-all) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2720
- Precision: 0.7536
- Recall: 0.7415
- F1: 0.7475
- Accuracy: 0.9264

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
- num_epochs: 40

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 240  | 0.2967          | 0.6682    | 0.6905 | 0.6791 | 0.9113   |
| No log        | 2.0   | 480  | 0.2534          | 0.7135    | 0.7351 | 0.7241 | 0.9210   |
| 0.3367        | 3.0   | 720  | 0.2390          | 0.7477    | 0.7281 | 0.7378 | 0.9236   |
| 0.3367        | 4.0   | 960  | 0.2386          | 0.7335    | 0.7462 | 0.7398 | 0.9235   |
| 0.1877        | 5.0   | 1200 | 0.2473          | 0.7302    | 0.7597 | 0.7446 | 0.9243   |
| 0.1877        | 6.0   | 1440 | 0.2435          | 0.7449    | 0.7477 | 0.7463 | 0.9261   |
| 0.1508        | 7.0   | 1680 | 0.2535          | 0.7251    | 0.7712 | 0.7474 | 0.9246   |
| 0.1508        | 8.0   | 1920 | 0.2564          | 0.7331    | 0.7604 | 0.7465 | 0.9254   |
| 0.1206        | 9.0   | 2160 | 0.2642          | 0.7435    | 0.7481 | 0.7458 | 0.9256   |
| 0.1206        | 10.0  | 2400 | 0.2720          | 0.7536    | 0.7415 | 0.7475 | 0.9264   |
| 0.0984        | 11.0  | 2640 | 0.2866          | 0.7462    | 0.7431 | 0.7446 | 0.9254   |
| 0.0984        | 12.0  | 2880 | 0.2982          | 0.7332    | 0.7561 | 0.7445 | 0.9250   |
| 0.08          | 13.0  | 3120 | 0.3123          | 0.7289    | 0.7584 | 0.7434 | 0.9252   |
| 0.08          | 14.0  | 3360 | 0.3167          | 0.7239    | 0.7633 | 0.7430 | 0.9237   |
| 0.0658        | 15.0  | 3600 | 0.3238          | 0.7408    | 0.7499 | 0.7453 | 0.9252   |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu126
- Datasets 3.6.0
- Tokenizers 0.22.1
