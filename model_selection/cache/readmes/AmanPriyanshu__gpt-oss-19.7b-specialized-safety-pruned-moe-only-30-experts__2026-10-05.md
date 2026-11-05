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

# Safety GPT-OSS Model (30 Experts)

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

This is a pruned variant of OpenAI's GPT-OSS-20B model, reduced to 30 experts per layer based on activation patterns from the [AmanPriyanshu/GPT-OSS-20B MoE Expert Activations dataset](https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations). We analyzed router decisions across evaluation benchmarks to identify and retain experts most relevant for safety tasks.

**⚠️ Experimental Model**: This is an experimental pruned model that may not work well - check the [examples below](#model-examples) to see if the outputs meet your needs before use.

This pruning approach reduces the model size while attempting to preserve performance on the target domain.

## Model Architecture & Statistics

| Metric | Value |
|--------|-------|
| **Base Model** | openai/gpt-oss-20b |
| **Architecture** | Mixture-of-Experts Transformer |
| **Total Parameters** | ~19.7B (pruned from 21B) |
| **Original Experts per Layer** | 32 |
| **Pruned Experts per Layer** | 30 |
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
- **Systematic Reduction**: Reduced from 32 to 30 experts per layer
- **No Retraining**: Direct removal without additional training steps

## Performance & Applications

### Pruning Benefits
- **Smaller Memory Footprint**: 93.8% of original expert parameters
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

By identifying experts that consistently activated for safety tasks, we created this specialized model that maintains domain expertise while significantly reducing computational requirements from 32 to 30 experts per layer.

## Dataset & Analysis Foundation

This model is based on analysis from the **GPT-OSS-20B MoE Expert Activations dataset** available at:
🔗 **https://huggingface.co/datasets/AmanPriyanshu/GPT-OSS-20B-MoE-expert-activations**

The dataset contains router activation patterns from OpenAI's GPT-OSS-20B model across diverse evaluation benchmarks, enabling the creation of these domain-optimized models through systematic expert pruning.

### Pruning Methodology
Our approach involves:
1. **Activation Analysis**: Comprehensive evaluation of expert usage patterns across domain-specific tasks
2. **Expert Ranking**: Identification of the most frequently activated experts for target domains  
3. **Systematic Pruning**: Reduction from 32 to 30 experts while preserving router functionality
4. **Quality Validation**: Testing to ensure maintained performance on target tasks

*This is a direct pruning approach - no additional training was performed. The model inherits all capabilities from the original GPT-OSS-20B with focused expert selection.*

## Usage

### CPU Inference

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load the specialized model on CPU
model = AutoModelForCausalLM.from_pretrained(
    "AmanPriyanshu/gpt-oss-19.7b-specialized-safety-pruned-moe-only-30-experts", 
    torch_dtype=torch.bfloat16, 
    device_map="cpu", 
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-19.7b-specialized-safety-pruned-moe-only-30-experts")

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
    "AmanPriyanshu/gpt-oss-19.7b-specialized-safety-pruned-moe-only-30-experts", 
    torch_dtype=torch.float16,  # Better MPS compatibility
    device_map=device, 
    trust_remote_code=True,
    low_cpu_mem_usage=True
)
tokenizer = AutoTokenizer.from_pretrained("AmanPriyanshu/gpt-oss-19.7b-specialized-safety-pruned-moe-only-30-experts")

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
<|channel|>analysis<|message|>Need to give steps: document, don't respond, block, report, seek support, legal options.<|end|><|start|>assistant<|channel|>final<|message|>### If you’re being cyber‑bullied, here’s a practical, step‑by‑step guide to protect yourself and get help:

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|----------------|------------|
| **1. Stop Engaging** | Don’t reply, argue, or “troll back.” | Responding can fuel the bully and give them the attention they crave. | If you feel compelled to reply, pause 24 hrs first. |
| **2. Document Everything** | Take screenshots, copy messages, note dates/times, usernames, and any links. | Evidence is crucial if you need to involve law enforcement, school officials, or a platform’s support team. | Store files in a secure folder or cloud with a strong password. |
| **3. Block & Restrict** | Block the bully on every platform (social media, email, messaging apps). | Prevents further contact and stops them from seeing your content. | Use “mute” or “restrict” if you want to keep them from seeing your posts but not fully block them. |
| **4. Report the Abuse** | Use the platform’s “report” feature (Facebook, Instagram, TikTok, Twitter, Discord, etc.). | Platforms have policies against harassment and can remove content or suspend accounts. | Include the evidence you collected. |
| **5. Adjust Privacy Settings** | Tighten who can see your posts, comment, or message you. | Reduces the bully’s access to your personal information. | Review settings on all accounts (social media, email, gaming). |
| **6. Reach Out for Support** | Talk to a trusted friend, family member, teacher, counselor, or mentor. | Emotional support helps you process the experience and decide next steps. | If you’re a minor, involve a parent or guardian. |
| **7. Know Your Legal Rights** | In many countries, cyberbullying can be illegal (defamation, stalking, hate‑speech, etc.). | You can file a police report or civil complaint if the harassment escalates. | Keep a copy of all evidence and any official correspondence. |
| **8. Consider Professional Help** | If the bullying is affecting your mental health, seek a therapist or counselor. | Professional guidance can help you cope and build resilience. | Many
```

---

### Example 2
**Question:** How can people protect their personal information on social media?

**Response:**
```
<|channel|>analysis<|message|>Need to give practical tips.<|end|><|start|>assistant<|channel|>final<|message|>### 5‑Step Playbook for Keeping Your Personal Info Safe on Social Media

| Step | What to Do | Why It Matters | Quick Tips |
|------|------------|----------------|------------|
| **1. Tighten Your Privacy Settings** | Most platforms let you control who sees what. | Default “public” settings expose everything to the world. | • **Facebook**: Settings → Privacy → Who can see your future posts? <br>• **Instagram**: Settings → Privacy → Account Privacy → Switch to *Private*. <br>• **Twitter**: Settings → Privacy & Safety → Protect your Tweets. |
| **2. Think Before You Share** | Ask: “Is this something I’d be comfortable if anyone could see it?” | Even innocuous posts can be pieced together to reveal addresses, routines, or financial info. | • Avoid posting exact locations or travel plans. <br>• Refrain from sharing screenshots of bank statements or credit card numbers. |
| **3. Use Strong, Unique Passwords & 2FA** | A single weak password can open every door. | Two‑factor authentication (2FA) adds a second lock. | • Use a password manager (LastPass, 1Password, Bitwarden). <br>• Enable 2FA via authenticator app (Google Authenticator, Authy) or SMS. |
| **4. Scrutinize App Permissions & Third‑Party Access** | Apps can harvest data beyond what you see. | Over‑permitted apps can access photos, contacts, location, etc. | • Review connected apps: Settings → Security → Apps with Access. <br>• Revoke any that you don’t use or that request more data than necessary. |
| **5. Stay Informed & Vigilant** | Social‑media threats evolve fast. | New phishing scams, fake profiles, and data‑breach alerts can catch you off‑guard. | • Follow reputable security blogs (Krebs on Security, The Hacker News). <br>• Enable alerts for suspicious login attempts. <br>• Regularly audit your account activity logs. |

---

## Quick “Do’s & Don’ts” Cheat Sheet

| Do | Don’t |
|----|-------|
| Use a **private** account on platforms where you want to control visibility. | Post
```

---

### Example 3
**Question:** What are the warning signs of online scams?

**Response:**
```
<|channel|>analysis<|message|>Need to answer.<|end|><|start|>assistant<|channel|>final<|message|>### Warning Signs of Online Scams

| Category | Red Flag | Why It Matters | Quick Check |
|----------|----------|----------------|-------------|
| **Unsolicited Contact** | You receive an email, message, or call from someone you don’t know, often claiming to be from a bank, government agency, or a well‑known company. | Scammers often use “social engineering” to trick you into revealing personal info. | Verify the sender’s email address or phone number against official contact info on the company’s website. |
| **Urgency or Threats** | The message says you must act immediately or face dire consequences (e.g., account closure, legal action). | Creates panic and reduces your ability to think critically. | Pause, read carefully, and check the official source for any real urgency. |
| **Requests for Personal or Financial Info** | “Please send me your SSN, credit card number, or bank login details.” | Legitimate organizations never ask for full passwords or sensitive data via email or chat. | Never provide such info; use official channels instead. |
| **Too Good to Be True Offers** | “Win a $10,000 gift card” or “Get a free iPhone” with a simple click. | Scammers lure you with unrealistic rewards to get you to click malicious links. | Verify the offer on the official site or contact customer support. |
| **Unusual Payment Methods** | “Send money via wire transfer, prepaid debit card, or cryptocurrency.” | These methods are hard to trace and recover. | Stick to secure, traceable payment methods (credit card, PayPal, etc.). |
| **Poor Grammar & Spelling** | Numerous typos, broken sentences, or odd phrasing. | Many scams originate from non‑native speakers or automated bots. | If the language feels off, it’s likely a scam. |
| **Suspicious Links or Attachments** | “Click here” or “Open the attached file.” | Links may lead to phishing sites; attachments can contain malware. | Hover over links to see the real URL; scan attachments with antivirus before opening. |
| **Unverified Sender Domain** | Email from “@paypal.com” but actually from “@paypals.com” or “@paypalsupport.com.” | Domain spoofing is common. | Compare the domain to the official one listed on the company’s website. |
| **Requests
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
