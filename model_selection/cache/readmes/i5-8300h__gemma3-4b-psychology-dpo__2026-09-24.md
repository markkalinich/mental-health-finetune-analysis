---
library_name: transformers
datasets:
- entfane/psychotherapy-dpo
base_model:
- google/gemma-3-4b-it
license: gemma
language:
- en
pipeline_tag: text-generation
---

# Model Card for i5-8300h/gemma3-4b-psychology-dpo


## Model Details
DPO and LoRA PeFT finetuned version of Gemma 3 4B for response tone adjustment

### Model Description


This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** Original model developed by Google Deepmind, finetuning by Ram Sundar Radhakrishnan
- **Model type:** Text-Text - Causal Text Generation (Base model is multimodal, finetuning has been done on text-text tasks only.)
- **Finetuned from model [optional]:** Google Gemma 3 4B (Instruction Tuned)



## Uses

Psychologically aligned chatbot tasks

### Direct Use

Psychologically aligned chatbot tasks


### Out-of-Scope Use

#### Medical advice, therapeutic advice - this model has not been trained to deliver any form of medical advice.
#### Not a substitute for a licensed professional.


### Recommendations

Do not use in any safety critical or medically critical applications.


## How to Get Started with the Model

Use the code below to get started with the model.

*This repo contains merged weights.*
```
from transformers import AutoTokenizer, AutoModelForCausalLM
model_name = "i5-8300h/gemma3-4b-psychology-dpo"
tok = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
```

## Training Details

### Training Data
https://huggingface.co/datasets/entfane/psychotherapy-dpo


### Training Procedure

- DPO Finetuning + PeFT and LoRA
- Datatype: torch.float16
- Learning rate = 2e-5
- 3 Epochs
- Max prompt length = 128
- Max length = 256
- Beta = 0.1
- Used precomputed reference log probabilities to avoid loading a reference model, and thus save VRAM.

#### Preprocessing [optional]

Custom collator pads prompt/chosen/rejected groups independently using tokenizer.pad and ensures ID tensors are torch.long.


#### Training Hyperparameters

- **Training regime:** FP16 mixed precision and QLoRA quantized weights (4bits), 3 epochs at 2e-5 lr

#### Speeds, Sizes, Times [optional]

- ~6.5 hours for all 3 epochs (33 steps)
- 3.8/4 GB VRAM used on RTX 3050Ti
- ~4GB additional shared GPU memory

## Technical Specifications [optional]

### Compute Infrastructure


#### Hardware

- Acer Swift X SFX14 R1SG
- AMD Ryzen 7 5800u
- NVIDIA RTX 3050Ti 4GB
- 16GB DDR4 @ 4266MT/s

#### Software

Python 3.11.8

**Environment**
- torch: 2.7.1+cu126
- transformers: 5.0.0
- peft: 0.18.1
- trl: 0.21.0
- datasets: 4.0.0
- accelerate: 1.8.1
- bitsandbytes: 0.46.0
- safetensors: 0.5.3
- tokenizers: 0.22.2
- huggingface_hub: 1.4.0
- sentencepiece: 0.2.0
- protobuf: 5.29.5
- packaging: 24.2
- numpy: 2.3.1



## Model Card Authors

Ram Sundar Radhakrishnan

## Model Card Contact

Hugging Face Profile