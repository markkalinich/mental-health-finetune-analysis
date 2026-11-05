---
library_name: transformers
pipeline_tag: text-classification
tags:
- medical
- guardrail
- onnx
- int8
---

# Medical Guardrail (mmBERT) V4

This is an optimized, multi-label sequence classification model designed for medical routing and safety guardrails. It is built on top of `jhu-clsp/mmBERT-base` and fine-tuned for high-speed, enterprise-grade inference.

### Architectures Included
This repository contains the model in three different formats to support various deployment environments:
* **Standard PyTorch:** Available in the root directory.
* **ONNX (FP32):** Available in the `onnx/fp32` directory.
* **ONNX (INT8 Quantized):** Available in the `onnx/int8` directory (Recommended for CPU production).

---

### Classes & Priority Order
The model outputs probabilities for 6 distinct classes. In production, we route based on the following strict priority order to ensure safety:
1. **Injection** (Class 5) - *Highest Priority (Instantly block prompt injection/jailbreaks)*
2. **Emergency** (Class 0) - *(Route to human/emergency protocols)*
3. **Malice_Abuse** (Class 4) - *(Block abusive language)*
4. **Medical_Illogical** (Class 2) - *(Flag logically flawed medical queries)*
5. **Medical_Logical** (Class 1) - *(Safe medical queries)*
6. **General_Chat** (Class 3) - *Lowest Priority (Standard non-medical conversation)*

> **Note on Outputs:** Because this is a Multi-Label classification model, the model outputs raw logits. You **must** apply a Sigmoid activation function (e.g., `torch.sigmoid()` or `scipy.special.expit()`) to the outputs to get the final confidence probabilities. Do not use Softmax.

---

## Usage 

### 1. Standard PyTorch
Because the PyTorch files are in the root directory, you can load them using standard `transformers`.
```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

repo_id = "Kirosama/medical-guardrail-mmbert-V4"
# fix_mistral_regex=True silences the known upstream regex warning
tokenizer = AutoTokenizer.from_pretrained(repo_id, fix_mistral_regex=True)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)

inputs = tokenizer("I have severe chest pain.", return_tensors="pt")
with torch.no_grad():
    logits = model(**inputs).logits
    # Apply Sigmoid to get probabilities
    probabilities = torch.sigmoid(logits)[0].tolist()
```

### 2. ONNX (FP32)
To load the ONNX graph, switch from `transformers` to `optimum` and specify the subfolder.
```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer

repo_id = "Kirosama/medical-guardrail-mmbert-V4"
tokenizer = AutoTokenizer.from_pretrained(repo_id, fix_mistral_regex=True)

ort_fp32_model = ORTModelForSequenceClassification.from_pretrained(
    repo_id,
    subfolder="onnx/fp32"
)
```

### 3. ONNX (INT8 Quantized) - Production
This is the ultra-fast production model. You must specify both the `subfolder` and the custom `file_name` because the quantizer appends `_quantized` to the file.
```python
from optimum.onnxruntime import ORTModelForSequenceClassification
from transformers import AutoTokenizer

repo_id = "Kirosama/medical-guardrail-mmbert-V4"
tokenizer = AutoTokenizer.from_pretrained(repo_id, fix_mistral_regex=True)

ort_int8_model = ORTModelForSequenceClassification.from_pretrained(
    repo_id,
    subfolder="onnx/int8",
    file_name="model_quantized.onnx"
)
```
