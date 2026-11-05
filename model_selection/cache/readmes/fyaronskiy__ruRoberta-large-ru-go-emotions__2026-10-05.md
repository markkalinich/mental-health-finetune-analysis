---
library_name: transformers
license: mit
datasets:
- seara/ru_go_emotions
base_model: ai-forever/ruRoberta-large
base_model_relation: finetune
language:
- ru
tags:
- Text Classification
- emotion-classification
- emotion-recognition
- emotion-detection
- emotion
metrics:
- f1
- precision
- recall
pipeline_tag: text-classification
---

This is the best russian opensource model for detecting all 27 types of emotions:


| Model                                                                  | F1 macro | F1 macro weighted | Precision macro | Recall macro | Size|
|------------------------------------------------------------------------|----------|-------------------|-----------------|--------------|-----|
| [seara/rubert-tiny2-ru-go-emotions](https://huggingface.co/seara/rubert-tiny2-russian-emotion-detection-ru-go-emotions)   | 0.33     | 0.48    | 0.51  | 0.29  | 29.2M| 
| [seara/rubert-base-cased-ru-go-emotions](https://huggingface.co/seara/rubert-base-cased-russian-emotion-detection-ru-go-emotions)  | 0.36     | 0.49      | 0.52  | 0.31   | 178M|
| [fyaronskiy/ruRoberta-large-ru-go-emotions](https://huggingface.co/fyaronskiy/ruRoberta-large-ru-go-emotions) default thresholds = 0.5  | 0.41     | 0.52   | **0.58**  | 0.36  | 355M |
| [fyaronskiy/ruRoberta-large-ru-go-emotions](https://huggingface.co/fyaronskiy/ruRoberta-large-ru-go-emotions) best thresholds               | **0.48** | **0.58** | 0.46 | **0.55**  | 355M |
| [fyaronskiy/deberta-v1-base-russian-go-emotions](https://huggingface.co/fyaronskiy/deberta-v1-base-russian-go-emotions)                          | **0.48** | 0.57 | 0.46   | 0.54  | 125M |


# Summary
This is [ruRoberta-large](https://huggingface.co/ai-forever/ruRoberta-large) model finetuned on [ru_go_emotions](https://huggingface.co/datasets/seara/ru_go_emotions) 
dataset for multilabel classification. Model can be used to extract all emotions from text or detect certain emotions. 
Thresholds are selected on validation set by maximizing f1 macro over all labels.

The quality of the model varies greatly across all classes (look at the table with metrics below). There are classes like 
amusement, gratitude, where the model shows high recognition quality, and classes that pose difficulties for the model - grief, relief, 
that do have much fewer examples in the training data.

Also ONNX version of model and INT8 quantized model is available. information about them is posted in the last sections. 

# Usage
Using model with Huggingface Transformers:
```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("fyaronskiy/ruRoberta-large-ru-go-emotions")
model = AutoModelForSequenceClassification.from_pretrained("fyaronskiy/ruRoberta-large-ru-go-emotions")

best_thresholds = [0.36734693877551017, 0.2857142857142857, 0.2857142857142857, 0.16326530612244897, 0.14285714285714285, 0.14285714285714285, 0.18367346938775508, 0.3469387755102041, 0.32653061224489793, 0.22448979591836732, 0.2040816326530612, 0.2857142857142857, 0.18367346938775508, 0.2857142857142857, 0.24489795918367346, 0.7142857142857142, 0.02040816326530612, 0.3061224489795918, 0.44897959183673464, 0.061224489795918366, 0.18367346938775508, 0.04081632653061224, 0.08163265306122448, 0.1020408163265306, 0.22448979591836732, 0.3877551020408163, 0.3469387755102041, 0.24489795918367346]
LABELS = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
ID2LABEL = dict(enumerate(LABELS))
```

Here is how you can extract emotions contained in text: 

```python
def predict_emotions(text):
  inputs = tokenizer(text, truncation=True, add_special_tokens=True, max_length=128, return_tensors='pt')
  with torch.no_grad():
      logits = model(**inputs).logits
  probas = torch.sigmoid(logits).squeeze(dim=0)  
  class_binary_labels = (probas > torch.tensor(best_thresholds)).int()
  return [ID2LABEL[label_id] for label_id, value in enumerate(class_binary_labels) if value == 1]

print(predict_emotions('У вас отличный сервис и лучший кофе в городе, обожаю вашу кофейню!'))

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

print(predict('У вас отличный сервис и лучший кофе в городе, обожаю вашу кофейню!'))
'''{'admiration': 0.81,
 'love': 0.538,
 'joy': 0.041,
 'gratitude': 0.031,
 'approval': 0.026,
 'excitement': 0.023,
 'neutral': 0.009,
 'curiosity': 0.006,
 'amusement': 0.005,
 'desire': 0.005,
 'realization': 0.005,
 'caring': 0.004,
 'confusion': 0.004,
 'surprise': 0.004,
 'disappointment': 0.003,
 'disapproval': 0.003,
 'anger': 0.002,
 'annoyance': 0.002,
 'disgust': 0.002,
 'fear': 0.002,
 'grief': 0.002,
 'optimism': 0.002,
 'pride': 0.002,
 'relief': 0.002,
 'sadness': 0.002,
 'embarrassment': 0.001,
 'nervousness': 0.001,
 'remorse': 0.001}
'''
```

# Eval results on test split of ru-go-emotions                                             


|              |precision|recall|f1-score|support|threshold|
|--------------|---------|------|--------|-------|---------|
|admiration    |0.63     |0.75  |0.69    |504    |0.37     |
|amusement     |0.76     |0.91  |0.83    |264    |0.29     |
|anger         |0.47     |0.32  |0.38    |198    |0.29     |
|annoyance     |0.33     |0.39  |0.36    |320    |0.16     |
|approval      |0.27     |0.58  |0.37    |351    |0.14     |
|caring        |0.32     |0.59  |0.41    |135    |0.14     |
|confusion     |0.41     |0.52  |0.46    |153    |0.18     |
|curiosity     |0.45     |0.73  |0.55    |284    |0.35     |
|desire        |0.54     |0.31  |0.40    |83     |0.33     |
|disappointment|0.31     |0.34  |0.33    |151    |0.22     |
|disapproval   |0.31     |0.57  |0.40    |267    |0.20     |
|disgust       |0.44     |0.40  |0.42    |123    |0.29     |
|embarrassment |0.48     |0.38  |0.42    |37     |0.18     |
|excitement    |0.29     |0.43  |0.34    |103    |0.29     |
|fear          |0.56     |0.78  |0.65    |78     |0.24     |
|gratitude     |0.95     |0.85  |0.89    |352    |0.71     |
|grief         |0.03     |0.33  |0.05    |6      |0.02     |
|joy           |0.48     |0.58  |0.53    |161    |0.31     |
|love          |0.73     |0.84  |0.78    |238    |0.45     |
|nervousness   |0.24     |0.48  |0.32    |23     |0.06     |
|optimism      |0.57     |0.54  |0.56    |186    |0.18     |
|pride         |0.67     |0.38  |0.48    |16     |0.04     |
|realization   |0.18     |0.31  |0.23    |145    |0.08     |
|relief        |0.30     |0.27  |0.29    |11     |0.10     |
|remorse       |0.53     |0.84  |0.65    |56     |0.22     |
|sadness       |0.56     |0.53  |0.55    |156    |0.39     |
|surprise      |0.55     |0.57  |0.56    |141    |0.35     |
|neutral       |0.59     |0.79  |0.68    |1787   |0.24     |
|micro avg     |0.50     |0.66  |0.57    |6329   |         |
|macro avg     |0.46     |0.55  |0.48    |6329   |         |
|weighted avg  |0.53     |0.66  |0.58    |6329   |         |


# ONNX and quantized versions of model


Full precision ONNX model (onnx/model.onnx) - 1.5x faster than Transformer model, quality is the same.

INT8 quantized model (onnx/model_quantized.onnx) - 2.5x faster than Transformer model, quality is almost the same.

In table below results of tests of inference of 5427 samples of test_set.
I tested inference with batch_size 1 on Intel Xeon CPU with 2 vCPUs (Google Colab).

|Model         |Size     |f1 macro|acceleration|Time of inference|
|--------------|---------|------|--------|-------|
|Original model|1.4 GB|0.48  |1x    |44 min 55 sec    |
|onnx.model     |1.4 GB|0.48  |1.5x   |29 min 52 sec    |
|model_quantized.onnx |0.36 GB     |0.48  |2.5x    |18 min 10 sec    |

# How to use ONNX versions

Loading full precision model
```python
from optimum.onnxruntime import ORTModelForSequenceClassification
model_id = "fyaronskiy/ruRoberta-large-ru-go-emotions"
file_name = "onnx/model.onnx"
model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name)
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

INT8 quantized model

```python
model_id = "fyaronskiy/ruRoberta-large-ru-go-emotions"
file_name = "onnx/model_quantized.onnx"

model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name)
tokenizer = AutoTokenizer.from_pretrained(model_id)
```

After loading, using ONNX models for inference is the same as for usual Transformer model:
```python
best_thresholds = [0.36734693877551017, 0.2857142857142857, 0.2857142857142857, 0.16326530612244897, 0.14285714285714285, 0.14285714285714285, 0.18367346938775508, 0.3469387755102041, 0.32653061224489793, 0.22448979591836732, 0.2040816326530612, 0.2857142857142857, 0.18367346938775508, 0.2857142857142857, 0.24489795918367346, 0.7142857142857142, 0.02040816326530612, 0.3061224489795918, 0.44897959183673464, 0.061224489795918366, 0.18367346938775508, 0.04081632653061224, 0.08163265306122448, 0.1020408163265306, 0.22448979591836732, 0.3877551020408163, 0.3469387755102041, 0.24489795918367346]
LABELS = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
ID2LABEL = dict(enumerate(LABELS))

def predict_emotions(text):
  inputs = tokenizer(text, truncation=True, add_special_tokens=True, max_length=128, return_tensors='pt')
  with torch.no_grad():
      logits = model(**inputs).logits
  probas = torch.sigmoid(logits).squeeze(dim=0)  
  class_binary_labels = (probas > torch.tensor(best_thresholds)).int()
  return [ID2LABEL[label_id] for label_id, value in enumerate(class_binary_labels) if value == 1]

print(predict_emotions('У вас отличный сервис и лучший кофе в городе, обожаю вашу кофейню!'))
#['admiration', 'love']
```