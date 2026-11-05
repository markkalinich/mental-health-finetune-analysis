---
license: apache-2.0
language:
- en
base_model:
- google/medgemma-4b-it
pipeline_tag: image-text-to-text
tags:
- medical
- vlm
- image-quality-assessment
- ct-scan
- medgemma
- sft
---

# Explainable Radiologist-Aligned VLM for CT Image Quality Assessment (CT-IQA)

## Model Summary

**MedGemma-4B-IT-SFTCTIQA** is a fine-tuned Vision-Language Model (VLM) designed to automate the assessment of Computed Tomography (CT) image quality. Based on Google's `medgemma-4b-it`, this model has been fine-tuned using Supervised Fine-Tuning (SFT) with Low-Rank Adaptation (LoRA) to align visual perception with expert radiologist judgments.

Unlike general-purpose VLMs that often fail to provide consistent medical quality scores in zero-shot settings, this model delivers:
1.  **Quantitative Scores:** A quality score ranging from 0 (very poor) to 4 (excellent).
2.  **Qualitative Explanations:** detailed, interpretable reasoning covering noise, artifacts, and contrast, simulating a radiologist's thought process.

## Key Improvements & Performance

The original MedGemma-4B-IT model struggles with the CT-IQA task in zero-shot settings, often showing negative correlation with human experts. Our fine-tuned version achieves state-of-the-art performance among open-weights models, significantly outperforming zero-shot baselines like Gemini 2.5 Pro and Flash.

| Model | SRCC (Spearman) | PLCC (Pearson) | MAE | RMSE |
| :--- | :--- | :--- | :--- | :--- |
| MedGemma-4B-IT (Zero-shot) | -0.2438 | -0.2029 | 1.4790 | 1.7566 |
| Gemini 2.5 Flash (Zero-shot) | 0.7170 | 0.6946 | 0.7360 | 0.8800 |
| Gemini 2.5 Pro (Zero-shot) | 0.7328 | 0.7204 | 0.6540 | 0.8340 |
| **Ours (Fine-tuned)** | **0.8396** | **0.8214** | **0.5080** | **0.6639** |

*   **Correlation:** Achieved an SRCC of **0.8396**, improving by over +1.0 compared to the base model.
*   **Accuracy:** Reduced Mean Absolute Error (MAE) by **65.65%** (from 1.4790 to 0.5080).
*   **Reliability:** Provides stable, diagnostically meaningful text explanations consistent with expert reasoning.

## Dataset Information

The model was fine-tuned on a specialized dataset constructed from:

*   **Images & Scores:** The **LDCTIQA (Low-Dose Computed Tomography Perceptual Image Quality Assessment)** dataset from the MICCAI 2023 Challenge. It contains 1,000 CT slices covering various anatomical regions and noise levels.
    *   *Split:* 800 (Train) / 100 (Val) / 100 (Test).
*   **Textual Explanations:** To enable Explainable AI (XAI), we generated expert-level reasoning text for the training set using **Gemini 2.5 Pro**. These texts were paired with the ground-truth scores to form structured instruction-response pairs for SFT.

## How to Use

You can load this model directly using the `transformers` library.

### Installation
```bash
pip install transformers torch pillow
```

### Inference Code

```python
import torch
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image

# 1. Load Model and Processor
model_id = "MikaJesse/medgemma-4b-it-sftCTIQA"
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForImageTextToText.from_pretrained(
    model_id,
    torch_dtype=torch.float32, 
    device_map="auto"
)

# 2. Prepare Inputs
# Prompt used during training
prompt_text = (
    "Evaluate the technical and diagnostic quality of this CT image. "
    "Predict a score from 0 (very poor) to 4 (excellent), and explain your reasoning clearly. "
    "Provide both the numerical score and the explanation in your answer."
)

image_path = "path/to/your/ct_image.png"
image = Image.open(image_path).convert("RGB")

messages = [
    {"role": "user", "content": [
        {"type": "text", "text": prompt_text},
        {"type": "image"}
    ]}
]

# 3. Inference
inputs = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=inputs, images=[image], return_tensors="pt").to(model.device)

with torch.inference_mode():
    output_ids = model.generate(**inputs, max_new_tokens=512, do_sample=False)

# 4. Decode Output
generated_text = processor.decode(output_ids[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
print(generated_text)
```

## Intended Use & Limitations

*   **Intended Use:** Research purposes for automated CT image quality assessment and explainable medical imaging analysis.
*   **Limitations:**
    *   The textual reasoning was distilled from Gemini 2.5 Pro and validated against scores, but subtle clinical linguistic nuances may differ from human radiologists.
    *   Validated primarily on the LDCTIQA dataset; generalization to other scanner types or anatomical regions requires further verification.
    *   **Not for Clinical Diagnosis:** This model is for quality assessment only and should not be used for primary diagnosis.

## Citation

If you use this model in your research, please cite our work (BVM 2026 submission):

```bibtex
@inproceedings{Wang2026CTIQA,
  title={Explainable Radiologist-Aligned VLM for CT Image Quality Assessment},
  author={Wang, Jiajun and Sun, Yipeng and Bayer, Siming and Maier, Andreas},
  booktitle={Bildverarbeitung für die Medizin (BVM)},
  year={2026}
}
```
*(Note: Citation details will be updated upon publication)*
```