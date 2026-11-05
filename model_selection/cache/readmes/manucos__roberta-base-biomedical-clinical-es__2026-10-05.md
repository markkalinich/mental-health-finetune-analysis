---
license: apache-2.0
base_model: BSC-LT/roberta-base-biomedical-clinical-es
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: roberta-base-biomedical-clinical-es
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es

This model is a fine-tuned version of [BSC-LT/roberta-base-biomedical-clinical-es](https://huggingface.co/BSC-LT/roberta-base-biomedical-clinical-es) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3818
- Precision: 0.8662
- Recall: 0.8919
- F1: 0.8788
- Accuracy: 0.9366

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 280  | 0.3298          | 0.7938    | 0.8326 | 0.8127 | 0.9125   |
| 0.5032        | 2.0   | 560  | 0.2747          | 0.8433    | 0.8770 | 0.8598 | 0.9296   |
| 0.5032        | 3.0   | 840  | 0.2891          | 0.8499    | 0.8637 | 0.8567 | 0.9265   |
| 0.1441        | 4.0   | 1120 | 0.2790          | 0.8453    | 0.8904 | 0.8672 | 0.9338   |
| 0.1441        | 5.0   | 1400 | 0.3087          | 0.8519    | 0.8948 | 0.8728 | 0.9344   |
| 0.0841        | 6.0   | 1680 | 0.3025          | 0.8746    | 0.8993 | 0.8868 | 0.9383   |
| 0.0841        | 7.0   | 1960 | 0.3373          | 0.8656    | 0.8874 | 0.8764 | 0.9358   |
| 0.0481        | 8.0   | 2240 | 0.3364          | 0.8717    | 0.8859 | 0.8788 | 0.9372   |
| 0.0355        | 9.0   | 2520 | 0.3608          | 0.8576    | 0.8830 | 0.8701 | 0.9338   |
| 0.0355        | 10.0  | 2800 | 0.3800          | 0.8719    | 0.8874 | 0.8796 | 0.9344   |
| 0.0243        | 11.0  | 3080 | 0.3760          | 0.8637    | 0.8919 | 0.8776 | 0.9363   |
| 0.0243        | 12.0  | 3360 | 0.3718          | 0.8615    | 0.8844 | 0.8728 | 0.9349   |
| 0.0207        | 13.0  | 3640 | 0.3724          | 0.8644    | 0.8874 | 0.8757 | 0.9358   |
| 0.0207        | 14.0  | 3920 | 0.3848          | 0.8680    | 0.8963 | 0.8819 | 0.9372   |
| 0.017         | 15.0  | 4200 | 0.3818          | 0.8662    | 0.8919 | 0.8788 | 0.9366   |


### Framework versions

- Transformers 4.41.1
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
