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

# Health Or Medicine GPT-OSS Model (29 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 29 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~19.1B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 29 |
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
- **Systematic Reduction**: Reduced from 32 to 29 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 90.6% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 29 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 29 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-19.1b-specialized-health_or_medicine-pruned-moe-only-29-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-19.1b-specialized-health_or_medicine-pruned-moe-only-29-experts")

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
    "AmanPriyanshu/gpt-oss-19.1b-specialized-health_or_medicine-pruned-moe-only-29-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-19.1b-specialized-health_or_medicine-pruned-moe-only-29-experts")

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
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>The human heart is a muscular pump that performs several essential functions to keep the body’s circulatory system running smoothly. Its main functions can be grouped into three broad categories:

| Function | What it does | Why it matters |
|----------|--------------|----------------|
| **Pumping blood** | The heart contracts (systole) and relaxes (diastole) to move blood through the body. | Keeps oxygen, nutrients, hormones, and waste products circulating. |
| **Maintaining blood pressure** | By generating enough force during systole, the heart sets the pressure that drives blood through arteries and capillaries. | Ensures tissues receive adequate perfusion and that blood returns to the heart. |
| **Regulating blood flow** | The heart’s rhythm and contractility can be adjusted by the autonomic nervous system and hormonal signals. | Allows the body to respond to changes in activity, stress, or metabolic demand. |

### 1. Pumping Blood
- **Four chambers**: Two atria (upper chambers) receive blood; two ventricles (lower chambers) pump it out.
- **Right side**: Receives de‑oxygenated blood from the body and pumps it to the lungs (pulmonary circulation).
- **Left side**: Receives oxygenated blood from the lungs and pumps it to the rest of the body (systemic circulation).

### 2. Maintaining Blood Pressure
- **Systolic pressure**: The peak pressure during ventricular contraction; drives blood into arteries.
- **Diastolic pressure**: The pressure when the heart relaxes; allows coronary arteries to fill and maintains perfusion of tissues.
- **Pulse pressure**: The difference between systolic and diastolic pressures; reflects arterial compliance and cardiac output.

### 3. Regulating Blood Flow
- **Heart rate**: Controlled by the sinoatrial (SA) node, autonomic nervous system, and hormones (e.g., adrenaline).
- **Stroke volume**: The amount of blood ejected per beat; influenced by preload (venous return), afterload (vascular resistance), and contractility.
- **Cardiac output**: Heart rate × stroke volume; the total volume of blood pumped per minute.

---

#### How These Functions Work Together

1. **Blood enters the right atrium** → passes to the right ventricle → pumped to the lungs.  
2. **Oxygenated blood returns to the left atr
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need concise explanation.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – the key differences**

| Feature | Bacteria | Viruses |
|---------|----------|---------|
| **Cellular status** | True cells – prokaryotic, with a cell membrane, cytoplasm, ribosomes, and a cell wall (often peptidoglycan). | Not cells – just a protein coat (capsid) surrounding genetic material (DNA or RNA). No cellular machinery. |
| **Size** | 0.5–5 µm (visible under light microscope). | 20–300 nm (visible only with electron microscopy). |
| **Reproduction** | Autonomous binary fission; can grow and divide on their own. | Must hijack a host cell’s machinery to replicate; no independent growth. |
| **Genetic material** | Usually circular or linear DNA; some have plasmids. | Either DNA or RNA, single‑ or double‑stranded, linear or circular. |
| **Metabolism** | Can be autotrophic (photosynthetic or chemosynthetic) or heterotrophic; many have diverse metabolic pathways. | No metabolism; rely entirely on host cell processes. |
| **Structure** | Cell wall, cytoplasmic membrane, ribosomes, sometimes flagella or pili. | Capsid (protein shell), sometimes an envelope derived from host membrane, and a nucleic acid core. |
| **Life cycle** | Can form colonies, biofilms, and spores (in some species). | Infects a single cell, replicates, assembles new virions, then exits (lysis or budding). |
| **Treatment** | Antibiotics target bacterial cell wall, protein synthesis, DNA replication, etc. | Antivirals target viral enzymes or entry/exit steps; antibiotics are ineffective. |
| **Role in disease** | Can cause infections (e.g., pneumonia, urinary tract infection) but many are harmless or beneficial. | Cause diseases by destroying host cells (e.g., influenza, HIV, COVID‑19). |
| **Examples** | *Escherichia coli*, *Staphylococcus aureus*, *Mycobacterium tuberculosis*. | Influenza virus, HIV, SARS‑CoV‑2, HPV. |

**Bottom line:**  
Bacteria are living, self‑sufficient cells that can grow and divide on their own. Viruses are sub‑cellular particles that need a host cell to replicate; they are
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a group of metabolic disorders characterized by chronic hyperglycemia (high blood sugar). The two most common types are type 1 and type 2, but there are other forms (gestational, monogenic, etc.). Below is a concise overview of the main symptoms, causes, and some key differences between the types.

---

## 1. Symptoms

| Symptom | Typical Onset | Why It Happens |
|---------|---------------|----------------|
| **Polyuria** (frequent urination) | Often early | Kidneys excrete excess glucose, pulling water with it. |
| **Polydipsia** (excessive thirst) | Early | Dehydration from fluid loss. |
| **Polyphagia** (increased hunger) | Early | Cells can’t use glucose, so the body signals for more food. |
| **Weight loss** (especially in type 1) | Early | Body breaks down fat and muscle for energy. |
| **Fatigue / weakness** | Early | Energy production is impaired. |
| **Blurred vision** | Early | Hyperglycemia causes fluid shifts in the lens. |
| **Slow‑healing cuts or infections** | Early‑mid | Poor blood flow and immune function. |
| **Numbness or tingling in extremities** | Mid‑to‑late | Peripheral neuropathy from chronic high glucose. |
| **Red, swollen, or painful gums** | Mid‑to‑late | Poor wound healing and gum disease. |
| **Recurrent urinary tract or vaginal infections** | Mid‑to‑late | High glucose in urine/glands promotes bacterial growth. |
| **Skin changes (e.g., dark patches, itching)** | Late | Advanced disease or associated conditions. |

> **Tip:** In type 2 diabetes, many people are asymptomatic for years; routine screening (fasting glucose, HbA1c) is essential if risk factors are present.

---

## 2. Causes & Risk Factors

| Type | Primary Cause | Key Risk Factors |
|------|---------------|------------------|
| **Type 1 Diabetes** | Autoimmune destruction of pancreatic β‑cells → insulin deficiency | • Genetic predisposition (HLA genes) <br>• Viral infections (e.g., enteroviruses) <br>• Early childhood onset <br>• Low vitamin D (possible link) |
| **Type 2 Diabetes
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
