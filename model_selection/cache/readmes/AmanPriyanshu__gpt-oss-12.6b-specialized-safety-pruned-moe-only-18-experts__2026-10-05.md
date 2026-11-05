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

# Safety GPT-OSS Model (18 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 18 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~12.6B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 18 |
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
- **Systematic Reduction**: Reduced from 32 to 18 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 56.2% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 18 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 18 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-12.6b-specialized-safety-pruned-moe-only-18-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-12.6b-specialized-safety-pruned-moe-only-18-experts")

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
    "AmanPriyanshu/gpt-oss-12.6b-specialized-safety-pruned-moe-only-18-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-12.6b-specialized-safety-pruned-moe-only-18-experts")

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
Below is a practical, step‑by‑step guide that covers what to do right after you notice the bullying, how to protect yourself, and how to seek help.

---

## 1. **Take a Moment to Pause**

| **Why?** | **What to do?** |
|---|---|
| Bulbulting can trigger a strong emotional reaction. | 1. **Step back** – don’t respond immediately. 2. **Take a breath** – 4–5 deep breaths or a quick walk. 3. **Write down** what you’re feeling (anger, sadness, confusion). |

---

## 2. **Document Everything**

| **Why?** | **What to do?** |
|---|---|
| Evidence is key if you need to involve authorities or a platform. | 1. **Save screenshots** of messages, posts, or comments. 2. **Record dates and times**. 3. **Keep a log** of any threats or repeated patterns. 4. **Do not delete** anything that could be useful. |

---

## 3. **Secure Your Digital Space**

| **Why?** | **What to do?** |
|---|---|
| Protect your privacy and reduce the bully’s access. | 1. **Change passwords** on all accounts. 2. **Enable two‑factor authentication**. 3. **Adjust privacy settings** (e.g., make your profile private, limit who can comment). 4. **Delete or block** the bully’s account. 5. **Use a “safe” email address** for sensitive communications. |

---

## 4. **Respond (or Don’t) – Choose Wisely**

| **Why?** | **What to do?** |
|---|---|
| A response can either de‑escalate or fuel the situation. | 1. **If you feel safe**: a calm, factual reply can sometimes shut it down. 2. **If you feel unsafe**: do **not** engage. 3. **Use “I” statements**: “I feel hurt when…” instead of “You’re…”. 4. **Keep it short** – no need to give a long defense. 5. **If
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1. **Think Before You Post**

| **What to Avoid** | Why it matters |
|-------------------|----------------|
| **Personal details** – full address, phone number, workplace, school, or travel plans | Gives a clear “profile” for anyone to target. |
| **Frequent location tags** – posting every place you visit | Lets algorithms and strangers map your routine. |
| **Sensitive photos** – pictures of family, pets, or personal spaces | Can be used for identity theft or stalking. |
| **Political or religious views** | May attract unwanted attention or harassment. |

> **Rule:** If you’re not comfortable with a friend, family member, or even a stranger seeing that piece of information, don’t post it.

---

### 2. **Use Strong, Unique Passwords**

| Feature | How to implement |
|---------|----------------|
| **Length** – 12+ characters | Mix letters, numbers, symbols |
| **Uniqueness** – separate passwords for each platform | Avoid “password reuse.” |
| **Password manager** – tools like LastPass, Authy, or a simple spreadsheet | Store them securely, not in a sticky note. |

> **Tip:** Enable two‑factor authentication (2FA) on every account that offers it. It adds a second layer of verification.

---

### 3. **Enable Privacy Settings**

| Setting | What it does |
|---------|----------------|
| **Profile visibility** – “Friends only” or “Private” | Limits who can see your posts. |
| **Location sharing** – “Hide location” or “Share only with selected people” | Keeps your whereabouts private. |
| **Tagging** – “Tag only friends” | Prevents strangers from tagging you in posts. |
| **Blocked users** – “Block” or “Mute” | Stops unwanted interactions. |

> **Action:** Review each platform’s privacy settings quarterly; they can change without notice.

---

### 4. **Use “Safe” or “Private” Posting Options**

- **Private groups** – Only invited members can see content.  
- **Stories/Live** – Set “Only for followers” or “Only for friends.”  
- **Delete or archive** – Remove old posts that may no longer be relevant.

---

### 5. **Limit “Public” Sharing**

| Platform | Public‑by‑default content |
|----------|----------------|
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Sc scams

| Category | Red Flag | Why It Matters | What to Do |
|----------|----------|----------------|----------------|
| **Unsolvable “Too‑Good‑to‑Be‑True” Offers** | Extremely high returns with little or no risk | Legitimate investments always carry some risk. | Verify the investment through reputable sources (SEC, FINSEC, etc.). |
| **Urgity & Pressure** | “Act now or lose your chance!” | Scers create a false sense of urgency to bypass rational thinking. | Take a break, research, and never sign anything under pressure. |
| **Unprofessional Communication** | Ty‑errors, broken English, or overly formal language | Real professionals use proper grammar and tone. | Flag it as a potential scam. |
| **Requests for Personal/Financial Info** | “Send me your SSN, bank details, or credit card” | Legit companies never ask for such data via email or chat. | Never share sensitive data unless verified. |
| **Unverified Payment Methods** | “Pay via wire transfer, gift cards, or cryptocurrency” | These are hard to trace and recover. | Stick to traceable, secure payment methods (bank transfer, credit card, PayPal). |
| **No Physical Address or Phone Number** | “We’re a virtual company” | Real businesses provide a verifiable address and phone line. | Verify the address via a phone call or a quick Google search. |
| **Too Many “Testimonials”** | “Everyone says this is the best!” | Fake reviews are often fabricated or paid. | Look for independent reviews on third‑party sites. |
| **No Clear Terms & Conditions** | “Terms are available on request” | Legit sites have publicly available T&C. | Ask for a copy and read it carefully. |
| **Unusual or Complex Fees** | “Processing fee, admin fee, etc.” | Legit fees are transparent and reasonable. | Ask for a breakdown and compare with industry standards. |
| **No Real Contact Person** | “You’ll be speaking with a representative” but no name or ID | Real reps have a name, photo, and contact details. | Request a real name and verify it. |
| **Unusual Email/Website Domain** | “.com.biz”, “.info”, or a domain that doesn’t match the company name | Many scammers use generic domains. | Check
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
