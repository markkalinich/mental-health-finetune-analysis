---
library_name: transformers
license: apache-2.0
tags:
  - image-classification
  - emotion-recognition
  - facial-expression-recognition
  - vit
  - pytorch
datasets:
  - abhilash88/fer2013-enhanced
metrics:
  - accuracy
  - f1
pipeline_tag: image-classification
---

# Facial Emotion Recognition (ViT, fine-tuned on FER2013)

Fine-tuned `google/vit-base-patch16-224-in21k` for 7-class facial emotion recognition,
with class-weighted + label-smoothed loss to handle FER2013's class imbalance
(disgust is heavily underrepresented) and data augmentation (flip/rotation/jitter).

## Classes
angry, disgust, fear, happy, sad, surprise, neutral

## Test set results
- Accuracy: 0.7082
- Macro F1: 0.6784

## ⚠️ Important: input format required

This model was trained on **FER2013**, which consists of **tightly cropped,
grayscale, 48x48 face images**. Feeding it a full, uncropped, color photo
(e.g. straight from your phone or the internet) will give poor, low-confidence
results, because that input looks nothing like what the model saw during training.

**For good results, always crop to the face and convert to grayscale before
running inference.** The example below does this automatically using a face
detector.

## Usage (Google Colab)

`facenet-pytorch` pins an old `numpy<2.0` / `pillow` combo that no longer has
prebuilt wheels on current Colab runtimes, which causes a source-build error.
Installing with `--no-deps` avoids re-resolving those pins and uses the
numpy/pillow/torch already present in Colab:

```python
%pip install facenet-pytorch --no-deps
%pip install requests torchvision --no-deps
```

**Restart the session** after installing (Runtime → Restart session in the
Colab menu), then run:

```python
import torch
import numpy as np
from PIL import Image
from facenet_pytorch import MTCNN
from transformers import AutoImageProcessor, AutoModelForImageClassification

processor = AutoImageProcessor.from_pretrained("bsgcasa/emotion-vit-model")
model = AutoModelForImageClassification.from_pretrained("bsgcasa/emotion-vit-model")
model.eval()

mtcnn = MTCNN(keep_all=False)

def predict_emotion(image_path):
    img = Image.open(image_path).convert("RGB")

    box, _ = mtcnn.detect(img)
    if box is None:
        print("No face detected.")
        return None

    x1, y1, x2, y2 = [int(v) for v in box[0]]
    face_crop = img.crop((x1, y1, x2, y2)).convert("L")  # grayscale, matches training

    face_rgb = Image.fromarray(np.stack([np.array(face_crop)] * 3, axis=-1).astype(np.uint8))

    inputs = processor(images=face_rgb, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits

    probs = torch.softmax(logits, dim=-1)[0]
    predicted_id = probs.argmax().item()

    print(f"Predicted: {model.config.id2label[predicted_id]}")
    for i, p in enumerate(probs):
        print(f"  {model.config.id2label[i]:>10}: {p:.3f}")

    return model.config.id2label[predicted_id]

predict_emotion("your_face_image.jpg")  # upload a photo to Colab and update this path
```

### Troubleshooting
- **`ModuleNotFoundError: No module named 'facenet_pytorch'`** — the install
  cell either didn't run or silently failed. Use `%pip` (not `!pip`), check
  the cell's output for errors, and restart the session after installing.
- **Build error on `numpy`/`pillow`** — this is the version-pin issue described
  above; use `--no-deps` as shown.
- **`your_face_image.jpg` not found** — upload an image to the Colab file
  browser (folder icon on the left) and update the path, or use
  `from google.colab import files; files.upload()` to upload interactively.

## Notes
- Trained with class-weighted + label-smoothed cross-entropy loss.
- Data augmentation applied during training (horizontal flip, rotation, color jitter).
- **Face detection + grayscale conversion is required at inference time** — the
  saved image processor only handles resizing/normalization, not face cropping.
  Using the model on full, uncropped, color photos will produce unreliable results.