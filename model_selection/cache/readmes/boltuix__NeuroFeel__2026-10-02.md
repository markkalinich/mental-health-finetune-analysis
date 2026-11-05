---
license: apache-2.0
language:
- en
metrics:
- precision
- recall
- f1
- accuracy
new_version: v1.0
datasets:
- custom
- chatgpt
pipeline_tag: text-classification
library_name: transformers
tags:
- emotion
- classification
- text-classification
- neurobert
- emojis
- emotions
- v1.0
- sentiment-analysis
- nlp
- lightweight
- chatbot
- social-media
- mental-health
- short-text
- emotion-detection
- transformers
- real-time
- expressive
- ai
- machine-learning
- english
- inference
- edge-ai
- smart-replies
- tone-analysis
- contextual-ai
- wearable-ai
base_model:
- neurobert
---

![Banner](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg0UoTe9pAO9rk0G-WYMo1YGlo7MCuQOIXNQR6d8hw8fxNGecfplPs904kZfkCY7EQW-YsvXLQoHBuHD_OXOieiCliKzoMNRdxxWmbWKWNU1hK5NKJMH5ycl1npJamFDUOUG52CIHxsiMhqs0gq_QsiDfXOev51F8_gtC34ZOHTYsMoomV5KjuaatjKIq8/s16000/NEURO-FEEL%20(1).jpg)

# 😊 NeuroFeel — Lightweight NeuroBERT for Real-Time Emotion Detection 🌟

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Model Size](https://img.shields.io/badge/Size-~25MB-blue)](#)
[![Tasks](https://img.shields.io/badge/Tasks-Emotion%20Detection%20%7C%20Text%20Classification%20%7C%20Sentiment%20Analysis-orange)](#)
[![Inference Speed](https://img.shields.io/badge/Optimized%20For-Edge%20Devices-green)](#)

## Table of Contents
- 📖 [Overview](#overview)
- ✨ [Key Features](#key-features)
- 💫 [Supported Emotions](#supported-emotions)
- 🧠 [Model Architecture](#model-architecture)
- ⚙️ [Installation](#installation)
- 📥 [Download Instructions](#download-instructions)
- 🚀 [Quickstart: Emotion Detection](#quickstart-emotion-detection)
- 💡 [Use Cases](#use-cases)
- 🖥️ [Hardware Requirements](#hardware-requirements)
- 📚 [Training Details](#training-details)
- 🔧 [Fine-Tuning Guide](#fine-tuning-guide)
- ⚖️ [Comparison to Other Models](#comparison-to-other-models)
- 🏷️ [Tags](#tags)
- 📄 [License](#license)
- 🙏 [Credits](#credits)
- 💬 [Support & Community](#support--community)
- ✍️ [Contact](#contact)



## 🚀 Model Training Tutorial Video

Watch this **step-by-step guide** to train your machine learning model! 🎥

[![YouTube Video](https://img.youtube.com/vi/FccGKE1kV4Q/hqdefault.jpg)](https://www.youtube.com/watch?v=FccGKE1kV4Q)

*Click the image above to watch the tutorial!*


## Overview

`NeuroFeel` is a **lightweight** NLP model built on **NeuroBERT**, fine-tuned for **short-text emotion detection** on **edge and IoT devices**. With a quantized size of **~25MB** and **~7M parameters**, it classifies text into **13 nuanced emotional categories** (e.g., Happiness, Sadness, Anger, Love) with high precision. Optimized for **low-latency** and **offline operation**, NeuroFeel is perfect for privacy-focused applications like chatbots, social media sentiment analysis, mental health monitoring, and contextual AI in resource-constrained environments such as wearables, smart home devices, and mobile apps.

- **Model Name**: NeuroFeel
- **Size**: ~25MB (quantized)
- **Parameters**: ~7M
- **Architecture**: Lightweight NeuroBERT (4 layers, hidden size 256, 8 attention heads)
- **Description**: Compact 4-layer, 256-hidden model for emotion detection
- **License**: Apache-2.0 — free for commercial and personal use

## Key Features

- ⚡ **Ultra-Compact Design**: ~25MB footprint for devices with limited storage.
- 🧠 **Rich Emotion Detection**: Classifies 13 emotions with expressive emoji mappings.
- 📶 **Offline Capability**: Fully functional without internet connectivity.
- ⚙️ **Real-Time Inference**: Optimized for CPUs, mobile NPUs, and microcontrollers.
- 🌍 **Versatile Applications**: Supports emotion detection, sentiment analysis, and tone analysis for short texts.
- 🔒 **Privacy-First**: On-device processing ensures user data stays local.

## Supported Emotions

NeuroFeel classifies text into one of 13 emotional categories, each paired with an emoji for enhanced interpretability:

| Emotion    | Emoji |
|------------|-------|
| Sadness    | 😢    |
| Anger      | 😠    |
| Love       | ❤️    |
| Surprise   | 😲    |
| Fear       | 😱    |
| Happiness  | 😄    |
| Neutral    | 😐    |
| Disgust    | 🤢    |
| Shame      | 🙈    |
| Guilt      | 😔    |
| Confusion  | 😕    |
| Desire     | 🔥    |
| Sarcasm    | 😏    |

## Model Architecture

NeuroFeel is derived from **NeuroBERT**, a lightweight transformer model optimized for edge computing. Key architectural details:

- **Layers**: 4 transformer layers for reduced computational complexity.
- **Hidden Size**: 256, balancing expressiveness and efficiency.
- **Attention Heads**: 8, enabling robust contextual understanding.
- **Parameters**: ~7M, significantly fewer than standard BERT models.
- **Quantization**: INT8 quantization for minimal memory usage and fast inference.
- **Vocabulary Size**: 30,522 tokens, compatible with NeuroBERT’s tokenizer.
- **Max Sequence Length**: 64 tokens, ideal for short-text inputs like social media posts or chatbot messages.

This architecture ensures NeuroFeel delivers high accuracy for emotion detection while maintaining compatibility with resource-constrained devices like Raspberry Pi, ESP32, or mobile NPUs.

## Installation

Install the required dependencies:

```bash
pip install transformers torch
```

Ensure your environment supports Python 3.6+ and has ~25MB of storage for model weights.

## Download Instructions

1. **Via Hugging Face**:
   - Access the model at [boltuix/NeuroFeel](https://huggingface.co/boltuix/NeuroFeel).
   - Download the model files (~25MB) or clone the repository:
     ```bash
     git clone https://huggingface.co/boltuix/NeuroFeel
     ```
2. **Via Transformers Library**:
   - Load the model directly in Python:
     ```python
     from transformers import AutoModelForSequenceClassification, AutoTokenizer
     model = AutoModelForSequenceClassification.from_pretrained("boltuix/NeuroFeel")
     tokenizer = AutoTokenizer.from_pretrained("boltuix/NeuroFeel")
     ```
3. **Manual Download**:
   - Download quantized model weights (Safetensors format) from the Hugging Face model hub.
   - Extract and integrate into your edge/IoT application.


4. **Dataset Download**:
![Banner](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYNXFTjcbG7QmV32WTE67vnrTDBOGjR3YtQvhHilQA9YzJBxC96CBpQzLSILuNH3Z4A0LS10SG3sfsnWLLjbcq3RpIqxkn-KToMTGTeeO-QeBYux28IpqoMYShHw9QP0NlDGSPdtE3_o7mYGN8fYZEqh9omisiLVQPqthProhe9MBJPnw0ha19wj2hjqg/s4000/emotions-dataset-banner.jpg)

# 🌟 Emotions Dataset — Infuse Your AI with Human Feelings! 😊😢😡

**[Start Exploring Dataset](https://huggingface.co/datasets/boltuix/emotions-dataset)** 🚀



## Quickstart: Emotion Detection

### Basic Inference Example
Classify emotions in short text inputs using the Hugging Face pipeline:

```python
from transformers import pipeline

# Load the fine-tuned NeuroFeel model
sentiment_analysis = pipeline("text-classification", model="boltuix/NeuroFeel")

# Analyze emotion
result = sentiment_analysis("i love you")
print(result)
```

**Output**:
```python
[{'label': 'Love', 'score': 0.8563215732574463}]
```

This indicates the emotion is **Love ❤️** with **85.63%** confidence.

### Extended Example with Emoji Mapping
Enhance the output with human-readable emotions and emojis:

```python
from transformers import pipeline

# Load the fine-tuned NeuroFeel model
sentiment_analysis = pipeline("text-classification", model="boltuix/NeuroFeel")

# Define label-to-emoji mapping
label_to_emoji = {
    "Sadness": "😢",
    "Anger": "😠",
    "Love": "❤️",
    "Surprise": "😲",
    "Fear": "😱",
    "Happiness": "😄",
    "Neutral": "😐",
    "Disgust": "🤢",
    "Shame": "🙈",
    "Guilt": "😔",
    "Confusion": "😕",
    "Desire": "🔥",
    "Sarcasm": "😏"
}

# Input text
text = "i love you"

# Analyze emotion
result = sentiment_analysis(text)[0]
label = result["label"].capitalize()
emoji = label_to_emoji.get(label, "❓")

# Output
print(f"Text: {text}")
print(f"Predicted Emotion: {label} {emoji}")
print(f"Confidence: {result['score']:.2%}")
```

**Output**:
```plaintext
Text: i love you
Predicted Emotion: Love ❤️
Confidence: 85.63%
```

*Note*: Fine-tune the model for domain-specific tasks to boost accuracy.



NeuroFeel excels in classifying a wide range of emotions in short texts, particularly in IoT, social media, and mental health contexts. Fine-tuning enhances performance on subtle emotions like Sarcasm or Shame.

### Evaluation Metrics

| Metric     | Value (Approx.)       |
|------------|-----------------------|
| ✅ Accuracy | ~92–96% on 13-class emotion tasks |
| 🎯 F1 Score | Balanced for multi-class classification |
| ⚡ Latency  | <40ms on Raspberry Pi 4 |
| 📏 Recall   | Competitive for lightweight models |

*Note*: Metrics depend on hardware and fine-tuning. Test on your target device for precise results.

## Use Cases

NeuroFeel is tailored for **edge and IoT scenarios** requiring real-time emotion detection for short texts. Key applications include:

- **Chatbot Emotion Understanding**: Detect user emotions, e.g., “I love you” (predicts “Love ❤️”) to tailor responses.
- **Social Media Sentiment Tagging**: Analyze posts, e.g., “This is disgusting!” (predicts “Disgust 🤢”) for moderation or trend analysis.
- **Mental Health Context Detection**: Monitor mood, e.g., “I feel so alone” (predicts “Sadness 😢”) for wellness apps or crisis alerts.
- **Smart Replies and Reactions**: Suggest replies, e.g., “I’m so happy!” (predicts “Happiness 😄”) for positive emojis or animations.
- **Emotional Tone Analysis**: Adjust IoT settings, e.g., “I’m terrified!” (predicts “Fear 😱”) to dim lights or play calming music.
- **Voice Assistants**: Local emotion-aware parsing, e.g., “Why does it break?” (predicts “Anger 😠”) to prioritize fixes.
- **Toy Robotics**: Emotion-driven interactions, e.g., “I really want that!” (predicts “Desire 🔥”) for engaging animations.
- **Fitness Trackers**: Analyze feedback, e.g., “Wait, what?” (predicts “Confusion 😕”) to clarify instructions.
- **Wearable Devices**: Real-time mood tracking, e.g., “I’m stressed out” (predicts “Fear 😱”) to suggest breathing exercises.
- **Smart Home Automation**: Contextual responses, e.g., “I’m so tired” (predicts “Sadness 😢”) to adjust lighting or music.
- **Customer Support Bots**: Detect frustration, e.g., “This is ridiculous!” (predicts “Anger 😠”) to escalate to human agents.
- **Educational Tools**: Analyze student feedback, e.g., “I don’t get it” (predicts “Confusion 😕”) to offer tailored explanations.

## Hardware Requirements

- **Processors**: CPUs, mobile NPUs, or microcontrollers (e.g., ESP32-S3, Raspberry Pi 4, Snapdragon NPUs)
- **Storage**: ~25MB for model weights (quantized, Safetensors format)
- **Memory**: ~70MB RAM for inference
- **Environment**: Offline or low-connectivity settings

Quantization ensures efficient memory usage, making NeuroFeel ideal for resource-constrained devices.

## Training Details

NeuroFeel was fine-tuned on a **custom emotion dataset** augmented with **ChatGPT-generated data** to enhance diversity and robustness. Key training details:

- **Dataset**:
  - **Custom Emotion Dataset**: ~10,000 labeled short-text samples covering 13 emotions (e.g., Happiness, Sadness, Love). Sourced from social media posts, IoT user feedback, and chatbot interactions.
  - **ChatGPT-Augmented Data**: Synthetic samples generated to balance underrepresented emotions (e.g., Sarcasm, Shame) and improve generalization.
  - **Preprocessing**: Lowercasing, emoji removal, and tokenization with NeuroBERT’s tokenizer (max length: 64 tokens).
- **Training Process**:
  - **Base Model**: NeuroBERT, pre-trained on general English text for masked language modeling.
  - **Fine-Tuning**: Supervised training for 13-class emotion classification using cross-entropy loss.
  - **Hyperparameters**:
    - Epochs: 5
    - Batch Size: 16
    - Learning Rate: 2e-5
    - Optimizer: AdamW
    - Scheduler: Linear warmup (10% of steps)
  - **Hardware**: Fine-tuned on a single NVIDIA A100 GPU, but inference optimized for edge devices.
  - **Quantization**: Post-training INT8 quantization to reduce model size to ~25MB and improve inference speed.
- **Data Augmentation**:
  - Synonym replacement and back-translation to enhance robustness.
  - Synthetic negative sampling to improve detection of nuanced emotions like Guilt or Confusion.
- **Validation**:
  - Split: 80% train, 10% validation, 10% test.
  - Validation F1 score: ~0.93 across 13 classes.

Fine-tuning on domain-specific data is recommended to optimize performance for specific use cases (e.g., mental health apps or smart home devices).

## Fine-Tuning Guide

To adapt NeuroFeel for custom emotion detection tasks:

1. **Prepare Dataset**: Collect labeled data with 13 emotion categories.
2. **Fine-Tune with Hugging Face**:
   ```python
    import pandas as pd
    from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
    from sklearn.model_selection import train_test_split
    import torch
    from torch.utils.data import Dataset
    
    # === 1. Load and preprocess data ===
    dataset_path = '/content/dataset.csv'
    df = pd.read_csv(dataset_path)
    # Use the correct original column name 'Label' in dropna
    df = df.dropna(subset=['Label'])  # Ensure no missing labels
    df.columns = ['text', 'label']  # Normalize column names
    
    # === 2. Encode labels ===
    labels = sorted(df["label"].unique())
    label_to_id = {label: idx for idx, label in enumerate(labels)}
    id_to_label = {idx: label for label, idx in label_to_id.items()}
    df['label'] = df['label'].map(label_to_id)
    
    # === 3. Train/val split ===
    train_texts, val_texts, train_labels, val_labels = train_test_split(
        df['text'].tolist(), df['label'].tolist(), test_size=0.2, random_state=42
    )
    
    # === 4. Tokenizer ===
    tokenizer = BertTokenizer.from_pretrained("boltuix/NeuroBERT-Pro")
    
    # === 5. Dataset class ===
    class SentimentDataset(Dataset):
        def __init__(self, texts, labels, tokenizer, max_length=128):
            self.texts = texts
            self.labels = labels
            self.tokenizer = tokenizer
            self.max_length = max_length
    
        def __len__(self):
            return len(self.texts)
    
        def __getitem__(self, idx):
            encoding = self.tokenizer(
                self.texts[idx],
                padding='max_length',
                truncation=True,
                max_length=self.max_length,
                return_tensors='pt'
            )
            return {
                'input_ids': encoding['input_ids'].squeeze(0),
                'attention_mask': encoding['attention_mask'].squeeze(0),
                'labels': torch.tensor(self.labels[idx], dtype=torch.long)
            }
    
    # === 6. Load datasets ===
    train_dataset = SentimentDataset(train_texts, train_labels, tokenizer)
    val_dataset = SentimentDataset(val_texts, val_labels, tokenizer)
    
    # === 7. Load model ===
    model = BertForSequenceClassification.from_pretrained(
        "boltuix/NeuroBERT-Pro",
        num_labels=len(label_to_id)
    )
    
    # Optional: Ensure tensor layout is contiguous
    for param in model.parameters():
        param.data = param.data.contiguous()
    
    # === 8. Training arguments ===
    training_args = TrainingArguments(
        output_dir='./results',
        run_name="NeuroFeel",
        num_train_epochs=5,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=16,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        eval_strategy="epoch",
        report_to="none"
    )
    
    # === 9. Trainer setup ===
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset
    )
    
    # === 10. Train and evaluate ===
    trainer.train()
    trainer.evaluate()
    
    # === 11. Save model and label mappings ===
    model.config.label2id = label_to_id
    model.config.id2label = id_to_label
    model.config.num_labels = len(label_to_id)
    
    model.save_pretrained("./neuro-feel")
    tokenizer.save_pretrained("./neuro-feel")
    
    print("✅ Training complete. Model and tokenizer saved to ./neuro-feel")
   ```
3. **Deploy**: Export to ONNX or TensorFlow Lite for edge devices.

## Comparison to Other Models

| Model           | Parameters | Size   | Edge/IoT Focus | Tasks Supported                     |
|-----------------|------------|--------|----------------|-------------------------------------|
| NeuroFeel       | ~7M        | ~25MB  | High           | Emotion Detection, Classification   |
| NeuroBERT       | ~7M        | ~30MB  | High           | MLM, NER, Classification            |
| BERT-Lite       | ~2M        | ~10MB  | High           | MLM, NER, Classification            |
| DistilBERT      | ~66M       | ~200MB | Moderate       | MLM, NER, Classification, Sentiment |

NeuroFeel is specialized for 13-class emotion detection, offering superior performance for short-text sentiment analysis on edge devices compared to general-purpose models like NeuroBERT, while being far more efficient than DistilBERT.

## Tags

`#NeuroFeel` `#edge-nlp` `#emotion-detection` `#on-device-ai` `#offline-nlp`  
`#mobile-ai` `#sentiment-analysis` `#text-classification` `#emojis` `#emotions`  
`#lightweight-transformers` `#embedded-nlp` `#smart-device-ai` `#low-latency-models`  
`#ai-for-iot` `#efficient-neurobert` `#nlp2025` `#context-aware` `#edge-ml`  
`#smart-home-ai` `#emotion-aware` `#voice-ai` `#eco-ai` `#chatbot` `#social-media`  
`#mental-health` `#short-text` `#smart-replies` `#tone-analysis` `#wearable-ai`

## License

**Apache-2.0 License**: Free to use, modify, and distribute for personal and commercial purposes. See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) for details.

## Credits

- **Base Model**: [neurobert](https://huggingface.co/neurobert)
- **Optimized By**: Boltuix, fine-tuned and quantized for edge AI applications
- **Library**: Hugging Face `transformers` team for model hosting and tools

## Support & Community

For issues, questions, or contributions:
- Visit the [Hugging Face model page](https://huggingface.co/boltuix/NeuroFeel)
- Open an issue on the [repository](https://huggingface.co/boltuix/NeuroFeel)
- Join discussions on Hugging Face or contribute via pull requests
- Check the [Transformers documentation](https://huggingface.co/docs/transformers) for guidance

We welcome community feedback to enhance NeuroFeel for IoT and edge applications!

## Contact

- 📬 Email: [boltuix@gmail.com](mailto:boltuix@gmail.com)
- 