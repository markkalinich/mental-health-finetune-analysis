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

# Health Or Medicine GPT-OSS Model (14 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 14 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~10.2B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 14 |
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
- **Systematic Reduction**: Reduced from 32 to 14 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 43.8% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 14 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 14 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-10.2b-specialized-health_or_medicine-pruned-moe-only-14-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-10.2b-specialized-health_or_medicine-pruned-moe-only-14-experts")

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
    "AmanPriyanshu/gpt-oss-10.2b-specialized-health_or_medicine-pruned-moe-only-14-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-10.2b-specialized-health_or_medicine-pruned-moe-only-14-experts")

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
<|channel|>analysis<|message|>Need to answer: pumping blood, regulating blood pressure, endocrine functions (atrial natriuretic peptide, renin), conduction system, valves, etc.<|end|><|start|>assistant<|channel|>final<|message|>**The human heart is a multi‑organ organ that performs several essential functions, all of which are tightly linked to the circulatory system.  Below are the main roles of the heart, grouped into the most common categories:**

| **Primary Function** | **What it does** | **Key anatomical/physological features** |
|---|---|---|
| **P pumping blood** | Moves oxygen‑rich blood from the left side of the body (lungs, upper extremities) to the right side (heart, lower extremities) and then back to the lungs. | • 4 chambers (right atrium, left atrium, right ventricle, left ventricle) | • 3 valves (tricuspid, mitral, aortic) | • 3 valves (tricuspid, mitral, pulmonary) |
| **Regulating blood pressure** | Maintains a constant blood pressure by adjusting the force of contraction (stroke volume) and the resistance of the systemic circulation. | • Autonomic nervous system (sym‑/parasym) | • Hormonal systems (renin‑angiotensin, atrial natriuretic peptide) |
| **Endocrine (h endocrine) functions** | Releases hormones that influence fluid balance, blood volume, and vascular tone. | • Atrial natriuretic peptide (ANP) – vasodilator, natriuretic | • Renin – stimulates angiotensin‑II production |
| **Electrical conduction** | Generates the heartbeat and coordinates the contraction of the heart muscle. | • Sino‑atrial (SA) node – “pacemaker” | • Atrioventricular (AV) node – delays impulse to ventricles | • Bundle of His, Purkinje fibers – rapid conduction |
| **Mechanical support** | Provides a structural scaffold for the circulatory system, protecting blood vessels and organs. | • Coronary arteries – supply the heart itself | • Cardiac valves – prevent back‑flow |
| **Metabolic support** | Supplies the heart’s own energy needs and recycles metabolic waste. | • Coronary circulation – oxygen, nutrients | • Myocardial glycogen stores – energy reserve |

---

### 1. **P Pumping Blood**

- **Stroke Volume**: The amount of blood
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need explain differences: size, structure, replication, genetics, etc.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – The Key Differences**

| Feature | Bacteria | Viruses |
|---|---|---|
| **Definition** | Single‑cell, living organisms that can grow and divide | Non‑living particles that need a host cell to replicate |
| **Size** | 1–10 µm (micrometers) – visible under a light microscope | 0.1–100 nm (nanometers) – invisible to the naked eye |
| **Structure** | Complex cell with a cell wall, membrane, cytoplasm, ribosomes, DNA, and often organelles | Very simple: a protein shell (capsid) that enclues genetic material (DNA or RNA); no cytoplasmic machinery |
| **Genetic Material** | Usually a double‑stranded DNA genome (some bacteria have plasmids) | Can be DNA or RNA; may be single‑ or double‑stranded |
| **Replication** | Grow by cell division (mitosis‑like process) – can multiply rapidly (hours) | Must hij‑take a host cell’s machinery; replication can be very fast (minutes) but depends on host |
| **Energy Source** | Metabolic pathways (oxidation, photosynthesis, etc.) | None – relies on host cell’s energy |
| **Infection Mechanism** | Can colonize surfaces, invade tissues, or remain in the gut; may cause disease by toxins, enzymes, or immune response | Attach to a cell, enter it, release genome, replicate, and exit (lyse or exocytosis) |
| **Immune Response** | Recognized by pattern‑recognation receptors (PRRs) and adaptive immunity; can be cleared by antibiotics | Recognized by PRRs and adaptive immunity; cleared by antiviral drugs or immune‑mediated killing |
| **Treatment** | Antibiotics (target cell wall, protein synthesis, etc.) | Antivirals (target viral enzymes, replication steps) or vaccines |
| **Examples** | *Staphylococcus aureus*, *E. coli*, *Mycobacterium tuberculosis* | Influenza A, HIV, SARS‑CoV‑2, HPV |

**Key Take‑aways**

1. **Living vs. Non‑living** – Bacteria are living cells that can grow on their own; viruses are inert particles that need a host cell to replicate.  
2
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to explain symptoms and causes.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a chronic metabolic disorder in which the body cannot produce or use insulin effectively, leading to high blood glucose levels. The two main types—Type 1 and Type 2—have overlapping symptoms but different underlying causes. Below is a concise overview of the symptoms and the causes for each type, plus a brief look at other forms of diabetes.

---

## 1.  Symptoms of Diabetes

| Symptom | Why it happens | How it shows on the day |
|---|---|---|
| **Freckle‑like, sticky skin** | High glucose damages skin cells | Skin looks shiny, dry, or “sticky” |
| **Frequent thirst** | Kidneys try to excrete glucose | “I’m always thirsty” |
| **Frequent urination** | Kidneys excrete excess glucose | “I’m peeing a lot” |
| **Weight loss** (Type 1) | Body burns more glucose | Losing weight even without dieting |
| **Weight gain** (Type 2) | Insulin resistance → more fat stored | Gaining weight despite normal diet |
| **Fatigue / low energy** | Cells can’t use glucose efficiently | Feeling tired, sluggish |
| **Poor wound healing** | High glucose impairs immune & collagen | Cuts or sores take longer to close |
| **Vision changes** | High glucose damages retina | Blurred vision, floaters |
| **Increased infections** | Immune system weakened | Frequent colwors, thrush |
| **Night‑time hypoglycemia** (Type 1) | Insulin spikes too high | “I’m suddenly low‑glucose at night” |
| **Hyperglycemic episodes** (Type 2) | Blood glucose spikes | “I’m suddenly high‑glucose” |

> **Note** – Many people have no obvious symptoms early on, especially Type 2. That’s why routine screening is key.

---

## 2.  Causes of Diabetes

### 2‑1.  Type 1 Diabetes (T1D)

| Cause | Mechanism | Risk factors |
|---|---|---|
| **Auto‑immune destruction of β‑cells** | Immune system attacks insulin‑producing cells in the pancreas | Genetics, viral infections (e.g., enterovirus), early childhood, certain ethnic groups |
| **Genetic predisposition** | Certain HLA genes increase
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
