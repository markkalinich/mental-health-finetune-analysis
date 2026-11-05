---
library_name: transformers
license: mit
datasets:
- google-research-datasets/go_emotions
base_model: answerdotai/ModernBERT-large
language:
- en
tags:
- Text Classification
- emotion-classification
- emotion-recognition
- emotion-detection
- emotion
- multilabel
metrics:
- f1
- precision
- recall
---

# Summary
This is [ModernBERT-large](https://huggingface.co/answerdotai/ModernBERT-large) model finetuned on [go_emotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) 
dataset for multilabel classification. Model can be used to extract all emotions from english text or detect certain emotions. 
Thresholds are selected on validation set by maximizing f1 macro over all labels.
You can use Flash Attention 2 to speed up inference.

Also ONNX version of model and INT8 quantized model is available. information about them is posted in the last sections. 

The quality of the model varies greatly across all classes (look at the table with metrics below). There are classes like 
admiration, amusement, optimism, fear, remorse and others where the model shows high recognition quality, and classes that pose difficulties for the model - disappointment, realization 
that do have much fewer examples in the training data.

# Usage
Using model is easy with Huggingface Transformers. 

ModernBERT architecture is supported in the transformers version 4.48.0 and later, so you need to install it:
```bash
pip install "transformers>=4.48.0"
```

Here is how you can extract emotions contained in text: 

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained('fyaronskiy/ModernBERT-large-go-emotions')
model = AutoModelForSequenceClassification.from_pretrained('fyaronskiy/ModernBERT-large-go-emotions')
best_thresholds = [0.5510204081632653, 0.26530612244897955, 0.14285714285714285, 0.12244897959183673, 0.44897959183673464, 0.22448979591836732, 0.2040816326530612, 0.4081632653061224, 0.5306122448979591, 0.22448979591836732, 0.2857142857142857, 0.3061224489795918, 0.2040816326530612, 0.14285714285714285, 0.1020408163265306, 0.4693877551020408, 0.24489795918367346, 0.3061224489795918, 0.2040816326530612, 0.36734693877551017, 0.2857142857142857, 0.04081632653061224, 0.3061224489795918, 0.16326530612244897, 0.26530612244897955, 0.32653061224489793, 0.12244897959183673, 0.2040816326530612]
LABELS = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
ID2LABEL = dict(enumerate(LABELS))
```


```python
def detect_emotions(text):
  inputs = tokenizer(text, truncation=True, add_special_tokens=True, max_length=128, return_tensors='pt')
  with torch.no_grad():
      logits = model(**inputs).logits
  probas = torch.sigmoid(logits).squeeze(dim=0)  
  class_binary_labels = (probas > torch.tensor(best_thresholds)).int()
  return [ID2LABEL[label_id] for label_id, value in enumerate(class_binary_labels) if value == 1]
print(detect_emotions('You have excellent service and the best coffee in the city, I love your coffee shop!'))
#['admiration', 'love']
```

This is the way to get all emotions and their scores:

```python
def predict(text):
    inputs = tokenizer(text, truncation=True, add_special_tokens=True, max_length=128, return_tensors='pt')
    with torch.no_grad():
        logits = model(**inputs).logits
    probas = torch.sigmoid(logits).squeeze(dim=0).tolist()
    probas = [round(proba, 3) for proba in probas]    
    
    labels2probas = dict(zip(LABELS, probas))
    probas_dict_sorted = dict(sorted(labels2probas.items(), key=lambda x: x[1], reverse=True))
    return probas_dict_sorted
print(predict('You have excellent service and the best coffee in the city, I love your coffee shop!'))
#{'admiration': 0.982, 'love': 0.689, 'approval': 0.014, 'gratitude': 0.003, 'joy': 0.003, 'amusement': 0.001, 'curiosity': 0.001, 'excitement': 0.001, 'realization': 0.001, 'surprise': 0.001, 'anger': 0.0, 'annoyance': 0.0, 'caring': 0.0, 'confusion': 0.0, 'desire': 0.0, 'disappointment': 0.0, 'disapproval': 0.0, 'disgust': 0.0, 'embarrassment': 0.0, 'fear': 0.0, 'grief': 0.0, 'nervousness': 0.0, 'optimism': 0.0, 'pride': 0.0, 'relief': 0.0, 'remorse': 0.0, 'sadness': 0.0, 'neutral': 0.0}
```

# Eval results on test split of go-emotions


|                |   precision |   recall |   f1-score |   support |   threshold |
|:---------------|------------:|---------:|-----------:|----------:|------------:|
| admiration     |        0.68 |     0.72 |       0.7  |       504 |        0.55 |
| amusement      |        0.76 |     0.91 |       0.83 |       264 |        0.27 |
| anger          |        0.44 |     0.53 |       0.48 |       198 |        0.14 |
| annoyance      |        0.27 |     0.46 |       0.34 |       320 |        0.12 |
| approval       |        0.41 |     0.38 |       0.4  |       351 |        0.45 |
| caring         |        0.37 |     0.46 |       0.41 |       135 |        0.22 |
| confusion      |        0.36 |     0.51 |       0.42 |       153 |        0.2  |
| curiosity      |        0.45 |     0.77 |       0.57 |       284 |        0.41 |
| desire         |        0.66 |     0.46 |       0.54 |        83 |        0.53 |
| disappointment |        0.41 |     0.26 |       0.32 |       151 |        0.22 |
| disapproval    |        0.39 |     0.54 |       0.45 |       267 |        0.29 |
| disgust        |        0.52 |     0.41 |       0.46 |       123 |        0.31 |
| embarrassment  |        0.52 |     0.41 |       0.45 |        37 |        0.2  |
| excitement     |        0.29 |     0.59 |       0.39 |       103 |        0.14 |
| fear           |        0.55 |     0.78 |       0.65 |        78 |        0.1  |
| gratitude      |        0.96 |     0.88 |       0.92 |       352 |        0.47 |
| grief          |        0.29 |     0.67 |       0.4  |         6 |        0.24 |
| joy            |        0.57 |     0.66 |       0.61 |       161 |        0.31 |
| love           |        0.74 |     0.87 |       0.8  |       238 |        0.2  |
| nervousness    |        0.37 |     0.43 |       0.4  |        23 |        0.37 |
| optimism       |        0.6  |     0.58 |       0.59 |       186 |        0.29 |
| pride          |        0.28 |     0.44 |       0.34 |        16 |        0.04 |
| realization    |        0.36 |     0.19 |       0.24 |       145 |        0.31 |
| relief         |        0.62 |     0.45 |       0.53 |        11 |        0.16 |
| remorse        |        0.51 |     0.84 |       0.63 |        56 |        0.27 |
| sadness        |        0.54 |     0.56 |       0.55 |       156 |        0.33 |
| surprise       |        0.47 |     0.63 |       0.54 |       141 |        0.12 |
| neutral        |        0.58 |     0.82 |       0.68 |      1787 |        0.2  |
| micro avg      |        0.54 |     0.67 |       0.6  |      6329 |             |
| macro avg      |        0.5  |     0.58 |       0.52 |      6329 |             |
| weighted avg   |        0.55 |     0.67 |       0.6  |      6329 |             |
| samples avg    |        0.59 |     0.69 |       0.61 |      6329 |             |

# ONNX and quantized versions of model


Full precision ONNX model (onnx/model.onnx) - 1.6x faster than Transformer model, quality is the same.

INT8 quantized model (onnx/model_quantized.onnx) - 2.5x faster than Transformer model, quality is almost the same.

In table below results of tests of inference of 5427 samples of test_set.
I tested inference with batch_size 1 on Intel Xeon CPU with 2 vCPUs (Google Colab).

|Model         |Size     |f1 macro|acceleration|Time of inference|
|--------------|---------|------|--------|-------|
|Original model|1.58 GB|0.52  |1x    |49 min 41 sec    |
|onnx.model     |1.58 GB|0.52  |1.6x   |30 min 42 sec    |
|model_quantized.onnx |0.55 GB     |0.51  |2.5x    |19 min 57 sec    |

# How to use ONNX versions

Loading full precision model
```python
import torch
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification
model_id = "fyaronskiy/ModernBERT-large-english-go-emotions"
file_name = "onnx/model.onnx"
model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name)
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

INT8 quantized model

```python
model_id = "fyaronskiy/ModernBERT-large-english-go-emotions"
subfolder = "onnx"
file_name = "model_quantized.onnx"
model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name, subfolder = subfolder)
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

After loading, using ONNX models for inference is the same as for usual Transformer model:
```python
# best thresholds for full precision ONNX model:
best_thresholds = [0.5510204081632653, 0.26530612244897955, 0.14285714285714285, 0.12244897959183673, 0.44897959183673464, 0.22448979591836732, 0.2040816326530612, 0.4081632653061224, 0.5306122448979591, 0.22448979591836732, 0.2857142857142857, 0.3061224489795918, 0.2040816326530612, 0.14285714285714285, 0.1020408163265306, 0.4693877551020408, 0.24489795918367346, 0.3061224489795918, 0.2040816326530612, 0.36734693877551017, 0.2857142857142857, 0.04081632653061224, 0.3061224489795918, 0.16326530612244897, 0.26530612244897955, 0.32653061224489793, 0.12244897959183673, 0.2040816326530612]
# best thresholds for INT8 quantized model:
# best_thresholds = [0.5510204081632653, 0.24489795918367346, 0.18367346938775508, 0.08163265306122448, 0.2857142857142857, 0.32653061224489793, 0.3877551020408163, 0.3877551020408163, 0.44897959183673464, 0.1020408163265306, 0.22448979591836732, 0.12244897959183673, 0.061224489795918366, 0.4693877551020408, 0.16326530612244897, 0.44897959183673464, 0.24489795918367346, 0.26530612244897955, 0.2040816326530612, 0.2040816326530612, 0.2857142857142857, 0.04081632653061224, 0.32653061224489793, 0.14285714285714285, 0.16326530612244897, 0.36734693877551017, 0.12244897959183673, 0.3061224489795918]
LABELS = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
ID2LABEL = dict(enumerate(LABELS))

def detect_emotions(text):
  inputs = tokenizer(text, truncation=True, add_special_tokens=True, max_length=128, return_tensors='pt')
  with torch.no_grad():
      logits = model(**inputs).logits
  probas = torch.sigmoid(logits).squeeze(dim=0)  
  class_binary_labels = (probas > torch.tensor(best_thresholds)).int()
  return [ID2LABEL[label_id] for label_id, value in enumerate(class_binary_labels) if value == 1]
print(detect_emotions('You have excellent service and the best coffee in the city, I love your coffee shop!'))
#['admiration', 'love']
```

I've done quantization with:
```python
from onnxruntime.quantization import quantize_dynamic, QuantType

quantize_dynamic(
    "models/fyaronskiy_ModernBERT-large-english-go-emotions/onnx/model.onnx",
    "models/fyaronskiy_ModernBERT-large-english-go-emotions/onnx/model_quantized.onnx",
    weight_type=QuantType.QUInt8,
    op_types_to_quantize=['MatMul', 'Gemm'],
    per_channel=False,
)
```

