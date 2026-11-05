---
language: en
license: mit
library_name: transformers
tags:
- generated_from_trainer
- text-classification
- fill-mask
- embeddings
metrics:
- accuracy
model-index:
- name: deberta-v3-xsmall-zyda-2
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: Zyphra/Zyda-2 (subset)
      type: Zyphra/Zyda-2
    metrics:
    - type: accuracy
      value: 0.5607
      name: Accuracy
base_model: microsoft/deberta-v3-xsmall
---

# DeBERTa-v3-xsmall-Zyda-2

## Model Description

This model is a fine-tuned version of [microsoft/deberta-v3-xsmall](https://huggingface.co/microsoft/deberta-v3-xsmall) on a subset of the [Zyphra/Zyda-2](https://huggingface.co/datasets/Zyphra/Zyda-2) dataset. It was trained using the Masked Language Modeling (MLM) objective to enhance its understanding of the English language.

## Performance

The model achieves the following results on the evaluation set:
- Loss: 2.6347
- Accuracy: 0.5607

## Intended Uses & Limitations

This model is designed to be used and finetuned for the following tasks:
- Text embedding
- Text classification
- Fill-in-the-blank tasks

**Limitations:**
- English language only
- May be inaccurate for specialized jargon, dialects, slang, code, and LaTeX

## Training Data

The model was trained on the first 300&thinsp;000 rows of the [Zyphra/Zyda-2](https://huggingface.co/datasets/Zyphra/Zyda-2) dataset.
5% of that data was used for validation.

## Training Procedure

### Hyperparameters

The following hyperparameters were used during training:
- Learning rate: 5e-05
- Train batch size: 8
- Eval batch size: 8
- Seed: 42
- Optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- Learning rate scheduler: Linear
- Number of epochs: 1.0

### Framework versions

- Transformers: 4.46.3
- Pytorch: 2.5.1+cu124
- Datasets: 3.1.0
- Tokenizers: 0.20.3

## Usage Examples

### Masked Language Modeling

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='agentlans/deberta-v3-xsmall-zyda-2')
result = unmasker("[MASK] is the capital of France.")
print(result)
```

### Text Embedding

```python
from transformers import AutoTokenizer, AutoModel
import torch

model_name = "agentlans/deberta-v3-xsmall-zyda-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

text = "Example sentence for embedding."
inputs = tokenizer(text, return_tensors='pt')
with torch.no_grad():
    outputs = model(**inputs)

embeddings = outputs.last_hidden_state.mean(dim=1)
print(embeddings)
```

## Ethical Considerations and Bias

As this model is trained on a subset of the Zyda-2 dataset, it may inherit biases present in that data. Users should be aware of potential biases and evaluate the model's output critically, especially for sensitive applications.

## Additional Information

For more details about the base model, please refer to [microsoft/deberta-v3-xsmall](https://huggingface.co/microsoft/deberta-v3-xsmall).
