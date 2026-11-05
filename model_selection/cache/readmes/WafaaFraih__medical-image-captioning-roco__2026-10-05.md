---
tags:
- image-captioning
- medical-imaging
- vision-language
- radiology
datasets:
- eltorio/ROCOv2-radiology
language:
- en
metrics:
- wer
base_model: microsoft/git-base
---

# Medical Image Captioning Model

This model is fine-tuned for medical image captioning using the ROCOv2 radiology dataset.

## Model Description

- **Base Model**: microsoft/git-base
- **Training Data**: ROCOv2 radiology images
- **Task**: Generate descriptive captions for medical/radiology images
- **Language**: English

## Usage

```python
from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image

# Load model and processor
processor = AutoProcessor.from_pretrained("WafaaFraih/medical-image-captioning-roco")
model = AutoModelForCausalLM.from_pretrained("WafaaFraih/medical-image-captioning-roco")

# Load and process image
image = Image.open("path_to_medical_image.jpg")
inputs = processor(images=image, return_tensors="pt")

# Generate caption
generated_ids = model.generate(pixel_values=inputs.pixel_values, max_length=100)
caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(caption)
```

## Training Details

- **Training Samples**: 1800
- **Validation Samples**: 200
- **Epochs**: 10
- **Batch Size**: 8
- **Learning Rate**: 5e-05

## Evaluation

Evaluated using Word Error Rate (WER) metric on medical image descriptions.

## Limitations

- Trained on a subset of ROCOv2 dataset
- Performance may vary on different imaging modalities
- Should not be used for clinical diagnosis without expert validation

## Citation

If you use this model, please cite:

```bibtex
@misc{medical-image-captioning,
  author = {WafaaFraih},
  title = {Medical Image Captioning Model},
  year = {2025},
  publisher = {Hugging Face},
  url = {https://huggingface.co/WafaaFraih/medical-image-captioning-roco}
}
```

## Acknowledgments

- Base model: Microsoft GIT
- Dataset: ROCOv2 Radiology Dataset
