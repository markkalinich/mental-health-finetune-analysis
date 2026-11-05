---
license: apache-2.0
---


## 🧠 MedGEMMA-4B-IT Fine-tuned on LLaVA-Med 10k — Stepwise Reasoning with Web Search Tags

This repository contains my **LoRA fine-tuned version of [`google/medgemma-4b-it`](https://huggingface.co/google/medgemma-4b-it)**, trained on a modified version of the [LLaVA-Med 10k dataset](https://github.com/microsoft/LLaVA-Med).

### 🔍 What’s New

My fine-tuned model is designed to:

* Provide **step-by-step visual reasoning** for medical images
* Generate **web search terms** that can be used to find similar cases or reference images online

### 📊 Dataset

I used the [`llava_med_instruct_fig_captions.json`](https://github.com/microsoft/LLaVA-Med/blob/main/data/instruct/llava_med_instruct_fig_captions.json) file (10k examples) and **converted each image-caption pair into a structured reasoning dataset**. Each entry includes stepwise analysis and a suggested web search tag based on the image content.

### 🛠️ Fine-tuning Method

* **Base model**: `google/medgemma-4b-it`
* **Method**: LoRA-based supervised fine-tuning (SFT)
* **Platform**: AWS SageMaker (`ml.g5.12xlarge`)
* **Objective**: Train the model to output detailed diagnostic steps and relevant search terms

---

## 🚀 How to Use

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import torch

# Load processor and model
processor = AutoProcessor.from_pretrained("Manusinhh/medgemma-4b-it-finetuned-llavamed-10k")
model = AutoModelForImageTextToText.from_pretrained(
    "Manusinhh/medgemma-4b-it-finetuned-llavamed-10k",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Load image
image = Image.open("test.jpg").convert("RGB")

# Chat-style prompt
messages = [
    {
        "role": "system",
        "content": [{"type": "text", "text": "You are a helpful assistant."}]
    },
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "Analyze this medical image and provide step-by-step findings."}
        ]
    }
]

# Prepare inputs
inputs = processor.apply_chat_template(
    messages,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
    add_generation_prompt=True
).to(model.device)

# Generate
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=200)

# Decode
print(processor.decode(outputs[0], skip_special_tokens=True))
```

---

## 💡 Sample Output

**Input Prompt**:

> Analyze this medical image and provide step-by-step findings.

**Output**:

```
Analyzing Right Middle Lobe: Ill-defined opacity observed in the right middle lobe on chest X-ray  
Analyzing Left Middle Lobe: Ill-defined opacity present in the left middle lobe on chest X-ray  
Analyzing Smaller Nodules: Multiple smaller nodules noted throughout both lungs on chest X-ray  
Analyzing Associated Findings: Bone lesions are present in the ribs and pelvis  
Final Answer: The chest X-ray demonstrates bilateral pulmonary nodules with associated rib and pelvic bone lesions, potentially indicative of advanced lung cancer.  
Web Search: Chest X-ray pulmonary nodules
```

## Training Data
This model was fine-tuned on the [MedGemma LLaVA-Med 10K Reasoning Dataset](https://huggingface.co/datasets/Manusinhh/medgemma_llava-med10k_dataset).

### Dataset Features:
```python
{
  "image": <PIL.Image>,
  "messages": [
    {"role": "user", "content": [{"type": "image"}, {"type": "text", "text": "Analyze..."}]},
    {"role": "assistant", "content": [{"type": "text", "text": "1. Finding A\n2. Finding B\nDiagnosis: X"}]}
  ]
}


```
### ⚠️ Note:
This model was fine-tuned for **research and learning purposes only**.
The outputs may contain **errors or hallucinations**, and should **not** be used for clinical diagnosis or medical decision-making.
Always consult a qualified medical professional for any real-world use.

## 🧑‍💻 Author

Created and fine-tuned by **Manusinh Thakor** for research and learning purposes.  
For more, visit: [https://huggingface.co/Manusinhh](https://huggingface.co/Manusinhh)

---

