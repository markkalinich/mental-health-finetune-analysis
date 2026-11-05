---
library_name: transformers
language:
- es
base_model:
- PlanTL-GOB-ES/roberta-large-bne
tags:
- spanish
- mental-health
- roberta
- domain-adaptation
- nlp
---

# Model Card for RoBERTa-es-mental-large

## Model Description

RoBERTa-es-mental-large is a Spanish domain-adapted language model specialized in mental health text analysis.
The model is designed to capture linguistic, emotional, and semantic patterns commonly found in mental health–related narratives shared on social media and online support communities.

It is based on a RoBERTa-large architecture and supports input sequences of up to 512 tokens, making it suitable for full-context (user-level) and context-level classification scenarios.
The model was obtained through domain-adaptive pre-training (DAP) on a large corpus of mental health–related texts translated into Spanish from Reddit communities focused on psychological support and mental health discussions.

RoBERTa-es-mental-large is released as a foundational model and does not include task-specific fine-tuning.

- Developed by: ELiRF group, VRAIN (Valencian Research Institute for Artificial Intelligence), Universitat Politècnica de València
- Funded by: Spanish Agencia Estatal de Investigación (AEI), MCIN/AEI, ERDF
- Shared by: ELiRF
- Model type: Transformer-based masked language model (RoBERTa)
- Language: Spanish
- License: Same as base model (PlanTL-GOB-ES models)
- Finetuned from model: PlanTL-GOB-ES/roberta-large-bne

## Model Sources

- Repository: https://huggingface.co/ELiRF/RoBERTa-es-mental-large
- Paper: Improving Mental Health Screening and Early Risk Detection in Spanish (under review)
- Demo: Not available

## Uses

This model is intended for research purposes in the mental health NLP domain.

### Direct Use

The model can be used directly as a language encoder or feature extractor for Spanish mental health–related texts, particularly in settings where the full user context fits within the standard Transformer input length.

### Downstream Use

RoBERTa-es-mental-large is primarily intended to be fine-tuned for downstream tasks such as:

- Mental disorder detection
- Mental health screening
- User-level and context-level classification
- Social media analysis related to psychological well-being

### Out-of-Scope Use

- Clinical diagnosis or medical decision-making
- Real-time intervention systems without human supervision
- Use on languages other than Spanish
- High-stakes decision-making affecting individuals’ health or safety

## Bias, Risks, and Limitations

- Training data originates from social media platforms, which may introduce demographic, cultural, and linguistic biases.
- All texts were automatically translated into Spanish, potentially introducing translation artifacts or subtle semantic shifts.
- Mental health language is highly contextual and subjective; predictions may be unreliable when very limited context is available.
- The model does not provide explanations or clinical interpretations of its outputs.

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("ELiRF/RoBERTa-es-mental-large")
model = AutoModel.from_pretrained("ELiRF/RoBERTa-es-mental-large")

inputs = tokenizer(
    "Ejemplo de texto relacionado con salud mental.",
    return_tensors="pt",
    truncation=True,
    max_length=512
)

outputs = model(**inputs)
```

## Training Details

### Training Data

The model was domain-adapted using a merged corpus composed of:

- Reddit SuicideWatch and Mental Health Collection (SWMH)
- Reddit Mental Health Narratives (RMHN)

All texts were automatically translated into Spanish using neural machine translation.
The resulting dataset contains approximately 1.9 million posts from multiple mental health-related communities (e.g., depression, anxiety, suicide ideation, loneliness), providing broad coverage of informal mental health discourse.

### Training Procedure

The model was trained using domain-adaptive pre-training (DAP) with a masked language modeling objective.

- Training regime: fp16 mixed precision
- Number of epochs: 20
- Hardware: multiple NVIDIA A40 GPUs
- Training duration: approximately 4 days

No task-specific fine-tuning is included in this checkpoint.

## Evaluation

### Results

When fine-tuned on Spanish mental health benchmarks, RoBERTa-es-mental-large shows competitive performance and improves upon the state of the art in full-context (user-level) mental health classification tasks.

## Technical Specifications

### Model Architecture and Objective

- Architecture: RoBERTa
- Objective: Masked Language Modeling

## Citation

The associated paper is currently under review and will be added to this model card once the publication process is completed.

## Model Card Authors

ELiRF research group (VRAIN, Universitat Politècnica de València)

