---
license: other
license_name: lg
license_link: LICENSE
datasets:
- LaurenGurgiolo/Music_by_Emotion
language:
- en
metrics:
- accuracy
  
base_model:
- MIT/ast-finetuned-audioset-10-10-0.4593
library_name: transformers
tags:
- music
- classifycation
- emotion
---
"🎵 Music Emotion Classification Model

This repository hosts a music emotion classification model fine-tuned from MIT/ast-finetuned-audioset-10-10-0.4593 using an iterative training and data augmentation strategy.

The model predicts emotional labels from 30-second music audio clips.

📌 Model Overview

Base model: MIT/ast-finetuned-audioset-10-10-0.4593

Task: Music Emotion Classification

Input: 30-second audio clips

Output: Emotion class labels

Framework: PyTorch / Hugging Face Transformers

📂 Dataset

The model was trained on the Music by Emotion dataset available on Hugging Face.

Source: SoundCloud

Size: 1,000 audio samples

Duration: 30 seconds per sample

Labels: Emotion categories

Split: Train / Validation / Test

🧠 Training Process

Initial Fine-Tuning

The base Audio Spectrogram Transformer (AST) model was fine-tuned on the original dataset.

Initial performance achieved approximately 40% accuracy.

Iterative Training & Data Augmentation

The dataset was augmented to improve robustness and generalization.

The fine-tuned model was trained iteratively on the augmented data.

This significantly improved performance across all classes.

📊 Performance

Final Test Accuracy: 99%

Evaluation Metric: Classification Accuracy

Inference Speed: Optimized for real-time or batch audio classification

Note: The high accuracy reflects performance on the augmented dataset and test split.

🚀 Usage
from transformers import AutoProcessor, AutoModelForAudioClassification
import torch

processor = AutoProcessor.from_pretrained("your-username/your-model-name")
model = AutoModelForAudioClassification.from_pretrained("your-username/your-model-name")

inputs = processor("audio.wav", return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

predicted_class = outputs.logits.argmax(dim=-1)

⚠️ Limitations

The model is trained on 30-second music clips and may not generalize well to:

Very short audio samples

Non-music audio (speech, noise, environmental sounds)

Emotion labels are subjective and dataset-dependent.

📜 License

Please refer to the original dataset and base model licenses:

Base Model: MIT/AST License

Dataset: Music by Emotion dataset license on Hugging Face

🙌 Acknowledgements

MIT CSAIL for the AST architecture

Hugging Face for model hosting and tooling

SoundCloud contributors for the audio data"
![image](https://cdn-uploads.huggingface.co/production/uploads/6744d44d6b525500a8cdb8c3/ByzEvchr75N7vpW6i8Izr.png)
