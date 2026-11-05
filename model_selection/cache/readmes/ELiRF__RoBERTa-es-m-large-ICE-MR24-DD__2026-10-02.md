---
library_name: transformers
tags:
- spanish
- mental-health
- roberta
- disorder-detection
- mentalrisk2024
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

RoBERTa-es-m-large-ICE-MR24-DD is a Spanish language model for **mental disorder detection**, trained using the **Incremental Context Expansion (ICE)** methodology.
The model was developed for the **MentalRisk 2024 Disorder Detection (MR24-DD)** shared task and builds upon the **RoBERTa-es-mental-large** foundation model.

The ICE methodology restructures the training data at the **context level**, enabling the model to learn from progressively expanding user message histories rather than complete user timelines.
This approach allows the model to effectively learn from early and partial evidence while remaining competitive in **full-context (user-level)** evaluation settings.

The model is based on a RoBERTa-large architecture and supports input sequences of up to **512 tokens**, making it suitable for disorder detection scenarios where contextual evidence is incrementally available.
It has been fine-tuned to classify users according to the presence of mental health disorders using Spanish user-generated content.

- Developed by: ELiRF group, VRAIN (Valencian Research Institute for Artificial Intelligence), Universitat Politècnica de València  
- Shared by: ELiRF  
- Model type: Transformer-based sequence classification model (RoBERTa)  
- Language: Spanish  
- Base model: RoBERTa-es-mental-large  
- License: Same as base model
  
## Uses

This model is intended for **research purposes** in mental health disorder detection.

### Direct Use

The model can be used directly for **mental disorder detection** from Spanish user-generated content, generating predictions from incrementally available user message histories.

### Downstream Use

- Mental disorder detection (user-level classification)  
- Early and incremental mental health screening  
- Comparative studies on disorder detection approaches  
- Research on temporally-aware and incremental NLP methods  

### Out-of-Scope Use

- Automated intervention systems without human supervision  
- Use on languages other than Spanish  
- High-stakes decision-making affecting individuals’ health or safety  

## ICE Methodology

Incremental Context Expansion (ICE) is a training methodology designed for early and incremental mental health detection tasks.
Rather than training on complete user histories, ICE generates **multiple incremental contexts per user**, each corresponding to a partial message history.

This methodology allows the model to:
- Learn from incomplete and early evidence  
- Improve robustness under early and incremental evaluation metrics  
- Better align training conditions with real-world deployment scenarios  

ICE modifies the dataset construction process while keeping the standard fine-tuning pipeline unchanged.

## Bias, Risks, and Limitations

- Training data originates from social media platforms and may contain demographic, cultural, and linguistic biases.  
- Automatically translated texts may introduce translation artifacts or subtle semantic shifts.  
- Disorder detection is inherently subjective and context-dependent.  
- The model does not provide explanations or clinical interpretations of its predictions.  

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ELiRF/RoBERTa-es-m-large-ICE-MR24-DD")
model = AutoModelForSequenceClassification.from_pretrained(
    "ELiRF/RoBERTa-es-m-large-ICE-MR24-DD"
)

inputs = tokenizer(
    "Ejemplo de historial de mensajes relacionado con salud mental.",
    return_tensors="pt",
    truncation=True,
    max_length=512
)

outputs = model(**inputs)
```

## Training Details

### Training Data

The model was fine-tuned on the **MentalRisk 2024 Disorder Detection (MR24-DD)** dataset.
Training data was restructured using the **ICE methodology**, generating incremental user contexts from original user timelines.

### Training Procedure

- Base model: RoBERTa-es-mental-large  
- Fine-tuning strategy: ICE-based context-level training  
- Objective: Sequence classification  
- Training regime: fp16 mixed precision  

## Evaluation

### Results

When evaluated on the MentalRisk 2024 Disorder Detection task, **RoBERTa-es-m-large-ICE-MR24-DD** shows **competitive performance and improves upon the state of the art** under both **full-context (user-level)** and **early / incremental detection** evaluation settings.

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
