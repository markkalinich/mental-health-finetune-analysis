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

# Health Or Medicine GPT-OSS Model (22 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 22 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~14.9B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 22 |
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
- **Systematic Reduction**: Reduced from 32 to 22 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 68.8% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 22 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 22 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-14.9b-specialized-health_or_medicine-pruned-moe-only-22-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-14.9b-specialized-health_or_medicine-pruned-moe-only-22-experts")

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
    "AmanPriyanshu/gpt-oss-14.9b-specialized-health_or_medicine-pruned-moe-only-22-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-14.9b-specialized-health_or_medicine-pruned-moe-only-22-experts")

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
<|channel|>analysis<|message|>Need concise answer.<|end|><|start|>assistant<|channel|>final<|message|>The human heart performs three core functions that keep the body alive and functioning:

| Function | What it does | How it works |
|----------|--------------|--------------|
| **Pumping** | Moves blood throughout the body | The left ventricle contracts to eject oxygen‑rich blood into the aorta; the right ventricle pumps oxygen‑poor blood into the pulmonary artery. |
| **Circulation** | Delivers oxygen, nutrients, hormones, and removes waste | Blood travels through arteries to tissues, returns via veins, and is filtered by the lungs and kidneys. |
| **Electrical regulation** | Generates and coordinates the heartbeat | The sinoatrial (SA) node initiates the impulse, the atrioventricular (AV) node delays it, and the Purkinje‑myocardial network conducts it, ensuring synchronized contraction. |

Together, these functions maintain blood pressure, tissue perfusion, and the body’s overall homeostasis.<|return|>
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need concise explanation.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – the key differences**

| Feature | Bacteria | Viruses |
|--------|----------|--------|
| **Size** | Microscopic, 0.2–2 µm (visible with a light microscope) | 20–300 nm (too small for light microscopy; need electron microscopy) |
| **Structure** | Complex, single‑cell organisms with a cell membrane (or wall), cytoplasm, nucleus‑like DNA/RNA, and organelles (e.g., ribosomes). | Simple: a nucleic acid core (DNA or RNA) surrounded by a protein coat (capsid); some have a lipid envelope. No cellular organelles. |
| **Life cycle** | Independent life form: can grow, divide, and reproduce on their own. | Not a living organism by itself; must infect a host cell and hijack its machinery to replicate. |
| **Replication** | Cell division (mitotic or bacterial division). | Viral replication uses host cell enzymes; can be rapid and produce many copies in a single cycle. |
| **Metabolism** | Metabolic pathways (photosynthesis, respiration, fermentation). | No metabolism; rely entirely on host cell’s metabolic machinery. |
| **Genetic material** | DNA (most) or RNA (rare). | DNA or RNA (single or double stranded). |
| **Treatment** | Antibiotics (target cell wall, protein synthesis, DNA replication, etc.). | Antiviral drugs (target viral enzymes or entry), vaccines, and immune responses. |
| **Infection mechanism** | Can colonize surfaces, food, water, or host tissues; may be harmless or pathogenic. | Must bind to a specific receptor on a host cell, enter, and replicate. |
| **Evolution** | Rapid mutation and horizontal gene transfer (plasmids, phages). | High mutation rates, especially in RNA viruses; recombination and recombination events. |
| **Examples** | *Staphylococcus aureus*, *E. coli*, *Bacillus subtilis*. | Influenza, HIV, SARS‑CoV‑2, measles, hepatitis B. |

**Bottom line:**  
Bacteria are true cells that can live and reproduce on their own, whereas viruses are essentially genetic packages that need a host cell to make copies of themselves. This fundamental difference shapes how we diagnose, treat, and prevent infections caused by each.<|return|>
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a group of metabolic disorders characterized by chronically high blood glucose (hyperglycemia).  The two most common types are type 1 (autoimmune β‑cell destruction) and type 2 (insulin resistance with relative insulin deficiency).  Gestational diabetes occurs during pregnancy.  Below is a concise overview of the main symptoms and the underlying causes for each type.

---

## 1.  Symptoms

| Symptom | Typical Onset | Why It Happens |
|---------|---------------|----------------|
| **Polyuria** (excessive urination) | Early | Glucose spills into urine when blood glucose exceeds renal threshold → osmotic diuresis |
| **Polydipsia** (excessive thirst) | Early | Loss of fluid through urine + osmotic effect on kidneys |
| **Polyphagia** (increased hunger) | Early | Cells cannot use glucose → perceived energy deficit |
| **Weight loss** (especially in type 1) | Early | Body breaks down fat & muscle for energy |
| **Fatigue** | Early | Poor cellular glucose uptake → low energy |
| **Blurred vision** | Early–mid | Hyperglycemia causes osmotic shifts in the lens |
| **Slow‑healing wounds** | Mid | Impaired leukocyte function & microvascular disease |
| **Recurrent infections** (urinary, skin, oral) | Mid | Hyperglycemia impairs immune function |
| **Peripheral neuropathy** (tingling, numbness) | Late | Chronic microvascular damage to nerves |
| **Retinopathy** (vision loss) | Late | Microvascular damage to retinal vessels |
| **Kidney disease** (proteinuria, edema) | Late | Microvascular damage to glomeruli |
| **Foot ulcers / Charcot foot** | Late | Neuropathy + vascular disease |

> **Note:** In type 2 diabetes, many people are asymptomatic for years; symptoms often appear only after significant hyperglycemia or complications develop.

---

## 2.  Causes

| Type | Primary Cause | Key Risk Factors |
|------|---------------|-----------------|
| **Type 1** | Autoimmune destruction of pancreatic β‑cells → absolute insulin deficiency | • Genetic predisposition (HLA‑DR, HLA‑DQ) <br>• Environmental triggers (viral infections, early cow‑milk exposure) <br>• Male sex,
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
