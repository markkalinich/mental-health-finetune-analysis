---
license: cc-by-nc-sa-4.0
base_model: microsoft/layoutlmv3-base
tags:
- generated_from_trainer
datasets:
- my_csv_dataset3
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pharma_label_v3.1
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: my_csv_dataset3
      type: my_csv_dataset3
      config: discharge
      split: test
      args: discharge
    metrics:
    - name: Precision
      type: precision
      value: 0.9623287671232876
    - name: Recall
      type: recall
      value: 0.9740034662045061
    - name: F1
      type: f1
      value: 0.9681309216192937
    - name: Accuracy
      type: accuracy
      value: 0.9890616004605642
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pharma_label_v3.1

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the my_csv_dataset3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0671
- Precision: 0.9623
- Recall: 0.9740
- F1: 0.9681
- Accuracy: 0.9891

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 1500

### Training results

| Training Loss | Epoch   | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.2987  | 100  | 0.5492          | 0.7759    | 0.7140 | 0.7437 | 0.9102   |
| No log        | 2.5974  | 200  | 0.1522          | 0.9281    | 0.9393 | 0.9337 | 0.9747   |
| No log        | 3.8961  | 300  | 0.1063          | 0.9332    | 0.9445 | 0.9388 | 0.9793   |
| No log        | 5.1948  | 400  | 0.0891          | 0.9448    | 0.9497 | 0.9473 | 0.9810   |
| 0.375         | 6.4935  | 500  | 0.0879          | 0.9435    | 0.9549 | 0.9492 | 0.9839   |
| 0.375         | 7.7922  | 600  | 0.0908          | 0.9485    | 0.9584 | 0.9534 | 0.9822   |
| 0.375         | 9.0909  | 700  | 0.0764          | 0.9636    | 0.9636 | 0.9636 | 0.9862   |
| 0.375         | 10.3896 | 800  | 0.0819          | 0.9671    | 0.9671 | 0.9671 | 0.9873   |
| 0.375         | 11.6883 | 900  | 0.0802          | 0.9686    | 0.9636 | 0.9661 | 0.9873   |
| 0.0225        | 12.9870 | 1000 | 0.0602          | 0.9722    | 0.9705 | 0.9714 | 0.9902   |
| 0.0225        | 14.2857 | 1100 | 0.0989          | 0.9438    | 0.9601 | 0.9519 | 0.9816   |
| 0.0225        | 15.5844 | 1200 | 0.0859          | 0.9538    | 0.9671 | 0.9604 | 0.9839   |
| 0.0225        | 16.8831 | 1300 | 0.0781          | 0.9554    | 0.9653 | 0.9603 | 0.9856   |
| 0.0225        | 18.1818 | 1400 | 0.0653          | 0.9605    | 0.9705 | 0.9655 | 0.9891   |
| 0.0105        | 19.4805 | 1500 | 0.0671          | 0.9623    | 0.9740 | 0.9681 | 0.9891   |


### Framework versions

- Transformers 4.40.1
- Pytorch 2.2.1+cu121
- Datasets 2.19.0
- Tokenizers 0.19.1
