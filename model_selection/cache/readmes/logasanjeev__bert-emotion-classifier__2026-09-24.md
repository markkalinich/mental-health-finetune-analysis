---
language: en
license: mit
pipeline_tag: text-classification
tags:
- text-classification
- transformers
- pytorch
- onnx
- multi-label-classification
- multi-class-classification
- emotion
- bert
- go_emotions
- emotion-classification
- sentiment-analysis
- tensorflow
datasets:
- google-research-datasets/go_emotions
metrics:
- f1
- precision
- recall
- accuracy
widget:
- text: I’m just chilling today.
  example_title: Neutral Example
- text: Thank you for saving my life!
  example_title: Gratitude Example
- text: I’m nervous about my exam tomorrow.
  example_title: Nervousness Example
- text: I love my new puppy so much!
  example_title: Love Example
- text: I’m so relieved the storm passed.
  example_title: Relief Example
base_model:
- google-bert/bert-base-uncased
base_model_relation: finetune
model-index:
- name: Bert Emotion Classifier
  results:
  - task:
      type: multi-label-classification
    dataset:
      name: GoEmotions
      type: google-research-datasets/go_emotions
    metrics:
    - name: Micro F1 (Optimized Thresholds)
      type: micro-f1
      value: 0.6006
    - name: Macro F1
      type: macro-f1
      value: 0.539
    - name: Precision
      type: precision
      value: 0.5371
    - name: Recall
      type: recall
      value: 0.6812
    - name: Hamming Loss
      type: hamming-loss
      value: 0.0377
    - name: Avg Positive Predictions
      type: avg-positive-predictions
      value: 1.4789
  - task:
      type: multi-label-classification
    dataset:
      name: GoEmotions
      type: google-research-datasets/go_emotions
    metrics:
    - name: F1 (admiration)
      type: f1
      value: 0.6987
    - name: F1 (amusement)
      type: f1
      value: 0.8071
    - name: F1 (anger)
      type: f1
      value: 0.503
    - name: F1 (annoyance)
      type: f1
      value: 0.3892
    - name: F1 (approval)
      type: f1
      value: 0.3915
    - name: F1 (caring)
      type: f1
      value: 0.4473
    - name: F1 (confusion)
      type: f1
      value: 0.4714
    - name: F1 (curiosity)
      type: f1
      value: 0.5781
    - name: F1 (desire)
      type: f1
      value: 0.5229
    - name: F1 (disappointment)
      type: f1
      value: 0.3333
    - name: F1 (disapproval)
      type: f1
      value: 0.4323
    - name: F1 (disgust)
      type: f1
      value: 0.4926
    - name: F1 (embarrassment)
      type: f1
      value: 0.4912
    - name: F1 (excitement)
      type: f1
      value: 0.4571
    - name: F1 (fear)
      type: f1
      value: 0.586
    - name: F1 (gratitude)
      type: f1
      value: 0.9102
    - name: F1 (grief)
      type: f1
      value: 0.3333
    - name: F1 (joy)
      type: f1
      value: 0.6135
    - name: F1 (love)
      type: f1
      value: 0.8065
    - name: F1 (nervousness)
      type: f1
      value: 0.4348
    - name: F1 (optimism)
      type: f1
      value: 0.5564
    - name: F1 (pride)
      type: f1
      value: 0.5217
    - name: F1 (realization)
      type: f1
      value: 0.2513
    - name: F1 (relief)
      type: f1
      value: 0.5833
    - name: F1 (remorse)
      type: f1
      value: 0.68
    - name: F1 (sadness)
      type: f1
      value: 0.557
    - name: F1 (surprise)
      type: f1
      value: 0.5562
    - name: F1 (neutral)
      type: f1
      value: 0.6867
    source:
      name: Kaggle Evaluation Notebook
      url: >-
        https://www.kaggle.com/code/ravindranlogasanjeev/evaluation-logasanjeev-bert-emotion-classifier/notebook
library_name: transformers
---

# Bert Emotion Classifier

Fine-tuned [BERT-base-uncased](https://huggingface.co/bert-base-uncased) on [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) for multi-label classification (28 emotions). This updated version includes improved Macro F1, ONNX support for efficient inference, and visualizations for better interpretability.

## Model Details

- **Architecture**: BERT-base-uncased (110M parameters)
- **Training Data**: [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) (58k Reddit comments, 28 emotions)
- **Loss Function**: Focal Loss (alpha=1, gamma=2)
- **Optimizer**: AdamW (lr=2e-5, weight_decay=0.01)
- **Epochs**: 5
- **Batch Size**: 16
- **Max Length**: 128
- **Hardware**: Kaggle P100 GPU (16GB)

## Try It Out

For accurate predictions with optimized thresholds, use the [Gradio demo](https://logasanjeev-bert-emotion-classifier-demo.hf.space). The demo now includes preprocessed text and the top 5 predicted emotions, in addition to thresholded predictions. Example predictions:

- **Input**: "I’m thrilled to win this award! 😄"
  - **Output**: `excitement: 0.5836, joy: 0.5290`
- **Input**: "This is so frustrating, nothing works. 😣"
  - **Output**: `annoyance: 0.6147, anger: 0.4669`
- **Input**: "I feel so sorry for what happened. 😢"
  - **Output**: `sadness: 0.5321, remorse: 0.9107`

## Performance

- **Micro F1**: 0.6006 (optimized thresholds)
- **Macro F1**: 0.5390
- **Precision**: 0.5371
- **Recall**: 0.6812
- **Hamming Loss**: 0.0377
- **Avg Positive Predictions**: 1.4789

For a detailed evaluation, including class-wise accuracy, precision, recall, F1, MCC, support, and thresholds, along with visualizations, check out the [Kaggle notebook](https://www.kaggle.com/code/ravindranlogasanjeev/evaluation-logasanjeev-bert-emotion-classifier/notebook).

### Class-Wise Performance

The following table shows per-class metrics on the test set using optimized thresholds (see `optimized_thresholds.json`):

| Emotion        | Accuracy | Precision | Recall | F1 Score | MCC    | Support | Threshold |
|---------------|----------|-----------|--------|----------|--------|---------|-----------|
| admiration    | 0.9410   | 0.6649    | 0.7361 | 0.6987   | 0.6672 | 504     | 0.4500    |
| amusement     | 0.9801   | 0.7635    | 0.8561 | 0.8071   | 0.7981 | 264     | 0.4500    |
| anger         | 0.9694   | 0.6176    | 0.4242 | 0.5030   | 0.4970 | 198     | 0.4500    |
| annoyance     | 0.9121   | 0.3297    | 0.4750 | 0.3892   | 0.3502 | 320     | 0.3500    |
| approval      | 0.8843   | 0.2966    | 0.5755 | 0.3915   | 0.3572 | 351     | 0.3500    |
| caring        | 0.9759   | 0.5196    | 0.3926 | 0.4473   | 0.4396 | 135     | 0.4500    |
| confusion     | 0.9711   | 0.4861    | 0.4575 | 0.4714   | 0.4567 | 153     | 0.4500    |
| curiosity     | 0.9368   | 0.4442    | 0.8275 | 0.5781   | 0.5783 | 284     | 0.4000    |
| desire        | 0.9865   | 0.5714    | 0.4819 | 0.5229   | 0.5180 | 83      | 0.4000    |
| disappointment| 0.9565   | 0.2906    | 0.3907 | 0.3333   | 0.3150 | 151     | 0.3500    |
| disapproval   | 0.9235   | 0.3405    | 0.5918 | 0.4323   | 0.4118 | 267     | 0.3500    |
| disgust       | 0.9810   | 0.6250    | 0.4065 | 0.4926   | 0.4950 | 123     | 0.5500    |
| embarrassment | 0.9947   | 0.7000    | 0.3784 | 0.4912   | 0.5123 | 37      | 0.5000    |
| excitement    | 0.9790   | 0.4486    | 0.4660 | 0.4571   | 0.4465 | 103     | 0.4000    |
| fear          | 0.9836   | 0.4599    | 0.8077 | 0.5860   | 0.6023 | 78      | 0.3000    |
| gratitude     | 0.9888   | 0.9450    | 0.8778 | 0.9102   | 0.9049 | 352     | 0.5500    |
| grief         | 0.9985   | 0.3333    | 0.3333 | 0.3333   | 0.3326 | 6       | 0.3000    |
| joy           | 0.9768   | 0.6061    | 0.6211 | 0.6135   | 0.6016 | 161     | 0.4500    |
| love          | 0.9825   | 0.7826    | 0.8319 | 0.8065   | 0.7978 | 238     | 0.5000    |
| nervousness   | 0.9952   | 0.4348    | 0.4348 | 0.4348   | 0.4324 | 23      | 0.4000    |
| optimism      | 0.9689   | 0.5436    | 0.5699 | 0.5564   | 0.5405 | 186     | 0.4000    |
| pride         | 0.9980   | 0.8571    | 0.3750 | 0.5217   | 0.5662 | 16      | 0.4000    |
| realization   | 0.9737   | 0.5217    | 0.1655 | 0.2513   | 0.2838 | 145     | 0.4500    |
| relief        | 0.9982   | 0.5385    | 0.6364 | 0.5833   | 0.5845 | 11      | 0.3000    |
| remorse       | 0.9912   | 0.5426    | 0.9107 | 0.6800   | 0.6992 | 56      | 0.3500    |
| sadness       | 0.9757   | 0.5845    | 0.5321 | 0.5570   | 0.5452 | 156     | 0.4500    |
| surprise      | 0.9724   | 0.4772    | 0.6667 | 0.5562   | 0.5504 | 141     | 0.3500    |
| neutral       | 0.7485   | 0.5821    | 0.8372 | 0.6867   | 0.5102 | 1787    | 0.4000    |

### Visualizations

#### Class-Wise F1 Scores
![Class-Wise F1 Scores](class_wise_f1_plot.png)

#### Training Curves
![Training and Validation Loss and Micro F1](training_curves_plot.png)

## Training Insights

The model was trained for 5 epochs with Focal Loss to handle class imbalance. Training and validation curves show consistent improvement:
- Training Loss decreased from 0.0429 to 0.0134.
- Validation Micro F1 peaked at 0.5874 (epoch 5).
- See the training curves plot above for details.

## Usage

### Quick Inference with inference.py (Recommended for PyTorch)

The easiest way to use the model with PyTorch is to programmatically fetch and use `inference.py` from the repository. The script handles all preprocessing, model loading, and inference for you.

#### Programmatic Download and Inference
Run the following Python script to download `inference.py` and make predictions:

```python
# pip install transformers torch huggingface_hub emoji -q

from huggingface_hub import hf_hub_download
import importlib.util

# download inference script
path = hf_hub_download(repo_id="logasanjeev/bert-emotion-classifier", filename="inference.py")

# load module
spec = importlib.util.spec_from_file_location("inference", path)
inference = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inference)

# run prediction
text = "I’m thrilled to win this award! 😄"
result, processed = inference.predict_emotions(text)

print("Input:", text)
print("Processed:", processed)
print("Predicted Emotions:", result)
```

#### Expected Output:
```
Input: I’m thrilled to win this award! 😄
Processed: i’m thrilled to win this award ! grinning_face_with_smiling_eyes
Predicted Emotions:
excitement: 0.5836
joy: 0.5290
```

#### Alternative: Manual Download
If you prefer to download `inference.py` manually:
1. Install the required dependencies:
   ```bash
   pip install transformers torch huggingface_hub emoji
   ```
2. Download `inference.py` from the repository.
3. Use it in Python or via the command line.

**Python Example:**
```python
from inference import predict_emotions

result, processed = predict_emotions("I’m thrilled to win this award! 😄")
print(f"Input: I’m thrilled to win this award! 😄")
print(f"Processed: {processed}")
print("Predicted Emotions:")
print(result)
```

**Command-Line Example:**
```bash
python inference.py "I’m thrilled to win this award! 😄"
```

### Quick Inference with onnx_inference.py (Recommended for ONNX)

For faster and more efficient inference using ONNX, you can use `onnx_inference.py`. This script leverages ONNX Runtime for inference, which is typically more lightweight than PyTorch.

#### Programmatic Download and Inference
Run the following Python script to download `onnx_inference.py` and make predictions:

```python
# pip install transformers torch huggingface_hub emoji -q

from huggingface_hub import hf_hub_download
import importlib.util

# download inference script
path = hf_hub_download(repo_id="logasanjeev/bert-emotion-classifier", filename="inference.py")

# load module
spec = importlib.util.spec_from_file_location("inference", path)
inference = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inference)

# run prediction
text = "I’m thrilled to win this award! 😄"
result, processed = inference.predict_emotions(text)

print("Input:", text)
print("Processed:", processed)
print("Predicted Emotions:", result)
```

#### Expected Output:
```
Input: I’m thrilled to win this award! 😄
Processed: i’m thrilled to win this award ! grinning_face_with_smiling_eyes
Predicted Emotions:
excitement: 0.5836
joy: 0.5290
```

#### Alternative: Manual Download
If you prefer to download `onnx_inference.py` manually:
1. Install the required dependencies:
   ```bash
   pip install transformers onnxruntime huggingface_hub emoji numpy
   ```
2. Download `onnx_inference.py` from the repository.
3. Use it in Python or via the command line.

**Python Example:**
```python
from onnx_inference import predict_emotions

result, processed = predict_emotions("I’m thrilled to win this award! 😄")
print(f"Input: I’m thrilled to win this award! 😄")
print(f"Processed: {processed}")
print("Predicted Emotions:")
print(result)
```

**Command-Line Example:**
```bash
python onnx_inference.py "I’m thrilled to win this award! 😄"
```

### Preprocessing
Before inference, preprocess text to match training conditions:
- Replace user mentions (`u/username`) with `[USER]`.
- Replace subreddits (`r/subreddit`) with `[SUBREDDIT]`.
- Replace URLs with `[URL]`.
- Convert emojis to text using `emoji.demojize` (e.g., 😊 → `smiling_face_with_smiling_eyes`).
- Lowercase the text.

### PyTorch Inference
```python
from transformers import BertForSequenceClassification, BertTokenizer
import torch
import json
import requests
import re
import emoji

def preprocess_text(text):
    text = re.sub(r'u/\w+', '[USER]', text)
    text = re.sub(r'r/\w+', '[SUBREDDIT]', text)
    text = re.sub(r'http[s]?://\S+', '[URL]', text)
    text = emoji.demojize(text, delimiters=(" ", " "))
    text = text.lower()
    return text

repo_id = "logasanjeev/bert-emotion-classifier"
model = BertForSequenceClassification.from_pretrained(repo_id)
tokenizer = BertTokenizer.from_pretrained(repo_id)

thresholds_url = f"https://huggingface.co/{repo_id}/raw/main/optimized_thresholds.json"
thresholds_data = json.loads(requests.get(thresholds_url).text)
emotion_labels = thresholds_data["emotion_labels"]
thresholds = thresholds_data["thresholds"]

text = "I’m just chilling today."
processed_text = preprocess_text(text)
encodings = tokenizer(processed_text, padding='max_length', truncation=True, max_length=128, return_tensors='pt')
with torch.no_grad():
    logits = torch.sigmoid(model(**encodings).logits).numpy()[0]
predictions = [(emotion_labels[i], round(logit, 4)) for i, (logit, thresh) in enumerate(zip(logits, thresholds)) if logit >= thresh]
predictions = sorted(predictions, key=lambda x: x[1], reverse=True)
print(predictions)
# Output: [('neutral', 0.8147)]
```

### ONNX Inference
For a simplified ONNX inference experience, use `onnx_inference.py` as shown above. Alternatively, you can use the manual approach below:

```python
import onnxruntime as ort
import numpy as np

onnx_url = f"https://huggingface.co/{repo_id}/raw/main/model.onnx"
with open("model.onnx", "wb") as f:
    f.write(requests.get(onnx_url).content)

text = "I’m thrilled to win this award! 😄"
processed_text = preprocess_text(text)
encodings = tokenizer(processed_text, padding='max_length', truncation=True, max_length=128, return_tensors='np')
session = ort.InferenceSession("model.onnx")
inputs = {
    'input_ids': encodings['input_ids'].astype(np.int64),
    'attention_mask': encodings['attention_mask'].astype(np.int64)
}
logits = session.run(None, inputs)[0][0]
logits = 1 / (1 + np.exp(-logits))  # Sigmoid
predictions = [(emotion_labels[i], round(logit, 4)) for i, (logit, thresh) in enumerate(zip(logits, thresholds)) if logit >= thresh]
predictions = sorted(predictions, key=lambda x: x[1], reverse=True)
print(predictions)
# Output: [('excitement', 0.5836), ('joy', 0.5290)]
```

## License

This model is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Usage Notes

- The model performs best on Reddit-style comments with similar preprocessing.
- Rare emotions (e.g., `grief`, support=6) have lower F1 scores due to limited data.
- ONNX inference requires `onnxruntime` and compatible hardware (opset 14).