
---
library_name: llama-cpp-python
tags:
- medical
- llama-3
- gguf
- quantized
- chatbot
- healthcare
license: llama3
datasets:
- ruslanmv/ai-medical-chatbot
language:
- en
---

# Llama-3-8B Medical Chatbot (GGUF)

This is a fine-tuned version of Meta's Llama-3-8B-Instruct model, specifically optimized for medical and healthcare-related conversations. The model has been quantized into the GGUF format (`Q4_K_M`) to allow efficient, lightweight inference on standard CPUs without requiring expensive GPU resources.

## Model Details

### Model Description

This model acts as an AI medical assistant. It was fine-tuned using Parameter-Efficient Fine-Tuning (PEFT/LoRA) on a large dataset of patient-doctor dialogues. After training, the adapter weights were merged with the base Llama-3 model, converted to `.gguf` format, and quantized to 4-bit precision to drastically reduce memory footprint (from ~16GB to ~4.9GB) while maintaining high-quality responses.

- **Developed by:** Erdem Yavuz
- **Model type:** Causal Language Model (Quantized GGUF)
- **Language(s) (NLP):** English
- **License:** Meta Llama 3 Community License
- **Finetuned from model:** `meta-llama/Meta-Llama-3-8B-Instruct`

### Model Sources

- **Demo:** [Link to your Hugging Face Space here, e.g., https://huggingface.co/spaces/erdemyavuz/medical-chatbot]
- **Base Model:** https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct

## Uses

### Direct Use

This model is intended for educational, research, and hobbyist purposes. It can be used directly with `llama.cpp` or `llama-cpp-python` to simulate a medical chatbot environment, helping developers build lightweight healthcare-assistive UI applications (like Gradio or Streamlit apps).

### Out-of-Scope Use

**Medical Disclaimer:** This model is **NOT** a certified medical professional. It cannot be used for actual medical diagnosis, treatment planning, or prescribing medication. The outputs are purely for informational and demonstrative purposes. Do not use this model in critical healthcare environments.

## Bias, Risks, and Limitations

Large Language Models can hallucinate, produce biased content, or confidently state incorrect facts. Because this model is trained on internet-sourced medical Q&A, it may reflect historical biases in healthcare or suggest outdated treatments. 

### Recommendations

Users should always implement a strict disclaimer in any UI deploying this model. Downstream applications should ideally include a human-in-the-loop (e.g., a real doctor verifying the information) before any AI-generated medical text is presented as factual.

## How to Get Started with the Model

Since this is a GGUF model, the easiest way to run it is using `llama-cpp-python`. Use the code below to get started:

```python
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

# Download the model
model_path = hf_hub_download(
    repo_id="erdemyavuz/llama-3-8b-chat-doctor", 
    filename="llama-3-8b-chat-doctor-Q4_K_M.gguf"
)

# Initialize the model (CPU optimized)
llm = Llama(
    model_path=model_path,
    n_ctx=2048,      # Context window
    n_threads=2,     # Adjust based on your CPU cores
    n_gpu_layers=0   # Set to >0 if you have a GPU
)

# Generate a response
prompt = "Patient: Hello doctor, I have a bad headache and fever. What should I do?\nDoctor:"
output = llm(prompt, max_tokens=256, stop=["Patient:"], echo=False)

print(output["choices"][0]["text"])

```

## Training Details

### Training Data

The model was fine-tuned on the `ruslanmv/ai-medical-chatbot` dataset, which contains approximately 250,000 distinct dialogues between patients and doctors, covering a wide range of symptoms, inquiries, and general medical advice.

### Training Procedure

#### Preprocessing

The dialogue data was formatted into a conversational prompt structure using the standard OpenAI `chatml` / Llama-3 instruction templates to ensure the model distinguishes between the "user" (patient) and the "assistant" (doctor).

#### Training Hyperparameters

* **Training regime:** QLoRA (4-bit base model loading)
* **Epochs:** 1
* **Learning Rate:** 2e-4
* **Optimizer:** `paged_adamw_32bit`
* **LoRA Rank (r):** 16
* **LoRA Alpha:** 32
* **Target Modules:** `['up_proj', 'down_proj', 'gate_proj', 'k_proj', 'q_proj', 'v_proj', 'o_proj']`

#### Speeds, Sizes, Times

* **Original Base Model Size:** ~16 GB
* **Quantized GGUF Size:** ~4.92 GB
* **Quantization Method:** `Q4_K_M` (via llama.cpp)

## Environmental Impact

* **Hardware Type:** GPU P100 (for fine-tuning via Kaggle) / Free CPU Tier (for HF Spaces Deployment)
* **Compute Region:** Global

## Model Card Contact

For any questions, issues, or collaborative inquiries regarding this model, please reach out via GitHub or Hugging Face.

```