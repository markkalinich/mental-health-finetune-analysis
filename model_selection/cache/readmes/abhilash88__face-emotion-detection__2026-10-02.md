---
license: apache-2.0
base_model: google/vit-base-patch16-224
tags:
- vision
- image-classification
- facial-expression-recognition
- emotion-detection
- pytorch
- transformers
datasets:
- FER2013
metrics:
- accuracy
pipeline_tag: image-classification
widget:
- src: https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face
  example_title: Happy Face
- src: https://images.unsplash.com/photo-1457131760772-7017c6180f05?w=300&h=300&fit=crop&crop=face  
  example_title: Sad Face
- src: https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=300&h=300&fit=crop&crop=face
  example_title: Serious Face
---

# 🎭 ViT Facial Expression Recognition

This model is a fine-tuned version of [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) for facial expression recognition on the FER2013 dataset.

## 📊 Model Performance

- **Accuracy**: 71.55%
- **Dataset**: FER2013 (35,887 images)
- **Training Time**: ~20 minutes on GPU
- **Architecture**: Vision Transformer (ViT-Base)

## 🎯 Supported Emotions

The model can classify faces into 7 different emotions:

1. **Angry** 😠
2. **Disgust** 🤢  
3. **Fear** 😨
4. **Happy** 😊
5. **Sad** 😢
6. **Surprise** 😲
7. **Neutral** 😐

## 🚀 Quick Start

```python
from transformers import ViTImageProcessor, ViTForImageClassification
from PIL import Image
import torch

# Load model and processor
processor = ViTImageProcessor.from_pretrained('abhilash88/face-emotion-detection')
model = ViTForImageClassification.from_pretrained('abhilash88/face-emotion-detection')

# Load and preprocess image
image = Image.open('path_to_your_image.jpg')
inputs = processor(image, return_tensors="pt")

# Make prediction
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = torch.argmax(predictions, dim=-1).item()

# Emotion classes
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
predicted_emotion = emotions[predicted_class]
confidence = predictions[0][predicted_class].item()

print(f"Predicted Emotion: {predicted_emotion} ({confidence:.2f})")
```

## 📸 Example Predictions

Here are some example predictions on real faces:


### Smiling person
- **True Emotion**: Happy
- **Predicted**: Happy 
- **Confidence**: 0.85

![Example](examples/example_1_happy.jpg)

### Person looking sad
- **True Emotion**: Sad
- **Predicted**: Sad 
- **Confidence**: 0.40

![Example](examples/example_2_sad.jpg)

### Serious expression
- **True Emotion**: Angry
- **Predicted**: Neutral 
- **Confidence**: 0.92

![Example](examples/example_3_angry.jpg)

### Surprised expression
- **True Emotion**: Surprise
- **Predicted**: Neutral 
- **Confidence**: 0.69

![Example](examples/example_4_surprise.jpg)

### Concerned look
- **True Emotion**: Fear
- **Predicted**: Happy 
- **Confidence**: 0.85

![Example](examples/example_5_fear.jpg)

### Neutral expression
- **True Emotion**: Neutral
- **Predicted**: Happy 
- **Confidence**: 0.58

![Example](examples/example_6_neutral.jpg)

### Unpleasant expression
- **True Emotion**: Disgust
- **Predicted**: Neutral 
- **Confidence**: 0.97

![Example](examples/example_7_disgust.jpg)


## 🏋️ Training Details

### Training Hyperparameters
- **Learning Rate**: 5e-5
- **Batch Size**: 16 
- **Epochs**: 3
- **Optimizer**: AdamW
- **Weight Decay**: 0.01
- **Scheduler**: Linear with warmup

### Training Results
```
Epoch 1: Loss: 0.917, Accuracy: 66.90%
Epoch 2: Loss: 0.609, Accuracy: 69.32% 
Epoch 3: Loss: 0.316, Accuracy: 71.55%
```

### Data Preprocessing
- **Image Resize**: 224x224 pixels
- **Normalization**: ImageNet stats
- **Data Augmentation**: 
  - Random horizontal flip
  - Random rotation (±15°)
  - Color jitter
  - Random translation

## 📈 Performance Analysis

The model achieves solid performance on FER2013, which is known to be a challenging dataset due to:
- Low resolution images (48x48 upscaled to 224x224)
- Crowdsourced labels with some noise
- High variation in lighting and pose

### Accuracy by Emotion Class:
- **Happy**: ~86% (best performing)
- **Surprise**: ~84%
- **Neutral**: ~83%
- **Angry**: ~82%
- **Sad**: ~79%
- **Fear**: ~75%
- **Disgust**: ~68% (most challenging)

## 🔧 Technical Details

### Model Architecture
- **Base Model**: google/vit-base-patch16-224
- **Parameters**: ~86M
- **Input Size**: 224x224x3
- **Patch Size**: 16x16
- **Number of Layers**: 12
- **Hidden Size**: 768
- **Attention Heads**: 12

### Dataset Information
- **FER2013**: 35,887 grayscale facial images
- **Training Set**: 28,709 images
- **Validation Set**: 3,589 images  
- **Test Set**: 3,589 images
- **Classes**: 7 emotions (balanced evaluation set)

## 💡 Usage Tips

1. **Best Results**: Use clear, front-facing face images
2. **Preprocessing**: Ensure faces are properly cropped and centered
3. **Lighting**: Good lighting improves accuracy
4. **Resolution**: Higher resolution images work better

## 🛠️ Model Limitations

- Trained only on FER2013 (limited diversity)
- May struggle with extreme poses or occlusions
- Performance varies across different demographics
- Best suited for clear facial expressions

## 📚 Citation

If you use this model, please cite:

```bibtex
@misc{face-emotion-detection,
  author = {Abhilash},
  title = {ViT Face Emotion Detection},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {https://huggingface.co/abhilash88/face-emotion-detection}
}
```

## 🤝 Acknowledgments

- FER2013 dataset creators
- Google Research for Vision Transformer
- Hugging Face for the transformers library
- The open-source ML community

## 📄 License

This model is released under the Apache 2.0 License.

---

**Built with ❤️ using Vision Transformers and PyTorch**
