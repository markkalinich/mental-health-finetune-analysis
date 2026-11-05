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

# Health Or Medicine GPT-OSS Model (28 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 28 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~18.5B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 28 |
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
- **Systematic Reduction**: Reduced from 32 to 28 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 87.5% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 28 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 28 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-18.5b-specialized-health_or_medicine-pruned-moe-only-28-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-18.5b-specialized-health_or_medicine-pruned-moe-only-28-experts")

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
    "AmanPriyanshu/gpt-oss-18.5b-specialized-health_or_medicine-pruned-moe-only-28-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-18.5b-specialized-health_or_medicine-pruned-moe-only-28-experts")

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
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>The human heart is a muscular pump that performs several essential functions to keep blood circulating throughout the body. Its main functions can be grouped into four key categories:

| Function | What it does | Why it matters |
|----------|--------------|----------------|
| **Pumping (Circulation)** | Moves blood through the body by contracting (systole) and relaxing (diastole). | Delivers oxygen, nutrients, hormones, and removes waste products. |
| **Pressure Generation** | Generates the pressure needed to propel blood through arteries, capillaries, and veins. | Maintains adequate blood flow against resistance in the vascular system. |
| **Electrical Conduction** | Coordinates the timing of contractions via the sino‑atrial (SA) node, atrioventricular (AV) node, bundle branches, and Purkinje fibers. | Ensures that the atria and ventricles contract in a synchronized, efficient rhythm. |
| **Regulation of Blood Volume & Composition** | Works with the kidneys and endocrine system to adjust blood volume, electrolyte balance, and blood pressure. | Keeps blood pressure stable and prevents dehydration or fluid overload. |

### How the Heart Performs These Functions

1. **Anatomical Structure**  
   - **Four chambers**: right atrium, right ventricle, left atrium, left ventricle.  
   - **Valves** (tricuspid, pulmonary, mitral, aortic) prevent back‑flow.  
   - **Myocardium** (heart muscle) provides the force for pumping.

2. **Electrical Cycle**  
   - **SA node** → initiates impulse → atrial contraction.  
   - **AV node** → delays impulse → ventricular contraction.  
   - **Bundle of His → Purkinje fibers** → rapid conduction to ventricles.

3. **Hemodynamic Cycle**  
   - **Right side**: deoxygenated blood → lungs (pulmonary circulation).  
   - **Left side**: oxygenated blood → systemic circulation (body tissues).

4. **Autoregulation & Reflexes**  
   - **Baroreceptor reflex** (in carotid sinus & aortic arch) adjusts heart rate and contractility.  
   - **Chemoreceptor reflex** (in carotid bodies) responds to CO₂/O₂ levels.  
   - **Neurohumoral control** (sympathetic/parasympathetic, hormones like adrenaline
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need concise explanation.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – the key differences**

| Feature | Bacteria | Viruses |
|--------|----------|---------|
| **Cellular structure** | True cells – have a cell wall, cytoplasm, ribosomes, and a plasma membrane. | Not cells – just a protein coat (capsid) surrounding genetic material; no membrane or organelles. |
| **Size** | 0.5–10 µm (micrometers). | 20–300 nm (nanometers). |
| **Genetic material** | DNA or RNA, usually circular (plasmids possible). | DNA or RNA, single‑stranded or double‑stranded, but never both. |
| **Reproduction** | Binary fission (autonomous, self‑replicating). | Must infect a host cell and hijack its machinery to replicate. |
| **Metabolism** | Can be autotrophic or heterotrophic; many can generate energy (e.g., photosynthesis, respiration). | No metabolism of their own; rely entirely on host cell processes. |
| **Living status** | Considered living organisms. | Debated; many scientists treat them as “non‑living” because they lack metabolism and reproduction outside a host. |
| **Pathogenic mechanisms** | Secrete toxins, invade tissues, trigger immune responses. | Attach to specific host receptors, inject genetic material, commandeer host replication. |
| **Treatment** | Antibiotics (target cell wall, protein synthesis, etc.). | Antiviral drugs (target viral enzymes or entry), vaccines; antibiotics ineffective. |
| **Examples** | *Escherichia coli*, *Staphylococcus aureus*, *Mycobacterium tuberculosis*. | Influenza virus, HIV, SARS‑CoV‑2, HPV. |

**Bottom line:**  
Bacteria are self‑sufficient, cellular organisms that can grow and divide on their own. Viruses are much smaller, lack cellular machinery, and can only replicate by taking over a host cell’s machinery. This fundamental difference shapes how we diagnose, treat, and prevent infections caused by each.<|return|>
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a group of metabolic disorders characterized by chronic hyperglycemia (high blood sugar). The two most common types are type 1 and type 2, but there are other forms (gestational, monogenic, etc.). Below is a concise overview of the main symptoms, causes, and key differences between the types.

---

## 1. Symptoms

| Symptom | Typical Onset | What It Means |
|---------|---------------|---------------|
| **Polyuria** (frequent urination) | Early | Kidneys excrete excess glucose, pulling water out of the body. |
| **Polydipsia** (excessive thirst) | Early | Dehydration from fluid loss. |
| **Polyphagia** (increased hunger) | Early | Cells can’t use glucose, so the body signals for more food. |
| **Weight loss** (especially in type 1) | Early | Body breaks down fat and muscle for energy. |
| **Fatigue / weakness** | Early | Energy production is impaired. |
| **Blurred vision** | Early | High glucose causes fluid shifts in the eye lens. |
| **Slow‑healing cuts or infections** | Early‑mid | Poor circulation and immune function. |
| **Numbness or tingling in extremities** | Mid‑to‑late | Peripheral neuropathy from chronic hyperglycemia. |
| **Skin changes** (dry, itchy, fungal infections) | Mid‑to‑late | Hyperglycemia creates a favorable environment for microbes. |
| **Recurrent urinary tract or genital infections** | Mid‑to‑late | High glucose in urine or vaginal secretions promotes bacterial growth. |
| **Ketoacidosis (type 1, sometimes type 2)** | Acute | Severe hyperglycemia + lack of insulin → ketone production → nausea, vomiting, abdominal pain, fruity breath. |

> **Note:** Many people with type 2 diabetes are asymptomatic for years; routine screening is essential, especially if risk factors are present.

---

## 2. Causes & Risk Factors

| Type | Primary Cause | Key Risk Factors |
|------|---------------|------------------|
| **Type 1 Diabetes** | Autoimmune destruction of pancreatic β‑cells → insulin deficiency | • Genetic predisposition (HLA‑DR3/DR4) <br>• Early childhood onset <br>• Viral infections (e
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
