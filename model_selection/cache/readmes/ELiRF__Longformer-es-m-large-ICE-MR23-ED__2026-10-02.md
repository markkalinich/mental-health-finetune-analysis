---
library_name: transformers
tags:
- spanish
- mental-health
- longformer
- early-detection
- eating-disorder
- ice
- nlp
language:
- es
base_model:
- ELiRF/Longformer-es-mental-large
---
# Model Card

## Model Description

Longformer-es-m-large-ICE-MR23-ED is a Spanish long-context language model for **early detection of eating disorder risk**, trained using the **Incremental Context Expansion (ICE)** methodology.
The model builds upon the Longformer-es-mental-large foundation model and is specifically adapted to detect eating disorder–related risk signals under early detection and user-level evaluation settings.

The ICE methodology restructures the training data at the **context level**, enabling the model to learn from progressively expanding user message histories rather than full user timelines.
This approach better reflects real-world early detection scenarios, where predictions must be issued before the full user history is available.

The model is based on the Longformer architecture and supports input sequences of up to **4096 tokens**, allowing it to effectively integrate evidence distributed across multiple messages over time.
It has been fine-tuned for the **Eating Disorder (ED)** task using the **MentalRisk 2023 (MR23)** benchmark under early detection conditions.

- Developed by: ELiRF group, VRAIN (Valencian Research Institute for Artificial Intelligence), Universitat Politècnica de València
- Shared by: ELiRF
- Model type: Transformer-based sequence classification model (Longformer)
- Language: Spanish
- Base model: Longformer-es-mental-large
- License: Same as base model

## Uses

This model is intended for **research purposes** in early mental health risk detection.

### Direct Use

The model can be used directly for **early detection of eating disorder risk** from Spanish user-generated content, where predictions are generated incrementally as new messages become available.

### Downstream Use

- Early risk detection for eating disorders
- User-level mental health screening
- Comparative studies on early detection methodologies

### Out-of-Scope Use

- Automated intervention systems without human supervision
- Use on languages other than Spanish
- High-stakes or real-time decision-making affecting individuals’ health

## ICE Methodology

Incremental Context Expansion (ICE) is a training methodology designed for early detection tasks.
Instead of training on full user histories, ICE creates **multiple incremental contexts per user**, each corresponding to a partial message history.

This approach allows the model to:
- Learn from early and incomplete evidence
- Reduce detection latency
- Improve robustness under early detection evaluation metrics

The ICE methodology modifies the dataset construction process while keeping the standard fine-tuning pipeline unchanged.

## Bias, Risks, and Limitations

- The training data originates from social media platforms and may contain demographic and cultural biases.
- Automatically translated texts may include translation artifacts.
- Early detection tasks are inherently uncertain due to limited available evidence.
- The model does not provide explanations or clinical interpretations of its predictions.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ELiRF/Longformer-es-m-large-ICE-MR23-ED")
model = AutoModelForSequenceClassification.from_pretrained(
    "ELiRF/Longformer-es-m-large-ICE-MR23-ED"
)

inputs = tokenizer(
    "Ejemplo de historial de mensajes relacionado con trastornos alimentarios.",
    return_tensors="pt",
    truncation=True,
    max_length=4096
)

outputs = model(**inputs)
```

## Training Details

### Training Data

The model was fine-tuned on the **MentalRisk 2023 Eating Disorder (MR23-ED)** dataset.
Training data was restructured using the **ICE methodology**, generating incremental user contexts from original user history.

### Training Procedure

- Base model: Longformer-es-mental-large
- Fine-tuning strategy: ICE-based context-level training
- Objective: Sequence classification
- Training regime: fp16 mixed precision

## Evaluation

### Results

When evaluated on the MentalRisk 2023 Eating Disorder task, Longformer-es-m-large-ICE-MR23-ED shows **competitive performance and improves upon the state of the art** under **early detection** evaluation settings, while also maintaining strong performance in **full-context (user-level)** scenarios.

## Environmental Impact

- Hardware type: NVIDIA A40 GPUs
- Training time: approximately several hours (fine-tuning)

## Technical Specifications

### Model Architecture and Objective

- Architecture: Longformer (large)
- Objective: Sequence classification
- Maximum sequence length: 4096 tokens
- Model size: approximately 435M parameters

## Citation

This model is part of an ongoing research project.
The associated paper is currently under review and will be added to this model card once the publication process is completed.

## Model Card Authors

ELiRF research group (VRAIN, Universitat Politècnica de València)