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

# Health Or Medicine GPT-OSS Model (32 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 32 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for health or medicine tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~20.9B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 32 |
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
- **Systematic Reduction**: Reduced from 32 to 32 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 100.0% of original expert parameters
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

By identifying experts that consistently activated for health or medicine tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 32 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 32 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-20.9b-specialized-health_or_medicine-pruned-moe-only-32-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-20.9b-specialized-health_or_medicine-pruned-moe-only-32-experts")

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
    "AmanPriyanshu/gpt-oss-20.9b-specialized-health_or_medicine-pruned-moe-only-32-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-20.9b-specialized-health_or_medicine-pruned-moe-only-32-experts")

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
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>The human heart is a muscular pump that performs several essential functions to keep the circulatory system working efficiently. Its main functions can be grouped into three broad categories:

| Function | What it does | Why it matters |
|----------|--------------|----------------|
| **Pumping blood** | The heart contracts (systole) and relaxes (diastole) in a coordinated rhythm, propelling blood through the body. | Keeps oxygen, nutrients, hormones, and waste products moving to and from tissues. |
| **Maintaining blood pressure** | By generating enough force during systole, the heart sets the pressure that drives blood through arteries, capillaries, and veins. | Adequate pressure is needed for capillary exchange and to ensure blood reaches all organs, especially the brain and kidneys. |
| **Regulating blood flow** | The heart’s rhythm and contractility can be adjusted by the autonomic nervous system and hormonal signals (e.g., adrenaline). | Allows the body to respond to changes in activity level, stress, or metabolic demand. |

### How the heart accomplishes these tasks

1. **Electrical conduction system**  
   - **Sinoatrial (SA) node**: “pacemaker” that initiates the heartbeat.  
   - **Atrioventricular (AV) node**: delays the impulse so the atria finish contracting before the ventricles.  
   - **Bundle of His → Purkinje fibers**: conduct the impulse rapidly to the ventricles, ensuring a coordinated contraction.

2. **Cardiac cycle**  
   - **Diastole**: atria and ventricles relax; the atrioventricular valves (mitral and tricuspid) open, allowing blood to fill the ventricles.  
   - **Systole**: ventricles contract; the semilunar valves (aortic and pulmonary) open, ejecting blood into the aorta and pulmonary artery.

3. **Pressure generation**  
   - **Left ventricle**: generates high pressure (~120 mm Hg systolic) to push blood into the systemic circulation.  
   - **Right ventricle**: generates lower pressure (~25 mm Hg systolic) to send blood to the lungs.

4. **Autoregulation**  
   - **Frank–Starling mechanism**: increased venous return stretches ventricular walls, leading to a stronger contraction.  
   - **Neural
```

---

### Example 2
**Question:** Explain the difference between bacteria and viruses.

**Response:**
```
<|channel|>analysis<|message|>Need concise explanation.<|end|><|start|>assistant<|channel|>final<|message|>**Bacteria vs. Viruses – the big differences**

| Feature | Bacteria | Viruses |
|---------|----------|---------|
| **Basic nature** | Living, single‑cell organisms (prokaryotes). | Non‑living particles; need a host cell to replicate. |
| **Size** | ~0.5–5 µm (visible under light microscope). | ~20–300 nm (visible only with electron microscope). |
| **Structure** | Cell wall, cytoplasm, ribosomes, DNA (circular or linear), sometimes plasmids. | Protein coat (capsid) surrounding a nucleic acid core (DNA or RNA). No metabolic machinery. |
| **Reproduction** | Binary fission (autonomous division). | Hijack host cell’s replication machinery to produce new virions. |
| **Metabolism** | Can be autotrophic or heterotrophic; can generate energy (e.g., via respiration, photosynthesis). | No metabolism of their own; rely entirely on host cell. |
| **Genetic material** | DNA (sometimes RNA). | DNA or RNA, but never both. |
| **Cellular components** | Membrane, ribosomes, enzymes, transporters. | Only capsid proteins and sometimes an envelope derived from host membrane. |
| **Response to antibiotics** | Many antibiotics target cell wall synthesis, protein synthesis, or DNA replication. | Antibiotics are ineffective; antiviral drugs target specific viral enzymes or entry steps. |
| **Disease mechanisms** | Can cause disease by toxin production, invasion, or immune activation. | Cause disease by destroying host cells, evading immunity, or triggering immune responses. |
| **Treatment** | Antibiotics, vaccines, phage therapy. | Antiviral drugs, vaccines, immune‑modulating therapies. |
| **Evolution** | Reproduce by mutation and horizontal gene transfer. | Rapid evolution via mutation, recombination, and reassortment. |

**Bottom line:**  
Bacteria are autonomous, living cells that can survive and reproduce on their own, whereas viruses are essentially genetic material wrapped in a protein coat that can only replicate by commandeering a host cell’s machinery. This fundamental difference shapes how we diagnose, treat, and prevent infections caused by each.<|return|>
```

---

### Example 3
**Question:** What are the symptoms and causes of diabetes?

**Response:**
```
<|channel|>analysis<|message|>Need to answer symptoms and causes.<|end|><|start|>assistant<|channel|>final<|message|>**Diabetes mellitus** is a group of metabolic disorders characterized by chronic hyperglycemia (high blood sugar). The two most common types are type 1 and type 2, but there are other less common forms (gestational, monogenic, etc.). Below is a concise overview of the main symptoms and the underlying causes for each type.

---

## 1. Symptoms of Diabetes

| Symptom | Typical Onset | Why It Happens |
|---------|---------------|----------------|
| **Polyuria** (frequent urination) | Early | High blood glucose spills into urine, pulling water with it (osmotic diuresis). |
| **Polydipsia** (excessive thirst) | Early | Loss of fluid through urine leads to dehydration, stimulating thirst. |
| **Polyphagia** (increased hunger) | Early | Cells cannot use glucose, so the body signals for more food. |
| **Weight loss** (especially in type 1) | Early | Body breaks down fat and muscle for energy when glucose can’t enter cells. |
| **Fatigue / Weakness** | Early | Energy production is impaired. |
| **Blurred vision** | Early | Hyperglycemia causes fluid shifts in the lens, altering its shape. |
| **Slow‑healing cuts or infections** | Early | High glucose impairs immune function and wound healing. |
| **Numbness or tingling in extremities** | Later | Chronic hyperglycemia damages nerves (diabetic neuropathy). |
| **Red, swollen, or painful gums** | Later | Diabetes worsens gum disease. |
| **Recurrent urinary tract or genital infections** | Later | High glucose in urine or vaginal secretions promotes bacterial growth. |
| **Night sweats, dizziness, or fainting** | Variable | Fluctuations in blood sugar or dehydration. |

> **Note:** In type 1 diabetes, symptoms often appear abruptly over days to weeks. In type 2, symptoms can develop gradually over months or years and may be subtle or absent until complications arise.

---

## 2. Causes of Diabetes

### A. Type 1 Diabetes (T1D)

| Cause | Mechanism |
|-------|-----------|
| **Autoimmune destruction of β‑cells** | The immune system mistakenly attacks insulin‑producing β‑cells in the pancreas. |
| **Genetic predisposition** | Certain HLA
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
