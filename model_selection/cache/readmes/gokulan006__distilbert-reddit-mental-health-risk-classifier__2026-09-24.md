---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: distillbert_model
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distillbert_model

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4282
- Accuracy: 0.8545
- F1: 0.8532

## Model description

---
language:
- en

license: mit

library_name: transformers

pipeline_tag: text-classification

tags:
- mental-health
- suicide-risk
- distilbert
- nlp
- text-classification
- reddit
- crisis-detection
- healthcare
---

# DistilBERT Reddit Mental Health Risk Classifier

A fine-tuned **DistilBERT** model for classifying Reddit posts into three mental health risk categories:

- 🔴 High Risk
- 🟡 Moderate Risk
- 🟢 Low Risk

This model was developed as part of the **Google Summer of Code (GSoC) 2026** project with **HumanAI** to support research on AI-assisted mental health crisis detection.

---

## Model Details

- **Base Model:** distilbert-base-uncased
- **Architecture:** DistilBERT
- **Framework:** Hugging Face Transformers
- **Task:** Multi-class Text Classification
- **Number of Classes:** 3

### Risk Categories

| Label | Description |
|--------|-------------|
| High Risk | Explicit suicidal ideation, suicide planning, self-harm intent, immediate crisis |
| Moderate Risk | Depression, anxiety, hopelessness, emotional distress, substance abuse without explicit suicidal intent |
| Low Risk | General discussions, daily life experiences, emotionally neutral or non-crisis mental health posts |

---

# Dataset

The model was fine-tuned on a Reddit-based mental health dataset containing approximately **55,000+ posts** collected from mental health related communities.

The dataset consists of three balanced risk categories:

- High Risk
- Moderate Risk
- Low Risk

Posts were preprocessed using:

- Text normalization
- URL removal
- Lowercasing
- Stopword removal
- Duplicate removal

---

# Training Configuration

| Parameter | Value |
|-----------|------:|
| Learning Rate | 2e-5 |
| Batch Size | 8 |
| Epochs | 3 |
| Weight Decay | 0.01 |
| Optimizer | AdamW |

---

# Evaluation

| Epoch | Training Loss | Validation Loss | Accuracy | Weighted F1 |
|------:|--------------:|----------------:|---------:|------------:|
| 1 | 0.2657 | 0.4282 | **85.45%** | **85.32%** |
| 2 | 0.2367 | 0.5043 | **85.80%** | **85.71%** |
| 3 | 0.1542 | 0.6890 | **85.79%** | **85.69%** |

Best Validation Accuracy:

**85.80%**

Best Weighted F1 Score:

**85.71%**

---

# Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "gokulan006/distilbert-reddit-mental-health-risk-classifier"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

text = "I don't want to live anymore."

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=128
)

with torch.no_grad():
    outputs = model(**inputs)

prediction = torch.argmax(outputs.logits, dim=1).item()

labels = {
    0: "High Risk",
    1: "Low Risk",
    2: "Moderate Risk"
}

print(labels[prediction])
```

---

# Example Predictions

| Input | Prediction |
|--------|------------|
| "I've recently started exercising and my mood has improved." | Low Risk |
| "I've been feeling empty for months and nothing makes me happy anymore." | Moderate Risk |
| "I've decided tonight will be my last night." | High Risk |

---

# Intended Use

This model is intended for:

- Mental health research
- NLP benchmarking
- AI-assisted crisis monitoring
- Educational purposes
- Research prototypes

---

# Limitations

- This model **does not provide medical advice**.
- Predictions should **never** be used as the sole basis for clinical or emergency decisions.
- Performance may vary across different platforms, writing styles, and populations.
- Human review is recommended for high-risk predictions.

---

# Citation

If you use this model in your research, please cite:

```
@misc{gokulan2026distilbert,
  title={DistilBERT Reddit Mental Health Risk Classifier},
  author={Gokulan M},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/gokulan006/distilbert-reddit-mental-health-risk-classifier}
}
```

---

# Acknowledgements

Developed during **Google Summer of Code (GSoC) 2026** under the **HumanAI** organization.

Special thanks to the HumanAI mentors and the open-source NLP community for their guidance and support.

 
 

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 0.2657        | 1.0   | 4790  | 0.4282          | 0.8545   | 0.8532 |
| 0.2367        | 2.0   | 9580  | 0.5043          | 0.8580   | 0.8571 |
| 0.1542        | 3.0   | 14370 | 0.6890          | 0.8579   | 0.8569 |


### Framework versions

- Transformers 5.12.1
- Pytorch 2.11.0+cu128
- Datasets 4.0.0
- Tokenizers 0.22.2
