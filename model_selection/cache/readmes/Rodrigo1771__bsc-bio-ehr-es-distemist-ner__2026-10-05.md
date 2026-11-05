---
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/distemist-ner
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
      name: Rodrigo1771/distemist-ner
      type: Rodrigo1771/distemist-ner
      config: DisTEMIST NER
      split: validation
      args: DisTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.7938948817994033
    - name: Recall
      type: recall
      value: 0.8093121197941039
    - name: F1
      type: f1
      value: 0.8015293708724366
    - name: Accuracy
      type: accuracy
      value: 0.9767668584453568
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/distemist-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1294
- Precision: 0.7939
- Recall: 0.8093
- F1: 0.8015
- Accuracy: 0.9768

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
| No log        | 0.9988 | 425  | 0.0738          | 0.7233    | 0.7866 | 0.7536 | 0.9733   |
| 0.0996        | 2.0    | 851  | 0.0787          | 0.7364    | 0.8065 | 0.7698 | 0.9743   |
| 0.0458        | 2.9988 | 1276 | 0.0788          | 0.7715    | 0.8154 | 0.7929 | 0.9759   |
| 0.0279        | 4.0    | 1702 | 0.0922          | 0.7754    | 0.8112 | 0.7929 | 0.9757   |
| 0.0169        | 4.9988 | 2127 | 0.0994          | 0.7585    | 0.8163 | 0.7863 | 0.9744   |
| 0.0114        | 6.0    | 2553 | 0.1080          | 0.7766    | 0.8058 | 0.7909 | 0.9765   |
| 0.0114        | 6.9988 | 2978 | 0.1166          | 0.7792    | 0.8100 | 0.7943 | 0.9760   |
| 0.0079        | 8.0    | 3404 | 0.1294          | 0.7939    | 0.8093 | 0.8015 | 0.9768   |
| 0.0053        | 8.9988 | 3829 | 0.1340          | 0.7876    | 0.8105 | 0.7989 | 0.9766   |
| 0.0038        | 9.9882 | 4250 | 0.1367          | 0.7882    | 0.8098 | 0.7988 | 0.9767   |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1
