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
  - safety
  - specialized
  - efficient
  - transformer
  - causal-lm
  - text-generation
  - pytorch
  - pruned-model
  - domain-specific
---

# Safety GPT-OSS Model (10 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 10 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~7.8B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 10 |
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
| **Specialization** | Safety |

## Pruning Methodology

### What is Expert Pruning?
Mixture-of-Experts models contain multiple specialized sub-networks (experts) per layer. During inference, only a subset of experts are activated for each token. Expert pruning involves:

1. **Analyzing Usage Patterns**: Tracking which experts activate most frequently for specific tasks
2. **Removing Underutilized Experts**: Discarding experts with low activation rates for the target domain
3. **Preserving Router Functionality**: Maintaining the routing mechanism with fewer available experts

### Our Approach
- **Data-Driven Selection**: Used activation patterns from safety evaluation tasks
- **Systematic Reduction**: Reduced from 32 to 10 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 31.2% of original expert parameters
- **Reduced Computational Load**: Fewer routing decisions during inference
- **Focused Capabilities**: Retains experts relevant to safety tasks

### Use Cases
- **Speculative Decoding**: Draft model for full GPT-OSS-20B
- **Resource-Constrained Deployment**: Edge devices, mobile applications
- **Research**: Study expert specialization in MoE models
- **Fine-tuning**: Smaller base model for domain adaptation

*Note: Performance may vary depending on how well the pruned experts match your specific use case.*

## Motivation & Expert Selection

This safety-focused model uses experts that performed well on safety evaluation tasks from SORRY-Bench. These experts are specialized in identifying and appropriately responding to potentially harmful content while maintaining helpful capabilities.

The expert selection process utilized our comprehensive analysis of router activation patterns across multiple evaluation benchmarks:

- **GPQA**: Graduate-level questions in physics, chemistry, biology (Diamond & Expert subsets)
- **MMLU/MMLU-Pro**: Comprehensive knowledge across 57+ subjects including science, medicine, law
- **SORRY-Bench**: Safety evaluation across harmful content categories  
- **Tulu3**: Persona-driven instruction following with verifiable constraints
- **Polyglot-or-Not**: Multilingual factual completion tasks

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 10 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 10 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-7.8b-specialized-safety-pruned-moe-only-10-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-7.8b-specialized-safety-pruned-moe-only-10-experts")

# Generate with the model
messages = [
    {"role": "user", "content": "What should someone do if they encounter cyberbullying online?"}
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
    "AmanPriyanshu/gpt-oss-7.8b-specialized-safety-pruned-moe-only-10-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-7.8b-specialized-safety-pruned-moe-only-10-experts")

# Generate with the model
messages = [
    {"role": "user", "content": "What should someone do if they encounter cyberbullying online?"}
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

The following examples demonstrate the model's performance on safety tasks:

### Example 1
**Question:** What should someone do if they encounter cyberbullying online?

**Response:**
```
<|channel|>analysis<|message|>Need advice.<|end|><|start|>assistant<|channel|>final<|message|>**If you’re being cyber‑bullied, act quickly and protect yourself.  Here’s a step‑by‑step guide you can follow:

---

## 1. **Take a Moment‑Pause**

| **Why?** | Cyber‑bulbuling can feel overwhelming, but a pause lets you decide how to respond. |  
| **What to do?** |  •  Stop scrolling or interacting with the bully’s content. |  •  Take a short break (walk, breathe, or text a friend). |  

---

## 2. **Document the Evidence**

| **Why?** | You’ll need proof if you decide to report or block the bully. |  
| **What to do?** |  •  Save screenshots, messages, or links. |  •  Keep them in a separate folder (e.g., a cloud drive or a secure app). |  

---

## 3. **Block or Unfollow the Bulizer**

| **Why?** | Removes the immediate source of harassment. |  
| **What to do?** |  •  Use the platform’s “Block” or “Mute” feature. |  •  If you’re on a forum, use “Report” or “Delete” options. |  

---

## 4. **Report the Content (If it’s a violation)**

| **Why?** | Platforms have policies against harassment. |  
| **What to do?** |  •  Find the “Report” button (often labelled “Har‑Har” or “Har‑Har”). |  •  Provide the evidence you saved. |  •  Some platforms let you choose “Private” or “Public” reporting. |  

---

## 5. **Reach Out to Trusted People**

| **Why?** | Emotional support and practical advice. |  
| **What to do?** |  •  Tell a friend, family member, or a teacher. |  •  If you’re a student, contact a school counselor or a school’s cyber‑bulbuling policy. |  

---

## 6. **Use the Platform’s Support Resources**

| **Why?** | Many platforms have hel‑hel lines, chat‑support, or self‑care guides. |  
| **What to do?** |  •  Search for “Help” or “Support” pages. |  •  Some platforms offer a “Self‑
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give tips.<|end|><|start|>assistant<|channel|>final<|message|>**Protecting your personal information on social media is a layered strategy that combines technical settings, smart behavior, and ongoing vigilance. Below is a practical “checheck” guide you can follow, whether you’re a casual user or a professional who needs to keep sensitive data out of prun‑s.  

---

## 1.  Know What You’re Exifying

| **What is “personal information?”**  
| • Full name, address, phone number, ID, or any data that can identify you.  
| • Photos of your home, pets, or your daily routine.  
| • Work details, salary, or upcoming travel.  
| • Anything that could be used for identity‑theft or stalking.  

| **Why it matters**  
| • Once it’s online, it can be copied, shared, or used for fraud.  
| • Even “anonymous” posts can be cross‑matched with other data.  

---

##  2.  Technical Settings

| **Profile Privacy**  
| • **Set “Friends only”** on your profile.  
| • Turn **“Location”** to “Off” (or “Hide” for specific posts).  
| • Use **“Private”** for photos and videos.  

| **Password & Authentication**  
| • Use a unique, strong password (e.g., 12‑digits, no repeats).  
| • Enable **Two‑Factor Authentication** (phone + key‑card).  

| **Data‑Deletion**  
| • Delete or “Archive” old posts that you no longer want public.  
| • Use the **“Delete”** option for posts that contain sensitive data.  

| **Use “Incognito” or “Private” mode** for browsing.  

| **Disable “Location Services”** (e.g., Apple’s “Find‑Me” feature).  

| **Enable “Block”** for strangers.  

| **Use “Custom Filters”** to hide certain content from public feed.  

| **Enable “Data‑Encryption”** on your device (e.g., Apple’s “Data‑Encryption” feature).  

| **Use “Secure Browsing”** on your device.  

| **Use “App‑Security”** to block suspicious apps.  

| **Use “App‑Security”** to block suspicious apps.  

| **Use “App‑Security”** to block suspicious apps.  

|
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer: warning signs of online scams. Provide list.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Sc Sc Sc

| 1 | **Too Good to Be True**  
- Offers huge rewards, “free” or “instant” money.  
- Claims you’ll get a “one‑step” investment or “gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑gu‑
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
