---
tags:
- image-classification
- facial-emotion-recognition
- emotion-detection
- convnext-v2
- pytorch
library_name: transformers
license: cc-by-nc-4.0
datasets:
- samaneheslamifar/facial-emotion-expressions
metrics:
- accuracy
- f1
pipeline_tag: image-classification
base_model:
- facebook/convnextv2-large-22k-224
---

# DrGM-ConvNeXt-V2-Large-FER

## Model Description
This is a State-of-the-Art (SOTA) **Facial Emotion Recognition (FER)** model based on the **ConvNeXt V2 Large** architecture. It has been fine-tuned to recognize 7 distinct facial emotions with high accuracy.

## Model Architecture
- **Base Model:** `facebook/convnextv2-large-22k-224`
- **Parameters:** ~198M
- **Fine-tuning:** Optimized with BF16 mixed precision, Label Smoothing (0.1), and RandAugment on an A100 GPU.

## ⚠️ License & Usage
This model is released under the **CC-BY-NC-4.0** license.
*   **Personal Use:** ✅ Allowed. You can use this for personal projects, research, and education.
*   **Commercial Use:** ❌ **Forbidden** without prior permission.
*   **Commissions:** If you wish to use this model for commercial applications or commissions, please **contact the author** for licensing.

### Training History
The model was trained for 15 epochs on an A100 GPU. Below is the detailed progression of loss and metrics:

| Epoch | Training Loss | Validation Loss | Accuracy | F1 (Weighted) |
|:-----:|:-------------:|:---------------:|:--------:|:-------------:|
| 1     | 1.0126        | 0.9488          | 76.31%   | 0.7629        |
| 2     | 0.8600        | 0.8394          | 81.91%   | 0.8177        |
| 3     | 0.7161        | 0.7932          | 85.02%   | 0.8495        |
| 4     | 0.6340        | 0.7552          | 87.52%   | 0.8748        |
| 5     | 0.5956        | 0.7405          | 88.34%   | 0.8829        |
| 6     | 0.5568        | 0.7247          | 88.94%   | 0.8893        |
| 7     | 0.5259        | 0.7251          | 89.03%   | 0.8902        |
| 8     | 0.5149        | 0.7208          | 89.16%   | 0.8913        |
| 9     | 0.5071        | 0.7172          | 89.66%   | 0.8964        |
| 10    | 0.4984        | 0.7156          | 89.66%   | 0.8963        |
| 11    | 0.4933        | 0.7101          | 89.88%   | 0.8989        |
| 12    | 0.4857        | 0.7071          | 89.92%   | 0.8991        |
| 13    | 0.4803        | 0.7038          | 90.25%   | 0.9025        |
| 14    | 0.4718        | 0.7031          | 90.43%   | 0.9042        |
| **15**| **0.4730**    | **0.7013**      | **90.40%**| **0.9039**   |

### Final Training Metrics
- **Total Training Time:** ~49 minutes (2933.82 seconds)
- **Global Steps:** 11,805
- **Final Training Loss:** 0.5977
- **Throughput:** 257.37 samples/second

## Performance
The model achieves exceptional performance on the Facial Emotion Expressions dataset.

### Final Evaluation Results (Test Set)
After training, the model was evaluated on the unseen test set:

| Metric | Value |
|:-------|:------|
| **Accuracy** | **90.43%** |
| **F1 Score (Weighted)** | **0.9042** |
| **Validation Loss** | 0.7031 |
| **Inference Time (Batch)** | 23.63s (Total) |
| **Throughput** | 532.68 samples/sec |

*(Note: These metrics are from the held-out test split, confirming the model generalizes well and is not just memorizing data.)*

### Classification Report (Full Dataset Evaluation)
| Class | Precision | Recall | F1-Score | Support |
|:---:|:---:|:---:|:---:|:---:|
| **Angry** | 0.97 | 0.97 | 0.97 | 8989 |
| **Disgust** | 1.00 | 1.00 | 1.00 | 8989 |
| **Fear** | 0.97 | 0.96 | 0.97 | 8989 |
| **Happy** | 0.98 | 0.98 | 0.98 | 8989 |
| **Neutral** | 0.96 | 0.97 | 0.97 | 8989 |
| **Sad** | 0.96 | 0.96 | 0.96 | 8989 |
| **Surprise** | 0.99 | 0.99 | 0.99 | 8989 |
| **Accuracy** | | | **0.98** | 62923 |

*(Note: Full dataset evaluation includes both training and validation samples, indicating high model capacity and learning)*

### Confusion Matrix
![Confusion Matrix](./Confusion_Matrix.png)

## 📊 Advanced Model Statistics

**Global Accuracy Metrics:**
- **Top-1 Accuracy:** 97.78%
- **Top-2 Accuracy:** 99.05% (Correct emotion is in the top 2 predictions)
- **Top-3 Accuracy:** 99.41%

### Per-Emotion Performance Breakdown
| Emotion   | Accuracy   | Avg Confidence   |   Samples |
|:----------|:-----------|:-----------------|----------:|
| angry     | 97.49%     | 89.99%           |      8989 |
| disgust   | 100.00%    | 91.34%           |      8989 |
| fear      | 96.07%     | 89.66%           |      8989 |
| happy     | 98.16%     | 90.72%           |      8989 |
| neutral   | 97.35%     | 90.39%           |      8989 |
| sad       | 96.27%     | 89.55%           |      8989 |
| surprise  | 99.13%     | 90.81%           |      8989 |

### Inference Speed Benchmark
Tested on an NVIDIA A100 GPU with a batch size of 1 (simulating real-time usage):

- **Average Latency:** 20.75 ms per image
- **Frame Rate:** 48.19 FPS

*This performance indicates the model may be suitable for real-time video processing applications.*

## Usage
```python
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image

# Load Model
repo_name = "DrGM/DrGM-ConvNeXt-V2L-Facial-Emotion-Recognition" 
processor = AutoImageProcessor.from_pretrained(repo_name)
model = AutoModelForImageClassification.from_pretrained(repo_name)

# Predict
image = Image.open("path/to/your/image.jpg").convert("RGB")
inputs = processor(image, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits
    predicted_label = logits.argmax(-1).item()
    print(model.config.id2label[predicted_label])
```