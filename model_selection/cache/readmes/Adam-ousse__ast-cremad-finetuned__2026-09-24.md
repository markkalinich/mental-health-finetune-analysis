---
library_name: transformers
pipeline_tag: audio-classification
tags:
  - audio-classification
  - audio
  - ast
  - cremad
  - emotion-recognition
datasets:
  - MahiA/CREMA-D
base_model: MIT/ast-finetuned-audioset-10-10-0.4593
---

# AST fine-tuned on CREMA-D

This model is an ASTForAudioClassification checkpoint fine-tuned from:

- MIT/ast-finetuned-audioset-10-10-0.4593

## Dataset

- Dataset: MahiA/CREMA-D
- Classes: anger, disgust, fear, happy, neutral, sad
- Split protocol:
  - official train.csv was split into train and validation
  - validation was stratified 10% of official train
  - official test.csv was used as test

## Training notes

- Loss: class-weighted cross-entropy to account for class imbalance

## Validation result

- Best epoch: 17
- Best validation accuracy: 0.662751677852349

## Test result

- Split: test
- Samples: 1489
- Loss: 1.767368
- Accuracy: 0.70047

### Per-class accuracy

- anger: 0.7280 (174/239)
- disgust: 0.3520 (44/125)
- fear: 0.4529 (77/170)
- happy: 0.4474 (34/76)
- neutral: 0.8608 (699/812)
- sad: 0.2239 (15/67)

## Usage

```python
import torch
from transformers import AutoFeatureExtractor, ASTForAudioClassification

model_id = "Adam-ousse/ast-cremad-finetuned"
feature_extractor = AutoFeatureExtractor.from_pretrained(model_id)
model = ASTForAudioClassification.from_pretrained(model_id)
model.eval()

# waveform: 1D float32 numpy array at 16 kHz
# inputs = feature_extractor([waveform], sampling_rate=16000, return_tensors="pt", padding=True)
# with torch.no_grad():
#     logits = model(**inputs).logits
#     pred = int(torch.argmax(logits, dim=1)[0])
```

## Labels

The model config includes:

- id2label: {0: anger, 1: disgust, 2: fear, 3: happy, 4: neutral, 5: sad}
- label2id: {anger: 0, disgust: 1, fear: 2, happy: 3, neutral: 4, sad: 5}
