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

# Safety GPT-OSS Model (21 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 21 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~14.3B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 21 |
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
- **Systematic Reduction**: Reduced from 32 to 21 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 65.6% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 21 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 21 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-14.3b-specialized-safety-pruned-moe-only-21-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-14.3b-specialized-safety-pruned-moe-only-21-experts")

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
    "AmanPriyanshu/gpt-oss-14.3b-specialized-safety-pruned-moe-only-21-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-14.3b-specialized-safety-pruned-moe-only-21-experts")

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

## 1. Stay Calm & Don’t Respond Immediately  
- **Pause** – Give yourself a few minutes (or hours) before replying.  
- **Avoid retaliation** – Responding with anger or insults often escalates the situation.  
- **Don’t share personal info** – If the bully is asking for details, refuse and block them.

---

## 2. Document Everything  
| What to record | Why it matters |
|-----------------|-----------------|
| Screenshots or copies of messages, posts, or comments | Evidence for reporting or legal action |
| Dates & times | Shows pattern & severity |
| Any threats of violence or self‑harm | May trigger mandatory reporting |
| The bully’s username, profile, or IP (if available) | Helps platforms identify the offender |

*Tip:* Use a secure, private folder or a cloud service you trust. Keep the original files; screenshots can be altered.

---

## 3. Block / Filter the Bully  
- **Block or mute** the user on every platform they’re using.  
- **Adjust privacy settings**:  
  - Make your profile private.  
  - Restrict who can comment or message you.  
  - Use “safe mode” or “restricted mode” if available.  
- **Use “ignore” or “report” features**: Most platforms let you ignore a user or report them for harassment.

---

## 4. Report to the Platform  
| Platform | Typical reporting process |
|-----------|---------------------------|
| Facebook / Instagram | “Harassment” → “Report a problem” |
| Twitter | “Report a tweet” → “Harassment” |
| TikTok / YouTube | “Report a video” → “Harassment” |
| Discord / Twitch | “Report a user” → “Harassment” |
| School or workplace portal | Contact the IT or HR department |

- **Provide the documentation** you collected.  
- **Follow up** if you don’t see a response within a week.

---

## 5. Reach Out for Support  
- **Friends & Family** – Let someone you trust know what’s happening.  
- **School / Workplace**
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give tips.<|end|><|start|>assistant<|channel|>final<|message|>### 1. **Think Before You Post**

| **What to Avoid** | **Why It Matters** | **Practical Tip** |
|-------------------|-------------------|-------------------|
| Exact birthdate, address, or phone number | Makes it easy for someone to locate you or create a fake profile. | Use a “birthday month” or “year only.” |
| Current location or travel plans | Enables “check‑in” stalking or planning a break‑in. | Disable location sharing or use a generic “city” tag. |
| Detailed work or school info | Gives recruiters or scammers a target. | Share only the job title, not the company name or department. |
| Personal photos with recognizable landmarks | Can be used to triangulate your home or routine. | Use blurred or generic backgrounds. |

---

### 2. **Use Strong, Unique Passwords & Two‑Factor Authentication (2FA)**

| **Step** | **How to Do It** |
|---------|-----------------|
| Create a password that’s at least 12 characters, mixes letters, numbers, and symbols. | Use a password manager (e.g., **LastPass**, **MFA**, **Bitwarden**) to generate and store them. |
| Enable 2FA on every account. | Prefer a hardware token (e.g., **YubiKey**) or a phone app (e.g., **Authenticator**, **Signal**). |
| Change passwords if you see a security alert. | Set a reminder every 6–12 months. |

---

### 3. **Limit Profile Visibility**

| **Feature** | **Recommended Setting** | **Why** |
|--------------|------------------------|--------|
| Public vs. Private | Keep most accounts private. | Reduces the amount of data visible to strangers. |
| Friend/Follow Lists | Use “Close Friends” or “Only Me” for sensitive posts. | Controls who sees what. |
| “People You May Know” | Turn off or limit to a small circle. | Prevents strangers from connecting to you. |

---

### 4. **Control What Others Can Do With Your Data**

| **Tool** | **Action** |
|----------|------------|
| **Google Search** | Search your name to see what’s publicly available. |
| **Google My Data** | Request a copy of data Google holds about you. |
| **Social Media “Right to be Forgotten
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red Flag | Why It Matters | What to Do |
|----------|----------|----------------|------------|
| **Unsolicited Contact** | You receive a message or email from a person or company you never heard of. | Scammers often start with a “friendly” outreach to build trust. | Verify the sender’s identity through an independent channel (phone, official website, etc.). |
| **Urgency or Pressure** | “Act now!” or “You’ll lose this offer in 5 minutes.” | Creates a false sense of urgency to bypass rational thinking. | Take a pause. Check the claim independently before responding. |
| **Too‑Good‑to‑Be‑True Offers** | “Free trip to Paris” or “$10,000 cash prize” with no effort required. | Legitimate offers usually require some work or have clear terms. | Research the offer online; look for reviews or complaints. |
| **Requests for Personal Info** | “Please send your SSN, bank account, or credit card details.” | Personal data is a goldmine for identity theft. | Never share sensitive data unless you’re sure the request is legitimate. |
| **Payment via Unusual Methods** | “Send money via wire transfer, cryptocurrency, or gift cards.” | These methods are hard to trace and recover. | Use secure, traceable payment methods (credit card, PayPal, etc.). |
| **Poor Grammar & Spelling** | Numerous typos, broken sentences, or odd phrasing. | Many scams are produced by non‑native speakers or automated bots. | Treat such messages with skepticism; legitimate companies usually proof‑read. |
| **No Contact Information** | No phone number, physical address, or official website. | Legitimate businesses provide multiple ways to verify them. | Search online for the company’s address or call the listed number. |
| **Unprofessional or Generic Email Addresses** | “info@company.com” or “support@123456.com” with no domain name. | Real companies use branded domains. | Verify the domain by searching the company’s name. |
| **Requests for “Confidential” or “Secret” Info** | “We’re a private company; we can’t share details publicly.” | Legitimate entities are usually transparent about basic info. | Ask for verifiable credentials or references. |
| **Too Many “Friends” or “
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
