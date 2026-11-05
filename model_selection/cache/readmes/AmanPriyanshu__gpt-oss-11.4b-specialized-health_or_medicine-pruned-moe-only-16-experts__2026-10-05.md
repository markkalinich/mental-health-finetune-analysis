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

# Health Or Medicine GPT-OSS Model (16 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 16 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~11.4B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 16 |
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
- **Systematic Reduction**: Reduced from 32 to 16 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 50.0% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 16 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 16 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-11.4b-specialized-health_or_medicine-pruned-moe-only-16-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-11.4b-specialized-health_or_medicine-pruned-moe-only-16-experts")

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
    "AmanPriyanshu/gpt-oss-11.4b-specialized-health_or_medicine-pruned-moe-only-16-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-11.4b-specialized-health_or_medicine-pruned-moe-only-16-experts")

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
<|channel|>analysis<|message|>Need to answer: main functions: pumping blood, maintaining circulation, delivering oxygen/nutrients, removing waste, regulating blood pressure, pumping blood to body, pumping blood to lungs, electrical conduction, etc.<|end|><|start|>assistant<|channel|>final<|message|>The human heart is a highly specialized organ whose primary purpose is to keep the body supplied with blood.  Its main functions can be grouped into three broad categories:

| **1. Pumping (Mechanical Function)** | **What it does** | **Why it matters** |
|---|---|---|
| **Systolic contraction** | The left ventricle contracts to eject oxygen‑rich blood into the systemic circulation (aorta). | Del delivers oxygen, nutrients, and hormones to every cell in the body. |
| **Diastolic relaxation** | The heart relaxes, allowing the chambers to fill with blood. | Ensures a steady supply of blood each heartbeat. |
| **Pulmonary circulation** | The right ventricle pumps de‑oxygenated blood to the lungs via the pulmonary artery. | Enables gas exchange (O₂ uptake, CO₂ removal). |

| **2. Electrical Coordination (Conduction System)** | **What it does** | **Why it matters** |
|---|---|---|
| **Initiation of rhythm** | The sino‑atrial (SA) node generates the heartbeat. | Sets the heart’s own pacemaker. |
| **Propagation of impulses** | Atrioventricular (AV) node, bundle branches, and Purkinje fibers conduct the signal. | Guarantees synchronized contraction of atria and ventricles. |
| **Regulation of rate** | Autonomic nervous system (sym‑/parasym) and hormonal signals adjust heart rate. | Matches blood flow to metabolic demands. |

| **3. Regulation of Blood Pressure & Volume (Autoregulation)** | **What it does** | **Why it matters** |
|---|---|---|
| **Pressure generation** | The force of ventricular contraction creates arterial pressure. | Maintains adequate perfusion pressure for tissues. |
| **Volume control** | Frank‑Starling relationship: preload (venous return) → stroke volume. | Allows the heart to adapt to changes in blood volume (exercise, posture, fluid status). |
| **Baroreceptor reflexes** | Sensors in aorta and carotid arteries adjust heart rate and vascular tone. | Keeps blood pressure stable during changes in posture or activity. |

---

### In short
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need explain differences: size, structure, replication, genetics, etc.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – The Key Differences**

| Feature | Bacteria | Viruses |
|---|---|---|
| **Basic definition** | Single‑cell, self‑living organisms (microorganisms) that can grow and reproduce on their own. | Particles (viruses) that are not living cells; they are essentially “packages” of genetic material surrounded by a protein coat (and sometimes a lipid envelope). |
| **Size** | 1 µm – 10 µm (roughly 10‑100 ×  the size of a virus). | 0.1 µm – 0.5 µm (about 100‑200 × smaller). |
| **Structure** | Complex: cell wall, plasma membrane, cytoplasm, ribosomes, DNA (often in a plasmid + chromosome). | Very simple: nucleic acid (DNA or RNA, single or double strand), protein coat (capsid), sometimes a lipid envelope. No organelles, no ribosomes. |
| **Genetic material** | DNA (most bacteria) – usually a single circular chromosome, sometimes plasmids. | DNA or RNA (single‑ or double‑strand). |
| **Replication** | Autonomous: bacteria divide by binary fission (cell division) using their own enzymes and ribosomes. | Dependent on the host cell: they hij‑take the host’s replication machinery to copy their genome and produce new particles. |
| **Energy source** | Metabolic pathways (photosynthesis, respiration, fermentation, etc.) to generate ATP. | No metabolism of their own; they rely on the host cell’s energy. |
| **Life cycle** | Continuous growth: a single bacterium can multiply into a colony in hours. | Episubstance: a virus infects a cell → replication → assembly → release (lytic or lysogenic). |
| **Infection mechanism** | Bacteria can attach to host cells, secrete toxins, or invade tissues. | Viruses bind to specific receptors on host cells, enter the cell, and use the host’s machinery to replicate. |
| **Immune response** | Recognized by innate and adaptive immunity; many bacteria are phagocytosed by macrophages. | Recognized by innate (interferons, NK cells) and adaptive immunity (antibodies, cytotoxic T cells
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a chronic metabolic disorder that occurs when the body cannot regulate blood glucose (sugar) levels properly. The two most common types are:

| Type | Key Features |
|------|--------------|
| **Type 1 (T1D)** | Autoimmune destruction of insulin‑producing β‑cells in the pancreas. |
| **Type 2 (T2D)** | Insulin resistance in tissues (muscle, fat, liver) and often inadequate insulin production. |

---

## 1.  Symptoms (Signs & Symptoms)

| Symptom | Why It Happens | Typical Onset |
|---------|----------------|--------------|
| **Polyuria** (excessive urination) | High glucose in the kidneys → osmotic diuresis. | Often first sign in both types. |
| **Polydipsia** (excessive thirst) | Low blood glucose triggers thirst; later, high glucose can impair thirst regulation. | Early in T1D; later in T2D. |
| **Polyphagia** (excessive hunger) | Body tries to get more glucose; also due to insulin resistance. | Early in T1D; later in T2D. |
| **Weight loss** | In T1D, rapid loss due to catabolism; in T2D, often weight gain or obesity. | Early in T1D; variable in T2D. |
| **Fatigue / Weakness** | Energy loss from inefficient glucose utilization. | Early in both types. |
| **Poor wound healing** | Hyperglycemia impairs immune function and collagen synthesis. | Often noticed after months. |
| **Increased infections** | Impaired neutrophil function, poor circulation. | Chronic. |
| **Blurred vision** | Osmotic shifts in the eye’s lens. | Early in both types. |
| **Peripheral neuropathy** | Long‑term hyperglycemia damages nerves. | Years of uncontrolled diabetes. |
| **Retinopathy** | Damage to retinal blood vessels. | Years of uncontrolled diabetes. |
| **Kidney disease (nephropathy)** | Glomerular damage from high glucose. | Years of uncontrolled diabetes. |
| **Cardiovascular disease** | Atherosclerosis accelerated by hyperglycemia. | Years of uncontrolled diabetes. |

> **Note:** In many people, especially with type 2 diabetes, the first few years may
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
