---
library_name: transformers
tags:
- audio-classification
- mood-detection
- music
- pytorch
- hubert
license: apache-2.0
datasets:
- beastLucifer/sangeetkar-mood-dataset
- beastLucifer/sangeetkar-teacher-labels
language:
- en
metrics:
- accuracy
base_model:
- sandychoii/distilhubert-finetuned-gtzan-audio-classification
pipeline_tag: audio-classification
---

# Ostrich-v1: Audio Mood Classification Model

## Model Overview

**Ostrich-v1** is a production-grade **multi-label audio classification model** fine-tuned for detecting **musical moods in Indian music** (Bollywood, Indie, Folk, Classical, Fusion, etc.).  
It uses a **teacher–student distillation pipeline** to map rich acoustic representations to **31 fine-grained mood dimensions**, including culturally specific emotional categories.

- **Developed by:** beastLucifer  
- **Model type:** Multi-label Audio Classification  
- **Domain:** Music (Indian & South Asian context)  
- **Languages:** English, Hindi (musical semantics)  
- **License:** Apache 2.0  
- **Finetuned from:** `sandychoii/distilhubert-finetuned-gtzan-audio-classification`  

---

## Model Description

Ostrich-v1 bridges the gap between generic audio emotion models and the **emotional textures unique to South Asian music**.  
The model is built on a **DistilHuBERT backbone**, fine-tuned on the **Sangeetkar** dataset using **teacher-generated soft labels** produced by a CLAP-based audio–text model.

It supports both:
- **Global moods** (e.g., *Happy, Sad, Angry*)
- **Regionally grounded moods** (e.g., *Dard-bhari, Tapori, Sufi-romantic*)

The output is a **31-dimensional probability vector**, allowing multiple moods to coexist per track.

---

## Model Sources

- **Repository:** `beastLucifer/ostrich-v1-audio-mood`
- **Training Audio Dataset:** `beastLucifer/sangeetkar-mood-dataset`
- **Teacher Label Dataset:** `beastLucifer/sangeetkar-teacher-labels`

---

## Intended Uses

### Direct Use
- Automated music tagging and metadata enrichment  
- Mood-based playlist generation  
- Music discovery systems for Indian sub-genres  
- Recommendation systems and catalog analytics  

### Out-of-Scope Use
- Speech-to-text or speaker recognition  
- Environmental sound classification  
- Real-time or ultra–low-latency streaming inference  
- Non-musical audio domains  

---

## Bias, Risks, and Limitations

- **Label Noise:**  
  Labels are distilled from a teacher model. Although class-wise weighting is applied, subtle secondary moods may bleed into primary predictions.

- **Genre Bias:**  
  Performance may degrade on:
  - Purely instrumental tracks  
  - Rare regional folk styles underrepresented in the teacher corpus  

- **Temporal Assumption:**  
  Optimized for **≤30s chunks**; long-form compositions should be chunked.

---

## How to Use the Model

```python
from transformers import AutoModelForAudioClassification, AutoFeatureExtractor
import torch
import librosa

model_id = "beastLucifer/ostrich-v1-audio-mood"

model = AutoModelForAudioClassification.from_pretrained(model_id)
processor = AutoFeatureExtractor.from_pretrained(model_id)

# Load audio
audio, sr = librosa.load("your_song.wav", sr=16000)

inputs = processor(
    audio,
    sampling_rate=16000,
    return_tensors="pt"
)

# Inference
with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.sigmoid(logits)  # multi-label probabilities

# Map predictions
id2label = model.config.id2label
predictions = {
    id2label[i]: probs[0][i].item()
    for i in range(len(id2label))
}
````

---

## Training Details

### Training Data

* **Audio:** Large-scale Indian music corpus
* **Labels:** 31 mood dimensions generated via a CLAP-based teacher model

### Preprocessing

* Resampling: **16 kHz**
* Normalization: Zero-mean, unit-variance
* Chunking: Max **30 seconds** per sample

---

## Training Configuration

* **Optimizer:** `adamw_bnb_8bit`
* **Learning Rate:** `5e-5`
* **Batch Size:** 4 per device
* **Effective Batch Size:** 16 (gradient accumulation)
* **Precision:** FP16 mixed precision
* **Loss Function:** Custom **Weighted BCEWithLogitsLoss**
* **Special Handling:**

  * *Motivational* (index 19) weight reduced to **0.3** due to high teacher variance

---

## Architecture

* **Backbone:** DistilHuBERT
* **Objective:** Multi-label mood classification
* **Distillation:** Teacher–student training for compactness and speed
* **Inference:** ~90% of HuBERT performance at significantly reduced compute cost

---

## Compute Infrastructure

### Hardware

* NVIDIA Tesla T4 (Google Colab)

### Software

* PyTorch
* Hugging Face Transformers
* Accelerate
* BitsAndBytes (8-bit optimization)

---

## Label Inventory (31 Classes)

Energetic
Calm
Happy
Sad
Angry
Romantic
Mysterious
Nostalgic
Dard-bhari
Masti
Sufi-romantic
Item Song
Qawwali Vibes
Judaai
Tapori
Chill-lofi
Hype Party
Dreamy
Dark
Motivational
Melancholic
Intense
Peaceful
Experimental
Ambient
Spiritual
Groovy
Folk
Indie
Electronic
Classical

---

## Model Card Authors

**beastLucifer**
