---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-fasttext-9-ner
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
      name: Rodrigo1771/symptemist-fasttext-9-ner
      type: Rodrigo1771/symptemist-fasttext-9-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6659969864389754
    - name: Recall
      type: recall
      value: 0.7257799671592775
    - name: F1
      type: f1
      value: 0.6946045049764275
    - name: Accuracy
      type: accuracy
      value: 0.9496615226667522
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-fasttext-9-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2450
- Precision: 0.6660
- Recall: 0.7258
- F1: 0.6946
- Accuracy: 0.9497

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
| No log        | 0.9968 | 155  | 0.1485          | 0.5669    | 0.6218 | 0.5931 | 0.9436   |
| No log        | 2.0    | 311  | 0.1609          | 0.5623    | 0.7159 | 0.6299 | 0.9409   |
| No log        | 2.9968 | 466  | 0.1635          | 0.6210    | 0.7219 | 0.6677 | 0.9487   |
| 0.1246        | 4.0    | 622  | 0.2047          | 0.6659    | 0.6765 | 0.6712 | 0.9493   |
| 0.1246        | 4.9968 | 777  | 0.2134          | 0.6562    | 0.7115 | 0.6828 | 0.9480   |
| 0.1246        | 6.0    | 933  | 0.2259          | 0.6518    | 0.7099 | 0.6796 | 0.9494   |
| 0.0242        | 6.9968 | 1088 | 0.2450          | 0.6660    | 0.7258 | 0.6946 | 0.9497   |
| 0.0242        | 8.0    | 1244 | 0.2650          | 0.6491    | 0.7230 | 0.6841 | 0.9491   |
| 0.0242        | 8.9968 | 1399 | 0.2745          | 0.6646    | 0.7126 | 0.6878 | 0.9498   |
| 0.0083        | 9.9678 | 1550 | 0.2774          | 0.6628    | 0.7187 | 0.6896 | 0.9503   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
