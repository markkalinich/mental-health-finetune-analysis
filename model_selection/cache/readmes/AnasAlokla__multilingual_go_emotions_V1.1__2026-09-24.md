---
datasets:
- AnasAlokla/multilingual_go_emotions
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
- AnasAlokla/multilingual_go_emotions
new_version: AnasAlokla/multilingual_go_emotions
pipeline_tag: text-classification
license: mit
---

# 🌍 Multilingual GoEmotions Classifier 💬

[![Dataset](https://img.shields.io/badge/Dataset-multilingual_go_emotions-blue)](https://huggingface.co/datasets/AnasAlokla/multilingual_go_emotions)
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

- **Model Name**: AnasAlokla/multilingual_go_emotions_V1.1
- **Architecture**: BERT (bert-base-multilingual-cased)
- **Tasks**: Multi-Label Text Classification | Emotion Detection | Sentiment Analysis
- **Languages**: Arabic, English, French, Spanish, Dutch, Turkish

## Key Features

- 🌍 **Truly Multilingual**: Natively supports 6 major languages, making it ideal for global applications.
- 🏷️ **Multi-Label Classification**: Capable of detecting multiple emotions in a single piece of text, capturing complex emotional expressions.
- 💪 **High Performance**: Built on `bert-base-multilingual-cased`, delivering strong results across all supported languages and emotions. See the detailed [evaluation metrics](#evaluation).
- 🔗 **Open & Accessible**: Comes with a live demo, the full dataset, and the complete training code for full transparency and reproducibility.
- V1.1 **Improved Version**: An updated model is available that specifically improves performance on low-frequency emotion samples.

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
*   **Dataset (Supports 6 Languages):** [**multilingual_go_emotions**](https://huggingface.co/datasets/AnasAlokla/multilingual_go_emotions)
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
    model="AnasAlokla/multilingual_go_emotions",
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
## Performance of Test Model (using class weight)

| Labels          | accuracy | precision | recall | f1    | mcc   | support | threshold |
| :-------------- | :------- | :-------- | :----- | :---- | :---- | :------ | :-------- |
| admiration      | 0.933    | 0.598     | 0.668  | 0.631 | 0.596 | 2790    | 0.15      |
| amusement       | 0.967    | 0.682     | 0.793  | 0.733 | 0.718 | 1866    | 0.10      |
| anger           | 0.952    | 0.327     | 0.356  | 0.341 | 0.317 | 1128    | 0.15      |
| annoyance       | 0.908    | 0.223     | 0.301  | 0.256 | 0.211 | 1704    | 0.10      |
| approval        | 0.920    | 0.351     | 0.288  | 0.317 | 0.276 | 2094    | 0.15      |
| caring          | 0.970    | 0.381     | 0.303  | 0.337 | 0.325 | 816     | 0.20      |
| confusion       | 0.959    | 0.359     | 0.390  | 0.374 | 0.353 | 1020    | 0.25      |
| curiosity       | 0.933    | 0.405     | 0.552  | 0.467 | 0.438 | 1734    | 0.10      |
| desire          | 0.984    | 0.385     | 0.420  | 0.402 | 0.394 | 414     | 0.30      |
| disappointment  | 0.958    | 0.278     | 0.216  | 0.243 | 0.224 | 1014    | 0.40      |
| disapproval     | 0.920    | 0.221     | 0.343  | 0.269 | 0.235 | 1398    | 0.10      |
| disgust         | 0.972    | 0.302     | 0.383  | 0.338 | 0.326 | 600     | 0.15      |
| embarrassment   | 0.991    | 0.388     | 0.346  | 0.366 | 0.362 | 240     | 0.45      |
| excitement      | 0.968    | 0.248     | 0.333  | 0.285 | 0.272 | 624     | 0.10      |
| fear            | 0.985    | 0.501     | 0.526  | 0.513 | 0.506 | 498     | 0.20      |
| gratitude       | 0.988    | 0.913     | 0.894  | 0.903 | 0.897 | 2004    | 0.35      |
| grief           | 0.999    | 0.529     | 0.250  | 0.340 | 0.363 | 36      | 0.85      |
| joy             | 0.959    | 0.381     | 0.472  | 0.422 | 0.403 | 1032    | 0.15      |
| love            | 0.971    | 0.715     | 0.789  | 0.750 | 0.736 | 1812    | 0.25      |
| nervousness    | 0.996    | 0.430     | 0.283  | 0.342 | 0.347 | 120     | 0.70      |
| optimism        | 0.971    | 0.573     | 0.423  | 0.487 | 0.478 | 1062    | 0.45      |
| pride           | 0.997    | 0.468     | 0.262  | 0.336 | 0.349 | 84      | 0.25      |
| realization     | 0.967    | 0.220     | 0.146  | 0.176 | 0.163 | 792     | 0.25      |
| relief          | 0.993    | 0.117     | 0.094  | 0.104 | 0.102 | 138     | 0.10      |
| remorse         | 0.987    | 0.586     | 0.638  | 0.611 | 0.605 | 516     | 0.20      |
| sadness         | 0.960    | 0.415     | 0.519  | 0.461 | 0.444 | 1062    | 0.15      |
| surprise        | 0.975    | 0.518     | 0.425  | 0.467 | 0.457 | 828     | 0.60      |
| neutral         | 0.733    | 0.582     | 0.621  | 0.601 | 0.401 | 10524   | 0.10      |

### Test Model Performance (Threshold = 0.5)

The table below shows the performance of the test model with a threshold of 0.5:

| Labels          | accuracy | precision | recall | f1    | mcc   | support | threshold |
| :-------------- | :------- | :-------- | :----- | :---- | :---- | :------ | :-------- |
| admiration      | 0.939    | 0.673     | 0.570  | 0.617 | 0.587 | 2790    | 0.5       |
| amusement       | 0.967    | 0.735     | 0.666  | 0.699 | 0.682 | 1866    | 0.5       |
| anger           | 0.961    | 0.400     | 0.264  | 0.318 | 0.306 | 1128    | 0.5       |
| annoyance       | 0.940    | 0.328     | 0.137  | 0.194 | 0.185 | 1704    | 0.5       |
| approval        | 0.931    | 0.432     | 0.211  | 0.283 | 0.269 | 2094    | 0.5       |
| caring          | 0.973    | 0.431     | 0.246  | 0.314 | 0.313 | 816     | 0.5       |
| confusion       | 0.963    | 0.401     | 0.337  | 0.366 | 0.349 | 1020    | 0.5       |
| curiosity       | 0.944    | 0.463     | 0.361  | 0.406 | 0.380 | 1734    | 0.5       |
| desire          | 0.985    | 0.409     | 0.384  | 0.396 | 0.389 | 414     | 0.5       |
| disappointment  | 0.961    | 0.300     | 0.198  | 0.239 | 0.224 | 1014    | 0.5       |
| disapproval     | 0.945    | 0.293     | 0.195  | 0.234 | 0.212 | 1398    | 0.5       |
| disgust         | 0.978    | 0.376     | 0.267  | 0.312 | 0.306 | 600     | 0.5       |
| embarrassment   | 0.991    | 0.392     | 0.333  | 0.360 | 0.357 | 240     | 0.5       |
| excitement      | 0.977    | 0.348     | 0.204  | 0.257 | 0.255 | 624     | 0.5       |
| fear            | 0.986    | 0.547     | 0.468  | 0.504 | 0.499 | 498     | 0.5       |
| gratitude       | 0.988    | 0.925     | 0.879  | 0.902 | 0.896 | 2004    | 0.5       |
| grief           | 0.999    | 0.400     | 0.278  | 0.328 | 0.333 | 36      | 0.5       |
| joy             | 0.966    | 0.451     | 0.367  | 0.405 | 0.389 | 1032    | 0.5       |
| love            | 0.971    | 0.742     | 0.747  | 0.744 | 0.729 | 1812    | 0.5       |
| nervousness    | 0.996    | 0.382     | 0.283  | 0.325 | 0.327 | 120     | 0.5       |
| optimism        | 0.971    | 0.583     | 0.413  | 0.484 | 0.477 | 1062    | 0.5       |
| pride           | 0.997    | 0.500     | 0.190  | 0.276 | 0.308 | 84      | 0.5       |
| realization     | 0.971    | 0.270     | 0.124  | 0.170 | 0.169 | 792     | 0.5       |
| relief          | 0.995    | 0.125     | 0.029  | 0.047 | 0.058 | 138     | 0.5       |
| remorse         | 0.988    | 0.644     | 0.560  | 0.599 | 0.594 | 516     | 0.5       |
| sadness         | 0.968    | 0.512     | 0.408  | 0.454 | 0.441 | 1062    | 0.5       |
| surprise        | 0.974    | 0.492     | 0.430  | 0.459 | 0.447 | 828     | 0.5       |
| neutral         | 0.742    | 0.648     | 0.440  | 0.524 | 0.368 | 10524   | 0.5       |

## Use Cases

This model is ideal for applications requiring nuanced emotional understanding across different languages:

Global Customer Feedback Analysis: Analyze customer reviews, support tickets, and survey responses from around the world to gauge sentiment.

Multilingual Social Media Monitoring: Track brand perception and public mood across different regions and languages.

Advanced Chatbot Development: Build more empathetic and responsive chatbots that can understand user emotions in their native language.

Content Moderation: Automatically flag toxic, aggressive, or sensitive content on international platforms.

Market Research: Gain insights into how different cultures express emotions in text.

## Trained On

Base Model: [**AnasAlokla/multilingual_go_emotions**](https://huggingface.co/AnasAlokla/multilingual_go_emotions)  - A powerful pretrained model supporting 104 languages.

Dataset: [**multilingual_go_emotions**](https://huggingface.co/datasets/AnasAlokla/multilingual_go_emotions) - A carefully translated and curated dataset for multilingual emotion analysis, based on the original Google GoEmotions dataset.

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