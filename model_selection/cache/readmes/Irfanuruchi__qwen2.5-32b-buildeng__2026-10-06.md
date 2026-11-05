---
license: apache-2.0
language:
  - en
pipeline_tag: text-generation
tags:
  - civil-engineering
  - structural-engineering
  - building-engineering
  - construction
  - engineering
  - qwen
  - qlora
  - reasoning
  - llm
  - safety
base_model:
  - Qwen/Qwen2.5-32B-Instruct
datasets:
  - Irfanuruchi/buildeng
---

# Qwen2.5-32B BuildEng

Repository: `Irfanuruchi/qwen2.5-32b-buildeng`

Qwen2.5-32B BuildEng is the flagship large-scale branch of the BuildEng V8 project, based on `Qwen/Qwen2.5-32B-Instruct`.

BuildEng is a domain-specialized engineering language model project focused on civil engineering, structural reasoning, construction workflows, field diagnostics, and conservative engineering-assistant behavior. The main objective is not to make the model sound confident at all costs, but to make it reason more carefully when information is incomplete, field conditions are uncertain, or structural safety may be involved.

Compared to the smaller BuildEng 1.5B and 3B branches, this 32B model is focused on deeper reasoning consistency, longer engineering workflows, stronger failure-analysis behavior, and broader civil/building engineering coverage.

---

# Dedication

This release is dedicated to my father for his birthday.

He is a civil and building engineer, and one of the main reasons I chose the engineering path myself. His discipline, responsibility, and way of thinking shaped how I understand engineering: not only as technical knowledge, but as judgment, patience, and care for the people who depend on the work being done correctly.

BuildEng is my own field, computer engineering and AI, connected with the engineering world that inspired me from him. In that sense, this project is both technical work and a personal thank you.

> “My father is the engineer I looked up to before I even understood what engineering really meant.”

Happy birthday, Dad. Thank you for everything.

---

# Base Model

Qwen/Qwen2.5-32B-Instruct

---

# Dataset

Dataset repository: `Irfanuruchi/buildeng`

Training dataset: BuildEng V8 Final

Total validated samples: 145,117

The BuildEng V8 dataset was designed primarily around civil and structural engineering workflows, with a focus on conservative engineering reasoning behavior. It covers reinforced concrete beams, slabs and slab-column behavior, columns, footings and foundations, retaining walls, structural load paths, settlement and soil reasoning, construction sequencing, structural failure analysis, temporary bracing and shoring, renovation and unknown-condition reasoning, waterproofing failures, HVAC airflow and duct reasoning, inspection workflows, uncertainty handling, contradiction handling, cause-versus-symptom separation, repair and refusal logic, multi-turn engineering diagnosis, and adversarial engineering prompts.

The dataset was intentionally structured to discourage unsafe certainty and encourage cautious engineering behavior.

---

# Training

The model was trained using QLoRA fine-tuning with vanilla Transformers, PEFT, and TRL. Training used 4-bit NF4 quantization, bf16 precision, LoRA rank 32, LoRA alpha 64, sequence length 4096, effective batch size 8, a cosine scheduler, and an NVIDIA A100 80GB GPU.

The model was initially trained as a LoRA adapter and later merged into the full base model. This repository contains the fully merged model weights.

---

# BuildEng Model Family

BuildEng V8 includes three main branches.

BuildEng 1.5B is the lightweight branch designed for efficient local inference and lower-VRAM systems while keeping the same conservative engineering reasoning direction.

BuildEng 3B is the mid-sized branch focused on improving reasoning consistency, workflow stability, and engineering coverage while remaining computationally efficient.

BuildEng 32B is the primary large-scale branch, focused on deeper structural reasoning, stronger inspection workflows, broader engineering coverage, and more stable long-context engineering behavior.

---

# Main Behavior Goals

BuildEng 32B was trained to separate symptoms from diagnosis, avoid unsupported structural approval, request missing engineering information, reduce unsafe certainty, follow inspection-first workflows, recognize load-path concerns, identify potentially unsafe field conditions, support investigation and repair workflows, distinguish serviceability concerns from structural-capacity concerns, and respond conservatively to demolition, cracking, settlement, corrosion, deflection, moisture, and structural damage scenarios.

The model intentionally avoids behaving like an overconfident general-purpose assistant.

---

# Important Limitation

This model is not a licensed engineer and must not be used as final engineering approval, design certification, or construction sign-off.

It is intended for research, education, engineering-assistant workflows, drafting support, preliminary engineering reasoning, and inspection-oriented analysis. Final decisions involving structural safety, demolition, occupancy, repairs, construction approval, or engineering certification should always be reviewed and approved by a qualified licensed engineer.

---

# Future Work

Planned future directions include GGUF releases, Ollama compatibility, stronger structural calculation support, improved inspection and drawing-oriented workflows, expanded engineering datasets, and optimized lightweight BuildEng variants.

---

# Author

Irfan Uruchi

Part of my ongoing work on domain-specialized engineering language models, structural reasoning datasets, and practical civil/building engineering AI systems.