---
license: apache-2.0
datasets:
- akahana/Driver-Drowsiness-Dataset
language:
- en
base_model:
- google/siglip2-base-patch16-224
pipeline_tag: image-classification
library_name: transformers
tags:
- SigLIP2
- Driver-Drowsiness-Detection
- biology
- chemistry
---

![2.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/yVIGKlu5LDDCbAHCOemKh.png)

# DOZE-GUARD-RLDD

> DOZE-GUARD-RLDD [Real-Time Distracted Driver Detection] is a vision-language encoder model fine-tuned from google/siglip2-base-patch16-224 for binary image classification. It is trained to detect whether a person in the image is drowsy or non-drowsy using the SiglipForImageClassification architecture.

> [!note]
> DOZE GUARD RLDD detection works best with crisp and high-quality images. Noisy images are not recommended for validation.

> [!note]
*SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features* https://arxiv.org/pdf/2502.14786

> [!note]
*Detection and Prediction of Driver Drowsiness for the Prevention of Road Accidents Using Deep Neural Networks Techniques* https://www.researchgate.net/publication/353397807_Detection_and_Prediction_of_Driver_Drowsiness_for_the_Prevention_of_Road_Accidents_Using_Deep_Neural_Networks_Techniques

```py
Classification Report:
              precision    recall  f1-score   support

      Drowsy     0.9818    0.9952    0.9885     17868
  Non Drowsy     0.9945    0.9788    0.9866     15566

    accuracy                         0.9876     33434
   macro avg     0.9881    0.9870    0.9875     33434
weighted avg     0.9877    0.9876    0.9876     33434
```

![download (1).png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/wW9HP_Ad5VBslP0FEG-Yq.png)


---

## Label Space: 2 Classes

The model classifies an image as either:

```
Class 0: Drowsy
Class 1: Non Drowsy
```

---

## Install Dependencies

```bash
pip install -q transformers torch pillow gradio hf_xet
```

---

## Inference Code

```python
import gradio as gr
from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch

# Load model and processor
model_name = "prithivMLmods/DOZE-GUARD-RLDD"  # Replace with your model path
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

# Label mapping
id2label = {
    "0": "Drowsy",
    "1": "Non Drowsy"
}

def classify_drowsiness(image):
    image = Image.fromarray(image).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()

    prediction = {
        id2label[str(i)]: round(probs[i], 3) for i in range(len(probs))
    }

    return prediction

# Gradio Interface
iface = gr.Interface(
    fn=classify_drowsiness,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Label(num_top_classes=2, label="Drowsiness Detection"),
    title="DOZE-GUARD-RLDD",
    description="Upload an image to classify whether the person is drowsy or non-drowsy."
)

if __name__ == "__main__":
    iface.launch()
```

---

## Demo Inference

![Screenshot 2025-05-14 at 19-20-23 DOZE-GUARD-RLDD.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/DbJ7FDMBoUtJqJwZUamuq.png)
![Screenshot 2025-05-14 at 19-05-19 DOZE-GUARD-RLDD.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/ddSxiC_PI_RNxY88_HNv4.png)
![Screenshot 2025-05-14 at 19-06-47 DOZE-GUARD-RLDD.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/nqKuxGZPysUPH5Jy87A2B.png)

## Intended Use

**DOZE-GUARD-RLDD** is useful in scenarios such as:

* **Driver Monitoring** – Detect drowsiness in drivers to prevent accidents.
* **Workplace Safety** – Monitor employee alertness to improve safety in high-risk environments.
* **Healthcare** – Assist in diagnosing conditions related to sleep deprivation or drowsiness.
* **Surveillance** – Real-time monitoring of individuals for drowsiness detection in critical areas.