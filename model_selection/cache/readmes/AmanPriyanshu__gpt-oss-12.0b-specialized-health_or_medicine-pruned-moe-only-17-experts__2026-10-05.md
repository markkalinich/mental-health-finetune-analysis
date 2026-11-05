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

# Health Or Medicine GPT-OSS Model (17 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 17 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~12.0B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 17 |
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
- **Systematic Reduction**: Reduced from 32 to 17 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 53.1% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 17 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 17 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-12.0b-specialized-health_or_medicine-pruned-moe-only-17-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-12.0b-specialized-health_or_medicine-pruned-moe-only-17-experts")

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
    "AmanPriyanshu/gpt-oss-12.0b-specialized-health_or_medicine-pruned-moe-only-17-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-12.0b-specialized-health_or_medicine-pruned-moe-only-17-experts")

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
<|channel|>analysis<|message|>Need answer.<|end|><|start|>assistant<|channel|>final<|message|>The human heart is a muscular organ that performs several essential functions to keep the body alive and functioning. Its main roles can be grouped into three broad categories:

| **Primary Function** | **What It Does** | **Why It Matters** |
|---------------------|----------------|----------------|
| **Pumping Blood** | The heart contracts (systole) and relaxes (diastole) to push blood through the circulatory system. | Keeps oxygen, nutrients, hormones, and waste products delivered to and removed from every cell. |
| **Maintaining Blood Pressure** | By regulating the force and rate of contraction, the heart sets the pressure needed to move blood against resistance in the vessels. | Keeps tissues perfused and prevents shock or organ failure. |
| **Regulating Blood Flow** | The heart’s rhythm and contractility are adjusted by the nervous system and hormones to match the body’s needs (e.g., exercise, rest, stress). | Allows the body to respond quickly to changing demands. |

### How the Heart Performs These Functions

1. **Electrical Conduction System**  
   - **Sinoatrial (SA) node**: natural pacemaker that initiates each heartbeat.  
   - **Atrioventricular (AV) node**: delays conduction to allow atria to finish contracting before ventricles.  
   - **Bundle of His → Purkinje fibers**: conduct impulses through ventricles, coordinating ventricular contraction.

2. **Cardiac Muscle (Myocardium)**  
   - **Contractile fibers**: generate force to pump blood.  
   - **Intercalated discs**: specialized junctions that allow rapid spread of electrical impulses and mechanical coupling between cells.

3. **Valvular System**  
   - **Aortic, pulmonary, mitral, and tricuspid valves**: prevent back‑flow of blood, ensuring unidirectional flow from chambers to major vessels.

4. **Autonomic Regulation**  
   - **Sympathetic nervous system**: increases heart rate and contractility (fight‑or‑flight).  
   - **Parasympathetic (vagal) tone**: slows heart rate (rest, relaxation).  
   - **Hormonal influences**: catecholamines, angiotensin II, atrial natriuretic peptide, etc., fine‑tune cardiac output.

5. **Metabolic Support**  
   - **Coronary circulation**: supplies
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need explain differences.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – the big differences**

| Feature | Bacteria | Viruses |
|---|---|---|
| **Basic nature** | Single‑cell, living organisms (prokaryotes) | Particles that are not living; they are just a package of genetic material surrounded by a coat (capsid) and sometimes a lipid envelope |
| **Size** | 1 µm to 10 µm (about 1000‑10,000 nm) | 0.25 µm to 0.5 µm (250‑500 nm) – roughly 100‑200 nm for most |
| **Structure** | Cell wall, plasma membrane, cytoplasm, ribosomes, DNA (often circular) | Genome (DNA or RNA, single or double strand), capsid, sometimes envelope; no internal organelles |
| **Reproduction** | Cell division (mitotic‑like) – one cell splits into two, then two into four, etc. | Replication inside a host cell: the virus injects its genome, hijaxes the host’s machinery to make copies of its genome and proteins, then assembles new particles |
| **Genetic material** | DNA (most) | DNA or RNA (single‑ or double‑strand) |
| **Energy source** | Metabolism – can produce energy from nutrients (photosynthesis, respiration, fermentation) | No metabolism; relies entirely on the host cell’s enzymes and energy |
| **Life cycle** | Can survive outside hosts (in soil, water, on surfaces) | Usually need a living host cell to produce new copies; many are short‑lived outside a host |
| **Infection mechanism** | Attach to host cells, penetrate, grow, and release new cells (often by lysis or budding) | Attach to host cells, inject genome, replicate, assemble, and exit (lysis, budding, or exocytosis) |
| **Immune response** | Recognized by innate and adaptive immunity; can be targeted by antibiotics, phage therapy, etc. | Recognized by innate and adaptive immunity; targeted by antiviral drugs, vaccines, monoclonal antibodies |
| **Treatment** | Antibiotics (target cell wall, protein synthesis, DNA replication, etc.) | Antivirals (target viral enzymes, entry, replication, etc.) |
| **Examples** | *Escherichia coli*,
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a chronic metabolic disorder in which the body cannot regulate blood glucose properly.  The two most common types are:

| Type | Main cause | Typical symptoms |
|------|------------|-----------------|
| **Type 1** (juvenile‑onset) | Autoimmune destruction of insulin‑producing β‑cells in the pancreas → little or no insulin | • Sudely rapid weight loss<br>• Polyphagia (constant hunger)<br>• Poluria (fre frequent urination)<br>• Polyphoria (fre frequent thirst)<br>• Fatigue, weakness<br>• Frequent infections (especially in the skin, mouth, and urinary tract)<br>• Delayed wound healing |
| **Type 2** (adult‑onset) | Insulin resistance in peripheral tissues + relative insulin deficiency | • Gradual weight gain or obesity (especially abdominal)<br>• Polyphagia, poluria, polyphoria (often milder than type 1)<br>• Fatigue, blurred vision, slow wound healing<br>• Occasional tingling or numbness in extremities (early neuropathy)<br>• Dark, itchy skin (acanthosis nigricans) in some cases |

---

### Common symptoms (present in both types)

1. **Polyphagia** – constant, unrelating hunger.  
2. **Poluria** – increased frequency and volume of urination.  
3. **Polydipsia** – excessive thirst.  
4. **Weight changes** – rapid loss in type 1; gradual gain in type 2.  
5. **Fatigue and weakness** – due to cells not getting glucose.  
6. **Blurred vision** – hyperglycemia causes fluid shifts in the eye.  
7. **Infections** – especially skin, mouth, and urinary tract.  
8. **Delayed wound healing** – impaired blood flow and immune function.  
9. **Peripheral neuropathy** – tingling, numbness, or pain in hands/feet.  
10. **Anemia** – low red‑cell count (especially in type 1).  

---

### Causes

| Factor | How it contributes to diabetes |
|--------|------------------------------|
| **Autoimmune attack** (type 1) | The immune system mistakenly targets β‑cells → loss of insulin production. |
| **Insulin resistance** (type 2
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
