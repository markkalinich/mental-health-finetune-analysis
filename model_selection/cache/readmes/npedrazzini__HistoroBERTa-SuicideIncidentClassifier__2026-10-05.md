---
license: mit
datasets:
- npedrazzini/hist_suicide_incident
language:
- en
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- roberta-based
- historical newspaper
- late modern english
- text classification
- not-for-all-audiences
widget:
- text: >-
    On Wednesday evening an inquest was held at the Stag and Pheasant before
    Major Taylor, coroner, and a jury, of whom Mr. Joel Casson was foreman, on
    the body of John William Birks, grocer, of 23, Huddersfield Road, who cut
    his throat on Tuesday evening.
  example_title: Example 1
- text: >-
    The death-rate by accidents among colliers is, at least, from six to seven
    times as great as the death-rate from violence among the whole population,
    including suicides homicides, and the dangerous occupations.
  example_title: Example 2
---

# HistoroBERTa-SuicideIncidentClassifier

A binary classifier based on the RoBERTa-base architecture, fine-tuned on [historical British newspaper articles](https://huggingface.co/datasets/npedrazzini/hist_suicide_incident) to discern whether news reports discuss (confirmed or speculated) suicide cases, investigations, or court cases related to suicides. It attempts to differentiate between texts where _suicide_(_s_); or _suicidal_ is used in the context of actual incidents and those where these terms appear figuratively or in broader, non-specific discussions (e.g., mention of the number of suicides in the context of vital statistics; philosophical discussions around the morality of suicide at an abstract level; etc.).

# Overview
- **Model Name:** HistoroBERTa-SuicideIncidentClassifier
- **Task**: Binary Classification 
- **Labels**: ['Incident', 'Not Incident']
- **Base Model:** [RoBERTa (A Robustly Optimized BERT Pretraining Approach) base model](https://huggingface.co/FacebookAI/roberta-base)
- **Language:** 19th-century English (1780-1920)
- **Developed by:** [Nilo Pedrazzini](https://huggingface.co/npedrazzini), [Daniel CS Wilson](https://huggingface.co/dcsw2)

# Input Format
A `str`-type input.

# Output Format
The predicted label (`Incident` or `Not Incident`), with the confidence score for each labels.

# Examples

### Example 1:

**Input:**
```
On Wednesday evening an inquest was held at the Stag and Pheasant before Major Taylor, coroner, and a jury, of whom Mr. Joel Casson was foreman, on the body of John William Birks, grocer, of 23, Huddersfield Road, who cut his throat on Tuesday evening.
```

**Output:**
```
{
  'Incident': 0.974,
  'Not Incident': 0.026
}
```

### Example 2:

**Input:**
```
The death-rate by accidents among colliers is, at least, from six to seven times as great as the death-rate from violence among the whole population, including suicides homicides, and the dangerous occupations.
```

**Output:**
```
{
  'Not Incident': 0.577,
  'Incident': 0.423
}
```

# Uses
The classifier can be used, for instance, to obtain larger datasets reporting on cases of suicide in historical digitized newspapers, to then carry out larger-scale analyses on the language used in the reports.

# Bias, Risks, and Limitations

The classifier was trained on digitized newspaper data containing many OCR errors and, while text segmentation was meant to capture individual news articles, each labeled item in the training dataset very often spans multiple articles. This will necessarily have introduced bias in the model because of the extra content unrelated to reporting on suicide. 

&#9888; **NB**: We did not carry out a systematic evaluation of the effect of bad news article segmentation on the quality of the classifier.

# Training Details

This model was released upon comparison with other runs, and its selection was based on its accuracy on the evaluation set. 
Models based on RoBERTa were also compared to those based on [bert_1760_1900](https://huggingface.co/Livingwithmachines/bert_1760_1900), which achieved a slightly lower performance despite hyperparameter tuning.

In the following report, the model in this repository corresponds to the one labeled `roberta-7`, specifically the output of epoch 4, which returned the highest accuracy (>0.96).

<img src="https://cdn-uploads.huggingface.co/production/uploads/6342a31d5b97f509388807f3/KXqMD4Pchpmkee5CMFFYb.png" style="width: 90%;" />

## Training Data

https://huggingface.co/datasets/npedrazzini/hist_suicide_incident

# Model Card Authors

Nilo Pedrazzini

# Model Card Contact

npedrazzini@turing.ac.uk

# How to use the model

Use the code below to get started with the model.

Import and load the model:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "npedrazzini/HistoroBERTa-SuicideIncidentClassifier"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

Generate prediction:

```python
input_text = "The death-rate by accidents among colliers is, at least, from six to seven times as great as the death-rate from violence among the whole population, including suicides homicides, and the dangerous occupations.."
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
probabilities = logits.softmax(dim=-1)
```

Print predicted label:

```python
predicted_label_id = probabilities.argmax().item()
predicted_label = model.config.id2label[predicted_label_id]
print(predicted_label)
```

Output:

```
NotIncident
```

Print probability of each label:

```python
label_probabilities = {label: prob for label, prob in zip(model.config.id2label.values(), probabilities.squeeze().tolist())}
label_probabilities_sorted = dict(sorted(label_probabilities.items(), key=lambda item: item[1], reverse=True))
print(label_probabilities_sorted)
```

Output:

```
{'NotIncident': 0.5880260467529297, 'Incident': 0.4119739532470703}
```