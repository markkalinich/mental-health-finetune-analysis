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

# Safety GPT-OSS Model (15 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 15 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

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
| **Specialization** | Safety |

## Pruning Methodology

### What is Expert Pruning?
Mixture-of-Experts models contain multiple specialized sub-networks (experts) per layer. During inference, only a subset of experts are activated for each token. Expert pruning involves:

1. **Analyzing Usage Patterns**: Tracking which experts activate most frequently for specific tasks
2. **Removing Underutilized Experts**: Discarding experts with low activation rates for the target domain
3. **Preserving Router Functionality**: Maintaining the routing mechanism with fewer available experts

### Our Approach
- **Data-Driven Selection**: Used activation patterns from safety evaluation tasks
- **Systematic Reduction**: Reduced from 32 to 15 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 46.9% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 15 experts per layer.

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
    "AmanPriyanshu/gpt-oss-10.8b-specialized-safety-pruned-moe-only-15-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-10.8b-specialized-safety-pruned-moe-only-15-experts")

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
    "AmanPriyanshu/gpt-oss-10.8b-specialized-safety-pruned-moe-only-15-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-10.8b-specialized-safety-pruned-moe-only-15-experts")

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
<|channel|>analysis<|message|>Need advice.<|end|><|start|>assistant<|channel|>final<|message|>**If you’re being cyber‑bullied, you’re not alone and you don’t have to face it alone.**  
Below is a practical, step‑by‑step guide that covers what to do right away, how to protect yourself, and how to seek help.

---

## 1. **Stop the Interaction (Immediately)**  

| Action | Why it matters | How to do it |
|--------|----------------|--------------|
| **Delete or block the bully** | Removes the source of harassment | Use the “Block” or “Remove” feature on the platform. |
| **Turn off notifications** | Prevents the bully from seeing your posts | Disable notifications for the account or app. |
| **Do not respond** | Avoides escalation | Let the bully know you’re not engaging. |

> *If the bully is a friend or family member, consider a “mute” option instead of a full block until you’re sure you’re safe.*

---

## 2. **Document Everything**  

| What to record | Why it matters | How to keep it |
|----------------|----------------|--------------|
| **Messages, screenshots, URLs** | Evidence for reporting or legal action | Save in a cloud folder (Google Drive, Dropbox) or a dedicated “bulry‑log” app. |
| **Date & time of each incident** | Shows pattern & severity | Note the timestamp or use the platform’s built‑in “Save” feature. |
| **Any replies or threats** | Shows intent & escalation | Keep a copy in a separate folder. |

> *Keep the original files; never alter them.*

---

## 3. **Report to the Platform**  

| Platform | Typical reporting process | Key points to include |
|-----------|----------------|----------------|
| **Facebook / Instagram** | “Block” + “Report” | Name, username, evidence, description of harassment. |
| **Twitter** | “Block” + “Report” | Same as above. |
| **WhatsApp** | “Block” + “Report” | Include screenshots. |
| **School/Work** | Contact IT or HR | Provide evidence, explain impact. |

> *Most platforms have a “Harcy / Hate” or “Abharcy” category. Use it.*

---

## 4. **Protect Your Digital Identity**  

| Step | Why it matters | How to do it |
|------|----------------|--------------|
| **Change passwords
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1. **Think Before You Post**

| **What to Avoid** | Why it matters |
|-------------------|----------------|
| Full names, birth dates, or exact addresses | Makes it easy to locate you |
| Photos of you in public places with clear faces | Can be used for facial‑recognition |
| Current travel plans or vacation details | Gives clues to your routine |
| Sensitive work details (project names, client info) | Can be exploited by competitors or scammers |

**Tip:** Use a “profile‑only” photo (e‑pencil, avatar, or blurred image) and keep location tags off or set to “Nearby” only.

---

### 2. **Control Your Privacy Settings**

| Platform | Recommended Settings |
|-----------|---------------------|
| **Facebook** | `Friends` only, disable “Location” and “Show me” |
| **Instagram** | `Followers` only, use “Private” for stories, disable location |
| **Twitter** | `Followers` only, disable “Location” |
| **LinkedIn** | Keep “Public” to a minimum, use “Connections” only |

- **Use “Incognito” or “Private” modes** when posting sensitive content.
- **Regularly audit** your friend/follower lists; remove people you no longer trust.

---

### 3. **Use Strong, Unique Passwords**

- **Password manager** (e.g., LastPass, PPG) to store and rotate passwords.
- **Two‑factor authentication** (TFA) on all accounts that support it.
- **Avoid “social‑media‑style” passwords** (e.g., “facebook123”).

---

### 4. **Enable “Location” Controls**

- **Turn off “Location”** on all accounts or set it to “Nearby” only.
- **Use “Location” only** for emergency contacts or close friends.

---

### 5. **Limit “Tagging” and “Mention” Features**

- **Disable “Tagging”** for strangers or public accounts.
- **Use “Mention”** sparfully; avoid tagging people in posts that contain sensitive info.

---

### 6. **Use “Safe Mode” or “Private” Browsing**

- **Private browsing** hides your search history from the platform.
- **Safe mode** on some apps (e.g., Instagram) prevents the platform from showing your profile to strangers.

---

###
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to list warning signs.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Sc scams

| # | Red Flag | Why it matters | How to spot it |
|---|-----------|----------------|----------------|
| 1 | **Too‑too‑good‑offers** | “Earn $10,000 in 30 days” or “free vacation” with no effort | Legitimate offers have realistic ROI and clear steps |
| 2 | **Urgity & pressure** | “Act now or you’ll lose this chance” | Scers use time‑pressure to bypass your rational mind |
| 3 | **Unverified “source”** | “I’m a friend of X” or “I’m a government rep” with no ID | Verify the identity via official channels or independent sources |
| 4 | **Requests for personal data** | “Send me your SSN, bank number, or address” | Legit sites never ask for full personal data upfront |
| 5 | **Payment before service** | “Pay $100 now, we’ll ship the product” | Real businesses ship after payment, but never ask for “proof” |
| 6 | **Too many “free” services** | “Free trial, no credit card needed” | Free trials usually require a credit card or a minimal deposit |
| 7 | **Unprofessional language** | Ty‑errors, broken grammar, or “Dear Sir/Mma” | Legit sites use professional copy‑editing |
| 8 | **Too many “guarantees”** | “100% guaranteed, no risk” | No legitimate investment can guarantee 100% returns |
| 9 | **Unusual payment methods** | “Pay via wire transfer, crypto, or gift‑cards” | These are hard to trace and recover |
| 10 | **No verable contact info** | No phone number, no physical address, only a generic email | Legit companies provide multiple ways to reach them |
| 11 | **Too many “social proof”** | “Thousands of customers, 5‑star rating” | Check independent reviews, not just the site’s own |
| 12 | **Requests for “quick” money** | “Earn $500 in a week” | Legit jobs take time, training, and skill |
| 13 | **Hidden fees** | “You’ll pay $50 for shipping” | Legit sites list all fees upfront |
| 14 | **Unclear terms** | “
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
