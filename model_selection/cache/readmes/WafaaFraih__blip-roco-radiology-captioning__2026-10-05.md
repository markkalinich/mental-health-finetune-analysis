---
language: en
license: mit
tags:
- medical
- radiology  
- image-captioning
- blip
- roco
datasets:
- eltorio/ROCOv2-radiology
library_name: transformers
pipeline_tag: image-to-text
---

# BLIP Fine-tuned for Radiology Image Captioning

This model is a fine-tuned version of BLIP on the ROCOv2 radiology dataset for generating captions of medical radiology images.

## Usage

```python
from transformers import BlipForConditionalGeneration, AutoProcessor
from PIL import Image

# Load model and processor
processor = AutoProcessor.from_pretrained("WafaaFraih/blip-roco-radiology-captioning")
model = BlipForConditionalGeneration.from_pretrained("WafaaFraih/blip-roco-radiology-captioning")

# Process image
image = Image.open("radiology_image.jpg")
inputs = processor(images=image, return_tensors="pt")

# Generate caption
generated_ids = model.generate(
    pixel_values=inputs["pixel_values"],
    max_new_tokens=64,
    num_beams=5,
    length_penalty=0.8
)

caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
print(caption)
```

## Model Details

- **Base Model**: Salesforce/blip-image-captioning-base
- **Dataset**: ROCOv2 Radiology  
- **Task**: Medical image captioning
- **Fine-tuning**: Full precision (FP32)
