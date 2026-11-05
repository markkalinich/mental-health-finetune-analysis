---
license: apache-2.0
datasets:
  - AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations
language:
  - en
pipeline_tag: text-generation
tags:
  - mixture-of-experts
  - moe
  - expert-pruning
  - gpt-oss
  - openai
  - reasoning
  - health-or-medicine
  - specialized
  - efficient
  - transformer
  - causal-lm
  - text-generation
  - pytorch
  - pruned-model
  - domain-specific
---

# Health Or Medicine GPT-OSS Model (9 Experts)

**Project**: https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/

<div align="center">

### 👥 Follow the Authors

**Aman Priyanshu**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aman-priyanshu/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/AmanPriyanshu6)
[![Website](https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox&logoColor=white)](https://amanpriyanshu.github.io/)

**Supriti Vijay**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/supriti-vijay/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://x.com/SupritiVijay)
[![Website](https://img.shields.io/badge/Website-FF7139?style=for-the-badge&logo=firefox&logoColor=white)](https://supritivijay.github.io/)

</div>

## Introduction

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 9 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~7.2B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 9 |
| **Layers** | 24 |
| **Top-k Routing** | 4 |
| **Context Length** | 128K tokens |
| **Attention Heads** | 64 (Query), 8 (Key-Value) |
| **Residual Dimension** | 2880 |
| **Attention Pattern** | Alternating dense & sliding window (128 tokens) |
| **Positional Encoding** | RoPE (Rotary Position Embedding) |
| **Normalization** | RMSNorm |
| **Precision** | BF16 |
| **License** | Apache 2.0 |
| **Specialization** | Health Or Medicine |

## Pruning Methodology

### What is Expert Pruning?
Mixture-of-Experts models contain multiple specialized sub-networks (experts) per layer. During inference, only a subset of experts are activated for each token. Expert pruning involves:

1. **Analyzing Usage Patterns**: Tracking which experts activate most frequently for specific tasks
2. **Removing Underutilized Experts**: Discarding experts with low activation rates for the target domain
3. **Preserving Router Functionality**: Maintaining the routing mechanism with fewer available experts

### Our Approach
- **Data-Driven Selection**: Used activation patterns from health or medicine evaluation tasks
- **Systematic Reduction**: Reduced from 32 to 9 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 28.1% of original expert parameters
- **Reduced Computational Load**: Fewer routing decisions during inference
- **Focused Capabilities**: Retains experts relevant to health or medicine tasks

### Use Cases
- **Speculative Decoding**: Draft model for full GPT-OSS-20B
- **Resource-Constrained Deployment**: Edge devices, mobile applications
- **Research**: Study expert specialization in MoE models
- **Fine-tuning**: Smaller base model for domain adaptation

*Note: Performance may vary depending on how well the pruned experts match your specific use case.*

## Motivation & Expert Selection

This medical domain model incorporates experts that activated highly during health and medical tasks from MMLU medical subjects. These experts specialize in clinical knowledge, anatomy, medical procedures, and health-related reasoning.

The expert selection process utilized our comprehensive analysis of router activation patterns across multiple evaluation benchmarks:

- **GPQA**: Graduate-level questions in physics, chemistry, biology (Diamond & Expert subsets)
- **MMLU/MMLU-Pro**: Comprehensive knowledge across 57+ subjects including science, medicine, law
- **SORRY-Bench**: Safety evaluation across harmful content categories  
- **Tulu3**: Persona-driven instruction following with verifiable constraints
- **Polyglot-or-Not**: Multilingual factual completion tasks

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 9 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 9 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-7.2b-specialized-health_or_medicine-pruned-moe-only-9-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-7.2b-specialized-health_or_medicine-pruned-moe-only-9-experts")

# Generate with the model
messages = [
    {"role": "user", "content": "What are the main functions of the human heart?"}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    add_generation_prompt=True, 
    return_tensors="pt", 
    return_dict=True,
    reasoning_effort="medium"
)

# Ensure inputs are on the same device as model
inputs = {k: v.to(model.device) for k, v in inputs.items()}

outputs = model.generate(
    **inputs, 
    max_new_tokens=512,
    do_sample=True,
    temperature=0.1,
    top_p=0.9,
    pad_token_id=tokenizer.eos_token_id,
    eos_token_id=tokenizer.eos_token_id
)

# Decode only the generated part
input_length = inputs['input_ids'].shape[1]
response_tokens = outputs[0][input_length:]
response = tokenizer.decode(response_tokens, skip_special_tokens=True)
print(response)
```

### Apple Silicon (MPS) Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Check MPS availability and load model
device = "mps" if torch.backends.mps.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-7.2b-specialized-health_or_medicine-pruned-moe-only-9-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-7.2b-specialized-health_or_medicine-pruned-moe-only-9-experts")

# Generate with the model
messages = [
    {"role": "user", "content": "What are the main functions of the human heart?"}
]

inputs = tokenizer.apply_chat_template(
    messages, 
    add_generation_prompt=True, 
    return_tensors="pt", 
    return_dict=True,
    reasoning_effort="medium"
)

# Move inputs to model device
inputs = {k: v.to(model.device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

# Use torch.no_grad for MPS stability
with torch.no_grad():
    outputs = model.generate(
        **inputs, 
        max_new_tokens=512,
        do_sample=True,
        temperature=0.1,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        use_cache=True
    )

# Decode only the generated part
input_length = inputs['input_ids'].shape[1]
response_tokens = outputs[0][input_length:]
response = tokenizer.decode(response_tokens, skip_special_tokens=True)
print(response)
```

### GPU Inference

For CUDA GPU inference, the models work with minimal modifications from the CPU example above. Simply change:
```python
device_map="auto"  # Will automatically use GPU if available
torch_dtype=torch.bfloat16  # or torch.float16
```

## Model Examples

The following examples demonstrate the model's performance on health or medicine tasks:

### Example 1
**Question:** What are the main functions of the human heart?

**Response:**
```
<|channel|>analysis<|message|>Need answer.<|end|><|start|>assistant<|channel|>final<|message|>The heart is a central organ that performs two essential functions—p pumping blood through the body and regulating the blood‑pressure system.  In short, the heart’s main functions are:

1. **P‑p (pump)** – The heart’s contractive action (the “s‑s” or systic‑s) moves blood from the heart chambers into the circulation, ensuring oxygen and nutrients reach every tissue.

2. **S‑s (system)** – The heart’s electrical and neuro‑hadroneal activity (the “s‑s” or sympathetic‑s) controls blood‑pressure, heart‑rate, and vascular tone, keeping blood volume and pressure within the body.

These two functions keep the body’s home‑balance and are the core of the heart’s life‑support.<|return|>
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need to explain differences: classification, structure, replication, disease, etc.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Virons – the “big” and the “small” in life**

| Feature | Bacteria | Virons |
|---|**What is** | Microorganisms that are *alive* – they are cells that can grow, divide, and make a self‑sbody. | Microorganisms that are *not alive* – they are particles that can replicate inside a cell but cannot grow or divide on themselves. |
|---|**Size** | Usually 1–2 – 3 – 4 – 5 – 6 – 7 – 8 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10 – 10
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes** is a chronic disease in the body’s blood‑sugar‑control system.  The main two types are:

* **Type 1 (T‑1)** – an autoimmune attack on the pancreas that destroys insulin‑producing β‑isompan cells.  
* **Type 2 (T‑2)** – insulin resistance in the target tissues (musmus, liver, fat) and a relative insulin‑seins deficiency.

Below is a quick guide to the symptoms and the causes of each type.

---

## 1.  Symptoms of Diabetes

| **Early‑stage (often silent)** | **Later‑stage (more obvious)** | **Common symptoms** | **What do you do?** |
|---|---|---|---|

| • **Blood‑sugar spikes** – high glucose in the blood | • **Weight loss** – especially in T‑2 | • **Polyglidity** – frequent “sweets” or “sure” cravings | • **Check your blood‑sugar** – fasting or random tests |
| • **Fatigue** – “I’m tired all day” | • **Weight gain** – especially in T‑1 | • **Polod** – “I’m thirsty all day” | • **Check your blood‑sugar** – fasting or random tests |
| • **Vision changes** – blurred vision, eye‑s problems | • **Skin changes** – dry, itchy skin | • **Skin changes** – dry, itchy skin | • **Check your blood‑sugar** – fasting or random tests |
| • **Infections** – frequent skin or urinary infections | • **Infections** – frequent skin or urinary infections | • **Infections** – frequent skin or urinary infections | • **Check your blood‑sugar** – fasting or random tests |

**Key points**  
* **T‑1** – symptoms appear early (weight loss, fatigue, low‑blood‑sugar).  
* **T‑2** – symptoms appear later (weight gain, thirst, blurred vision).  
* **Both** – high‑blood‑sugar can cause “sweets” cravings, “sure” cravings, and “sure” thirst.

---

## 2.  Causes of Diabetes

| **Type 1** | **Type 2** | **Other factors** | **What do you do?** |
|---
```

---

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{priyanshu2025gptoss,
  title={{GPT-OSS MoE Expert Fingerprinting: Analyzing Expert Activation Patterns in Mixture of Experts Models}},
  author={Priyanshu, Aman and Vijay, Supriti},
  year={2025},
  howpublished={\url{https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/}},
  note={Interactive analysis tool for expert activation patterns in MoE architectures}
}
```

## References & Resources

- **Original Model**: [OpenAI GPT-OSS Model Card](https://openai.com/index/introducing-gpt-oss/)
- **Model Hub**: [GPT-OSS-20B on Hugging Face](https://huggingface.co/openai/gpt-oss-20b)
- **Expert Analysis Dataset**: [GPT-OSS-20B MoE Expert Activations](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations)
- **Project Page**: [GPT-OSS MoE Expert Fingerprinting](https://amanpriyanshu.github.io/GPT-OSS-MoE-ExpertFingerprinting/)
- **GitHub Repository**: [OpenAI GPT-OSS](https://github.com/openai/gpt-oss)
