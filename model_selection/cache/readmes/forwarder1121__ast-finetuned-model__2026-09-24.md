---
language:
  - en
datasets:
  - CREMA-D
library_name: transformers
tags:
  - emotion-classification
  - audio-classification
  - audio-spectrogram
  - transformer
  - fine-tuned
license: apache-2.0
pipeline_tag: audio-classification
base_model: "MIT/ast-finetuned-audioset-10-10-0.4593"
metrics:
  - accuracy
  - f1
task_categories:
  - audio-classification
---


# AST Fine-Tuned Model for Emotion Classification


# **AST Fine-Tuned Model for Emotion Classification**

This is a fine-tuned Audio Spectrogram Transformer (AST) model, specifically designed for classifying emotions in speech audio. The model was fine-tuned on the **CREMA-D dataset**, focusing on six emotional categories. The base model was sourced from **MIT's pre-trained AST model**.

---

## **Model Details**
- **Base Model**: `MIT/ast-finetuned-audioset-10-10-0.4593`
- **Fine-Tuned Dataset**: CREMA-D
- **Architecture**: Audio Spectrogram Transformer (AST)
- **Model Type**: Single-label classification
- **Input Features**: Log-Mel Spectrograms (128 mel bins)
- **Output Classes**:
  - **ANG**: Anger
  - **DIS**: Disgust
  - **FEA**: Fear
  - **HAP**: Happiness
  - **NEU**: Neutral
  - **SAD**: Sadness

---

## **Model Configuration**
- **Hidden Size**: 768
- **Number of Attention Heads**: 12
- **Number of Hidden Layers**: 12
- **Patch Size**: 16
- **Maximum Length**: 1024
- **Dropout Probability**: 0.0
- **Activation Function**: GELU (Gaussian Error Linear Unit)
- **Optimizer**: Adam
- **Learning Rate**: 1e-4

---

## **Training Details**
- **Dataset**: CREMA-D (Emotion-Labeled Speech Data)
- **Data Augmentation**:
  - Noise injection
  - Time shifting
  - Speed perturbation
- **Fine-Tuning Epochs**: 5
- **Batch Size**: 16
- **Learning Rate Scheduler**: Linear decay
- **Best Validation Accuracy**: 60.71%
- **Best Checkpoint**: `./results/checkpoint-1119`

---

## **How to Use**

### **Load the Model**
```python
from transformers import AutoModelForAudioClassification, AutoProcessor

# Load the model and processor
model = AutoModelForAudioClassification.from_pretrained("forwarder1121/ast-finetuned-model")
processor = AutoProcessor.from_pretrained("forwarder1121/ast-finetuned-model")

# Prepare input audio (e.g., waveform) as log-mel spectrogram
inputs = processor("path_to_audio.wav", sampling_rate=16000, return_tensors="pt")

# Make predictions
outputs = model(**inputs)
predicted_class = outputs.logits.argmax(-1).item()

print(f"Predicted emotion: {model.config.id2label[str(predicted_class)]}")
```

---

## **Metrics**

### **Validation Results**
- **Best Validation Accuracy**: 60.71%
- **Validation Loss**: 1.1126

### **Evaluation Details**
- **Eval Dataset**: CREMA-D test split
- **Batch Size**: 16
- **Number of Steps**: 94

---

## **Limitations**
- The model was trained on CREMA-D, which has a specific set of speech data. It may not generalize well to datasets with different accents, speech styles, or languages.
- Validation accuracy is 60.71%, indicating room for improvement for real-world deployment.

---

## **Acknowledgments**
This work is based on the **Audio Spectrogram Transformer (AST)** model by MIT, fine-tuned for emotion classification. Special thanks to the developers of Hugging Face and the CREMA-D dataset contributors.

---

## **License**
The model is shared under the MIT License. Refer to the licensing details in the repository.

---

## **Citation**
If you use this model in your work, please cite:
```
@misc{ast-finetuned-model,
  author = {forwarder1121},
  title = {Fine-Tuned Audio Spectrogram Transformer for Emotion Classification},
  year = {2024},
  url = {https://huggingface.co/forwarder1121/ast-finetuned-model},
}
```

---

## **Contact**
For questions, reach out to `forwarder1121@naver.com`.