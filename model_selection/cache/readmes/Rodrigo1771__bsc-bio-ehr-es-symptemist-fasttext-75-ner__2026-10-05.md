---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-fasttext-75-ner
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
      name: Rodrigo1771/symptemist-fasttext-75-ner
      type: Rodrigo1771/symptemist-fasttext-75-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6784232365145229
    - name: Recall
      type: recall
      value: 0.715927750410509
    - name: F1
      type: f1
      value: 0.696671105193076
    - name: Accuracy
      type: accuracy
      value: 0.9490359010555359
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-fasttext-75-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3374
- Precision: 0.6784
- Recall: 0.7159
- F1: 0.6967
- Accuracy: 0.9490

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
| No log        | 1.0   | 258  | 0.1517          | 0.6354    | 0.6448 | 0.6400 | 0.9488   |
| 0.1357        | 2.0   | 516  | 0.2025          | 0.6306    | 0.7137 | 0.6696 | 0.9460   |
| 0.1357        | 3.0   | 774  | 0.2294          | 0.6649    | 0.7039 | 0.6839 | 0.9496   |
| 0.0238        | 4.0   | 1032 | 0.2818          | 0.6689    | 0.7066 | 0.6873 | 0.9492   |
| 0.0238        | 5.0   | 1290 | 0.2762          | 0.6528    | 0.7039 | 0.6774 | 0.9487   |
| 0.0081        | 6.0   | 1548 | 0.2938          | 0.6663    | 0.7203 | 0.6923 | 0.9484   |
| 0.0081        | 7.0   | 1806 | 0.3145          | 0.6789    | 0.7001 | 0.6893 | 0.9499   |
| 0.0039        | 8.0   | 2064 | 0.3267          | 0.6686    | 0.7055 | 0.6866 | 0.9491   |
| 0.0039        | 9.0   | 2322 | 0.3374          | 0.6784    | 0.7159 | 0.6967 | 0.9490   |
| 0.0021        | 10.0  | 2580 | 0.3400          | 0.6827    | 0.7077 | 0.6950 | 0.9495   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
