---
library_name: transformers
tags:
- spanish
- mental-health
- longformer
- domain-adaptation
- nlp
language:
- es
base_model:
- PlanTL-GOB-ES/longformer-base-4096-bne-es
---

## Model Description

Longformer-es-mental-base is the base-sized version of the Longformer-es-mental family, a Spanish domain-adapted language model designed for mental health text analysis on long user-generated content.
The model is intended for scenarios where relevant mental health signals are distributed across multiple messages, such as social media timelines, forum threads, or user message histories.

It is based on the Longformer architecture, which extends the standard Transformer attention mechanism to efficiently process long sequences.
The model supports input sequences of up to 4096 tokens, enabling it to capture long-range dependencies and temporal patterns that are particularly relevant for mental health screening tasks.

Longformer-es-mental-base was obtained through domain-adaptive pre-training (DAP) on a large corpus of mental health–related texts translated into Spanish from Reddit communities focused on psychological support and mental health discussions.
This adaptation allows the model to better capture emotional expression, self-disclosure patterns, and discourse structures characteristic of mental health narratives in Spanish.

The model is released as a foundational model and does not include task-specific fine-tuning.

- Developed by: ELiRF group, VRAIN (Valencian Research Institute for Artificial Intelligence), Universitat Politècnica de València
- Funded by: Spanish Agencia Estatal de Investigación (AEI), MCIN/AEI, ERDF
- Shared by: ELiRF
- Model type: Transformer-based masked language model (Longformer)
- Language: Spanish
- License: Same as base model (PlanTL-GOB-ES models)
- Finetuned from model: PlanTL-GOB-ES/longformer-base-4096-bne-es

## Uses

This model is intended for research purposes in the mental health NLP domain.

### Direct Use

The model can be used directly as a language encoder or feature extractor for Spanish mental health–related texts when long input sequences are required and computational efficiency is a concern.

### Downstream Use

Longformer-es-mental-base is primarily intended to be fine-tuned for downstream tasks such as:

- Mental disorder detection
- Mental health screening
- User-level and context-level classification
- Early risk detection tasks involving long message histories
- Social media analysis related to psychological well-being

### Out-of-Scope Use

- Real-time intervention systems without human supervision
- Use on languages other than Spanish
- High-stakes decision-making affecting individuals’ health or safety

## Bias, Risks, and Limitations

- Training data originates from social media platforms, which may introduce demographic, cultural, and linguistic biases.
- All texts were automatically translated into Spanish, potentially introducing translation artifacts or subtle semantic shifts.
- Mental health language is highly contextual and subjective; predictions may be unreliable when very limited evidence is available.
- The model does not provide explanations or clinical interpretations of its outputs.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("ELiRF/Longformer-es-mental-base")
model = AutoModel.from_pretrained("ELiRF/Longformer-es-mental-base")

inputs = tokenizer(
    "Ejemplo de texto relacionado con salud mental.",
    return_tensors="pt",
    truncation=True,
    max_length=4096
)

outputs = model(**inputs)
```

## Training Details

### Training Data

The model was domain-adapted using a merged corpus composed of:

- Reddit SuicideWatch and Mental Health Collection (SWMH)
- Reddit Mental Health Narratives (RMHN)

All texts were automatically translated into Spanish using neural machine translation.
The resulting dataset contains approximately 1.9 million posts from multiple mental health–related communities (e.g., depression, anxiety, suicide ideation, loneliness), providing broad coverage of informal mental health discourse.

### Training Procedure

The model was trained using domain-adaptive pre-training (DAP) with a masked language modeling objective.

- Training regime: fp16 mixed precision
- Number of epochs: 20
- Hardware: multiple NVIDIA A40 GPUs
- Training duration: approximately 4 days

No task-specific fine-tuning is included in this checkpoint.

## Evaluation

### Results

When fine-tuned on Spanish mental health benchmarks, Longformer-es-mental-base shows competitive performance.

## Technical Specifications

### Model Architecture and Objective

- Architecture: Longformer
- Objective: Masked Language Modeling
- Model size: approximately 150M parameters (base version)

## Citation

This model is part of an ongoing research project.
The associated paper is currently under review and will be added to this model card once the publication process is completed.

## Model Card Authors

ELiRF research group (VRAIN, Universitat Politècnica de València)