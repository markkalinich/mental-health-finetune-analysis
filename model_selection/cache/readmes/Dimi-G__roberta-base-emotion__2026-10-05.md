---
library_name: transformers
tags:
- emotion
- text-classification
- pytorch
license: apache-2.0
datasets:
- dair-ai/emotion
language:
- en
metrics:
- accuracy
- f1
pipeline_tag: text-classification
---

# RoBERTa for Emotion Classification
## Model Description

This model is a fine-tuned version of `RoBERTaForSequenceClassification` trained to classify text into six emotion categories: Sadness, Joy, Love, Anger, Fear, and Surprise. 
- [RoBERTa](https://huggingface.co/docs/transformers/v4.41.3/en/model_doc/roberta#transformers.RobertaForSequenceClassification)
- Special thanks to [bhadresh-savani](https://huggingface.co/bhadresh-savani/roberta-base-emotion), whose notebook was the main guide for this work.

## Intended Use

The model is intended for classifying emotions in text data. It can be used in applications involving sentiment analysis, chatbots, social media monitoring, diary entries.

### Limitations

- The model is trained on a specific emotion dataset and may not generalize well to other datasets or domains.
- It might not perform well on text with mixed or ambiguous emotions.

## How to use the model 
```python
from transformers import pipeline
classifier = pipeline(model="Dimi-G/roberta-base-emotion")
emotions=classifier("i feel very happy and excited since i learned so many things", top_k=None)
print(emotions)

"""
Output:
[{'label': 'Joy', 'score': 0.9991986155509949},
 {'label': 'Love', 'score': 0.0003064649645239115},
 {'label': 'Sadness', 'score': 0.0001680034474702552},
 {'label': 'Anger', 'score': 0.00012623333896044642},
 {'label': 'Surprise', 'score': 0.00011396403715480119},
 {'label': 'Fear', 'score': 8.671794785186648e-05}]
"""
```

## Training Details

The model was trained on a randomized subset of the [dar-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset from the Hugging Face datasets library. Here are the training parameters:

- **Batch size**: 64
- **Number of epochs**: 10
- **Learning rate**: 5e-5
- **Warmup steps**: 500
- **Weight decay**: 0.03
- **Evaluation strategy**: epoch
- **Save strategy**: epoch
- **Metric for best model**: F1 score

## Evaluation
```python
{'eval_loss': 0.18195335566997528,
 'eval_accuracy': 0.94,
 'eval_f1': 0.9396676959491667,
 'eval_runtime': 1.1646,
 'eval_samples_per_second': 858.685,
 'eval_steps_per_second': 13.739,
 'epoch': 10.0}
```

## Model Resources
Link to the notebook with details on fine-tuning the model and our approach with other models for emotion classification:
- **Repository:** [Beginners Guide to Emotion Classification](https://github.com/Dimi-G/Capstone_Project/blob/main/Beginners_guide_to_emotion_classification.ipynb)


## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).


## Citation
- [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://huggingface.co/papers/1907.11692)

