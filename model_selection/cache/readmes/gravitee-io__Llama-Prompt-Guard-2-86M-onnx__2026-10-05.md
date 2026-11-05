---
license: llama4
language:
  - en
  - fr
  - de
  - hi
  - it
  - pt
  - es
  - th
base_model:
- meta-llama/Llama-Prompt-Guard-2-86M
pipeline_tag: text-classification
tags:
  - facebook
  - meta
  - llama
  - llama4
  - safety
  - gravitee-io
  - ai-gateway
---

# Llama-Prompt-Guard-2-86M-onnx

This repository provides a ONNX converted and quantized version of meta-llama/Llama-Prompt-Guard-2-86M

## 🧠 Built With

- Meta LLaMA – Foundation model powering the classifier 
  - [meta-llama/Llama-Prompt-Guard-2-22M](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-22M)
  - [meta-llama/Llama-Prompt-Guard-2-86M](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M)
- 🤗 Hugging Face Transformers – Model and tokenizer loading
- ONNX – Model export and runtime format
- ONNX Runtime – Efficient inference backend

## 📥 Evaluation Dataset

We use [`jackhhao/jailbreak-classification`](https://huggingface.co/datasets/jackhhao/jailbreak-classification)
for the evaluation (train+test)

## 🧪 Evaluation Results

| Model                      | Accuracy | Precision | Recall | F1 Score | AUC-ROC |
|----------------------------|----------|-----------|--------|----------|---------|
| Llama-Prompt-Guard-2-22M   | 0.9564   | 0.9888    | 0.9249 | 0.9558   | 0.9234  |
| Llama-Prompt-Guard-2-22M-q | 0.9579   | 0.9967    | 0.9204 | 0.9449   | 0.9180  |
| Llama-Prompt-Guard-2-86M   | 0.9801   | 0.9984    | 0.9625 | 0.9801   | 0.9519  |
| Llama-Prompt-Guard-2-86M-q | 0.8989   | 1.0000    | 0.8018 | 0.89     | 0.7452  |

## 🤗 Usage

```python
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForSequenceClassification
import numpy as np

# Load model and tokenizer using optimum
model = ORTModelForSequenceClassification.from_pretrained("gravitee-io/Llama-Prompt-Guard-2-86M-onnx", file_name="model.quant.onnx")
tokenizer = AutoTokenizer.from_pretrained("gravitee-io/Llama-Prompt-Guard-2-86M-onnx")

# Tokenize input
text = "Your comment here"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

# Run inference
outputs = model(**inputs)
logits = outputs.logits

# Optional: convert to probabilities
probs = 1 / (1 + np.exp(-logits))
print(probs)
```

## 🐙 GitHub Repository: 

You can find the full source code, CLI tools, and evaluation scripts in the official [GitHub repository](https://github.com/gravitee-io-labs/Llama-Prompt-Guard-2-onnx).