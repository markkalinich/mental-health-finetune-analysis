---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/cantemist-fasttext-75-ner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: output
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: Rodrigo1771/cantemist-fasttext-75-ner
      type: Rodrigo1771/cantemist-fasttext-75-ner
      config: CantemistNer
      split: validation
      args: CantemistNer
    metrics:
    - name: Precision
      type: precision
      value: 0.8462436745815493
    - name: Recall
      type: recall
      value: 0.8562426152028357
    - name: F1
      type: f1
      value: 0.8512137823022711
    - name: Accuracy
      type: accuracy
      value: 0.991867253328732
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/cantemist-fasttext-75-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0478
- Precision: 0.8462
- Recall: 0.8562
- F1: 0.8512
- Accuracy: 0.9919

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0571        | 0.9992 | 616  | 0.0266          | 0.7767    | 0.8492 | 0.8113 | 0.9906   |
| 0.018         | 2.0    | 1233 | 0.0304          | 0.8075    | 0.8476 | 0.8271 | 0.9914   |
| 0.0101        | 2.9992 | 1849 | 0.0356          | 0.8159    | 0.8468 | 0.8311 | 0.9906   |
| 0.0057        | 4.0    | 2466 | 0.0365          | 0.8239    | 0.8460 | 0.8348 | 0.9910   |
| 0.0027        | 4.9992 | 3082 | 0.0396          | 0.8211    | 0.8480 | 0.8343 | 0.9916   |
| 0.0018        | 6.0    | 3699 | 0.0435          | 0.8306    | 0.8633 | 0.8467 | 0.9915   |
| 0.0013        | 6.9992 | 4315 | 0.0478          | 0.8462    | 0.8562 | 0.8512 | 0.9919   |
| 0.0008        | 8.0    | 4932 | 0.0469          | 0.8347    | 0.8614 | 0.8478 | 0.9915   |
| 0.0004        | 8.9992 | 5548 | 0.0515          | 0.8414    | 0.8610 | 0.8511 | 0.9919   |
| 0.0002        | 9.9919 | 6160 | 0.0520          | 0.8386    | 0.8598 | 0.8491 | 0.9918   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
