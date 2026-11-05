---
base_model: unsloth/llama-3.2-11b-vision-instruct-unsloth-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
license: apache-2.0
language:
- en
---
# Radiologist Llama (`Cosmobillian/radiologist_llama`)

`Radiologist Llama` is a high-performance, multimodal large language model based on `unsloth/Llama-3.2-11B-Vision-Instruct`, fine-tuned to generate radiology reports from chest X-ray (CXR) images. This model is trained to analyze a given X-ray image and produce findings and impressions in text format, mimicking the expertise of a radiologist.

The training process was accelerated using the **Unsloth** library, which enabled training to be completed **2x faster** and with significantly less VRAM consumption compared to standard fine-tuning methods.

## 🚀 Key Features

- **Specialization:** Radiology, specifically the analysis and reporting of chest X-rays.
- **Base Model:** Built on the powerful `Llama-3.2-11B-Vision-Instruct`.
- **Dataset:** Fine-tuned on tens of thousands of images and reports from the `itsanmolgupta/mimic-cxr-dataset` available on Hugging Face.
- **Efficient Training:** Utilized the 4-bit QLoRA (Quantized Low-Rank Adaptation) technique with Unsloth to efficiently fine-tune both the vision and language layers of the model.
- **Ready to Use:** The model is saved with its LoRA adapters merged into `float16` format, allowing for direct, high-performance inference with libraries such as VLLM.

## 🔧 Model Architecture and Training Details

The development of this model followed these steps:

1.  **Model Loading:** The `unsloth/Llama-3.2-11B-Vision-Instruct` model was loaded in **4-bit** precision to significantly reduce memory usage.
2.  **PEFT (LoRA) Integration:** **LoRA (Low-Rank Adaptation)** adapters were added to both the vision encoder and the language decoder layers of the model. This approach avoids training all the parameters of the massive model, instead focusing on the small and manageable adapters, which speeds up the process and enhances resource efficiency.
    - `r = 16`
    - `lora_alpha = 32`
    - `lora_dropout = 0.05`
3.  **Dataset Preparation:** Each sample from the `mimic-cxr-dataset` was converted into a conversational format:
    - **User:** The X-ray image + the instruction: `"You are an expert radiographer. Describe accurately what you see in this image."`
    - **Assistant:** The text from the `impression` or `findings` section of the corresponding radiology report.
4.  **Training:** The model was trained for 1 epoch on 30,633 prepared samples using the `SFTTrainer` from the `trl` library. The data processing pipeline was optimized with Unsloth's custom `UnslothVisionDataCollator`.

### Training Hyperparameters

| Parameter                   | Value      |
| :-------------------------- | :--------- |
| **Learning Rate** | `1e-4`     |
| **Number of Epochs** | `1`        |
| **Batch Size (per device)** | `2`        |
| **Gradient Accumulation Steps** | `8`      |
| **Effective Batch Size** | `16`       |
| **Optimizer** | `adamw_8bit` |
| **LR Scheduler** | `linear`   |
| **Warmup Steps** | `5`        |
| **Weight Decay** | `0.01`     |
| **Max Sequence Length** | `2048`     |

## 👨‍💻 How to Use (Inference)

Generating a report for a chest X-ray image using this model is straightforward.

### 1. Install Necessary Libraries

```bash

%%capture
import os, re
if "COLAB_" not in "".join(os.environ.keys()):
    !pip install unsloth
else:
    import torch; v = re.match(r"[0-9\\.]{3,}", str(torch.__version__)).group(0)
    xformers = "xformers==" + ("0.0.32.post2" if v == "2.8.0" else "0.0.29.post3")
    !pip install --no-deps bitsandbytes accelerate {xformers} peft trl triton cut_cross_entropy unsloth_zoo
    !pip install sentencepiece protobuf "datasets>=3.4.1,<4.0.0" "huggingface_hub>=0.34.0" hf_transfer
    !pip install --no-deps unsloth
!pip install transformers==4.55.4
!pip install --no-deps trl==0.22.2
```

### 2. Run Inference with Python

The following code snippet demonstrates how to load the model and generate a report from an image.

```python
from unsloth import FastVisionModel
from transformers import TextStreamer
from PIL import Image
import torch

# Load the model and tokenizer in 16-bit (float16)
# If you have less VRAM, you can use load_in_4bit=True
model, tokenizer = FastVisionModel.from_pretrained(
    "Cosmobillian/radiologist_llama",
    dtype=torch.float16,
    load_in_4bit=False, # False is ideal since the model was saved in 16-bit
)

# Prepare the model for inference
FastVisionModel.for_inference(model)

# Load your image (specify the path to your own X-ray image)
try:
    image = Image.open("path/to/your/xray.jpg")
except FileNotFoundError:
    print("Please provide a valid file path instead of 'path/to/your/xray.jpg'.")
    # Creating a blank image as a placeholder
    image = Image.new('RGB', (512, 512), 'black')


# The instruction format the model was trained on
instruction = "You are an expert radiographer. Describe accurately what you see in this image."

# Format the messages according to the chat template
messages = [
    {"role": "user", "content": [
        {"type": "image"},
        {"type": "text", "text": instruction}
    ]}
]

# Prepare the inputs with the tokenizer
input_text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
inputs = tokenizer(
    image,
    input_text,
    add_special_tokens=False, # Already present in the template
    return_tensors="pt",
).to("cuda")

# Use TextStreamer for real-time output
text_streamer = TextStreamer(tokenizer, skip_prompt=True)

print("Model is generating the report...\n---")

# Run the model and stream the output
_ = model.generate(
    **inputs,
    streamer=text_streamer,
    max_new_tokens=256 # Maximum number of tokens to generate
)
```

## ⚠️ Disclaimer and Limitations

- **Not Medical Advice:** This model was developed for **research and experimental purposes only**. The text it generates **MUST NOT** be considered a real medical diagnosis or a substitute for the professional judgment of a qualified radiologist.
- **Not for Clinical Use:** The model's outputs should not be used as a basis for patient diagnosis, treatment, or any clinical decision-making process. It may produce incorrect or incomplete information.
- **Dataset Limitations:** The model's knowledge is limited to the information contained in the `MIMIC-CXR` dataset. It may not be able to accurately report on rare conditions, artifacts, or different imaging protocols not present in the dataset. Furthermore, the model may have inherited biases present in the training data.
- **No Guarantees:** No guarantees are made regarding the accuracy, consistency, or reliability of the model's outputs.

## Author

✍️ Author & Acknowledgement
This model was developed by **Cengizhan **BAYRAM (Cosmobillian) using the Unsloth and Hugging Face ecosystems.

Acknowledgement: This project was developed as a submission for the Samsung Innovation Campus program.