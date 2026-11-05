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

# Health Or Medicine GPT-OSS Model (25 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 25 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~16.7B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 25 |
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
- **Systematic Reduction**: Reduced from 32 to 25 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 78.1% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 25 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 25 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-16.7b-specialized-health_or_medicine-pruned-moe-only-25-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-16.7b-specialized-health_or_medicine-pruned-moe-only-25-experts")

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
    "AmanPriyanshu/gpt-oss-16.7b-specialized-health_or_medicine-pruned-moe-only-25-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-16.7b-specialized-health_or_medicine-pruned-moe-only-25-experts")

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
<|channel|>analysis<|message|>Need concise answer.<|end|><|start|>assistant<|channel|>final<|message|>The human heart is a muscular pump that performs three core functions:

| Function | What it does | How it works |
|----------|--------------|--------------|
| **Pumping blood** | Moves oxygen‑rich blood to tissues and returns oxygen‑poor blood to the lungs | The left ventricle contracts to send blood into the aorta; the right ventricle pumps to the pulmonary artery. |
| **Maintaining circulation** | Keeps blood flowing through the body’s network of arteries, capillaries, and veins | The heart’s rhythmic contractions create pressure gradients that drive blood through the circulatory system. |
| **Regulating blood pressure** | Controls the force and volume of blood flow | The heart’s contractility, heart rate, and the compliance of the vascular system together set arterial pressure. |

Together, these functions ensure that oxygen, nutrients, hormones, and waste products are delivered and removed efficiently throughout the body.<|return|>
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need concise explanation.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – the key differences**

| Feature | Bacteria | Viruses |
|--------|----------|---------|
| **Cellular structure** | True cells – have a cell membrane, cytoplasm, ribosomes, and a cell wall (in most). | Not cells – just a protein coat (capsid) surrounding genetic material; no membrane or organelles. |
| **Size** | 0.5–5 µm (micrometers). | 20–300 nm (nanometers). Bacteria are ~10–100× larger. |
| **Genetic material** | DNA (most) or RNA; usually a single circular chromosome, sometimes plasmids. | DNA or RNA, but never both. |
| **Reproduction** | Binary fission (a single cell splits into two). Requires nutrients and a suitable environment. | Must hijack a host cell’s machinery to replicate. No independent metabolism. |
| **Metabolism** | Can be autotrophic (photosynthetic, chemosynthetic) or heterotrophic. | No metabolism of their own. |
| **Life cycle** | Can grow, divide, and form colonies. | Infect a host cell, replicate, then exit (lysis or budding). |
| **Treatment** | Antibiotics target bacterial cell wall, protein synthesis, DNA replication, etc. | Antivirals target viral replication steps; vaccines are the main prevention. |
| **Disease mechanisms** | Direct damage (toxins, enzymes), immune response to bacterial components. | Direct damage from viral replication, immune response to viral proteins. |
| **Transmission** | Often via contact, food, water, vectors. | Often via droplets, direct contact, vectors, or bodily fluids. |
| **Examples** | *Escherichia coli*, *Staphylococcus aureus*, *Mycobacterium tuberculosis*. | Influenza virus, HIV, SARS‑CoV‑2, HPV. |

**Bottom line:**  
Bacteria are living, self‑sufficient cells that can grow and divide on their own. Viruses are non‑living particles that can only replicate inside a host cell, relying entirely on the host’s machinery. This fundamental difference shapes how they cause disease, how we diagnose them, and how we treat or prevent infections.<|return|>
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a group of metabolic disorders characterized by chronic hyperglycemia (high blood sugar). The two most common types are type 1 and type 2, but there are other forms (gestational, monogenic, etc.). Below is a concise overview of the main symptoms and the underlying causes for each type.

---

## 1. Symptoms of Diabetes

| Symptom | Typical Onset | Why It Happens |
|---------|---------------|----------------|
| **Polyuria** (frequent urination) | Early | Kidneys excrete excess glucose, pulling water out of the body. |
| **Polydipsia** (increased thirst) | Early | Dehydration from fluid loss triggers thirst. |
| **Polyphagia** (increased hunger) | Early | Cells can’t use glucose, so the body signals for more food. |
| **Weight loss** (especially in type 1) | Early | Body breaks down fat and muscle for energy. |
| **Fatigue / weakness** | Early | Energy isn’t being efficiently used. |
| **Blurred vision** | Early‑mid | High glucose causes fluid shifts in the lens. |
| **Slow‑healing cuts or infections** | Mid‑to‑late | Poor blood flow and immune function. |
| **Numbness or tingling in hands/feet** | Late | Chronic high glucose damages nerves (diabetic neuropathy). |
| **Red, swollen, or painful gums** | Late | Diabetes worsens gum disease. |
| **Recurrent urinary tract infections** | Late | High glucose in urine promotes bacterial growth. |
| **Skin changes (dry, itchy, fungal infections)** | Late | Poor circulation and immune changes. |

> **Note:** Many people with type 2 diabetes are asymptomatic for years; routine screening is essential, especially if risk factors are present.

---

## 2. Causes (Pathophysiology)

| Type | Primary Cause | Key Mechanisms |
|------|---------------|----------------|
| **Type 1 Diabetes** | Autoimmune destruction of pancreatic β‑cells | • Autoantibodies (GAD, IA‑2, ZnT8) target β‑cells.<br>• T‑cell mediated cytotoxicity.<br>• Result: Insulin deficiency → hyperglycemia. |
| **Type 2 Diabetes** | Insulin resistance + β‑cell dysfunction | • Obesity
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
