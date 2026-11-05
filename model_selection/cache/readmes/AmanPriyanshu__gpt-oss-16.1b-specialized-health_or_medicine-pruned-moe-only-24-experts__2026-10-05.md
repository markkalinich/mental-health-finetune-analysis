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

# Health Or Medicine GPT-OSS Model (24 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 24 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~16.1B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 24 |
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
- **Systematic Reduction**: Reduced from 32 to 24 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 75.0% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 24 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 24 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-16.1b-specialized-health_or_medicine-pruned-moe-only-24-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-16.1b-specialized-health_or_medicine-pruned-moe-only-24-experts")

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
    "AmanPriyanshu/gpt-oss-16.1b-specialized-health_or_medicine-pruned-moe-only-24-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-16.1b-specialized-health_or_medicine-pruned-moe-only-24-experts")

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
| **Pumping blood** | Moves oxygen‑rich blood from the body to the lungs and back, and delivers oxygenated blood to tissues. | The heart’s chambers contract in a coordinated rhythm (systole) and relax (diastole), creating pressure gradients that drive blood flow. |
| **Maintaining circulation** | Keeps blood pressure and flow steady so organs receive the nutrients and oxygen they need. | The heart’s electrical conduction system (SA node, AV node, bundle branches, Purkinje fibers) ensures timely, synchronized contractions that sustain a steady cardiac output. |
| **Regulating blood volume and pressure** | Adjusts the amount of blood pumped per beat (stroke volume) and overall cardiac output to match the body’s metabolic demands. | Reflexes (baroreceptor, chemoreceptor) and hormonal signals (e.g., adrenaline, angiotensin) modify heart rate, contractility, and vascular tone. |

Together, these functions allow the heart to circulate blood continuously, delivering oxygen and nutrients while removing waste products, thereby sustaining life.<|return|>
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
| **Size** | 0.5–5 µm (micrometers) – visible under a light microscope. | 20–300 nm (nanometers) – require an electron microscope to see. |
| **Genetic material** | DNA or RNA, usually circular plasmids plus a chromosome; can be single‑ or double‑stranded. | DNA or RNA, single‑ or double‑stranded; always encapsulated in a capsid. |
| **Reproduction** | Binary fission (cell division) – they grow and split into two identical daughter cells. | Must hijack a host cell’s machinery to replicate their genome and assemble new virions. |
| **Metabolism** | Autonomous – can metabolize nutrients, produce energy, and grow independently. | No metabolism of their own – rely entirely on the host cell’s enzymes and energy. |
| **Life cycle** | Can live freely in many environments (soil, water, body). | Only survive outside a host for a short time; must infect a host cell to replicate. |
| **Treatment** | Antibiotics (target cell wall, ribosomes, DNA replication, etc.) can kill or inhibit them. | Antiviral drugs target specific viral enzymes or entry steps; antibiotics are ineffective. |
| **Disease mechanisms** | Direct damage (toxins, enzymes), immune response to bacterial components, or secondary infections. | Direct damage from viral replication, immune response to viral antigens, or immune evasion strategies. |
| **Examples** | *Escherichia coli*, *Staphylococcus aureus*, *Mycobacterium tuberculosis*. | Influenza virus, HIV, SARS‑CoV‑2, HPV. |

**Bottom line:**  
Bacteria are living, self‑sustaining cells that can grow and divide on their own, whereas viruses are non‑living particles that need a host cell to replicate. This fundamental difference shapes how they cause disease, how they’re treated, and how they’re studied.<|return|>
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a group of metabolic disorders characterized by chronic hyperglycemia (high blood sugar). The two most common types are type 1 and type 2, but there are other forms (gestational, monogenic, etc.). Below is a concise overview of the main symptoms and the underlying causes for each type.

---

## 1. Type 1 Diabetes (T1D)

| **Symptoms** | **Typical Onset** | **Underlying Cause** |
|--------------|------------------|----------------------|
| • Polyuria (frequent urination) | Childhood or adolescence | Autoimmune destruction of pancreatic β‑cells → insulin deficiency |
| • Polydipsia (excessive thirst) | | |
| • Polyphagia (increased hunger) | | |
| • Unintentional weight loss | | |
| • Fatigue, weakness | | |
| • Blurred vision | | |
| • Slow‑healing cuts or infections | | |
| • Ketoacidosis (in severe cases) – nausea, vomiting, abdominal pain, fruity breath | | |
| • Rapid heart rate, dehydration | | |

**Key Points**

- The immune system mistakenly targets insulin‑producing β‑cells in the pancreas.
- Genetic predisposition (HLA genes) + environmental triggers (viruses, diet) are thought to initiate the autoimmune attack.
- Once β‑cells are destroyed, the body cannot produce insulin, so exogenous insulin therapy is required.

---

## 2. Type 2 Diabetes (T2D)

| **Symptoms** | **Typical Onset** | **Underlying Cause** |
|--------------|------------------|----------------------|
| • Polyuria, polydipsia, polyphagia | Often adult‑onset, but increasingly seen in adolescents | Insulin resistance + relative insulin deficiency |
| • Fatigue, blurred vision | | |
| • Slow‑healing wounds, frequent infections | | |
| • Peripheral neuropathy (tingling, numbness) | | |
| • Vision changes, eye problems (retinopathy) | | |
| • Cardiovascular symptoms (chest pain, shortness of breath) | | |
| • No obvious weight loss; may be overweight/obese | | |

**Key Points**

- **Insulin resistance**: cells (especially muscle, liver, fat) become less responsive to insulin.
- **β‑cell dysfunction**: the pancreas cannot
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
