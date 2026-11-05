---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-85-ner
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
      name: Rodrigo1771/symptemist-85-ner
      type: Rodrigo1771/symptemist-85-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6646525679758308
    - name: Recall
      type: recall
      value: 0.722495894909688
    - name: F1
      type: f1
      value: 0.6923682140047207
    - name: Accuracy
      type: accuracy
      value: 0.9499021463633739
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-85-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2884
- Precision: 0.6647
- Recall: 0.7225
- F1: 0.6924
- Accuracy: 0.9499

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
| No log        | 1.0   | 174  | 0.1427          | 0.5737    | 0.6667 | 0.6167 | 0.9481   |
| No log        | 2.0   | 348  | 0.1535          | 0.6222    | 0.7050 | 0.6610 | 0.9492   |
| 0.1242        | 3.0   | 522  | 0.1802          | 0.6378    | 0.7181 | 0.6756 | 0.9486   |
| 0.1242        | 4.0   | 696  | 0.2066          | 0.6301    | 0.7263 | 0.6748 | 0.9466   |
| 0.1242        | 5.0   | 870  | 0.2270          | 0.6438    | 0.7181 | 0.6789 | 0.9476   |
| 0.0245        | 6.0   | 1044 | 0.2420          | 0.6445    | 0.7225 | 0.6813 | 0.9476   |
| 0.0245        | 7.0   | 1218 | 0.2623          | 0.6585    | 0.7252 | 0.6903 | 0.9491   |
| 0.0245        | 8.0   | 1392 | 0.2849          | 0.6513    | 0.7176 | 0.6828 | 0.9484   |
| 0.0086        | 9.0   | 1566 | 0.2880          | 0.6748    | 0.7088 | 0.6914 | 0.9504   |
| 0.0086        | 10.0  | 1740 | 0.2884          | 0.6647    | 0.7225 | 0.6924 | 0.9499   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
