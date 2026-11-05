---
license: mit
datasets:
- tweet_eval
- bookcorpus
- wikipedia
- cc_news
language:
- en
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- medical
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

Pretrained model on English language for text classification. Model trained from [tweet_emotion_eval](https://huggingface.co/elozano/tweet_emotion_eval) ([roberta-base](https://huggingface.co/roberta-base) fine-tuned on emotion task of [tweet_eval](https://huggingface.co/datasets/tweet_eval) dataset) on psychotherapy text transcripts.

Given a sentence, this model provides a binary classification as either symptomatic or non-symptomatic where symptomatic means the sentence displays signs of anxiety and/or depression.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Margot Wagner, Jasleen Jagayat, Anchan Kumar, Amir Shirazi, Nazanin Alavi, Mohsen Omrani
- **Funded by:** Queen's University
- **Model type:** RoBERTa
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** [elonzano/tweet_emotion_eval](https://huggingface.co/elozano/tweet_emotion_eval)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
This model is intended to be used to assess the mental health status using sentence-level text data. Specifically, it looks for symptoms related to anxiety and depression.

## How to Get Started with the Model

Use the code below to get started with the model.
```python
from transformers import pipeline

classifier = pipeline(task="text-classification", model="margotwagner/roberta-psychotherapy-eval")

sentences = ["I am not having a great day"]

model_outputs = classifier(sentences)
print(model_outputs[0])
# produces a list of dicts for each of the labels
```

## Training Details

### Training Data

This model was fine-tuned using English sentence-level data in a supervised manner where symptomatic labels were obtained from expert clinicians. Sentences were required to be independent in nature. Back-translation was utilized to increase the size of the training dataset.

### Training Procedure 

Weighted cross-entropy loss function was employed to address class imbalance. Model accuracy in the form of F1 was used for model selection.

### Metrics

F1 score was used as the model accuracy metric, as it maintains a balance between precision and recall with particular importance given to positive examples.
