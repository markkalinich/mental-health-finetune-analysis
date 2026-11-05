---
library_name: transformers
tags:
- spanish
- mental-health
- roberta
- depression
- mentalrisk2023
- early-detection
- ice
- nlp
language:
- es
base_model:
- ELiRF/RoBERTa-es-mental-large
---
# Model Card

## Model Description

RoBERTa-es-m-large-ICE-MR23-D is a Spanish language model for **early detection of depression risk**, trained using the **Incremental Context Expansion (ICE)** methodology.
The model was developed for the **MentalRisk 2023 Depression (MR23-D)** shared task and builds upon the **RoBERTa-es-mental-large** foundation model.

The ICE methodology restructures the training data at the **context level**, enabling the model to learn from progressively expanding user message histories rather than complete user timelines.
This training setup better reflects real-world early detection scenarios, where predictions must be generated with limited and evolving evidence, while remaining effective in **full-context (user-level)** evaluation settings.

The model is based on a RoBERTa-large architecture and supports input sequences of up to **512 tokens**, making it suitable for depression detection scenarios where contextual information is incrementally available.
It has been fine-tuned to detect depression-related risk signals from Spanish user-generated content.

- Developed by: ELiRF group, VRAIN (Valencian Research Institute for Artificial Intelligence), Universitat Politècnica de València  
- Shared by: ELiRF  
- Model type: Transformer-based sequence classification model (RoBERTa)  
- Language: Spanish  
- Base model: RoBERTa-es-mental-large  
- License: Same as base model  

## Uses

This model is intended for **research purposes** in early mental health risk detection, specifically for depression.

### Direct Use

The model can be used directly for **early detection of depression risk** from Spanish user-generated content, generating predictions incrementally as new user messages become available.

### Downstream Use

- Early risk detection for depression  
- User-level mental health screening  
- Comparative studies on early detection methodologies  
- Research on temporally-aware and incremental NLP models  

### Out-of-Scope Use

- Automated intervention systems without human supervision  
- Use on languages other than Spanish  
- High-stakes decision-making affecting individuals’ health or safety  

## ICE Methodology

Incremental Context Expansion (ICE) is a training methodology designed for early and incremental mental health detection tasks.
Rather than training on complete user histories, ICE generates **multiple incremental contexts per user**, each corresponding to a partial message history.

This approach allows the model to:
- Learn from incomplete and early evidence  
- Reduce detection latency  
- Improve robustness under early detection evaluation metrics  

ICE modifies the dataset construction process while keeping the standard fine-tuning pipeline unchanged.

## Bias, Risks, and Limitations

- Training data originates from social media platforms and may contain demographic, cultural, and linguistic biases.  
- Automatically translated texts may introduce translation artifacts or subtle semantic shifts.  
- Depression detection is inherently subjective and context-dependent.  
- The model does not provide explanations or clinical interpretations of its predictions.  


## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ELiRF/RoBERTa-es-m-large-ICE-MR23-D")
model = AutoModelForSequenceClassification.from_pretrained(
    "ELiRF/RoBERTa-es-m-large-ICE-MR23-D"
)

inputs = tokenizer(
    "Ejemplo de historial de mensajes relacionado con depresión.",
    return_tensors="pt",
    truncation=True,
    max_length=512
)

outputs = model(**inputs)
```

## Training Details

### Training Data

The model was fine-tuned on the **MentalRisk 2023 Depression (MR23-D)** dataset.
Training data was restructured using the **ICE methodology**, generating incremental user contexts from original user timelines.

### Training Procedure

- Base model: RoBERTa-es-mental-large  
- Fine-tuning strategy: ICE-based context-level training  
- Objective: Sequence classification  
- Training regime: fp16 mixed precision  

## Evaluation

### Results

When evaluated on the MentalRisk 2023 Depression task, **RoBERTa-es-m-large-ICE-MR23-D** shows **competitive performance and improves upon the state of the art** under both **early detection** and **full-context (user-level)** evaluation settings.

## Environmental Impact

- Hardware type: NVIDIA A40 GPUs  
- Training time: several hours (fine-tuning)   

## Technical Specifications

### Model Architecture and Objective

- Architecture: RoBERTa (large)  
- Objective: Sequence classification  
- Maximum sequence length: 512 tokens  
- Model size: approximately 355M parameters  

## Citation

This model is part of an ongoing research project.  
The associated paper is currently under review and will be added to this model card once the publication process is completed.


## Model Card Authors

ELiRF research group (VRAIN, Universitat Politècnica de València)