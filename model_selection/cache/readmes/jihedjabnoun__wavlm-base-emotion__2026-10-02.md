---
language: en
license: mit
tags:
- audio
- speech-emotion-recognition
- wavlm
- emotion-classification
- pytorch
- transformers
datasets:
- MELD
- CREMA-D  
- TESS
- RAVDESS
- SAVEE
metrics:
- accuracy
- f1
model-index:
- name: wavlm-base-emotion-recognition
  results:
  - task:
      type: audio-classification
      name: Speech Emotion Recognition
    metrics:
    - type: accuracy
      name: Accuracy
      value: 0.303  # Your final accuracy
---

# Speech Emotion Recognition with WavLM-Base

This model is a fine-tuned version of `microsoft/wavlm-base` for speech emotion recognition. It can classify audio into 7 different emotions: Anger, Disgust, Fear, Happiness, Neutral, Sadness, and Surprise.

## Model Details

- **Model Type**: WavLM-Base for Sequence Classification
- **Base Model**: `microsoft/wavlm-base`
- **Parameters**: ~95M parameters
- **Language**: English
- **Task**: Multi-class emotion classification from speech audio
- **Final Training Accuracy**: 30.3%

## Training Data

The model was trained on a diverse multi-dataset collection totaling **18,687 training samples** and validated on **4,672 validation samples**:

- **MELD**: 8,906 samples
- **CREMA-D**: 5,950 samples
- **TESS**: 2,305 samples
- **RAVDESS**: 1,145 samples
- **SAVEE**: 381 samples

### Emotion Distribution (Training Set)
- **Neutral**: 5,659 samples (30.3%)
- **Happiness**: 3,063 samples (16.4%) 
- **Anger**: 2,548 samples (13.6%)
- **Sadness**: 2,173 samples (11.6%)
- **Fear**: 1,785 samples (9.6%)
- **Disgust**: 1,773 samples (9.5%)
- **Surprise**: 1,686 samples (9.0%)

### Speaker Diversity
- **Training**: 380 unique speakers
- **Validation**: 283 unique speakers
- **Top speakers**: Ross, Joey, Rachel, Phoebe (from MELD dataset)

## Usage

```python
from transformers import Wav2Vec2FeatureExtractor, Wav2Vec2ForSequenceClassification
import torch
import librosa

# Load model and feature extractor
model_name = "jihedjabnoun/wavlm-base-emotion"
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(model_name)
model = Wav2Vec2ForSequenceClassification.from_pretrained(model_name)

# Load and preprocess audio
audio_path = "path_to_your_audio.wav"
audio, sr = librosa.load(audio_path, sr=16000, mono=True)

# Extract features
inputs = feature_extractor(audio, sampling_rate=16000, return_tensors="pt", padding=True)

# Predict emotion
with torch.no_grad():
    logits = model(**inputs).logits
    predicted_id = torch.argmax(logits, dim=-1).item()
    
# Get emotion label
emotions = ['Anger', 'Disgust', 'Fear', 'Happiness', 'Neutral', 'Sadness', 'Surprise']
predicted_emotion = emotions[predicted_id]
print(f"Predicted emotion: {predicted_emotion}")

# Get confidence scores
probabilities = torch.softmax(logits, dim=-1)
confidence_scores = {emotion: prob.item() for emotion, prob in zip(emotions, probabilities[0])}
print(f"Confidence scores: {confidence_scores}")
```

## Training Procedure

### Training Hyperparameters
- **Epochs**: 5
- **Batch Size**: 4
- **Learning Rate**: 3e-5
- **Optimizer**: AdamW
- **Scheduler**: Linear with warmup
- **Mixed Precision**: FP16
- **Gradient Checkpointing**: Enabled for memory efficiency

### Data Preprocessing
- **Sampling Rate**: 16kHz
- **Audio Length**: Padded/truncated to 10 seconds maximum
- **Normalization**: Peak normalization applied
- **Feature Extraction**: Using Wav2Vec2FeatureExtractor

## Performance

The model was trained for 5 epochs and achieved a final accuracy of **30.3%** on the validation set. 

**Note**: The relatively low accuracy suggests the model may need:
- More training epochs
- Different hyperparameters
- Additional data preprocessing
- Class balancing techniques

## Training History

| Epoch | Training Loss | Validation Loss | Accuracy |
|-------|---------------|-----------------|----------|
| 1     | 1.875         | 1.848           | 30.29%   |
| 2     | 1.877         | 1.847           | 30.29%   |
| 3     | 1.799         | 1.848           | 30.29%   |
| 4     | 1.827         | 1.846           | 30.29%   |
| 5     | 1.877         | 1.846           | 30.29%   |

## Datasets Used

1. **MELD (Multimodal EmotionLines Dataset)**: Emotion recognition in conversations from TV series
2. **CREMA-D**: Crowdsourced Emotional Multimodal Actors Dataset  
3. **TESS**: Toronto Emotional Speech Set
4. **RAVDESS**: Ryerson Audio-Visual Database of Emotional Speech and Song
5. **SAVEE**: Surrey Audio-Visual Expressed Emotion Database

## Limitations

- Trained primarily on English speech
- Performance may vary on different accents or speaking styles not well represented in training data
- Audio quality and background noise can affect performance
- Model shows signs of potential overfitting (plateau in validation accuracy)
- May have bias towards neutral emotions due to class imbalance

## Recommendations for Improvement

1. **Longer Training**: Try training for more epochs with early stopping
2. **Learning Rate Scheduling**: Use cosine annealing or reduce LR on plateau
3. **Data Augmentation**: Add noise, speed perturbation, or pitch shifting
4. **Class Balancing**: Use weighted loss or oversampling techniques
5. **Regularization**: Add dropout or weight decay

## Ethical Considerations

This model should be used responsibly and not for:
- Unauthorized emotion detection or surveillance
- Making critical decisions about individuals without proper validation
- Applications that could harm user privacy or well-being

## Citation

If you use this model, please cite the original datasets and the base model:

```bibtex
@article{chen2022wavlm,
  title={WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing},
  author={Chen, Sanyuan and Wang, Chengyi and Chen, Zhengyang and Wu, Yu and Liu, Shujie and Chen, Zhuo and Li, Jinyu and Kanda, Naoyuki and Yoshioka, Takuya and Xiao, Xiong and others},
  journal={IEEE Journal of Selected Topics in Signal Processing},
  volume={16},
  number={6},
  pages={1505--1518},
  year={2022},
  publisher={IEEE}
}
```

## Model Card Authors

This model card was created as part of an emotion recognition research project.
