---
library_name: transformers
tags:
- spanish
- mental-health
- roberta
- early-detection
- eating-disorder
- ice
- nlp
language:
- es
base_model:
- ELiRF/RoBERTa-es-mental-large
---
# Model Card

## Model Description

RoBERTa-es-m-large-ICE-MR23-ED is a Spanish language model for **early detection of eating disorder risk**, trained using the **Incremental Context Expansion (ICE)** methodology.
The model builds upon the RoBERTa-es-mental-large foundation model and is specifically fine-tuned to detect eating disorder–related risk signals under early detection and user-level evaluation settings.

The ICE methodology restructures the training data at the **context level**, enabling the model to learn from progressively expanding user message histories instead of complete user timelines.
This training setup better reflects real-world early detection scenarios, where predictions must be issued with limited and incomplete evidence.

The model is based on a RoBERTa-large architecture and supports input sequences of up to **512 tokens**, making it suitable for early detection settings where contextual information is incrementally available.
It has been fine-tuned for the **Eating Disorder (ED)** task using the **MentalRisk 2023 (MR23)** benchmark under early detection conditions.

- Developed by: ELiRF group, VRAIN (Valencian Research Institute for Artificial Intelligence), Universitat Politècnica de València
- Shared by: ELiRF
- Model type: Transformer-based sequence classification model (RoBERTa)
- Language: Spanish
- Base model: RoBERTa-es-mental-large
- License: Same as base model

## Uses

This model is intended for **research purposes** in early mental health risk detection.

### Direct Use

The model can be used directly for **early detection of eating disorder risk** from Spanish user-generated content, where predictions are generated incrementally as new user messages become available.

### Downstream Use

- Early risk detection for eating disorders
- User-level mental health screening
- Comparative studies of early detection methodologies
- Research on incremental and temporally-aware NLP approaches

### Out-of-Scope Use

- Automated intervention systems without human supervision
- Use on languages other than Spanish
- High-stakes or real-time decision-making affecting individuals’ health

## ICE Methodology

Incremental Context Expansion (ICE) is a training methodology designed for early detection tasks.
Rather than training on full user histories, ICE generates **multiple incremental contexts per user**, each corresponding to a partial message history.

This approach enables the model to:
- Learn from early and incomplete evidence
- Improve robustness under early detection evaluation metrics
- Better align training with real-world deployment scenarios

ICE modifies the dataset construction process while keeping the standard fine-tuning pipeline unchanged.

## Bias, Risks, and Limitations

- Training data originates from social media platforms and may contain demographic and cultural biases.
- Automatically translated texts may include translation artifacts.
- Early detection tasks are inherently uncertain due to limited available evidence.
- The model does not provide explanations or clinical interpretations of its predictions.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ELiRF/RoBERTa-es-m-large-ICE-MR23-ED")
model = AutoModelForSequenceClassification.from_pretrained(
    "ELiRF/RoBERTa-es-m-large-ICE-MR23-ED"
)

inputs = tokenizer(
    "Ejemplo de historial de mensajes relacionado con trastornos alimentarios.",
    return_tensors="pt",
    truncation=True,
    max_length=512
)

outputs = model(**inputs)
```

## Training Details

### Training Data

The model was fine-tuned on the **MentalRisk 2023 Eating Disorder (MR23-ED)** dataset.
Training data was restructured using the **ICE methodology**, generating incremental user contexts from original user timelines.

### Training Procedure

- Base model: RoBERTa-es-mental-large
- Fine-tuning strategy: ICE-based context-level training
- Objective: Sequence classification
- Training regime: fp16 mixed precision

## Evaluation

### Results

When evaluated on the MentalRisk 2023 Eating Disorder task, RoBERTa-es-m-large-ICE-MR23-ED shows **competitive performance and improves upon the state of the art** under **early detection** evaluation settings, while also maintaining strong performance in **full-context (user-level)** scenarios.

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
