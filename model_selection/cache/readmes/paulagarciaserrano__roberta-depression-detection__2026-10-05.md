---
language: "en"
datasets:
- Shared task on Detecting Signs of Depression from Social Media Text at LT-EDI 2022-ACL 2022
metrics:
- Macro F1-Score
---

# Roberta for depression signs detection

This model is a fine-tuned version the <a href="https://huggingface.co/cardiffnlp/twitter-roberta-base">cardiffnlp/twitter-roberta-base</a> model. It has been trained using a recently published corpus: <a href="https://competitions.codalab.org/competitions/36410#learn_the_details">Shared task on Detecting Signs of Depression from Social Media Text at LT-EDI 2022-ACL 2022</a>. 

The obtained macro f1-score is 0.54, on the development set of the competition.

# Intended uses
This model is trained to classify the given text into one of the following classes: *moderate*, *severe*, or *not depression*.
It corresponds to a **multiclass classification** task.

# How to use

You can use this model directly with a pipeline for text classification:

```python
>>> from transformers import pipeline
>>> classifier = pipeline("text-classification", model="paulagarciaserrano/roberta-depression-detection")
>>> your_text = "I am very sad."
>>> classifier (your_text)
```

# Training and evaluation data
The **train** dataset characteristics are:

<table>
  <tr>
    <th>Class</th>
    <th>Nº sentences</th>
    <th>Avg. document length (in sentences)</th>
    <th>Nº words</th>
    <th>Avg. sentence length (in words)</th>
  </tr>
  <tr>
    <th>not depression</th>
    <td>7,884</td>
    <td>4</td>
    <td>153,738</td>
    <td>78</td>
  </tr>
  <tr>
    <th>moderate</th>
    <td>36,114</td>
    <td>6</td>
    <td>601,900</td>
    <td>100</td>
  </tr>
  <tr>
    <th>severe</th>
    <td>9,911</td>
    <td>11</td>
    <td>126,140</td>
    <td>140</td>
  </tr>
</table>

Similarly, the **evaluation** dataset characteristics are:

<table>
  <tr>
    <th>Class</th>
    <th>Nº sentences</th>
    <th>Avg. document length (in sentences)</th>
    <th>Nº words</th>
    <th>Avg. sentence length (in words)</th>
  </tr>
  <tr>
    <th>not depression</th>
    <td>3,660</td>
    <td>2</td>
    <td>10,980</td>
    <td>6</td>
  </tr>
  <tr>
    <th>moderate</th>
    <td>66,874</td>
    <td>29</td>
    <td>804,794</td>
    <td>349</td>
  </tr>
  <tr>
    <th>severe</th>
    <td>2,880</td>
    <td>8</td>
    <td>75,240</td>
    <td>209</td>
  </tr>
</table>

# Training hyperparameters
The following hyperparameters were used during training:

* learning_rate: 2e-05
* evaluation_strategy: epoch
* save_strategy: epoch
* per_device_train_batch_size: 8
* per_device_eval_batch_size: 8
* num_train_epochs: 5
* seed: 10
* weight_decay: 0.01
* metric_for_best_model: macro-f1