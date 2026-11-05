
# 🩺 Fine-Tuned Medical QA Assistant (Llama-3.1-8B + QLoRA)

[![Hugging Face Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue)](https://huggingface.co/Himanshu-Vishwakarma-HF/Llama-3.1-8B-MedicalQA-LoRA)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Framework](https://img.shields.io/badge/Framework-Unsloth%20%2F%20PEFT-orange)](https://github.com/unslothai/unsloth)

An end-to-end parameter-efficient fine-tuning (PEFT) project that adapts Meta's **Llama-3.1-8B-Instruct** for domain-specific medical question answering. Utilizing **QLoRA via Unsloth**, the model was trained on a single NVIDIA T4 GPU inside Google Colab, minimizing memory consumption while retaining strong contextual reasoning.

The primary objective of this assistant is to process dense clinical or medical texts, abstract them accurately, and answer complex queries with high factual fidelity based on the **PubMedQA** dataset.

---

## 📊 Performance Benchmark

To measure domain-specific alignment, the model was evaluated against the base vanilla architecture using exact matching verification over a sample test batch from the PubMedQA evaluation set.

| Metric | Base Model (`Llama-3.1-8B-Instruct`) | Fine-Tuned Model (Medical-QA) |
| :--- | :--- | :--- |
| **Accuracy** | 62.0% | **89.0%** 🚀 |
| **Response Style** | Generic / Verbose / General Knowledge | Context-Aligned / Fact-Driven |
| **Hallucination Rate** | Moderate on niche technical terms | Low (Strictly bound to Context) |
| **Compute Overhead** | — | ~22 minutes training time on 1x T4 GPU |

---

## 🛠️ Technical Stack & Frameworks

- **Base Architecture:** `meta-llama/Meta-Llama-3.1-8B-Instruct` (Pre-quantized 4-bit via BitsAndBytes)
- **Fine-Tuning Paradigm:** QLoRA (Quantized Low-Rank Adaptation)
- **Acceleration Pipeline:** **Unsloth** (Optimized Triton kernels, reducing memory footprint and speeding up processing)
- **Dataset:** PubMedQA (`ori_pqal.json`) — Contextual medical questions mapping academic abstracts to direct interpretations.
- **Frontend Layer:** Streamlit (Option A) / Ollama Local Engine (Option B)

---

## 📈 Hyperparameters & Training Execution

The model was trained for a targeted sequence duration to balance alignment without catastrophic forgetting.

```python
# Key Hyperparameters Used During Training
training_args = TrainingArguments(
    per_device_train_batch_size = 2,
    gradient_accumulation_steps = 4,
    warmup_steps                = 5,
    max_steps                   = 80,         # Optimized training window
    learning_rate               = 2e-4,       # Standard QLoRA learning rate
    optim                       = "adamw_8bit",
    weight_decay                = 0.01,
    lr_scheduler_type           = "linear",
    seed                        = 3407,
)


### Target Modules (LoRA Adaption)

Adapters were injected into the following attention projections and feed-forward layers to capture contextual nuances:

* `q_proj`, `k_proj`, `v_proj`, `o_proj`
* `gate_proj`, `up_proj`, `down_proj`
* **LoRA Parameters:** $r = 16$, $\alpha = 16$, $\text{dropout} = 0$

---

## 📋 Instruction Template Format

The model utilizes the explicit Llama-3.1 Instruct system marker pattern to safely bind the context parameters:

```text
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an expert medical assistant. Answer the medical question accurately based strictly on the provided context.<|eot_id|><|start_header_id|>user<|end_header_id|>
Context: {Medical Abstract Text}
Question: {Clinical Inquiry}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
{Model Target Response}<|eot_id|>

```

---

## 📦 How To Run and Deploy

### Repository Architecture

```text
├── .gitignore
├── README.md
├── requirements.txt
├── Fine_Tuning_Llama_3_1_8B.ipynb      # Core Unsloth pipeline notebook script
├── app.py                   # Streamlit UI production app
└── Modelfile                # Local Ollama config engine file

```

### Option A: Local Streamlit Interactive Application

1. **Clone and Enter the Target Space:**
```bash
git clone https://github.com/Himanshu-Vishwakarma-GH/Llama-Medical-QA--Fine-Tune.git
cd Llama-Medical-QA--Fine-Tune

```


2. **Install Structural Requirements:**
```bash
pip install -r requirements.txt

```


3. **Boot Up the Native UI Interface:**
```bash
streamlit run app.py

```



### Option B: Local Runtime Execution Via Ollama GGUF

If you exported the architecture directly into GGUF variables, build and initialize via the terminal:

```bash
# Build custom system endpoint model from the manifest target
ollama create medical-qa -f ./Modelfile

# Start running local client dialogue instance
ollama run medical-qa

```

---

## 🤝 Acknowledgments & References

* **Unsloth Team** for open-sourcing extremely fast memory-efficient training mechanics.
* **PubMedQA Creators** for data parsing structures.

---
base_model: unsloth/meta-llama-3.1-8b-instruct-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- llama
license: apache-2.0
language:
- en
---

# Uploaded finetuned  model

- **Developed by:** Himanshu-Vishwakarma-HF
- **License:** apache-2.0
- **Finetuned from model :** unsloth/meta-llama-3.1-8b-instruct-bnb-4bit

This llama model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)
