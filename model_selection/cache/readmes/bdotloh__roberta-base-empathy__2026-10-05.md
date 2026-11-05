---
language: en
license: apache-2.0
datasets:
- empathic reactions to news stories
model-index:
- name: roberta-base-empathy
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: Reaction to News Stories
      type: Reaction to News Stories
      config: sst2
      split: validation
    metrics:
    - name: MSE loss
      type: MSE loss
      value: 7.07853364944458
    - name: Pearson's R (empathy)
      type: Pearson's R (empathy)
      value: 0.4336383660597612
    - name: Pearson's R (distress)
      type: Pearson's R (distress)
      value: 0.40006974689041663

---

# Roberta base finetuned on a dataset of empathic reactions to news stories (Buechel et al., 2018; Tafreshi et al., 2021, 2022)

## Table of Contents
- [Model Details](#model-details)
- [How to Get Started With the Model](#how-to-get-started-with-the-model)
- [Uses](#uses)
- [Risks, Limitations and Biases](#risks-limitations-and-biases)
- [Training](#training)

## Model Details
**Model Description:** This model is a fine-tuned checkpoint of [RoBERTA-base](https://huggingface.co/roberta-base), fine-tuned for Track 1 of the[WASSA 2022 Shared Task](https://aclanthology.org/2022.wassa-1.20.pdf) - predicting empathy and distress scores on a dataset of reactions to news stories.
This model attained an average Pearson's correlation (r) of 0.416854 on the dev set (for comparison, the top team had an average r of .54 on the test set ).

# Training

#### Training Data
An extended version of the [empathic reactions to news stories dataset](https://codalab.lisn.upsaclay.fr/competitions/834#learn_the_details-datasets)

###### Fine-tuning hyper-parameters


- learning_rate = 1e-5
- batch_size = 32
- warmup = 600
- max_seq_length = 128
- num_train_epochs = 3.0


