---
license: cc-by-4.0
base_model: google/medgemma-4b-it
tags:
- medical
- radiology
- chest-x-ray
- multimodal
- report-generation
- structured-reporting
- contextualized
- temporal-reasoning
- impression
- lora
- medical-imaging
- clinical-nlp
language:
- en
pipeline_tag: image-text-to-text
library_name: transformers
datasets:
- erjui/csrrg_ift_dataset
---

# medgemma-4b: Contextualized Structured Radiology Report Generation (Impression)

This model is a fine-tuned version of [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it) for generating the **IMPRESSION** section of contextualized structured chest X-ray radiology reports.
It was trained using LoRA (Low-Rank Adaptation) on the [csrrg_ift_dataset](https://huggingface.co/datasets/erjui/csrrg_ift_dataset) containing instruction-following examples from MIMIC-CXR and CheXpert+ datasets.

## Model Description

This model performs **Contextualized Structured Radiology Report Generation (CSRRG)** for chest X-rays, generating concise impression sections with rich clinical context including patient history, imaging technique, comparison to prior studies, and temporal reasoning.

**Key characteristics:**
- Generates the **IMPRESSION** section of radiology reports
- Incorporates **clinical history/indication**, **technique**, and **comparison** to prior studies
- Performs temporal reasoning across multiple examinations
- Produces clinically relevant summaries with contextual awareness
- Fine-tuned with LoRA for parameter-efficient adaptation

## Intended Use

### Primary Use Cases
- Research on contextualized radiology report generation
- Development of temporal reasoning systems for medical imaging
- Clinical decision support with longitudinal patient data
- Medical AI and multimodal model research
- Educational tools for radiology training

### Intended Users
- Medical AI researchers
- Healthcare technology developers
- Clinical informatics specialists
- Radiology departments (research use only)

### Out-of-Scope Use
- **NOT intended for clinical diagnosis without physician review**
- Should not replace human radiologists in clinical practice
- Requires validation before any clinical deployment

## Training Details

### Training Data
- **Dataset**: [csrrg_ift_dataset](https://huggingface.co/datasets/erjui/csrrg_ift_dataset) (csrrg_ift_dataset_impression subset)
- **Training samples**: ~405,971 instruction-following examples
- **Data sources**: MIMIC-CXR and CheXpert+ chest X-ray datasets
- **Task format**: Instruction fine-tuning with rich clinical context
- **Context includes**: Clinical history/indication, imaging technique, comparison to prior studies, current and prior images

### Training Procedure

**Fine-tuning method**: LoRA (Low-Rank Adaptation)

**LoRA Configuration:**
- Rank (r): 32
- Alpha: 64
- Dropout: 0.1
- Target modules: `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`

**Training hyperparameters:**
- Learning rate: 2e-4
- Batch size: 4 per device
- Gradient accumulation steps: 32 (effective batch size: 128)
- Epochs: 1
- Optimizer: AdamW
- Learning rate scheduler: Cosine with 3% warmup
- Precision: bfloat16
- Attention implementation: Flash Attention 2
- Max sequence length: 2048
- Max images per sample: 3

**Hardware:**
- GPU: NVIDIA H100
- Training framework: HuggingFace Transformers + PEFT

## Usage

### Loading the Model

```python
from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import torch

# Load model and processor
model_name = "erjui/medgemma-4b-csrrg-impression"
model = AutoModelForVision2Seq.from_pretrained(
    model_name,
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained("google/medgemma-4b-it", trust_remote_code=True)

# Load chest X-ray images (current and prior studies)
# CSRRG models support multiple images for temporal comparison (max_images_per_sample: 3)
current_image = Image.open("current_xray.jpg")

# Prepare input with clinical context
messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are an expert radiologist."}]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": """Analyze the chest X-ray images and write the IMPRESSION section of a radiology report. Provide a concise clinical summary and diagnosis based on the imaging findings. Consider the available clinical contexts when formulating your impression.

=== CLINICAL HISTORY/INDICATION ===
Male patient with leukocytosis and fever, query pneumonia.

=== TECHNIQUE ===
Portable anteroposterior chest radiograph.

=== COMPARISON ===
None.

=== CURRENT IMAGES ==="""
            },
            {"type": "image"}  # Current image (supports multiple images for temporal comparison)
        ]
    }
]

# Process and generate
inputs = processor(images=current_image, text=messages, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256)
generated_text = processor.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
```

### Expected Output Format

```
IMPRESSION:
1. Right apical rounded opacity concerning for infection or malignancy.
2. Recommend repeat dedicated AP and lateral chest radiograph, or CT for further evaluation.
```

## Citation

If you use this model, please cite:

```bibtex
@article{kang2025automated,
  title={Automated Structured Radiology Report Generation with Rich Clinical Context},
  author={Kang, Seongjae and Lee, Dong Bok and Jung, Juho and Kim, Dongseop and Kim, Won Hwa and Joo, Sunghoon},
  journal={arXiv preprint arXiv:2510.00428},
  year={2025}
}
```

Also cite the base model:
```bibtex
@article{sellergren2025medgemma,
  title={Medgemma technical report},
  author={Sellergren, Andrew and Kazemzadeh, Sahar and Jaroensri, Tiam and Kiraly, Atilla and Traverse, Madeleine and Kohlberger, Timo and Xu, Shawn and Jamil, Fayaz and Hughes, C{\'\i}an and Lau, Charles and others},
  journal={arXiv preprint arXiv:2507.05201},
  year={2025}
}
```

## Model Card Authors

Seongjae Kang (erjui)

## Model Card Contact

For questions or issues, please open an issue on the [model repository](https://huggingface.co/erjui/medgemma-4b-csrrg-impression/discussions).

