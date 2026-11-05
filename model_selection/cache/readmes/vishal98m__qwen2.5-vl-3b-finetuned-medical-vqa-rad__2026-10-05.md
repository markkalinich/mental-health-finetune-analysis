---
license: apache-2.0
base_model: Qwen/Qwen2.5-VL-3B-Instruct
datasets:
  - flaviagiammarino/vqa-rad
language:
  - en
tags:
  - medical
  - radiology
  - vqa
  - vision-language-model
  - qwen2.5-vl
  - qlora
  - peft
  - fine-tuned
pipeline_tag: visual-question-answering
---
 
# Qwen2.5-VL-3B — Medical VQA (VQA-RAD)
 
This is a fine-tuned version of [Qwen/Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) trained on the [VQA-RAD](https://huggingface.co/datasets/flaviagiammarino/vqa-rad) radiology visual question answering dataset using **QLoRA**. The LoRA adapter weights have been **merged into the base model**, so no PEFT dependency is required at inference time.
 
---
 
## Model Details
 
| Property | Value |
|----------|-------|
| **Base Model** | `Qwen/Qwen2.5-VL-3B-Instruct` |
| **Fine-tuning Method** | QLoRA (4-bit quantized base, LoRA adapters) |
| **LoRA Rank** | 16 |
| **LoRA Alpha** | 32 |
| **LoRA Dropout** | 0.05 |
| **Vision Encoder** | Frozen (language layers only fine-tuned) |
| **Merged** | Yes — `merge_and_unload()` applied post-training |
| **Language** | English |
| **License** | Apache 2.0 |
 
---
 
## Training Details
 
| Hyperparameter | Value |
|----------------|-------|
| **Epochs** | 3 |
| **Learning Rate** | 2e-4 |
| **LR Scheduler** | Cosine |
| **Warmup Ratio** | 0.03 |
| **Batch Size (per device)** | 1 |
| **Gradient Accumulation Steps** | 4 |
| **Effective Batch Size** | 4 |
| **Max Sequence Length** | 512 |
| **Optimizer** | Paged AdamW 8-bit |
| **Precision** | bfloat16 |
| **Gradient Checkpointing** | Yes (Unsloth patched) |
| **Framework** | Unsloth + TRL SFTTrainer |
 
### LoRA Target Modules
Language attention and MLP layers. Vision encoder weights were **frozen** during training — only the language decoder was adapted.
 
---
 
## Dataset
 
**VQA-RAD** ([flaviagiammarino/vqa-rad](https://huggingface.co/datasets/flaviagiammarino/vqa-rad)) is a clinician-generated radiology VQA dataset with 2,248 question-answer pairs across 315 radiology images covering chest X-rays, head CTs, and abdominal scans.
 
Questions are split into two types:
- **Closed-ended**: Yes/No and constrained categorical answers
- **Open-ended**: Free-form short phrase answers
 
Evaluation is on the official **test split (451 samples)**.
 
---
 
## Evaluation Results
 
### Overall
 
| Metric | Base Model | Fine-tuned | Improvement |
|--------|-----------|------------|-------------|
| **Exact Match (EM)** | 48.12% | **53.88%** | +11.97% (relative) |
| **Token F1** | — | **58.43%** | — |
 
### By Question Type (Fine-tuned Model)
 
| Question Type | Exact Match | Token F1 |
|---------------|-------------|----------|
| Closed-ended | 77.29% | 77.29% |
| Open-ended | 24.50% | 34.75% |
 
> **Note on metrics**: Closed-ended EM and F1 are identical because yes/no answers are single tokens. The open-ended EM→F1 gap (24.50% → 34.75%) indicates that many EM failures are phrasing mismatches rather than factual errors — the model produces semantically correct answers that don't exactly match the ground truth string.
 
---
 
## Usage
 
```python
from transformers import Qwen2_5_VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
from PIL import Image
import torch
 
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    "vishal98m/qwen2.5-vl-3b-finetuned-medical-vqa-rad",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(
    "Qwen/Qwen2.5-VL-3B-Instruct",
    use_fast=False
)
 
def ask(image: Image.Image, question: str) -> str:
    prompt = (
        f"{question}\n"
        "Provide only the short direct answer in 1-5 words. "
        "Do not explain or add any extra text."
    )
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text",  "text": prompt},
            ],
        }
    ]
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs = process_vision_info(messages)
    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    ).to("cuda")
 
    with torch.no_grad():
        generated_ids = model.generate(**inputs, max_new_tokens=32)
 
    trimmed = [
        out[len(inp):]
        for inp, out in zip(inputs.input_ids, generated_ids)
    ]
    return processor.batch_decode(
        trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )[0].strip()
 
# Example
image = Image.open("chest_xray.jpg")
print(ask(image, "Is there any abnormality in this chest X-ray?"))
```
 
---
 
## Inference Tips
 
- **Prompt format matters**: The model was trained to produce short answers. Prompting with *"Provide only the short direct answer in 1-5 words"* significantly improves exact match performance by suppressing verbose outputs.
- **Normalization**: For evaluation, lowercase and strip punctuation before comparing answers.
- **Hardware**: Runs on a single 8GB+ VRAM GPU in bfloat16. For CPU inference, switch to `torch_dtype=torch.float32`.
 
---
 
## Intended Use
 
### ✅ Suitable For
- Medical radiology question answering (academic and educational contexts)
- Study aid for medical and life science students
- Generating explanations of radiological findings and imaging concepts
- Prototype development for medical education tools
 
### ❌ Not Suitable For
- Clinical decision-making or patient diagnosis
- Replacing licensed medical professionals
- Providing personalised medical advice
- Any safety-critical medical application
 
---
 
## Limitations
 
- **Domain**: Fine-tuned exclusively on VQA-RAD. Generalization to other medical VQA benchmarks (PathVQA, SLAKE) has not been evaluated.
- **Open-ended answers**: Token F1 (34.75%) is a more faithful measure of open-ended performance than EM (24.50%) — strict string matching penalizes valid paraphrases.
- **Not for clinical use**: This model is a research artifact. It should not be used for clinical decision-making or patient care.
- **Model size**: At 3B parameters, absolute performance is below larger medical VLMs. Larger variants would likely yield higher scores.
- **Vision encoder frozen**: Only the language decoder was fine-tuned. Fine-tuning the vision encoder may yield additional gains.
 
---
 
## Citation
 
If you use this model, please cite the original VQA-RAD dataset:
 
```bibtex
@article{lau2018dataset,
  title={A Dataset of Clinically Generated Visual Questions and Answers about Radiology Images},
  author={Lau, Jason J and Gayen, Soumya and Ben Abacha, Asma and Demner-Fushman, Dina},
  journal={Scientific data},
  volume={5},
  number={1},
  pages={1--10},
  year={2018},
  publisher={Nature Publishing Group}
}
```
 
And the relevant methods:
 
```bibtex
@article{hu2022lora,
  title={LoRA: Low-Rank Adaptation of Large Language Models},
  author={Hu, Edward J and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
  journal={ICLR},
  year={2022}
}
 
@article{dettmers2023qlora,
  title={QLoRA: Efficient Finetuning of Quantized LLMs},
  author={Dettmers, Tim and Pagnoni, Artidoro and Fansi, Ari and Zettlemoyer, Luke},
  journal={NeurIPS},
  year={2023}
}
```

# Uploaded  model

- **Developed by:** vishal98m
- **License:** apache-2.0
- **Finetuned from model :** unsloth/Qwen2.5-VL-3B-Instruct

This qwen2_5_vl model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth)

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
