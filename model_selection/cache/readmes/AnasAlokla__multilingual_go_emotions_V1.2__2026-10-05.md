---
language:
- ar
- en
- fr
- es
- de
- tr
library_name: transformers
tags:
- emotion
- classification
- text-classification
- bert
- emojis
- emotions
- v1.0
- sentiment-analysis
- nlp
- chatbot
- social-media
- mental-health
- short-text
- emotion-detection
- transformers
- expressive
- ai
- machine-learning
- inference
- edge-ai
- smart-replies
- tone-analysis
metrics:
- accuracy
- f1
- recall
base_model:
- AnasAlokla/multilingual_go_emotions_V1.1
new_version: AnasAlokla/multilingual_go_emotions
pipeline_tag: text-classification
license: mit
---

# 🌍 Multilingual GoEmotions Classifier 💬

[![Languages](https://img.shields.io/badge/Languages-6-brightgreen)](https://huggingface.co/AnasAlokla/multilingual_go_emotions#key-features)
[![Task](https://img.shields.io/badge/Task-Multi--Label%20Classification%20%7C%20Emotion%20Detection%20%7C%20Text%20Classification%20%7C%20Sentiment%20Analysis-orange)](https://huggingface.co/AnasAlokla/multilingual_go_emotions#overview)
[![Base Model](https://img.shields.io/badge/Base%20Model-mBERT-purple)](https://huggingface.co/AnasAlokla/multilingual_go_emotions)

## Table of Contents
- 📖 [Overview](#overview)
- ✨ [Key Features](#key-features)
- 💫 [Supported Emotions](#supported-emotions)
- 🔗 [Links](#links)
- ⚙️ [Installation](#installation)
- 🚀 [Quickstart: Emotion Detection](#quickstart-emotion-detection)
- 📊 [Evaluation](#evaluation)
- 💡 [Use Cases](#use-cases)
- 📚 [Trained On](#trained-on)
- 🔧 [Fine-Tuning Guide](#fine-tuning-guide)
- 🏷️ [Tags](#tags)
- 💬 [Support & Contact](#support--contact)

## Overview

This repository contains a powerful **multilingual, multi-label emotion classification model**. It is fine-tuned from the robust `bert-base-multilingual-cased` model on the comprehensive `multilingual_go_emotions` dataset. The model is designed to analyze text and identify a wide spectrum of 27 different emotions, plus a neutral category. Its ability to detect multiple emotions simultaneously makes it highly effective for understanding nuanced text from diverse sources.

- **Model Name**: AnasAlokla/multilingual_go_emotions_V1.2
- **Architecture**: BERT (bert-base-multilingual-cased)
- **Tasks**: Multi-Label Text Classification | Emotion Detection | Sentiment Analysis
- **Languages**: Arabic, English, French, Spanish, Dutch, Turkish

## Key Features

- 🌍 **Truly Multilingual**: Natively supports 6 major languages, making it ideal for global applications.
- 🏷️ **Multi-Label Classification**: Capable of detecting multiple emotions in a single piece of text, capturing complex emotional expressions.
- 💪 **High Performance**: Built on `bert-base-multilingual-cased`, delivering strong results across all supported languages and emotions. See the detailed [evaluation metrics](#evaluation).
- 🔗 **Open & Accessible**: Comes with a live demo, the full dataset, and the complete training code for full transparency and reproducibility.
- V1.2 **Improved Version**: An updated model with an augmented dataset using LLMs.

## Supported Emotions

The model is trained to classify text into 27 distinct emotion categories as well as a neutral class:

| Emotion        | Emoji | Emotion        | Emoji |
|----------------|-------|----------------|-------|
| Admiration     | 🤩    | Love           | ❤️    |
| Amusement      | 😄    | Nervousness    | 😰    |
| Anger          | 😠    | Optimism       | ✨    |
| Annoyance      | 🙄    | Pride          | 👑    |
| Approval       | 👍    | Realization    | 💡    |
| Caring         | 🤗    | Relief         | 😌    |
| Confusion      | 😕    | Remorse        | 😔    |
| Curiosity      | 🤔    | Sadness        | 😢    |
| Desire         | 🔥    | Surprise       | 😲    |
| Disappointment | 😞    | Disapproval    | 👎    |
| Disgust        | 🤢    | Gratitude      | 🙏    |
| Embarrassment  | 😳    | Grief          | 😭    |
| Excitement     | 🎉    | Joy            | 😊    |
| Fear           | 😱    | Neutral        | 😐    |

## Links

*   **Live Demo:** [**Hugging Face Space**](https://huggingface.co/spaces/AnasAlokla/test_emotion_chatbot)
*   **Dataset (Supports 6 Languages):** the dataset augmented using LLMs model with  train: 6619306 samples, test: 825643 samples, validation: 825643 samples.
*   **Based Model Used:** [**AnasAlokla/multilingual_go_emotions**](https://huggingface.co/AnasAlokla/multilingual_go_emotions)
*   **GitHub Code:** [**emotion_chatbot**](https://github.com/anasAloklah/emotion_chatbot)

## Installation

Install the required libraries using pip:

```bash
pip install transformers torch
```
## Quickstart: Emotion Detection

You can easily use this model for multi-label emotion classification with the transformers pipeline. Set top_k=None to see all predicted emotions above the model's default threshold.

```python
from transformers import pipeline

# Load the multilingual, multi-label emotion classification pipeline
emotion_classifier = pipeline(
    "text-classification",
    model="multilingual_go_emotions_V1.2",
    top_k=None # To return all scores for each label
)

# --- Example 1: English ---
text_en = "I'm so happy for you, but I'm also a little bit sad to see you go."
results_en = emotion_classifier(text_en)
print(f"Text (EN): {text_en}")
print(f"Predictions: {results_en}\n")

# --- Example 2: Spanish ---
text_es = "¡Qué sorpresa! No me lo esperaba para nada."
results_es = emotion_classifier(text_es)
print(f"Text (ES): {text_es}")
print(f"Predictions: {results_es}\n")

# --- Example 3: Arabic ---
text_ar = "أشعر بخيبة أمل وغضب بسبب ما حدث"
results_ar = emotion_classifier(text_ar)
print(f"Text (AR): {text_ar}")
print(f"Predictions: {results_ar}")
```

Expected Output (structure):

Text (EN): I'm so happy for you, but I'm also a little bit sad to see you go.
Predictions: [[{'label': 'joy', 'score': 0.9...}, {'label': 'sadness', 'score': 0.8...}, {'label': 'caring', 'score': 0.5...}, ...]]

Text (ES): ¡Qué sorpresa! No me lo esperaba para nada.
Predictions: [[{'label': 'surprise', 'score': 0.9...}, {'label': 'excitement', 'score': 0.4...}, ...]]

Text (AR): أشعر بخيبة أمل وغضب بسبب ما حدث
Predictions: [[{'label': 'disappointment', 'score': 0.9...}, {'label': 'anger', 'score': 0.9...}, ...]]

## Evaluation

The model's performance was rigorously evaluated on the test set.

Test Set Performance

The following table shows the performance metrics of the fine-tuned model on the test set, broken down by emotion category.

The table below shows the performance of the test model:
## Performance of Test Model

| Labels          | accuracy | precision | recall | f1    | mcc   | support | threshold |
| :-------------- | :------- | :-------- | :----- | :---- | :---- | :------ | :-------- |
| admiration      | 0.988    | 0.956     | 0.942  | 0.949 | 0.942 | 96372   | 0.60      |
| amusement       | 0.989    | 0.951     | 0.936  | 0.943 | 0.937 | 81726   | 0.55      |
| anger           | 0.990    | 0.938     | 0.904  | 0.921 | 0.915 | 54456   | 0.65      |
| annoyance       | 0.976    | 0.891     | 0.856  | 0.873 | 0.860 | 78312   | 0.50      |
| approval        | 0.986    | 0.950     | 0.903  | 0.926 | 0.919 | 79992   | 0.65      |
| caring          | 0.992    | 0.958     | 0.936  | 0.947 | 0.943 | 64296   | 0.55      |
| confusion       | 0.989    | 0.941     | 0.913  | 0.927 | 0.921 | 64638   | 0.70      |
| curiosity       | 0.991    | 0.957     | 0.937  | 0.947 | 0.942 | 73308   | 0.70      |
| desire          | 0.992    | 0.953     | 0.934  | 0.943 | 0.939 | 59862   | 0.55      |
| disappointment  | 0.979    | 0.910     | 0.858  | 0.883 | 0.873 | 75726   | 0.60      |
| disapproval     | 0.982    | 0.900     | 0.879  | 0.890 | 0.880 | 67158   | 0.50      |
| disgust         | 0.992    | 0.954     | 0.919  | 0.936 | 0.932 | 54216   | 0.65      |
| embarrassment   | 0.994    | 0.949     | 0.931  | 0.940 | 0.936 | 44316   | 0.60      |
| excitement      | 0.988    | 0.922     | 0.899  | 0.910 | 0.904 | 55560   | 0.60      |
| fear            | 0.989    | 0.912     | 0.904  | 0.908 | 0.902 | 50658   | 0.50      |
| gratitude       | 0.996    | 0.976     | 0.979  | 0.978 | 0.976 | 74142   | 0.50      |
| grief           | 0.992    | 0.927     | 0.909  | 0.918 | 0.914 | 39426   | 0.60      |
| joy             | 0.983    | 0.913     | 0.886  | 0.899 | 0.890 | 72498   | 0.55      |
| love            | 0.994    | 0.967     | 0.955  | 0.961 | 0.957 | 68226   | 0.65      |
| nervousness     | 0.989    | 0.898     | 0.872  | 0.885 | 0.879 | 40146   | 0.60      |
| optimism        | 0.987    | 0.949     | 0.932  | 0.941 | 0.933 | 90498   | 0.65      |
| pride           | 0.997    | 0.955     | 0.952  | 0.954 | 0.952 | 30918   | 0.50      |
| realization     | 0.990    | 0.956     | 0.926  | 0.941 | 0.935 | 73908   | 0.55      |
| relief          | 0.997    | 0.966     | 0.955  | 0.960 | 0.959 | 31728   | 0.70      |
| remorse         | 0.995    | 0.966     | 0.949  | 0.957 | 0.955 | 49086   | 0.65      |
| sadness         | 0.980    | 0.906     | 0.872  | 0.889 | 0.877 | 77154   | 0.55      |
| surprise        | 0.989    | 0.928     | 0.904  | 0.916 | 0.910 | 56130   | 0.60      |
| neutral         | 0.981    | 0.920     | 0.876  | 0.898 | 0.887 | 79140   | 0.55      |

### Test Model Performance (Threshold = 0.5)

The table below shows the performance of the test model with a threshold of 0.5:

| Labels          | accuracy | precision | recall | f1    | mcc   | support | threshold |
| :-------------- | :------- | :-------- | :----- | :---- | :---- | :------ | :-------- |
| admiration      | 0.988    | 0.949     | 0.948  | 0.949 | 0.942 | 96372   | 0.5       |
| amusement       | 0.989    | 0.947     | 0.938  | 0.943 | 0.937 | 81726   | 0.5       |
| anger           | 0.989    | 0.921     | 0.917  | 0.919 | 0.913 | 54456   | 0.5       |
| annoyance       | 0.976    | 0.891     | 0.856  | 0.873 | 0.860 | 78312   | 0.5       |
| approval        | 0.986    | 0.937     | 0.915  | 0.926 | 0.918 | 79992   | 0.5       |
| caring          | 0.992    | 0.955     | 0.939  | 0.947 | 0.943 | 64296   | 0.5       |
| confusion       | 0.988    | 0.924     | 0.927  | 0.926 | 0.919 | 64638   | 0.5       |
| curiosity       | 0.990    | 0.943     | 0.946  | 0.945 | 0.939 | 73308   | 0.5       |
| desire          | 0.992    | 0.949     | 0.937  | 0.943 | 0.939 | 59862   | 0.5       |
| disappointment  | 0.979    | 0.894     | 0.872  | 0.883 | 0.871 | 75726   | 0.5       |
| disapproval     | 0.982    | 0.900     | 0.879  | 0.890 | 0.880 | 67158   | 0.5       |
| disgust         | 0.992    | 0.942     | 0.929  | 0.935 | 0.931 | 54216   | 0.5       |
| embarrassment   | 0.993    | 0.941     | 0.937  | 0.939 | 0.935 | 44316   | 0.5       |
| excitement      | 0.988    | 0.910     | 0.910  | 0.910 | 0.904 | 55560   | 0.5       |
| fear            | 0.989    | 0.912     | 0.904  | 0.908 | 0.902 | 50658   | 0.5       |
| gratitude       | 0.996    | 0.976     | 0.979  | 0.978 | 0.976 | 74142   | 0.5       |
| grief           | 0.992    | 0.916     | 0.919  | 0.918 | 0.913 | 39426   | 0.5       |
| joy             | 0.982    | 0.907     | 0.891  | 0.899 | 0.889 | 72498   | 0.5       |
| love            | 0.993    | 0.960     | 0.960  | 0.960 | 0.957 | 68226   | 0.5       |
| nervousness     | 0.989    | 0.881     | 0.886  | 0.884 | 0.878 | 40146   | 0.5       |
| optimism        | 0.987    | 0.938     | 0.941  | 0.940 | 0.932 | 90498   | 0.5       |
| pride           | 0.997    | 0.955     | 0.952  | 0.954 | 0.952 | 30918   | 0.5       |
| realization     | 0.989    | 0.952     | 0.928  | 0.940 | 0.934 | 73908   | 0.5       |
| relief          | 0.997    | 0.956     | 0.963  | 0.959 | 0.958 | 31728   | 0.5       |
| remorse         | 0.995    | 0.957     | 0.956  | 0.956 | 0.953 | 49086   | 0.5       |
| sadness         | 0.979    | 0.897     | 0.879  | 0.888 | 0.877 | 77154   | 0.5       |
| surprise        | 0.988    | 0.918     | 0.912  | 0.915 | 0.909 | 56130   | 0.5       |
| neutral         | 0.981    | 0.914     | 0.882  | 0.897 | 0.887 | 79140   | 0.5       |

## Use Cases

This model is ideal for applications requiring nuanced emotional understanding across different languages:

Global Customer Feedback Analysis: Analyze customer reviews, support tickets, and survey responses from around the world to gauge sentiment.

Multilingual Social Media Monitoring: Track brand perception and public mood across different regions and languages.

Advanced Chatbot Development: Build more empathetic and responsive chatbots that can understand user emotions in their native language.

Content Moderation: Automatically flag toxic, aggressive, or sensitive content on international platforms.

Market Research: Gain insights into how different cultures express emotions in text.

## Trained On

Base Model: [**AnasAlokla/multilingual_go_emotions**](https://huggingface.co/AnasAlokla/multilingual_go_emotions)  - A powerful pretrained model supporting 104 languages.

Dataset: specialized dataset based on the original Google GoEmotions dataset, augmented using LLMs.

## Fine-Tuning Guide

To adapt this model for your own dataset or to replicate the training process, you can follow the methodology outlined in the official code repository. The repository provides a complete, end-to-end example, including data preprocessing, training scripts, and evaluation logic.

For full details, please refer to the GitHub repository:
[**emotion_chatbot**](https://github.com/anasAloklah/emotion_chatbot)



## Tags

`#multilingual-nlp` `#emotion-classification` `#text-classification` `#multi-label` `#bert`
`#transformer` `#natural-language-processing` `#sentiment-analysis` `#deep-learning`
`#arabic-nlp` `#french-nlp` `#spanish-nlp` `#goemotions`
`#BERT-Emotion` `#edge-nlp` `#emotion-detection` `#offline-nlp`  
`#sentiment-analysis` `#emojis` `#emotions`  `#embedded-nlp` 
`#ai-for-iot` `#efficient-bert` `#nlp2025` `#context-aware` `#edge-ml`  
`#smart-home-ai` `#emotion-aware` `#voice-ai` `#eco-ai` `#chatbot` `#social-media`  
`#mental-health` `#short-text` `#smart-replies` `#tone-analysis`

## Support & Contact

For questions, bug reports, or collaboration inquiries, please open an issue on the Hugging Face Hub repository or contact the author directly.

Author: Anas Hamid Alokla

📬 Email: anasaloklahaaa@gmail.com