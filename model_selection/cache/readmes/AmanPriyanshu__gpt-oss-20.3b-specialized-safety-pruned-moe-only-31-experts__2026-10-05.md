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

# Safety GPT-OSS Model (31 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 31 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~20.3B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 31 |
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
- **Systematic Reduction**: Reduced from 32 to 31 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 96.9% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 31 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 31 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-20.3b-specialized-safety-pruned-moe-only-31-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-20.3b-specialized-safety-pruned-moe-only-31-experts")

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
    "AmanPriyanshu/gpt-oss-20.3b-specialized-safety-pruned-moe-only-31-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-20.3b-specialized-safety-pruned-moe-only-31-experts")

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
<|channel|>analysis<|message|>Need to give steps: document, don't respond, block, report, seek support, legal options.<|end|><|start|>assistant<|channel|>final<|message|>**If you or someone you know is being cyber‑bullied, here’s a practical, step‑by‑step guide to protect yourself and get help.**  

---

## 1. Stay Calm & Don’t Respond

| Why it matters | What to do |
|-----------------|------------|
| Responding can fuel the bully and give them the “attention” they’re after. | **Pause**. Take a deep breath, step away from the screen, and give yourself a few minutes before you react. |
| The bully may try to provoke you into a heated reply that could be used against you later. | **Avoid replying** to harassing messages or comments. If you must respond (e.g., to clarify a misunderstanding), keep it short, factual, and non‑emotional. |

---

## 2. Document Everything

| Why it matters | What to do |
|-----------------|------------|
| Evidence is crucial if you need to involve authorities, schools, or employers. | **Save screenshots, copy URLs, and record dates/times** of every harassing post, message, or email. |
| Keep a separate, secure folder or cloud storage (password‑protected) for this evidence. | Use a dedicated device or account that you don’t use for everyday browsing to avoid accidental exposure. |

---

## 3. Block & Restrict the Bully

| Platform | How to block |
|----------|--------------|
| **Social media (Facebook, Instagram, TikTok, etc.)** | Go to the user’s profile → “Block” or “Report” → follow prompts. |
| **Messaging apps (WhatsApp, Telegram, Signal, etc.)** | Open chat → “Info” → “Block contact.” |
| **Email** | Mark as spam or block the sender’s address. |
| **Gaming platforms** | Use the in‑game “Block” or “Mute” feature. |

*Tip:* After blocking, consider adjusting your privacy settings so that only friends or approved contacts can see your posts.

---

## 4. Report the Abuse

| Platform | How to report |
|----------|--------------|
| **Social media** | Use the “Report” button on the post or profile. Provide the evidence you collected. |
| **Messaging apps** | Report the user or the specific message thread. |
| **Online forums / communities
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 5‑Step Guide to Safeguarding Your Personal Info on Social Media

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|----------------|------------|
| **1. Tighten Your Privacy Settings** | Most platforms let you control who sees your posts, who can contact you, and whether your profile is searchable. | Default settings are often “public” or “friends only.” | • Go to *Settings → Privacy*.<br>• Set “Who can see my posts?” to *Friends* or *Only me*.<br>• Turn off “Allow search engines to link to your profile.” |
| **2. Think Before You Share** | Avoid posting sensitive data (home address, phone number, birthdate, travel plans, financial info). | Even a single post can be scraped or shared by others. | • Use a “private” or “draft” mode for posts you’re unsure about.<br>• Review the audience before hitting *Share*. |
| **3. Use Strong, Unique Passwords & 2FA** | A strong password plus two‑factor authentication (2FA) makes it hard for attackers to access your account. | Password reuse or weak passwords are the biggest vulnerability. | • Use a password manager (LastPass, 1Password, Bitwarden).<br>• Enable 2FA via authenticator app (Google Authenticator, Authy) or SMS. |
| **4. Monitor Your Digital Footprint** | Regularly search your name, email, and phone number to see what’s publicly available. | You may not realize how much data is out there. | • Google “Your Name + City”.<br>• Use tools like *Have I Been Pwned* to check if your email was in a breach. |
| **5. Be Wary of Third‑Party Apps & Links** | Many apps request access to your profile or data. Phishing links can steal credentials. | Third‑party apps can harvest data or redirect you to fake login pages. | • Only authorize apps you trust and that are necessary.<br>• Hover over links to see the real URL before clicking.<br>• Use a browser extension that warns about phishing sites. |

---

## Quick “Do’s & Don’ts” Checklist

| Do | Don’t |
|----|-------|
| Use a unique password for each platform. | Post
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| # | Warning Sign | Why It Matters | What to Do |
|---|--------------|----------------|------------|
| 1 | **Unsolicited Contact** | Scammers often reach out via email, social media, or messaging apps with no prior relationship. | Verify the sender’s identity through a separate channel (phone, official website, or known contact). |
| 2 | **Urgency or Pressure** | “Act now!” or “You’ll lose this opportunity if you don’t respond immediately” is a classic tactic to bypass rational thinking. | Take a step back. Legitimate offers rarely require instant decisions. |
| 3 | **Too Good to Be True** | Extremely high returns, free gifts, or “guaranteed” outcomes are red flags. | Research the claim. Check independent reviews, forums, or regulatory bodies. |
| 4 | **Requests for Personal or Financial Info** | Legitimate companies never ask for passwords, PINs, or full bank statements via email or chat. | Never share sensitive data. Use secure, official channels only. |
| 5 | **Unprofessional Communication** | Typos, broken grammar, or generic greetings (“Dear Customer”) suggest a mass‑sent scam. | Look for consistent branding, correct spelling, and personalized details. |
| 6 | **Unusual Payment Methods** | Requests for wire transfers, prepaid debit cards, or cryptocurrency are common scam tactics. | Stick to reputable payment methods (credit cards, PayPal, or bank transfers with traceability). |
| 7 | **No Physical Address or Contact Info** | Legitimate businesses provide a verifiable address, phone number, and customer support. | Verify the address via Google Maps or a phone lookup. |
| 8 | **Suspicious URLs** | Shortened links, misspelled domains, or unfamiliar top‑level domains (e.g., .xyz, .info) can hide phishing sites. | Hover over links to see the real URL, or type the address manually into a browser. |
| 9 | **Requests for “Confidential” or “Secret” Information** | Scammers claim the information is sensitive to create a sense of exclusivity. | Legitimate requests are transparent and explain why the data is needed. |
| 10 | **Inconsistent or Contradictory Details** | Dates, names, or product specs that don’t match up.
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
