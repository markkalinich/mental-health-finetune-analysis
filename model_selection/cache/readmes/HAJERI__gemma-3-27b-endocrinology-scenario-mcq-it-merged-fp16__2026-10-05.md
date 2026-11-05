---
license: apache-2.0
language:
- en
---

Gemma-3 Endocrinology Scenario-Based MCQ Models (20 Variants)
=============================================================

This collection contains **20 instruction-tuned Gemma-3 variants (270M–27B)** optimized for **endocrinology scenario-based MCQs** and **clinical Q&A**. Variants are provided as **LoRA adapters**, **merged FP16**, and **GGUF builds** (FP16 and Q4\_K\_M) for flexible deployment from research servers to local/offline inference.

Collection link: [https://huggingface.co/collections/HAJERI/gemma-3-endocrinology-scenario-based-mcq-models](https://huggingface.co/collections/HAJERI/gemma-3-endocrinology-scenario-based-mcq-models)

What the models can do
----------------------
All variants are designed for **three primary inference modes**:
1.  **Scenario MCQ Answering (with explanation)**: Provide the single best answer (A/B/C/D) and explain the reasoning.  
2.  **Scenario MCQ Generation**: Generate a full clinical MCQ (stem + options + correct answer + brief explanation).
3.  **General Endocrinology Q&A**: Provide concise, structured answers to general endocrinology questions.

> **Important:** These models are intended for **educational and research purposes only** and must not be used for clinical decision-making.

Dataset provenance and medical review
-------------------------------------
The dataset was **designed and prepared by Professor** _**Saeed Awad M. Alqahtani** _ (Taibah University, Saudi Arabia) and **reviewed and approved by three licensed medical doctors**:
*   Two **consultant endocrinologists**
*   One **general medical doctor**

    
Model variants in this collection:
---------------------------------

### 270M (4 variants)
*   HAJERI/gemma-3-270m-endocrinology-scenario-mcq-it-lora
*   HAJERI/gemma-3-270m-endocrinology-scenario-mcq-it-merged-fp16
*   HAJERI/gemma-3-270m-endocrinology-scenario-mcq-it-fp16-gguf
*   HAJERI/gemma-3-270m-endocrinology-scenario-mcq-it-Q4\_K\_M-gguf

### 1B (4 variants)
*   HAJERI/gemma-3-1b-endocrinology-scenario-mcq-it-lora
*   HAJERI/gemma-3-1b-endocrinology-scenario-mcq-it-merged-fp16  
*   HAJERI/gemma-3-1b-endocrinology-scenario-mcq-it-fp16-gguf  
*   HAJERI/gemma-3-1b-endocrinology-scenario-mcq-it-Q4\_K\_M-gguf
   

### 4B (4 variants)
*   HAJERI/gemma-3-4b-endocrinology-scenario-mcq-it-lora
*   HAJERI/gemma-3-4b-endocrinology-scenario-mcq-it-merged-fp16
*   HAJERI/gemma-3-4b-endocrinology-scenario-mcq-it-fp16-gguf
*   HAJERI/gemma-3-4b-endocrinology-scenario-mcq-it-Q4\_K\_M-gguf
    
### 12B (4 variants)
*   HAJERI/gemma-3-12b-endocrinology-scenario-mcq-it-lora
*   HAJERI/gemma-3-12b-endocrinology-scenario-mcq-it-merged-fp16
*   HAJERI/gemma-3-12b-endocrinology-scenario-mcq-it-fp16-gguf
*   HAJERI/gemma-3-12b-endocrinology-scenario-mcq-it-Q4\_K\_M-gguf

### 27B (4 variants)
*   HAJERI/gemma-3-27b-endocrinology-scenario-mcq-it-lora
*   HAJERI/gemma-3-27b-endocrinology-scenario-mcq-it-merged-fp16
*   HAJERI/gemma-3-27b-endocrinology-scenario-mcq-it-fp16-gguf
*   HAJERI/gemma-3-27b-endocrinology-scenario-mcq-it-Q4\_K\_M-gguf

How to choose the right variant
-------------------------------
### Pick by **deployment format**

*   **\-lora**: best if you want to keep the **base model separate** and apply adapters (research workflows, experimentation).
    
*   **\-merged-fp16**: best for **GPU inference** with a standard Transformers pipeline (higher quality, higher VRAM).
    
*   **\-fp16-gguf**: best for **llama.cpp** inference with high quality (larger RAM/VRAM than quantized).
    
*   **\-Q4\_K\_M-gguf**: best for **fast, memory-efficient local inference** (most users on laptops/desktops).
    

### Pick by **model size**
*   **270M / 1B**: fastest, lowest resource, good for lightweight education and constrained hardware.
*   **4B**: strong balance of speed and reasoning.
*   **12B**: best general quality/medical reasoning balance for many users.
*   **27B**: highest reasoning quality (requires more compute).
    

Prompt templates (the 3 modes)
------------------------------
### Mode 1 — MCQ Answer + Explanation

You are an expert endocrinologist.

Clinical scenario:

A 32-year-old woman presents with weight loss, heat intolerance, and palpitations.

Labs: suppressed TSH and elevated free T4.

Options:
A. Subacute thyroiditis
B. Graves disease
C. Hashimoto thyroiditis
D. Pituitary adenoma

Instructions:
1) Choose the single best answer.
2) Explain the reasoning.


### Mode 2 — Generate a full MCQ

You are an expert endocrinologist.

Create a clinical multiple-choice question on diabetic ketoacidosis suitable for
final-year medical students.

Include:
- A clinical scenario
- Four answer options
- The correct answer
- A brief explanation

### Mode 3 — General Endocrinology Q&A

You are an expert endocrinologist.

Question:
Explain the mechanism of action of metformin.

Inference examples
------------------

### A) GGUF inference with llama.cpp (recommended for GGUF models)

Example (Q4\_K\_M GGUF):

./main \
  -m gemma-3-12b-endocrinology-scenario-mcq-it-Q4_K_M.gguf \
  -p "You are an expert endocrinologist. Explain the pathophysiology of diabetic ketoacidosis." \
  -n 400 \
  --temp 0.7

Example (FP16 GGUF):

./main \
  -m gemma-3-12b-endocrinology-scenario-mcq-it-fp16.gguf \
  -p "You are an expert endocrinologist. Create a clinical MCQ on DKA with 4 options and explanation." \
  -n 500 \
  --temp 0.7

### B) Merged FP16 inference with Transformers (for -merged-fp16)

from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "HAJERI/gemma-3-12b-endocrinology-scenario-mcq-it-merged-fp16"

tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto")

prompt = """You are an expert endocrinologist.

Question:
Explain the mechanism of action of metformin.
"""
inputs = tok(prompt, return_tensors="pt")
out = model.generate(**inputs, max_new_tokens=350, temperature=0.7, do_sample=True)

print(tok.decode(out[0], skip_special_tokens=True))

Safety note
-----------

These models can generate clinically plausible text. Always apply:

*   Human expert review
    
*   Educational context only
    
*   No patient-specific decisions
    
Compute acknowledgement
-----------------------
Compute resources (**NVIDIA A100 80GB**) were supplied by the **National eLearning Center (NeLC), Saudi Arabia**, as part of the **AI Sandbox in Digital Learning** initiative.

Authors and contact
-------------------

Model author: **Professor Saeed Awad M. Alqahtani**

Affiliation: **Taibah University, Saudi Arabia**

email: **samqahtani@taibahu.edu.sa**

For academic, educational, or research inquiries: please open an issue on the relevant model repository.
