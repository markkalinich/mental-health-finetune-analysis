---
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
- FreedomIntelligence/Medical-R1-Distill-Data
- UCSC-VLAA/MedReason
language:
- en
base_model:
- unsloth/gpt-oss-20b-BF16
pipeline_tag: text-generation
tags:
- SFT
- llama.cpp
- unsloth
- huggingface
- QAT
- Clinical
- chain-of-thought
- gguf
license: apache-2.0
---
# Clinical Chain-of-Thought Medical Assistant (GPT-OSS-20B, GGUF)

This repository provides GGUF builds of a clinical reasoning model that was fine-tuned from `unsloth/gpt-oss-20b-BF16`. Medical questions are answered with an explicit reasoning trace, which is emitted inside `<think> ... </think>` tags, followed by a final answer. The GGUF files are intended for inference through llama.cpp, Ollama, and `llama-cpp-python`. A merged 16-bit checkpoint is also included as safetensors so that the model can be loaded with Transformers from the same repository.

> **Disclaimer:** This model was built for research and educational purposes only. It is not a medical device and is not intended to be used for diagnosis, treatment, or any clinical decision making. Professional medical advice should always be sought from a qualified clinician.

## GGUF Files

Four GGUF builds are provided. The quantization level of each file is indicated by its name.

| File | Quantization | Size | Recommended for |
|---|---|---|---|
| `model-q4_k_m.gguf` | 4-bit (Q4_K_M) | 15.8 GB | Default choice. The strongest balance between size and quality is offered here. |
| `model-q5_k_m.gguf` | 5-bit (Q5_K_M) | 16.9 GB | Slightly higher fidelity at a modestly larger footprint. |
| `model-q8_0.gguf` | 8-bit (Q8_0) | 22.3 GB | Near-lossless quality where footprint is less of a concern. |
| `model-f16.gguf` | 16-bit (F16) | 41.9 GB | Unquantized reference. It is mainly intended for re-quantization rather than direct use. |

For most deployments, `model-q4_k_m.gguf` is recommended. Runtime memory roughly tracks the file size, with additional headroom required for the context window.

The merged 16-bit checkpoint (`model-0000*-of-00009.safetensors`), the tokenizer, and `chat_template.jinja` are also stored in this repository for use with Transformers.

## Model Details

| Property | Value |
|---|---|
| Base model | `unsloth/gpt-oss-20b-BF16` (OpenAI GPT-OSS-20B, Mixture-of-Experts, 21B total / 3.6B active parameters) |
| Fine-tuning method | LoRA supervised fine-tuning (SFT) followed by quantization-aware training (QAT) |
| Reasoning format | Harmony chat template with reasoning emitted inside `<think>` tags |
| Language | English |
| Training hardware | AMD MI300X (ROCm 6.4) |
| License | Apache 2.0 (inherited from the base model) |

## Usage

The harmony chat template must be used so that the model behaves correctly. The GGUF files already carry this template.

### Ollama

```bash
ollama run hf.co/Melikshah/gpt-oss-20b-clinical-cot-gguf:Q4_K_M
```

### llama.cpp

```bash
# A single quant can be downloaded with the Hugging Face CLI
huggingface-cli download Melikshah/gpt-oss-20b-clinical-cot-gguf model-q4_k_m.gguf --local-dir .

# The downloaded file can then be run
./llama-cli -m model-q4_k_m.gguf \
  -p "What are the differential diagnoses for acute chest pain?" -n 512
```

### llama-cpp-python

```python
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="Melikshah/gpt-oss-20b-clinical-cot-gguf",
    filename="model-q4_k_m.gguf",
    n_ctx=4096,
    n_gpu_layers=-1,
)

messages = [{"role": "user", "content": "What are the differential diagnoses for acute chest pain?"}]
out = llm.create_chat_completion(messages=messages, max_tokens=512, temperature=0.6, top_p=0.95)
print(out["choices"][0]["message"]["content"])
```

### Transformers (merged 16-bit checkpoint)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Melikshah/gpt-oss-20b-clinical-cot-gguf"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)

messages = [{"role": "user", "content": "What are the differential diagnoses for acute chest pain?"}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

outputs = model.generate(inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

The reasoning trace is returned inside `<think> ... </think>` and is intended for inspection and debugging rather than for display to end users.

## Training Data

Three medical reasoning datasets were merged and normalized to a unified `instruction`, `reasoning`, `output` schema. The reasoning component was wrapped in `<think>` tags during formatting.

| Dataset | Description |
|---|---|
| [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT) | Complex chain-of-thought medical reasoning |
| [FreedomIntelligence/Medical-R1-Distill-Data](https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data) | Distilled medical reasoning data |
| [UCSC-VLAA/MedReason](https://huggingface.co/datasets/UCSC-VLAA/MedReason) | Medical question answering with structured reasoning |

Rows with empty instructions or answers were filtered out, and a 95% / 5% train / eval split was created.

## Training Procedure

The model was trained in two stages. First, a LoRA adapter was trained on the merged dataset and merged back into the base weights. Second, the merged checkpoint was refined with quantization-aware training so that low-bit quality could be preserved. The refined checkpoint was then exported to the GGUF formats listed above.

| Stage | Key settings |
|---|---|
| SFT | LoRA rank 32, alpha 64, dropout 0.05, learning rate 1e-4, cosine schedule, 2 epochs, sequence packing, max sequence length 4096 |
| QAT | `int4_weight_only` scheme, LoRA rank 16, alpha 32, learning rate 5e-5, 1 epoch |

LoRA adapters were applied to `q_proj`, `k_proj`, `v_proj`, `o_proj`, `up_proj`, `down_proj`, and `gate_proj`. Training was performed with Unsloth and TRL, and runs were tracked with Weights and Biases.

## Evaluation

An LLM-as-a-judge protocol was used. Responses to 50 held-out questions were generated by four candidates, anonymized, shuffled, and then scored against the ground truth. Scores were assigned for accuracy, reasoning quality, safety, and completeness, and an overall score was aggregated from them. The figures below were reported with a GPT-5.2 judge.

**Win rate (out of 50 prompts)**

| Model | Wins | Win rate |
|---|---|---|
| Fine-tuned GPT-OSS (BF16) | 35 | 70.0% |
| QAT fine-tuned GPT-OSS | 14 | 28.0% |
| Base GPT-OSS (unfine-tuned) | 1 | 2.0% |
| GPT-4.1 (OpenAI API) | 0 | 0.0% |

**Average overall score (1 to 10)**

| Model | Score |
|---|---|
| Fine-tuned GPT-OSS (BF16) | 9.16 |
| QAT fine-tuned GPT-OSS | 8.32 |
| GPT-4.1 (OpenAI API) | 7.37 |
| Base GPT-OSS (unfine-tuned) | 7.12 |

> These figures were obtained from a 50-question sample scored by a single judge, and they should therefore be treated as preliminary.

## Demo
[![Clinical CoT Medical Assistant Demo](https://i9.ytimg.com/vi_webp/IGAzB2DXqoM/mqdefault.webp?v=69538fc2&sqp=CMS5zsoG&rs=AOn4CLA1idn9AqUggv0AJyr9And76Abc1Q)](https://www.youtube.com/watch?v=IGAzB2DXqoM "Clinical CoT Medical Assistant Demo")

## Intended Use and Limitations

This model is intended to be used for research into medical reasoning, for educational demonstrations, and for the study of chain-of-thought fine-tuning. Clinical deployment is not supported.

The following limitations should be kept in mind. Incorrect or fabricated information may be produced, since hallucination is not eliminated by fine-tuning. Coverage is limited to the topics present in the training datasets, and English is the only language that was targeted. Some quality loss is expected at lower quantization levels. The published evaluation is small in scale and was scored by a single automated judge, so the reported quality should not be over-interpreted.

## Acknowledgements and Citation

The base model `gpt-oss-20b` was released by OpenAI under the Apache 2.0 license, and fine-tuning was performed with [Unsloth](https://github.com/unslothai/unsloth). The full training and evaluation pipeline is available at [TheDeadcoder/medical-cot-assistant](https://github.com/TheDeadcoder/medical-cot-assistant).

The source datasets should be cited if this model is used:

```bibtex
@misc{medical-o1-reasoning, title={Medical-O1-Reasoning-SFT}, author={FreedomIntelligence}, year={2024}, publisher={HuggingFace}}
@misc{medical-r1-distill, title={Medical-R1-Distill-Data}, author={FreedomIntelligence}, year={2024}, publisher={HuggingFace}}
@misc{medreason, title={MedReason}, author={UCSC-VLAA}, year={2024}, publisher={HuggingFace}}
```