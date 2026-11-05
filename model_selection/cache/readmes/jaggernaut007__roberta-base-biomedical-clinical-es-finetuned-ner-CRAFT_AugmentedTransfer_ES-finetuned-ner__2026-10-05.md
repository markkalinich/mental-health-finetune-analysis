---
license: apache-2.0
base_model: StivenLancheros/roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_AugmentedTransfer_ES
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_AugmentedTransfer_ES-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_AugmentedTransfer_ES-finetuned-ner

This model is a fine-tuned version of [StivenLancheros/roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_AugmentedTransfer_ES](https://huggingface.co/StivenLancheros/roberta-base-biomedical-clinical-es-finetuned-ner-CRAFT_AugmentedTransfer_ES) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2282
- Precision: 0.9407
- Recall: 0.9284
- F1: 0.9345
- Accuracy: 0.9271

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
| No log        | 0.37  | 100  | 0.7545          | 0.7917    | 0.8473 | 0.8186 | 0.7901   |
| No log        | 0.75  | 200  | 0.5437          | 0.8113    | 0.8586 | 0.8343 | 0.8102   |
| No log        | 1.12  | 300  | 0.4143          | 0.8746    | 0.8822 | 0.8784 | 0.8678   |
| No log        | 1.49  | 400  | 0.3410          | 0.9114    | 0.8919 | 0.9015 | 0.8937   |
| 0.625         | 1.87  | 500  | 0.3050          | 0.9128    | 0.8935 | 0.9030 | 0.8958   |
| 0.625         | 2.24  | 600  | 0.2825          | 0.9171    | 0.9005 | 0.9087 | 0.9020   |
| 0.625         | 2.61  | 700  | 0.2688          | 0.9195    | 0.9060 | 0.9127 | 0.9059   |
| 0.625         | 2.99  | 800  | 0.2610          | 0.9244    | 0.9044 | 0.9143 | 0.9078   |
| 0.625         | 3.36  | 900  | 0.2537          | 0.9261    | 0.9070 | 0.9165 | 0.9099   |
| 0.2911        | 3.73  | 1000 | 0.2498          | 0.9285    | 0.9128 | 0.9206 | 0.9141   |
| 0.2911        | 4.1   | 1100 | 0.2437          | 0.9283    | 0.9150 | 0.9216 | 0.9154   |
| 0.2911        | 4.48  | 1200 | 0.2396          | 0.9295    | 0.9183 | 0.9239 | 0.9178   |
| 0.2911        | 4.85  | 1300 | 0.2385          | 0.9324    | 0.9198 | 0.9261 | 0.9195   |
| 0.2911        | 5.22  | 1400 | 0.2354          | 0.9344    | 0.9223 | 0.9283 | 0.9214   |
| 0.2505        | 5.6   | 1500 | 0.2343          | 0.9347    | 0.9223 | 0.9285 | 0.9216   |
| 0.2505        | 5.97  | 1600 | 0.2343          | 0.9362    | 0.9234 | 0.9297 | 0.9224   |
| 0.2505        | 6.34  | 1700 | 0.2318          | 0.9368    | 0.9251 | 0.9310 | 0.9238   |
| 0.2505        | 6.72  | 1800 | 0.2301          | 0.9375    | 0.9265 | 0.9319 | 0.9250   |
| 0.2505        | 7.09  | 1900 | 0.2304          | 0.9379    | 0.9263 | 0.9321 | 0.9250   |
| 0.2219        | 7.46  | 2000 | 0.2283          | 0.9387    | 0.9283 | 0.9335 | 0.9265   |
| 0.2219        | 7.84  | 2100 | 0.2305          | 0.9392    | 0.9265 | 0.9328 | 0.9254   |
| 0.2219        | 8.21  | 2200 | 0.2299          | 0.9398    | 0.9268 | 0.9332 | 0.9257   |
| 0.2219        | 8.58  | 2300 | 0.2289          | 0.9398    | 0.9277 | 0.9337 | 0.9264   |
| 0.2219        | 8.96  | 2400 | 0.2282          | 0.9407    | 0.9284 | 0.9345 | 0.9271   |
| 0.219         | 9.33  | 2500 | 0.2281          | 0.9407    | 0.9287 | 0.9347 | 0.9274   |
| 0.219         | 9.7   | 2600 | 0.2277          | 0.9403    | 0.9287 | 0.9345 | 0.9275   |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.2+cu121
- Datasets 2.19.0
- Tokenizers 0.15.2
