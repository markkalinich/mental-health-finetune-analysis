---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
  - emotion-classification
  - text-classification
  - distilbert
metrics:
  - accuracy
---

# emotion-classification-model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased).
It achieves the following results on the evaluation set:
- **Loss:** 0.1789
- **Accuracy:** 0.931

## Model Description

The **Emotion Classification Model** is a fine-tuned version of the `distilbert-base-uncased` transformer architecture, adapted specifically for classifying text into six distinct emotions. DistilBERT, a distilled version of BERT, offers a lightweight yet powerful foundation, enabling efficient training and inference without significant loss in performance.

This model leverages the pre-trained language understanding capabilities of DistilBERT to accurately categorize textual data into the following emotion classes:

- **Sadness**
- **Joy**
- **Love**
- **Anger**
- **Fear**
- **Surprise**

By fine-tuning on the `dair-ai/emotion` dataset, the model has been optimized to recognize and differentiate subtle emotional cues in various text inputs, making it suitable for applications that require nuanced sentiment analysis and emotional intelligence.

## Intended Uses & Limitations

### Intended Uses

The Emotion Classification Model is designed for a variety of applications where understanding the emotional tone of text is crucial. Suitable use cases include:

- **Sentiment Analysis:** Gauging customer feedback, reviews, and social media posts to understand emotional responses.
- **Social Media Analysis:** Tracking and analyzing emotional trends and public sentiment across platforms like Twitter, Facebook, and Instagram.
- **Content Recommendation:** Enhancing recommendation systems by aligning content suggestions with users' current emotional states.
- **Chatbots and Virtual Assistants:** Enabling more empathetic and emotionally aware interactions with users.

### Limitations

While the Emotion Classification Model demonstrates strong performance across various tasks, it has certain limitations:

- **Bias in Training Data:** The model may inherit biases present in the `dair-ai/emotion` dataset, potentially affecting its performance across different demographics, cultures, or contexts.
- **Contextual Understanding:** The model analyzes text in isolation and may struggle with understanding nuanced emotions that depend on broader conversational context or preceding interactions.
- **Language Constraints:** Currently optimized for English, limiting its effectiveness with multilingual or non-English inputs without further training or adaptation.
- **Emotion Overlap:** Some emotions have overlapping linguistic cues, which may lead to misclassifications in ambiguous text scenarios.
- **Dependence on Text Quality:** The model's performance can degrade with poorly structured, slang-heavy, or highly informal text inputs.

## Training and Evaluation Data

### Dataset

The model was trained and evaluated on the [`dair-ai/emotion`](https://huggingface.co/datasets/dair-ai/emotion) dataset, a comprehensive collection of textual data annotated for emotion classification.

### Dataset Statistics

- **Total Samples:** 20,000
  - **Training Set:** 16,000 samples
  - **Validation Set:** 2,000 samples
  - **Test Set:** 2,000 samples

### Data Preprocessing

Prior to training, the dataset underwent the following preprocessing steps:

1. **Tokenization:** Utilized the `DistilBertTokenizerFast` from the `distilbert-base-uncased` model to tokenize the input text. Each text sample was converted into token IDs, ensuring compatibility with the DistilBERT architecture.
2. **Padding & Truncation:** Applied padding and truncation to maintain a uniform sequence length of 32 tokens. This step ensures efficient batching and consistent input dimensions for the model.
3. **Batch Processing:** Employed parallel processing using all available CPU cores minus one to expedite the tokenization process across training, validation, and test sets.
4. **Format Conversion:** Converted the tokenized datasets into PyTorch tensors to facilitate seamless integration with the PyTorch-based `Trainer` API.

### Evaluation Metrics

The model's performance was assessed using the following metrics:

- **Accuracy:** Measures the proportion of correctly predicted samples out of the total samples.

## Training Procedure

### Training Hyperparameters

The following hyperparameters were used during training:

- **Learning Rate:** `6e-05`
- **Training Batch Size:** `16` per device
- **Evaluation Batch Size:** `32` per device
- **Number of Epochs:** `2`
- **Weight Decay:** `0.01`
- **Gradient Accumulation Steps:** `2` (effectively simulating a batch size of `32`)
- **Mixed Precision Training:** Enabled (Native AMP) if CUDA is available

### Optimization Strategies

- **Mixed Precision Training:** Utilized PyTorch's Native AMP to accelerate training and reduce memory consumption when a CUDA-enabled GPU is available.
- **Gradient Accumulation:** Implemented gradient accumulation with `2` steps to effectively increase the batch size without exceeding GPU memory limits.
- **Checkpointing:** Configured to save model checkpoints at the end of each epoch, retaining only the two most recent checkpoints to manage storage efficiently.

### Training Duration

- **Total Training Time:** Approximately `2.40` minutes
### Logging and Monitoring

- **Logging Directory:** `./logs`
- **Logging Steps:** Every `10` steps
- **Reporting To:** TensorBoard
- **Tools Used:** TensorBoard for real-time visualization of training metrics, including loss and accuracy.

### Training Results

After training, the model achieved the following performance metrics:

- **Validation Accuracy:** `93.10%`
- **Test Accuracy:** `93.10%`
