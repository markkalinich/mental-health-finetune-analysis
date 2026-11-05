---
license: apache-2.0
base_model:
- google/siglip2-base-patch16-224
language:
- en
pipeline_tag: image-classification
library_name: transformers
tags:
- text-generation-inference
- siglip2
- image-filter
- safe-image-moderation
- adult-content-filter
- content-safety
- anime-detection
- ai-safety
---

# **Image-Guard-ckpt-3312**

> **Image-Guard-ckpt-3312** is a **multiclass image safety classification model** fine-tuned from **google/siglip2-base-patch16-224**.
> This checkpoint is provided for **experimental purposes**. For production or actual usage, please refer to the final released models.
> It classifies images into multiple safety-related categories using the **SiglipForImageClassification** architecture.



```py
Model Evaluation:
                     precision    recall  f1-score   support

          Anime-SFW     0.8696    0.8718    0.8707      5600
             Hentai     0.9057    0.8567    0.8805      4180
         Normal-SFW     0.8865    0.8726    0.8795      5503
        Pornography     0.9451    0.9230    0.9340      5600
Enticing or Sensual     0.8705    0.9371    0.9026      5600

           accuracy                         0.8942     26483
          macro avg     0.8955    0.8923    0.8934     26483
       weighted avg     0.8950    0.8942    0.8942     26483
```

![4e](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/ex1AtmwRq0g1UVj4bYOXN.png)

## **Label Space: 5 Classes**

| Class ID | Label               | Description                                                               |
| -------- | ------------------- | ------------------------------------------------------------------------- |
| **0**    | Anime-SFW           | Safe-for-work anime-style images.                                         |
| **1**    | Hentai              | Explicit or adult anime content.                                          |
| **2**    | Normal-SFW          | Realistic or photographic images that are safe for work.                  |
| **3**    | Pornography         | Explicit adult content involving nudity or sexual acts.                   |
| **4**    | Enticing or Sensual | Suggestive imagery that is not explicit but intended to evoke sensuality. |

---

## **Install Dependencies**

```bash
pip install -q transformers torch pillow gradio
```

## **Inference Code**

```python
import gradio as gr
from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch

# Load model and processor
model_name = "prithivMLmods/Image-Guard-ckpt-3312"
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

# Label mapping
id2label = {
    "0": "Anime-SFW",
    "1": "Hentai",
    "2": "Normal-SFW",
    "3": "Pornography",
    "4": "Enticing or Sensual"
}

def classify_image_safety(image):
    image = Image.fromarray(image).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()

    prediction = {id2label[str(i)]: round(probs[i], 3) for i in range(len(probs))}
    return prediction

# Gradio Interface
iface = gr.Interface(
    fn=classify_image_safety,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Label(num_top_classes=5, label="Image Safety Classification"),
    title="Image-Guard-ckpt-3312",
    description="Upload an image to classify it into one of five safety categories: Anime-SFW, Hentai, Normal-SFW, Pornography, or Enticing/Sensual."
)

if __name__ == "__main__":
    iface.launch()
```

## **Intended Use**

**Image-Guard-ckpt-3312** is designed for:

* **Content Moderation** – Identify and filter sensitive or NSFW imagery.
* **Dataset Curation** – Separate clean and explicit data for research and training.
* **Platform Safety** – Support compliance for social, educational, and media-sharing platforms.
* **AI Model Input Filtering** – Prevent unsafe data from entering multimodal or generative pipelines.

> **Note:** This checkpoint is experimental. For production-grade usage, use the final verified model versions.

## **Limitations**

* The model may misclassify borderline or artistically abstract images.
* It does not perform face recognition or identify individuals.
* Performance depends on lighting, resolution, and visual context.
* Human moderation is still recommended for sensitive content.