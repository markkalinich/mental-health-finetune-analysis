---
base_model: microsoft/resnet-50
tags:
- image-classification
- ferplus
- emotions
---

# Fine-Tuned ResNet-50 on FERPlus Dataset

This model is a fine-tuned version of ResNet-50 on the [FERPlus dataset](https://www.kaggle.com/datasets/arnabkumarroy02/ferplus), which is more balanced ferplus dataset as owner claimed.

## Model Details
- **Base Model**: [Microsoft ResNet-50](https://huggingface.co/microsoft/resnet-50)
- **Dataset**: FERPlus, which contains grayscale images of faces labeled with emotion categories.
- **Task**: Emotion Classification
- **Labels**:
  - 0: Angry
  - 1: Contempt
  - 2: Disgust
  - 3: Fear
  - 4: Happy
  - 5: Neutral
  - 6: Sad
  - 7: Surprise

## Preprocessing Details
This model was fine-tuned on FERPlus dataset images resized to 224x224 pixels. Standard data augmentation techniques were applied, and normalization was performed with the following values:
- **Mean**: `[0.485, 0.456, 0.406]`
- **Standard Deviation**: `[0.229, 0.224, 0.225]`

### Training Hyperparameters
- **Batch Size**: 16
- **Epochs**: 10
- **Learning Rate**: 2e-5
- **Weight Decay**: 0.01