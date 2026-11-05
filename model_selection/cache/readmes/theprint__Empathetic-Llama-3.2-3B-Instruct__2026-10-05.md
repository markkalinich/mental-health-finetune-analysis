---
base_model: meta-llama/Llama-3.2-3B-Instruct
library_name: peft
pipeline_tag: text-generation
language: en
license: apache-2.0
tags:
- lora
- sft
- transformers
- trl
- unsloth
- fine-tuned
datasets:
- theprint/Empathetic-Alpaca
---
# Empathetic-Llama-3.2-3B-Instruct

A fine-tuned Llama 3.1 3B model, fine tuned for chat with empathic and supportive responses.

## Model Details

This model is a fine-tuned version of meta-llama/Llama-3.2-3B-Instruct using the Unsloth framework with LoRA (Low-Rank Adaptation) for efficient training.

- **Developed by:** theprint
- **Model type:** Causal Language Model (Fine-tuned with LoRA)
- **Language:** en
- **License:** apache-2.0
- **Base model:** meta-llama/Llama-3.2-3B-Instruct
- **Fine-tuning method:** LoRA with rank 128

## GGUF Quantized Versions

Quantized GGUF versions are available [right here](https://huggingface.co/theprint/Empathetic-Llama-3.2-3B-Instruct-GGUF):

- `Empathetic-Llama-3.2-3B-Instruct-f16.gguf` (6135.6 MB) - 16-bit float (original precision, largest file)
- `Empathetic-Llama-3.2-3B-Instruct-q3_k_m.gguf` (1609.0 MB) - 3-bit quantization (medium quality)
- `Empathetic-Llama-3.2-3B-Instruct-q4_k_m.gguf` (1925.8 MB) - 4-bit quantization (medium, recommended for most use cases)
- `Empathetic-Llama-3.2-3B-Instruct-q5_k_m.gguf` (2214.6 MB) - 5-bit quantization (medium, good quality)
- `Empathetic-Llama-3.2-3B-Instruct-q6_k.gguf` (2521.4 MB) - 6-bit quantization (high quality)
- `Empathetic-Llama-3.2-3B-Instruct-q8_0.gguf` (3263.4 MB) - 8-bit quantization (very high quality)

## Intended Use

Casual conversation.

## Training Details

### Training Data

The "Empathetic" data set was specifically created with friendly responses in mind.

- **Dataset:** theprint/Empathetic-Alpaca
- **Format:** alpaca

### Training Procedure

- **Training epochs:** 3
- **LoRA rank:** 128
- **Learning rate:** 0.0001
- **Batch size:** 4
- **Framework:** Unsloth + transformers + PEFT
- **Hardware:** NVIDIA RTX 5090

## Usage

```python
from unsloth import FastLanguageModel
import torch

# Load model and tokenizer
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="theprint/Empathetic-Llama-3.2-3B-Instruct",
    max_seq_length=4096,
    dtype=None,
    load_in_4bit=True,
)

# Enable inference mode
FastLanguageModel.for_inference(model)

# Example usage
inputs = tokenizer(["Your prompt here"], return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Alternative Usage (Standard Transformers)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "theprint/Empathetic-Llama-3.2-3B-Instruct",
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("theprint/Empathetic-Llama-3.2-3B-Instruct")

# Example usage
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Your question here"}
]

inputs = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)
outputs = model.generate(inputs, max_new_tokens=256, temperature=0.7, do_sample=True)
response = tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)
print(response)
```

### Using with llama.cpp

```bash
# Download a quantized version (q4_k_m recommended for most use cases)
wget https://huggingface.co/theprint/Empathetic-Llama-3.2-3B-Instruct/resolve/main/gguf/Empathetic-Llama-3.2-3B-Instruct-q4_k_m.gguf

# Run with llama.cpp
./llama.cpp/main -m Empathetic-Llama-3.2-3B-Instruct-q4_k_m.gguf -p "Your prompt here" -n 256
```
## Limitations

May provide incorrect information.

## Citation

If you use this model, please cite:

```bibtex
@misc{empathetic_llama_3.2_3b_instruct,
  title={Empathetic-Llama-3.2-3B-Instruct: Fine-tuned meta-llama/Llama-3.2-3B-Instruct},
  author={theprint},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/theprint/Empathetic-Llama-3.2-3B-Instruct}
}
```

## Acknowledgments

- Base model: [meta-llama/Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct)
- Training dataset: [theprint/Empathetic-Alpaca](https://huggingface.co/datasets/theprint/Empathetic-Alpaca)
- Fine-tuning framework: [Unsloth](https://github.com/unslothai/unsloth)
- Quantization: [llama.cpp](https://github.com/ggerganov/llama.cpp)
