---
license: mit
base_model: Clinical-AI-Apollo/Medical-NER
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Medical-NER-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Medical-NER-finetuned-ner

This model is a fine-tuned version of [Clinical-AI-Apollo/Medical-NER](https://huggingface.co/Clinical-AI-Apollo/Medical-NER) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2045
- Precision: 0.9394
- Recall: 0.9282
- F1: 0.9338
- Accuracy: 0.9296

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-06
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.37  | 100  | 0.4486          | 0.8318    | 0.8662 | 0.8486 | 0.8331   |
| No log        | 0.75  | 200  | 0.3747          | 0.8608    | 0.8834 | 0.8720 | 0.8646   |
| No log        | 1.12  | 300  | 0.3245          | 0.8801    | 0.8932 | 0.8866 | 0.8828   |
| No log        | 1.49  | 400  | 0.2846          | 0.9128    | 0.9038 | 0.9083 | 0.9028   |
| 0.4808        | 1.87  | 500  | 0.2554          | 0.9199    | 0.9067 | 0.9133 | 0.9083   |
| 0.4808        | 2.24  | 600  | 0.2480          | 0.9270    | 0.9073 | 0.9171 | 0.9102   |
| 0.4808        | 2.61  | 700  | 0.2269          | 0.9271    | 0.9172 | 0.9221 | 0.9171   |
| 0.4808        | 2.99  | 800  | 0.2319          | 0.9270    | 0.9089 | 0.9179 | 0.9129   |
| 0.4808        | 3.36  | 900  | 0.2303          | 0.9284    | 0.9088 | 0.9185 | 0.9133   |
| 0.2633        | 3.73  | 1000 | 0.2246          | 0.9311    | 0.9111 | 0.9210 | 0.9155   |
| 0.2633        | 4.1   | 1100 | 0.2120          | 0.9343    | 0.9218 | 0.9280 | 0.9236   |
| 0.2633        | 4.48  | 1200 | 0.2111          | 0.9361    | 0.9222 | 0.9291 | 0.9243   |
| 0.2633        | 4.85  | 1300 | 0.2152          | 0.9320    | 0.9185 | 0.9252 | 0.9208   |
| 0.2633        | 5.22  | 1400 | 0.2068          | 0.9333    | 0.9227 | 0.9280 | 0.9239   |
| 0.2218        | 5.6   | 1500 | 0.2070          | 0.9360    | 0.9256 | 0.9308 | 0.9267   |
| 0.2218        | 5.97  | 1600 | 0.2045          | 0.9394    | 0.9282 | 0.9338 | 0.9296   |
| 0.2218        | 6.34  | 1700 | 0.2020          | 0.9357    | 0.9275 | 0.9316 | 0.9284   |
| 0.2218        | 6.72  | 1800 | 0.2054          | 0.9354    | 0.9227 | 0.9290 | 0.9246   |
| 0.2218        | 7.09  | 1900 | 0.2053          | 0.9372    | 0.9253 | 0.9312 | 0.9269   |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.2+cu121
- Datasets 2.19.0
- Tokenizers 0.15.2
