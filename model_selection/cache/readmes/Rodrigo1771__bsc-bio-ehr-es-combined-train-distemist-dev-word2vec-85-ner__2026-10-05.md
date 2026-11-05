---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/combined-train-distemist-dev-85-ner
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
      name: Rodrigo1771/combined-train-distemist-dev-85-ner
      type: Rodrigo1771/combined-train-distemist-dev-85-ner
      config: CombinedTrainDisTEMISTDevNER
      split: validation
      args: CombinedTrainDisTEMISTDevNER
    metrics:
    - name: Precision
      type: precision
      value: 0.3152508603513856
    - name: Recall
      type: recall
      value: 0.8144595226953674
    - name: F1
      type: f1
      value: 0.45455732567249935
    - name: Accuracy
      type: accuracy
      value: 0.8564886649182308
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/combined-train-distemist-dev-85-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7006
- Precision: 0.3153
- Recall: 0.8145
- F1: 0.4546
- Accuracy: 0.8565

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.3191        | 1.0   | 541  | 0.4772          | 0.2725    | 0.8074 | 0.4075 | 0.8443   |
| 0.1619        | 2.0   | 1082 | 0.4584          | 0.3041    | 0.7941 | 0.4398 | 0.8553   |
| 0.11          | 3.0   | 1623 | 0.6447          | 0.2976    | 0.8000 | 0.4338 | 0.8435   |
| 0.0764        | 4.0   | 2164 | 0.7413          | 0.2896    | 0.7871 | 0.4234 | 0.8399   |
| 0.0567        | 5.0   | 2705 | 0.7006          | 0.3153    | 0.8145 | 0.4546 | 0.8565   |
| 0.0428        | 6.0   | 3246 | 0.8112          | 0.3071    | 0.8210 | 0.4470 | 0.8504   |
| 0.0332        | 7.0   | 3787 | 0.9046          | 0.3114    | 0.8070 | 0.4494 | 0.8533   |
| 0.0257        | 8.0   | 4328 | 0.9723          | 0.3060    | 0.8109 | 0.4444 | 0.8482   |
| 0.022         | 9.0   | 4869 | 1.0028          | 0.3087    | 0.8077 | 0.4467 | 0.8502   |
| 0.0181        | 10.0  | 5410 | 1.0023          | 0.3116    | 0.8119 | 0.4504 | 0.8533   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
