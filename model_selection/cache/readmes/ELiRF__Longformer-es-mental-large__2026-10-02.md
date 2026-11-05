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
- ELiRF/RoBERTa-es-mental-large
---

# Model Card for Model ID


### Model Description

Longformer-es-mental-large is a Spanish domain-adapted language model designed for the analysis of mental health–related content in long user-generated texts.

It is based on the Longformer architecture, which extends the standard Transformer attention mechanism to efficiently process long sequences. The model supports input sequences of up to 4096 tokens, enabling it to capture long-range dependencies and temporal patterns that are particularly relevant in mental health monitoring and early risk detection settings.

This model was obtained through domain-adaptive pre-training (DAP) on a large corpus of mental health–related texts translated into Spanish from Reddit communities focused on psychological support and mental health discussions. The adaptation process allows the model to better capture emotional expressions, self-disclosure patterns, and discourse structures characteristic of mental health narratives in Spanish.

Longformer-es-mental-large is released as a foundational model and does not include task-specific fine-tuning.

This is the model card of a 🤗 transformers model that has been pushed on the Hub. 

- **Developed by:** ELiRF group, VRAIN (Valencian Research Institute for Artificial Intelligence), Universitat Politècnica de València
- **Model type:** Transformer-based masked language model (Longformer)
- **Language(s) (NLP):** Spanish
- **License:** Same as base model (PlanTL-GOB-ES models)
- **Finetuned from model:** ELiRF/RoBERTa-es-mental-large

## Uses

This model is intended for research purposes in the mental health NLP domain.

### Direct Use

The model can be used directly as a feature extractor or encoder for Spanish mental health–related texts, particularly when long input sequences are required.


### Downstream Use

The model is primarily intended to be fine-tuned for downstream tasks such as:

- Mental disorder detection
- Early risk detection
- User-level and context-level classification
- Analysis of long social media timelines related to psychological well-being

It has been evaluated in early detection benchmarks when fine-tuned using task-specific datasets and methodologies.

### Out-of-Scope Use

- Use on languages other than Spanish
- High-stakes decision-making affecting individuals’ health or safety
- Real-time intervention systems without human supervision

## Bias, Risks, and Limitations

- The training data originates from social media platforms, which may introduce demographic, cultural, and linguistic biases.
- The data was automatically translated into Spanish, which may introduce translation artifacts or subtle semantic drift.
- Mental health language is highly contextual and subjective; predictions may be unstable when evidence is limited.
- The model does not provide explanations or clinical interpretations of its outputs.


## How to Get Started with the Model

Use the code below to get started with the model.

```python
  from transformers import AutoTokenizer, AutoModel
  
  tokenizer = AutoTokenizer.from_pretrained("ELiRF/Longformer-es-mental-large")
  model = AutoModel.from_pretrained("ELiRF/Longformer-es-mental-large")
  
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

All texts were automatically translated into Spanish using neural machine translation. The final dataset contains approximately 1.9 million posts from multiple mental health–related communities.

### Training Procedure

The model was trained using domain-adaptive pre-training (DAP) with a masked language modeling objective.
Pre-training was performed for 20 epochs using multiple GPUs, following the same procedure applied to the other foundational models described in the paper “Improving Mental Health Screening and Early Risk Detection in Spanish”.

No task-specific fine-tuning is included in this checkpoint.

#### Preprocessing [optional]

- Automatic translation to Spanish
- Text normalization and tokenization using the base model tokenizer


#### Training Hyperparameters

- **Training regime:** fp 16 mixed precision

#### Speeds, Sizes, Times [optional]

- **Model size:** ~435M parameters
- **Training duration:** 4 days
- **Checkpoint size:** 1.7GB

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model was evaluated after fine-tuning on Spanish mental health benchmarks (e.g., MentalRisk shared tasks).

#### Factors

- Disorder type
- Amount of available user context
- Early vs full-context settings

#### Metrics

- Macro F1-score
- ERDE (Early Risk Detection Error)
- Latency True Positive (LTP)

### Results

When fine-tuned on Spanish mental health benchmarks, Longformer-es-mental shows competitive performance and improves upon the state of the art in both full-context (user-level) and early detection mental health tasks.

#### Summary

Longformer-es-mental is a Spanish domain-adapted long-context language model for mental health text analysis.
It is based on the Longformer architecture and supports input sequences of up to 4096 tokens, enabling the modeling of long user message histories. The model shows strong performance on Spanish mental health detection and early risk detection tasks when fine-tuned on domain-specific datasets.

## Technical Specifications [optional]

### Model Architecture and Objective

- Longformer architecture
- Masked Language Modeling objective

### Compute Infrastructure

#### Hardware

- Multiple NVIDIA A40 GPUs

## Citation

This model is part of ongoing research currently under review. The final version of the paper will be linked once it is published.

## Model Card Authors 

ELiRF research group (VRAIN, Universitat Politècnica de València)
