---
license: mit
base_model: roberta-base
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: roberta-base-suicide-prediction-phr-v2
  results:
  - task:
      type: text-classification
      name: Suicidal Tendency Prediction in text 
    dataset:
      type: vibhorag101/phr_suicide_prediction_dataset_clean_light
      name: Suicide Prediction Dataset
      split: val
    metrics:
      - type: accuracy
        value: 0.9869
      - type: f1
        value: 0.9875
      - type: recall
        value: 0.9846
      - type: precision
        value: 0.9904
datasets:
- vibhorag101/phr_suicide_prediction_dataset_clean_light
language:
- en
library_name: transformers
---


<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vibhorag101/roberta-base-suicide-prediction-phr-v2

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on [Suicide Prediction Dataset](https://huggingface.co/datasets/vibhorag101/phr_suicide_prediction_dataset_clean_light), sourced from Reddit.
It achieves the following results on the evaluation set:
- Loss: 0.0553
- Accuracy: 0.9869
- Recall: 0.9846
- Precision: 0.9904
- F1: 0.9875

## Model description
This model is a finetune of roberta-base to detect suicidal tendencies in a given text.

## Training and evaluation data
- The dataset is sourced from Reddit and is available on [Kaggle](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch).
- The dataset contains text with binary labels for suicide or non-suicide. 
- The dataset was cleaned minimally, as BERT depends on contextually sensitive information, which can worsely effect its performance.
  - Removed numbers
  - Removed URLs, Emojis, and accented characters.
  - Remove any extra white spaces and any extra spaces after a single space.
  - Removed any consecutive characters repeated more than 3 times.
  - The rows with more than 512 BERT Tokens were removed, as they exceeded BERT's max token.
- The cleaned dataset can be found [here](https://huggingface.co/datasets/vibhorag101/phr_suicide_prediction_dataset_clean_light)   
- The evaluation set had ~33k samples, while the training set had ~153k samples, i.e., a 70:15:15 (train:test:val) split.

## Training procedure
- The model was trained on an RTXA5000 GPU.

### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- weight_decay=0.1
- warmup_ratio: 0.06
- num_epochs: 3
- eval_steps: 500
- save_steps: 500
- Early Stopping:
  - early_stopping_patience: 5
  - early_stopping_threshold: 0.001
  - parameter: F1 Score

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Recall | Precision | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.1928        | 0.05  | 500  | 0.2289          | 0.9340   | 0.9062 | 0.9660    | 0.9352 |
| 0.0833        | 0.1   | 1000 | 0.1120          | 0.9752   | 0.9637 | 0.9888    | 0.9761 |
| 0.0366        | 0.16  | 1500 | 0.1165          | 0.9753   | 0.9613 | 0.9915    | 0.9762 |
| 0.071         | 0.21  | 2000 | 0.0973          | 0.9709   | 0.9502 | 0.9940    | 0.9716 |
| 0.0465        | 0.26  | 2500 | 0.0680          | 0.9829   | 0.9979 | 0.9703    | 0.9839 |
| 0.0387        | 0.31  | 3000 | 0.1583          | 0.9705   | 0.9490 | 0.9945    | 0.9712 |
| 0.1061        | 0.37  | 3500 | 0.0685          | 0.9848   | 0.9802 | 0.9907    | 0.9854 |
| 0.0593        | 0.42  | 4000 | 0.0550          | 0.9872   | 0.9947 | 0.9813    | 0.9879 |
| 0.0382        | 0.47  | 4500 | 0.0551          | 0.9871   | 0.9912 | 0.9842    | 0.9877 |
| 0.0831        | 0.52  | 5000 | 0.0502          | 0.9840   | 0.9768 | 0.9927    | 0.9847 |
| 0.0376        | 0.58  | 5500 | 0.0654          | 0.9865   | 0.9852 | 0.9889    | 0.9871 |
| 0.0634        | 0.63  | 6000 | 0.0422          | 0.9877   | 0.9897 | 0.9870    | 0.9883 |
| 0.0235        | 0.68  | 6500 | 0.0553          | 0.9869   | 0.9846 | 0.9904    | 0.9875 |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.1.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.0
