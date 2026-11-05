---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
widget:
- text: "I struggle with my relationship with food and my body image, often feeling guilt or shame after eating."
  example_title: "EDAnonymous Example"
- text: "I have a dependency on substances or behaviors, and I find it difficult to control my urges or cravings."
  example_title: "Addiction Example"
- text: "I have a problem with alcohol and find it hard to limit my drinking despite negative consequences."
  example_title: "Alcoholism Example"
- text: "I have difficulty focusing, organizing tasks, and managing my time, which often leads to forgetfulness and impulsivity."
  example_title: "ADHD Example"
- text: "I experience excessive worry or fear in everyday situations, often leading to physical symptoms like rapid heartbeat or sweating."
  example_title: "Anxiety Example"
- text: "I have challenges with social skills, communication, and repetitive behaviors, and I often prefer routines and sameness."
  example_title: "Autism Example"
- text: "I experience extreme mood swings that include emotional highs (mania or hypomania) and lows (depression)."
  example_title: "Bipolar Disorder Example"
- text: "I have intense and unstable emotions, self-image, and relationships, often leading to impulsive and self-destructive behavior."
  example_title: "BPD Example"
- text: "I feel persistently sad, hopeless, and lose interest in activities I once enjoyed, often accompanied by sleep and appetite changes."
  example_title: "Depression Example"
- text: "I am excessively worried about having a serious illness despite medical reassurance, often leading to frequent checking of symptoms."
  example_title: "Health Anxiety Example"
- text: "I feel isolated and disconnected from others, longing for meaningful relationships and struggling with feelings of emptiness."
  example_title: "Loneliness Example"
- text: "I have flashbacks, nightmares, and severe anxiety as a result of a past traumatic event, often leading to avoidance of triggers."
  example_title: "PTSD Example"
- text: "I experience hallucinations, delusions, and disorganized thinking, often causing me to withdraw from reality and society."
  example_title: "Schizophrenia Example"
- text: "I feel overwhelming anxiety and self-consciousness in social situations, fearing judgment and embarrassment."
  example_title: "Social Anxiety Example"
- text: "I have thoughts of ending my own life, feeling hopeless and believing that others would be better off without me."
  example_title: "Suicide Watch Example"
---
# Mental Health Text Classification Model v0.2

## !! Accuracy: 69.87% !!

This model is designed to classify texts into different mental health categories. It uses 2% of the dataset from the following study:

@article{low2020natural,\
title={Natural Language Processing Reveals Vulnerable Mental Health Support Groups and Heightened Health Anxiety on Reddit During COVID-19: Observational Study},\
  author={Low, Daniel M and Rumker, Laurie and Torous, John and Cecchi, Guillermo and Ghosh, Satrajit S and Talkar, Tanya},\
  journal={Journal of medical Internet research},\
  volume={22},\
  number={10},\
  pages={e22635},\
  year={2020},\
  publisher={JMIR Publications Inc., Toronto, Canada}\
}

## Model Details

This model is fine-tuned to classify texts into the following mental health categories:
- EDAnonymous
- addiction
- alcoholism
- adhd
- anxiety
- autism
- bipolarreddit
- bpd
- depression
- healthanxiety
- lonely
- ptsd
- schizophrenia
- socialanxiety
- suicidewatch

### Example Usage

An example usage of the model is:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("tahaenesaslanturk/mental-health-classification-v0.2")
model = AutoModelForSequenceClassification.from_pretrained("tahaenesaslanturk/mental-health-classification-v0.2")

# Encode the input text
input_text = "I struggle with my relationship with food and my body image, often feeling guilt or shame after eating."
inputs = tokenizer(input_text, return_tensors="pt")

# Perform inference
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted label
predicted_label = torch.argmax(outputs.logits, dim=1).item()
label = model.config.id2label[predicted_label]

print(f"Predicted label: {label}")
```
