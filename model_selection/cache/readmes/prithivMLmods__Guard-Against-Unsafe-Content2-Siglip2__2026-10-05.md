---
license: apache-2.0
base_model:
- prithivMLmods/Guard-Against-Unsafe-Content-Siglip2
pipeline_tag: image-classification
library_name: transformers
tags:
- siglip2
- nsfw-filter
language:
- en
---
![11.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/84Z_eydm-a5iARLkRmAjH.png)

# **Guard-Against-Unsafe-Content2-Siglip2**  

> **Guard-Against-Unsafe-Content2-Siglip2** is an image classification vision-language encoder model fine-tuned from **google/siglip2-base-patch16-224** for a binary classification task. It is designed to classify images as either **"normal"** or **"nsfw"** using the **SiglipForImageClassification** architecture.

> [!WARNING]
> Experimental: This NSFW filter is an experimental model. Since I haven't found a better dataset to improve it, its performance may be inconsistent in some cases. I am currently looking for a better open dataset to enhance its effectiveness in a multi-label classification problem.

```py
Classification Report:
              precision    recall  f1-score   support

      normal     0.9975    0.9988    0.9981      4000
        nsfw     0.9992    0.9983    0.9987      6000

    accuracy                         0.9985     10000
   macro avg     0.9983    0.9985    0.9984     10000
weighted avg     0.9985    0.9985    0.9985     10000
```

![output.png](https://cdn-uploads.huggingface.co/production/uploads/65bb837dbfb878f46c77de4c/5lZQcFfc1pAKHweYHD9h4.png)

The model categorizes images into 2 classes:  

- **Class 0:** "normal"  
- **Class 1:** "nsfw"  

# **Run with Transformers🤗**  

```python
!pip install -q transformers torch pillow gradio
```  

```python
import gradio as gr
from transformers import AutoImageProcessor
from transformers import SiglipForImageClassification
from transformers.image_utils import load_image
from PIL import Image
import torch

# Load model and processor
model_name = "prithivMLmods/Guard-Against-Unsafe-Content2-Siglip2"
model = SiglipForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)

def nsfw_classification(image):
    """Predicts whether an image is NSFW or normal."""
    image = Image.fromarray(image).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1).squeeze().tolist()
    
    labels = {
        "0": "normal", 
        "1": "nsfw"
    }
    predictions = {labels[str(i)]: round(probs[i], 3) for i in range(len(probs))}
    
    return predictions

# Create Gradio interface
iface = gr.Interface(
    fn=nsfw_classification,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Label(label="Prediction Scores"),
    title="NSFW Image Classification",
    description="Upload an image to classify whether it is normal or NSFW."
)

# Launch the app
if __name__ == "__main__":
    iface.launch()
```

# **Intended Use:**  

The **Guard-Against-Unsafe-Content2-Siglip2** model is designed to classify images as either **"normal"** or **"nsfw"**. Potential use cases include:  

- **Content Moderation:** Automatically filtering explicit images on social media, forums, and messaging apps.  
- **Parental Control:** Ensuring children are not exposed to inappropriate content.  
- **Image Search Filtering:** Improving search engine safety by removing NSFW images.  
- **Automated Image Analysis:** Enhancing AI-driven applications that require content safety monitoring.