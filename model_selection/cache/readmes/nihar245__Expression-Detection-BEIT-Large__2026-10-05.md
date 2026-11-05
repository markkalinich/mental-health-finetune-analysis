---
language: en
license: mit
tags:
- vision
- image-classification
- emotion-recognition
- student-engagement
- education
- beit
- pytorch
- transformers
datasets:
- custom
metrics:
- accuracy
- f1
base_model: microsoft/beit-base-patch16-224-pt22k-ft22k
widget:
- src: https://huggingface.co/spaces/scikit-learn/model-cards/resolve/main/assets/faces.jpg
  example_title: Sample Face
---

# Student Engagement Detection - BEiT Fine-tuned Model

<div align="center">

![Model](https://img.shields.io/badge/Model-BEiT--Large-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Framework](https://img.shields.io/badge/Framework-PyTorch-red)
![Accuracy](https://img.shields.io/badge/Accuracy-94.2%25-brightgreen)

**Real-time student engagement detection for online education**

[GitHub Repository](https://github.com/nihar245/Student-Engagement-Detection) • [Demo](https://github.com/nihar245/Student-Engagement-Detection#usage) • [Paper](#citation)

</div>

---

## 📋 Model Description

This model is a fine-tuned version of [microsoft/beit-base-patch16-224-pt22k-ft22k](https://huggingface.co/microsoft/beit-base-patch16-224-pt22k-ft22k) specifically designed for **student engagement detection in online classrooms**. 

The model classifies facial expressions into **4 engagement states**:
- 😴 **Bored** - Student shows disinterest or fatigue
- 🤔 **Confused** - Student appears uncertain or needs help
- ✨ **Engaged** - Student actively participates and focuses
- 😐 **Neutral** - Baseline emotional state

### 🎯 Key Features

- ✅ **Two-Stage Transfer Learning**: Built upon emotion-recognition pre-training (FER2013/RAF-DB/AffectNet by [Tanneru](https://huggingface.co/Tanneru))
- ✅ **High Accuracy**: 94.2% accuracy with only 150 samples per class
- ✅ **Lightweight**: Fast inference (~45ms per face on GPU)
- ✅ **Production-Ready**: Integrated with MTCNN face detection and Grad-CAM explainability
- ✅ **Privacy-Focused**: Works with screen capture without storing facial data

---

## 🚀 Intended Uses

### Primary Use Cases
- **Online Education Platforms**: Monitor student engagement in Zoom/Google Meet
- **E-Learning Analytics**: Track attention patterns in MOOCs
- **Virtual Classroom Management**: Real-time feedback for instructors
- **Educational Research**: Study engagement dynamics in remote learning

### Out-of-Scope Use
- ❌ General emotion recognition (use base FER models instead)
- ❌ Security/surveillance applications
- ❌ Clinical mental health diagnosis
- ❌ Employment/hiring decisions

---

## 📊 Training Data

### Dataset Composition
- **Total Samples**: 600 images (150 per class after augmentation)
- **Original Size**: ~50 images per class (custom webcam captures)
- **Classes**: Bored, Confused, Engaged, Neutral
- **Resolution**: 224×224 pixels
- **Data Source**: Custom dataset captured with consent from students

### Data Augmentation
```python
transforms.Compose([
    transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3),
    transforms.RandomRotation(10),
])
```

### Training Configuration
- **Base Model**: BEiT-Base (86M parameters)
- **Fine-tuning Epochs**: 7
- **Batch Size**: 8
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW with weight decay 0.01
- **Hardware**: Google Colab (Tesla T4 GPU)

---

## 📈 Performance Metrics

### Overall Performance
| Metric | Value |
|--------|-------|
| **Training Accuracy** | 94.2% |
| **Validation F1-Score** | 0.91 (weighted) |
| **Inference Time (GPU)** | ~45ms per face |
| **Inference Time (CPU)** | ~180ms per face |

### Per-Class Metrics
| Engagement State | Precision | Recall | F1-Score | Support |
|------------------|-----------|--------|----------|---------|
| Bored | 0.89 | 0.92 | 0.90 | 38 |
| Confused | 0.87 | 0.85 | 0.86 | 35 |
| Engaged | 0.95 | 0.93 | 0.94 | 42 |
| Neutral | 0.92 | 0.94 | 0.93 | 40 |

---

## 🔧 How to Use

### Quick Start

```python
from transformers import BeitForImageClassification, AutoImageProcessor
from PIL import Image
import torch

# Load model and processor
model = BeitForImageClassification.from_pretrained("nihar245/student-engagement-beit")
processor = AutoImageProcessor.from_pretrained("nihar245/student-engagement-beit")

# Prepare image
image = Image.open("student_face.jpg").convert("RGB")
inputs = processor(images=image, return_tensors="pt")

# Inference
with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    pred_class = torch.argmax(probs, dim=-1).item()

# Get prediction
labels = ["Bored", "Confused", "Engaged", "Neutral"]
print(f"Prediction: {labels[pred_class]} ({probs[0][pred_class]:.2%} confidence)")
```

### Integration with Face Detection

```python
from facenet_pytorch import MTCNN
import cv2

# Initialize face detector
mtcnn = MTCNN(keep_all=True, device='cuda')

# Detect faces
frame = cv2.imread("classroom.jpg")
boxes, _ = mtcnn.detect(frame)

# Process each face
for box in boxes:
    x1, y1, x2, y2 = [int(b) for b in box]
    face = frame[y1:y2, x1:x2]
    
    # Convert to PIL and predict
    face_pil = Image.fromarray(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
    inputs = processor(images=face_pil, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)
        pred = torch.argmax(outputs.logits, dim=-1).item()
    
    print(f"Face at {box}: {labels[pred]}")
```

### Real-Time Webcam Detection

```python
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect faces
    boxes, _ = mtcnn.detect(frame)
    
    if boxes is not None:
        for box in boxes:
            x1, y1, x2, y2 = [int(b) for b in box]
            face = frame[y1:y2, x1:x2]
            
            # Predict engagement
            face_pil = Image.fromarray(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
            inputs = processor(images=face_pil, return_tensors="pt")
            
            with torch.no_grad():
                outputs = model(**inputs)
                pred = torch.argmax(outputs.logits, dim=-1).item()
            
            # Draw results
            color = (0, 255, 0) if labels[pred] == "Engaged" else (0, 165, 255)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, labels[pred], (x1, y1-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    cv2.imshow('Engagement Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## ⚠️ Limitations and Biases

### Known Limitations
- **Limited Diversity**: Trained on small custom dataset (~10 individuals)
- **Lighting Sensitivity**: Performance degrades in poor lighting conditions
- **Pose Variations**: Best results with frontal faces (±30° rotation)
- **Age Bias**: Primarily trained on young adults (18-25 years)
- **Cultural Context**: May not generalize to all cultural expressions of engagement

### Potential Biases
- **Gender**: Balanced dataset but may show slight gender bias
- **Ethnicity**: Limited ethnic diversity in training data
- **Context**: Optimized for webcam/classroom settings, not general scenarios

### Recommendations
- Use ensemble with other engagement metrics (audio, gaze tracking)
- Calibrate thresholds per classroom/cultural context
- Regular retraining with diverse data
- Human-in-the-loop for high-stakes decisions

---

## 🛡️ Ethical Considerations

### Privacy
- Model processes images locally without cloud transmission
- No facial recognition/identification capability
- Designed for aggregate analytics, not individual surveillance

### Transparency
- Grad-CAM visualizations show decision-making process
- Confidence scores provided with each prediction
- Open-source implementation for auditing

### Fairness
- Regular bias audits recommended
- Should not be sole factor in student evaluation
- Provides supportive feedback, not punitive measures

---

## 📚 Training Procedure

### Fine-Tuning Process

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=7,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics,
)

trainer.train()
```

### Hardware Requirements
- **Minimum**: 6GB GPU VRAM (GTX 1060 or equivalent)
- **Recommended**: 12GB GPU VRAM (RTX 3060 or better)
- **Training Time**: ~20 minutes on Tesla T4 (Google Colab)

---

## 🔗 Framework Versions

- **Transformers**: 4.44.2
- **PyTorch**: 2.4.1+cu121
- **Python**: 3.11
- **CUDA**: 11.8+

---

## 📖 Citation

If you use this model in your research, please cite:

```bibtex
@misc{mehta2025studentengagement,
  author = {Nihar Mehta},
  title = {Student Engagement Detection using BEiT Vision Transformer},
  year = {2025},
  publisher = {HuggingFace},
  howpublished = {\url{https://huggingface.co/nihar245/student-engagement-beit}},
  note = {Fine-tuned from microsoft/beit-base-patch16-224-pt22k-ft22k}
}
```

### Acknowledgments
- **Base Model**: [Microsoft BEiT](https://huggingface.co/microsoft/beit-base-patch16-224-pt22k-ft22k)
- **Emotion Pre-training**: [Tanneru's FER Models](https://huggingface.co/Tanneru)
- **Face Detection**: [facenet-pytorch](https://github.com/timesler/facenet-pytorch)

---

## 📧 Contact & Support

- **GitHub**: [@nihar245](https://github.com/nihar245)
- **Repository**: [Student-Engagement-Detection](https://github.com/nihar245/Student-Engagement-Detection)
- **Issues**: [GitHub Issues](https://github.com/nihar245/Student-Engagement-Detection/issues)

---

## 📄 License

This model is released under the [MIT License](https://opensource.org/licenses/MIT).

```
MIT License

Copyright (c) 2025 Nihar Mehta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**⭐ Star the [GitHub repo](https://github.com/nihar245/Student-Engagement-Detection) if you find this useful!**

Made with ❤️ for improving online education

</div>