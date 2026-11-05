---
language:
- la
license: mit
tags:
- tr-ocr
- optical-character-recognition
- handwriting-recognition
- historical-documents
- htr
- trocr
pipeline_tag: image-to-text
datasets:
- magistermilitum/Tridis
- ENC-PSL/MEDUSA_Synthetic_Lines
base_model:
- microsoft/trocr-base-handwritten
---

# TrOCR Finetuned for Medieval Handwriting

A handwritten text recognition (HTR) model based on
[`microsoft/trocr-base-handwritten`](https://huggingface.co/microsoft/trocr-base-handwritten),
finetuned on medieval manuscript lines (Latin and Old French).

It transcribes handwritten text lines from historical documents, such as
acts, cartularies and late-medieval manuscripts.

## Usage

```python
import torch
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

model_id = "LaMOP/TrOCR_Manicule_2026_Latin_Medieval"

processor = TrOCRProcessor.from_pretrained(model_id)
model = VisionEncoderDecoderModel.from_pretrained(model_id)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

image = Image.open("line.png").convert("RGB")
pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

with torch.inference_mode():
    generated_ids = model.generate(pixel_values, max_new_tokens=128)

text = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False,
)[0].strip()
print(text)
```

## Technical details

- **Base model**: `microsoft/trocr-base-handwritten`
- **Architecture**: TrOCR (ViT vision encoder + RoBERTa decoder)
- **Input resolution**: 384 × 384
- **Frameworks**: PyTorch, Transformers
- **Inference**: CUDA if available, otherwise CPU

## License

`mit`

## Acknowledgements:

We thank the Jacques Monod Institute for providing the computing and data processing resources required for this work.