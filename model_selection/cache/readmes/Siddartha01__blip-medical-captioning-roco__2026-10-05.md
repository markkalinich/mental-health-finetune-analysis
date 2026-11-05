---
library_name: transformers
tags:
- medical
- radiology
- image-captioning
- blip
- vision-language
---

# Medical Report Generator (BLIP fine-tuned on ROCO)

Fine-tuned BLIP model for generating radiology reports from medical images, developed as part of a capstone project in medical image analysis.

This model generates descriptive captions for radiology images (e.g., X-rays, CT scans) using the Salesforce/blip-image-captioning-base as the base model, fine-tuned on the eltorio/ROCOv2-radiology dataset.

## Model Details

### Model Description
Developed by a Computer Science student focusing on ML for medical imaging.  
Funded by: optional (e.g., academic project).  
Shared by: Siddartha01.  
Model type: BLIP (vision-language).  
Languages: English (NLP for captions).  
License: apache-2.0 (or specify your choice).  
Finetuned from model: Salesforce/blip-image-captioning-base.

### Model Sources
- Repository: https://huggingface.co/Siddartha01/blip-medical-captioning-roco
- Dataset: [eltorio/ROCOv2-radiology](https://huggingface.co/datasets/eltorio/ROCOv2-radiology).
- Demo: Siddartha01/medical-report-generator.

## Uses

### Direct Use
This model generates radiology-style captions from medical images without further fine-tuning. Suitable for research, education, and prototyping medical report generators. Example: Input chest X-ray → Output: "Chest X-ray shows normal lung fields."

### Downstream Use
Integrate into web apps with Gradio/Hugging Face Spaces, RAG systems for reports, or LLMs for detailed analysis.

### Out-of-Scope Use
Not for clinical diagnosis, real-world medical decisions, or non-radiology images. Misuse may lead to inaccurate reports.

## Bias, Risks, and Limitations
Medical datasets like ROCO have biases toward common pathologies and English-language captions from publications. Model may underperform on rare conditions, diverse demographics, or low-quality images. Risks include over-reliance leading to misdiagnosis—use only for research.

### Recommendations
Users should validate outputs with experts, disclose model limitations in deployments, and fine-tune further on domain-specific data. Monitor for hallucinations in generated reports.

## How to Get Started with the Model
```python
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

model = BlipForConditionalGeneration.from_pretrained("[YOUR HF USERNAME]/[YOUR REPO NAME]")
processor = BlipProcessor.from_pretrained("[YOUR HF USERNAME]/[YOUR REPO NAME]")

url = "https://example.com/radiology-image.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

inputs = processor(images=image, return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
caption = processor.decode(outputs, skip_special_tokens=True)

print("Generated Report:", caption)
