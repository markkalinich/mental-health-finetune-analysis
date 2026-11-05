---
language: "en"
license: apache-2.0
tags:
- financial-sentiment-analysis
- sentiment-analysis
- language-perceiver
datasets:
- financial_phrasebank
widget:
- text: "INDEX100 fell sharply today."
- text: "ImaginaryJetCo bookings hit by Omicron variant as losses total £1bn."
- text: "Q1 ImaginaryGame's earnings beat expectations."
- text: "Should we buy IMAGINARYSTOCK today?"
metrics:
- recall
- f1
- accuracy
- precision
model-index:
- name: fin-perceiver
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: financial_phrasebank
      type: financial_phrasebank
      args: sentences_50agree
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8624
    - name: F1
      type: f1
      value: 0.8416
      args: macro
    - name: Precision
      type: precision
      value: 0.8438
      args: macro
    - name: Recall
      type: recall
      value: 0.8415
      args: macro
---

# FINPerceiver
FINPerceiver is a fine-tuned Perceiver IO language model for financial sentiment analysis.
More details on the training process of this model are available on the [GitHub repository](https://github.com/warwickai/fin-perceiver).

Weights & Biases was used to track experiments.

We achieved the following results with 10-fold cross validation.

```
eval/accuracy  0.8624 (stdev 0.01922)
eval/f1        0.8416 (stdev 0.03738)
eval/loss      0.4314 (stdev 0.05295)
eval/precision 0.8438 (stdev 0.02938)
eval/recall    0.8415 (stdev 0.04458)
```

The hyperparameters used are as follows.

```
per_device_train_batch_size  16
per_device_eval_batch_size   16
num_train_epochs             4
learning_rate                2e-5
```

## Datasets
This model was trained on the Financial PhraseBank (>= 50% agreement)
