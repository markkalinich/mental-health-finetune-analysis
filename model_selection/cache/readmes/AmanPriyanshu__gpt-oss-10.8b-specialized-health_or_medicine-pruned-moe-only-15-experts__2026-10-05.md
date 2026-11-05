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

# Health Or Medicine GPT-OSS Model (15 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 15 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~10.8B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 15 |
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
- **Systematic Reduction**: Reduced from 32 to 15 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 46.9% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 15 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 15 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-10.8b-specialized-health_or_medicine-pruned-moe-only-15-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-10.8b-specialized-health_or_medicine-pruned-moe-only-15-experts")

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
    "AmanPriyanshu/gpt-oss-10.8b-specialized-health_or_medicine-pruned-moe-only-15-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-10.8b-specialized-health_or_medicine-pruned-moe-only-15-experts")

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
<|channel|>analysis<|message|>Need to answer: main functions: pumping blood, maintaining circulation, delivering oxygen/nutrients, removing waste, regulating blood pressure, electrical conduction, etc.<|end|><|start|>assistant<|channel|>final<|message|>The human heart is a muscular organ that performs several essential functions to keep the body alive and functioning. Its primary roles can be grouped into three major categories:

| **1. Pumping Blood** | **2. Regulating Blood Flow** | **3. Maintaining Electrical Coordination** |
|---|---|---|
| • **Cardiac Output** – The heart continuously pumps blood into the systemic and pulmonary circulations, delivering oxygen and nutrients to tissues and removing waste products. | • **Blood Pressure Control** – By adjusting stroke volume and heart rate, the heart helps maintain arterial pressure within a range that supports organ perfusion. | • **Electrical Conduction System** – The sino‑atrial (SA) node, atrioventricular (AV) node, bundle branches, and Purkinje fibers coordinate the heartbeat, ensuring that the atria and ventricles contract in a timely, synchronized fashion. |
| • **Stroke Volume** – The amount of blood ejected per beat (≈ 250 mL in a resting adult). | • **Heart Rate** – Beats per minute (≈ 60–70 bpm at rest) that can be modulated by the autonomic nervous system and hormones. | • **Concordance** – The heart’s ability to contract against the resistance of the blood vessels (arterial compliance). |
| • **Cardiac Output** – Stroke volume × heart rate (≈ 5 L/min in a resting adult). | • **Vascular Resistance** – The heart responds to changes in peripheral resistance (e.g., vasoconstriction or vasodilation). | • **Pacemaker Activity** – The SA node initiates the impulse; the AV node delays it to allow atrial filling before ventricular contraction. |

### Key Functions in Detail

1. **P pumping blood (Cardiac Output)**
   * **Systemic circulation** – Oxygenated blood is pumped from the left ventricle into the aorta, supplying all body tissues.
   * **Pulmonary circulation** – De‑oxygenated blood is pumped from the right ventricle into the lungs for gas exchange.

2. **Regulating blood flow**
   * **Autoregulation** – The heart can adjust its output to match the metabolic demands of organs (e.g., during exercise, the heart rate
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need explain differences: size, complexity, replication, genetics, etc.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – The Key Differences**

| Feature | Bacteria | Viruses |
|---|---|---|
| **Cellular nature** | True cells – have a distinct cytoplasm, membrane, and organelles (e.g., ribosomes, mitochondria in some). | No cell structure; they are just genetic material (DNA or RNA) surrounded by a protein coat (capsid) and sometimes a lipid envelope. |
| **Size** | Microscopic but larger: 1–10 µm (≈ 1000–10 000 nm). | Tiny: 0.1–100 nm (≈ 100–1000 nm). |
| **Genetic material** | Usually a single‑stranded or double‑stranded DNA genome (≈ 1–10 M bp). | DNA or RNA genome (≈ 0.1–10 M bp). |
| **Replication** | Can replicate autonomically inside a cell: they grow, divide (bacterial cell division), and can produce many copies of themselves. | Must hij‑take a host cell’s machinery to replicate; they cannot divide on their own. |
| **Metabolism** | Have metabolic pathways: they can oxidize, ferment, photosynthesize, etc. | No metabolism; they rely entirely on the host cell’s metabolic machinery. |
| **Structure** | Cell wall (peptidoglycan in Gram‑positive, peptidoglycan + outer membrane in Gram‑negative), cytoplasmic membrane, ribosomes, sometimes flagella or pili. | Capsid (protein shell) and sometimes a lipid envelope; no ribosomes or other organelles. |
| **Life cycle** | Simple: growth → division → death. | Complex: attachment → entry → replication → assembly → release (lytic or latent). |
| **Infection mechanism** | Can invade tissues, produce toxins, or compete for nutrients. | Attach to specific receptors, inject genetic material, commandeer host cell. |
| **Immune response** | Recognized by innate and adaptive immunity; can be cleared by phagocytosis, antibiotics, etc. | Recognized by innate and adaptive immunity; often evade immune detection by hiding in host genome or altering antigens. |
| **Treatment** | Antibiotics (target cell wall synthesis, protein synthesis, etc.). |
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a chronic metabolic disorder that occurs when the body cannot use glucose (sugar) properly.  The two most common types are type 1 (autoimmune destruction of insulin‑producing β‑cells) and type 2 (insulin resistance with eventual β‑cell failure).  Below is a quick‑look guide to the symptoms and the underlying causes for each type.

---

## 1.  Symptoms of Diabetes

| Symptom | Why it happens | How it shows in everyday life |
|---|---|---|
| **Polyuria** (excessive urination) | High blood glucose → kidneys try to flush it out | Frequent trips to the bathroom, especially at night |
| **Polydipsia** (excessive thirst) | Osmotic effect of glucose + low insulin → brain signals “thirst” | Constant feeling of thirst, even after drinking |
| **Polyphagia** (excessive hunger) | Low insulin → cells think you’re starved | Eating more than usual, cravings for sugary foods |
| **Weight loss** (especially type 1) | Rapid glucose loss through urine & poor appetite | Noticeable weight drop despite normal or increased food intake |
| **Fatigue / weakness** | Cells can’t use glucose → energy deficit | Feeling tired, sluggish, or “low‑energy” |
| **Blurred vision** | Fluctuating blood sugar changes fluid balance in the eye | Vision changes, especially after meals or at night |
| **Slow wound healing** | Poor circulation & immune function | Cuts or sores that take weeks to heal |
| **Increased infections** | Immune system is weakened | Frequent col col, thrush, or skin infections |
| **Peripheral neuropathy** | High glucose damages nerves | Tingling, numbness, or burning in feet and hands |
| **Gangrene or amputations** | Severe peripheral vascular disease | Rare, but can lead to tissue death in extremities |

> **Note**: In type 1 diabetes, symptoms often appear suddenly and can be severe. In type 2, symptoms may develop gradually and can be subtle, especially in the early stages.

---

## 2.  Causes of Diabetes

### Type 1 Diabetes (T1D)

| Cause | Mechanism | Risk factors |
|---|---|---|
| **Autoimmune destruction of β‑cells** | The immune system mistakenly attacks
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
